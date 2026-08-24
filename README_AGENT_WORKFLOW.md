# Agent 分镜生产工作流

这套流程已经作为项目的生产主流程：Python 不负责调用模型，也不负责启动 Codex/Qwen/Claude CLI；Python 只做文件工作区准备、客观格式校验和结果收集。真正的分镜生成、审核、局部修复由 Codex、Claude Code、Qwen Code 这类 agent 在自己的会话里完成。

## 为什么用这套流程

- 生成和审核在同一个 agent 会话里完成，避免“换会话越修越歪”。
- 每集是独立任务，可以并发；每集内部可按场景拆段，降低长剧本文本漂移。
- Python 只检查客观边界：文件是否存在、自然格式是否干净、是否能收集结果。
- 最终稿是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
- 默认 `seedance-2.0` 竖屏固定尾部“画面风格”和基础 `--neg` 由 Python 收集阶段统一拼接；独立 `seedance-2.5-live-vertical` 改为专属真人画面/原生声音尾部，不追加旧版大包通用 `--neg`。worker 的 `final.txt` 都不需要逐组重复固定尾部。
- 复杂动作、保护站位、关键道具连续组可以在 `final.txt` 写 `视频禁止项：...`；收集阶段会把它并入该组 `--neg`。每组只写 2-5 个具体剧情错误，且每条必须锚定本组人物名、关键道具名、场景名，或本集全文已出现的人物/道具；不要写“人物换位”“道具消失”“场景变形”这类无锚点通用词。
- 视频禁止项质量规则由 `agent_skills/storyboard-quality-policy.json` 管理，Python 校验读取该 policy 的泛泛词、占位词、数量限制和上下文锚点停用词，再结合本组 `人物/道具/场景` 和本集全文上下文做锚点检查，避免为不同剧维护不同硬编码词表。
- 失败也保留 `draft.txt`、`review.md`、`final.txt` 和 `status.json`，方便人工或 agent 继续接力。

## 目录约定

- `inputs/`：原始剧本文档或文本。
- `split_scripts/`：拆好的一集一集剧本文本。
- `agent_skills/storyboard-generator/SKILL.md`：默认竖屏生成 skill。
- `agent_skills/storyboard-reviewer/SKILL.md`：默认竖屏审核 skill。
- `agent_skills/storyboard-horizontal-generator/SKILL.md`：横屏 16:9 生成 skill，只在 `--aspect horizontal` / `-Aspect horizontal` 工作区中使用。
- `agent_skills/storyboard-horizontal-reviewer/SKILL.md`：横屏 16:9 审核 skill，输出 raw JSON 审核结果。
- `agent_skills/storyboard-horizontal-generator/TOPIC_PACKS.md`：横屏可选题材包；只有任务书、剧本或用户明确指向对应题材时启用。
- `agent_skills/storyboard-horizontal-generator/project_packs/`：横屏项目专属包；只有任务书、剧本标题、角色设定或用户明确指定对应项目时启用。
- `agent_skills/seedance-prompt-profile/SKILL.md`：Seedance 2.0 官方模板风格摘要，只作为生成前参考层，不复制模板正文。
- `agent_skills/seedance-2-5-live-vertical/SKILL.md`：独立 Seedance 2.5 真人竖屏模型硬合同。
- `agent_skills/seedance-2-5-live-vertical-generator/SKILL.md`：2.5 profile 专属分镜生成器。
- `agent_skills/seedance-2-5-live-vertical-reviewer/SKILL.md`：2.5 profile 专属真实审核器。
- `agent_skills/asset-extractor/SKILL.md`：分镜完成后的生图资产表抽取 skill。
- `agent_runs/`：每次 agent 运行的工作区。
- `outputs_agent_*`：收集后的最终分镜输出目录。

## 模式选择

`single`：整集一次生成、一次审核。适合短集、格式规整、场景很少的剧本。

`scene`：先按场景拆段，每段生成审核，最后组装整集。生产默认推荐 `scene`，尤其适合长集、场景切换明显、剧情密度高的剧本。

## 标准流程

### 1. 准备输入

如果剧本已经是一集一个 `.txt` 或 `.docx`，直接把目录作为 `-Source`。

如果一个文件里包含多集，先拆成一集一集。规则不稳定的剧本不要盲目硬编码；先让 agent 识别集数边界，再写一个专用、可复用的拆分脚本。

示例：

```powershell
.\split-youyuanzhai6.ps1
```

### 2. 创建 agent 工作区

推荐用 `scene`：

```powershell
.\prepare-agent.ps1 scene youyuanzhai6-scene `
  -Source .\split_scripts\youyuanzhai-6 `
  -OutDir .\outputs_agent_youyuanzhai6_scene `
  -Force
```

如果要用整集模式：

```powershell
.\prepare-agent.ps1 single test-single `
  -Source .\split_scripts\youyuanzhai-6 `
  -OutDir .\outputs_agent_test_single `
  -Force
```

如果要生成横屏 16:9 分镜，显式指定 `-Aspect horizontal`：

```powershell
.\prepare-agent.ps1 scene yulongyin-horizontal `
  -Source .\split_scripts\yulongyin-duanwu `
  -OutDir .\outputs_agent_yulongyin_horizontal `
  -Aspect horizontal `
  -Force
```

横屏工作区的 `TASK.md` 会指向 `storyboard-horizontal-generator` 和 `storyboard-horizontal-reviewer`。不要把横屏任务交给默认竖屏 skill，也不要把横屏题材包或项目包迁移到无关剧本。

如果要生成动漫 3D CG 短剧风格，显式指定 `-VisualStyle 3d-cg`：

```powershell
.\prepare-agent.ps1 scene my-cg-run `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_my_cg_run `
  -VisualStyle 3d-cg `
  -Force
```

`VisualStyle` 是媒介风格维度，不替代 `Aspect`。默认 `live-action` 继续输出真人实拍短剧口径；`3d-cg` 会让工作区任务读取 `agent_skills/3d-cg-visual-style/SKILL.md`，并让生成提示、收集尾部和资产提示词切换为动漫 3D CG 口径：二次元角色设计、风格化面部与眼睛、清晰轮廓线、高质量卡通渲染、PBR材质与手绘质感融合、表情绑定、口型同步，以及冷冽刀光、气流压迫、碎石悬浮、贴地冲击尘浪、金属裂纹冷光等动作服务型大片特效。无论哪种风格，分镜结构、对白对象、时间规则、组首/组尾连续和 reviewer 门禁不变。

如果目标是 Seedance 2.5 真人竖屏短剧，显式选择独立 profile：

```powershell
.\prepare-agent.ps1 scene my-seedance25-run `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_my_seedance25 `
  -Aspect vertical `
  -VisualStyle live-action `
  -VideoProfile seedance-2.5-live-vertical `
  -VideoResolution 720p `
  -Force
```

也可使用固定入口（默认 720p），减少重复参数且不改变通用入口的 2.0 默认值：

```powershell
.\prepare-agent-seedance25.ps1 scene my-seedance25-run `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_my_seedance25 `
  -Force
```

该 profile 只允许 `vertical` + `live-action`，目标模型为 `doubao-seedance-2-5-260628`，唯一任务类型为 `multimodal_generation`。工作区会写出 `video_profile.json`，并把任务类型、至少 1 项真实图片/视频/音频素材要求、禁用任务模式、9:16、480p/720p、24fps、原生音频、4-30 秒整数时间轴写入 manifest、episode metadata、context 和 TASK；默认 720p。图片、视频、音频只是多模态输入素材，不代表独立“参考生成”模式；纯文本、参考生成、首尾帧/关键帧、编辑、延长/续写、轨道补全均禁用。不要与横屏或 3D CG 混用。不显式选择时，旧 `seedance-2.0` 仍是默认值，现有 run 不迁移。

**仓库边界：** `final.txt` 仍是资产无关母版；`asset_bindings.json` 仍只是 `cut_id -> 逻辑静态资产`，单独存在不满足真实多模态输入。本仓库新增确定性素材交接层，负责编译逻辑需求、登记本地文件、校验 ManJuWeb 回写并生成受哈希保护的请求包；ManJuWeb 是 Ark 上传、轮询、`assetId` 和状态的唯一权威来源。本仓库不复制 Ark 密钥和状态机。详见 `agent_skills/seedance-2-5-live-vertical/SKILL.md` 与 `docs/seedance-material-handoff-v1.md`。

生成后会得到：

```text
agent_runs\<run-name>\
├── context.md
├── manifest.json
├── video_profile.json
├── NEXT_STEPS.md
├── COLLECT_RESULTS.ps1
└── episodes\
    ├── ep01\
    │   ├── TASK.md
    │   ├── agent_prompt.md
    │   ├── script.txt
    │   └── segments\seg01\script.txt
    └── ...
```

### 3. 分发 agent

打开 `agent_runs\<run-name>\NEXT_STEPS.md`，按里面的 `agent_prompt.md` 分发任务。

在 Codex app 里，推荐直接用 subagents 并发处理。质量单位永远是单集；调度单位可以是 1 集 / worker，也可以在短集、单段、剧情密度低时使用 2 集 / worker。`prepare-agent` 会在 `NEXT_STEPS.md` / `DISPATCH_PROMPT.md` 里按复杂度生成动态 worker batches：当前默认只有脚本不超过 2500 字符且 scene 拆分后只有 1 段的相邻两集才合并；其他集仍保持一集一个 worker。最多同时运行 5 个 worker，完成一个再补下一个。

默认安全模式例如先启动：

- worker 1：`ep01`
- worker 2：`ep02`
- worker 3：`ep03`
- worker 4：`ep04`
- worker 5：`ep05`

短集批处理模式可以先启动：

- worker 1：`ep01`, `ep02`
- worker 2：`ep03`, `ep04`
- worker 3：`ep05`, `ep06`
- worker 4：`ep07`, `ep08`
- worker 5：`ep09`, `ep10`

其中任意一个完成后，再启动新的 worker 处理后续 1-2 集，依次滚动。2 集 / worker 时，必须先完整完成第一集的生成、审核、修复、校验，再处理第二集；每集仍独立写 `final.txt`、`review.txt`、`status.json`，不能合并审核或合并输出。不要把 3 集以上交给同一个 worker，除非用户明确批准。

注意：不要让 Python 调用 CLI。可以人工在 Codex、Claude Code、Qwen Code 里跑，也可以在 Codex app 当前会话里派发 subagents。

### 4. 单集必须写出的文件

`scene` 模式下，每个 segment：

- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`

每集目录：

- `final.txt`
- `review.txt`
- `status.json`

`status.json` 建议：

```json
{
  "status": "done",
  "hard_issues_remaining": [],
  "warnings": [],
  "reviewer_source": "storyboard-reviewer",
  "reviewer_pass": true,
  "reviewer_issues_count": 0,
  "reviewer_warnings_count": 0
}
```

如果仍有硬问题但需要保留当前最佳稿，写 `status: "needs_review"`，并把残留问题写清楚。

`review.txt` 和 `segments/segXX/review.md` 必须是 `storyboard-reviewer` 返回的原始 JSON。`validate-episode` 会检查 reviewer 证据；clean-format 校验不能替代审稿，占位 review 会导致校验失败。

横屏 run 中，`reviewer_source` 必须是 `storyboard-horizontal-reviewer`，`review.txt` 和 `segments/segXX/review.md` 必须来自横屏 reviewer 的 raw JSON。横屏最终 `final.txt` 仍是自然分镜正文，不输出 JSON；只有审核文件是 JSON。

完整生产审核必须提供同一 episode 的原剧本、当前分镜和当前 run 指定的 skill。若只提供分镜稿而没有原剧本，横屏 reviewer 只能做 `technical_review_only`，不得声称 `script_fidelity` 已通过，也不能把技术审核包装成生产审核通过。

质量下限也会被校验：禁止“空间先被交代出来”“人物面部肌肉随局势绷紧”等模板化镜头描述；普通空间/环境交代镜头默认应为 2 秒，不能批量用 3 秒凑时长。单个时间段默认只承载一个主动作目标；同一主体、同一空间、同一目标且顺序和结果清楚的紧凑动作链可在 2-3 秒完成，不按动词数量机械拆分。多个主体/目标争抢画面、关键状态不清、明显跨位移、重物搬运、多人协同或精细操作时，才按真实需求拆段或加时。组首空间锁定必须与第一帧一致，不能写成前情回顾。车辆抵达、门打开、人员下车、群众反应、主角对峙这类外部事件进入，必须按必要阶段拆开，不能塞进同一镜头。喝止、闯入、身份揭露、证据亮出这类高冲击打断后，应先稳定打断/反应，再处理放下道具、跨位移、保护站位、团圆确认等归位动作。竖屏运镜不设数量指标，但每一镜必须写清动机、主体、路径和落点，并与人物动作、竖屏构图和连续性兼容。`视频禁止项` 不靠剧目专属词表判定，而是按 policy 中的少量全局模板词、上下文锚点停用词、本组上下文和本集全文上下文锚点校验。

### 5. 校验

单集校验：

```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\youyuanzhai6-scene\episodes\ep01
```

默认校验只检查并保留分镜 `final.txt`、`review.txt`、`status.json` 等生产必需文件，不导出 `storyboard_index.json` / `storyboard_index.xlsx`。**例外：`seedance-2.5-live-vertical` 完整校验会自动生成并保留索引**，作为后续素材交接的稳定主键。其他 profile 如需索引，显式加 `--export-index`，或单独运行 `export-storyboard-index`。

整轮校验可在 PowerShell 中跑：

```powershell
$failed=@()
Get-ChildItem .\agent_runs\youyuanzhai6-scene\episodes -Directory | Sort-Object Name | ForEach-Object {
  python .\storyboard_agent_workspace.py validate-episode --episode-dir $_.FullName
  if ($LASTEXITCODE -ne 0) { $failed += $_.Name }
}
if ($failed.Count -gt 0) { throw "Validation failed: $($failed -join ', ')" }
```

### 6. 收集结果

```powershell
.\collect-agent.ps1 .\agent_runs\youyuanzhai6-scene
```

收集后检查：

- `outputs_agent_*` 下应有每集一个最终分镜 `.txt`。
- `seedance-2.5-live-vertical` 会自动复制 `storyboard_index.json` / `storyboard_index.xlsx`；其他 profile 默认不复制，如需索引运行 `.\collect-agent.ps1 .\agent_runs\<run-name> -ExportIndex`。
- `agent_runs\<run-name>\SUMMARY.md` 应显示全部 `clean_format_passed, quality_floor_passed, storyboard_reviewer_passed`。

### 7. 可选：生成生图资产表

当需要把分镜交给其他 AI 生图/视频模型提前准备资产时，读取 `agent_skills/asset-extractor/SKILL.md` 和 `agent_skills/asset-reviewer/SKILL.md`，从单集 `final.txt` 和 `storyboard_index.json` 生成 `assets.md`、`assets.xlsx`、`asset_bindings.json`、`asset_review.json` 和 `asset_status.json`。Seedance 2.5 的索引已经由完整校验自动保留；其他 profile 先显式导出索引。

> **索引保留规则：** Seedance 2.5 的完整 `validate-episode` 与 `collect-agent` 自动保留/收集索引，不需要 `--export-index`。其他 profile 仍是 txt-only：不带 `--export-index` 的普通校验会主动删除已有索引；资产阶段前需显式导出，并在后续校验/收集时持续带上 `--export-index`。

多集项目不要让每集各自临场编人物设定。必须先创建 run 级别全局资产设定：

```text
agent_runs\<run-name>\asset_bible.md
```

`asset_bible.md` 用来固定基础资产和状态资产：

- 基础人物：角色名、年龄段、性别、身份、身高体态、面部稳定特征、发型、气质关键词。
- 人物状态：服装变化、脏污、湿身、受伤、身份阶段等会影响多镜头一致性的变化。
- 服装资产：上装、下装、鞋、配饰、颜色、面料、年代感、磨损程度。
- 场景基础与状态：布景结构、材质、陈设，以及白天、夜雨、断电、爆炸后、破损后等状态。
- 道具基础与状态：材质、形状、文字限制，以及完整、破损、盖章、沾血等状态。

分集资产 worker 必须读取 `asset_bible.md` 后再生成每集 `assets.md`。分集默认不重复输出 `asset_bible.md` 已有基础资产的完整提示词；如果发现本集新增基础资产或新增状态，只在 `assets.md`、`asset_status.json` 的 `bible_update_candidates` 或交付说明中标记，不要多个 worker 并发改写全局设定。

资产表固定包含六部分：

- 本集复用资产索引
- 本集新增资产状态
- 本集新增基础资产
- 本集关键道具与场景状态
- 本集不建议入库元素
- 本集分镜资产绑定索引

资产表继续输出 Markdown + Excel，不输出 HTML。episode 模式转换 `assets.xlsx` 时必须同步导出 `asset_bindings.json`，让 Web 工程按 `cut_id -> asset_id/state_id` 自动绑定参考图。新增基础资产和新增状态必须有稳定 `asset_id` 或 `state_id`。需要生成新图的条目，提示词列拆成 `静态生图提示词(中文)`、`负面提示词(中文)`、`静态生图提示词(英文)`、`负面提示词(英文)`，用于同时交付中文生产和英文生图模型。

要求：

- 基础人物资产只记录身份、脸、体态、发型、气质；服装细节由服装资产或人物状态引用，不要每集重写完整人物定妆。
- 场景基础资产和场景状态必须明确“空镜、无人、无人脸”，不得包含人物；场景状态用于记录白天、夜雨、断电、爆炸后、整洁后、破损后等变化。
- 道具基础资产和道具状态只提取需要稳定生成的关键物件；普通桌椅、门窗、背景灯具、一次性纸张、短暂表情、普通手势写入“不建议入库元素”。
- `cut_ids` 和第六表 `cut_id` 必须来自 `storyboard_index.json`，不得杜撰。
- 适用时间段必须来自分镜。
- 不得杜撰分镜中不存在的地点、角色、道具。
- `assets.md` 方便审稿和版本管理；`assets.xlsx` 方便筛选、复制单元格和生产使用；`asset_review.json` 和 `asset_status.json` 是收集门禁。

资产 reviewer 门禁：

- `asset_review.json` 必须来自 `asset-reviewer` 对照 `final.txt`、`assets.md`、`asset_bible.md` 和两份资产 skill 的真实审核。
- 如果 reviewer 返回 hard issues，必须局部修复后复审，不能只跑 Excel 转换。
- 转换 Excel 后必须运行 `node .\agent_skills\asset-extractor\scripts\validate-assets.mjs <episode-dir> --storyboard-index=<episode-dir>\storyboard_index.json` 做机械门禁校验。
- 只有 `asset_status.json` 中 `status=done`、`reviewer_source=asset-reviewer`、`reviewer_pass=true`、`reviewer_issues_count=0` 的 episode 可以进入正式资产收集。

### 8. 可选：编译 Seedance 2.5 素材交接与生成包

资产审核及 `validate-assets.mjs` 通过后，先编译逻辑素材需求和本地素材登记模板：

```powershell
python .\storyboard_agent_workspace.py export-seedance-material-requirements --episode-dir <episode-dir>
```

在 `seedance_local_materials.json` 中填写真实文件、MIME、SHA-256 和授权确认，把两份 JSON 与实际图片交给 ManJuWeb。ManJuWeb 后端完成 Ark 复用/上传后，将响应原样保存为同目录 `ark_sync_results.json`。Auto-Storyboard 不写 Ark ID 或 Ark 状态。

回写后执行门禁和编译：

```powershell
python .\storyboard_agent_workspace.py validate-seedance-materials --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py export-seedance-package --episode-dir <episode-dir>
```

只有输出 `generation_ready=true`、`submit_allowed=true` 才能提交 Seedance。生成包绑定 `final.txt`、索引、两份素材清单、Ark 回写和实际文件哈希，任一输入变化都会使旧包失效。当前 MVP 自动入库静态图片；视频、音频和公网 URL 会明确保持未就绪，不会被图片或旧 Ark ID 静默替代。

资产阶段调度建议：

- 默认 3 集 / worker。
- 单集短、复用度高、全局设定稳定时可用 4 集 / worker。
- 不要超过 4 集 / worker，避免资产表过长后漏道具或串镜号。
- 每个 worker 必须逐集闭环：生成 `assets.md`，用 `asset-reviewer` 真实审核，修复 hard issues 并复审，通过后写 `asset_status.json`，再用脚本转换 `assets.xlsx`，运行 `validate-assets.mjs`，然后进入下一集。
- `assets.xlsx` 由本地脚本从 `assets.md` 转换，不额外消耗模型 token。

## 生产审核口径

默认竖屏以 `storyboard-reviewer` 为审核器；`seedance-2.5-live-vertical` 以独立 `seedance-2-5-live-vertical-reviewer` 为审核器；横屏以 `storyboard-horizontal-reviewer` 为审核器。三者都必须对照原剧本和当前分镜做真实审核。

- 忠于原剧本：不删关键台词，不乱改人物关系，不额外添加剧情。
- 对话指向：真人对话必须写清“谁对谁说”。
- 台词速度：普通对白目标约 4.5 字/秒，情绪对白目标约 5.2 字/秒；有效字数 / 秒 > 6.5 是 hard issue，5.8-6.5 是 warning。
- 镜头过长也要审：不能靠新增停顿、长凝视、慢动作凑时长。
- 无台词镜头通常 2-3 秒，不能用 4-5 秒凑组时长。
- 默认 `seedance-2.0` 竖屏组内时间段允许 0.5 秒粒度，组总时长硬范围 6-15 秒；10-15 秒是常用承载区间，6-9 秒只用于合理短组。
- `seedance-2.5-live-vertical` 组内只用整数秒边界，组总时长硬范围 4-30 秒；同场、同目标、同批人物且合并后不超过 30 秒的连续流程优先使用分阶段的 16-30 秒长组，8-15 秒用于无法跨真实空间/目标/人物断点、独立戏剧节拍、信息落点、反应落点或原剧本明确停顿继续合并的独立块，4-7 秒只用于真实短节拍。
- `seedance-2.5-live-vertical` reviewer 还必须检查 `multimodal_task_scope`：正文只能服务 `multimodal_generation`，任何纯文本、参考生成、首尾帧/关键帧、编辑、延长或轨道补全指令都是 hard issue。
- 横屏使用 `**本镜估算时长**`，组总时长必须是整数 6-15 秒，默认优先 10-15 秒；只有短承接、单句反应、道具插入、短动作余波、片尾意象或不可硬凑的极短戏剧节拍才允许 6-9 秒短组。
- 景别重复不要机械判错，正反打同景别可接受。
- 最终稿禁止 JSON、调试标记或其他非分镜正文内容，必须是自然分镜文本。

## 当前验证过的落地案例

- `legacy/old_outputs/outputs_agent_youyuanzhai_scene`：旧版《有缘斋剧本》scene 模式，15 集已通过。
- `outputs_agent_youyuanzhai6_scene`：新版《有缘斋剧本-6》scene 模式，14 集已通过。
- `legacy/old_outputs/outputs_agent_6688_clean`：早期 agent-clean 输出，可作为格式参考，但生产推荐用当前 `scene` 工作流。

## 常见问题

### 为什么不要 Python 调 CLI？

之前的 GUI/API 链路和“Python 启动 CLI”都会引入额外不稳定因素：进程管理、编码、日志、token 消耗、失败恢复都更复杂。现在的做法是文件工作区 + agent 原生会话，失败点更少，也更容易人工接管。

### 为什么不是所有剧本都自动拆集？

剧本格式经常不统一。有的有“第X集完”，有的只有“本集完”，有的后半段没有标题。生产上更稳的方式是先识别边界，再写专用拆分脚本，避免通用硬编码误拆。

### 什么时候用 `single`？

当单集很短、只有一个场景、模型一次性处理稳定时用 `single`。否则默认 `scene`。

### agent 生成慢怎么办？

优先增加“集级并发”，不要把多集合并到一个请求。一般 3-5 个并发 worker 比较稳；单集内按场景拆段已经能减少偏移。
