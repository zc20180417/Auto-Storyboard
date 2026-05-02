#!/usr/bin/env python3
"""Prepare and collect file-native storyboard agent workspaces.

This script does not call a model API or launch an agent CLI. It creates a
transparent file workspace that Codex, Qwen Code, or another agent can operate
on directly.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import textwrap
from datetime import datetime
from pathlib import Path

from batch_generate_storyboards import (
    EpisodeInput,
    build_episode_inputs,
    build_episode_inputs_from_paths,
    extract_episode_number,
    extract_series_title,
    find_prompt_file,
    load_review_skill_text,
    make_output_path,
    read_script_text,
    read_utf8_text,
    sanitize_filename_part,
    split_episode_collection_text,
    split_episode_into_segments,
    chinese_numeral_to_int,
)


DEFAULT_AGENT_RUNS_DIR = "agent_runs"
DEFAULT_AGENT_OUTPUT_DIR = "outputs_agent"
PROJECT_AGENT_SKILLS_DIR = "agent_skills"
AGENT_WORKSPACE_VERSION = 1


def write_utf8(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: dict) -> None:
    write_utf8(path, json.dumps(payload, ensure_ascii=False, indent=2))


def resolve_source_episodes(source: Path) -> list[EpisodeInput]:
    source = source.resolve()
    if source.is_dir():
        paths = sorted(
            path
            for pattern in ("*.docx", "*.txt")
            for path in source.glob(pattern)
            if path.is_file()
        )
        return build_episode_inputs_from_paths(paths)

    if not source.is_file():
        raise FileNotFoundError(f"source not found: {source}")

    text = read_script_text(source)
    try:
        split_episodes = split_episode_collection_text(text, source.stem)
    except ValueError:
        split_episodes = []

    if split_episodes:
        return [
            EpisodeInput(
                source_path=source,
                episode_number=item.episode_number,
                display_name=item.display_name,
                series_title=item.series_title,
                script_text=item.script_text,
            )
            for item in split_episodes
        ]

    episode_number = extract_episode_number(text, source.stem)
    return [
        EpisodeInput(
            source_path=source,
            episode_number=episode_number,
            display_name=source.stem,
            series_title=extract_series_title(source.stem),
            script_text=text,
        )
    ]


def make_episode_id(episode: EpisodeInput, sequence_index: int) -> str:
    episode_number = episode.episode_number or sequence_index
    return f"ep{episode_number:02d}"


def make_agent_context(
    *,
    project_root: Path,
    generation_rules_source: Path,
    reviewer_rules_source: Path,
    out_dir: Path,
    episodes_count: int,
    generator_skill_path: Path,
    reviewer_skill_path: Path,
    mode: str,
) -> str:
    return textwrap.dedent(
        f"""
        # Storyboard Agent Context

        ## Workspace
        - Project root: `{project_root}`
        - Generation rules source: `{generation_rules_source}`
        - Review rules source: `{reviewer_rules_source}`
        - Final output directory: `{out_dir}`
        - Episodes in this run: `{episodes_count}`
        - Generation mode: `{mode}`
        - Generation Skill: `{generator_skill_path}`
        - Review Skill: `{reviewer_skill_path}`

        ## Core Rules
        - 你是竖屏古装短剧分镜生产 agent。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准，不要在任务文件里重新解释规则。
        - 生成和审核必须在同一个 agent 会话内完成，避免“换会话越修越歪”。
        - `single` 模式：整集一次生成，再整集审核一次。
        - `scene` 模式：按场景标题拆段生成，再组装整集并审核。
        - 审核后只修硬错误；不要每次全量重写。
        - 每集最终产出 `final.txt` 和 `status.json`。
        - 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
        - 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；这次由当前 CLI agent 自己完成文本生成和审核。
        - 最终 `final.txt` 必须是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
        """
    ).strip()


def make_episode_task(
    *,
    run_dir: Path,
    episode_dir: Path,
    episode: EpisodeInput,
    episode_id: str,
    output_name: str,
    generator_skill_path: Path,
    reviewer_skill_path: Path,
    mode: str,
) -> str:
    rel_root = episode_dir.relative_to(run_dir)
    if mode == "scene":
        inputs = "- Segment scripts: `segments/seg*/script.txt`"
        outputs = textwrap.dedent(
            """
            - `segments/segXX/draft.txt`
            - `segments/segXX/review.md`
            - `segments/segXX/final.txt`
            - `final.txt`
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            """
            1. Read `../../context.md`, both standard `SKILL.md` files, `script.txt`, and each segment script.
            2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
            3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组; each group keeps its own time ranges from 0 seconds.
            4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
            5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
            6. Write `status.json` with reviewer metadata, then run validation.
            7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.
            """
        ).strip()
    else:
        inputs = "- Segment scripts: not used in `single` mode."
        outputs = textwrap.dedent(
            """
            - `final.txt`
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            """
            1. Read `../../context.md`, both standard `SKILL.md` files, and `script.txt`.
            2. Generate the full episode directly into `final.txt`.
            3. Review the full episode once using the review skill; write `review.txt`.
            4. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups.
            5. Re-run `storyboard-reviewer` after repairs and update `review.txt`.
            6. Write `status.json` with reviewer metadata, then run validation.
            7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.
            """
        ).strip()
    return f"""# Task: {episode.display_name}

Mode: `{mode}`

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `{generator_skill_path}`
- Review skill: `{reviewer_skill_path}`
- Full episode script: `script.txt`
{inputs}

## Required Outputs
{outputs}

## Workflow
{workflow}

Validation command:

```powershell
python "{Path(__file__).resolve()}" validate-episode --episode-dir "{episode_dir}"
```

`status.json` shape:

```json
{{
  "episode_id": "{episode_id}",
  "status": "done",
  "output_name": "{output_name}",
  "summary": "short Chinese summary",
  "hard_issues_remaining": [],
  "warnings": [],
  "reviewer_source": "storyboard-reviewer",
  "reviewer_pass": true,
  "reviewer_issues_count": 0,
  "reviewer_warnings_count": 0
}}
```

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `storyboard-reviewer`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.

## Important Constraints
- Rules live in the two `SKILL.md` files. Do not duplicate or reinterpret them here.
- Work only inside `{rel_root}`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
""".strip()


def make_agent_prompt(episode_dir: Path) -> str:
    return textwrap.dedent(
        f"""
        You are a storyboard production agent running inside a prepared file workspace.

        Start by reading `TASK.md`.
        Complete the task end-to-end for this episode.
        Write all required files.
        Run the validation command from `TASK.md`.
        When finished, leave the final answer concise and point to `final.txt` and `status.json`.

        Episode workspace: `{episode_dir}`
        """
    ).strip()


def make_standard_skill_md(*, name: str, description: str, title: str, body: str) -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
        f"# {title}\n\n"
        f"{body.strip()}\n"
    )


def ensure_project_agent_skills(
    *,
    project_root: Path,
    prompt_path: Path | None,
    review_skill_path: Path | None,
) -> tuple[Path, Path, Path, Path]:
    skills_root = project_root / PROJECT_AGENT_SKILLS_DIR
    generator_skill_dir = skills_root / "storyboard-generator"
    reviewer_skill_dir = skills_root / "storyboard-reviewer"
    generator_skill_dir.mkdir(parents=True, exist_ok=True)
    reviewer_skill_dir.mkdir(parents=True, exist_ok=True)

    generator_skill_path = generator_skill_dir / "SKILL.md"
    reviewer_skill_path = reviewer_skill_dir / "SKILL.md"
    if prompt_path is not None:
        prompt_text = read_utf8_text(prompt_path)
        write_utf8(
            generator_skill_path,
            make_standard_skill_md(
                name="storyboard-generator",
                description=(
                    "Generate vertical Chinese costume-drama storyboard prompts from episode scripts. "
                    "Use when converting short-drama scripts into natural grouped storyboard output."
                ),
                title="Storyboard Generator",
                body=prompt_text,
            ),
        )
        generation_rules_source = prompt_path.resolve()
    elif generator_skill_path.is_file():
        generation_rules_source = generator_skill_path.resolve()
    else:
        raise FileNotFoundError(
            f"Generation skill not found: {generator_skill_path}. "
            "Create agent_skills/storyboard-generator/SKILL.md or pass --prompt explicitly."
        )

    if review_skill_path is not None:
        review_skill_text = read_utf8_text(review_skill_path.resolve())
        write_utf8(
            reviewer_skill_path,
            make_standard_skill_md(
                name="storyboard-reviewer",
                description=(
                    "Review vertical storyboard drafts against the source script, natural format, timing, "
                    "space locking, and dialogue-direction rules. Use after storyboard generation."
                ),
                title="Storyboard Reviewer",
                body=review_skill_text,
            ),
        )
        reviewer_rules_source = review_skill_path.resolve()
    elif reviewer_skill_path.is_file():
        reviewer_rules_source = reviewer_skill_path.resolve()
    else:
        review_skill_text = load_review_skill_text(None)
        write_utf8(
            reviewer_skill_path,
            make_standard_skill_md(
                name="storyboard-reviewer",
                description=(
                    "Review vertical storyboard drafts against the source script, natural format, timing, "
                    "space locking, and dialogue-direction rules. Use after storyboard generation."
                ),
                title="Storyboard Reviewer",
                body=review_skill_text,
            ),
        )
        reviewer_rules_source = reviewer_skill_path.resolve()

    return (
        generator_skill_path.resolve(),
        reviewer_skill_path.resolve(),
        generation_rules_source,
        reviewer_rules_source,
    )


def write_runner_scripts(
    *,
    run_dir: Path,
    agent: str,
    parallelism: int,
    model: str | None,
) -> None:
    manifest = read_json(run_dir / "manifest.json")
    tasks = manifest["episodes"]

    for stale in ("run_codex_parallel.ps1", "run_qwen_parallel.ps1"):
        stale_path = run_dir / stale
        if stale_path.exists():
            stale_path.unlink()

    task_lines = []
    for task in tasks:
        task_lines.append(
            f"- `{task['episode_id']}`: open `{task['prompt_file']}` and process it as an independent episode. "
            f"Required outputs are under `{task['episode_dir']}`."
        )

    codex_model_arg = f" -m {model}" if model else ""
    sample_task = tasks[0] if tasks else None
    codex_example = ""
    qwen_example = ""
    if sample_task:
        codex_example = (
            f'codex exec --skip-git-repo-check --sandbox workspace-write --cd "{run_dir}"'
            f'{codex_model_arg} - < "{sample_task["prompt_file"]}"'
        )
        qwen_example = f'qwen < "{sample_task["prompt_file"]}"'
    tasks_markdown = "\n".join(task_lines)

    write_utf8(
        run_dir / "NEXT_STEPS.md",
        f"""# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes.
Quality is checked per episode. Dispatch can use one episode per worker, or two adjacent short/simple episodes per worker when the scripts are small.
Run up to {parallelism} workers in parallel if the host agent supports safe parallel work.
When one worker handles two episodes, finish generation, review, repair, and validation for the first episode before starting the second. Never merge reviews or outputs across episodes.

## Episode Tasks

{tasks_markdown}

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

```powershell
{codex_example}
```

Qwen example:

```powershell
{qwen_example}
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\\COLLECT_RESULTS.ps1
```
""",
    )

    write_utf8(
        run_dir / "RUN_THIS.ps1",
        textwrap.dedent(
            f"""
            $ErrorActionPreference = 'Stop'
            Write-Error "Disabled by design: Python-generated launchers do not start agent CLIs. Read NEXT_STEPS.md. To collect finished files, run .\\COLLECT_RESULTS.ps1."
            exit 2
            """
        ).strip(),
    )
    write_utf8(
        run_dir / "COLLECT_RESULTS.ps1",
        textwrap.dedent(
            f"""
            $ErrorActionPreference = 'Stop'
            python "{Path(__file__).resolve()}" collect --run-dir "{run_dir}"
            """
        ).strip(),
    )


CLEAN_GROUP_RE = re.compile(
    r"(?m)^\ufeff?\s*===\s*第(?P<num>[0-9一二三四五六七八九十百千万零〇两]+)组(?!结束)(?P<rest>.*?)$"
)
CLEAN_LEGACY_SHOT_RE = re.compile(r"(?m)^\s*(?P<group>\d{1,3})-(?P<shot>\d{1,2})(?:\s|\[|$)")
CLEAN_SHOT_TIME_RANGE_RE = re.compile(
    r"(?:时间段[：:]\s*)?(?P<start>\d{1,3})\s*[-－—–到至]\s*(?P<end>\d{1,3})\s*秒"
)
CLEAN_SHOT_TIME_RANGE_LINE_RE = re.compile(
    r"(?m)^\s*(?:时间段[：:]\s*)?(?P<start>\d{1,3})\s*[-－—–到至]\s*(?P<end>\d{1,3})\s*秒[：:]?\s*$"
)
CLEAN_SHOT_SECONDS_RE = re.compile(r"本镜估算时长[：:]\s*(?P<seconds>\d{1,3})\s*秒")
CLEAN_GROUP_TOTAL_RE = re.compile(r"总时长[：:]\s*(?P<seconds>\d{1,3})\s*秒")
CLEAN_GROUP_SHOTS_RE = re.compile(r"镜头数[：:]\s*(?P<shots>\d{1,3})\s*个")
MACHINE_TAG_RE = re.compile(r"(?m)^\ufeff?\s*<<<(?:GROUP|GROUP_END|SHOT|SHOT_END)\b.*?>>>\s*$")
LOW_QUALITY_TEMPLATE_PATTERNS = (
    "空间先被交代出来",
    "镜头从场景布局转向在场人物",
    "视线关系落在当前冲突中心",
    "人物面部肌肉随局势绷紧",
    "眉头和嘴角随情绪细微变化",
    "现场冲突继续推进",
)
SCENE_ESTABLISHING_RE = re.compile(
    # Alt 1: natural format "0-3秒：\n镜头描述：全景..." (time-before-description)
    r"(?m)^\s*(?P<start2>\d{1,3})\s*[-－—–到至]\s*(?P<end2>\d{1,3})\s*秒\s*[：:]?\s*\n"
    r"\s*镜头描述[：:][^\n]*(?:空间先被交代出来|场景布局|环境|全景|旧工业环境)"
    r"|"
    # Alt 2: original format (description-then-time)
    r"镜头描述[：:][^\n]*(?:空间先被交代出来|场景布局|环境|全景|旧工业环境)[\s\S]{0,160}?"
    r"(?:(?:时间段[：:]\s*)?(?P<start>\d{1,3})\s*[-－—–到至]\s*(?P<end>\d{1,3})\s*秒|"
    r"本镜估算时长[：:]\s*(?P<seconds>\d{1,3})\s*秒)"
)


def strip_machine_tags(content: str) -> str:
    """Remove legacy machine protocol tags from user-facing storyboard text."""
    return re.sub(r"\n{3,}", "\n\n", MACHINE_TAG_RE.sub("", content)).strip()


def normalize_clean_storyboard_numbering(content: str) -> tuple[str, list[str]]:
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content, []

    parts: list[str] = []
    changes: list[str] = []
    cursor = 0
    for index, group_match in enumerate(group_matches, start=1):
        block_start = group_match.start()
        block_end = group_matches[index].start() if index < len(group_matches) else len(content)
        old_raw = group_match.group("num")
        old_number = _group_number(old_raw)
        block = content[block_start:block_end]

        block, heading_count = re.subn(
            r"(?m)^(\s*===\s*)第[0-9一二三四五六七八九十百千万零〇两]+组",
            rf"\1第{index}组",
            block,
            count=1,
        )
        block = re.sub(
            r"(?m)^(\s*===\s*)第[0-9一二三四五六七八九十百千万零〇两]+组结束",
            rf"\1第{index}组结束",
            block,
        )

        shot_counter = 0

        def replace_shot(match: re.Match) -> str:
            nonlocal shot_counter
            shot_counter += 1
            return f"{match.group(1)}{index}-{shot_counter}{match.group(3)}"

        block = re.sub(
            r"(?m)^(\s*)\d{1,3}-(\d{1,2})(\s*(?:\[.*\])?\s*)$",
            replace_shot,
            block,
        )

        if heading_count and old_number != index:
            changes.append(f"第{old_number or old_raw}组->{index}组")
        parts.append(content[cursor:block_start])
        parts.append(block)
        cursor = block_end

    parts.append(content[cursor:])
    return "".join(parts), changes


def _group_number(value: str) -> int | None:
    if value.isdigit():
        return int(value)
    return chinese_numeral_to_int(value)


def _extract_time_range_durations(time_matches: list[re.Match]) -> tuple[list[int], list[str]]:
    durations: list[int] = []
    issues: list[str] = []
    previous_end: int | None = None

    for index, match in enumerate(time_matches):
        start = int(match.group("start"))
        end = int(match.group("end"))
        duration = end - start
        label = f"{start}-{end}秒"
        durations.append(duration)
        if duration <= 0:
            issues.append(f"{label} 时间段结束秒数必须大于开始秒数。")
        if index == 0 and start != 0:
            issues.append(f"{label} 时间段应从 0 秒开始。")
        if previous_end is not None and start != previous_end:
            issues.append(f"{label} 时间段起点={start}秒，但上一镜结束={previous_end}秒。")
        previous_end = end

    return durations, issues


def _extract_legacy_shot_durations(block: str, shot_matches: list[re.Match]) -> tuple[list[int], list[str]]:
    durations: list[int] = []
    issues: list[str] = []

    for index, shot_match in enumerate(shot_matches):
        shot_label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
        shot_start = shot_match.end()
        shot_end = shot_matches[index + 1].start() if index + 1 < len(shot_matches) else len(block)
        shot_block = block[shot_start:shot_end]

        seconds_match = CLEAN_SHOT_SECONDS_RE.search(shot_block)
        if seconds_match:
            durations.append(int(seconds_match.group("seconds")))
        else:
            issues.append(f"{shot_label} 缺少时间段，例如：0-4秒：。")

    return durations, issues


def validate_clean_storyboard_format(content: str) -> list[str]:
    issues: list[str] = []
    if MACHINE_TAG_RE.search(content):
        issues.append("最终分镜中仍包含三尖括号机器标签，请删除这些标签。")

    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return issues + ["缺少自然分镜组标题，例如：=== 第1组：...（总时长：XX秒，镜头数：X个） ==="]

    expected_group = 1
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group)
        if group_number is None:
            issues.append(f"第{expected_group}个组标题无法识别组号：{raw_group}")
            group_number = expected_group
        if group_number != expected_group:
            issues.append(f"组号不连续：期望第{expected_group}组，实际为第{group_number}组。")

        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        legacy_shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))

        if time_matches:
            seconds, time_issues = _extract_time_range_durations(time_matches)
            shot_count = len(time_matches)
        else:
            seconds, time_issues = _extract_legacy_shot_durations(block, legacy_shot_matches)
            shot_count = len(legacy_shot_matches)
        issues.extend(time_issues)
        if not time_matches and not legacy_shot_matches:
            issues.append(f"第{group_number}组缺少时间段，例如 0-4秒：。")
        if not time_matches:
            for shot_index, shot_match in enumerate(legacy_shot_matches, start=1):
                shot_group = int(shot_match.group("group"))
                shot_number = int(shot_match.group("shot"))
                if shot_group != group_number:
                    issues.append(f"第{group_number}组内出现跨组镜头编号：{shot_group}-{shot_number}。")
                if shot_number != shot_index:
                    issues.append(
                        f"第{group_number}组镜头编号不连续：期望 {group_number}-{shot_index}，实际 {shot_group}-{shot_number}。"
                    )

        if len(seconds) != shot_count:
            issues.append(
                f"第{group_number}组镜头数量与时间段数量不一致：镜头{shot_count}个，时长{len(seconds)}个。"
            )
        if any(value <= 1 for value in seconds):
            issues.append(f"第{group_number}组出现 1 秒或更短镜头。")

        total_match = CLEAN_GROUP_TOTAL_RE.search(group_match.group("rest"))
        shots_match = CLEAN_GROUP_SHOTS_RE.search(group_match.group("rest"))
        seconds_sum = sum(seconds)
        if total_match and seconds:
            declared_total = int(total_match.group("seconds"))
            if declared_total != seconds_sum:
                issues.append(f"第{group_number}组标题总时长={declared_total}秒，但镜头时长相加={seconds_sum}秒。")
        if seconds and not (10 <= seconds_sum <= 15):
            issues.append(f"第{group_number}组镜头时长相加={seconds_sum}秒，不在10-15秒范围内。")
        if shots_match:
            declared_shots = int(shots_match.group("shots"))
            if declared_shots != shot_count:
                issues.append(f"第{group_number}组标题镜头数={declared_shots}，实际镜头数={shot_count}。")

        expected_group += 1

    return issues


def validate_storyboard_quality_floor(content: str) -> list[str]:
    issues: list[str] = []
    for pattern in LOW_QUALITY_TEMPLATE_PATTERNS:
        if pattern in content:
            issues.append(f"最终分镜包含模板化镜头描述：`{pattern}`，请改为贴合剧本现场的具体动作、道具和人物站位。")
    for match in SCENE_ESTABLISHING_RE.finditer(content):
        if match.group("start2") is not None:
            seconds = int(match.group("end2")) - int(match.group("start2"))
        elif match.group("seconds"):
            seconds = int(match.group("seconds"))
        else:
            seconds = int(match.group("end")) - int(match.group("start"))
        if seconds > 3:
            issues.append(
                f"普通空间/环境交代镜头标为{seconds}秒；生产规则要求通常2秒，"
                "只有原剧本明确连续动作时才可到3秒。"
            )
    return issues


def _read_review_json(path: Path) -> tuple[dict | None, str | None]:
    if not path.is_file():
        return None, f"missing review file: {path.name}"

    raw = path.read_text(encoding="utf-8-sig", errors="replace").strip()
    if not raw:
        return None, f"empty review file: {path.name}"

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, f"{path.name} must contain raw storyboard-reviewer JSON: {exc}"

    if not isinstance(payload, dict):
        return None, f"{path.name} must contain a JSON object"

    required_types = {
        "pass": bool,
        "summary": str,
        "issues": list,
        "warnings": list,
    }
    for key, expected_type in required_types.items():
        if not isinstance(payload.get(key), expected_type):
            return None, f"{path.name} missing reviewer field `{key}` with type {expected_type.__name__}"

    summary = payload["summary"].strip()
    if not summary:
        return None, f"{path.name} reviewer summary is empty"
    placeholder_markers = (
        "占位",
        "placeholder",
        "待脚本校验",
        "客观格式",
        "clean-format",
        "clean format",
    )
    if any(marker.lower() in summary.lower() for marker in placeholder_markers):
        return None, f"{path.name} looks like a placeholder review, not storyboard-reviewer output"

    return payload, None


def _status_reviewer_metadata(status_payload: dict) -> dict | None:
    nested = status_payload.get("reviewer")
    if isinstance(nested, dict):
        return {
            "source": nested.get("source"),
            "pass": nested.get("pass"),
            "issues_count": nested.get("issues_count", nested.get("hard_issues_count")),
            "warnings_count": nested.get("warnings_count"),
        }

    if any(key in status_payload for key in ("reviewer_pass", "reviewer_issues_count", "reviewer_source")):
        return {
            "source": status_payload.get("reviewer_source"),
            "pass": status_payload.get("reviewer_pass"),
            "issues_count": status_payload.get("reviewer_issues_count"),
            "warnings_count": status_payload.get("reviewer_warnings_count"),
        }

    return None


def validate_review_artifacts(episode_dir: Path) -> list[str]:
    """Require evidence that storyboard-reviewer ran; clean format is not review."""
    issues: list[str] = []

    review_payload, review_error = _read_review_json(episode_dir / "review.txt")
    if review_error:
        issues.append(review_error)

    status_path = episode_dir / "status.json"
    status_payload: dict | None = None
    if not status_path.is_file():
        issues.append("missing status.json with reviewer metadata")
    else:
        try:
            status_payload = read_json(status_path)
        except Exception as exc:
            issues.append(f"status.json is not valid JSON: {exc}")

    if status_payload is not None:
        metadata = _status_reviewer_metadata(status_payload)
        if metadata is None:
            issues.append(
                "status.json missing reviewer metadata: add reviewer_source, "
                "reviewer_pass, reviewer_issues_count, and reviewer_warnings_count"
            )
        else:
            if metadata.get("source") != "storyboard-reviewer":
                issues.append("status.json reviewer_source must be `storyboard-reviewer`")
            if not isinstance(metadata.get("pass"), bool):
                issues.append("status.json reviewer_pass must be a boolean")
            if not isinstance(metadata.get("issues_count"), int):
                issues.append("status.json reviewer_issues_count must be an integer")
            if not isinstance(metadata.get("warnings_count"), int):
                issues.append("status.json reviewer_warnings_count must be an integer")

            if review_payload is not None:
                review_pass = review_payload["pass"]
                review_issues_count = len(review_payload["issues"])
                review_warnings_count = len(review_payload["warnings"])
                if metadata.get("pass") != review_pass:
                    issues.append("status.json reviewer_pass does not match review.txt pass")
                if metadata.get("issues_count") != review_issues_count:
                    issues.append("status.json reviewer_issues_count does not match review.txt issues length")
                if metadata.get("warnings_count") != review_warnings_count:
                    issues.append("status.json reviewer_warnings_count does not match review.txt warnings length")

                status = status_payload.get("status")
                if status == "done" and (not review_pass or review_issues_count):
                    issues.append("status.json cannot be `done` when storyboard-reviewer reports hard issues")
                if status == "done" and status_payload.get("hard_issues_remaining"):
                    issues.append("status.json cannot be `done` with hard_issues_remaining")

    segments_dir = episode_dir / "segments"
    if segments_dir.is_dir():
        for segment_dir in sorted(path for path in segments_dir.iterdir() if path.is_dir()):
            if not (segment_dir / "script.txt").is_file():
                continue
            _, segment_error = _read_review_json(segment_dir / "review.md")
            if segment_error:
                issues.append(f"{segment_dir.name}: {segment_error}")

    return issues


def prepare_workspace(args: argparse.Namespace) -> int:
    project_root = Path.cwd().resolve()
    source = args.source.resolve()
    prompt_path = find_prompt_file(project_root, args.prompt).resolve() if args.prompt else None
    episodes = resolve_source_episodes(source)
    if not episodes:
        print("[error] no episodes found", file=sys.stderr)
        return 1

    run_id = args.run_name or datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = (args.workspace_dir / run_id).resolve()
    out_dir = args.out_dir.resolve()
    if run_dir.exists() and not args.force:
        print(f"[error] run directory already exists: {run_dir}", file=sys.stderr)
        return 1
    if run_dir.exists() and args.force:
        workspace_root = args.workspace_dir.resolve()
        if run_dir == workspace_root or workspace_root not in run_dir.parents:
            print(f"[error] refusing to clear unexpected run directory: {run_dir}", file=sys.stderr)
            return 1
        shutil.rmtree(run_dir)

    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "episodes").mkdir(exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    generator_skill_path, reviewer_skill_path, generation_rules_source, reviewer_rules_source = ensure_project_agent_skills(
        project_root=project_root,
        prompt_path=prompt_path,
        review_skill_path=args.review_skill,
    )

    write_utf8(run_dir / "context.md", make_agent_context(
        project_root=project_root,
        generation_rules_source=generation_rules_source,
        reviewer_rules_source=reviewer_rules_source,
        out_dir=out_dir,
        episodes_count=len(episodes),
        generator_skill_path=generator_skill_path,
        reviewer_skill_path=reviewer_skill_path,
        mode=args.mode,
    ))
    manifest: dict = {
        "version": AGENT_WORKSPACE_VERSION,
        "run_id": run_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "project_root": str(project_root),
        "source": str(source),
        "prompt_path": str(prompt_path) if prompt_path else None,
        "generation_rules_source": str(generation_rules_source),
        "reviewer_rules_source": str(reviewer_rules_source),
        "generator_skill_path": str(generator_skill_path),
        "reviewer_skill_path": str(reviewer_skill_path),
        "out_dir": str(out_dir),
        "agent": args.agent,
        "mode": args.mode,
        "parallelism": args.parallelism,
        "episodes": [],
    }

    for index, episode in enumerate(episodes, start=1):
        episode_id = make_episode_id(episode, index)
        episode_dir = run_dir / "episodes" / episode_id
        episode_dir.mkdir(parents=True, exist_ok=True)
        output_path = make_output_path(out_dir, episode, index, model=args.output_model_suffix)

        write_utf8(episode_dir / "script.txt", episode.script_text)
        episode_meta = {
            "episode_id": episode_id,
            "episode_number": episode.episode_number,
            "display_name": episode.display_name,
            "series_title": episode.series_title,
            "source_path": str(episode.source_path),
            "output_path": str(output_path),
        }
        write_json(episode_dir / "episode.json", episode_meta)

        segments = []
        if args.mode == "scene":
            segments_dir = episode_dir / "segments"
            segments_dir.mkdir(exist_ok=True)
            segments = split_episode_into_segments(episode)
            for segment in segments:
                seg_dir = segments_dir / f"seg{segment.index:02d}"
                seg_dir.mkdir(exist_ok=True)
                write_utf8(seg_dir / "script.txt", segment.script_text)
                write_json(
                    seg_dir / "segment.json",
                    {
                        "index": segment.index,
                        "total": segment.total,
                        "title": segment.title,
                    },
                )

        task_text = make_episode_task(
            run_dir=run_dir,
            episode_dir=episode_dir,
            episode=episode,
            episode_id=episode_id,
            output_name=output_path.name,
            generator_skill_path=generator_skill_path,
            reviewer_skill_path=reviewer_skill_path,
            mode=args.mode,
        )
        write_utf8(episode_dir / "TASK.md", task_text)
        prompt_file = episode_dir / "agent_prompt.md"
        write_utf8(prompt_file, make_agent_prompt(episode_dir))

        manifest["episodes"].append(
            {
                **episode_meta,
                "episode_dir": str(episode_dir),
                "task_file": str(episode_dir / "TASK.md"),
                "prompt_file": str(prompt_file),
                "last_message_file": str(episode_dir / "agent-last-message.txt"),
                "agent_log_file": str(episode_dir / "agent-stdout.log"),
                "segments": len(segments),
            }
        )

    write_json(run_dir / "manifest.json", manifest)
    write_utf8(
        run_dir / "AGENTS.md",
        textwrap.dedent(
            """
            # Storyboard Agent Run Instructions

            This directory is an agent-native workspace. Each `episodes/epXX` folder is an independent task.

            Agents must:
            - Read the task files instead of relying on hidden state.
            - Write durable outputs to files.
            - Run validation before marking a task done.
            - Preserve drafts and review notes even when the final status is `needs_review`.
            """
        ).strip(),
    )
    write_runner_scripts(run_dir=run_dir, agent=args.agent, parallelism=args.parallelism, model=args.model)

    print(f"[done] agent workspace: {run_dir}")
    print(f"[next] read: {run_dir / 'NEXT_STEPS.md'}")
    print("[next] dispatch episode agents outside Python; then run .\\COLLECT_RESULTS.ps1")
    return 0


def validate_episode(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    final_path = episode_dir / "final.txt"
    if not final_path.is_file():
        print(f"[error] final.txt not found: {final_path}", file=sys.stderr)
        return 1

    content = final_path.read_text(encoding="utf-8", errors="replace")
    if args.fix_metadata:
        fix_messages: list[str] = []
        cleaned = strip_machine_tags(content)
        if cleaned != content:
            content = cleaned
            fix_messages.append("removed legacy machine tags")
        content, numbering_changes = normalize_clean_storyboard_numbering(content)
        if numbering_changes:
            fix_messages.append("renumbered " + "; ".join(numbering_changes[:8]))
        if fix_messages:
            write_utf8(final_path, content)
            print("[fixed] " + " | ".join(fix_messages))

    clean_issues = validate_clean_storyboard_format(content)
    quality_issues = validate_storyboard_quality_floor(content)
    review_issues = validate_review_artifacts(episode_dir)
    issues = clean_issues + quality_issues + review_issues
    report_lines = ["# Episode Validation", ""]
    if issues:
        report_lines.append("status: failed")
        report_lines.append("")
        if clean_issues:
            report_lines.append("## Clean Format")
            report_lines.extend(f"- {issue}" for issue in clean_issues)
            report_lines.append("")
        if quality_issues:
            report_lines.append("## Quality Floor")
            report_lines.extend(f"- {issue}" for issue in quality_issues)
            report_lines.append("")
        if review_issues:
            report_lines.append("## Storyboard Reviewer Evidence")
            report_lines.extend(f"- {issue}" for issue in review_issues)
        write_utf8(episode_dir / "protocol_report.md", "\n".join(report_lines))
        print(f"[failed] {len(issues)} validation issue(s)")
        for issue in issues:
            print(f"- {issue}")
        return 1

    report_lines.append("status: passed")
    report_lines.append("")
    report_lines.append("- clean_format: passed")
    report_lines.append("- quality_floor: passed")
    report_lines.append("- storyboard_reviewer: passed")
    write_utf8(episode_dir / "protocol_report.md", "\n".join(report_lines))
    print("[passed] episode validation")
    return 0


def collect_run(args: argparse.Namespace) -> int:
    run_dir = args.run_dir.resolve()
    manifest = read_json(run_dir / "manifest.json")
    out_dir = Path(manifest["out_dir"]).resolve()
    if args.out_dir:
        out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    summary_lines = ["# Agent Run Summary", ""]
    copied = 0
    failed = 0
    for item in manifest["episodes"]:
        episode_dir = Path(item["episode_dir"])
        final_path = episode_dir / "final.txt"
        status_path = episode_dir / "status.json"
        output_path = out_dir / Path(item["output_path"]).name
        summary_lines.append(f"## {item['episode_id']} {item['display_name']}")
        if not final_path.is_file():
            failed += 1
            summary_lines.append("- status: missing final.txt")
            summary_lines.append("")
            continue

        content = strip_machine_tags(final_path.read_text(encoding="utf-8", errors="replace"))
        content, changes = normalize_clean_storyboard_numbering(content)
        clean_issues = validate_clean_storyboard_format(content)
        quality_issues = validate_storyboard_quality_floor(content)
        review_issues = validate_review_artifacts(episode_dir)
        issues = clean_issues + quality_issues + review_issues
        write_utf8(output_path, content)
        copied += 1
        status = "unknown"
        if status_path.is_file():
            try:
                status = read_json(status_path).get("status", "unknown")
            except Exception:
                status = "invalid status.json"
        if issues:
            failed += 1
            summary_lines.append(f"- status: {status}, validation_failed")
            summary_lines.extend(f"- clean_format: {issue}" for issue in clean_issues[:8])
            summary_lines.extend(f"- quality_floor: {issue}" for issue in quality_issues[:8])
            summary_lines.extend(f"- storyboard_reviewer: {issue}" for issue in review_issues[:8])
        else:
            summary_lines.append(f"- status: {status}, clean_format_passed, quality_floor_passed, storyboard_reviewer_passed")
        if changes:
            summary_lines.append(f"- clean_numbering_fixed: {'; '.join(changes[:8])}")
        summary_lines.append(f"- copied: `{output_path}`")
        summary_lines.append("")

    summary_lines.append(f"Copied: {copied}")
    summary_lines.append(f"Validation/collection failures: {failed}")
    write_utf8(run_dir / "SUMMARY.md", "\n".join(summary_lines))
    print(f"[done] copied {copied} final file(s) to {out_dir}")
    print(f"[summary] {run_dir / 'SUMMARY.md'}")
    return 1 if failed else 0


def run_workspace(args: argparse.Namespace) -> int:
    print(
        "[error] disabled by design: Python must not launch agent CLIs. "
        "Open NEXT_STEPS.md and dispatch agents directly; use collect afterward.",
        file=sys.stderr,
    )
    return 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare/collect CLI-agent storyboard workspaces.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Create a file-native agent workspace.")
    prepare.add_argument("--source", type=Path, required=True, help="Script file, collection docx, or directory.")
    prepare.add_argument("--prompt", type=Path, default=None, help="Generation prompt file.")
    prepare.add_argument("--review-skill", type=Path, default=None, help="Review skill file.")
    prepare.add_argument("--workspace-dir", type=Path, default=Path(DEFAULT_AGENT_RUNS_DIR))
    prepare.add_argument("--out-dir", type=Path, default=Path(DEFAULT_AGENT_OUTPUT_DIR))
    prepare.add_argument("--run-name", default=None)
    prepare.add_argument("--agent", choices=["codex", "qwen"], default="codex")
    prepare.add_argument("--model", default=None, help="Optional CLI model override.")
    prepare.add_argument("--output-model-suffix", default="agent-cli")
    prepare.add_argument("--parallelism", type=int, default=3)
    prepare.add_argument(
        "--mode",
        choices=["single", "scene"],
        default="single",
        help="single=generate/review a full episode; scene=split by scene and assemble.",
    )
    prepare.add_argument("--force", action="store_true")
    prepare.set_defaults(func=prepare_workspace)

    validate = subparsers.add_parser("validate-episode", help="Validate one episode final.txt.")
    validate.add_argument("--episode-dir", type=Path, required=True)
    validate.add_argument("--fix-metadata", action="store_true")
    validate.set_defaults(func=validate_episode)

    collect = subparsers.add_parser("collect", help="Collect final files from an agent run.")
    collect.add_argument("--run-dir", type=Path, required=True)
    collect.add_argument("--out-dir", type=Path, default=None)
    collect.set_defaults(func=collect_run)

    run = subparsers.add_parser("run", help="Disabled: Python does not launch agent CLIs.")
    run.add_argument("--run-dir", type=Path, required=True)
    run.set_defaults(func=run_workspace)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
