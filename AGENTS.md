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
3. `agent_skills/storyboard-generator/SKILL.md`
4. `agent_skills/storyboard-reviewer/SKILL.md`
5. 如需从分镜生成生图资产表，再读 `agent_skills/asset-extractor/SKILL.md`

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
- 简单批处理模式：2 集 / worker。只适合短集、单段或剧情密度低的剧本。
- 未经用户明确批准，不要超过 2 集 / worker。
- 最多同时运行 5 个 worker；如果使用 2 集 / worker，等价于最多同时推进约 10 集。
- 同一个 worker 处理 2 集时，必须先完整完成第一集的生成、审核、修复、校验，再处理第二集。
- 不要把 `ep01-ep08`、`ep09-ep16` 这类大范围交给一个 worker。
- 处理某个 episode 时，只能写入该 episode 目录，不要改其他集或其他输出目录。
- 两集同在一个 worker 时，也不能合并剧情、合并审核、合并输出或互相引用上下文。

如果当前环境要求用户授权才能创建 worker/subagent，必须先问用户确认。不能因为不能直接开 worker，就降级为脚本批量生成正文。

## Worker 必须做的事

worker 处理的每个 episode 都必须：

1. 读取自己的 `TASK.md`、`agent_prompt.md`、`script.txt`、两份标准 skill。
2. 按 `TASK.md` 的 `Mode` 执行，不要自行改模式。
3. 使用 `storyboard-generator` 生成分镜草稿。
4. 使用 `storyboard-reviewer` 做真实审核，审核必须对照原剧本和当前分镜逐项检查。
5. 只修 reviewer 指出的 hard issues，不做无关重写。
6. 修复后必须再次使用 `storyboard-reviewer` 复审，不能只跑格式校验。
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

### Reviewer 硬门槛

`review.txt` 和 `segments/segXX/review.md` 必须是真实审核结果，不能写占位文本、JSON、或伪造通过状态。`validate-episode` 只是客观格式校验和 reviewer 证据校验，不能替代真实审核。

真实审核必须满足以下证据要求：

- reviewer 必须读取并对照同一 episode 的 `script.txt`、当前 `final.txt`，以及两份标准 skill。
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

## 校验与收集

收集前必须先确认每集已完成真实 reviewer：

- 查看每集 `review.txt`，确认它是按 `storyboard-reviewer` 对照原剧本和 `final.txt` 生成的审核 JSON。
- 查看 `status.json`，确认 `reviewer_source` 为 `storyboard-reviewer`，且 `reviewer_pass`、`reviewer_issues_count`、`reviewer_warnings_count` 与 `review.txt` 一致。
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

## 资产表生成

分镜完成后，如用户需要给其他 AI 生图/视频模型提前准备资产，使用 `agent_skills/asset-extractor/SKILL.md` 从单集 `final.txt` 生成资产表。

资产表生成规则：

- 输入必须是已经完成的单集分镜 `final.txt`。
- 输出写入该集目录下的 `assets.md` 和 `assets.xlsx`，不要改写 `final.txt`。
- 资产表包含：场景资产、人物资产、服装资产、道具资产、特殊视角/构图资产。
- 场景资产必须为空镜；人物、服装、道具、特殊构图必须按可复用资产去重合并。
- 资产表继续使用 Markdown + Excel 输出，不使用 HTML；提示词列拆成 `静态生图提示词(中文)` 和 `静态生图提示词(英文)`。
- 多集项目必须先维护 run 级别 `asset_bible.md`，再分集生成资产表。推荐路径：`agent_runs/<run-name>/asset_bible.md`。
- `asset_bible.md` 用于固定跨集人物全身装造、面部稳定特征、核心场景、关键道具和服装状态。分集 worker 必须读取它，不能在不同集里随意改变同一人物的脸型、发型、体态、主服装颜色。
- 人物资产必须偏“全身装造/角色定妆照”，提示词要包含年龄段、性别、身份气质、身高体态、面部稳定特征、发型、上装、下装、鞋/配饰、关键表情动作。
- 场景资产提示词要足够丰富：年代感、空间结构、前中后景、材质、陈设、光线、色调、空镜、无人、无人脸、可作为视频背景资产，并包含真实世界比例参照和至少两项真实瑕疵细节。
- `适用镜号` 必须来自分镜原文，不得杜撰。
- 资产抽取不得替代分镜审核，也不得改变分镜生产结果。

资产阶段调度规则：

- 资产抽取不同于分镜生成，可以在保证 `asset_bible.md` 已稳定的前提下提高 batch。
- 默认推荐：3 集 / worker。
- 单集短、场景和人物复用度高、前 1-2 个资产 worker 结果稳定后，可用 4 集 / worker。
- 未经用户明确批准，不要超过 4 集 / worker。
- 同一个 worker 处理 3-4 集时，必须逐集闭环：先完成某集 `assets.md`、检查五类表格和中英双语提示词、转换 `assets.xlsx`，再处理下一集。
- worker 可以读取全局 `asset_bible.md`，但不要并发写它；新增人物/服装/场景/道具只在交付说明中标记，最后由主线程统一合并。

## 当前生产参考

- 最新已验证 `scene` 工作区：`agent_runs/youyuanzhai6-scene`
- 最新已验证 `single` 工作区：`agent_runs/youyuanzhai-single`
- 当前主生成规则：`agent_skills/storyboard-generator/SKILL.md`
- 不再默认使用 `6688竖屏古装分镜prompt.txt` 覆盖生成 skill；只有用户明确要求临时替换生成规则时，才可使用 prompt override。

旧 GUI/API 文件已归档到 `legacy/`。除非用户明确要求恢复旧流程，否则不要使用归档文件。
