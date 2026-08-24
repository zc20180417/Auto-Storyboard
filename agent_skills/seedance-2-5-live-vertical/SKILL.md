---
name: seedance-2-5-live-vertical
description: Apply the multimodal-generation-only Seedance 2.5 live-action vertical short-drama model contract in Auto-Storyboard. Use when a run selects video profile seedance-2.5-live-vertical or targets doubao-seedance-2-5-260628 for 9:16 live-action drama with actual image, video, or audio inputs and native audio.
---

# Seedance 2.5 真人竖屏短剧 Profile

把本 Skill 当作模型硬合同，不要当作通用写作模板。它把视频任务固定为唯一的 `multimodal_generation`，并覆盖 Seedance 2.5 特有的参数、时长、时间轴、素材职责、原生音频和收集尾部；原剧本忠实、空间锁定、可拍性、连续性、`cut_id` 与真实 reviewer 证据仍由本 run 的 generator/reviewer Skill 负责。

## 适用边界

- 仅在 run 明确选择 `seedance-2.5-live-vertical` 时启用。
- 目标模型固定为 `doubao-seedance-2-5-260628`。
- 仅支持 `vertical` + `live-action`，画幅参数固定为 `9:16`。
- 本 profile 唯一支持 `multimodal_generation`；不开放其他视频任务类型。
- 不得把本 profile 的规则回写到旧 `seedance-2.0` 默认流程。

完整机器合同和官方来源见 [references/model-contract.md](references/model-contract.md)。

## 唯一任务合同

- `video_task_type=multimodal_generation`，没有可切换的次级模式。
- 每次真正调用模型前必须绑定至少 1 项真实、可用且有权使用的图片、视频或音频素材；只有剧本文本时不得回退为纯文本/文生视频。
- 图片、视频、音频是本次多模态生成的输入素材，不把它们另称为“参考生成”任务。
- 明确禁止：纯文本生成、参考生成、首尾帧/关键帧生成、视频编辑、视频延长/续写、轨道补全。
- 视频文件可以作为输入素材提供动作、节奏、运镜或其他明确职责，但不能作为待编辑或待延长的目标视频。
- `final.txt` 是资产无关的分镜母版；未取得真实多模态素材绑定时只能继续准备素材，不能宣称已可发起模型生成。Auto-Storyboard 负责逻辑需求、文件完整性与生成包编译，ManJuWeb 是 Ark 上传状态和 `assetId` 的唯一权威来源，详见下方「仓库边界」。

## 硬参数合同

- 单次生成片段：4-30 个整数秒。
- 模型可见时间轴：只使用整数秒边界；内部可先精确估时，最终再整理成整数秒阶段。
- 默认分辨率：720p；当前 profile 只开放 480p、720p。
- 输出帧率：24 fps。
- 原生音频：`generate_audio=true`。
- 参数分离：画幅、时长、分辨率、帧率、是否生成音频由工作区元数据/API 参数控制，不要写进自然语言镜头正文。
- 不得用“4K画质”冒充分辨率参数，也不得在 profile 未升级前擅自启用 1080p。

## 短剧分组合同

1. 先按原剧本自然表演容量切剧情块，再决定片段长度。
2. **每组是一次独立生成，组与组之间的接缝是连贯性风险最高的地方**（人物位置、道具、光线、口型都可能在接缝处失配）。在内容真的连续时，**更少更长的组优于更多更短的组**。
3. **16-30 秒是同一主要空间、同一冲突目标下连贯长段的首选区间**，不是例外情况。同场同目标的连续流程（拨打/夺取/递出/登记/复核/追问/僵持等）应优先合并成一个长组，而不是逐步切成多个短组。
4. 8-15 秒用于无法再向前后合并的独立剧情块：换空间、换冲突目标、换在场人物，或与相邻组之间确有叙事停顿。
5. 4-7 秒只用于确有必要的短打断、单句反应、道具插入、短动作余波或片尾意象。
6. 16-30 秒组必须分成清楚阶段，每阶段只保留一个主要状态变化，并写明阶段结束状态。
7. 合并的前提是内容本身连续，**不是把稀薄内容拉长**。不得为了凑长度新增凝视、沉默、无信息停顿或普通微表情；也不得把多个并列冲突、跨空间动作、多人协同和多个关键揭示塞进一段。内容不够就老实用 8-15 秒。
8. 普通空间/环境交代通常 2 秒；只有原剧本明确连续动作时才可到 3 秒。

## 模型友好结构

按以下顺序组织每组信息，但保持 Auto-Storyboard 的自然分镜格式：

1. 人物、场景、关键道具。
2. 第一帧可生成的组首空间锁定。
3. 组内整数秒时间段，逐段写主体、动作目标、镜头、台词/声音和结束状态。
4. 组尾衔接。
5. 收集阶段追加真人短剧画面/声音尾部；必要时再把本组具体 `视频禁止项` 转成聚焦负面词。

长段按“建立 -> 推进 -> 转折/打断 -> 结果”分阶段。每个阶段写清谁在做什么、镜头为何运动、动作落到哪里、谁说话、声音从哪里来。关键动作可以具体，普通动作使用可见结果表达，不要堆动词。

## 原生音频合同

- 保留原剧本现场对白原文和说话对象，口型镜头给足自然时长。
- 心声、旁白、电话音、广播音、门外音与现场开口分开写；心声/旁白由画面人物承载时写明闭口、不做口型。
- 写清必要环境音和剧情音效的来源与发生时点。
- 默认不添加字幕和背景音乐；不要用大包负面词替代声音设计。
- 对话、动作和音效必须能在同一阶段内同步完成；不能用画外音掩盖被压缩的关键表演。

## 多模态素材职责

- 只引用真实存在且有权使用的上传素材；不得虚构 `@图片N`、`@视频N`、`@音频N`。
- 下游生成提示词必须按实际上传顺序引用素材，并明确每个素材“提供什么”和“不提供什么”。
- 优先遵守用户给出的素材映射；没有职责的实际素材列为“未采用素材”，不要硬塞进正文。
- 角色素材只负责身份、脸、体态、发型或服装状态；场景素材只负责空间与材质；道具素材只负责外观与状态；视频/音频素材必须写清动作、节奏、运镜或声音职责。
- `final.txt` 是资产无关的分镜母版，不手写控制台占位符。只有 ManJuWeb 返回与本轮清单哈希一致的 Active Ark 结果后，Auto-Storyboard 的确定性编译器才生成带 `@素材` 的生成包。
- 没有任何实际素材绑定时必须标记为未就绪，不得用剧本文本单独发起模型调用。

## 仓库边界与交接文件

- Seedance 2.5 整集校验通过后，本仓库自动保留 `storyboard_index.json` / `storyboard_index.xlsx`；收集结果时也自动带上索引。每组使用稳定 `cut_id`，例如 `EP01-G01`。
- `asset_bindings.json` 仍是 `cut_id -> 逻辑资产/状态` 的静态绑定，**单独存在不满足**真实多模态输入要求。它当前只有 `scene_reference`、`character_reference`、`costume_reference`、`prop_reference`、`composition_reference` 五种静态参考图角色；`use_for_video=yes` 表示该图片可用于视频生成，不表示它是视频素材。
- Auto-Storyboard 从可用于视频的静态绑定编译 `seedance_material_requirements.json`，并维护不含任何 Ark 字段的 `seedance_local_materials.json`。前者说明每个 `cut_id` 需要什么、参考什么和不参考什么；后者只记录本地文件/公网 URL、MIME、SHA-256 与授权确认。
- ManJuWeb 接收上述两份 JSON 和实际素材，复核文件 SHA-256、复用或上传 Ark、轮询到真实状态，再回写 `ark_sync_results.json`。Ark 状态和 `ark_asset_id` 只能由 ManJuWeb 维护，Auto-Storyboard 不复制上传、轮询、密钥或状态机逻辑。
- Auto-Storyboard 只在 `final.txt`、`storyboard_index.json`、素材需求、本地素材清单和 Ark 回写结果的哈希全部匹配，并且每个 `cut_id` 至少有一项 Active 素材时，编译 `seedance_generation_package.json`。任一输入变化，旧生成包立即失效；`generation_ready=false` / `submit_allowed=false` 时禁止提交模型任务。
- 当前 MVP 从 `asset_bindings.json` 自动编译静态图片职责。动作视频、运镜视频和声音素材角色已在交接合同中预留 `video` / `audio` 类型，但不从现有静态绑定中猜测，也不会把图片错误冒充视频或音频。
- 使用真人脸素材前确认授权、合规来源和平台可接受性；不明来源的真人脸不得进入生成任务。

单集交接命令：

```powershell
python .\storyboard_agent_workspace.py export-seedance-material-requirements --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py validate-seedance-materials --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py export-seedance-package --episode-dir <episode-dir>
```

完整 JSON 合同和 ManJuWeb 边界见 `docs/seedance-material-handoff-v1.md`。

## 负面约束

- 不追加旧版大包通用 `--neg`。
- 只有复杂动作、保护站位或关键道具存在明确生成风险时，写 2-5 个本组特有错误。
- 每条必须锚定本组人物名、场景名、关键道具名或本集已出现实体。
- 禁止项不能反向禁止原剧本必须发生的动作，也不能机械复制到所有组。

## 冲突优先级

发生冲突时按以下顺序处理：

1. 原剧本事实、台词、因果与人物关系。
2. `seedance-2.5-live-vertical` 的模型特定硬合同。
3. 本 run 的 generator/reviewer 可拍性、空间、连续性与证据合同。
4. 普通审美偏好。

旧 Skill 中只要出现“Seedance 2.0”“6-15 秒硬范围”“0.5 秒模型时间轴”“固定 4K 尾部”“每组固定大包负面词”，在本 profile 下均由本 Skill 对应条款替换；其他剧情质量规则继续生效。

## 交付自检

- profile、模型 ID、9:16、720p/480p、24fps、原生音频是否写入工作区元数据，而非正文。
- `video_task_type` 是否严格等于 `multimodal_generation`，且实际模型调用至少绑定 1 项图片/视频/音频素材。
- 是否完全没有纯文本、参考生成、首尾帧/关键帧、编辑、延长或轨道补全任务指令。
- 每组是否处于 4-30 秒，并使用整数秒边界。
- 16-30 秒组是否真的有容量、分阶段、每阶段只有一个主要状态变化。
- 对白原文、对象、口型、画外声音来源是否正确。
- `final.txt` 是否没有虚构素材编号、API 参数、模板说明或大包通用负面词。
- reviewer 是否使用本 profile 的独立 reviewer，并完成真实逐项证据审核。
