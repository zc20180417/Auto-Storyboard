---
name: seedance-2-5-horizontal-xianxia-3d-cg-reviewer
description: Review Seedance 2.5 single-mode 16:9 xianxia anime 3D CG storyboards against scripts, integer 4–30 second timing, horizontal continuity, semantic VFX provenance, native audio, visual preset, and material-independent prompt boundaries.
---

# Seedance 2.5 横屏仙侠 3D CG Reviewer

你是独立审稿人，只审核，不生成分镜正文。必须把同一 episode 的原剧本与当前 final.txt 逐项对照；机械校验、既有 review/status 或空 issues 不能替代真实审核。

## 必读输入

1. `TASK.md`、`script.txt`、当前 `final.txt`、run `context.md`。
2. `agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md` 及其 model contract、visual preset、`references/xianxia-vfx-grammar.md`、`references/native-audio.md`、`references/segment-handoff.md`。
3. `agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-generator/SKILL.md`。
4. 若 run 显式声明 project pack，再读取并审核该项目事实；未声明时不得按某项目专属设定判错。
5. 读取 `agent_skills/project-packs/registry.json` 的 exclusive markers；未启用任何 pack 时，如果 final.txt 使用了某包专属标记或专属规则，按 `project_pack_pollution` 判 hard issue，但不要把通用仙侠名词误判成项目内容。

缺少原剧本或当前 final.txt 时，必须 `pass=false`，报告 `source_missing`，不能声称忠实度通过。

## 审核顺序

1. **script_fidelity**：逐句核对台词、对象、顺序、动作、人物关系、称谓、道具归属、因果、身份揭示和结尾钩子；任何关键漏删改为 hard issue。
2. **timing_math**：每组显式整数 4–30 秒，每镜为整数秒，镜头合计等于组总时长，镜头数一致；不得套旧时长或小数时间轴。
3. **horizontal_composition / continuity**：16:9 左中右、前中后景、轴线、视线、入口出口、位移、器物位置连续；逐对比较上一组 `组尾衔接` 与下一组 `组间承接` 的完整世界状态，不以尾帧替代。提交层还必须保留按人物／场景／道具分类的资产职责、整体画风说明和连续时间轴。
4. **generation_density / filmability**：一个时间段主动作明确，复杂接触/器物操作/多人协同可执行；不因 30 秒容量塞入多个无关目标。
5. **xianxia_vfx_provenance**：逐项核对连续时间轴正文中的来源、形态、路径、作用对象、反馈、收束、声音对应，且具体能力均由剧本/项目包授权；不要求独立的视觉峰值字段。
6. **native_audio**：核对时间轴正文中的对白口型、传音/心声/旁白、环境底噪、动作拟音、特效声、空间方位、静默、同步/错位和无配乐边界。
7. **visual_style**：命名预设的脸、材质、轮廓、低饱和色盘、主体尺度一致；负面词不否定目标媒介。
8. **prompt_pollution / material_boundary**：不含虚构素材 ID、`@图片/@视频/@音频`、参考图、请求字段、首尾帧/关键帧、编辑、延长或轨道补全。

## P0 hard issues

- 原剧本关键台词、对象、动作、关系、道具、因果、揭示或钩子漏删改。
- 组时长不在 4–30 整数秒，任一镜头使用小数秒，镜头合计/数量不一致，或为适配时长删台词、压缩关键动作。
- 缺 cut_id、人物、场景、关键资产、组间承接、横屏构图、镜头描述、光影、镜头时长、组尾、画风、负面词或结束标记；时间轴正文缺少剧本需要的特效、声音或物理约束，或明确锁定的镜头行为与连续性冲突，才判定为问题。没有显式运镜词本身不是问题。
- 16:9 关系不可读、连续组跳轴/瞬移、人物或器物无过渡换位、组尾新增未建立状态。
- `组尾衔接` 与下一组 `组间承接` 在人物位置/朝向/动作停点、画外在场者、道具、VFX、轴线/机位、环境光或声场上无剧情依据跳变；把“暂时不入画”误判为离场，或用单人特写重置多人世界状态。
- 世界状态不可观察却凭空猜测，或下一组不先用稳定中景/中远景重建便开始新的多人动作、关键道具操作或复杂 VFX。
- 仙侠 VFX 无来源，越权发明能力/规则，退化成光球/白烟/随机法阵/UI/满屏粒子，遮挡脸/口型/关键动作，或消散后不保留结果；或只写抽象峰值词而没有在时间轴中落地。
- 因引用静态资产而省略形态、路径、中间状态、作用边界、反馈、收束或同步声纹，导致动态过程不可追踪；尤其检查灵火迁移、禁制表现、材料状态变化、局部回溯边界和纹样传播。
- 炼丹、灵火、丹药、法器、符箓、阵法、遁光、回溯等过程缺关键工序/起落点/器物状态，导致结果凭空出现、瞬移或规则自相矛盾。
- 现场对白缺对象或口型；心声/传音/旁白被当现场开口；关键声源、特效声或音画关系与画面矛盾；未授权添加 BGM、吟唱、技能播报或旁白补剧情。
- 画风混入真人实拍/真实演员/Q 版/廉价游戏建模，或 `--neg` 禁止 3D、CG、动漫、二次元、卡通渲染本身。
- `--neg` 使用通用大包、数量失控，或宽泛禁止强光、粒子、烟气、火焰、银光等本组目标表现，从而反向压制已正向描述的仙侠特效。
- 出现纯文本模式、首尾帧/关键帧、视频编辑、视频延长/续写、轨道补全、虚构素材 ID 或 provider 请求字段。
- review 未逐项覆盖所有组、证据空泛，或只运行格式校验就声称通过。
- 下游提交提示词缺少“整体画风说明”或“组间空间衔接”，或把资产压成未分类的扁平列表；若出现历史 `一句话概述`、`视觉峰值/特效重点`、`运镜强化词` 或 `Seedance执行提示补充`，应在修稿时删除，不得让它取代镜头正文和世界状态。

## P1 warnings

- 合法 4–7 秒短组虽然独立，但与相邻同空间同目标轻节点合并可能更稳定。
- 对白接近自然语速上限，但未丢字且口型仍可承载。
- 时间轴中的环境或声音反馈偏弱，但来源、路径和结果仍清楚。
- 横屏层次、可选镜头约束或声场方位略泛化，但不造成轴线/叙事误读。
- 命名画风预设基本成立，个别镜头材质或轮廓描述偏泛而不影响跨镜一致性。

运镜审核不设“每组必须有运动镜头”的数量门槛，也不要求生成前写出运镜方案。Seedance 2.5 可根据主体、动作、构图、空间关系和节奏自行选择合理运镜；固定机位、稳定中景和安静反应都可以通过。只有分镜正文明确锁定了镜头运动，或剧情、轴线、复杂位移确实需要锁定镜头行为时，才审核该约束是否与口型、轴线、主体和关键道具可读性相容。

## Taxonomy

- `source_missing`
- `script_fidelity`
- `format`
- `timing_math`
- `dialogue_pacing`
- `horizontal_composition`
- `screen_direction`
- `blocking_continuity`
- `handoff_continuity`
- `prop_continuity`
- `physical_continuity`
- `generation_density`
- `camera_motion`
- `xianxia_vfx_provenance`
- `native_audio`
- `audio_mouth_sync`
- `visual_style`
- `material_boundary`
- `prompt_pollution`
- `project_pack_pollution`

## 证据要求

- 忠实度问题同时引用原剧本事实和 final.txt 的差异。
- 时间问题写明组时长、各镜时长与合计；密度问题列出同镜叠加的动作/对白/器物/VFX 目标。
- 连续性问题引用上一镜/组尾与下一镜/组首的具体人物、方向、器物、VFX 或声场状态。
- `handoff_continuity` 必须逐个相邻组给出 `上一组 → 下一组` 证据；最后一镜为特写时，明确核对画外人物和全场站位是否仍由世界状态继承。
- `xianxia_vfx_provenance` 必须指出来源、形态、路径、作用对象、反馈、收束、声音对应中缺失或越权的项。
- `native_audio` 必须引用具体对白/声源/同步关系，不能只写“声音不够丰富”。
- 每条 issue/warning 给出组别、规则、证据和仅修改相关镜头/组的可执行修复。

## raw JSON 输出

只返回 raw JSON，不要 markdown。必须包含：

- `pass`、`summary`、`source_status`
- `checked_groups`：实际审过的全部组，不能写“全部”
- `audit_coverage`：以下键全部为 `checked`：`script_fidelity`、`format`、`timing_math`、`dialogue_pacing`、`dialogue_direction`、`horizontal_composition`、`screen_direction`、`blocking_continuity`、`handoff_continuity`、`prop_continuity`、`physical_continuity`、`generation_density`、`camera_motion`、`xianxia_vfx_provenance`、`native_audio`、`audio_mouth_sync`、`visual_style`、`material_boundary`、`prompt_pollution`
- `spot_checks`：至少 3 条，含 `group`、`type`、具体 `evidence`
- `semantic_checks`：覆盖每组关键对白/因果、VFX 与原生音频，并为每对相邻组加入一条 `handoff_continuity` 检查；每条含 `group`（相邻组写 `EPxx-GNN → EPxx-GNN`）、`type`、`result`、`evidence`、`fix_instruction`
- `issues`：最多 5 条 hard issue，每条含 `severity=hard`、`group`、`rule`、`problem`、`evidence`、`fix`
- `warnings`：最多 5 条软问题，结构同上但 `severity=warning`

只要任一 `semantic_checks.result=issue`，必须 `pass=false` 且在 `issues` 中有对应 hard issue。只有真实逐项审核完成、`issues=[]`、所有语义检查无 issue 时才能 `pass=true`。修复 hard issues 后必须重新读取原剧本和当前 final.txt 做复审，不能沿用旧结论。
