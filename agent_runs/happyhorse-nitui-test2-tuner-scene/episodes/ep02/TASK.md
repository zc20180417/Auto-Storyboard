# Task: EP-02

Mode: `scene`

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
- Review skill: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
- Target video model: `happyhorse`
- HappyHorse prompt profile: `G:\Auto-Storyboard\agent_skills\happyhorse-prompt-profile\SKILL.md`，只作为 HappyHorse 1.0 视频提示词参考层，不得复制官方 case、控制台占位符或非短剧模板语气到 `final.txt`
- AI video prompt skill: `G:\Auto-Storyboard\agent_skills\ai-video-prompt\SKILL.md`，只在 HappyHorse 目标模型下作为提示词优化参考；不得复制 `@图`、`Image`、参考图/首帧槽位、独立音频时间轴、BGM 或视频编辑模板语气到 `final.txt`
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
1. Read `../../context.md`, both standard `SKILL.md` files, the HappyHorse / Seedance prompt profiles, and the AI video prompt skill, `script.txt`, and each segment script.
2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组; each group keeps its own time ranges from 0 seconds. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. Group-internal time ranges may use 0.5-second boundaries, but the group total must be an integer 10-15 seconds.
4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation. Validation exports `storyboard_index.json` and `storyboard_index.xlsx` from `final.txt`.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.

## HappyHorse Output Contract
- For HappyHorse, every group must use this visible wrapper: `【场景】`, `【主体】`, `【运动】`, `【音频】`, `组尾衔接`, `【画面风格】`.
- Do not use the default Seedance-looking wrapper in `final.txt`: no `**人物**`, `**场景**`, `**道具**`, `组首空间锁定`, `画面风格：`, or standalone `--neg` lines.
- Use HappyHorse Prompt Tuner as a minimal repair / structure cleanup layer, not an aggressive rewrite layer. Preserve key shots, action stages, character relations, key props, original dialogue, and sound design.
- Before writing each group, internally check five anchors: subject, scene, motion, camera, and sound. Fill only missing anchors; do not add brands, props, subtitles, BGM, or interface settings that are not in the script.
- Put scene/time/light/environment into `【场景】`. Put visible characters, key props, positions, body orientation, gaze, dialogue targets, and prop ownership into `【主体】`.
- Put all time-coded shot ranges only under `【运动】`. Each time range must be a standalone Chinese `秒` line, for example `0-4.5秒：`, followed by `镜头描述：` and `光影设计：`.
- `【运动】` is for visible action, camera movement, mouth movement, body reaction, prop operation, and light changes. Do not repeat full dialogue there; full script dialogue belongs in `【音频】`.
- Use `【音频】` for sounds and dialogue, but do not repeat timecodes there. Use `第一段/第二段/第三段` to align with the movement segments.
- Keep `【画面风格】` short: visual style, no subtitles/no music, and a compact `负向：...` list of at most 8 items.
- Do not put production-side interface parameters in `final.txt`: no aspect ratio such as `16:9` / `9:16`, no repeated group duration such as `11秒` / `11s`, and no resolution labels such as `4K` / `1080p`.
- Use `ai-video-prompt` only to improve HappyHorse-friendly wording: concrete visual compensation, stable camera movement, and clear dialogue/audio ownership.
- Keep the Auto-Storyboard contract unchanged: natural Chinese storyboard text, `cut_id`, group headings, Chinese `秒` time ranges, group tail continuity, reviewer pass, and validate gate.
- Do not write production-side image bindings such as `@图`, `Image 1`, `参考图`, `首帧`, `尾帧`, or reference-image instructions. Reference images are bound later by the video production workflow.
- Do not add BGM, subtitles, interface parameters, bracketed `[0-3s]` timelines, `s` time units, or a separate audio timeline.
- Dialogue and dubbing hints from `ai-video-prompt` must be converted into natural `【音频】` prose. Do not copy raw `[]` / `<>` acoustic-control markup into `final.txt` unless the original script explicitly contains that audible content.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\happyhorse-nitui-test2-tuner-scene\episodes\ep02"
```

`status.json` requirements:

- `episode_id`: `ep02`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `EP-02-ep02-agent-cli-storyboard.txt`
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
- Preferred heading format: `=== [cut_id: EPxx-GNN] 第N组：标题（总时长：XX秒，镜头数：X个） ===`.
- Do not put asset IDs in `final.txt`; asset binding belongs to the asset extraction stage.

## Important Constraints
- Rules live in the two standard `SKILL.md` files; HappyHorse / Seedance Prompt Profiles and AI Video Prompt Skill are only reference layers for the HappyHorse target. Do not duplicate or reinterpret them here.
- Work only inside `episodes\ep02`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
