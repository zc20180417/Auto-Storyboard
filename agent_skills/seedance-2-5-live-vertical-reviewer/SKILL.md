---
name: seedance-2-5-live-vertical-reviewer
description: Review Auto-Storyboard live-action 9:16 short-drama drafts made for the multimodal-generation-only seedance-2.5-live-vertical profile. Use after generation to verify task scope, script fidelity, 4-30 second integer staging, native audio, continuity, filmability, and reviewer evidence.
---

# Seedance 2.5 真人竖屏短剧审核器

只审稿，不润色，不全量重写。worker 启动时完整读取本 reviewer、`seedance-2-5-live-vertical-generator/SKILL.md` 和 `seedance-2-5-live-vertical/SKILL.md` 一次；同一 worker、同一 run 内文件未变化时直接复用，不在生成、审核、修复复审之间重复加载。每次审核仍必须重新读取同一 episode 的 `script.txt`、当前待审 draft/final，以及存在时的 `boundary_context.md` 和上一集实际末组。只有组装后的 v3 整集 `final.txt` 审核额外读取预检生成的 `review_facts.json`；scene 的 segment 草稿/成稿审核不读取该文件。不得用已有 review、status、校验器或生成者自评代替真实语义审核。

`review_facts.json` 只提供当前 `final.txt` 的 SHA-256 和机械计数；跨集连续时还绑定上一集实际 `final.txt` 的集号与 SHA-256。它能证明审的是哪一版正文，也能替代重复输出逐镜数字数组，但不能判断剧情忠实、说话对象、动作可演性、道具接续或空间连续性。

## 判定原则

- 逐组对照原剧本和当前分镜，问题必须给出组别、原文/镜头证据和可执行局部修复。
- hard issue 放入 `issues` 并令 `pass=false`；软风险只放 `warnings`。
- `pass=true` 时 `issues=[]`，任何 `semantic_checks.result=issue` 都必须同步使 `pass=false`。
- 不按审美喜好判错，不因运镜多/少、组长/组短本身判错；判断可拍性、容量、连续性和模型合同。
- 旧 Seedance 2.0 的 6-15 秒、0.5 秒边界、4K固定尾部、大包 `--neg` 不适用于本 reviewer。
- 本 profile 的唯一视频任务是 `multimodal_generation`；图片、视频、音频只能是实际输入素材，不能被改写成独立参考、编辑或延长任务。

## Hard issue

### 格式与 2.5 时间合同

- 缺少或重复 `cut_id`，不是当前集连续的 `EPxx-GNN`。
- 组标题总时长不是整数秒，或不在 4-30 秒。
- 时间段未从 0 开始、不连续、出现小数秒边界、最后结束秒不等于标题总时长。
- 标题镜头数与实际时间段数不一致，或缺 `人物`、`场景`、`道具`、组首空间锁定、镜头描述、光影设计、组尾衔接、组结束标记。
- 4-7 秒组不是必要短打断/反应/插入/余波/意象，且可自然合并；或为了把短节拍拉长，新增凝视、沉默、普通微表情和无信息停顿。
- 16-30 秒组没有足够台词/声音、完整动作/道具变化、冲突升级/揭示/关系变化中的至少两类；没有清楚阶段；同一阶段包含多个并列状态变化；或只靠流程、看向、等待、站位延续撑时长。
- **过度切碎（`generation_density`）：相邻两组或多组处于同一主要空间、同一冲突目标、同一批在场人物，属于一条连续流程（拨打/夺取/递出/登记/复核/追问/僵持等），合并后总时长仍 ≤30 秒，却被切成多个短组。** 每个接缝都是一次独立生成之间的连贯性风险，无理由的切分必须判 hard issue，`fix_instruction` 写明应合并哪几组、合并后总时长与阶段划分。存在跨空间、跨冲突目标、多主体并行、明显跨位移、重物搬运、多人协同、精细操作、独立戏剧节拍、信息落点、反应落点、原剧本明确停顿，或合并后关键状态说不清楚时，拆分是正当的，不判错。
- 自然需要更长时间的剧情被硬压进 30 秒，导致对白、动作、转折或关键操作不可表演。

### 原剧本忠实

- 漏、改、错置关键台词、说话对象、台词顺序、因果、人物关系、情绪转折、关键动作或道具。
- 新增改变剧情的强动作、进出场、递物、打人、跪下、拥抱、逃跑、开枪或摔物。
- 把关键动作/道具压成无法理解；普通走位、重复微表情和无关停顿允许压缩。

### 台词、原生音频与口型

- 现场开口没有真实对象，或发明“对空气/文件/桌面说道”。
- 心声、旁白、电话音、广播音、门外音被写成现场开口；画面人物承载心声却未写闭口、不做口型。
- 关键画外声音没有来源或可见载体/人物反应。
- 有效台词字数 ÷ 镜头秒数超过 6.5 字/秒；5.8-6.5 字/秒可做 warning。
- 普通长台词被明显拖慢，短句无迟疑/哽咽/虚弱/同步动作却被拉长，或“一字一顿”等慢语没有给足时间。
- 声音与动作不能在同阶段同步完成，或用画外音掩盖被压缩的关键表演。

### 密度与动作原子性

- 同一时间段有多个主体、多个动作目标或竞争结果；不能仅按动词数量误判同一主体/空间/目标下顺序和结果清楚的 2-3 秒紧凑链。
- 外部事件把到达、开门、下车、群众反应、主角对峙压进同一短阶段，现场状态无法稳定。
- 高冲击打断后继续压入放道具、跨位移、保护站位、团圆确认等归位动作，导致站位/道具不可执行。
- 保护动作不写挡在谁前面/保护谁；旁观人物抢原剧本主动作。
- 明显跨位移、重物搬运、多人协同、精细操作或关键道具操作时间不足。

### 空间、人物与连续性

- 同组跨两个主要物理空间且无原剧本明确例外。
- 组首不是第一帧状态，包含“进入、走来、递出、拿起、打开”等过程动作或回顾前情。
- 可见具名人物未逐人写画面位置、相对镜头身体朝向和脸朝画左/右；人物未在场也无入场/声音/屏幕来源却直接行动或说话。
- 组首与首镜矛盾；组尾与下一组组首在人物位置姿态、道具归属、门窗/车辆、时间光线或持续声音上无过渡跳变。
- 同组关键道具从 A 变为 B 可操作，缺少递出、放下、推近、拿起、抢走或滑落等可见过渡。
- 跨集连续边界重置光线、人物姿态、保护关系、道具、门窗/车辆或持续声音；若源剧本自身冲突，记录 `source_continuity_conflict` warning。

### 可拍性、运镜与 prompt 污染

- 不可视关键信息没有转成可见动作、道具、表情、光影、声音或台词。
- 普通环境交代超过 3 秒，或超过 2 秒且明显凑时长。
- 运镜缺动机、主体、路径或落点；与人物位移冲突；遮掉口型/关键手部；制造瞬移、道具跳手；短镜头同时推摇环绕。固定机位和合理运镜均可通过。
- 最终正文出现模型参数、4K/1080p控制、模型自述、虚构 `@图片/@视频/@音频`、模板编号、JSON、自检文字或模板化空话。
- 最终正文指示纯文本/文生视频、参考生成、首尾帧/关键帧生成、视频编辑、视频延长/续写或轨道补全；统一按 `multimodal_task_scope` hard issue 处理。
- worker 写入旧版固定画面/声音尾部或大包通用 `--neg`。
- `视频禁止项` 超过 5 条、是泛词/模板词、无人物/道具/场景锚点、机械复制，或禁止原剧本必须动作。

## Warning

- 5.8-6.5 字/秒但仍可表演的偏快台词。
- 合法 4-7 秒短组或 16-30 秒长组接近容量边缘，现场不可再叠加停顿/动作。
- 6 个以上整数阶段略碎但仍清楚。
- 关键道具过渡略含糊但仍可推断，不构成跳手。
- 复杂动作/保护站位/关键道具组缺少聚焦 `视频禁止项`，但正文已经清楚。
- 原剧本自身连续性冲突或信息含糊，分别用 `source_continuity_conflict`、`source_ambiguity`。

## 必做证据

- `checked_groups` 列出全部实际审核组。
- `audit_coverage` 下列字段全部为 `checked`：`script_fidelity`、`dialogue_direction`、`timing_math`、`dialogue_pacing`、`space_locking`、`format`、`character_availability`、`handoff_continuity`、`filmability`、`audio_mouth_sync`、`generation_density`、`action_atomicity`、`video_negative_constraints`、`prompt_pollution`、`prop_continuity`、`camera_motion_reasonableness`、`cross_episode_continuity`。
- `audit_coverage.multimodal_task_scope=checked`，明确检查正文没有其他任务模式，并确认分镜母版只等待真实多模态素材绑定。
- `spot_checks` 至少 3 条，引用具体台词、人物、道具、空间或动作。
- `semantic_checks` 至少 3 条，每条含 `group/type/result/evidence/fix_instruction`。
- v3 整集 `review.txt` 先运行 `validate-episode --pre-check`，把 `review_facts.json.mechanical_evidence` 原样复制到审核 JSON；不得自行改哈希或计数。审核当前 `final.txt` 后，再按正文顺序把全部已核对项目的原文标签写入紧凑 `semantic_coverage`：全部对白镜头、全部相邻组接缝、跨集连续时的 `上一集实际末组->第1组`、全部明确运镜镜头；只写标签，不展开通过项长证据。多 segment 的 `segments/segXX/review.md` 不写 `mechanical_evidence` 或 `semantic_coverage`，两者由组装后的整集审核统一绑定。
- 仍逐镜检查全部对白/旁白/心声的声音类型、对象、口型和可表演性，逐接缝检查人物/道具/门车/光线，逐个明确运镜检查动机、主体、路径、落点和动作兼容性；通过项不再展开成 `dialogue_checks`、`handoff_checks`、`camera_motion_checks` 数组。
- 存在 `boundary_context.md` 时，`semantic_checks` 必须有一条 `type=cross_episode_continuity`、`group=第1组` 的具体证据，明确对照上一集实际末态与本集首帧；仅写 `handoff_count` 或覆盖标签不能替代这条语义证据。
- 跨集 v3 预检若提示上一集 `final.txt` 不存在，必须等待前集完成；审核后若上一集哈希变化，本集必须重新 pre-check、重新审核，不能沿用旧 `review.txt`。
- 任何机械计数对应内容里的语义异常，都写进 `semantic_checks`，并按严重性同步进入 `issues` 或 `warnings`；不能因为 Python 预检通过就跳过人工语义核对。
- `issue_instances_total` 记录实际 hard 证据点总数；`affected_groups` 列全受影响组，不能被最多 5 条展示限制掩盖。

## 稳定 taxonomy

使用：`format`、`script_fidelity`、`dialogue_direction`、`timing_math`、`audio_mouth_sync`、`dialogue_pacing`、`generation_density`、`space_locking`、`character_availability`、`handoff_continuity`、`prop_continuity`、`filmability`、`action_atomicity`、`video_negative_constraints`、`camera_motion_reasonableness`、`cross_episode_continuity`、`prompt_pollution`、`multimodal_task_scope`。

## 输出

只返回原始 JSON，不要 markdown 或解释。结构必须为：

```json
{
  "pass": false,
  "summary": "一句话真实审核总结",
  "checked_groups": ["第1组", "第2组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked",
    "prop_continuity": "checked",
    "camera_motion_reasonableness": "checked",
    "cross_episode_continuity": "checked",
    "multimodal_task_scope": "checked"
  },
  "spot_checks": [
    {"group": "第1组", "type": "dialogue_pacing", "evidence": "具体台词、字数、秒数和字秒比。"},
    {"group": "第1组", "type": "space_locking", "evidence": "具体人物第一帧位置与朝向。"},
    {"group": "第2组", "type": "script_fidelity", "evidence": "具体原剧本动作/道具/关系如何保留。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "audio_mouth_sync", "result": "pass", "evidence": "具体证据", "fix_instruction": "失败时的局部修法"},
    {"group": "第1组", "type": "generation_density", "result": "pass", "evidence": "具体证据", "fix_instruction": "失败时的局部修法"},
    {"group": "第2组", "type": "handoff_continuity", "result": "issue", "evidence": "具体矛盾", "fix_instruction": "补哪个组尾/组首状态"}
  ],
  "mechanical_evidence": {
    "final_sha256": "从 review_facts.json 原样复制的64位小写哈希",
    "group_count": 2,
    "dialogue_shot_count": 1,
    "handoff_count": 1,
    "camera_motion_shot_count": 1
  },
  "semantic_coverage": {
    "dialogue_shots_checked": ["第1组 0-3秒"],
    "handoffs_checked": ["第1组->第2组"],
    "camera_motion_shots_checked": ["第1组 3-7秒"]
  },
  "issue_instances_total": 1,
  "affected_groups": ["第2组"],
  "issues": [
    {"severity": "hard", "group": "第2组", "rule": "handoff_continuity", "problem": "具体问题", "evidence": "具体证据", "fix": "可执行局部修复"}
  ],
  "warnings": [
    {"severity": "soft", "group": "第1组", "rule": "dialogue_pacing", "problem": "具体风险", "evidence": "具体证据", "fix": "可选优化"}
  ]
}
```

`issues` 和 `warnings` 各最多展示 5 条代表项；`issue_instances_total` 与 `affected_groups` 仍必须覆盖全部实际 hard 问题。

兼容旧 run：若 `episode.json.vertical_review_contract_version=2`，仍按该 run 已生成的 `TASK.md` 输出完整 `dialogue_checks`、`handoff_checks`、`camera_motion_checks`；只有 v3 使用 `review_facts.json`、紧凑 `mechanical_evidence` 和条目标识式 `semantic_coverage`。
