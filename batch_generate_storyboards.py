#!/usr/bin/env python3
"""
Batch-generate storyboard prompts from DOCX episode scripts with chat-completion APIs.

Workflow:
1. Read the shared system prompt from a local .txt file.
2. Extract plain text from each episode .docx file.
3. Send one stateless chat-completion request per episode to the selected provider.
4. Save each response as a UTF-8 text file under ./outputs.

The script uses only Python's standard library so it can run in a minimal setup.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import http.client
import json
import os
import re
import ssl
import sys
import textwrap
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


DOCX_XML_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
DEFAULT_PROMPT_GLOB = "*prompt*.txt"
DEFAULT_SCRIPT_GLOB = "*.docx"
DEFAULT_THINKING_ENABLED = True
DEFAULT_REVIEW_THINKING_ENABLED = False
DEEPSEEK_REASONING_EFFORT_OPTIONS = ["high", "max"]
DEFAULT_GENERATION_REASONING_EFFORT = "high"
DEFAULT_REVIEW_REASONING_EFFORT = "high"
DEFAULT_PARALLELISM = 3
DEFAULT_EPISODES_PER_REQUEST = 2
MAX_EPISODES_PER_REQUEST = 3
DEFAULT_SPLIT_DIR_NAME = "split_scripts"
DEFAULT_AGENT_REVIEW_ENABLED = False
DEFAULT_AGENT_REVIEW_ROUNDS = 2
DEFAULT_REVIEW_SKILL_FILENAME = "storyboard_review_skill.txt"
DEFAULT_STABLE_SEGMENT_MODE = False
DEFAULT_SEGMENT_TARGET_CHARS = 3200
SUPPORTED_SCRIPT_SUFFIXES = {".docx", ".txt"}
PROVIDER_DEEPSEEK = "deepseek"
PROVIDER_QWEN_CHAT = "qwen-chat"
PROVIDER_BLTCY_CHAT = "bltcy-chat"
DEFAULT_PROVIDER = PROVIDER_DEEPSEEK
EPISODE_HEADING_RE = re.compile(
    r"^\s*第\s*([0-9一二三四五六七八九十百零〇两]+)\s*集(?:\s*[:：\-—].*|\s*[（(【\[].*[）)】\]])?\s*$"
)
EPISODE_NUMBER_RE = re.compile(r"第\s*([0-9一二三四五六七八九十百零〇两]+)\s*集")
EPISODE_END_RE = re.compile(
    r"(?:本\s*集\s*完|第\s*[0-9一二三四五六七八九十百零〇两]+\s*集\s*完)"
)
SCENE_ONE_RE = re.compile(r"^\s*(?:\*\*)?\s*【?\s*场景\s*1\s*】?")
SERIES_TITLE_RE = re.compile(r"《[^》]+》")
PROVIDER_CONFIGS = {
    PROVIDER_DEEPSEEK: {
        "display_name": "DeepSeek",
        "api_base": "https://api.deepseek.com",
        "model": "deepseek-v4-flash",
        "default_max_tokens": 32768,
        "api_key_env": "DEEPSEEK_API_KEY",
        "api_base_env": "DEEPSEEK_BASE_URL",
        "model_env": "DEEPSEEK_MODEL",
        "api_key_label": "DeepSeek Key",
        "model_options": [
            "deepseek-v4-flash",
            "deepseek-v4-pro",
            "deepseek-chat",
            "deepseek-reasoner",
        ],
        "supports_thinking": True,
        "supports_reasoning_effort": True,
        "reasoning_effort_options": DEEPSEEK_REASONING_EFFORT_OPTIONS,
        "endpoint": "/chat/completions",
    },
    PROVIDER_QWEN_CHAT: {
        "display_name": "Qwen Chat",
        "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen3.6-plus",
        "default_max_tokens": 65536,
        "api_key_env": "DASHSCOPE_API_KEY",
        "api_base_env": "DASHSCOPE_BASE_URL",
        "model_env": "DASHSCOPE_MODEL",
        "api_key_label": "DashScope Key",
        "model_options": ["qwen3.6-plus"],
        "supports_thinking": True,
        "supports_reasoning_effort": False,
        "reasoning_effort_options": [],
        "endpoint": "/chat/completions",
    },
    PROVIDER_BLTCY_CHAT: {
        "display_name": "BLTCY Chat",
        "api_base": "https://api.bltcy.ai/v1/chat/completions",
        "model": "gpt-5.4",
        "default_max_tokens": 12000,
        "api_key_env": "BLTCY_API_KEY",
        "api_base_env": "BLTCY_BASE_URL",
        "model_env": "BLTCY_MODEL",
        "api_key_label": "BLTCY Key",
        "model_options": ["gpt-5.4", "gemini-3.1-pro-preview"],
        "supports_thinking": False,
        "supports_reasoning_effort": False,
        "reasoning_effort_options": [],
        "endpoint": "/chat/completions",
    },
}
SYSTEM_PROMPT_HINT = (
    "下面是完整剧本。请严格遵守系统提示词中的全部规则，"
    "直接输出最终分镜提示词，不要解释，不要省略。"
)
REVISION_HINT = (
    "下面先给出上一版审核意见，再给出完整剧本。"
    "请逐条修正问题后，重新输出完整最终分镜提示词。"
    "不要输出解释，不要输出审核结论。"
)
OUTPUT_PROTOCOL_CONTRACT = textwrap.dedent(
    """
    【最终输出格式强制检查】
    最终答案必须使用自然分镜格式，禁止输出任何三尖括号 GROUP/SHOT 机器标签。
    每一组必须使用自然组标题，例如：=== 第1组：组名（总时长：12秒，镜头数：3个） ===
    每一个镜头必须用自然编号单独成行，例如：1-1、1-2、2-1。
    每个镜头必须写明景别、画面/调度、台词或心声，并包含“（本镜估算时长：X秒）”。
    组总时长应等于本组所有镜头估算时长相加；每组 10-15 秒；禁止 1 秒或更短镜头。
    不要输出机器标签、解释、目录、前言、总结或额外说明。
    """
).strip()
DEEPSEEK_NO_INNER_OS_MARKER = (
    "\n\n〖思维模式要求〗在你的思考过程（标签内）中，请遵守以下规则：\n"
    "1. 禁止使用圆括号包裹内心独白，例如“（心想：……）”或“(内心OS：……)” ，所有分析内容直接陈述即可\n"
    "2. 禁止以角色第一人称描写内心活动，例如“我心想”“我觉得”“我暗自”等，请用分析性语言替代\n"
    "3. 思考内容应聚焦于剧情走向分析和回复内容规划，不要在思考中进行角色扮演式的内心戏表演"
)
DEFAULT_REVIEW_SKILL_TEXT = textwrap.dedent(
    """
    你是“竖屏古装分镜审核 skill”，只负责严格审稿，不负责润色，不负责帮用户改稿。

    审核目标：
    1. 严格依据“原剧本”和“当前分镜稿”做审核，禁止脑补导演风格或额外剧情。
    2. 只检查硬规则是否满足，不要输出审美偏好。
    3. 每个问题都必须指出具体组别、具体证据、具体修改建议。
    4. 如果没有硬性问题，必须返回 pass=true，issues=[]；软问题只能放入 warnings，不能让 pass=false。
    5. 只拦截真正会导致成片失真或结构混乱的硬错误；不要因为可微调的小误差直接判整集失败。

    必查规则：
    - 严格自检集要点
    - 输出格式边界：禁止出现三尖括号 GROUP/SHOT 机器标签；每组必须使用 `=== 第X组：...（总时长：XX秒，镜头数：X个） ===`；每镜必须使用 `X-Y` 自然编号，并写明 `（本镜估算时长：X秒）`
    - 组首空间锁定：每组独立、完整，不允许“同上”等简写，必须明确列出所有在场人物及位置
    - 对话指向：每句真人开口对话都要写明“谁对谁说”，视线指向对方眼睛；人物对话镜头切换是否合理；对话估算时长是否合理
    - 心声/内心独白/画外音：允许写“关联/指向某人”，不等同真人开口对话；不得仅因心声没有与对方眼神对视、或心声被合理拆分成短句，就判为硬错误。只有心声导致剧情信息缺失、对象明显错乱或新增删改剧情时，才可判硬错误。
    - 时长计算：普通语速按有效台词字数÷4 作为舒适参考；审核可接受上限为有效台词字数÷7，只要台词语速不超过 7 字/秒，不得仅因台词时长判为硬错误。6-7 字/秒属于偏快但可接受，必须放入 warnings 并写明“有效字数 / 镜头秒数 / 字秒比”。
    - 组总时长：每组必须在 10-15 秒，只能微压缩，可以合理拆分；严禁出现 1 秒镜头
    - 景别切换：人物对话切换时景别必须有变化
    - 估算时长：必须合理；剧情衔接必须连贯；不删减或添加剧情；只能微压，不能压缩剧情
    - 新场景交代：必须交代清楚
    - 组尾衔接：必须以自然状态收尾，并注明“不强制静止”

    判不通过的口径：
    - 只把下面这些视为硬错误：剧情被删减/新增；组编号混乱到影响阅读；场景或在场人物缺失到无法拍；关键对话没有“谁对谁说”；出现明显 1 秒镜头；组时长明显失真且无法靠微调修正。
    - 自然格式缺失、组号/镜头号混乱、组标题总时长与镜头估算时长明显不一致、镜头数声明与实际镜头数明显不一致，属于硬错误；这是为了后续局部修复，不属于审美偏好。
    - 组标题总时长与镜头时长相加不一致时，只有组内镜头实际总时长明显低于8秒或高于17秒，才判硬错误；如果实际总时长仍在8-17秒之间，只能放入 warnings。
    - 单镜头台词明显塞不下时才判硬错误：必须证明台词语速超过 7 字/秒，或出现 1 秒镜头，或台词与复杂动作明显无法同镜完成。若台词语速在 6-7 字/秒之间，只能放入 warnings。
    - 景别重复、视线描述不够细、局部镜头时长偏短1-2秒、组尾衔接措辞不够漂亮，默认都是 warnings，不得作为 pass=false 的唯一原因。
    - 时长是估算，不是数学竞赛。不要因为 0.5-2 秒级的轻微误差就判失败。
    - 单组时长只有在明显低于 8 秒或明显高于 17 秒时，才优先判为硬错误；8-10 秒或 15-17 秒之间，如果能靠轻微表演、停顿、动作节奏修正，则不要判失败。
    - 单句台词估时允许存在小幅浮动；不要把抬头、转视线、轻微停顿机械地都算成整秒。
    - 审核时必须区分“基础台词时长”和“镜头最终时长”；严禁只用台词字数÷4直接判定最终镜头时长。只要镜头包含动作、停顿、反应、走位、递物、转身、起坐等，就必须检查是否额外加秒。
    - 如果需要提到“字数”或“台词长度”，只能粗略统计有效文本内容：汉字、英文单词、阿拉伯数字；必须忽略标点、引号、省略号、破折号、括号、空格、换行、镜头编号和说话人标签。
    - 所有台词时长类 issues 或 warnings 都必须写明“有效字数 / 镜头秒数 / 字秒比”。例如：有效字数42字，镜头7秒，约6.0字/秒。
    - 除非属于“明显塞不下”的情况，否则不要给出精确字数和精确秒数；优先使用“明显偏短 / 明显超载 / 基本可容纳”这类判断。
    - 对同一类重复问题要合并，不要把整集几十个近似的时长小误差逐条展开。
    - 如果整稿主体可用，只剩少量局部时长微调、镜头润色或措辞优化，必须返回 pass=true。

    输出要求：
    - 只返回 JSON
    - 不要输出 markdown
    - 不要输出代码块
    - 不要输出解释文字
    - issues 最多返回 5 条；只放硬错误，优先返回最关键、最能代表问题的条目
    - warnings 最多返回 5 条；只放不阻断产出的质检提醒

    JSON 结构如下：
    {
      "pass": true,
      "summary": "一句话总结",
      "issues": [
        {
          "severity": "hard",
          "group": "第3组",
          "rule": "对话指向",
          "problem": "具体问题",
          "evidence": "具体证据",
          "fix": "可执行修改建议"
        }
      ],
      "warnings": [
        {
          "severity": "soft",
          "group": "第5组",
          "rule": "景别切换",
          "problem": "不阻断产出的质检提醒",
          "evidence": "具体证据",
          "fix": "可选优化建议"
        }
      ]
    }
    """
).strip()


@dataclass
class EpisodeInput:
    source_path: Path
    episode_number: int | None
    display_name: str
    series_title: str
    script_text: str


@dataclass
class GenerationResult:
    output_path: Path
    status: str
    error: str | None = None


@dataclass
class SplitEpisode:
    episode_number: int | None
    heading: str
    display_name: str
    series_title: str
    script_text: str


@dataclass
class ReviewIssue:
    severity: str
    group: str
    rule: str
    problem: str
    evidence: str
    fix: str


@dataclass
class ReviewDecision:
    passed: bool
    summary: str
    issues: list[ReviewIssue]
    warnings: list[ReviewIssue]
    raw_text: str


@dataclass
class EpisodeJob:
    sequence_index: int
    episode: EpisodeInput
    output_path: Path


@dataclass
class RequestBatchJob:
    batch_index: int
    items: list[EpisodeJob]


@dataclass
class BatchGenerationResult:
    completed_count: int
    errors: list[str]


@dataclass
class FallbackReviewState:
    review_feedback: str | None = None
    consumed_rounds: int = 0
    draft_text: str | None = None
    draft_metadata: dict | None = None


@dataclass
class EpisodeSegment:
    index: int
    total: int
    title: str
    script_text: str


@dataclass
class SegmentGenerationResult:
    segment: EpisodeSegment
    content: str
    metadata: dict
    status: str
    review_feedback: str | None = None


def validate_api_key_for_provider(provider: str, api_key: str) -> None:
    normalized_key = api_key.strip()
    if not normalized_key:
        raise ValueError(f"请先填写 {get_provider_api_key_label(provider)}。")

    lowered = normalized_key.lower()
    if provider == PROVIDER_DEEPSEEK and lowered.startswith("sk-kimi-"):
        raise ValueError(
            "当前填写的是 Kimi Key（前缀 `sk-kimi-`），不是 DeepSeek Key。"
            "请在 GUI 里把 DeepSeek Key 改成正确的 `DEEPSEEK_API_KEY` 后再重试。"
        )


def runtime_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def load_review_skill_text(explicit_path: Path | None = None) -> str:
    candidate_paths = [explicit_path] if explicit_path is not None else []
    candidate_paths.append(runtime_base_dir() / DEFAULT_REVIEW_SKILL_FILENAME)
    candidate_paths.append(Path.cwd() / DEFAULT_REVIEW_SKILL_FILENAME)
    for path in candidate_paths:
        if path and path.is_file():
            return read_utf8_text(path)
    return DEFAULT_REVIEW_SKILL_TEXT


def is_deepseek_v4_model(provider: str, model: str) -> bool:
    return provider == PROVIDER_DEEPSEEK and model.strip().lower() in {
        "deepseek-v4-flash",
        "deepseek-v4-pro",
    }


def apply_provider_skill_optimizations(provider: str, model: str, user_content: str) -> str:
    if is_deepseek_v4_model(provider, model):
        return user_content + DEEPSEEK_NO_INNER_OS_MARKER
    return user_content


def append_output_protocol_contract(user_content: str) -> str:
    return f"{user_content.rstrip()}\n\n{OUTPUT_PROTOCOL_CONTRACT}"


def get_provider_config(provider: str) -> dict[str, str]:
    if provider not in PROVIDER_CONFIGS:
        raise ValueError(f"Unsupported provider: {provider}")
    return PROVIDER_CONFIGS[provider]


def get_provider_display_name(provider: str) -> str:
    return get_provider_config(provider)["display_name"]


def get_provider_api_key_label(provider: str) -> str:
    return get_provider_config(provider).get("api_key_label", "API Key")


def get_provider_model_options(provider: str) -> list[str]:
    return list(get_provider_config(provider).get("model_options", []))


def provider_supports_thinking(provider: str) -> bool:
    return bool(get_provider_config(provider).get("supports_thinking", False))


def provider_supports_reasoning_effort(provider: str) -> bool:
    return bool(get_provider_config(provider).get("supports_reasoning_effort", False))


def get_provider_reasoning_effort_options(provider: str) -> list[str]:
    return list(get_provider_config(provider).get("reasoning_effort_options", []))


def normalize_reasoning_effort(provider: str, reasoning_effort: str | None) -> str | None:
    if not provider_supports_reasoning_effort(provider):
        return None
    normalized_value = (reasoning_effort or DEFAULT_GENERATION_REASONING_EFFORT).strip().lower()
    alias_map = {
        "low": "high",
        "medium": "high",
        "high": "high",
        "max": "max",
        "xhigh": "max",
    }
    return alias_map.get(normalized_value, DEFAULT_GENERATION_REASONING_EFFORT)


def resolve_review_model(provider: str, generation_model: str) -> str:
    normalized_model = generation_model.strip().lower()
    if provider == PROVIDER_DEEPSEEK and normalized_model in {"deepseek-v4-pro", "deepseek-reasoner"}:
        return "deepseek-v4-flash"
    if provider == PROVIDER_QWEN_CHAT:
        return "qwen3.6-flash"
    return generation_model


def resolve_api_base(provider: str, explicit_value: str | None = None) -> str:
    config = get_provider_config(provider)
    if explicit_value:
        return explicit_value
    return os.environ.get(config["api_base_env"], config["api_base"])


def resolve_model(provider: str, explicit_value: str | None = None) -> str:
    config = get_provider_config(provider)
    if explicit_value:
        return explicit_value
    return os.environ.get(config["model_env"], config["model"])


def resolve_api_key(provider: str) -> str | None:
    return os.environ.get(get_provider_config(provider)["api_key_env"])


def resolve_default_max_tokens(provider: str) -> int:
    return int(get_provider_config(provider)["default_max_tokens"])


def resolve_default_max_tokens_for_model(provider: str, model: str | None = None) -> int:
    normalized_model = (model or "").strip().lower()
    if normalized_model in {"deepseek-v4-flash", "deepseek-v4-pro"}:
        return 32768
    if normalized_model == "deepseek-chat":
        return 8000
    if normalized_model == "deepseek-reasoner":
        return 65536
    if normalized_model in {"qwen3.6-plus", "qwen3.6-flash"}:
        return 65536
    return resolve_default_max_tokens(provider)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch-generate storyboard prompts with DeepSeek, Qwen Chat, or BLTCY Chat API."
    )
    parser.add_argument(
        "--provider",
        choices=sorted(PROVIDER_CONFIGS.keys()),
        default=DEFAULT_PROVIDER,
        help=f"Provider to use. Default: {DEFAULT_PROVIDER}",
    )
    parser.add_argument(
        "--prompt",
        type=Path,
        help="Path to the shared prompt txt file. Defaults to the first match of '*prompt*.txt'.",
    )
    parser.add_argument(
        "--scripts-glob",
        default=DEFAULT_SCRIPT_GLOB,
        help=f"Glob for episode script files. Default: {DEFAULT_SCRIPT_GLOB}",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for generated outputs. Default: ./outputs",
    )
    parser.add_argument(
        "--api-base",
        default=None,
        help="Provider API base URL. Defaults to the selected provider's standard endpoint.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Provider model name. Defaults to the selected provider's standard model.",
    )
    parser.add_argument(
        "--disable-thinking",
        action="store_true",
        help="Legacy alias: disable generation thinking mode.",
    )
    parser.add_argument(
        "--disable-generation-thinking",
        action="store_true",
        help="Disable thinking mode for the generation skill.",
    )
    parser.add_argument(
        "--enable-review-thinking",
        action="store_true",
        help="Enable thinking mode for the review skill. Default: disabled.",
    )
    parser.add_argument(
        "--generation-reasoning-effort",
        choices=DEEPSEEK_REASONING_EFFORT_OPTIONS,
        default=DEFAULT_GENERATION_REASONING_EFFORT,
        help=(
            "Reasoning effort for DeepSeek generation thinking. "
            f"Choices: {', '.join(DEEPSEEK_REASONING_EFFORT_OPTIONS)}. "
            f"Default: {DEFAULT_GENERATION_REASONING_EFFORT}"
        ),
    )
    parser.add_argument(
        "--review-reasoning-effort",
        choices=DEEPSEEK_REASONING_EFFORT_OPTIONS,
        default=DEFAULT_REVIEW_REASONING_EFFORT,
        help=(
            "Reasoning effort for DeepSeek review thinking. "
            f"Choices: {', '.join(DEEPSEEK_REASONING_EFFORT_OPTIONS)}. "
            f"Default: {DEFAULT_REVIEW_REASONING_EFFORT}"
        ),
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.3,
        help="Sampling temperature. Default: 0.3",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=1800,
        help="HTTP timeout for one provider request. Default: 1800",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Maximum output tokens. Default: depends on the selected provider/model.",
    )
    parser.add_argument(
        "--delay-seconds",
        type=float,
        default=1.0,
        help="Delay between successful requests. Default: 1.0",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Retry count for transient API failures. Default: 3",
    )
    parser.add_argument(
        "--parallelism",
        type=int,
        default=DEFAULT_PARALLELISM,
        help=f"How many episodes to generate in parallel. Default: {DEFAULT_PARALLELISM}",
    )
    parser.add_argument(
        "--episodes-per-request",
        type=int,
        default=DEFAULT_EPISODES_PER_REQUEST,
        help=(
            "How many episodes to pack into one generation request. "
            f"Allowed: 1-{MAX_EPISODES_PER_REQUEST}. Default: {DEFAULT_EPISODES_PER_REQUEST}"
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output files if they already exist.",
    )
    parser.add_argument(
        "--agent-review",
        action="store_true",
        help="Enable the generate-skill + review-skill agent loop.",
    )
    parser.add_argument(
        "--stable-segments",
        action="store_true",
        help=(
            "When --agent-review is enabled, split each episode by scene and keep "
            "generate-review-repair loops inside each segment before stitching."
        ),
    )
    parser.add_argument(
        "--review-rounds",
        type=int,
        default=DEFAULT_AGENT_REVIEW_ROUNDS,
        help=f"Maximum generate-review rounds when --agent-review is enabled. Default: {DEFAULT_AGENT_REVIEW_ROUNDS}",
    )
    parser.add_argument(
        "--review-skill",
        type=Path,
        default=None,
        help=f"Optional path to the review skill file. Defaults to ./{DEFAULT_REVIEW_SKILL_FILENAME} if present.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print the execution plan without calling the API.",
    )
    return parser.parse_args()


def find_prompt_file(root: Path, explicit_path: Path | None) -> Path:
    if explicit_path:
        path = explicit_path.resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Prompt file not found: {path}")
        return path

    matches = sorted(
        path for path in root.glob(DEFAULT_PROMPT_GLOB) if path.is_file()
    )
    if not matches:
        raise FileNotFoundError(
            f"No prompt file found with pattern {DEFAULT_PROMPT_GLOB!r} in {root}"
        )
    if len(matches) > 1:
        print(
            f"[info] Found multiple prompt candidates; using: {matches[0].name}",
            file=sys.stderr,
        )
    return matches[0].resolve()


def read_utf8_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_prompt_like_file(path: Path) -> bool:
    return path.suffix.lower() == ".txt" and "prompt" in path.name.lower()


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path, "r") as archive:
        xml_bytes = archive.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", DOCX_XML_NS):
        fragments = [node.text for node in paragraph.findall(".//w:t", DOCX_XML_NS)]
        line = "".join(fragment for fragment in fragments if fragment).strip()
        if line:
            paragraphs.append(line.replace("\xa0", " ").strip())
    return "\n".join(paragraphs)


def read_script_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx_text(path)
    if suffix == ".txt":
        return read_utf8_text(path)
    raise ValueError(f"Unsupported script file type: {path}")


def chinese_numeral_to_int(value: str) -> int | None:
    digits = {
        "零": 0,
        "〇": 0,
        "一": 1,
        "二": 2,
        "两": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
    }
    if not value:
        return None
    if value.isdigit():
        return int(value)
    if value == "十":
        return 10
    if "十" in value:
        left, _, right = value.partition("十")
        tens = digits.get(left, 1 if left == "" else None)
        ones = digits.get(right, 0 if right == "" else None)
        if tens is None or ones is None:
            return None
        return tens * 10 + ones
    total = 0
    for char in value:
        if char not in digits:
            return None
        total = total * 10 + digits[char]
    return total


def extract_episode_number(text: str, fallback_name: str) -> int | None:
    patterns = [
        re.compile(r"第\s*(\d+)\s*集"),
        re.compile(r"第\s*([零〇一二两三四五六七八九十]+)\s*集"),
    ]
    for source in (text[:200], fallback_name):
        for pattern in patterns:
            match = pattern.search(source)
            if not match:
                continue
            number = chinese_numeral_to_int(match.group(1))
            if number is not None:
                return number
    return None


def extract_series_title(display_name: str) -> str:
    title = re.sub(
        r"第\s*(?:\d+|[零〇一二两三四五六七八九十]+)\s*集$",
        "",
        display_name,
    ).strip()
    title = re.sub(r"[\s\-_]+$", "", title)
    return title or display_name.strip()


def sanitize_filename_part(value: str) -> str:
    sanitized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value).strip(" .")
    return sanitized or "storyboard"


def extract_collection_series_title(text: str, fallback_name: str) -> str:
    for source in [*text.splitlines()[:5], fallback_name]:
        match = SERIES_TITLE_RE.search(source.strip())
        if match:
            return match.group(0)

    cleaned_name = re.sub(
        r"[（(][^）)]*(?:\d+|[一二三四五六七八九十百零〇两]+)\s*集[^）)]*[）)]",
        "",
        fallback_name,
    ).strip()
    return extract_series_title(cleaned_name or fallback_name)


def extract_collection_expected_episode_count(text: str) -> int | None:
    header_lines = [line.strip() for line in text.splitlines()[:5] if line.strip()]
    for source in header_lines:
        # 排除单纯的单集标题（如"第1集"），避免误把第一集标题当成总集数声明
        if re.match(r"^第\s*\d+\s*集\s*$", source):
            continue
        # 匹配明确的总集数声明（如"共20集""全20集""合计20集"）
        match = re.search(r"(?:共|全|合计|总共)\s*(\d+)\s*集", source)
        if match:
            return int(match.group(1))
    return None


def parse_episode_heading_line(line: str) -> tuple[str, int | None] | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("场"):
        return None
    heading_candidate = stripped
    if heading_candidate.startswith("**") and heading_candidate.endswith("**"):
        heading_candidate = heading_candidate[2:-2].strip()

    exact_match = EPISODE_HEADING_RE.match(heading_candidate)
    if exact_match:
        return stripped, chinese_numeral_to_int(exact_match.group(1))

    search_match = EPISODE_NUMBER_RE.search(heading_candidate)
    if not search_match:
        return None

    looks_like_heading = (
        heading_candidate.startswith("第")
        or "剧本" in heading_candidate
        or "分集" in heading_candidate
        or "集数" in heading_candidate
        or "片名" in heading_candidate
        or "《" in heading_candidate
    )
    if not looks_like_heading:
        return None
    return stripped, chinese_numeral_to_int(search_match.group(1))


def is_episode_end_line(line: str) -> bool:
    stripped = line.strip().strip("*").strip()
    return bool(EPISODE_END_RE.search(stripped))


def is_scene_one_line(line: str) -> bool:
    return bool(SCENE_ONE_RE.match(line.strip()))


def trim_trailing_series_label(lines: list[str]) -> list[str]:
    trimmed = list(lines)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()
    if len(trimmed) < 2:
        return trimmed
    last = trimmed[-1].strip().strip("*").strip()
    prev = trimmed[-2]
    if is_episode_end_line(prev) and 1 <= len(last) <= 20 and not any(char in last for char in "：:（）()【】"):
        trimmed.pop()
    return trimmed


def split_episode_collection_text(text: str, fallback_name: str) -> list[SplitEpisode]:
    lines = text.splitlines()
    heading_rows: list[tuple[int, str, int | None]] = []
    for index, line in enumerate(lines):
        parsed_heading = parse_episode_heading_line(line)
        if not parsed_heading:
            continue
        heading, episode_number = parsed_heading
        if heading_rows:
            prev_index, _, prev_episode_number = heading_rows[-1]
            if (
                episode_number is not None
                and prev_episode_number == episode_number
                and index - prev_index <= 2
            ):
                continue
        heading_rows.append((index, heading, episode_number))

    explicit_heading_count = len(heading_rows)
    existing_starts = {row[0] for row in heading_rows}
    for index, line in enumerate(lines):
        if not is_episode_end_line(line):
            continue
        next_index = index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1
        if next_index >= len(lines):
            continue
        if next_index in existing_starts:
            continue
        if is_scene_one_line(lines[next_index]):
            heading_rows.append((next_index, f"第{len(heading_rows) + 1}集", None))
            existing_starts.add(next_index)

    heading_rows.sort(key=lambda row: row[0])

    if len(heading_rows) < 2:
        raise ValueError("未识别到稳定的多集标题，至少需要 2 个独立的“第X集”标题行。")

    series_title = extract_collection_series_title(text, fallback_name)
    episodes: list[SplitEpisode] = []
    for idx, (start_line, heading, episode_number) in enumerate(heading_rows, start=1):
        end_line = heading_rows[idx][0] if idx < len(heading_rows) else len(lines)
        chunk_lines = trim_trailing_series_label([line.rstrip() for line in lines[start_line:end_line]])
        chunk = "\n".join(chunk_lines).strip()
        resolved_episode_number = episode_number or idx
        display_name = f"{series_title}第{resolved_episode_number:02d}集"
        episodes.append(
            SplitEpisode(
                episode_number=resolved_episode_number,
                heading=heading,
                display_name=display_name,
                series_title=series_title,
                script_text=chunk,
            )
        )

    expected_count = extract_collection_expected_episode_count(text)
    if expected_count is not None and expected_count != len(episodes) and explicit_heading_count == len(episodes):
        raise ValueError(
            f"合集标题标注为 {expected_count} 集，但实际只识别到 {len(episodes)} 个分集标题，请检查原文件格式。"
        )
    return episodes


def split_episode_collection_file(
    source_path: Path,
    out_dir: Path,
    overwrite: bool = True,
) -> list[Path]:
    text = read_script_text(source_path)
    episodes = split_episode_collection_text(text, source_path.stem)
    out_dir.mkdir(parents=True, exist_ok=True)

    written_paths: list[Path] = []
    for index, episode in enumerate(episodes, start=1):
        episode_number = episode.episode_number or index
        output_name = f"{sanitize_filename_part(episode.series_title)}第{episode_number:02d}集.txt"
        output_path = out_dir / output_name
        if output_path.exists() and not overwrite:
            written_paths.append(output_path)
            continue
        output_path.write_text(episode.script_text.strip() + "\n", encoding="utf-8")
        written_paths.append(output_path)
    return written_paths


def episode_input_from_path(path: Path) -> EpisodeInput | None:
    if path.name.startswith("~$"):
        return None
    if path.suffix.lower() not in SUPPORTED_SCRIPT_SUFFIXES:
        return None
    if is_prompt_like_file(path):
        return None

    script_text = read_script_text(path)
    episode_number = extract_episode_number(script_text, path.stem)
    series_title = extract_series_title(path.stem)
    return EpisodeInput(
        source_path=path.resolve(),
        episode_number=episode_number,
        display_name=path.stem,
        series_title=series_title,
        script_text=script_text,
    )


def build_episode_inputs_from_paths(paths: list[Path]) -> list[EpisodeInput]:
    episode_inputs: list[EpisodeInput] = []
    for path in sorted(paths):
        episode = episode_input_from_path(path)
        if episode is not None:
            episode_inputs.append(episode)
    return episode_inputs


def build_episode_inputs(root: Path, scripts_glob: str) -> list[EpisodeInput]:
    paths = [path for path in root.glob(scripts_glob) if path.is_file()]
    return build_episode_inputs_from_paths(paths)


def make_output_path(
    out_dir: Path,
    episode: EpisodeInput,
    sequence_index: int,
    model: str | None = None,
) -> Path:
    episode_number = episode.episode_number or sequence_index
    title_part = sanitize_filename_part(episode.series_title)
    model_part = sanitize_filename_part(model) if model else "default-model"
    return out_dir / f"{title_part}-ep{episode_number:02d}-{model_part}-storyboard.txt"


def build_generation_messages(
    prompt_text: str,
    episode: EpisodeInput,
    provider: str,
    model: str,
    review_feedback: str | None = None,
) -> list[dict[str, str]]:
    if review_feedback:
        user_content = (
            f"{REVISION_HINT}\n\n"
            f"剧本文件：{episode.source_path.name}\n"
            f"剧本标题：{episode.display_name}\n\n"
            f"【审核意见】\n{review_feedback.strip()}\n\n"
            f"【原剧本】\n{episode.script_text}"
        )
    else:
        user_content = (
            f"{SYSTEM_PROMPT_HINT}\n\n"
            f"剧本文件：{episode.source_path.name}\n"
            f"剧本标题：{episode.display_name}\n\n"
            f"{episode.script_text}"
        )
    user_content = append_output_protocol_contract(user_content)
    user_content = apply_provider_skill_optimizations(provider, model, user_content)
    return [
        {"role": "system", "content": prompt_text},
        {"role": "user", "content": user_content},
    ]


SCENE_HEADING_RE = re.compile(
    r"(?mx)"
    r"^[\ufeff \t#]*("
    r"(?:场\s*[-－—]?\s*\d+(?:[-－—]\d+)?[^\n]*)"
    r"|(?:第\s*[0-9一二三四五六七八九十百零〇两]+\s*集\s+\d+\s*[-－—]\s*\d+[^\n]*)"
    r"|(?:\d{1,3}\s*[-－—]\s*\d{1,3}\s+(?:日|夜|晨|晚|清晨|傍晚|黄昏)?\s*/\s*(?:内|外|内外|外内)\s+[^\n]+)"
    r")$"
)


def split_episode_into_segments(
    episode: EpisodeInput,
    target_chars: int = DEFAULT_SEGMENT_TARGET_CHARS,
) -> list[EpisodeSegment]:
    """Split an episode into scene-sized chunks for stable same-context repair loops."""
    text = episode.script_text.strip()
    matches = list(SCENE_HEADING_RE.finditer(text))
    raw_segments: list[tuple[str, str]] = []
    if matches:
        preamble = text[: matches[0].start()].strip()
        for index, match in enumerate(matches):
            start = match.start()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            scene_text = text[start:end].strip()
            if preamble:
                scene_text = f"{preamble}\n{scene_text}"
            title = re.sub(r"\s+", " ", match.group(1).strip())
            raw_segments.append((title, scene_text))
    else:
        paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
        current: list[str] = []
        current_length = 0
        for paragraph in paragraphs:
            if current and current_length + len(paragraph) > target_chars:
                raw_segments.append((f"文本段{len(raw_segments) + 1}", "\n\n".join(current)))
                current = []
                current_length = 0
            current.append(paragraph)
            current_length += len(paragraph)
        if current:
            raw_segments.append((f"文本段{len(raw_segments) + 1}", "\n\n".join(current)))

    if not raw_segments:
        raw_segments = [("全文", text)]

    # If a scene is unusually long, split by paragraph without crossing the segment boundary.
    normalized: list[tuple[str, str]] = []
    for title, segment_text in raw_segments:
        if len(segment_text) <= target_chars * 1.4:
            normalized.append((title, segment_text))
            continue
        paragraphs = [part.strip() for part in re.split(r"\n\s*\n", segment_text) if part.strip()]
        current: list[str] = []
        current_length = 0
        part_index = 1
        for paragraph in paragraphs:
            if current and current_length + len(paragraph) > target_chars:
                normalized.append((f"{title} part{part_index}", "\n\n".join(current)))
                part_index += 1
                current = []
                current_length = 0
            current.append(paragraph)
            current_length += len(paragraph)
        if current:
            suffix = f" part{part_index}" if part_index > 1 else ""
            normalized.append((f"{title}{suffix}", "\n\n".join(current)))

    total = len(normalized)
    return [
        EpisodeSegment(index=index, total=total, title=title, script_text=segment_text)
        for index, (title, segment_text) in enumerate(normalized, start=1)
    ]


def build_segment_episode_input(episode: EpisodeInput, segment: EpisodeSegment) -> EpisodeInput:
    segment_script = textwrap.dedent(
        f"""
        【分段稳定模式】
        当前只处理本集的第 {segment.index}/{segment.total} 段：{segment.title}
        只能覆盖本段原剧本内容，不要补写其他段剧情；本段必须完整保留台词、动作、表情和剧情信息。

        {segment.script_text}
        """
    ).strip()
    return EpisodeInput(
        source_path=episode.source_path,
        episode_number=episode.episode_number,
        display_name=f"{episode.display_name} - 段{segment.index:02d}/{segment.total} {segment.title}",
        series_title=episode.series_title,
        script_text=segment_script,
    )


def build_segment_repair_user_message(feedback: str, *, protocol_only: bool = False) -> str:
    if protocol_only:
        repair_goal = (
            "只允许修复自然格式边界、组标题总时长、镜头数、镜头估算时长和编号。"
            "不要改剧情、不要改台词、不要改镜头描述、不要增删未被格式要求影响的镜头。"
        )
    else:
        repair_goal = (
            "只修正审核指出的硬错误，尽量保留上一版结构和未被指出的问题区域。"
            "不要重写整段，不要新增或删减原剧本剧情。"
        )
    user_content = textwrap.dedent(
        f"""
        继续在同一个剧情段内修稿。
        {repair_goal}
        修完后重新输出本段完整最终分镜提示词，不要解释，不要输出审核结论。

        【需要修正的问题】
        {feedback.strip()}
        """
    ).strip()
    return append_output_protocol_contract(user_content)


def make_batch_output_marker(job: EpisodeJob) -> str:
    episode_number = job.episode.episode_number or job.sequence_index
    return f"EP{episode_number:02d}"


def build_batch_generation_messages(
    prompt_text: str,
    jobs: list[EpisodeJob],
    provider: str,
    model: str,
) -> list[dict[str, str]]:
    output_rules = []
    episode_blocks = []
    for job in jobs:
        marker = make_batch_output_marker(job)
        output_rules.append(
            f"[[{marker}_START]]\n对应这一集的完整最终分镜提示词\n[[{marker}_END]]"
        )
        episode_blocks.append(
            textwrap.dedent(
                f"""
                【{marker}】
                剧本文件：{job.episode.source_path.name}
                剧本标题：{job.episode.display_name}

                {job.episode.script_text}
                """
            ).strip()
        )

    output_rules_text = "\n".join(output_rules)
    episode_blocks_text = "\n\n".join(episode_blocks)
    user_content = textwrap.dedent(
        f"""
        下面一次处理 {len(jobs)} 集剧本。请对每一集分别独立输出完整最终分镜提示词，禁止跨集混写、禁止合并集数、禁止省略其中任何一集。
        除下面指定的分隔符正文外，不要输出解释、目录、前言、总结或额外说明。

        请严格按以下格式输出每一集：
        {output_rules_text}

        【剧本列表】
        {episode_blocks_text}
        """
    ).strip()
    user_content = append_output_protocol_contract(user_content)
    user_content = apply_provider_skill_optimizations(provider, model, user_content)
    return [
        {"role": "system", "content": prompt_text},
        {"role": "user", "content": user_content},
    ]


def build_review_messages(
    review_skill_text: str,
    episode: EpisodeInput,
    draft_text: str,
    provider: str,
    model: str,
) -> list[dict[str, str]]:
    user_content = textwrap.dedent(
        f"""
        请严格审核下面这份分镜稿是否符合所有硬规则。
        如果存在硬错误，只把硬错误放入 issues 并返回 pass=false。
        如果只有景别重复、视线措辞不够细、局部时长轻微偏差等软问题，把它们放入 warnings，并返回 pass=true、issues=[]。
        不要把 warnings 当作回修阻断原因。

        剧本文件：{episode.source_path.name}
        剧本标题：{episode.display_name}

        【原剧本】
        {episode.script_text}

        【当前分镜稿】
        {draft_text.strip()}
        """
    ).strip()
    user_content = apply_provider_skill_optimizations(provider, model, user_content)
    return [
        {"role": "system", "content": review_skill_text},
        {"role": "user", "content": user_content},
    ]


def extract_json_object(raw_text: str) -> dict:
    cleaned = raw_text.strip()
    fenced_match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", cleaned, flags=re.DOTALL)
    if fenced_match:
        cleaned = fenced_match.group(1).strip()
    else:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start == -1 or end == -1 or end < start:
            raise ValueError("审核 skill 没有返回可解析的 JSON。")
        cleaned = cleaned[start : end + 1]
    return json.loads(cleaned, strict=False)


def _contains_out_of_bounds_group_duration(text: str) -> bool:
    duration_patterns = [
        r"(?:镜头时长相加为|镜头时长之和为|实际总时长|实际镜头时长|共)(\d{1,3})秒",
        r"(\d{1,3})秒(?:，|,)?(?:明显)?(?:高于|超过|低于|远低于)",
    ]
    for pattern in duration_patterns:
        for match in re.finditer(pattern, text):
            seconds = int(match.group(1))
            if seconds < 8 or seconds > 17:
                return True
    return any(keyword in text for keyword in ("高于17秒", "超过17秒", "低于8秒", "远低于10秒", "总时长仅4秒"))


def _extract_chars_per_second_values(text: str) -> list[float]:
    values: list[float] = []
    patterns = [
        r"(\d+(?:\.\d+)?)\s*字\s*/\s*秒",
        r"(\d+(?:\.\d+)?)\s*字每秒",
        r"(\d+(?:\.\d+)?)\s*字／秒",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            values.append(float(match.group(1)))
    return values


def _is_dialogue_timing_issue(text: str) -> bool:
    return any(keyword in text for keyword in ("台词", "有效字", "字/秒", "字每秒", "语速", "明显塞不下"))


def should_downgrade_review_issue(issue: ReviewIssue) -> bool:
    text = f"{issue.group} {issue.rule} {issue.problem} {issue.evidence} {issue.fix}"
    if issue.severity in {"soft", "warning", "warn", "advice", "notice"}:
        return True
    if _is_dialogue_timing_issue(text):
        speeds = _extract_chars_per_second_values(text)
        if speeds and max(speeds) <= 7.0:
            return True
        if any(keyword in text for keyword in ("不超过7字/秒", "7字/秒以内", "小于7字/秒", "低于7字/秒")):
            return True
    if "景别" in text:
        return True
    if any(keyword in text for keyword in ("组尾衔接", "措辞", "轻微", "可微调")):
        return True
    if any(keyword in text for keyword in ("视线未指向", "视线没有指向", "未指向对方眼睛", "背对")):
        if not any(keyword in text for keyword in ("没有“谁对谁说”", "缺少明确", "未写明对谁", "对话对象错误", "改变了对话对象")):
            return True
    if any(keyword in text for keyword in ("组标题总时长", "镜头时长相加不一致", "镜头时长之和", "时长相加")):
        if not _contains_out_of_bounds_group_duration(text):
            return True
    return False


def parse_review_decision(raw_text: str) -> ReviewDecision:
    data = extract_json_object(raw_text)
    issues_raw = data.get("issues", [])
    warnings_raw = data.get("warnings", [])
    issues: list[ReviewIssue] = []
    warnings: list[ReviewIssue] = []

    def parse_issue(item: dict, default_severity: str) -> ReviewIssue:
        severity = str(item.get("severity", default_severity)).strip().lower() or default_severity
        return ReviewIssue(
            severity=severity,
            group=str(item.get("group", "")).strip() or "未标明组别",
            rule=str(item.get("rule", "")).strip() or "未标明规则",
            problem=str(item.get("problem", "")).strip() or "未描述问题",
            evidence=str(item.get("evidence", "")).strip() or "未提供证据",
            fix=str(item.get("fix", "")).strip() or "未提供修改建议",
        )

    for item in issues_raw:
        if not isinstance(item, dict):
            continue
        issue = parse_issue(item, "hard")
        if issue.severity in {"soft", "warning", "warn", "advice", "notice"}:
            warnings.append(issue)
        else:
            issues.append(issue)
    for item in warnings_raw:
        if not isinstance(item, dict):
            continue
        warnings.append(parse_issue(item, "soft"))
    hard_issues: list[ReviewIssue] = []
    for issue in issues:
        if should_downgrade_review_issue(issue):
            issue.severity = "soft"
            warnings.append(issue)
        else:
            hard_issues.append(issue)
    issues = hard_issues
    passed = not issues
    summary = str(data.get("summary", "")).strip()
    if issues:
        passed = False
    if not summary:
        summary = "审核通过。" if passed else f"审核未通过，共 {len(issues)} 个问题。"
    return ReviewDecision(passed=passed, summary=summary, issues=issues, warnings=warnings, raw_text=raw_text)


def format_review_feedback(decision: ReviewDecision) -> str:
    lines = [decision.summary.strip()]
    for index, issue in enumerate(decision.issues, start=1):
        lines.append(
            textwrap.dedent(
                f"""
                {index}. 组别：{issue.group}
                规则：{issue.rule}
                问题：{issue.problem}
                证据：{issue.evidence}
                修改建议：{issue.fix}
                """
            ).strip()
        )
    return "\n".join(lines).strip()


def format_review_warnings(decision: ReviewDecision) -> str:
    lines = [decision.summary.strip() or "审核通过，但存在质检提醒。"]
    lines.append("审核通过，但以下质检提醒已记录；不会触发自动回修。")
    for index, issue in enumerate(decision.warnings, start=1):
        lines.append(
            textwrap.dedent(
                f"""
                {index}. 组别：{issue.group}
                规则：{issue.rule}
                问题：{issue.problem}
                证据：{issue.evidence}
                建议：{issue.fix}
                """
            ).strip()
        )
    return "\n".join(lines).strip()


def summarize_review_issues(decision: ReviewDecision) -> str:
    if not decision.issues:
        return decision.summary
    preview = []
    for issue in decision.issues[:3]:
        preview.append(f"{issue.group}/{issue.rule}: {issue.problem}")
    suffix = " ..." if len(decision.issues) > 3 else ""
    return "; ".join(preview) + suffix


def summarize_review_warnings(decision: ReviewDecision) -> str:
    if not decision.warnings:
        return ""
    preview = []
    for issue in decision.warnings[:3]:
        preview.append(f"{issue.group}/{issue.rule}: {issue.problem}")
    suffix = " ..." if len(decision.warnings) > 3 else ""
    return "; ".join(preview) + suffix


def emit_review_warnings(log: Callable[[str], None] | None, decision: ReviewDecision) -> None:
    for index, issue in enumerate(decision.warnings, start=1):
        emit_log(
            log,
            f"[review-warning] {index}. {issue.group}/{issue.rule}: {issue.problem} | 证据：{issue.evidence}",
        )


GROUP_START_RE = re.compile(
    r'<<<GROUP\s+id="(?P<id>\d{3})"\s+total="(?P<total>\d+)"\s+shots="(?P<shots>\d+)"\s*>>>'
)
GROUP_END_RE = re.compile(r'<<<GROUP_END\s+id="(?P<id>\d{3})"\s*>>>')
SHOT_START_RE = re.compile(r'<<<SHOT\s+id="(?P<id>\d{3}-\d{2})"\s+seconds="(?P<seconds>\d+)"\s*>>>')
SHOT_END_RE = re.compile(r'<<<SHOT_END\s+id="(?P<id>\d{3}-\d{2})"\s*>>>')
MACHINE_PROTOCOL_TAG_LINE_RE = re.compile(r"(?m)^\ufeff?\s*<<<(?:GROUP|GROUP_END|SHOT|SHOT_END)\b.*?>>>\s*$")


def strip_storyboard_protocol_tags(content: str) -> str:
    """Remove internal GROUP/SHOT protocol tags from user-facing output files."""
    return re.sub(r"\n{3,}", "\n\n", MACHINE_PROTOCOL_TAG_LINE_RE.sub("", content)).strip()


CLEAN_GROUP_RE = re.compile(
    r"(?m)^\s*===\s*第(?P<num>[0-9一二三四五六七八九十百千万零〇两]+)组(?!结束)(?P<rest>.*?)$"
)
CLEAN_SHOT_RE = re.compile(r"(?m)^\s*(?P<group>\d{1,3})-(?P<shot>\d{1,2})(?:\s|\[|$)")
CLEAN_SHOT_SECONDS_RE = re.compile(r"本镜估算时长[：:]\s*(?P<seconds>\d{1,3})\s*秒")
CLEAN_GROUP_TOTAL_RE = re.compile(r"总时长[：:]\s*(?P<seconds>\d{1,3})\s*秒")
CLEAN_GROUP_SHOTS_RE = re.compile(r"镜头数[：:]\s*(?P<shots>\d{1,3})\s*个")


def _clean_group_number(value: str) -> int | None:
    if value.isdigit():
        return int(value)
    return chinese_numeral_to_int(value)


def renumber_clean_storyboard(
    content: str,
    start_group_number: int = 1,
) -> tuple[str, int, list[str]]:
    """Renumber natural storyboard groups and shot IDs without adding machine tags."""
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content.strip(), start_group_number, []

    parts: list[str] = []
    changes: list[str] = []
    cursor = 0
    next_group_number = start_group_number
    for index, group_match in enumerate(group_matches):
        block_start = group_match.start()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        old_raw = group_match.group("num")
        old_number = _clean_group_number(old_raw)
        desired_group = next_group_number
        block = content[block_start:block_end]

        block, heading_count = re.subn(
            r"(?m)^(\s*===\s*)第[0-9一二三四五六七八九十百千万零〇两]+组",
            rf"\1第{desired_group}组",
            block,
            count=1,
        )
        block = re.sub(
            r"(?m)^(\s*===\s*)第[0-9一二三四五六七八九十百千万零〇两]+组结束",
            rf"\1第{desired_group}组结束",
            block,
        )

        shot_counter = 0

        def replace_shot(match: re.Match) -> str:
            nonlocal shot_counter
            shot_counter += 1
            return f"{match.group(1)}{desired_group}-{shot_counter}{match.group(3)}"

        block = re.sub(r"(?m)^(\s*)\d{1,3}-(\d{1,2})(.*)$", replace_shot, block)

        if heading_count and old_number != desired_group:
            changes.append(f"第{old_number or old_raw}组->{desired_group}组")
        parts.append(content[cursor:block_start])
        parts.append(block)
        cursor = block_end
        next_group_number += 1

    parts.append(content[cursor:])
    return "".join(parts).strip(), next_group_number, changes


def validate_clean_storyboard_format(content: str) -> list[str]:
    """Validate the natural storyboard format used for user-facing output."""
    issues: list[str] = []
    if MACHINE_PROTOCOL_TAG_LINE_RE.search(content):
        issues.append("最终分镜中仍包含三尖括号机器标签，请删除这些标签。")

    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return issues + ["缺少自然分镜组标题，例如：=== 第1组：...（总时长：XX秒，镜头数：X个） ==="]

    expected_group = 1
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _clean_group_number(raw_group)
        if group_number is None:
            issues.append(f"第{expected_group}个组标题无法识别组号：{raw_group}")
            group_number = expected_group
        if group_number != expected_group:
            issues.append(f"组号不连续：期望第{expected_group}组，实际为第{group_number}组。")

        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]
        heading_line = group_match.group(0)

        shot_matches = list(CLEAN_SHOT_RE.finditer(block))
        seconds = [int(match.group("seconds")) for match in CLEAN_SHOT_SECONDS_RE.finditer(block)]
        if not shot_matches:
            issues.append(f"第{group_number}组缺少镜头编号，例如 {group_number}-1。")
        for shot_index, shot_match in enumerate(shot_matches, start=1):
            shot_group = int(shot_match.group("group"))
            shot_number = int(shot_match.group("shot"))
            if shot_group != group_number:
                issues.append(f"第{group_number}组内出现错误镜头组号：{shot_group}-{shot_number}。")
            if shot_number != shot_index:
                issues.append(f"第{group_number}组镜头号不连续：期望 {group_number}-{shot_index}，实际 {shot_group}-{shot_number}。")

        if len(seconds) < len(shot_matches):
            issues.append(f"第{group_number}组有镜头缺少“本镜估算时长：X秒”。")
        for shot_index, seconds_value in enumerate(seconds, start=1):
            if seconds_value <= 1:
                issues.append(f"第{group_number}组第{shot_index}镜 seconds={seconds_value}，出现禁止的 1 秒或更短镜头。")

        total_match = CLEAN_GROUP_TOTAL_RE.search(heading_line)
        if total_match:
            declared_total = int(total_match.group("seconds"))
            if declared_total < 10 or declared_total > 15:
                issues.append(f"第{group_number}组总时长={declared_total}，不在 10-15 秒范围内。")
            if seconds:
                actual_total = sum(seconds)
                if declared_total != actual_total:
                    issues.append(f"第{group_number}组总时长={declared_total}，但镜头估算时长相加为 {actual_total}。")
        else:
            issues.append(f"第{group_number}组标题缺少总时长。")

        shots_match = CLEAN_GROUP_SHOTS_RE.search(heading_line)
        if shots_match:
            declared_shots = int(shots_match.group("shots"))
            if declared_shots != len(shot_matches):
                issues.append(f"第{group_number}组镜头数={declared_shots}，但实际镜头数为 {len(shot_matches)}。")
        else:
            issues.append(f"第{group_number}组标题缺少镜头数。")

        expected_group += 1

    return issues


def validate_storyboard_protocol(content: str) -> list[str]:
    issues: list[str] = []
    group_starts = list(GROUP_START_RE.finditer(content))
    if not group_starts:
        return ["缺少 GROUP 协议标签，无法进行局部修复定位。"]

    seen_group_ids: set[str] = set()
    last_group_number = 0
    search_from = 0
    for group_start in group_starts:
        group_id = group_start.group("id")
        group_number = int(group_id)
        group_total = int(group_start.group("total"))
        declared_shots = int(group_start.group("shots"))

        if group_start.start() < search_from:
            issues.append(f"GROUP {group_id} 与上一组范围交叉或嵌套。")
            continue
        if group_id in seen_group_ids:
            issues.append(f"GROUP {group_id} 重复。")
        seen_group_ids.add(group_id)
        if group_number != last_group_number + 1:
            issues.append(f"GROUP id 不连续：期望 {last_group_number + 1:03d}，实际 {group_id}。")
        last_group_number = group_number
        if group_total < 10 or group_total > 15:
            issues.append(f"GROUP {group_id} total={group_total}，不在 10-15 秒范围内。")

        group_end = GROUP_END_RE.search(content, group_start.end())
        if group_end is None:
            issues.append(f"GROUP {group_id} 缺少 GROUP_END。")
            search_from = group_start.end()
            continue
        if group_end.group("id") != group_id:
            issues.append(f"GROUP {group_id} 的结束标签 id={group_end.group('id')}，与开始标签不一致。")
        group_body = content[group_start.end() : group_end.start()]
        search_from = group_end.end()

        shot_starts = list(SHOT_START_RE.finditer(group_body))
        if not shot_starts:
            issues.append(f"GROUP {group_id} 缺少 SHOT 协议标签。")
            continue
        if declared_shots != len(shot_starts):
            issues.append(f"GROUP {group_id} shots={declared_shots}，但实际 SHOT 数为 {len(shot_starts)}。")

        seen_shot_ids: set[str] = set()
        shot_seconds_sum = 0
        shot_search_from = 0
        for shot_start in shot_starts:
            shot_id = shot_start.group("id")
            seconds = int(shot_start.group("seconds"))
            if shot_start.start() < shot_search_from:
                issues.append(f"SHOT {shot_id} 与上一镜头范围交叉或嵌套。")
                continue
            if not shot_id.startswith(f"{group_id}-"):
                issues.append(f"SHOT {shot_id} 不属于当前 GROUP {group_id}。")
            if shot_id in seen_shot_ids:
                issues.append(f"SHOT {shot_id} 重复。")
            seen_shot_ids.add(shot_id)
            if seconds <= 1:
                issues.append(f"SHOT {shot_id} seconds={seconds}，出现禁止的 1 秒或更短镜头。")
            shot_seconds_sum += seconds

            shot_end = SHOT_END_RE.search(group_body, shot_start.end())
            if shot_end is None:
                issues.append(f"SHOT {shot_id} 缺少 SHOT_END。")
                shot_search_from = shot_start.end()
                continue
            if shot_end.group("id") != shot_id:
                issues.append(f"SHOT {shot_id} 的结束标签 id={shot_end.group('id')}，与开始标签不一致。")
            shot_search_from = shot_end.end()

        if shot_seconds_sum != group_total:
            issues.append(f"GROUP {group_id} total={group_total}，但 SHOT seconds 相加为 {shot_seconds_sum}。")

    return issues


def protocol_issue_score(issues: list[str]) -> int:
    """Rank protocol failures by how destructive they are for local repair."""
    score = 0
    for issue in issues:
        if "缺少 GROUP 协议标签" in issue:
            score += 100
        elif "缺少 GROUP_END" in issue or "缺少 SHOT 协议标签" in issue or "缺少 SHOT_END" in issue:
            score += 30
        elif "范围交叉" in issue or "重复" in issue or "不属于当前 GROUP" in issue:
            score += 20
        elif "不连续" in issue:
            score += 12
        elif "1 秒或更短" in issue or "不在 10-15 秒范围内" in issue:
            score += 10
        elif "total=" in issue or "shots=" in issue:
            score += 3
        else:
            score += 5
    return score


def normalize_storyboard_protocol_metadata(content: str) -> tuple[str, list[str]]:
    """Fix objective GROUP metadata when existing SHOT tags already define the truth."""
    changes: list[str] = []
    group_starts = list(GROUP_START_RE.finditer(content))
    if not group_starts:
        return content, changes

    parts: list[str] = []
    cursor = 0
    for group_start in group_starts:
        group_end = GROUP_END_RE.search(content, group_start.end())
        if group_end is None:
            continue

        block_start = group_start.start()
        block_end = group_end.end()
        block = content[block_start:block_end]
        group_id = group_start.group("id")
        declared_total = int(group_start.group("total"))
        declared_shots = int(group_start.group("shots"))
        shot_starts = list(SHOT_START_RE.finditer(block))
        if not shot_starts:
            continue

        actual_shots = len(shot_starts)
        seconds_sum = sum(int(match.group("seconds")) for match in shot_starts)
        normalized_total = declared_total
        normalized_shots = declared_shots
        group_changes: list[str] = []

        if declared_shots != actual_shots:
            normalized_shots = actual_shots
            group_changes.append(f"shots {declared_shots}->{actual_shots}")
        if declared_total != seconds_sum and 10 <= seconds_sum <= 15:
            normalized_total = seconds_sum
            group_changes.append(f"total {declared_total}->{seconds_sum}")

        if not group_changes:
            continue

        new_block = GROUP_START_RE.sub(
            f'<<<GROUP id="{group_id}" total="{normalized_total}" shots="{normalized_shots}">>>',
            block,
            count=1,
        )
        parts.append(content[cursor:block_start])
        parts.append(new_block)
        cursor = block_end
        changes.append(f"GROUP {group_id}: {', '.join(group_changes)}")

    if not changes:
        return content, changes
    parts.append(content[cursor:])
    return "".join(parts), changes


def renumber_storyboard_protocol(content: str, start_group_number: int = 1) -> tuple[str, int]:
    """Extract protocol groups and renumber them sequentially for stitched segment output."""
    output_blocks: list[str] = []
    next_group_number = start_group_number
    group_starts = list(GROUP_START_RE.finditer(content))
    for group_start in group_starts:
        group_end = GROUP_END_RE.search(content, group_start.end())
        if group_end is None:
            continue
        old_group_id = group_start.group("id")
        new_group_id = f"{next_group_number:03d}"
        block = content[group_start.start() : group_end.end()]

        block = re.sub(
            r'<<<GROUP\s+id="\d{3}"\s+total="(?P<total>\d+)"\s+shots="(?P<shots>\d+)"\s*>>>',
            lambda match: (
                f'<<<GROUP id="{new_group_id}" total="{match.group("total")}" '
                f'shots="{match.group("shots")}">>>'
            ),
            block,
            count=1,
        )
        block = re.sub(
            rf'<<<GROUP_END\s+id="{re.escape(old_group_id)}"\s*>>>',
            f'<<<GROUP_END id="{new_group_id}">>>',
            block,
            count=1,
        )

        shot_id_map: dict[str, str] = {}
        shot_counter = 0

        def replace_shot_start(match: re.Match) -> str:
            nonlocal shot_counter
            shot_counter += 1
            old_shot_id = match.group("id")
            new_shot_id = f"{new_group_id}-{shot_counter:02d}"
            shot_id_map[old_shot_id] = new_shot_id
            return f'<<<SHOT id="{new_shot_id}" seconds="{match.group("seconds")}">>>'

        block = SHOT_START_RE.sub(replace_shot_start, block)

        def replace_shot_end(match: re.Match) -> str:
            old_shot_id = match.group("id")
            return f'<<<SHOT_END id="{shot_id_map.get(old_shot_id, old_shot_id)}">>>'

        block = SHOT_END_RE.sub(replace_shot_end, block)
        block = re.sub(r"===\s*第\d+组", f"=== 第{next_group_number}组", block)
        block = re.sub(
            r"(?m)^(\s*)\d{1,3}-(\d{1,2})(\s*)$",
            lambda match: f"{match.group(1)}{next_group_number}-{int(match.group(2))}{match.group(3)}",
            block,
        )
        output_blocks.append(block.strip())
        next_group_number += 1

    return "\n\n".join(output_blocks), next_group_number


def merge_metadata(metadata_items: list[dict]) -> dict:
    usage_totals: dict[str, int] = {}
    response_models: list[str] = []
    finish_reasons: list[str] = []
    for metadata in metadata_items:
        usage = metadata.get("usage", {}) if metadata else {}
        for key, value in usage.items():
            if isinstance(value, int):
                usage_totals[key] = usage_totals.get(key, 0) + value
        model = metadata.get("model") if metadata else None
        if model and model not in response_models:
            response_models.append(str(model))
        choices = metadata.get("choices", []) if metadata else []
        if choices:
            finish_reason = choices[0].get("finish_reason")
            if finish_reason and finish_reason not in finish_reasons:
                finish_reasons.append(str(finish_reason))
    merged: dict = {}
    if usage_totals:
        merged["usage"] = usage_totals
    if response_models:
        merged["model"] = "+".join(response_models)
    if finish_reasons:
        merged["choices"] = [{"finish_reason": "+".join(finish_reasons)}]
    return merged


def summarize_protocol_issues(issues: list[str]) -> str:
    preview = "; ".join(issues[:3])
    suffix = " ..." if len(issues) > 3 else ""
    return preview + suffix


def format_protocol_feedback(issues: list[str]) -> str:
    lines = [
        "格式校验未通过：自然分镜组号、镜头号、组总时长、镜头数或镜头估算时长存在客观错误，请只修正对应组内容。",
        "禁止输出三尖括号机器标签；必须保留自然分镜格式，例如“=== 第1组：...（总时长：XX秒，镜头数：X个） ===”和“1-1”。",
    ]
    for index, issue in enumerate(issues, start=1):
        lines.append(f"{index}. {issue}")
    return "\n".join(lines)


def parse_batch_generation_output(raw_text: str, jobs: list[EpisodeJob]) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for job in jobs:
        marker = make_batch_output_marker(job)
        start_token = f"[[{marker}_START]]"
        end_token = f"[[{marker}_END]]"
        match = re.search(
            rf"{re.escape(start_token)}\s*(.*?)\s*{re.escape(end_token)}",
            raw_text,
            flags=re.DOTALL,
        )
        if not match:
            continue
        content = match.group(1).strip()
        if content:
            outputs[job.output_path] = content
    return outputs


def emit_log(log: Callable[[str], None] | None, message: str) -> None:
    if log:
        log(message)
        return
    print(message)


def review_episode_draft(
    *,
    episode: EpisodeInput,
    draft_text: str,
    review_skill_text: str,
    provider: str,
    api_base: str,
    api_key: str,
    model: str,
    review_thinking_enabled: bool,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    log: Callable[[str], None] | None = None,
) -> ReviewDecision:
    review_model = resolve_review_model(provider, model)
    review_messages = build_review_messages(
        review_skill_text=review_skill_text,
        episode=episode,
        draft_text=draft_text,
        provider=provider,
        model=review_model,
    )
    review_raw_text, _ = call_chat_completion(
        provider=provider,
        api_base=api_base,
        api_key=api_key,
        model=review_model,
        thinking_enabled=review_thinking_enabled,
        reasoning_effort=review_reasoning_effort,
        messages=review_messages,
        temperature=temperature,
        timeout_seconds=timeout_seconds,
        max_tokens=max_tokens,
        max_retries=max_retries,
        log=log,
    )
    return parse_review_decision(review_raw_text)


def generate_single_episode(
    *,
    episode: EpisodeInput,
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    generation_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    review_feedback: str | None = None,
    log: Callable[[str], None] | None = None,
) -> tuple[str, dict]:
    messages = build_generation_messages(
        prompt_text=prompt_text,
        episode=episode,
        provider=provider,
        model=model,
        review_feedback=review_feedback,
    )
    return call_chat_completion(
        provider=provider,
        api_base=api_base,
        api_key=api_key,
        model=model,
        thinking_enabled=generation_thinking_enabled,
        reasoning_effort=generation_reasoning_effort,
        messages=messages,
        temperature=temperature,
        timeout_seconds=timeout_seconds,
        max_tokens=max_tokens,
        max_retries=max_retries,
        log=log,
    )


def call_generation_messages(
    *,
    messages: list[dict[str, str]],
    provider: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    generation_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    log: Callable[[str], None] | None = None,
) -> tuple[str, dict]:
    return call_chat_completion(
        provider=provider,
        api_base=api_base,
        api_key=api_key,
        model=model,
        thinking_enabled=generation_thinking_enabled,
        reasoning_effort=generation_reasoning_effort,
        messages=messages,
        temperature=temperature,
        timeout_seconds=timeout_seconds,
        max_tokens=max_tokens,
        max_retries=max_retries,
        log=log,
    )


def generate_segment_with_review_loop(
    *,
    episode: EpisodeInput,
    segment: EpisodeSegment,
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    review_rounds: int,
    review_skill_text: str,
    log: Callable[[str], None] | None = None,
) -> SegmentGenerationResult:
    segment_episode = build_segment_episode_input(episode, segment)
    messages = build_generation_messages(
        prompt_text=prompt_text,
        episode=segment_episode,
        provider=provider,
        model=model,
    )
    total_rounds = max(1, review_rounds)
    latest_content = ""
    latest_metadata: dict = {}
    latest_feedback: str | None = None
    best_protocol_content = ""
    best_protocol_metadata: dict = {}
    best_protocol_issues: list[str] | None = None

    for round_index in range(1, total_rounds + 1):
        emit_log(log, f"[segment] 段{segment.index:02d}/{segment.total} 第 {round_index} 轮生成中：{segment.title}")
        latest_content, latest_metadata = call_generation_messages(
            messages=messages,
            provider=provider,
            api_base=api_base,
            api_key=api_key,
            model=model,
            generation_thinking_enabled=generation_thinking_enabled,
            generation_reasoning_effort=generation_reasoning_effort,
            temperature=temperature,
            timeout_seconds=timeout_seconds,
            max_tokens=max_tokens,
            max_retries=max_retries,
            log=log,
        )
        latest_content = strip_storyboard_protocol_tags(latest_content)
        latest_content, _, normalized_changes = renumber_clean_storyboard(latest_content)
        if normalized_changes:
            emit_log(
                log,
                f"[segment] 段{segment.index:02d} 自然格式编号已自动校准：{'; '.join(normalized_changes[:5])}"
                + (" ..." if len(normalized_changes) > 5 else ""),
            )
        protocol_issues = validate_clean_storyboard_format(latest_content)
        if best_protocol_issues is None or (
            protocol_issue_score(protocol_issues),
            len(protocol_issues),
        ) < (
            protocol_issue_score(best_protocol_issues),
            len(best_protocol_issues),
        ):
            best_protocol_content = latest_content
            best_protocol_metadata = latest_metadata
            best_protocol_issues = list(protocol_issues)
        if protocol_issues:
            latest_feedback = format_protocol_feedback(protocol_issues)
            emit_log(
                log,
                f"[segment] 段{segment.index:02d} 格式校验未通过（第 {round_index} 轮，"
                f"{len(protocol_issues)} 个问题）：{summarize_protocol_issues(protocol_issues)}",
            )
            if round_index >= total_rounds:
                if best_protocol_content and best_protocol_content != latest_content:
                    latest_feedback += (
                        "\n\n系统已保留自然格式更完整的上一版草稿；"
                        "本轮回修结果因为格式破坏更严重，未作为最终段落。"
                    )
                return SegmentGenerationResult(
                    segment=segment,
                    content=best_protocol_content or latest_content,
                    metadata=best_protocol_metadata or latest_metadata,
                    status="needs_review",
                    review_feedback=latest_feedback,
                )
            messages.extend(
                [
                    {"role": "assistant", "content": latest_content},
                    {
                        "role": "user",
                        "content": apply_provider_skill_optimizations(
                            provider,
                            model,
                            build_segment_repair_user_message(latest_feedback, protocol_only=True),
                        ),
                    },
                ]
            )
            continue

        emit_log(log, f"[segment] 段{segment.index:02d}/{segment.total} 第 {round_index} 轮审核中：{segment.title}")
        try:
            decision = review_episode_draft(
                review_skill_text=review_skill_text,
                episode=segment_episode,
                draft_text=latest_content,
                provider=provider,
                api_base=api_base,
                api_key=api_key,
                model=model,
                review_thinking_enabled=review_thinking_enabled,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                log=log,
            )
        except Exception as exc:
            latest_feedback = (
                f"段{segment.index:02d} 审核异常，已保留当前段生成稿。\n"
                f"异常原因：{exc}"
            )
            emit_log(log, f"[segment-warn] 段{segment.index:02d} 审核异常：{exc}")
            return SegmentGenerationResult(
                segment=segment,
                content=latest_content,
                metadata=latest_metadata,
                status="needs_review",
                review_feedback=latest_feedback,
            )

        if decision.passed:
            feedback = format_review_warnings(decision) if decision.warnings else None
            if decision.warnings:
                emit_log(log, f"[segment] 段{segment.index:02d} 审核通过但有提醒：{summarize_review_warnings(decision)}")
            else:
                emit_log(log, f"[segment] 段{segment.index:02d} 审核通过：{decision.summary}")
            return SegmentGenerationResult(
                segment=segment,
                content=latest_content,
                metadata=latest_metadata,
                status="done",
                review_feedback=feedback,
            )

        latest_feedback = format_review_feedback(decision)
        emit_log(
            log,
            f"[segment] 段{segment.index:02d} 审核未通过（第 {round_index} 轮，"
            f"{len(decision.issues)} 个问题）：{summarize_review_issues(decision)}",
        )
        if round_index >= total_rounds:
            return SegmentGenerationResult(
                segment=segment,
                content=latest_content,
                metadata=latest_metadata,
                status="needs_review",
                review_feedback=latest_feedback,
            )
        messages.extend(
            [
                {"role": "assistant", "content": latest_content},
                {
                    "role": "user",
                    "content": apply_provider_skill_optimizations(
                        provider,
                        model,
                        build_segment_repair_user_message(latest_feedback, protocol_only=False),
                    ),
                },
            ]
        )

    return SegmentGenerationResult(
        segment=segment,
        content=latest_content,
        metadata=latest_metadata,
        status="needs_review",
        review_feedback=latest_feedback or "分段稳定模式异常退出，未得到审核通过结果。",
    )


def build_episode_jobs(
    out_dir: Path,
    episodes: list[EpisodeInput],
    model: str,
) -> list[EpisodeJob]:
    return [
        EpisodeJob(
            sequence_index=index,
            episode=episode,
            output_path=make_output_path(out_dir, episode, index, model=model),
        )
        for index, episode in enumerate(episodes, start=1)
    ]


def build_request_batches(
    episode_jobs: list[EpisodeJob],
    episodes_per_request: int,
) -> list[RequestBatchJob]:
    normalized_batch_size = max(1, min(MAX_EPISODES_PER_REQUEST, episodes_per_request))
    batches: list[RequestBatchJob] = []
    for start in range(0, len(episode_jobs), normalized_batch_size):
        items = episode_jobs[start : start + normalized_batch_size]
        batches.append(RequestBatchJob(batch_index=len(batches) + 1, items=items))
    return batches


def resolve_effective_episodes_per_request(
    episodes_per_request: int,
    agent_review_enabled: bool,
) -> int:
    normalized = max(1, min(MAX_EPISODES_PER_REQUEST, episodes_per_request))
    if agent_review_enabled and normalized > 1:
        return 1
    return normalized


def log_generation_plan(
    prompt_path: Path,
    episodes: list[EpisodeInput],
    out_dir: Path,
    provider: str,
    model: str,
    api_base: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    timeout_seconds: int,
    parallelism: int,
    max_tokens: int,
    episodes_per_request: int = DEFAULT_EPISODES_PER_REQUEST,
    agent_review_enabled: bool = False,
    stable_segment_mode: bool = DEFAULT_STABLE_SEGMENT_MODE,
    review_rounds: int = DEFAULT_AGENT_REVIEW_ROUNDS,
    log: Callable[[str], None] | None = None,
) -> None:
    supports_thinking = provider_supports_thinking(provider)
    supports_reasoning_effort = provider_supports_reasoning_effort(provider)
    effective_generation_thinking = generation_thinking_enabled and supports_thinking
    effective_review_thinking = review_thinking_enabled and supports_thinking
    episode_jobs = build_episode_jobs(out_dir, episodes, model)
    effective_episodes_per_request = resolve_effective_episodes_per_request(
        episodes_per_request,
        agent_review_enabled,
    )
    request_batches = build_request_batches(episode_jobs, effective_episodes_per_request)
    emit_log(log, f"[info] Provider: {get_provider_display_name(provider)}")
    emit_log(log, f"[info] Model: {model}")
    emit_log(log, f"[info] Review model: {resolve_review_model(provider, model)}")
    emit_log(log, f"[info] API base: {api_base}")
    emit_log(log, f"[info] Prompt: {prompt_path.name}")
    emit_log(log, f"[info] Episodes found: {len(episodes)}")
    emit_log(log, f"[info] Output directory: {out_dir.resolve()}")
    if supports_thinking:
        emit_log(log, f"[info] Generation thinking: {'enabled' if effective_generation_thinking else 'disabled'}")
        emit_log(log, f"[info] Review thinking: {'enabled' if effective_review_thinking else 'disabled'}")
        if supports_reasoning_effort:
            generation_effort_label = (
                normalize_reasoning_effort(provider, generation_reasoning_effort)
                if effective_generation_thinking
                else "n/a (thinking disabled)"
            )
            review_effort_label = (
                normalize_reasoning_effort(provider, review_reasoning_effort)
                if effective_review_thinking
                else "n/a (thinking disabled)"
            )
            emit_log(log, f"[info] Generation reasoning effort: {generation_effort_label}")
            emit_log(log, f"[info] Review reasoning effort: {review_effort_label}")
    else:
        emit_log(log, "[info] Thinking mode: unsupported by current provider")
    emit_log(log, f"[info] Max tokens: {max_tokens}")
    emit_log(log, f"[info] Request timeout: {timeout_seconds}s")
    emit_log(log, f"[info] Parallelism: {max(1, parallelism)}")
    emit_log(log, f"[info] Episodes per request: {effective_episodes_per_request}")
    if agent_review_enabled and episodes_per_request != effective_episodes_per_request:
        emit_log(
            log,
            "[info] Agent审核回修已启用，计划自动按单集请求执行，以提高严格审核稳定性。",
        )
    emit_log(log, f"[info] Request batches: {len(request_batches)}")
    if agent_review_enabled:
        emit_log(log, f"[info] Agent review: enabled (max rounds={max(1, review_rounds)})")
        emit_log(log, f"[info] Stable segment mode: {'enabled' if stable_segment_mode else 'disabled'}")
    else:
        emit_log(log, "[info] Agent review: disabled")

    for batch in request_batches:
        batch_sources = ", ".join(job.episode.source_path.name for job in batch.items)
        batch_outputs = ", ".join(job.output_path.name for job in batch.items)
        emit_log(
            log,
            f"[batch-plan] Request {batch.batch_index}: {batch_sources} -> {batch_outputs}",
        )


def build_chat_payload(
    provider: str,
    model: str,
    thinking_enabled: bool,
    reasoning_effort: str | None,
    messages: list[dict[str, str]],
    temperature: float,
    max_tokens: int,
) -> dict:
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "stream": False,
    }
    if provider == PROVIDER_DEEPSEEK:
        payload["temperature"] = temperature
        if thinking_enabled:
            payload["thinking"] = {"type": "enabled"}
            normalized_effort = normalize_reasoning_effort(provider, reasoning_effort)
            if normalized_effort:
                payload["reasoning_effort"] = normalized_effort
    elif provider == PROVIDER_QWEN_CHAT:
        payload["temperature"] = temperature
        payload["enable_thinking"] = bool(thinking_enabled)
    elif provider == PROVIDER_BLTCY_CHAT:
        payload["temperature"] = temperature
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    return payload


def build_chat_completion_url(provider: str, api_base: str) -> str:
    config = get_provider_config(provider)
    normalized_base = api_base.rstrip("/")
    endpoint = config.get("endpoint", "")
    if not endpoint:
        return normalized_base
    if normalized_base.endswith(endpoint):
        return normalized_base
    return normalized_base + endpoint


def call_chat_completion(
    provider: str,
    api_base: str,
    api_key: str,
    model: str,
    thinking_enabled: bool,
    reasoning_effort: str | None,
    messages: list[dict[str, str]],
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    log: callable | None = None,
) -> tuple[str, dict]:
    url = build_chat_completion_url(provider, api_base)
    payload = build_chat_payload(
        provider=provider,
        model=model,
        thinking_enabled=thinking_enabled and provider_supports_thinking(provider),
        reasoning_effort=reasoning_effort,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    body = json.dumps(payload).encode("utf-8")

    for attempt in range(1, max_retries + 1):
        request = urllib.request.Request(
            url,
            data=body,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
                "User-Agent": "AutoStoryboardGenerator/1.0",
                "Connection": "close",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                raw = response.read().decode("utf-8")
            data = json.loads(raw)
            content = data["choices"][0]["message"]["content"]
            return content, data
        except urllib.error.HTTPError as exc:
            status = exc.code
            error_body = exc.read().decode("utf-8", errors="replace")
            if status in {429, 500, 503} and attempt < max_retries:
                sleep_seconds = attempt * 3
                message = (
                    f"[warn] HTTP {status}, retrying in {sleep_seconds}s "
                    f"({attempt}/{max_retries})..."
                )
                if log:
                    log(message)
                else:
                    print(message, file=sys.stderr)
                time.sleep(sleep_seconds)
                continue
            raise RuntimeError(
                f"{get_provider_display_name(provider)} API request failed with HTTP {status}: {error_body}"
            ) from exc
        except urllib.error.URLError as exc:
            if attempt < max_retries:
                sleep_seconds = attempt * 3
                message = (
                    f"[warn] Network error, retrying in {sleep_seconds}s "
                    f"({attempt}/{max_retries})..."
                )
                if log:
                    log(message)
                else:
                    print(message, file=sys.stderr)
                time.sleep(sleep_seconds)
                continue
            raise RuntimeError(
                f"Network error while calling {get_provider_display_name(provider)} API: {exc}"
            ) from exc
        except (
            http.client.RemoteDisconnected,
            http.client.BadStatusLine,
            ConnectionResetError,
            TimeoutError,
            ssl.SSLError,
        ) as exc:
            if attempt < max_retries:
                sleep_seconds = attempt * 3
                message = (
                    f"[warn] Upstream connection dropped, retrying in {sleep_seconds}s "
                    f"({attempt}/{max_retries})..."
                )
                if log:
                    log(message)
                else:
                    print(message, file=sys.stderr)
                time.sleep(sleep_seconds)
                continue
            raise RuntimeError(
                f"Upstream connection dropped while calling {get_provider_display_name(provider)} API: {exc}"
            ) from exc

    raise RuntimeError(f"{get_provider_display_name(provider)} API request failed after all retries.")


def run_single_episode_fallbacks(
    *,
    jobs: list[EpisodeJob],
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    delay_seconds: float,
    overwrite: bool,
    agent_review_enabled: bool,
    stable_segment_mode: bool,
    review_rounds: int,
    review_skill_text: str,
    fallback_states: dict[Path, FallbackReviewState] | None = None,
    log: Callable[[str], None] | None = None,
) -> list[str]:
    errors: list[str] = []
    for job in jobs:
        emit_log(log, f"[fallback] 单集重跑 {job.output_path.name} ...")
        fallback_state = fallback_states.get(job.output_path) if fallback_states else None
        if agent_review_enabled and stable_segment_mode and fallback_state is None:
            result = generate_segmented_episode_output(
                episode=job.episode,
                output_path=job.output_path,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                delay_seconds=delay_seconds,
                overwrite=overwrite,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                log=log,
            )
        else:
            result = generate_episode_output(
                episode=job.episode,
                output_path=job.output_path,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                delay_seconds=delay_seconds,
                overwrite=overwrite,
                agent_review_enabled=agent_review_enabled,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                initial_review_feedback=None if fallback_state is None else fallback_state.review_feedback,
                consumed_review_rounds=0 if fallback_state is None else fallback_state.consumed_rounds,
                initial_draft_text=None if fallback_state is None else fallback_state.draft_text,
                initial_draft_metadata=None if fallback_state is None else fallback_state.draft_metadata,
                log=log,
            )
        if result.error:
            errors.append(result.error)
    return errors


def generate_episode_batch(
    *,
    batch_job: RequestBatchJob,
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    delay_seconds: float,
    overwrite: bool,
    agent_review_enabled: bool,
    stable_segment_mode: bool,
    review_rounds: int,
    review_skill_text: str,
    log: Callable[[str], None] | None = None,
) -> BatchGenerationResult:
    pending_jobs: list[EpisodeJob] = []
    for job in batch_job.items:
        if job.output_path.exists() and not overwrite:
            emit_log(log, f"[skip] {job.output_path.name} already exists.")
            continue
        pending_jobs.append(job)

    if not pending_jobs:
        return BatchGenerationResult(completed_count=len(batch_job.items), errors=[])

    if len(pending_jobs) == 1:
        errors = run_single_episode_fallbacks(
            jobs=pending_jobs,
            provider=provider,
            prompt_text=prompt_text,
            api_base=api_base,
            api_key=api_key,
            model=model,
            generation_thinking_enabled=generation_thinking_enabled,
            review_thinking_enabled=review_thinking_enabled,
            generation_reasoning_effort=generation_reasoning_effort,
            review_reasoning_effort=review_reasoning_effort,
            temperature=temperature,
            timeout_seconds=timeout_seconds,
            max_tokens=max_tokens,
            max_retries=max_retries,
            delay_seconds=delay_seconds,
            overwrite=overwrite,
            agent_review_enabled=agent_review_enabled,
            stable_segment_mode=stable_segment_mode,
            review_rounds=review_rounds,
            review_skill_text=review_skill_text,
            log=log,
        )
        return BatchGenerationResult(completed_count=len(batch_job.items), errors=errors)

    batch_label = ", ".join(job.output_path.name for job in pending_jobs)
    emit_log(log, f"[run] Batch request {batch_job.batch_index}: {batch_label}")
    call_log = None if log is None else lambda message: emit_log(log, f"[batch {batch_job.batch_index}] {message}")

    try:
        batch_messages = build_batch_generation_messages(
            prompt_text=prompt_text,
            jobs=pending_jobs,
            provider=provider,
            model=model,
        )
        batch_raw_text, batch_metadata = call_chat_completion(
            provider=provider,
            api_base=api_base,
            api_key=api_key,
            model=model,
            thinking_enabled=generation_thinking_enabled,
            reasoning_effort=generation_reasoning_effort,
            messages=batch_messages,
            temperature=temperature,
            timeout_seconds=timeout_seconds,
            max_tokens=max_tokens,
            max_retries=max_retries,
            log=call_log,
        )
        parsed_outputs = parse_batch_generation_output(batch_raw_text, pending_jobs)
    except Exception as exc:
        emit_log(log, f"[warn] 批量请求失败，回落单集重跑：{exc}")
        errors = run_single_episode_fallbacks(
            jobs=pending_jobs,
            provider=provider,
            prompt_text=prompt_text,
            api_base=api_base,
            api_key=api_key,
            model=model,
            generation_thinking_enabled=generation_thinking_enabled,
            review_thinking_enabled=review_thinking_enabled,
            generation_reasoning_effort=generation_reasoning_effort,
            review_reasoning_effort=review_reasoning_effort,
            temperature=temperature,
            timeout_seconds=timeout_seconds,
            max_tokens=max_tokens,
            max_retries=max_retries,
            delay_seconds=delay_seconds,
            overwrite=overwrite,
            agent_review_enabled=agent_review_enabled,
            stable_segment_mode=stable_segment_mode,
            review_rounds=review_rounds,
            review_skill_text=review_skill_text,
            log=log,
        )
        return BatchGenerationResult(completed_count=len(batch_job.items), errors=errors)

    fallback_jobs: list[EpisodeJob] = []
    fallback_states: dict[Path, FallbackReviewState] = {}
    errors: list[str] = []
    batch_succeeded = True
    for job in pending_jobs:
        draft_text = parsed_outputs.get(job.output_path)
        if not draft_text:
            emit_log(log, f"[warn] 批量输出缺少 {job.output_path.name} 的分隔段，回落单集重跑。")
            fallback_jobs.append(job)
            batch_succeeded = False
            continue
        if not agent_review_enabled:
            write_output(job.output_path, job.episode, draft_text, batch_metadata)
            emit_log(log, f"[done] Saved {job.output_path}")
            continue
        try:
            decision = review_episode_draft(
                episode=job.episode,
                draft_text=draft_text,
                review_skill_text=review_skill_text,
                provider=provider,
                api_base=api_base,
                api_key=api_key,
                model=model,
                review_thinking_enabled=review_thinking_enabled,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                log=call_log,
            )
        except Exception as exc:
            emit_log(log, f"[warn] 批量结果审核失败，回落单集重跑 {job.output_path.name}：{exc}")
            fallback_jobs.append(job)
            batch_succeeded = False
            continue
        if decision.passed:
            emit_log(log, f"[agent] 批量结果审核通过：{job.output_path.name}")
            if decision.warnings:
                emit_log(
                    log,
                    f"[agent] 批量质检提醒（不回修）：{summarize_review_warnings(decision)}",
                )
                emit_review_warnings(log, decision)
                report_path = make_review_report_path(job.output_path)
                write_review_report(
                    report_path,
                    job.episode,
                    job.output_path,
                    format_review_warnings(decision),
                    status="passed_with_warnings",
                )
                emit_log(log, f"[agent] 质检报告：{report_path}")
            write_output(job.output_path, job.episode, draft_text, batch_metadata)
            emit_log(log, f"[done] Saved {job.output_path}")
            continue
        emit_log(
            log,
            f"[agent] 批量结果未通过审核，回落单集重跑 {job.output_path.name}："
            f"{summarize_review_issues(decision)}",
        )
        fallback_jobs.append(job)
        fallback_states[job.output_path] = FallbackReviewState(
            review_feedback=format_review_feedback(decision),
            consumed_rounds=1,
            draft_text=draft_text,
            draft_metadata=batch_metadata,
        )
        emit_log(
            log,
            f"[agent] {job.output_path.name} 已在批量阶段消耗第 1 轮审核，"
            f"单集回落剩余轮数：{max(0, max(1, review_rounds) - 1)}",
        )
        batch_succeeded = False

    if batch_succeeded and delay_seconds > 0:
        time.sleep(delay_seconds)

    if fallback_jobs:
        errors.extend(
            run_single_episode_fallbacks(
                jobs=fallback_jobs,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                delay_seconds=delay_seconds,
                overwrite=overwrite,
                agent_review_enabled=agent_review_enabled,
                stable_segment_mode=stable_segment_mode,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                fallback_states=fallback_states,
                log=log,
            )
        )

    return BatchGenerationResult(completed_count=len(batch_job.items), errors=errors)


def generate_segmented_episode_output(
    *,
    episode: EpisodeInput,
    output_path: Path,
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    delay_seconds: float,
    overwrite: bool,
    review_rounds: int,
    review_skill_text: str,
    log: Callable[[str], None] | None = None,
) -> GenerationResult:
    if output_path.exists() and not overwrite:
        emit_log(log, f"[skip] {output_path.name} already exists.")
        return GenerationResult(output_path=output_path, status="skipped")

    emit_log(log, f"[run] Stable segmented generation {output_path.name} ...")
    try:
        call_log = None if log is None else lambda message: emit_log(log, f"[{output_path.name}] {message}")
        segments = split_episode_into_segments(episode)
        emit_log(log, f"[segment] {output_path.name} 已拆为 {len(segments)} 个剧情段。")

        segment_results: list[SegmentGenerationResult] = []
        metadata_items: list[dict] = []
        next_group_number = 1
        stitched_blocks: list[str] = []
        review_notes: list[str] = []

        for segment in segments:
            result = generate_segment_with_review_loop(
                episode=episode,
                segment=segment,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                log=call_log,
            )
            segment_results.append(result)
            metadata_items.append(result.metadata)

            cleaned_segment_content = strip_storyboard_protocol_tags(result.content)
            segment_protocol_issues = validate_clean_storyboard_format(cleaned_segment_content)
            if segment_protocol_issues:
                renumbered_block, new_next_group_number, _ = renumber_clean_storyboard(
                    cleaned_segment_content,
                    start_group_number=next_group_number,
                )
                if renumbered_block.strip():
                    stitched_block = renumbered_block
                    next_group_number = new_next_group_number
                else:
                    stitched_block = cleaned_segment_content.strip()
                review_notes.append(
                    f"段{segment.index:02d}/{segment.total}《{segment.title}》格式仍未通过："
                    f"{summarize_protocol_issues(segment_protocol_issues)}"
                )
            else:
                stitched_block, next_group_number, _ = renumber_clean_storyboard(
                    cleaned_segment_content,
                    start_group_number=next_group_number,
                )
            stitched_blocks.append(
                f"## 分段 {segment.index:02d}/{segment.total}：{segment.title}\n\n{stitched_block.strip()}"
            )
            if result.review_feedback:
                review_notes.append(
                    f"段{segment.index:02d}/{segment.total}《{segment.title}》状态：{result.status}\n"
                    f"{result.review_feedback}"
                )

        final_content = "\n\n".join(stitched_blocks).strip()
        final_metadata = merge_metadata(metadata_items)
        final_protocol_issues = validate_clean_storyboard_format(final_content)
        if final_protocol_issues:
            review_notes.insert(
                0,
                "拼接后格式校验未通过：\n" + "\n".join(final_protocol_issues),
            )

        has_needs_review = any(result.status != "done" for result in segment_results) or bool(final_protocol_issues)
        if has_needs_review:
            return save_needs_review_draft(
                output_path=output_path,
                episode=episode,
                content=final_content,
                metadata=final_metadata,
                review_feedback="\n\n".join(review_notes) or "分段稳定模式存在未通过片段。",
                log=log,
                delay_seconds=delay_seconds,
            )

        write_output(output_path, episode, final_content, final_metadata)
        if review_notes:
            report_path = make_review_report_path(output_path)
            write_review_report(
                report_path,
                episode,
                output_path,
                "\n\n".join(review_notes),
                status="passed_with_warnings",
            )
            emit_log(log, f"[segment] 质检报告：{report_path}")
        emit_log(log, f"[done] Saved {output_path}")
        if delay_seconds > 0:
            time.sleep(delay_seconds)
        return GenerationResult(output_path=output_path, status="done")
    except Exception as exc:
        error_message = f"{output_path.name}: {exc}"
        emit_log(log, f"[error] {error_message}")
        return GenerationResult(output_path=output_path, status="error", error=error_message)


def generate_episode_output(
    *,
    episode: EpisodeInput,
    output_path: Path,
    provider: str,
    prompt_text: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    delay_seconds: float,
    overwrite: bool,
    agent_review_enabled: bool,
    review_rounds: int,
    review_skill_text: str,
    initial_review_feedback: str | None = None,
    consumed_review_rounds: int = 0,
    initial_draft_text: str | None = None,
    initial_draft_metadata: dict | None = None,
    log: Callable[[str], None] | None = None,
) -> GenerationResult:
    if output_path.exists() and not overwrite:
        emit_log(log, f"[skip] {output_path.name} already exists.")
        return GenerationResult(output_path=output_path, status="skipped")

    emit_log(log, f"[run] Generating {output_path.name} ...")
    try:
        call_log = None if log is None else lambda message: emit_log(log, f"[{output_path.name}] {message}")

        if not agent_review_enabled:
            content, metadata = generate_single_episode(
                episode=episode,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                log=call_log,
            )
            content = strip_storyboard_protocol_tags(content)
            content, _, normalized_changes = renumber_clean_storyboard(content)
            if normalized_changes:
                emit_log(
                    log,
                    f"[info] 自然格式编号已自动校准：{'; '.join(normalized_changes[:5])}"
                    + (" ..." if len(normalized_changes) > 5 else ""),
                )
            write_output(output_path, episode, content, metadata)
            emit_log(log, f"[done] Saved {output_path}")
            if delay_seconds > 0:
                time.sleep(delay_seconds)
            return GenerationResult(output_path=output_path, status="done")

        total_rounds = max(1, review_rounds)
        feedback: str | None = initial_review_feedback
        final_content = initial_draft_text or ""
        final_metadata: dict = initial_draft_metadata or {}
        if consumed_review_rounds >= total_rounds:
            if final_content:
                return save_needs_review_draft(
                    output_path=output_path,
                    episode=episode,
                    content=final_content,
                    metadata=final_metadata,
                    review_feedback=feedback or "已用尽回修轮次。",
                    log=log,
                    delay_seconds=delay_seconds,
                )
            raise RuntimeError(f"审核未通过：{feedback or '已用尽回修轮次。'}")
        for round_index in range(consumed_review_rounds + 1, total_rounds + 1):
            emit_log(log, f"[agent] {output_path.name} 第 {round_index} 轮生成中...")
            final_content, final_metadata = generate_single_episode(
                prompt_text=prompt_text,
                episode=episode,
                provider=provider,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                review_feedback=feedback,
                log=call_log,
            )
            final_content = strip_storyboard_protocol_tags(final_content)
            final_content, _, normalized_changes = renumber_clean_storyboard(final_content)
            if normalized_changes:
                emit_log(
                    log,
                    f"[agent] 自然格式编号已自动校准：{'; '.join(normalized_changes[:5])}"
                    + (" ..." if len(normalized_changes) > 5 else ""),
                )
            protocol_issues = validate_clean_storyboard_format(final_content)
            if protocol_issues:
                feedback = format_protocol_feedback(protocol_issues)
                emit_log(
                    log,
                    f"[agent] 格式校验未通过（第 {round_index} 轮，{len(protocol_issues)} 个问题）："
                    f"{summarize_protocol_issues(protocol_issues)}",
                )
                if round_index >= total_rounds:
                    return save_needs_review_draft(
                        output_path=output_path,
                        episode=episode,
                        content=final_content,
                        metadata=final_metadata,
                        review_feedback=feedback,
                        log=log,
                        delay_seconds=delay_seconds,
                    )
                continue
            emit_log(log, f"[agent] {output_path.name} 第 {round_index} 轮审核中...")
            try:
                decision = review_episode_draft(
                    review_skill_text=review_skill_text,
                    episode=episode,
                    draft_text=final_content,
                    provider=provider,
                    api_base=api_base,
                    api_key=api_key,
                    model=model,
                    review_thinking_enabled=review_thinking_enabled,
                    review_reasoning_effort=review_reasoning_effort,
                    temperature=temperature,
                    timeout_seconds=timeout_seconds,
                    max_tokens=max_tokens,
                    max_retries=max_retries,
                    log=call_log,
                )
            except Exception as exc:
                feedback = (
                    "审核异常，已保留当前生成稿供人工查看。\n"
                    f"异常原因：{exc}\n"
                    "建议：如果这是 JSON 解析异常，通常是审核模型返回了不严格 JSON；当前分镜稿本身已保存。"
                )
                emit_log(log, f"[warn] 审核异常，保存当前稿：{exc}")
                return save_needs_review_draft(
                    output_path=output_path,
                    episode=episode,
                    content=final_content,
                    metadata=final_metadata,
                    review_feedback=feedback,
                    log=log,
                    delay_seconds=delay_seconds,
                )
            if decision.passed:
                emit_log(log, f"[agent] 审核通过：{decision.summary}")
                if decision.warnings:
                    emit_log(
                        log,
                        f"[agent] 质检提醒（不回修）：{summarize_review_warnings(decision)}",
                    )
                    emit_review_warnings(log, decision)
                    report_path = make_review_report_path(output_path)
                    write_review_report(
                        report_path,
                        episode,
                        output_path,
                        format_review_warnings(decision),
                        status="passed_with_warnings",
                    )
                    emit_log(log, f"[agent] 质检报告：{report_path}")
                write_output(output_path, episode, final_content, final_metadata)
                emit_log(log, f"[done] Saved {output_path}")
                if delay_seconds > 0:
                    time.sleep(delay_seconds)
                return GenerationResult(output_path=output_path, status="done")
            emit_log(
                log,
                f"[agent] 审核未通过（第 {round_index} 轮，{len(decision.issues)} 个问题）："
                f"{summarize_review_issues(decision)}",
            )
            feedback = format_review_feedback(decision)
            if round_index >= total_rounds:
                return save_needs_review_draft(
                    output_path=output_path,
                    episode=episode,
                    content=final_content,
                    metadata=final_metadata,
                    review_feedback=feedback,
                    log=log,
                    delay_seconds=delay_seconds,
                )
        raise RuntimeError("agent 审核回修流程异常退出，未得到最终结果。")
    except Exception as exc:
        error_message = f"{output_path.name}: {exc}"
        emit_log(log, f"[error] {error_message}")
        return GenerationResult(output_path=output_path, status="error", error=error_message)


def write_output(
    path: Path,
    episode: EpisodeInput,
    content: str,
    metadata: dict,
) -> None:
    content = strip_storyboard_protocol_tags(content)
    usage = metadata.get("usage", {})
    finish_reason = None
    response_model = metadata.get("model")
    choices = metadata.get("choices", [])
    if choices:
        finish_reason = choices[0].get("finish_reason")

    header = [
        f"# Source: {episode.source_path.name}",
        f"# Title: {episode.display_name}",
    ]
    if response_model:
        header.append(f"# Model: {response_model}")
    if episode.episode_number is not None:
        header.append(f"# Episode: {episode.episode_number}")
    if finish_reason:
        header.append(f"# Finish Reason: {finish_reason}")
    if usage:
        header.append(
            "# Usage: "
            f"prompt_tokens={usage.get('prompt_tokens')} "
            f"completion_tokens={usage.get('completion_tokens')} "
            f"total_tokens={usage.get('total_tokens')}"
        )

    path.write_text("\n".join(header) + "\n\n" + content.strip() + "\n", encoding="utf-8")


def make_review_report_path(output_path: Path) -> Path:
    return output_path.with_name(f"{output_path.stem}.review.txt")


def write_review_report(
    path: Path,
    episode: EpisodeInput,
    output_path: Path,
    review_feedback: str,
    status: str = "needs_review",
) -> None:
    header = [
        f"# Source: {episode.source_path.name}",
        f"# Title: {episode.display_name}",
        f"# Output: {output_path.name}",
        f"# Review Status: {status}",
    ]
    if episode.episode_number is not None:
        header.append(f"# Episode: {episode.episode_number}")
    path.write_text("\n".join(header) + "\n\n" + review_feedback.strip() + "\n", encoding="utf-8")


def save_needs_review_draft(
    *,
    output_path: Path,
    episode: EpisodeInput,
    content: str,
    metadata: dict,
    review_feedback: str,
    log: Callable[[str], None] | None,
    delay_seconds: float,
) -> GenerationResult:
    report_path = make_review_report_path(output_path)
    write_output(output_path, episode, content, metadata)
    write_review_report(report_path, episode, output_path, review_feedback)
    emit_log(log, f"[warn] 审核未通过，已保存当前稿：{output_path}")
    emit_log(log, f"[warn] 审核报告：{report_path}")
    if delay_seconds > 0:
        time.sleep(delay_seconds)
    return GenerationResult(output_path=output_path, status="needs_review")


def run_batch_generation(
    *,
    episodes: list[EpisodeInput],
    prompt_text: str,
    out_dir: Path,
    provider: str,
    api_base: str,
    api_key: str,
    model: str,
    generation_thinking_enabled: bool,
    review_thinking_enabled: bool,
    generation_reasoning_effort: str,
    review_reasoning_effort: str,
    temperature: float,
    timeout_seconds: int,
    max_tokens: int,
    max_retries: int,
    delay_seconds: float,
    overwrite: bool,
    parallelism: int,
    episodes_per_request: int = DEFAULT_EPISODES_PER_REQUEST,
    agent_review_enabled: bool = False,
    stable_segment_mode: bool = DEFAULT_STABLE_SEGMENT_MODE,
    review_rounds: int = DEFAULT_AGENT_REVIEW_ROUNDS,
    review_skill_text: str = DEFAULT_REVIEW_SKILL_TEXT,
    log: Callable[[str], None] | None = None,
    on_progress: Callable[[int, int], None] | None = None,
) -> None:
    worker_count = max(1, parallelism)
    episode_jobs = build_episode_jobs(out_dir, episodes, model)
    effective_episodes_per_request = resolve_effective_episodes_per_request(
        episodes_per_request,
        agent_review_enabled,
    )
    if agent_review_enabled and episodes_per_request != effective_episodes_per_request:
        emit_log(
            log,
            "[info] Agent审核回修已启用，自动按单集请求执行；如需多集打包，请关闭 Agent审核回修。",
        )
    request_batches = build_request_batches(episode_jobs, effective_episodes_per_request)
    total = len(episode_jobs)
    completed = 0
    failures: list[str] = []

    def finish_job(result: BatchGenerationResult) -> None:
        nonlocal completed
        completed += result.completed_count
        failures.extend(result.errors)
        if on_progress:
            on_progress(completed, total)

    if worker_count == 1 or len(request_batches) <= 1:
        for batch_job in request_batches:
            result = generate_episode_batch(
                batch_job=batch_job,
                provider=provider,
                prompt_text=prompt_text,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                delay_seconds=delay_seconds,
                overwrite=overwrite,
                agent_review_enabled=agent_review_enabled,
                stable_segment_mode=stable_segment_mode,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                log=log,
            )
            finish_job(result)
    else:
        with ThreadPoolExecutor(max_workers=min(worker_count, len(request_batches))) as executor:
            future_to_job = {
                executor.submit(
                    generate_episode_batch,
                    batch_job=batch_job,
                    provider=provider,
                    prompt_text=prompt_text,
                    api_base=api_base,
                    api_key=api_key,
                    model=model,
                    generation_thinking_enabled=generation_thinking_enabled,
                    review_thinking_enabled=review_thinking_enabled,
                    generation_reasoning_effort=generation_reasoning_effort,
                    review_reasoning_effort=review_reasoning_effort,
                    temperature=temperature,
                    timeout_seconds=timeout_seconds,
                    max_tokens=max_tokens,
                    max_retries=max_retries,
                    delay_seconds=delay_seconds,
                    overwrite=overwrite,
                    agent_review_enabled=agent_review_enabled,
                    stable_segment_mode=stable_segment_mode,
                    review_rounds=review_rounds,
                    review_skill_text=review_skill_text,
                    log=log,
                ): batch_job
                for batch_job in request_batches
            }

            for future in as_completed(future_to_job):
                batch_job = future_to_job[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = BatchGenerationResult(
                        completed_count=len(batch_job.items),
                        errors=[f"Batch {batch_job.batch_index}: {exc}"],
                    )
                    emit_log(log, f"[error] Batch {batch_job.batch_index}: {exc}")
                finish_job(result)

    if failures:
        raise RuntimeError("Some episodes failed:\n" + "\n".join(failures))


def main() -> int:
    args = parse_args()
    if args.parallelism < 1:
        print("[error] --parallelism must be at least 1.", file=sys.stderr)
        return 1
    if args.episodes_per_request < 1 or args.episodes_per_request > MAX_EPISODES_PER_REQUEST:
        print(
            f"[error] --episodes-per-request must be between 1 and {MAX_EPISODES_PER_REQUEST}.",
            file=sys.stderr,
        )
        return 1
    if args.review_rounds < 1:
        print("[error] --review-rounds must be at least 1.", file=sys.stderr)
        return 1

    api_base = resolve_api_base(args.provider, args.api_base)
    model = resolve_model(args.provider, args.model)
    max_tokens = args.max_tokens
    if max_tokens is None:
        max_tokens = resolve_default_max_tokens_for_model(args.provider, model)
    review_skill_text = load_review_skill_text(args.review_skill)
    root = Path.cwd()
    prompt_path = find_prompt_file(root, args.prompt)
    prompt_text = read_utf8_text(prompt_path)
    episodes = build_episode_inputs(root, args.scripts_glob)

    if not episodes:
        print("[error] No episode script files found.", file=sys.stderr)
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)
    generation_thinking_enabled = not (args.disable_thinking or args.disable_generation_thinking)
    review_thinking_enabled = args.enable_review_thinking
    generation_reasoning_effort = normalize_reasoning_effort(args.provider, args.generation_reasoning_effort) or DEFAULT_GENERATION_REASONING_EFFORT
    review_reasoning_effort = normalize_reasoning_effort(args.provider, args.review_reasoning_effort) or DEFAULT_REVIEW_REASONING_EFFORT
    log_generation_plan(
        prompt_path=prompt_path,
        episodes=episodes,
        out_dir=args.out_dir,
        provider=args.provider,
        model=model,
        api_base=api_base,
        generation_thinking_enabled=generation_thinking_enabled,
        review_thinking_enabled=review_thinking_enabled,
        generation_reasoning_effort=generation_reasoning_effort,
        review_reasoning_effort=review_reasoning_effort,
        timeout_seconds=args.timeout_seconds,
        parallelism=args.parallelism,
        max_tokens=max_tokens,
        episodes_per_request=args.episodes_per_request,
        agent_review_enabled=args.agent_review,
        stable_segment_mode=args.stable_segments,
        review_rounds=args.review_rounds,
    )

    if args.dry_run:
        print("[info] Dry run complete. No API requests were sent.")
        return 0

    api_key = resolve_api_key(args.provider)
    if not api_key:
        print(
            f"[error] Missing {get_provider_config(args.provider)['api_key_env']} environment variable.",
            file=sys.stderr,
        )
        return 1
    validate_api_key_for_provider(args.provider, api_key)

    try:
        run_batch_generation(
            episodes=episodes,
            prompt_text=prompt_text,
            out_dir=args.out_dir,
            provider=args.provider,
            api_base=api_base,
            api_key=api_key,
            model=model,
            generation_thinking_enabled=generation_thinking_enabled,
            review_thinking_enabled=review_thinking_enabled,
            generation_reasoning_effort=generation_reasoning_effort,
            review_reasoning_effort=review_reasoning_effort,
            temperature=args.temperature,
            timeout_seconds=args.timeout_seconds,
            max_tokens=max_tokens,
            max_retries=args.max_retries,
            delay_seconds=args.delay_seconds,
            overwrite=args.overwrite,
            parallelism=args.parallelism,
            episodes_per_request=args.episodes_per_request,
            agent_review_enabled=args.agent_review,
            stable_segment_mode=args.stable_segments,
            review_rounds=args.review_rounds,
            review_skill_text=review_skill_text,
        )
    except Exception as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[done] Batch generation finished.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
