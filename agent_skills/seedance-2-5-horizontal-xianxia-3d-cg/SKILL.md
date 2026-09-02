---
name: seedance-2-5-horizontal-xianxia-3d-cg
description: Route Seedance 2.5 single-mode 16:9 xianxia anime 3D CG storyboard work through its strict model, material, visual-preset, and native-audio contract.
---

# Seedance 2.5 横屏仙侠 3D CG Profile

这是模型与工作流的硬合同路由层，不负责替代 generator、reviewer 或项目设定包。

## 适用范围

- 只接受 `single + horizontal + 3d-cg`。
- 固定 `16:9 + 720p`，验收画幅为 `1280×720`。
- 每个模型生成单元必须显式使用 4–30 秒整数时长和整数秒时间轴。
- 要求原生音频，且提交前至少绑定一项有权使用的图片、视频或音频素材。
- 支持命名画风 preset；项目专属事实只能由单独 project pack 提供。

## 启动时读取

1. 始终读取 [references/model-contract.md](references/model-contract.md)，确认模型、请求映射、参数边界和证据边界。
2. 始终读取 [references/visual-presets.md](references/visual-presets.md)，按 run 元数据选择并锁定画风预设。
3. 始终读取 [references/segment-handoff.md](references/segment-handoff.md)，把相邻生成单元的世界状态作为连续性真源；尾帧只可作局部、可选的普通 reference。
4. 按 `TASK.md` 读取专属 generator 和 reviewer；它们负责横屏调度、仙侠特效语法、原生音频和真实审核。
5. 只有 run 显式声明 project pack 时才读取该项目包；通用 profile 不推断任何作品人物、法器、宗门或修炼规则。

## 硬边界

- 内部任务名保持 `multimodal_generation`；provider 创建请求由下游编译为 reference content，并写入 `omni_reference_task_type=reference`。
- 创建请求不得发送内部 `video_task_type` 或 `fps`；24 fps 是结果媒体 QA 条件。
- 禁止 provider 自动时长 `-1`、纯文本、首尾帧、关键帧、编辑、延长/续写和轨道补全。
- `final.txt` 是资产无关母版，不虚构素材编号、`@图片`、`@视频` 或 `@音频`。只有真实素材完成静态绑定、传输回写和门禁校验后才能编译提交包。
- 下游提交提示词必须把本组全部真实引用资产及职责按“人物资产／场景资产／道具与关键视觉资产”三类前置，再写完整整体画风说明、组间空间衔接、横屏空间和连续整数秒时间轴，最后只保留少量聚焦负面约束；不添加扁平资产列表或“一句话概述”。特效、光影、声音、物理约束和确有必要的镜头约束直接写在它们发生的时间段，不另设“视觉峰值/特效重点”“运镜强化词”或“Seedance执行提示补充”章节。不得从尾帧反推未入画人物、道具或空间状态。
- `final.txt` 的三类资产字段（`人物`、`场景`、`道具/关键视觉资产`）是资产增量与审核母版；真实素材绑定后，编译器将它们转换成带 `@图片N/@视频N/@音频N` token、逻辑键和职责说明的提交提示词。provider `content[0]` 仍是该文本，后续才是真实 reference content。
- 每组提交提示词必须有“整体画风说明”和“组间空间衔接”：前者完整锁定“写实材质＋克制卡通轮廓”及横屏国漫 3D CG 语汇，后者承接上一组冻结的世界末态并明确本组开场锚点。连续时间轴直接承载特效的来源→形态→路径→作用对象→反馈→收束→声音；不使用 `atmosphere`、`beat`、`hero` 标签或重复的结尾说明。连续性真源是文字世界状态，不是尾帧。
- 不预设运镜，也不设运镜数量指标。Seedance 2.5 会根据主体、动作、构图、空间关系和节奏自行选择合理运镜；只有剧情、轴线、复杂位移或连续性确实需要锁定镜头行为时，才在对应镜头正文中补充最少必要的镜头约束。固定机位、稳定中景和安静反应都可以成立。
- 本 profile 首期不接受 `scene`；不能回退到旧横屏 6–15 秒或 0.5 秒合同。
- 未通过账号、中转、素材权利和签收门禁时，保持 `submit_allowed=false`。
