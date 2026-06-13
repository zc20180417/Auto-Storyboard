# Task: 剑破九天第06集

Mode: `scene`
Aspect: `horizontal` (横屏)

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-generator\SKILL.md`
- Review skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-reviewer\SKILL.md`
- Target video model: `seedance`
- Visual style: `3d-cg` (动漫3D CG)
- Seedance prompt profile: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`，只作为短剧风格参考层，不得复制模板正文、模板编号、官方占位符或非短剧模板语气到 `final.txt`

- 3D CG visual style skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\3d-cg-visual-style\SKILL.md`，只作为 3D CG 媒介风格参考层，不得替代主生成和审核规则
- Full episode script: `script.txt`
- Segment scripts: `segments/seg*/script.txt`

## Required Outputs
- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`
- `final.txt`
- `review.txt`
- `status.json`



## Visual Style Contract
- 本 run 的视觉风格是 `3d-cg`（动漫3D CG）。
- 动漫3D CG短剧风格：保留短剧分镜、对白、站位、道具连续和时间规则，但画面描述应服务于二次元角色设计、风格化面部与眼睛、清晰轮廓线、高质量卡通渲染、PBR材质与手绘质感融合、稳定表情绑定、清楚口型同步和流畅动作；动作/打斗/压迫/情绪峰值可以加入刀光、气流、碎石、尘浪、金属冷光等动作服务型大片特效；仙侠、玄幻、古武、强者归来、灵药/玄铁/真气/罡气/剑气题材的强节拍必须把克制可见特效写入镜头描述或光影设计，不能只靠固定画面风格尾部；特效必须跟随具体动作、灵物、压迫和受力结果，不得写成法阵、满屏粒子、游戏技能 UI 或盖住人物主体；不要写真人实拍、真实摄影、真实演员、纪录片摄影等真人媒介词。
- 横屏 final.txt 每组必须直接写入 3D CG 版 `**画面风格**` 和 `**--neg**`：正向包含高质量动漫3D CG短剧风格、二次元角色设计、风格化面部与眼睛、清晰轮廓线、高质量卡通渲染、PBR材质与手绘质感融合、电影级布光、自然景深；不得写真人实拍、真实摄影、真实演员；负向不得包含 `3D渲染`、`CG感`、`动画感`、`卡通`、`动漫`、`二次元`。3D CG 横屏每组至少安排 1 个有明确路径或落点的可见运镜，例如横向跟拍、前景掠过、半环绕、贴地推进、低角度推近、焦点转移或急停落点；对白密集段仍保留稳定镜头承载口型，不要全组炫技运动。
- `视频禁止项` 仍只写本组剧情错误，不要混入通用画质词或媒介风格词。

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, the Seedance prompt profile, the 3D CG visual style skill, `script.txt`, and each segment script.
2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. Horizontal groups use bare `N-M` shot numbers and `**本镜估算时长**：X秒` per shot; each group's estimated shot durations must sum to the integer group total. Prefer integer shot durations; use 0.5 seconds only for short reactions, prop inserts, or action aftershocks. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds. Do not compress key dialogue meaning just to fit the 15-second cap; split shots or groups instead.
4. Review the assembled `final.txt` once using `storyboard-horizontal-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-horizontal-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation. Validation is txt-only by default; storyboard index JSON/XLSX export is opt-in and not part of the current required output.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.

Pre-check command (run before calling storyboard-horizontal-reviewer to catch mechanical issues early):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06" --pre-check
```

For segment-level pre-check (scene mode, validate a segment draft before review):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06" --pre-check --content-file "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06/segments/segXX/draft.txt"
```

Full validation command (run after review.txt and status.json are written):

```powershell
python "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06"
```

`status.json` requirements:

- `episode_id`: `ep06`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `剑破九天-ep06-agent-cli-storyboard.txt`
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
- Work only inside `episodes\ep06`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
