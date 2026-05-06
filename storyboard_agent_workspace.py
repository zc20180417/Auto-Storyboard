#!/usr/bin/env python3
"""Prepare and collect file-native storyboard agent workspaces.

This script does not call a model API or launch an agent CLI. It creates a
transparent file workspace that Codex, Qwen Code, or another agent can operate
on directly.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import sys
import textwrap
import zipfile
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

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


def episode_id_for_cut_contract(episode_dir: Path) -> str:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
            raw = str(meta.get("episode_id") or episode_dir.name)
        except Exception:
            raw = episode_dir.name
    else:
        raw = episode_dir.name

    match = re.search(r"(\d+)", raw)
    if match:
        return f"EP{int(match.group(1)):02d}"
    return re.sub(r"[^A-Za-z0-9_-]+", "_", raw).strip("_").upper()


def _desired_cut_id(episode_id: str, group_index: int) -> str:
    return f"{episode_id}-G{group_index:02d}"


def _ensure_heading_cut_id(heading: str, desired_cut_id: str) -> str:
    if CUT_ID_RE.search(heading):
        return CUT_ID_RE.sub(f"cut_id：{desired_cut_id}", heading, count=1)

    if "（" in heading:
        return heading.replace("（", f"（cut_id：{desired_cut_id}，", 1)
    if "(" in heading:
        return heading.replace("(", f"(cut_id: {desired_cut_id}, ", 1)
    return re.sub(r"\s*===\s*$", f"（cut_id：{desired_cut_id}） ===", heading, count=1)


def ensure_storyboard_cut_ids(content: str, episode_id: str) -> tuple[str, list[str]]:
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content, []

    parts: list[str] = []
    changes: list[str] = []
    cursor = 0
    for index, group_match in enumerate(group_matches, start=1):
        heading = group_match.group(0)
        desired_cut_id = _desired_cut_id(episode_id, index)
        updated_heading = _ensure_heading_cut_id(heading, desired_cut_id)
        parts.append(content[cursor:group_match.start()])
        parts.append(updated_heading)
        cursor = group_match.end()
        if updated_heading != heading:
            changes.append(f"第{index}组->{desired_cut_id}")

    parts.append(content[cursor:])
    return "".join(parts), changes


def validate_storyboard_cut_ids(content: str, episode_id: str) -> list[str]:
    issues: list[str] = []
    seen: set[str] = set()
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches, start=1):
        heading = group_match.group(0)
        cut_match = CUT_ID_RE.search(heading)
        desired = _desired_cut_id(episode_id, index)
        if not cut_match:
            issues.append(f"第{index}组缺少 cut_id；应为 {desired}。")
            continue
        cut_id = cut_match.group("cut_id")
        if cut_id != desired:
            issues.append(f"第{index}组 cut_id={cut_id}，应为 {desired}。")
        if cut_id in seen:
            issues.append(f"cut_id 重复：{cut_id}。")
        seen.add(cut_id)
    return issues


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
        - dispatcher 不生成、不审核、不修稿；dispatcher 只创建 subagents/workers 并分发 episode prompt。
        - episode worker 是竖屏短剧分镜生产 agent，只处理自己被分配的单个 episode。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准，不要在任务文件里重新解释规则。
        - episode worker 可以生成和初审，但 `review.txt` 必须按 `storyboard-reviewer/SKILL.md` 逐项审稿，不能写空泛通过。
        - 若用户要求强审核模式，reviewer-only worker 必须独立复审 `final.txt`。
        - `single` 模式：整集一次生成，再整集审核一次。
        - `scene` 模式：按场景标题拆段生成，再组装整集并审核。
        - 审核后只修硬错误；不要每次全量重写。
        - 每集最终产出 `final.txt` 和 `status.json`。
        - 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
        - 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；Python 只准备、校验和收集。
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
            - `storyboard_index.json`
            - `storyboard_index.xlsx`
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            """
            1. Read `../../context.md`, both standard `SKILL.md` files, `script.txt`, and each segment script.
            2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
            3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组; each group keeps its own time ranges from 0 seconds. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== 第1组：标题（cut_id：EP02-G01，总时长：12秒，镜头数：4个） ===`.
            4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
            5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
            6. Write `status.json` with reviewer metadata, then run validation. Validation exports `storyboard_index.json` and `storyboard_index.xlsx` from `final.txt`.
            7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.
            """
        ).strip()
    else:
        inputs = "- Segment scripts: not used in `single` mode."
        outputs = textwrap.dedent(
            """
            - `final.txt`
            - `storyboard_index.json`
            - `storyboard_index.xlsx`
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            """
            1. Read `../../context.md`, both standard `SKILL.md` files, and `script.txt`.
            2. Generate the full episode directly into `final.txt`. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== 第1组：标题（cut_id：EP02-G01，总时长：12秒，镜头数：4个） ===`.
            3. Review the full episode once using the review skill; write `review.txt`.
            4. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups.
            5. Re-run `storyboard-reviewer` after repairs and update `review.txt`.
            6. Write `status.json` with reviewer metadata, then run validation. Validation exports `storyboard_index.json` and `storyboard_index.xlsx` from `final.txt`.
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

`status.json` requirements:

- `episode_id`: `{episode_id}`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `{output_name}`
- `summary`: short Chinese summary
- `hard_issues_remaining`: copy unresolved hard issues from the real reviewer result
- `warnings`: copy or summarize warnings from the real reviewer result
- `reviewer_source`: must be `storyboard-reviewer`
- `reviewer_pass`: copy the boolean `pass` from `review.txt` after `review.txt` exists
- `reviewer_issues_count`: copy `len(review.txt.issues)` after `review.txt` exists
- `reviewer_warnings_count`: copy `len(review.txt.warnings)` after `review.txt` exists

Do not prefill `reviewer_pass=true` or issue/warning counts before writing the real `review.txt`.

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `storyboard-reviewer`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.
Reviewer JSON must include non-empty `checked_groups` and full `audit_coverage` fields as required by `storyboard-reviewer/SKILL.md`.
Reviewer JSON must also include at least 3 `spot_checks` items with `group`, `type`, and `evidence`.
Reviewer JSON must include at least 3 `semantic_checks` items with `group`, `type`, `result`, `evidence`, and `fix_instruction`; this is the reviewer semantic audit record, not a substitute for fixing hard issues.
`status.json` reviewer fields must stay consistent with `review.txt`.
`final.txt` cut_id contract:

- Every group heading must include exactly one `cut_id`.
- Use the current episode id and group number: `EP01-G01`, `EP01-G02`, ... for ep01; `EP30-G01`, ... for ep30.
- Do not put asset IDs in `final.txt`; asset binding belongs to the asset extraction stage.

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
    initial_worker_lines = []
    pending_prompt_lines = []
    for index, task in enumerate(tasks, start=1):
        task_lines.append(
            f"- `{task['episode_id']}`: dispatch `{task['prompt_file']}` to one worker. "
            f"Worker writes only under `{task['episode_dir']}`."
        )
        pending_prompt_lines.append(f"- `{task['prompt_file']}`")
        if index <= parallelism:
            initial_worker_lines.append(f"- worker {index}: `{task['prompt_file']}`")

    codex_model_arg = f" -m {model}" if model else ""
    sample_task = tasks[0] if tasks else None
    codex_example = ""
    qwen_example = ""
    kimi_example = ""
    if sample_task:
        codex_example = (
            f'codex exec --skip-git-repo-check --sandbox workspace-write --cd "{run_dir}"'
            f'{codex_model_arg} - < "{sample_task["prompt_file"]}"'
        )
        qwen_example = f'qwen < "{sample_task["prompt_file"]}"'
        kimi_example = (
            f'Open Kimi Code in the workspace and use the Agent tool with the prompt '
            f'from `{sample_task["prompt_file"]}`.'
        )
    tasks_markdown = "\n".join(task_lines)

    if agent == "kimi":
        worker_capability = "Kimi Code Agent tools"
    elif agent == "qwen":
        worker_capability = "Qwen worker/subagent tools"
    else:
        worker_capability = "Codex subagents/workers"

    manual_cli_blocks = []
    if codex_example:
        manual_cli_blocks.append(f"Codex example:\n\n```powershell\n{codex_example}\n```")
    if qwen_example:
        manual_cli_blocks.append(f"Qwen example:\n\n```powershell\n{qwen_example}\n```")
    if agent == "kimi" and kimi_example:
        manual_cli_blocks.append(f"Kimi Code example:\n\n{kimi_example}")
    manual_cli_section = "\n\n".join(manual_cli_blocks)

    write_utf8(
        run_dir / "NEXT_STEPS.md",
        f"""# Dispatcher Instructions

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, Kimi Code, or any model process.

Do not treat this file as a production task list.
Give `DISPATCH_PROMPT.md` to the host agent. The host agent is a dispatcher only and must not write episode files itself.

## Hard Stop

- Main thread is the dispatcher, not a storyboard production worker.
- Main thread must not directly process any episode.
- Main thread must not open `episodes/ep*/script.txt` and start writing storyboard content.
- Main thread must not write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
- Main thread's only job is to create subagents/workers and dispatch episode prompts.
- If the current environment cannot create subagents/workers, or needs user authorization before creating them, immediately stop and reply `NEED_USER_DISPATCH` with the pending prompt list.
- Do not downgrade to sequential main-thread episode processing.

## Required Dispatch

Use {worker_capability}.
Run up to {parallelism} workers in parallel.
Default to one episode per worker.
Use two episodes per worker only for short/simple episodes and only after explicit user approval.
When one worker handles two episodes, it must fully finish generation, review, repair, and validation for the first episode before starting the second.
Never merge reviews or outputs across episodes.

Initial worker wave:

{chr(10).join(initial_worker_lines) if initial_worker_lines else "- No episodes found."}

When any worker finishes, dispatch the next unfinished episode prompt.

## Episode Tasks

{tasks_markdown}

## Pending Prompt List

{chr(10).join(pending_prompt_lines) if pending_prompt_lines else "- No episodes found."}

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

{manual_cli_section}

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\\COLLECT_RESULTS.ps1
```
""",
    )

    write_utf8(
        run_dir / "DISPATCH_PROMPT.md",
        f"""# Auto-Storyboard Dispatcher Prompt

You are the dispatcher, not a storyboard production worker.

Your only tasks:
1. Read this file.
2. Create subagents/workers for the episode prompts below.
3. Wait for workers to finish, then run collection and summary checks.

## Absolute Prohibitions

- Do not directly generate any storyboard body in the main thread.
- Do not process `ep01`, `ep02`, `ep03`, or any other episode in the main thread.
- Do not open `episodes/ep*/script.txt` and begin production work.
- Do not write `episodes/ep*/draft.txt`, `episodes/ep*/final.txt`, `episodes/ep*/review.txt`, or `episodes/ep*/status.json` from the main thread.
- Do not sequentially process all episodes yourself.
- If you cannot create subagents/workers, immediately output `NEED_USER_DISPATCH` and list the prompt paths below.
- Do not downgrade to sequential main-thread episode processing.

## Worker Dispatch

Use {worker_capability}.
Run up to {parallelism} workers in parallel.
Default to one episode per worker.
Use two episodes per worker only for short/simple episodes and only after explicit user approval.
When one worker handles two episodes, it must complete the first episode's generation, real review, hard-issue repair, re-review, and validation before starting the second.

Initial worker wave:

{chr(10).join(initial_worker_lines) if initial_worker_lines else "- No episodes found."}

All episode prompts:

{chr(10).join(pending_prompt_lines) if pending_prompt_lines else "- No episodes found."}

## After Workers Finish

After workers finish writing `final.txt`, `review.txt`, and `status.json` in each episode directory, run:

```powershell
.\\COLLECT_RESULTS.ps1
```

If any episode is unfinished or validation fails, dispatch only that episode's `agent_prompt.md` to a worker for focused repair.
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
    r"(?m)^\ufeff?\s*===\s*(?:\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*)?"
    r"第(?P<num>[0-9一二三四五六七八九十百千万零〇两]+)组(?!结束)(?P<rest>.*?)$"
)
CUT_ID_RE = re.compile(r"cut_id\s*[:：]\s*(?P<cut_id>[A-Z0-9_-]+)")
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
REQUIRED_AUDIT_COVERAGE_KEYS = (
    "script_fidelity",
    "dialogue_direction",
    "timing_math",
    "dialogue_pacing",
    "space_locking",
    "format",
    "character_availability",
    "handoff_continuity",
    "filmability",
)
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
DIALOGUE_QUOTE_RE = re.compile(r"[“\"]([^”\"]+)[”\"]")
DIALOGUE_PUNCT_RE = re.compile(r"[，。！？、；：,.!?;:\s“”\"'（）()《》【】\[\]—…]")
EMOTIONAL_DIALOGUE_MARKERS = (
    "喊",
    "怒",
    "吼",
    "质问",
    "反问",
    "哭",
    "哭喊",
    "哽咽",
    "发飙",
    "崩溃",
    "冷笑",
    "讥讽",
    "咬牙",
    "厉声",
    "急切",
    "急促",
    "紧急",
    "反讽",
    "嘲讽",
    "爽点",
)
SLOW_DIALOGUE_MARKERS = (
    "缓慢",
    "停顿",
    "哽咽",
    "一字一顿",
    "虚弱",
    "无力",
    "低声艰难",
    "气若游丝",
    "喘着气",
)
NECESSARY_LONG_ACTION_MARKERS = (
    "走到",
    "跑到",
    "冲到",
    "穿过",
    "翻过",
    "爬到",
    "蹲下",
    "跪下",
    "站起身",
    "坐下",
    "转身离开",
    "推开门",
    "抱起",
    "放下",
    "搬起",
    "拖着",
    "背起",
)
AUTO_MULTISHOT_MARKERS = (
    "连续短句交锋",
    "连续对话节拍",
    "快速短句交锋",
    "短促交锋",
    "快速问答",
    "来回对话",
)
MODEL_META_PROMPT_PATTERNS = (
    "Seedance 可",
    "由 Seedance",
    "Seedance 自动",
    "Seedance自动",
    "自动正反打",
    "自动分镜",
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


def _effective_dialogue_chars(text: str) -> int:
    quoted = "".join(DIALOGUE_QUOTE_RE.findall(text))
    return len(DIALOGUE_PUNCT_RE.sub("", quoted))


def _has_any_marker(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def _iter_storyboard_shots(content: str) -> list[tuple[int | None, str, int, str]]:
    shots: list[tuple[int | None, str, int, str]] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches):
        group_number = _group_number(group_match.group("num"))
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        if time_matches:
            for shot_index, time_match in enumerate(time_matches):
                start = int(time_match.group("start"))
                end = int(time_match.group("end"))
                shot_start = time_match.end()
                shot_end = time_matches[shot_index + 1].start() if shot_index + 1 < len(time_matches) else len(block)
                label = f"第{group_number or '?'}组 {start}-{end}秒"
                shots.append((group_number, label, end - start, block[shot_start:shot_end]))
            continue

        legacy_shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))
        for shot_index, shot_match in enumerate(legacy_shot_matches):
            shot_label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
            shot_start = shot_match.end()
            shot_end = legacy_shot_matches[shot_index + 1].start() if shot_index + 1 < len(legacy_shot_matches) else len(block)
            shot_block = block[shot_start:shot_end]
            seconds_match = CLEAN_SHOT_SECONDS_RE.search(shot_block)
            if seconds_match:
                shots.append((group_number, shot_label, int(seconds_match.group("seconds")), shot_block))

    return shots


def validate_dialogue_pacing_floor(content: str) -> list[str]:
    issues: list[str] = []
    for _group_number, shot_label, seconds, shot_text in _iter_storyboard_shots(content):
        if seconds <= 0:
            continue

        chars = _effective_dialogue_chars(shot_text)
        if chars == 0:
            continue

        cps = chars / seconds
        is_emotional = _has_any_marker(shot_text, EMOTIONAL_DIALOGUE_MARKERS)
        is_slow = _has_any_marker(shot_text, SLOW_DIALOGUE_MARKERS)
        has_necessary_action = _has_any_marker(shot_text, NECESSARY_LONG_ACTION_MARKERS)
        is_auto_multishot = _has_any_marker(shot_text, AUTO_MULTISHOT_MARKERS)
        target_speed = 3.8 if is_slow else (5.2 if is_emotional else 4.5)
        target_seconds = math.ceil(chars / target_speed)

        if is_auto_multishot:
            dialogue_turns = len(DIALOGUE_QUOTE_RE.findall(shot_text))
            speaker_switches = max(0, dialogue_turns - 1)
            switch_gap = 0.3 if is_emotional else 0.4
            action_extra = 1 if has_necessary_action else 0
            block_target_seconds = math.ceil(chars / target_speed + speaker_switches * switch_gap + action_extra)
            if seconds > block_target_seconds + 1 and not is_slow:
                issues.append(
                    f"{shot_label} 连续对话节拍时长偏长；有效字数 {chars}，"
                    f"台词轮次 {dialogue_turns}，镜头 {seconds} 秒，字秒比 {cps:.1f}。"
                    f"请按整块台词量、换人间隙和必要动作压到约 {block_target_seconds} 秒，"
                    "或合并相邻同场景冲突内容，不要拉慢短句凑时长。"
                )
            continue

        if seconds >= 9 and not (is_slow or has_necessary_action):
            issues.append(
                f"{shot_label} 有台词镜头 {seconds} 秒过长；有效字数 {chars}，字秒比 {cps:.1f}。"
                "除非原剧本明确慢语或必要长动作，否则 ≥9 秒台词镜头应拆成正反打、反应镜头或画外音反打。"
            )
            continue

        # Tiny acknowledgements like “好” or “知道了” often ride on the action beat.
        # Keep the deterministic slow-dialogue gate focused on substantive dialogue.
        if chars < 12:
            continue

        min_cps = 4.5 if is_emotional else 3.8
        if cps < min_cps and not is_slow and not (has_necessary_action and not is_emotional):
            issues.append(
                f"{shot_label} 台词节奏偏慢；有效字数 {chars}，镜头 {seconds} 秒，字秒比 {cps:.1f}，"
                f"低于 {min_cps:.1f} 字/秒。请缩短到约 {target_seconds} 秒，或拆成正反打/反应镜头承载。"
            )

    return issues


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
    for pattern in MODEL_META_PROMPT_PATTERNS:
        if pattern in content:
            issues.append(
                f"最终分镜正文包含模型说明词 `{pattern}`，应改成自然画面描述，"
                "不要在 prompt 中指挥 Seedance 自动分镜。"
            )
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
    issues.extend(validate_dialogue_pacing_floor(content))
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
        "checked_groups": list,
        "audit_coverage": dict,
        "spot_checks": list,
        "semantic_checks": list,
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

    checked_groups = payload["checked_groups"]
    if not checked_groups or not all(isinstance(item, str) and item.strip() for item in checked_groups):
        return None, f"{path.name} missing non-empty checked_groups list"

    audit_coverage = payload["audit_coverage"]
    for key in REQUIRED_AUDIT_COVERAGE_KEYS:
        if audit_coverage.get(key) != "checked":
            return None, f"{path.name} audit_coverage missing `{key}`"

    spot_checks = payload["spot_checks"]
    if len(spot_checks) < 3:
        return None, f"{path.name} must include at least 3 reviewer spot_checks"
    for index, item in enumerate(spot_checks, start=1):
        if not isinstance(item, dict):
            return None, f"{path.name} spot_checks[{index}] must be an object"
        if not item.get("group") or not item.get("type") or not item.get("evidence"):
            return None, f"{path.name} spot_checks[{index}] missing group/type/evidence"

    semantic_checks = payload["semantic_checks"]
    if len(semantic_checks) < 3:
        return None, f"{path.name} must include at least 3 reviewer semantic_checks"
    for index, item in enumerate(semantic_checks, start=1):
        if not isinstance(item, dict):
            return None, f"{path.name} semantic_checks[{index}] must be an object"
        for key in ("group", "type", "result", "evidence", "fix_instruction"):
            if not item.get(key):
                return None, f"{path.name} semantic_checks[{index}] missing {key}"

    return payload, None


def _storyboard_review_passed(payload: dict | None) -> bool:
    return (
        payload is not None
        and payload.get("pass") is True
        and isinstance(payload.get("issues"), list)
        and len(payload["issues"]) == 0
    )


def _storyboard_group_labels(content: str) -> list[str]:
    labels: list[str] = []
    for group_match in CLEAN_GROUP_RE.finditer(content):
        group_number = _group_number(group_match.group("num"))
        if group_number is not None:
            labels.append(f"第{group_number}组")
    return labels


def _split_list_field(value: str) -> list[str]:
    value = value.strip()
    if not value or value in {"无", "无明确"}:
        return []
    return [
        item.strip()
        for item in re.split(r"[、,，/]+", value)
        if item.strip()
    ]


def _extract_bold_meta(block: str, label: str) -> list[str] | str:
    pattern = re.compile(rf"(?m)^\s*\*\*{re.escape(label)}\*\*\s*[：:]\s*(?P<value>.+?)\s*$")
    match = pattern.search(block)
    if not match:
        return [] if label in {"人物", "道具"} else ""
    value = match.group("value").strip()
    if label in {"人物", "道具"}:
        return _split_list_field(value)
    return value


def _extract_group_title(heading_rest: str) -> str:
    rest = re.sub(r"===\s*$", "", heading_rest).strip()
    rest = CUT_ID_RE.sub("", rest)
    rest = re.sub(r"[，,]?\s*\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*", "", rest)
    rest = re.sub(r"^[：:]\s*", "", rest).strip()
    rest = re.split(r"[（(]\s*(?:cut_id|总时长|镜头数)", rest, maxsplit=1)[0].strip()
    return rest or "未命名分镜组"


def build_storyboard_index_payload(
    *,
    content: str,
    episode_dir: Path,
    project: str | None = None,
) -> dict:
    episode_id = episode_id_for_cut_contract(episode_dir)
    if project is None:
        try:
            project = read_json(episode_dir / "episode.json").get("series_title") or episode_dir.parent.parent.name
        except Exception:
            project = episode_dir.parent.parent.name

    cuts: list[dict] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    running_start = 0
    for index, group_match in enumerate(group_matches, start=1):
        block_start = group_match.end()
        block_end = group_matches[index].start() if index < len(group_matches) else len(content)
        block = content[block_start:block_end]
        heading = group_match.group(0)
        cut_match = CUT_ID_RE.search(heading)
        cut_id = cut_match.group("cut_id") if cut_match else _desired_cut_id(episode_id, index)

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        if time_matches:
            durations, _ = _extract_time_range_durations(time_matches)
            duration_sec = sum(value for value in durations if value > 0)
        else:
            duration_match = CLEAN_GROUP_TOTAL_RE.search(group_match.group("rest"))
            duration_sec = int(duration_match.group("seconds")) if duration_match else 0

        cuts.append(
            {
                "cut_id": cut_id,
                "group_index": index,
                "title": _extract_group_title(group_match.group("rest")),
                "scene": _extract_bold_meta(block, "场景"),
                "characters": _extract_bold_meta(block, "人物"),
                "props": _extract_bold_meta(block, "道具"),
                "duration_sec": duration_sec,
                "group_start_sec": running_start,
                "group_end_sec": running_start + duration_sec,
                "source_group_label": f"第{index}组",
            }
        )
        running_start += duration_sec

    return {
        "project": project,
        "episode_id": episode_id,
        "cuts": cuts,
    }


def write_simple_xlsx(path: Path, sheet_name: str, rows: list[list[object]]) -> None:
    """Write a minimal XLSX file without adding a third-party runtime dependency."""

    def column_name(number: int) -> str:
        name = ""
        while number:
            number, rem = divmod(number - 1, 26)
            name = chr(65 + rem) + name
        return name

    def cell_xml(value: object, row_index: int, col_index: int) -> str:
        ref = f"{column_name(col_index)}{row_index}"
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return f'<c r="{ref}"><v>{value}</v></c>'
        text = xml_escape("" if value is None else str(value))
        return f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>'

    sheet_rows = []
    for row_index, row in enumerate(rows, start=1):
        cells = "".join(cell_xml(value, row_index, col_index) for col_index, value in enumerate(row, start=1))
        sheet_rows.append(f'<row r="{row_index}">{cells}</row>')

    dimension = f"A1:{column_name(max(len(row) for row in rows) if rows else 1)}{max(len(rows), 1)}"
    worksheet_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<dimension ref="{dimension}"/><sheetData>{"".join(sheet_rows)}</sheetData></worksheet>'
    )
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheets><sheet name="{xml_escape(sheet_name)}" sheetId="1" r:id="rId1"/></sheets></workbook>'
    )
    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '</Types>'
    )
    root_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '</Relationships>'
    )
    workbook_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
        '</Relationships>'
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml)
        archive.writestr("_rels/.rels", root_rels_xml)
        archive.writestr("xl/workbook.xml", workbook_xml)
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml)
        archive.writestr("xl/worksheets/sheet1.xml", worksheet_xml)


def write_storyboard_index_files(episode_dir: Path, content: str | None = None) -> tuple[Path, Path]:
    final_path = episode_dir / "final.txt"
    if content is None:
        content = final_path.read_text(encoding="utf-8", errors="replace")
    payload = build_storyboard_index_payload(content=content, episode_dir=episode_dir)
    json_path = episode_dir / "storyboard_index.json"
    xlsx_path = episode_dir / "storyboard_index.xlsx"
    write_json(json_path, payload)

    rows: list[list[object]] = [
        [
            "project",
            "episode_id",
            "cut_id",
            "group_index",
            "title",
            "scene",
            "characters",
            "props",
            "duration_sec",
            "source_group_label",
        ]
    ]
    for cut in payload["cuts"]:
        rows.append(
            [
                payload["project"],
                payload["episode_id"],
                cut["cut_id"],
                cut["group_index"],
                cut["title"],
                cut["scene"],
                "、".join(cut["characters"]),
                "、".join(cut["props"]),
                cut["duration_sec"],
                cut["source_group_label"],
            ]
        )
    write_simple_xlsx(xlsx_path, "storyboard_index", rows)
    return json_path, xlsx_path


def _validate_review_checked_groups(payload: dict, content: str, review_name: str) -> list[str]:
    expected = _storyboard_group_labels(content)
    if not expected:
        return []
    checked = {item.strip() for item in payload.get("checked_groups", []) if isinstance(item, str)}
    missing = [label for label in expected if label not in checked]
    if missing:
        return [f"{review_name} checked_groups missing reviewed groups: {', '.join(missing[:8])}"]
    return []


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
    elif review_payload is not None:
        final_path = episode_dir / "final.txt"
        if final_path.is_file():
            final_content = final_path.read_text(encoding="utf-8", errors="replace")
            issues.extend(_validate_review_checked_groups(review_payload, final_content, "review.txt"))

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
            segment_payload, segment_error = _read_review_json(segment_dir / "review.md")
            if segment_error:
                issues.append(f"{segment_dir.name}: {segment_error}")
            elif segment_payload is not None:
                segment_final = segment_dir / "final.txt"
                segment_draft = segment_dir / "draft.txt"
                review_target = segment_final if segment_final.is_file() else segment_draft
                if review_target.is_file():
                    target_content = review_target.read_text(encoding="utf-8", errors="replace")
                    for issue in _validate_review_checked_groups(segment_payload, target_content, "review.md"):
                        issues.append(f"{segment_dir.name}: {issue}")

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
                "segment_titles": [segment.title for segment in segments],
            }
        )

    write_json(run_dir / "manifest.json", manifest)
    write_utf8(
        run_dir / "AGENTS.md",
        textwrap.dedent(
            """
            # Storyboard Agent Run Instructions

            This directory is an agent-native workspace. Each `episodes/epXX` folder is an independent task.

            ## Dispatcher Hard Stop

            If this run contains 2 or more episodes, the host/main agent is a dispatcher only.

            Dispatcher must:
            - Create subagents/workers and dispatch `episodes/epXX/agent_prompt.md`.
            - Run up to the configured worker limit in parallel.
            - Stop with `NEED_USER_DISPATCH` and list prompt paths if worker creation is unavailable or requires user authorization.

            Dispatcher must not:
            - Directly generate storyboard body text.
            - Sequentially process multiple episodes in the main thread.
            - Open `episodes/ep*/script.txt` and begin production work.
            - Write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
            - Downgrade to main-thread sequential production when subagents/workers are unavailable.

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
    print(f"[next] read: {run_dir / 'DISPATCH_PROMPT.md'}")
    print("[next] dispatch episode agents outside Python; then run .\\COLLECT_RESULTS.ps1")
    return 0


def validate_episode(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    episode_id = episode_id_for_cut_contract(episode_dir)
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
        content, cut_id_changes = ensure_storyboard_cut_ids(content, episode_id)
        if cut_id_changes:
            fix_messages.append("normalized cut_id " + "; ".join(cut_id_changes[:8]))
        if fix_messages:
            write_utf8(final_path, content)
            print("[fixed] " + " | ".join(fix_messages))

    clean_issues = validate_clean_storyboard_format(content)
    cut_id_issues = validate_storyboard_cut_ids(content, episode_id)
    quality_issues = validate_storyboard_quality_floor(content)
    review_issues = validate_review_artifacts(episode_dir)
    review_payload, review_error = _read_review_json(episode_dir / "review.txt")
    review_pass_issues: list[str] = []
    if review_error is None and not _storyboard_review_passed(review_payload):
        review_pass_issues.append("storyboard_reviewer: reviewer_not_passed")
    issues = clean_issues + cut_id_issues + quality_issues + review_issues + review_pass_issues
    report_lines = ["# Episode Validation", ""]
    if issues:
        report_lines.append("status: failed")
        report_lines.append("")
        if clean_issues:
            report_lines.append("## Clean Format")
            report_lines.extend(f"- {issue}" for issue in clean_issues)
            report_lines.append("")
        if cut_id_issues:
            report_lines.append("## Cut ID Contract")
            report_lines.extend(f"- {issue}" for issue in cut_id_issues)
            report_lines.append("")
        if quality_issues:
            report_lines.append("## Quality Floor")
            report_lines.extend(f"- {issue}" for issue in quality_issues)
            report_lines.append("")
        if review_issues:
            report_lines.append("## Storyboard Reviewer Evidence")
            report_lines.extend(f"- {issue}" for issue in review_issues)
            report_lines.append("")
        if review_pass_issues:
            report_lines.append("## Storyboard Reviewer Pass")
            report_lines.extend(f"- {issue}" for issue in review_pass_issues)
        write_utf8(episode_dir / "protocol_report.md", "\n".join(report_lines))
        print(f"[failed] {len(issues)} validation issue(s)")
        for issue in issues:
            print(f"- {issue}")
        return 1

    report_lines.append("status: passed")
    report_lines.append("")
    report_lines.append("- clean_format: passed")
    report_lines.append("- cut_id_contract: passed")
    report_lines.append("- quality_floor: passed")
    report_lines.append("- review_evidence: passed")
    report_lines.append("- storyboard_reviewer: passed")
    write_storyboard_index_files(episode_dir, content)
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
        episode_contract_id = episode_id_for_cut_contract(episode_dir)
        content, cut_id_changes = ensure_storyboard_cut_ids(content, episode_contract_id)
        changes.extend(cut_id_changes)
        clean_issues = validate_clean_storyboard_format(content)
        cut_id_issues = validate_storyboard_cut_ids(content, episode_contract_id)
        quality_issues = validate_storyboard_quality_floor(content)
        review_issues = validate_review_artifacts(episode_dir)
        issues = clean_issues + cut_id_issues + quality_issues + review_issues
        review_payload, review_error = _read_review_json(episode_dir / "review.txt")
        review_passed = review_error is None and _storyboard_review_passed(review_payload)
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
            summary_lines.extend(f"- cut_id_contract: {issue}" for issue in cut_id_issues[:8])
            summary_lines.extend(f"- quality_floor: {issue}" for issue in quality_issues[:8])
            summary_lines.extend(f"- storyboard_reviewer: {issue}" for issue in review_issues[:8])
            summary_lines.append("- copied: skipped because validation failed")
            summary_lines.append("- existing_output: not modified")
            summary_lines.append("")
            continue
        if status != "done" or not review_passed:
            failed += 1
            summary_lines.append(f"- status: {status}, reviewer_not_passed")
            if review_error:
                summary_lines.append(f"- review_evidence: failed: {review_error}")
            else:
                summary_lines.append("- review_evidence: passed")
                summary_lines.append("- storyboard_reviewer: failed")
            summary_lines.append("- copied: skipped because status is not done or storyboard reviewer did not pass")
            summary_lines.append("- existing_output: not modified")
            summary_lines.append("")
            continue

        write_utf8(output_path, content)
        index_json_path, index_xlsx_path = write_storyboard_index_files(episode_dir, content)
        index_output_json = out_dir / f"{output_path.stem}_index.json"
        index_output_xlsx = out_dir / f"{output_path.stem}_index.xlsx"
        shutil.copy2(index_json_path, index_output_json)
        shutil.copy2(index_xlsx_path, index_output_xlsx)
        copied += 1
        summary_lines.append(
            f"- status: {status}, clean_format_passed, quality_floor_passed, "
            f"review_evidence_passed, storyboard_reviewer_passed"
        )
        if changes:
            summary_lines.append(f"- clean_numbering_fixed: {'; '.join(changes[:8])}")
        summary_lines.append(f"- copied: `{output_path}`")
        summary_lines.append(f"- storyboard_index_json: `{index_output_json}`")
        summary_lines.append(f"- storyboard_index_xlsx: `{index_output_xlsx}`")
        summary_lines.append("")

    summary_lines.append(f"Copied: {copied}")
    summary_lines.append(f"Validation/collection failures: {failed}")
    write_utf8(run_dir / "SUMMARY.md", "\n".join(summary_lines))
    print(f"[done] copied {copied} final file(s) to {out_dir}")
    print(f"[summary] {run_dir / 'SUMMARY.md'}")
    return 1 if failed else 0


def export_storyboard_index(args: argparse.Namespace) -> int:
    targets: list[Path] = []
    if args.episode_dir:
        targets.append(args.episode_dir.resolve())
    if args.run_dir:
        run_dir = args.run_dir.resolve()
        manifest_path = run_dir / "manifest.json"
        if manifest_path.is_file():
            manifest = read_json(manifest_path)
            targets.extend(Path(item["episode_dir"]) for item in manifest.get("episodes", []))
        else:
            targets.extend(sorted(path for path in (run_dir / "episodes").iterdir() if path.is_dir()))

    if not targets:
        print("[error] pass --episode-dir or --run-dir", file=sys.stderr)
        return 2

    exported = 0
    failed = 0
    for episode_dir in targets:
        final_path = episode_dir / "final.txt"
        if not final_path.is_file():
            print(f"[skip] missing final.txt: {episode_dir}", file=sys.stderr)
            failed += 1
            continue
        content = final_path.read_text(encoding="utf-8", errors="replace")
        if args.fix_metadata:
            content = strip_machine_tags(content)
            content, _ = normalize_clean_storyboard_numbering(content)
            content, _ = ensure_storyboard_cut_ids(content, episode_id_for_cut_contract(episode_dir))
            write_utf8(final_path, content)

        cut_issues = validate_storyboard_cut_ids(content, episode_id_for_cut_contract(episode_dir))
        if cut_issues:
            print(f"[failed] {episode_dir}", file=sys.stderr)
            for issue in cut_issues:
                print(f"- {issue}", file=sys.stderr)
            failed += 1
            continue
        json_path, xlsx_path = write_storyboard_index_files(episode_dir, content)
        print(f"[exported] {json_path}")
        print(f"[exported] {xlsx_path}")
        exported += 1

    print(f"[done] exported {exported} storyboard index file set(s)")
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
    prepare.add_argument("--agent", choices=["codex", "qwen", "kimi"], default="codex")
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

    export_index = subparsers.add_parser("export-storyboard-index", help="Export storyboard_index.json/xlsx for episode cuts.")
    export_index.add_argument("--episode-dir", type=Path, default=None)
    export_index.add_argument("--run-dir", type=Path, default=None)
    export_index.add_argument("--fix-metadata", action="store_true")
    export_index.set_defaults(func=export_storyboard_index)

    run = subparsers.add_parser("run", help="Disabled: Python does not launch agent CLIs.")
    run.add_argument("--run-dir", type=Path, required=True)
    run.set_defaults(func=run_workspace)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
