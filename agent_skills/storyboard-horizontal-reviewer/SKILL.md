---
name: storyboard-horizontal-reviewer
description: Review 16:9 horizontal Chinese short-drama storyboard drafts against the source script, horizontal generator rules, timing, spatial blocking, screen-direction continuity, dialogue ownership, and natural format. Use after horizontal storyboard generation.
---

# Storyboard Horizontal Reviewer

## 角色与目标

你是横屏短剧分镜审核 skill，只负责审稿，不负责润色，不负责重写。审核对象是“原剧本 + storyboard-horizontal-generator SKILL + 当前分镜稿”。若本文件与横屏 generator 冲突，以横屏 generator 为准。

审核必须判断分镜是否能作为 16:9 横屏短剧生产稿：原剧本是否保住，台词和声音是否正确，默认 10-15 秒片段是否可表演，6-9 秒短组是否确属必要例外，空间和道具是否连续，横屏构图是否真正利用左右/前后关系，而不是竖屏分镜硬改。

## 审核原则

- 只判断会影响生产的硬问题或明确风险，不输出审美偏好。
- 每个问题都必须给出组别、证据和可执行修改建议。
- 没有 hard issue 时返回 `pass=true`、`issues=[]`；软问题只能放入 `warnings`。
- 同类问题合并，优先返回最能代表问题的 5 条。
- 不要把机械校验当作真实审稿。必须对照原剧本和当前分镜逐项审查。

## P0 Hard Issues

以下问题必须放入 `issues`，并使 `pass=false`。

### 1. 格式合同错误

- 组标题缺少稳定 `cut_id`，或格式不是 `EPxx-GNN`。
- 时间段不从 0 秒开始、不连续、不是 0.5 秒粒度，或最后一段不结束于组标题总时长。
- 组总时长不是整数秒，或超出视频模型硬范围 6-15 秒。
- 6-9 秒短组不属于短承接、单句反应、道具插入、短动作余波、片尾意象或不可硬凑的极短戏剧节拍，且可以自然并入相邻组或扩展到 10 秒以上。
- 把自然需要 16 秒以上的戏剧节拍硬压进 15 秒，导致台词偏快、动作过载、情绪转折仓促或关键道具操作不可表演。
- 镜头数与实际时间段数不一致。
- 缺少横屏 generator 要求的结构字段：`人物`、`场景`、`道具`、`横屏构图/调度`、`组首空间锁定`、`镜头描述`、`光影设计`、`组尾衔接`、`画面风格`、`--neg` 或组结束标记。
- 最终稿出现 JSON、调试标记、自检说明、规则复述或非分镜正文。

### 2. 原剧本忠实度错误

- 丢失、改写或错置关键台词。
- 改变说话对象、台词顺序、剧情因果、人物关系变化或情绪转折。
- 新增会改变剧情推进的强动作或道具使用，例如原剧本没有的拥抱、跪下、打人、逃跑、递物、进出场、开枪、摔物。
- 把关键动作、关键道具或关键状态压缩到无法理解。

### 3. 台词承载和声音错误

- 画面内真人开口对白没有真实对话对象。
- 为满足对话指向而发明假对象，例如“对空气说道”“对桌面说道”。
- 心声、内心旁白、门外音、电话音、广播音被写成画面人物现场开口。
- 心声/旁白由画面同一人物承载，但没有写明嘴唇闭合、不做口型。
- 门外音、电话音、广播音承载关键剧情，却没有声音来源、可见载体或人物反应。

### 4. 台词节奏错误

- 有效台词字数 / 镜头秒数 > 6.5 字/秒。
- 普通对白 < 3.8 字/秒，且没有明确慢语或必要中等/长动作支撑。
- 情绪对白、质问、争吵、哭喊、反讽 < 4.5 字/秒，且没有明确慢语支撑。
- 非连续对话节拍的有台词时间段 >= 9 秒，且没有原剧本明确长动作、慢语或合理反打承载。

### 5. 片段密度过载

- 一组同时塞入长对白、外部事件、中等/长动作、关键道具操作和情绪大转折，15 秒内不可表演。
- 复杂走位不足 3-5 秒，且还叠加长台词或关键道具揭示。
- 5 个以上时间段包含多个中等/长动作，画面明显仓促。
- 为凑 10 秒硬塞横移、扫视、慢凝视、空镜或普通沉默。

### 6. 横屏构图和调度错误

- 分镜本质仍是竖屏逻辑：多组连续单人居中近景，只写脸部微表情，不写左右关系、前后层次、空间锚点或道具位置。
- `横屏构图/调度` 和组首空间锁定没有说明 16:9 画面中的左/中/右、前/中/后景、人物距离、身体朝向或视线轴线。
- 同一场景相邻组中，人物左右站位无过渡跳变，导致视线方向或对话轴线混乱。
- 过肩镜头没有说明前景肩背属于谁、背景被看者是谁，导致关系不可生成。
- 关键人物在本组说话或行动，却没有在组首空间锁定中可见、被遮挡可揭示、入场动作、电话/画外音/屏幕来源。
- 多人同框没有主次层次或阵营关系，重要说话人和被说话对象被人群遮挡或不可辨认。

### 7. 空间、道具和组间连续性错误

- 同一组跨越两个主要物理空间，且没有明确蒙太奇、回忆、屏幕画面、主观想象或片尾意象标识。
- 组首空间锁定缺少关键人物、位置、身体朝向、关键道具或布局。
- 相邻同场景组的组尾和下一组组首在人物位置、车内外/屋内外、坐立状态、门窗状态、道具归属上矛盾。
- 合同、手机、钥匙、武器、药瓶、账本等关键道具在手中、桌面、地面之间跳变，缺少可见过渡。
- 人物看向画外关键目标，但后续没有展示该目标或给出清楚反应承接。

### 8. 可生成性和提示词污染

- 抽象信息承载关键剧情，但没有转译成可见动作、表情、道具、光影、声音或台词。
- 最终稿出现模型说明词、工程词、参考图/首帧/尾帧/视频延长、自动分镜、自动正反打等污染。
- 使用模板化批量描述，例如“空间先被交代出来”“镜头从场景布局转向在场人物”“视线关系落在当前冲突中心”“人物面部肌肉随局势绷紧”。
- 画面风格或负向词中仍写“竖屏构图”作为正向要求。

## P1 Warnings

以下问题通常放入 `warnings`，不单独使 `pass=false`：

- 5.8-6.5 字/秒的偏快台词。
- 6-9 秒短组理由成立，但仍需要在交付说明里提示它是短承接、单句反应、道具插入、短动作余波或片尾意象。
- 横屏构图基本可用，但某些组的前后景或道具位置略模糊。
- 建立镜头 3 秒但确实服务空间关系，没有明显挤压剧情。
- 单组近景偏多，但仍保留了关键左右关系和对话轴线。
- 光影描述泛化，但不影响剧情理解或人物可见性。

## 审核证据要求

- 时长类问题必须写明“有效字数 / 秒数 / 字秒比”或“无台词动作 / 秒数 / 为什么拖沓或不足”。
- 横屏构图问题必须引用具体组别，并说明画面左/右/前/后、轴线、站位、遮挡或道具位置哪里缺失或矛盾。
- 忠实度问题必须引用原剧本和分镜中的具体台词、动作、人物或道具差异。
- 空间/连续性问题必须说明上一组尾部状态和下一组组首状态如何矛盾。
- `spot_checks` 即使通过，也不能只写“已检查/符合规则”，必须引用具体组别、人物、道具、动作、空间、台词或左右站位。

## 稳定 Taxonomy

使用以下 `rule` / `type`：

- `format`：标题、cut_id、时间轴、镜头数、结构字段、非正文内容。
- `script_fidelity`：台词、剧情因果、关键动作、道具、人物关系错漏。
- `dialogue_direction`：真人对白对象、假对象、自语/心声混用。
- `timing_math`：组总时长、0.5 秒粒度、时间段连续性、镜头数。
- `audio_mouth_sync`：心声、画外音、电话音、广播音与口型和声音来源。
- `dialogue_pacing`：字秒比过快、过慢、慢语误用、长台词未拆。
- `generation_density`：强节拍过载、复杂动作时间不足、硬凑时长。
- `space_locking`：单组物理空间、组首空间锁定、人物可用性。
- `character_availability`：人物在组首、入场、遮挡、电话、画外音或屏幕来源上的可用性。
- `handoff_continuity`：相邻同空间组的组尾与组首状态衔接。
- `prop_continuity`：关键道具归属、位置、可操作状态和过渡动作。
- `horizontal_composition`：16:9 左右关系、前后景、画面平衡、双人/多人同框层次。
- `screen_direction`：左右站位、视线方向、对话轴线、无过渡换边。
- `blocking_continuity`：走位路线、遮挡关系、人物距离、场面调度连续性。
- `filmability`：不可视信息未转译、画面无法生成。
- `prompt_pollution`：模型说明词、模板化批量描述、参考图/首尾帧/视频延长等工程词进入正文。

## 输出要求

- 只返回 JSON。
- 不要输出 markdown、代码块或解释文字。
- `issues` 最多 5 条，只放 hard issues。
- `warnings` 最多 5 条，只放软问题。
- `checked_groups` 必须列出实际审过的全部组别，不能留空，不能只写“全部”。
- `audit_coverage` 至少包含以下字段，且全部写成 `"checked"`：`script_fidelity`、`dialogue_direction`、`timing_math`、`dialogue_pacing`、`space_locking`、`format`、`character_availability`、`handoff_continuity`、`filmability`。
- 横屏审核必须额外包含：`horizontal_composition`、`screen_direction`、`blocking_continuity`、`audio_mouth_sync`、`generation_density`、`prompt_pollution`。
- `spot_checks` 至少 3 条，优先覆盖台词节奏、横屏构图/轴线、空间/道具连续性、原剧本忠实度。
- `semantic_checks` 记录最关键语义审稿点；`result` 使用 `pass`、`warning` 或 `issue`。
- `pass=true` 时，`issues` 必须为空，且 `semantic_checks` 中不得出现 `result=issue`。
- `pass=false` 时，`issues` 必须包含阻断交付的 hard issue。

JSON 结构：

```json
{
  "pass": true,
  "summary": "一句话总结",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "说明该组如何建立画面左/右、前/后景、视线轴线和关键道具位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "说明具体台词字数、秒数、字秒比或连续对话节拍为什么合理。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "说明关键台词、动作、道具和人物关系如何保留原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "说明左右站位和视线方向如何连续。",
      "fix_instruction": "若不通过，说明应在哪个组尾或组首补充走位、换边过渡或中性镜头。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "说明关键道具从哪里到哪里，是否有可见过渡。",
      "fix_instruction": "若不通过，说明应补充递出、放下、拿起、推近、抢走或滑落等动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "说明强节拍数量和表演时间是否合理。",
      "fix_instruction": "若不通过，说明应拆组、延长动作链或压缩非关键动作。"
    }
  ],
  "issues": [
    {
      "severity": "hard",
      "group": "第1组",
      "rule": "horizontal_composition",
      "problem": "具体问题",
      "evidence": "具体证据",
      "fix": "可执行修改建议"
    }
  ],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "screen_direction",
      "problem": "不阻断交付的风险",
      "evidence": "具体证据",
      "fix": "可选优化建议"
    }
  ]
}
```

输出前强制交叉检查：只要 `semantic_checks` 中有任何 `result=issue`，就必须设置 `pass=false`，并把该问题写入 `issues`。不得在语义检查中标为 issue 却整体通过。
