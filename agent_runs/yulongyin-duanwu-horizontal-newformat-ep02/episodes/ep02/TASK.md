# Task: 雨龙吟端午第02集

Mode: `single`
Aspect: `horizontal` (横屏)

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `G:\Auto-Storyboard\agent_skills\storyboard-horizontal-generator\SKILL.md`
- Review skill: `G:\Auto-Storyboard\agent_skills\storyboard-horizontal-reviewer\SKILL.md`
- Target video model: `seedance`
- Seedance prompt profile: `G:\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`，只作为短剧风格参考层，不得复制模板正文、模板编号、官方占位符或非短剧模板语气到 `final.txt`
- Full episode script: `script.txt`
- Segment scripts: not used in `single` mode.

## Required Outputs
- `final.txt`
- `storyboard_index.json`
- `storyboard_index.xlsx`
- `review.txt`
- `status.json`

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, the Seedance prompt profile, and `script.txt`.
2. Generate the full episode directly into `final.txt`. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. Horizontal groups use `N-M` shot numbers and `**本镜估算时长**：X秒` per shot; each group's estimated shot durations must sum to the integer group total. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds.
3. Review the full episode once using the review skill; write `review.txt`.
4. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups.
5. Re-run `storyboard-horizontal-reviewer` after repairs and update `review.txt`.
6. Write `status.json` with reviewer metadata, then run validation. Validation exports `storyboard_index.json` and `storyboard_index.xlsx` from `final.txt`.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.



Pre-check command (run before calling storyboard-horizontal-reviewer to catch mechanical issues early):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-newformat-ep02\episodes\ep02" --pre-check
```

For segment-level pre-check (scene mode, validate a segment draft before review):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-newformat-ep02\episodes\ep02" --pre-check --content-file "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-newformat-ep02\episodes\ep02/segments/segXX/draft.txt"
```

Full validation command (run after review.txt and status.json are written):

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\yulongyin-duanwu-horizontal-newformat-ep02\episodes\ep02"
```

`status.json` requirements:

- `episode_id`: `ep02`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `雨龙吟端午-ep02-agent-cli-storyboard.txt`
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
- Do not put asset IDs in `final.txt`; asset binding belongs to the asset extraction stage.

## Important Constraints
- Rules live in the two standard `SKILL.md` files; Seedance Prompt Profile is only a reference layer. Do not duplicate or reinterpret them here.
- Horizontal outputs must use the current horizontal Seedance wrapper: `**人物**`, `**场景**`, `**道具/关键视觉资产**`, `**组间承接**`, `**横屏构图/调度**`, `N-M` shot numbers with `**镜头描述**`, `**光影设计**`, `**本镜估算时长**`, then `**组尾衔接**`, `**画面风格**`, `**运镜强化词**`, `**Seedance执行提示补充**`, and `**--neg**`. Do not use the old horizontal `组首空间锁定` or per-shot `运镜设计` fields.
- Work only inside `episodes\ep02`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
