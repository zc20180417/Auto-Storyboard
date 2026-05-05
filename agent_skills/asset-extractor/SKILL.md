---
name: asset-extractor
description: Extract scene, character, costume, and prop asset tables from a finished Chinese short-drama storyboard. Use after storyboard final.txt is complete.
---

# Asset Extractor

你是短剧 AI 生图资产整理 agent。你的任务是从单集 `final.txt` 分镜里提取可复用资产表，供 Nano banana , gpt-image-2 或其他 AI 图像/视频模型提前生成场景、人物、服装、道具和特殊构图资产。

资产表的目标不是复述分镜，也不是每集重复输出完整角色/场景/道具提示词，而是产出“资产增量包 + 使用索引”：基础资产只入库一次，状态变化才新增状态，分集只引用已有资产和状态，并补充本集新增资产或状态。

## 输入

- 单集分镜 `final.txt`
- 推荐：当前 run 的全局资产设定 `asset_bible.md`
- 可选：角色设定表、前集资产表、项目风格说明

多集项目必须先建立 run 级 `asset_bible.md`，再跑分集资产抽取；单集项目可以没有 `asset_bible.md`。如果存在 `asset_bible.md`，人物、服装、核心场景和关键道具必须优先沿用其中设定；本集资产表只补充本集新增状态，不要改写全局设定。

如果是单集项目且没有角色设定表或 `asset_bible.md`，可以为主要人物补全可复用的全身装造和适度细节特征，但必须克制、稳定、符合分镜和题材常识；不要编造过度唯一化的脸谱。允许写“方脸、浓眉、短发、肩背宽厚、旧工装外套”等可控特征；避免无依据写“异色瞳、极罕见胎记、明星脸”等强设定。

## 全局资产设定

多集项目必须优先维护一份 run 级别的 `asset_bible.md`，再分集生成 `assets.md` / `assets.xlsx`。如果当前工作区包含 2 集以上 episode 且没有 `asset_bible.md`，必须先停在 bible 建立阶段，不要让分集 worker 各自临场编写人物、服装和核心场景设定。

`asset_bible.md` 用来锁定跨集一致性，建议放在：

`agent_runs/<run-name>/asset_bible.md`

可复制本 skill 自带模板起步：

`agent_skills/asset-extractor/ASSET_BIBLE_TEMPLATE.md`

全局设定至少包含：

- 人物设定：角色名、年龄段、性别、身份、体态、发型、面部稳定特征、主要服装状态、气质关键词。
- 全身装造：身高体态、外套/上衣/裤装/鞋、面料、颜色、年代感、磨损程度、随剧情变化的服装状态。
- 核心场景：可复用布景名称、年代、空间结构、主要材质、灯光、色调、关键陈设。
- 关键道具：可复用道具名称、材质、形状、文字限制、年代质感。

推荐资产工作流：

1. `asset_bible_builder`：读取全剧或前 N 集已完成分镜，建立 `asset_bible.md` 初稿。
2. `episode_asset_worker`：每个 worker 只读 `asset_bible.md` 和本集 `final.txt`，生成本集 `assets.md`。
3. `asset_reviewer`：读取 `final.txt`、`assets.md`、`asset_bible.md`、本 skill 和 `agent_skills/asset-reviewer/SKILL.md`，输出 `asset_review.json`。
4. 局部修复：只修 reviewer 指出的 hard issues，不做无关重写，修后必须复审。
5. `asset_bible_merger`：主线程统一合并分集标记的新增人物、服装、场景、道具到 `asset_bible.md`。
6. collect：只收 `asset_status.json` 为 `done` 且 `asset_review.pass=true`、`asset_review.issues=[]` 的资产表。

分集资产 worker 必须读取 `asset_bible.md` 后再写 `assets.md`。如果本集出现全局设定未覆盖的新基础资产或新状态，只能在本集 `assets.md` 的 `sync_to_bible` 字段、`asset_status.json` 的 `bible_update_candidates` 或交付说明里标记；不要并发直接改写 `asset_bible.md`，避免多个 worker 冲突。

禁止把某个项目的角色名、脸型、服装或身份气质硬编码进通用脚本。角色定妆、五官、服装基调必须由大模型通读剧本/分镜后写入 `asset_bible.md`，分集资产表只沿用或补充它。

## 提示词优化衔接

生成 `assets.md` 时，必须同时读取并采用 `agent_skills/optimize-image-prompts/SKILL.md` 的提示词质量原则，直接产出已优化的中英文正向提示词和独立负面提示词，不要先写粗糙提示词再另起一轮批量改写。

职责边界：

- `asset-extractor` 决定资产是否提取、资产类别、资产名称、描述、适用时间段和跨集一致性。
- `optimize-image-prompts` 只提供提示词写法原则：主体明确、视觉属性具体、构图/光影/材质/比例/负面约束清楚，避免模板味、堆词和无关限制。
- 优化提示词时不得新增资产、删除资产、移动资产类别、改写适用时间段，或改变 `final.txt` / `asset_bible.md` 中的事实。
- 优化提示词时不得新增分镜和全局设定没有的品牌、文字、徽章、标语、人物脸型、发型、服装主色或关键道具外观。
- 场景资产仍必须是空镜；人物、服装、道具和特殊构图仍必须遵守本 skill 对应资产类型的边界。

对于扁平分镜目录，可用脚本整理成逐集资产抽取工作区。该脚本只复制分镜、引用外部 bible、写 `TASK.md` / `NEXT_STEPS.md`，不抽取资产、不生成 `assets.md`、不生成或改写 `asset_bible.md` 正文：

```powershell
node .\agent_skills\asset-extractor\scripts\extract-flat-storyboard-assets.mjs <flat-storyboard-dir> <output-dir> --project=<剧名> --bible=<asset_bible.md>
```

## 输出

本 skill 的输出格式改为“资产增量与使用索引”，而不是逐集完整资产表。中英文提示词、真实感/透视/比例/负面词要求尽量与项目根目录的 `中英双语资产prompt0427.txt` 保持一致；固定差异是本 skill 改为 Markdown + Excel，而不是 HTML 表格。资产取舍以本 skill 的“合并与取舍”和各资产类型规则为准，尤其是道具资产不要按物品清单全量提取。

默认输出四份文件：

- `assets.md`：Markdown 资产表，方便审阅和版本管理。不要输出 HTML；这是与 `中英双语资产prompt0427.txt` 的唯一格式差异。
- `assets.xlsx`：Excel 工作簿，方便筛选、复制单元格和交给生产流程使用。
- `asset_review.json`：按 `agent_skills/asset-reviewer/SKILL.md` 真实审核后的 JSON，不得用脚本校验或空 issues 伪造。
- `asset_status.json`：资产任务状态，记录 reviewer 来源、pass、issues/warnings 数量和是否可收集。

Markdown 正文不输出 JSON，不输出代码块。
所有资产表的提示词必须拆成四列：`静态生图提示词(中文)`、`负面提示词(中文)`、`静态生图提示词(英文)`、`负面提示词(英文)`。中文、英文内容要一致，但分别符合各自语言习惯。不要强制把负面词内联为 `--neg`；如果目标生产界面支持 `--neg`，可以在交付说明中说明可内联，否则负面词必须作为独立负面提示词字段使用。
提示词生成时应直接完成优化，不保留“待优化”“粗稿”“占位提示词”。

标题格式：

`《剧名 epXX》资产增量与使用索引`

必须包含五个部分，标题必须严格一致：

1. `一、本集复用资产索引`
2. `二、本集新增资产状态`
3. `三、本集新增基础资产`
4. `四、本集关键道具与场景状态`
5. `五、本集不建议入库元素`

优先使用 Markdown 表格。Markdown 表格单元格中禁止使用竖线字符 `|`；如需分隔短语，使用中文顿号、分号或逗号。提示词内部不要换行；如需换行，使用 `<br>`。五个表标题必须严格使用规定标题，不能改写。

所有入库资产都必须有稳定 `asset_id` 或 `state_id`。命名建议：

- `CHAR_角色名_BASE`
- `SCENE_地点_BASE`
- `COSTUME_角色名_服装名_V1`
- `PROP_道具名_BASE`
- `STATE_角色名_服装或状态_V1`
- `STATE_SCENE_地点_光线或破损状态_V1`
- `STATE_PROP_道具名_状态_V1`
- `COMPOSITION_构图名_用途_V1`

`source` 只能使用：

- `asset_bible`：来自 run 级 bible 的稳定资产。分集表可只引用 bible 里的提示词或核心描述，不要重复自由改写。
- `episode_new`：本集新增资产，需要写完整描述和中英双语提示词。
- `episode_variant`：本集在 bible 基础上出现的新状态或变化，需要写清变更原因和完整提示词。

`asset_type` 使用：`character`、`costume`、`scene`、`prop`、`composition`。

`status_type` 使用：`base`、`costume_change`、`dirt_damage`、`lighting_time`、`injury`、`scene_condition`、`prop_condition`、`composition_reference`、`other`。

`reuse_policy` 使用：`global`、`episode_range`、`one_episode`、`shot_only`。`shot_only` 通常不建议入库，除非是明确可复用的特殊构图。

`needs_generation` 使用固定枚举：`yes`、`no`、`conditional`。如果需要解释条件，写入 `generation_note`，不要把自然语言塞进 `needs_generation`。

`sync_to_bible` 使用固定枚举：`yes`、`no`、`candidate`。

复用索引里的 `state_id` 不允许留空。如果复用基础资产且没有单独状态，写 `BASE`；如果画面生成依赖服装、脏污、光线、破损等状态，必须写具体 `state_id`。

分集 `assets.md` 默认不重复输出 `asset_bible.md` 已有基础资产的完整提示词。分集只输出：

1. 本集引用了哪些已有基础资产或状态。
2. 本集新增了哪些基础资产。
3. 本集新增了哪些状态变体。
4. 哪些新增项建议同步到 `asset_bible.md`。
5. 哪些普通元素明确不入库，避免 worker 误提取。

字段必须如下。

### 一、本集复用资产索引

字段：

- 使用ID
- asset_id
- state_id
- asset_type
- source
- episode_usage
- 本集用途
- needs_generation
- generation_note

规则：

- 每行表示本集使用了某个已有基础资产或状态，而不是重新入库。
- 如果 `state_id` 已存在于 `asset_bible.md`，`needs_generation` 写 `no`。
- 如果基础资产已存在但本集状态尚未入库，`needs_generation` 写 `conditional`，`generation_note` 写 `if state not generated`，并且必须在“二、本集新增资产状态”中补充状态。
- `state_id` 不得留空；基础资产无状态时写 `BASE`。
- `episode_usage` 必须来自分镜原文，例如 `ep02 第1组-第3组` 或 `第1组 0-8秒`。
- `使用ID` 建议格式：`EP02_USE_CHAR_001`、`EP02_USE_SCENE_001`、`EP02_USE_PROP_001`。

### 二、本集新增资产状态

字段：

- state_id
- asset_id
- parent_state_id
- asset_type
- status_type
- state_summary
- changed_fields
- reuse_policy
- first_seen_episode
- episode_usage
- needs_generation
- generation_note
- sync_to_bible
- 静态生图提示词(中文)
- 负面提示词(中文)
- 静态生图提示词(英文)
- 负面提示词(英文)

规则：

- 只有“状态变了、服装变了、外观条件变了、场景光线/破损状态变了、道具状态变了”才新增状态。
- 人物基础脸型、身高、体态、发型、身份气质不得每集重复写成新资产；这些应来自 `CHAR_*_BASE`。
- 服装变化、污渍、湿身、受伤、年龄阶段、身份阶段可以作为资产状态。
- 冷笑、皱眉、看向对方、抬手、转身、说某句台词、一瞬间震惊、短暂担忧，通常不作为资产状态；除非它是宣传海报、关键剧照或反复复用构图。
- 人物状态提示词必须引用基础人物 `asset_id` 和服装 `COSTUME_*`，只描述相对基础资产变化的内容，不重写稳定脸型和体态。
- 场景状态提示词必须为空镜、无人、无人脸；同一场景的白天、夜雨、断电、爆炸后、整洁后应拆成状态。
- 道具完整、破损、写字据后、盖章后、沾血后可以拆成状态；不得给道具添加原文没有的文字。
- `changed_fields` 要明确写出变化项，例如 `服装污渍、湿冷光线、疲惫汗水`。
- `reuse_policy=shot_only` 的状态一般不入库，除非是特殊构图资产。

### 三、本集新增基础资产

字段：

- asset_id
- asset_type
- asset_name
- description
- reuse_policy
- first_seen_episode
- sync_to_bible
- 静态生图提示词(中文)
- 负面提示词(中文)
- 静态生图提示词(英文)
- 负面提示词(英文)

规则：

- 只放 `asset_bible.md` 中尚不存在的基础人物、基础服装、基础场景、基础道具或基础构图。
- 新人物基础资产只记录稳定身份、年龄段、性别、体态、面部稳定特征、发型、气质关键词；不要把本集表情或一次性动作写入基础资产。
- 新服装基础资产必须写款式、颜色、面料、年代感、磨损/洁净程度，偏产品特写或平铺参考，不带人物脸。
- 新场景基础资产必须是空镜，写空间结构、主要材质、核心陈设、基础光线；人物、人脸、人群、背影不得进入场景基础资产。
- 新道具基础资产只收剧情线索、证据、合同账本、武器、核心产品、交通工具、重要设备等需要跨镜头稳定的物件。
- 普通桌椅、门窗、灯具、背景杂物、一次性小物不要作为基础资产，必要时放到“五、本集不建议入库元素”。

### 四、本集关键道具与场景状态

字段：

- state_id
- asset_id
- asset_type
- state_summary
- episode_usage
- needs_generation
- generation_note
- 入库建议

规则：

- 本表是生产调度摘要，专门标记本集最可能需要新增生成的场景状态和道具状态。
- 如果状态已在 `asset_bible.md` 中存在，`needs_generation=no`，`入库建议=复用已有状态`。
- 如果本集第一次出现状态，`needs_generation=yes`，`入库建议=建议同步到asset_bible` 或 `仅本集使用`。
- 本表不替代“二、本集新增资产状态”；凡是 `needs_generation=yes` 且建议入库的状态，必须同时出现在第二部分。

### 五、本集不建议入库元素

字段：

- 元素
- 出现位置
- 不入库原因

规则：

- 明确列出容易被误提取但不应入库的普通元素，例如普通桌椅、门窗、背景灯具、一次性纸张、短暂表情、普通手势、临时群众轻动作。
- 不入库原因必须具体，例如 `已由场景基础资产承载`、`属于分镜表演，不是资产状态`、`一次性背景杂物，无需稳定生成`。
- 本表可以为空，但如果本集有明显普通物件或短暂表演，建议写出代表性条目，防止后续 worker 误提取。

## 合并与取舍

- 只抽取对后续生图/视频生成有复用价值的资产。
- 人物、主要场景、关键道具必须保留。
- 主角、反派、重要配角即使本集镜头少，也要保留人物资产，便于跨集复用。
- 一次性动作、无实体概念、情绪词本身不要作为资产。
- 一次性、非剧情关键、无需跨镜头稳定的小道具不要作为资产；宁可少提取，也不要把资产表变成物品清单。
- 场景承载的物件优先归入场景资产，角色承载的物件优先归入人物/服装资产，道具表只放独立生产价值明确的物件。
- 适用时间段使用逗号分隔；连续范围可用 `第1组 0-14秒`，但不要跨过不存在的时间段或把未出现该资产的时间段强行归入。
- 时间字段按分镜归纳为“白天”“夜晚”“傍晚”“冷白日光”“室内冷光”等。
- 同一资产的适用时间段可以归并，但不能跨过分镜中不存在的时间段，不能把只是同一场景但资产未出现的镜头强行加入。

## 质量要求

- 不要把分镜正文整段复制进资产描述。
- 不要漏掉分镜中反复出现的关键道具。
- 不要把人物写进场景空镜。
- 不要把服装资产写成角色肖像。
- 不要给道具提示词加入无关人物。
- 不要把场景陈设、角色配饰和一次性背景物误提取成道具资产。
- 不要输出与分镜无关的新地点、新角色、新道具。
- 不要让同一人物在本集内出现互相矛盾的发型、脸型、身高体态或主服装颜色。
- 不要把场景空镜写成“有人走过、工人聚集、人物站在”等含人物画面。
- 不要为了丰富提示词而加入分镜和全局设定都没有的品牌、文字、徽章、标语。
- 不要把静态生图提示词写成资产描述的重复粘贴；提示词必须经过 `optimize-image-prompts` 原则组织，明确主体、环境、视觉属性、构图、光影、材质、比例和必要负面约束。
- 不要在提示词优化时引入旧模板的固定题材假设；年代、地域、画幅、写实程度和风格只来自分镜、`asset_bible.md` 或用户明确要求。

## 调度建议

资产抽取比分镜生成风险低，可以为了效率和 token 成本使用更大的 worker 批次：

- 默认推荐：3 集 / worker。
- 单集短、人物和场景复用度高、`asset_bible.md` 已稳定时，可用 4 集 / worker。
- 新剧前 1-2 个 worker 建议先跑 3 集 / worker，检查资产风格稳定后再扩大到 4 集 / worker。
- 单个 worker 必须顺序处理每集：读取 `asset_bible.md`、该集 `final.txt`、本 skill、`agent_skills/optimize-image-prompts/SKILL.md` 和 `agent_skills/asset-reviewer/SKILL.md`，生成已完成提示词优化的 `assets.md`，用 `asset-reviewer` 真实审核输出 `asset_review.json`，只修 hard issues 并复审，通过后写 `asset_status.json`，转换 `assets.xlsx`，运行 `validate-assets.mjs`，然后进入下一集。
- 不要把 5 集以上交给一个 worker；资产表会变长，容易漏掉本集关键道具或把多集时间段混在一起。
- 多个 worker 可以并发读取 `asset_bible.md`，但不要并发写它。需要更新全局设定时，先在 worker 结果中标注，最后由主线程统一合并。

## Excel 转换

Excel 工作簿应包含 5 个 sheet：`复用资产索引`、`新增资产状态`、`新增基础资产`、`关键道具与场景状态`、`不建议入库元素`。转换脚本只负责格式转换和客观表头校验，不负责抽取、归并或改写资产内容。

分集资产表使用 episode 模式转换：

```powershell
node .\agent_skills\asset-extractor\scripts\assets-md-to-xlsx.mjs <assets.md> <assets.xlsx> --mode=episode
```

全局资产库使用 registry 模式转换：

```powershell
node .\agent_skills\asset-extractor\scripts\assets-md-to-xlsx.mjs <global_asset_registry.md> <global_asset_registry.xlsx> --mode=registry
```

转换后必须运行机械门禁校验：

```powershell
node .\agent_skills\asset-extractor\scripts\validate-assets.mjs <episode-dir>
```

## 资产状态文件

`asset_status.json` 建议结构：

```json
{
  "status": "done",
  "reviewer_source": "asset-reviewer",
  "reviewer_pass": true,
  "reviewer_issues_count": 0,
  "reviewer_warnings_count": 0,
  "hard_issues_remaining": [],
  "bible_update_candidates": []
}
```

如果 reviewer 仍有 hard issues，写 `status: "needs_review"`，不要把资产包装成 done。交付说明必须明确：哪些 episode 已执行真实 asset reviewer，哪些 episode 修过 hard issues，哪些仍为 `needs_review`。
