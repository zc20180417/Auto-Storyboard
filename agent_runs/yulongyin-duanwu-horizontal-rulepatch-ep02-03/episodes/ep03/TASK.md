# Task: 雨龙吟端午-第03集

Mode: `scene`
Aspect: `horizontal` (横屏)

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `G:\Auto-Storyboard\agent_skills\storyboard-horizontal-generator\SKILL.md`
- Review skill: `G:\Auto-Storyboard\agent_skills\storyboard-horizontal-reviewer\SKILL.md`
- Target video model: `seedance`
- Seedance prompt profile: `G:\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`，只作为短剧风格参考层，不得复制模板正文、模板编号、官方占位符或非短剧模板语气到 `final.txt`
- Full episode script: `script.txt`
- Segment scripts: `segments/seg*/script.txt`

## Required Outputs
- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`
- `final.txt`
- `storyboard_index.json`
- `storyboard_index.xlsx`
- `review.txt`
- `status.json`

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, the Seedance prompt profile, `script.txt`, and each segment script.
2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. Horizontal groups use bare `N-M` shot numbers and `**本镜估算时长**：X秒` per shot; each group's estimated shot durations must sum to the integer group total. Prefer integer shot durations; use 0.5 seconds only for short reactions, prop inserts, or action aftershocks. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds. Do not compress key dialogue meaning just to fit the 15-second cap; split shots or groups instead.
4. Review the assembled `final.txt` once using `storyboard-horizontal-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-horizontal-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation. Validation exports `storyboard_index.json` and `storyboard_index.xlsx` from `final.txt`.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.



Pre-check command (run before calling storyboard-horizontal-reviewer to catch mechanical issues early):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-rulepatch-ep02-03\episodes\ep03" --pre-check
```

For segment-level pre-check (scene mode, validate a segment draft before review):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-rulepatch-ep02-03\episodes\ep03" --pre-check --content-file "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-rulepatch-ep02-03\episodes\ep03/segments/segXX/draft.txt"
```

Full validation command (run after review.txt and status.json are written):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-rulepatch-ep02-03\episodes\ep03"
```

`status.json` requirements:

- `episode_id`: `ep03`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `雨龙吟端午-ep03-agent-cli-storyboard.txt`
- `summary`: short Chinese summary
- `hard_issues_remaining`: copy unresolved hard issues from the real reviewer result
- `warnings`: copy or summarize warnings from the real reviewer result
- `reviewer_source`: must be `storyboard-horizontal-reviewer`
- `reviewer_pass`: copy the boolean `pass` from `review.txt` after `review.txt` exists
- `reviewer_issues_count`: copy `len(review.txt.issues)` after `review.txt` exists
- `reviewer_warnings_count`: copy `len(review.txt.warnings)` after `review.txt` exists

Do not prefill `reviewer_pass=true` or issue/warning counts before writing the real `review.txt`.

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `storyboard-horizontal-reviewer`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.
Reviewer JSON must include non-empty `checked_groups` and full `audit_coverage` fields as required by `storyboard-horizontal-reviewer/SKILL.md`.
Reviewer JSON must also include at least 3 `spot_checks` items with `group`, `type`, and `evidence`.
Reviewer JSON must include at least 3 `semantic_checks` items with `group`, `type`, `result`, `evidence`, and `fix_instruction`; `result` must be `pass`, `warning`, or `issue`.
If `pass=true`, `issues` must be empty and no `semantic_checks` item may use `result=issue`; if `pass=false`, `issues` must contain the blocking hard issue.
Template/model-term pollution must use `prompt_pollution` as the issue/warning `rule` or semantic check `type`.
`status.json` reviewer fields must stay consistent with `review.txt`.
`final.txt` cut_id contract:

- Every group heading must include exactly one `cut_id`.
- Use the current episode id and group number: `EP01-G01`, `EP01-G02`, ... for ep01; `EP30-G01`, ... for ep30.
- Preferred heading format: `=== [cut_id: EPxx-GNN] 第N组：标题（总时长：XX秒，镜头数：X个） ===`.
- Horizontal final.txt may preserve user-provided asset IDs in `**人物**`, `**场景**`, and `**道具/关键视觉资产**`, such as `天天图8`; do not invent asset IDs, and do not write `参考图`, `首帧参考`, `尾帧参考`, `@图片`, `@视频`, or upload/call instructions.

## Important Constraints
- Rules live in the two standard `SKILL.md` files; Seedance Prompt Profile is only a reference layer. Do not duplicate or reinterpret them here.
- Horizontal outputs must be generated as polished, Seedance-ready deliverables on the first pass, not rough drafts waiting for a separate rewrite. Use the current horizontal Seedance wrapper: `**人物**`, `**场景**`, `**道具/关键视觉资产**`, `**组间承接**`, `**横屏构图/调度**`, bare `N-M` shot-number lines, then each shot with `**镜头描述**`, `**光影设计**`, `**本镜估算时长**`, followed by `**组尾衔接**`, `**画面风格**`, `**运镜强化词**`, `**Seedance执行提示补充**`, and `**--neg**`. Do not write `**镜头号**：N-M`; do not use the old horizontal `组首空间锁定` or per-shot `运镜设计` fields. Keep assets under 9 per group; if the script requires more, split the group instead of deleting key story elements.
- Work only inside `episodes\ep03`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
