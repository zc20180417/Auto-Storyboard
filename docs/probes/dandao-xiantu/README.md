# 《丹道仙途》Seedance 2.5 探针提示词归档

本目录保存历史探针提示词和此前的静态资产提示词，专门用于方案对比、回归讨论和后续实验复盘。这里的文本是提示词方案档案，不是视频证据，也不表示任何一次真实 Seedance 2.5 任务已经通过。

## 版本与来源

| 文件 | 版本定义 | 来源与真实性 |
|---|---|---|
| [probe-v0-initial.md](probe-v0-initial.md) | 最早一套完整三探针 | 会话记录 ordinal 4486 的 assistant 输出，原文复制；历史原文 |
| [probe-v1-first-preferred.md](probe-v1-first-preferred.md) | 资产前置的第一版 | 会话记录 ordinal 4534 的 assistant 输出；用户后来称“两版中前一版更好”；历史原文 |
| [probe-v2-current.md](probe-v2-current.md) | 按 Seedance 2.5 官方指南压缩的后一版 | 会话记录 ordinal 4691 的 assistant 输出；历史原文，文件末尾另记后续修订，不把修订冒充原文 |
| [asset-prompts-previous.md](asset-prompts-previous.md) | 之前使用的静态资产提示词 | 同时保留会话 ordinal 4517 的资产规格原文，以及项目中的 imagegen prompts.jsonl 原文 |
| [comparison.md](comparison.md) | v1、v2 与当前分镜/提交规则的阶段性对比 | 基于上述历史原文与当前 profile 合同整理；分析文档，不是历史提示词原文或视频证据 |

会话记录位置（本机历史证据源）：

`C:\Users\A\.codex\sessions\2026\08\31\rollout-2026-08-31T14-57-37-01a0569b-f72b-7760-94b0-4f77b322c67a.jsonl`

## 三类探针对应关系

- `ordinary-alchemy`：EP005，正常炼丹与失败前兆。
- `failed-alchemy-rewind`：EP003，焦渣 → 药液 → 原始药材的鼎内局部回溯。
- `yuanding-ability-reveal`：EP028，元鼎复苏、品阶提升但能力边界不扩张。

## 如何读这组档案

- v0 用来确认最早的详细动作/VFX基线；它没有把资产清单集中放在提示词最前。
- v1 用来确认“资产按人物/场景/道具职责前置、完整画风说明、详细时间线”的用户偏好。
- v2 用来确认官方指南式的“参考素材映射 → 概述 → 连续时间轴 → 声音 → 全程保持”压缩方向。
- 当前工作流并不是简单复制其中一版：当前 `final.txt` 是资产无关审核母版，下游编译器才生成真实素材绑定后的提交 prompt。当前规则吸收 v1 的资产职责和画风、v2 的正向结构与少量约束，并补充组间世界状态和动态 VFX 因果链。

## 证据边界

本目录不保存或伪造 Ark/CPA/ManJuWeb 任务 ID、素材上传回执、输出视频、媒体元数据或 QA 签收。当前项目仍未完成真实 Seedance 视频调用验证；离线分镜、逻辑素材绑定和本目录文本都不能替代真实视频证据。
