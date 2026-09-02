# Auto Storyboard Agent 入口

本文件用于固化已经验证过的“文件工作区式 Agent 工作流”，避免后续 agent 自作主张降级成脚本批量生成、伪造审核、或把多集合并到同一个上下文里。

如果本文件与项目脚本生成的 `DISPATCH_PROMPT.md` / `NEXT_STEPS.md` / `TASK.md` 冲突，以当前 run 的 `DISPATCH_PROMPT.md` / `NEXT_STEPS.md` / `TASK.md` 为准，因为它们是该工作区的具体任务书。

## 启动前硬检查

如果当前任务包含 2 集以上 episode，当前会话默认是 dispatcher。

dispatcher 禁止直接生产分镜正文。
dispatcher 禁止顺序处理多个 episode。
dispatcher 禁止写入 `episodes/ep*/draft.txt`、`episodes/ep*/final.txt`、`episodes/ep*/review.txt`、`episodes/ep*/status.json`。
dispatcher 必须创建 subagents/workers 并发分发，每个 worker 默认处理 1 集。

如果当前环境不能创建 subagent/worker，或者创建 worker 需要用户授权，必须立即停止并向用户请求分发授权，或按当前 run 的 `DISPATCH_PROMPT.md` 输出 `NEED_USER_DISPATCH` 和待分发 prompt 路径。

不得因为不能创建 subagent/worker，就降级为主线程顺序处理 episode。

## 先读这些文件

1. `README.md`
2. `README_AGENT_WORKFLOW.md`
3. 默认竖屏：`agent_skills/storyboard-generator/SKILL.md`
4. 默认竖屏：`agent_skills/storyboard-reviewer/SKILL.md`
5. 如果当前 run 的 `TASK.md` / `context.md` 标记 `Aspect: horizontal` 或 `storyboard_aspect=horizontal`，且没有标记 `video_profile=seedance-2.5-horizontal-xianxia-3d-cg`，改读 `agent_skills/storyboard-horizontal-generator/SKILL.md` 和 `agent_skills/storyboard-horizontal-reviewer/SKILL.md`，不要把横屏任务交给竖屏 skill。新 Seedance 2.5 横屏仙侠 profile 改按第 7 项读取专属 skill，不能同时加载带旧时长合同的通用横屏 skill。
6. 如果当前 run 标记 `Video profile: seedance-2.5-live-vertical` 或 `video_profile=seedance-2.5-live-vertical`，改读 `agent_skills/seedance-2-5-live-vertical-generator/SKILL.md`、`agent_skills/seedance-2-5-live-vertical-reviewer/SKILL.md` 和 `agent_skills/seedance-2-5-live-vertical/SKILL.md`；该 profile 只允许 `vertical` + `live-action` + `multimodal_generation`，真实调用至少绑定 1 项图片/视频/音频素材，禁止纯文本、参考生成、首尾帧/关键帧、编辑、延长/续写和轨道补全；不要再套用 2.0 的 6-15 秒、0.5 秒时间轴或固定大包 `--neg`。
7. 如果当前 run 标记 `Video profile: seedance-2.5-horizontal-xianxia-3d-cg` 或 `video_profile=seedance-2.5-horizontal-xianxia-3d-cg`，改读 `agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-generator/SKILL.md`、`agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-reviewer/SKILL.md`、`agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md` 及其 `references/`；显式启用 project pack 时还必须读 pack 的 `SKILL.md` 与其引用的事实源。该 profile 固定 `horizontal + 3d-cg`、`16:9`、720p、4-30 秒整数时长、原生音频和 reference-only provider 映射，首期只允许 `single`；不得回退到通用横屏 6-15 秒规则，也不得把离线 fixture 当成真实视频证据。
8. 其他 run 读取 `agent_skills/seedance-prompt-profile/SKILL.md`（Seedance 2.0 官方模板风格摘要，只做参考层，不得复制模板正文）。
9. 如需从分镜生成生图资产表，再读 `agent_skills/asset-extractor/SKILL.md` 和 `agent_skills/asset-reviewer/SKILL.md`
10. 如需执行三类真实探针，再读 `docs/seedance25-real-probe-protocol.md`、`tests/fixtures/seedance25/probe-evidence/protocol-contract-v1.json` 和 `tests/fixtures/seedance25/probe-evidence/qa-rubric-v1.json`；这些是证据/审核合同，不授权真实付费提交。
11. 三类探针先逐集运行 `workflow-status --episode-dir <episode-dir>`，再运行 `workflow-status --run-dir <run-dir>` 生成唯一 run/probe 汇总；缺可信 ManJuWeb verifier 时 run 命令返回 blocked 是正确结果，不得用本地 `lambda True` 或手写 run 文件解除门禁。

## 两种生产模式

旧版已验证流程支持两个模式，不是只有一种：

- `single`：整集一次生成，再整集审核一次。适合短集、单场景、文本长度低、模型一次性处理稳定的剧本。
- `scene`：按场景标题拆段，每段生成和审核，再组装成整集。生产默认优先用 `scene`，尤其适合长集、场景切换明显、剧情密度高的剧本。

选择规则：

- 用户明确指定 `single` 或 `scene` 时，按用户指定执行。
- 用户未指定时，默认使用 `scene`。
- 只有在单集很短、场景少、上下文不会压垮生成质量时，才主动选择 `single`。

创建工作区示例：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Force
```

```powershell
.\prepare-agent.ps1 single <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Force
```

## 调度规则

无论使用 `single` 还是 `scene`，质量单位永远是“单集”，调度单位可以是“单集”或“短集双集 batch”：

- 默认安全模式：1 集 / worker。适合长集、复杂集、多 scene 集、质量优先任务。
- 动态批处理模式：`prepare-agent` 可以把短集、单段、剧情密度低的相邻两集分到同一个 worker；当前默认阈值是脚本不超过 2500 字符且 scene 拆分后只有 1 段。
- 未经用户明确批准，不要超过 2 集 / worker。
- 最多同时运行 5 个 worker；如果使用 2 集 / worker，等价于最多同时推进约 10 集。
- 同一个 worker 处理 2 集时，必须先完整完成第一集的生成、审核、修复、校验，再处理第二集。
- 不要把 `ep01-ep08`、`ep09-ep16` 这类大范围交给一个 worker。
- 处理某个 episode 时，只能写入该 episode 目录，不要改其他集或其他输出目录。
- 两集同在一个 worker 时，也不能合并剧情、合并审核、合并输出或互相引用上下文。

如果当前环境要求用户授权才能创建 worker/subagent，必须先问用户确认。不能因为不能直接开 worker，就降级为脚本批量生成正文。

## Worker 必须做的事

worker 启动时必须完整读取当前 run 指定的两份标准 skill 和 profile；同一 worker、同一 run 内这些文件未变化时只读一次，不在生成、审核、修复复审或第二集之间重复加载。worker 处理的每个 episode 都必须：

1. 读取自己的 `TASK.md`、`agent_prompt.md`、`script.txt`；复用本 worker 已加载且未变化的标准 skill。
2. 按 `TASK.md` 的 `Mode` 执行，不要自行改模式。
3. 使用 `TASK.md` 指定的 generator skill 生成分镜草稿，不按 aspect 猜测或覆盖 profile 路由。
4. 使用 `TASK.md` 指定的 reviewer skill 做真实审核，审核必须对照原剧本和当前分镜逐项检查。
5. 只修 reviewer 指出的 hard issues，不做无关重写。
6. 修复后必须再次使用当前 run 指定 reviewer 复审，不能只跑格式校验。
7. 写出该模式要求的全部文件。
8. 运行 `TASK.md` 中的 `validate-episode` 命令直到通过，或在确实无法修复时标记 `needs_review`。

`single` 模式要求：

- `final.txt`
- `review.txt`
- `status.json`

`scene` 模式要求：

- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`
- `final.txt`
- `review.txt`
- `status.json`

仅当当前 run 的 `TASK.md` / `episode.json` 标记 `vertical_review_contract_version >= 3` 时，整集 `final.txt` 通过 pre-check 后还会生成 `review_facts.json`；它不是 v2 或横屏 run 的必需输出，也不得手写。`scene` 的 segment 审核发生在整集事实文件生成之前，不读取或输出该文件。

### Reviewer 硬门槛

`review.txt` 和 `segments/segXX/review.md` 必须是真实审核结果，不能写占位文本、JSON、或伪造通过状态。`validate-episode` 只是客观格式校验和 reviewer 证据校验，不能替代真实审核。

真实审核必须满足以下证据要求：

- reviewer 必须读取并对照同一 episode 的 `script.txt` 和当前待审 draft/final；只有 vertical review contract v3 的整集审核额外读取 pre-check 生成的 `review_facts.json`。当前 run 指定的标准 skill 可复用本 worker 已完整加载且未变化的版本，不能用已有 review/status 代替。
- vertical review contract v3 的整集审核必须用紧凑 `semantic_coverage` 列出实际逐项核对的对白镜头、相邻组/跨集接缝和明确运镜；存在跨集边界时，还必须在 `semantic_checks` 写出第1组与上一集实际末态的具体连续性证据。
- vertical review contract v3 的跨集 pre-check 会把上一集实际 `final.txt` 的集号和哈希绑定到 `review_facts.json`；上一集不存在时不得先审本集，上一集后续有修改时本集必须重新 pre-check 和复审。
- `scene` 模式下，每个 `segments/segXX/review.md` 必须是该 segment 草稿的真实 reviewer JSON；整集 `review.txt` 必须是组装后 `final.txt` 的真实 reviewer JSON。
- reviewer 至少检查：原剧本台词是否漏删改、人物关系是否错置、对话对象是否明确、组首空间锁定是否完整、组尾衔接是否自然、组时长和镜头时长是否符合规则、是否新增剧情或模板化描述。
- 如果 reviewer 没有逐项审查，不允许写 `pass: true`；应写 `status: "needs_review"`，并在 `hard_issues_remaining` 中说明“reviewer 未完成”。
- 如果 reviewer 返回 hard issues，必须先局部修复对应组，再复审；复审前不允许把 `status.json` 写成 `done`。
- 不允许把 `validate-episode`、`SUMMARY.md`、脚本检查、人工粗看、或空 issues JSON 当作 reviewer 结果。
- 交付说明必须明确写出：哪些 episode 已执行真实 reviewer，哪些 episode 修过 hard issues，哪些仍为 `needs_review`。

## Python / 脚本边界

允许脚本做：

- 准备工作区。
- 拆分或镜像输入文件。
- clean-format / reviewer 证据校验。
- 为 vertical review contract v3 生成只含当前 final 哈希、机械计数，以及跨集时上一集 final 绑定信息的 `review_facts.json`。
- 收集结果。
- 统计 SUMMARY。

禁止脚本做：

- 批量生成分镜正文。
- 批量伪造 `review.txt`、`segments/segXX/review.md` 或 `status.json`。
- 把剧本文本套模板改写成分镜。
- 用脚本替代 worker 的生成、审核、修稿。
- 让 Python 调用 Codex CLI、Qwen CLI、Claude Code、Kimi Code 或任何模型 CLI。

## 质量底线

最终分镜必须是自然中文分镜文本，不要输出 JSON、调试标记或其他非分镜正文内容。

禁止模板化批量稿，尤其是这类表达：

- “空间先被交代出来”
- “镜头从场景布局转向在场人物”
- “视线关系落在当前冲突中心”
- “人物面部肌肉随局势绷紧”
- “眉头和嘴角随情绪细微变化”

普通空间 / 环境交代镜头通常 2 秒；只有原剧本明确存在连续动作时才可到 3 秒。不能用 3 秒环境镜头批量凑组时长。

视频执行稳定性同样是质量底线：单个时间段默认只承载一个主动作目标；同一主体、同一空间、同一目标且顺序和结果清楚的紧凑动作链可在 2-3 秒完成，不按动词数量机械拆段。只有多个主体/目标争抢画面、关键状态不清、明显跨位移、重物搬运、多人协同或精细操作时，才按真实需求拆段或加时。保护型动作必须写清挡在谁前面；非主动作人物不能抢戏；关键道具要写清归属、位置和状态变化。外部事件进入（车辆抵达、门打开、人员下车、群众反应、主角对峙等）要按必要阶段拆开。高冲击打断（喝止、闯入、身份揭露、证据亮出等）后，先稳定打断/反应，再处理放下道具、跨位移、保护站位、团圆确认等归位动作；不能把这些压成一个短组。普通竖屏/横屏规则下，每个镜头都可以合理运镜，也可以固定机位，不设数量指标；需要预写镜头运动时再写清动机、主体、路径和落点，并与人物动作、构图和连续性兼容。`seedance-2.5-horizontal-xianxia-3d-cg` 是例外：Seedance 2.5 可根据主体、动作、构图、空间关系和节奏自行选择运镜，不因没有显式运镜词判错，只有剧情、轴线、复杂位移或连续性确实需要锁定时才补充最少约束。复杂动作、保护站位或关键道具组可在 `final.txt` 写 `视频禁止项：...`，每组只写 2-5 个具体剧情错误，且每条必须锚定本组人物名、关键道具名、场景名，或本集全文已出现的人物/道具；收集阶段会并入该组 `--neg`。视频禁止项的少量全局模板词、上下文锚点停用词和数量限制由 `agent_skills/storyboard-quality-policy.json` 管理，不要为单个剧硬编码独立词表。

## 校验与收集

收集前必须先确认每集已完成真实 reviewer：

- 查看每集 `review.txt`，确认它是按当前 run 指定 reviewer 对照原剧本和 `final.txt` 生成的审核 JSON。
- 查看 `status.json`，确认 `reviewer_source` 与当前 run 的 `TASK.md` 指定 reviewer 完全一致，且 `reviewer_pass`、`reviewer_issues_count`、`reviewer_warnings_count` 与 `review.txt` 一致。
- 如果发现 `review.txt` 是占位、空 issues 伪通过、只来自脚本校验、或没有真实审稿过程，必须停止收集，重新审核该 episode。
- 只有真实 reviewer 通过或明确标记 `needs_review` 的 episode，才能进入收集；不能把未审核 episode 包装成 `done`。

校验单集：

```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\<run-name>\episodes\ep01
```

收集最终输出：

```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

当前除 Seedance 2.5 外默认只收集分镜 `.txt`，不导出、不复制 `storyboard_index.json` / `storyboard_index.xlsx`。`seedance-2.5-live-vertical` 完整校验后必须自动保留并收集索引；其他 profile 只有资产或 Web 链路明确需要索引时，才显式使用 `-ExportIndex` 或 `export-storyboard-index`。

## 资产表生成

分镜完成后，如用户需要给其他 AI 生图/视频模型提前准备资产，使用 `agent_skills/asset-extractor/SKILL.md` 从单集 `final.txt` 生成资产表，并使用 `agent_skills/asset-reviewer/SKILL.md` 做真实审核。

资产表生成规则：

- 输入必须是已经完成的单集分镜 `final.txt`。
- 输出写入该集目录下的 `assets.md`、`assets.xlsx`、`asset_review.json` 和 `asset_status.json`，不要改写 `final.txt`。
- 资产表是“资产增量与使用索引”，不是逐集完整资产表；必须包含：本集复用资产索引、本集新增资产状态、本集新增基础资产、本集关键道具与场景状态、本集不建议入库元素。
- 基础人物、基础场景、基础服装、基础道具只入库一次；同一角色/场景/道具的脏污、夜雨、受伤、换装、破损、盖章等变化新增 `state_id`，不要重复写成新的基础资产。
- 资产表继续使用 Markdown + Excel 输出，不使用 HTML；新增基础资产和新增状态的提示词列拆成 `静态生图提示词(中文)`、`负面提示词(中文)`、`静态生图提示词(英文)`、`负面提示词(英文)`。
- 多集项目必须先维护 run 级别 `asset_bible.md`，再分集生成资产表。推荐路径：`agent_runs/<run-name>/asset_bible.md`。
- `asset_bible.md` 用于固定跨集人物全身装造、面部稳定特征、核心场景、关键道具和服装状态。分集 worker 必须读取它，不能在不同集里随意改变同一人物的脸型、发型、体态、主服装颜色。
- 基础人物资产只记录身份、脸、体态、发型、气质；服装细节由服装资产或人物状态引用，不要在每集自由重写。
- 场景基础资产和场景状态必须为空镜；场景状态用于记录白天、夜雨、断电、爆炸后、整洁后、破损后等变化。
- 短暂表情、眼神、手势、台词动作、一次性背景杂物、普通桌椅门窗通常不入库，应写入“本集不建议入库元素”或由分镜即时生成。
- `适用镜号` 必须来自分镜原文，不得杜撰。
- 资产抽取不得替代分镜审核，也不得改变分镜生产结果。
- `asset_review.json` 必须来自 `asset-reviewer` 对照 `final.txt`、`assets.md`、`asset_bible.md` 和相关 skill 的真实审核；不能用 Excel 转换、脚本检查或空 issues JSON 伪造通过。
- 转换 Excel 后必须运行 `node .\agent_skills\asset-extractor\scripts\validate-assets.mjs <episode-dir>` 做机械门禁校验。
- `seedance-2.5-live-vertical` 在资产门禁通过后运行 `export-seedance-material-requirements`；`asset_bindings.json` 只代表逻辑静态绑定，不能冒充真实多模态素材。Auto-Storyboard 的本地清单不得写 Ark 字段，ManJuWeb 回写 `ark_sync_results.json` 后再运行 `validate-seedance-materials` 和 `export-seedance-package`。只有 `generation_ready=true`、`submit_allowed=true` 才可提交模型任务。
- 只有 `asset_status.json` 中 `status=done`、`reviewer_source=asset-reviewer`、`reviewer_pass=true`、`reviewer_issues_count=0` 的资产可以收集。

资产阶段调度规则：

- 资产抽取不同于分镜生成，可以在保证 `asset_bible.md` 已稳定的前提下提高 batch。
- 默认推荐：3 集 / worker。
- 单集短、场景和人物复用度高、前 1-2 个资产 worker 结果稳定后，可用 4 集 / worker。
- 未经用户明确批准，不要超过 4 集 / worker。
- 同一个 worker 处理 3-4 集时，必须逐集闭环：先完成某集 `assets.md`，用 `asset-reviewer` 审核，局部修复 hard issues 并复审，写 `asset_status.json`，转换 `assets.xlsx`，运行 `validate-assets.mjs`，再处理下一集。
- worker 可以读取全局 `asset_bible.md`，但不要并发写它；新增人物/服装/场景/道具在 `assets.md`、`asset_status.json` 或交付说明中标记，最后由主线程统一合并。

## 当前生产参考

- 最新已验证 `scene` 工作区：`agent_runs/youyuanzhai6-scene`
- 最新已验证 `single` 工作区：`agent_runs/youyuanzhai-single`
- 当前竖屏主生成规则：`agent_skills/storyboard-generator/SKILL.md`
- Seedance 2.5 真人竖屏独立 profile：`agent_skills/seedance-2-5-live-vertical/SKILL.md`；唯一任务是 `multimodal_generation`，生成器与审核器分别为 `agent_skills/seedance-2-5-live-vertical-generator/SKILL.md`、`agent_skills/seedance-2-5-live-vertical-reviewer/SKILL.md`。
- 当前横屏主生成规则：`agent_skills/storyboard-horizontal-generator/SKILL.md`，审核规则为 `agent_skills/storyboard-horizontal-reviewer/SKILL.md`，只在横屏 run 中使用。
- Seedance 风格参考层：`agent_skills/seedance-prompt-profile/SKILL.md`，只用于选择性参考官方模板结构，不得替代主生成规则。
- 不再默认使用 `6688竖屏古装分镜prompt.txt` 覆盖生成 skill；只有用户明确要求临时替换生成规则时，才可使用 prompt override。

旧 GUI/API 文件已归档到 `legacy/`。除非用户明确要求恢复旧流程，否则不要使用归档文件。
