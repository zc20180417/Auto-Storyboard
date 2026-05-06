# Agent 分镜生产工作流

这套流程已经作为项目的生产主流程：Python 不负责调用模型，也不负责启动 Codex/Qwen/Claude CLI；Python 只做文件工作区准备、客观格式校验和结果收集。真正的分镜生成、审核、局部修复由 Codex、Claude Code、Qwen Code 这类 agent 在自己的会话里完成。

## 为什么用这套流程

- 生成和审核在同一个 agent 会话里完成，避免“换会话越修越歪”。
- 每集是独立任务，可以并发；每集内部可按场景拆段，降低长剧本文本漂移。
- Python 只检查客观边界：文件是否存在、自然格式是否干净、是否能收集结果。
- 最终稿是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
- 失败也保留 `draft.txt`、`review.md`、`final.txt` 和 `status.json`，方便人工或 agent 继续接力。

## 目录约定

- `inputs/`：原始剧本文档或文本。
- `split_scripts/`：拆好的一集一集剧本文本。
- `agent_skills/storyboard-generator/SKILL.md`：生成 skill。
- `agent_skills/storyboard-reviewer/SKILL.md`：审核 skill。
- `agent_skills/seedance-prompt-profile/SKILL.md`：Seedance 2.0 官方模板风格摘要，只作为生成前参考层，不复制模板正文。
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

生成后会得到：

```text
agent_runs\<run-name>\
├── context.md
├── manifest.json
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

在 Codex app 里，推荐直接用 subagents 并发处理。质量单位永远是单集；调度单位可以是 1 集 / worker，也可以在短集、单段、剧情密度低时使用 2 集 / worker。最多同时运行 5 个 worker，完成一个再补下一个。

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

质量下限也会被校验：禁止“空间先被交代出来”“人物面部肌肉随局势绷紧”等模板化镜头描述；普通空间/环境交代镜头默认应为 2 秒，不能批量用 3 秒凑时长。

### 5. 校验

单集校验：

```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\youyuanzhai6-scene\episodes\ep01
```

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
- `agent_runs\<run-name>\SUMMARY.md` 应显示全部 `clean_format_passed, quality_floor_passed, storyboard_reviewer_passed`。

### 7. 可选：生成生图资产表

当需要把分镜交给其他 AI 生图/视频模型提前准备资产时，读取 `agent_skills/asset-extractor/SKILL.md` 和 `agent_skills/asset-reviewer/SKILL.md`，从单集 `final.txt` 生成 `assets.md`、`assets.xlsx`、`asset_review.json` 和 `asset_status.json`。

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

资产表固定包含五部分：

- 本集复用资产索引
- 本集新增资产状态
- 本集新增基础资产
- 本集关键道具与场景状态
- 本集不建议入库元素

资产表继续输出 Markdown + Excel，不输出 HTML。新增基础资产和新增状态必须有稳定 `asset_id` 或 `state_id`。需要生成新图的条目，提示词列拆成 `静态生图提示词(中文)`、`负面提示词(中文)`、`静态生图提示词(英文)`、`负面提示词(英文)`，用于同时交付中文生产和英文生图模型。

要求：

- 基础人物资产只记录身份、脸、体态、发型、气质；服装细节由服装资产或人物状态引用，不要每集重写完整人物定妆。
- 场景基础资产和场景状态必须明确“空镜、无人、无人脸”，不得包含人物；场景状态用于记录白天、夜雨、断电、爆炸后、整洁后、破损后等变化。
- 道具基础资产和道具状态只提取需要稳定生成的关键物件；普通桌椅、门窗、背景灯具、一次性纸张、短暂表情、普通手势写入“不建议入库元素”。
- 适用时间段必须来自分镜。
- 不得杜撰分镜中不存在的地点、角色、道具。
- `assets.md` 方便审稿和版本管理；`assets.xlsx` 方便筛选、复制单元格和生产使用；`asset_review.json` 和 `asset_status.json` 是收集门禁。

资产 reviewer 门禁：

- `asset_review.json` 必须来自 `asset-reviewer` 对照 `final.txt`、`assets.md`、`asset_bible.md` 和两份资产 skill 的真实审核。
- 如果 reviewer 返回 hard issues，必须局部修复后复审，不能只跑 Excel 转换。
- 转换 Excel 后必须运行 `node .\agent_skills\asset-extractor\scripts\validate-assets.mjs <episode-dir>` 做机械门禁校验。
- 只有 `asset_status.json` 中 `status=done`、`reviewer_source=asset-reviewer`、`reviewer_pass=true`、`reviewer_issues_count=0` 的 episode 可以进入正式资产收集。

资产阶段调度建议：

- 默认 3 集 / worker。
- 单集短、复用度高、全局设定稳定时可用 4 集 / worker。
- 不要超过 4 集 / worker，避免资产表过长后漏道具或串镜号。
- 每个 worker 必须逐集闭环：生成 `assets.md`，用 `asset-reviewer` 真实审核，修复 hard issues 并复审，通过后写 `asset_status.json`，再用脚本转换 `assets.xlsx`，运行 `validate-assets.mjs`，然后进入下一集。
- `assets.xlsx` 由本地脚本从 `assets.md` 转换，不额外消耗模型 token。

## 生产审核口径

- 忠于原剧本：不删关键台词，不乱改人物关系，不额外添加剧情。
- 对话指向：真人对话必须写清“谁对谁说”。
- 台词速度：有效字数 / 秒 > 7 才是硬问题；6-7 是 warning，不阻断。
- 镜头过长也要审：不能靠新增停顿、长凝视、慢动作凑时长。
- 无台词镜头通常 2-3 秒，不能用 4-5 秒凑组时长。
- 组总时长 10-15 秒，标题总时长要等于镜头时长相加。
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
