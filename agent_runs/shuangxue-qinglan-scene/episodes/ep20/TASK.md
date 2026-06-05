# Task: ep20

Mode: `scene`
Aspect: `vertical` (竖屏)

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
- Review skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
- Target video model: `seedance`
- Seedance prompt profile: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`，只作为短剧风格参考层，不得复制模板正文、模板编号、官方占位符或非短剧模板语气到 `final.txt`
- Full episode script: `script.txt`
- Segment scripts: `segments/seg*/script.txt`

## Required Outputs
- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`
- `final.txt`
- `review.txt`
- `status.json`

## Production Focus
- 组首空间锁定等于本组第一帧，只写当前可生成状态，不写前情回顾。
- 每个时间段默认只承载一个主动作；复杂动作、外部事件进入、保护站位必须拆成可执行段。
- 高冲击打断后先稳定打断/反应，放下道具、跨位移、保护站位、团圆确认等归位动作另起时间段或另组。
- 不要为凑满 10 秒硬塞动作、对白或停顿；短承接和单句反应允许保留 6-9 秒。
- 保护动作写清挡在谁前面，非主动作人物只写站位和轻反应，不抢主动作。
- 关键道具写清归属、位置和状态变化，组尾必须能接到下一组。
- `视频禁止项` 只写 2-5 个具体剧情错误，必须锚定本组或本集上下文；完整规则仍以 generator/reviewer skill 和 quality policy 为准（policy: `storyboard-quality-policy-2026-05-31-v1`）。

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, the Seedance prompt profile, `script.txt`, and each segment script.
2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. Group-internal time ranges may use 0.5-second boundaries, and the group total must be an integer second. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds.
4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation. Validation is txt-only by default; storyboard index JSON/XLSX export is opt-in and not part of the current required output.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.



Pre-check command (run before calling storyboard-reviewer to catch mechanical issues early):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-scene\episodes\ep20" --pre-check
```

For segment-level pre-check (scene mode, validate a segment draft before review):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-scene\episodes\ep20" --pre-check --content-file "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-scene\episodes\ep20/segments/segXX/draft.txt"
```

Full validation command (run after review.txt and status.json are written):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-scene\episodes\ep20"
```

`status.json` requirements:

- `episode_id`: `ep20`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `ep20-ep20-agent-cli-storyboard.txt`
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
- Vertical outputs follow the vertical generator skill contract; do not apply horizontal camera-motion fields unless the run aspect is horizontal.
- Work only inside `episodes\ep20`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
