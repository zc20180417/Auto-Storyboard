# Claude Code 入口

先读 `AGENTS.md`。生产主流程写在 `README_AGENT_WORKFLOW.md`。

重要规则：不要让 Python 调用 Claude Code、Codex CLI、Qwen CLI、Kimi Code 或其他模型 CLI。请直接在 `prepare-agent.ps1` 创建的文件工作区里完成生成、审核和修复。

## 当前合同同步

- 以当前 run 的 `TASK.md`、`context.md`、`DISPATCH_PROMPT.md`、`NEXT_STEPS.md` 为准；它们覆盖通用说明。
- Worker 必须读取 `TASK.md` 指定的 generation skill 和 review skill。竖屏默认是 `agent_skills/storyboard-generator/SKILL.md` + `agent_skills/storyboard-reviewer/SKILL.md`；横屏 `Aspect: horizontal` 必须改读 `agent_skills/storyboard-horizontal-generator/SKILL.md` + `agent_skills/storyboard-horizontal-reviewer/SKILL.md`。
- 竖屏主生成合同是每组 `10-15 秒`，不要生成 `6-9 秒`竖屏短组；如果旧任务书仍出现“竖屏 6-9 秒短组可用”之类提示，先重新准备工作区或停止确认，不要继续生产。
- `agent_skills/storyboard-generator/REFERENCE.md` 只是旧版长规则参考层，不是 active skill，不自动升级为 reviewer hard issue 来源。
- 短结尾集不要过度合并；同一空间里如果剧情目标切换，例如“爽点结果 → 新任务启动 → 下一地点落点”，应拆组或给独立收束段，不能为了减少组数压进一个 15 秒组。
- 除非 `TASK.md` / `context.md` 明确 `target_video_model=happyhorse`，不要读取或套用 HappyHorse 规则。

## Claude Code 分发模式

本流程兼容 Claude Code 原生 Agent 工具。`prepare-agent.ps1` 创建的工作区与 CLI 无关，以下是用 Claude Code 特性完成分发生产的规则。

### 你是 dispatcher

当用户要求处理某个 run（如 `agent_runs/youyuanzhai6-scene`）时，你的角色是 dispatcher：

1. 先读 `agent_runs/<run-name>/NEXT_STEPS.md` 获取该 run 的剧集列表和输出目录。
2. 读 `agent_runs/<run-name>/context.md` 获取生成/审核 skill 路径和模式。
3. 用 Agent 工具（`run_in_background: true`）派发后台 worker，每个 worker 处理 1-2 集。

如果当前环境不能创建后台 worker/subagent，或需要用户授权才能创建，不能降级成主线程顺序生产多集；应输出 `NEED_USER_DISPATCH` 并列出待分发的 episode prompt 路径。

### 调度规则（沿用 AGENTS.md）

- **质量单位是单集**，不是批次。
- 默认 **1 集 / worker**。仅当单集很短、场景少、剧情密度低时可 **2 集 / worker**。
- 未经用户明确批准，不要超过 2 集 / worker。
- 最多同时运行 **5 个 worker**。
- 同一个 worker 处理 2 集时，必须完整完成第一集（生成→审核→修复→校验），再处理第二集。不能合并审核、合并输出或互相引用上下文。
- 完成一个 worker 后再启动新的，滚动推进。
- 不要一次把全部集数派完；每次派发当前空闲槽位数量的 worker。

### Worker 必须做的事（每个 episode）

每个 worker agent 会收到自己的 episode 目录路径，必须：

1. 读 `TASK.md`（确认 mode 和所需输出文件）。
2. 读 `agent_prompt.md`。
3. 读 `script.txt`（和 `segments/segXX/script.txt`，如果有）。
4. 读 `TASK.md` 指定的 generator skill 和 reviewer skill；不要把横屏任务交给竖屏 skill。
5. 使用当前 generator skill 生成分镜草稿。
6. 使用当前 reviewer skill 做真实审核（输出原始 JSON 到 `review.txt` 或 `segments/segXX/review.md`）。
7. 只修 reviewer 指出的 hard issues，不做无关重写。
8. 修复后必须再次使用 reviewer 复审，不能只跑格式校验。
9. 写出该模式要求的全部文件（见 TASK.md）。
10. 运行 `python storyboard_agent_workspace.py validate-episode --episode-dir <episode_dir>` 直到通过，或无法修复时标记 `needs_review`。
11. 完成后简要报告：哪一集、pass 还是 needs_review、剩余 issues 数。

**关键：** `review.txt` 和 `segments/segXX/review.md` 必须是当前 run 指定 reviewer 返回的真实原始 JSON。不能写占位文本、不能伪造 review。validate-episode 会检查 reviewer 证据。

### Reviewer 硬门槛

`review.txt` 和 `segments/segXX/review.md` 必须是真实审核结果，不能写占位文本、JSON、或伪造通过状态。`validate-episode` 只是客观格式校验和 reviewer 证据校验，不能替代真实审核。

真实审核必须满足以下证据要求：

- reviewer 必须读取并对照同一 episode 的 `script.txt`、当前 `final.txt`，以及当前 run 指定的 generator/reviewer skill。
- `scene` 模式下，每个 `segments/segXX/review.md` 必须是该 segment 草稿的真实 reviewer JSON；整集 `review.txt` 必须是组装后 `final.txt` 的真实 reviewer JSON。
- reviewer 至少检查：原剧本台词是否漏删改、人物关系是否错置、对话对象是否明确、组首空间锁定是否完整、组尾衔接是否自然、组时长和镜头时长是否符合规则、是否新增剧情或模板化描述。
- 如果 reviewer 没有逐项审查，不允许写 `pass: true`；应写 `status: "needs_review"`，并在 `hard_issues_remaining` 中说明"reviewer 未完成"。
- 如果 reviewer 返回 hard issues，必须先局部修复对应组，再复审；复审前不允许把 `status.json` 写成 `done`。
- 不允许把 `validate-episode`、`SUMMARY.md`、脚本检查、人工粗看、或空 issues JSON 当作 reviewer 结果。
- 交付说明必须明确写出：哪些 episode 已执行真实 reviewer，哪些 episode 修过 hard issues，哪些仍为 `needs_review`。

### Worker prompt 模板

派发 worker 时，使用以下结构的 prompt（替换 `{episode_dir}` 等变量）：

```
你是分镜生产 worker agent。你只负责处理一集（或多集 batch 中的当前一集）。

## 工作目录
Episode 目录：{episode_dir}

## 第一步：读入所有规则和输入
1. 读 `{episode_dir}/TASK.md` 了解 mode 和所需输出。
2. 读 `{episode_dir}/agent_prompt.md`。
3. 读 `TASK.md` 指定的 generator skill 和 reviewer skill；竖屏默认用 `storyboard-generator/storyboard-reviewer`，横屏必须用 `storyboard-horizontal-generator/storyboard-horizontal-reviewer`。
4. 读 `{episode_dir}/script.txt`（和 segments 下的分段剧本，如有）。

## 第二步：按 TASK.md 的 Mode 执行

### 阶段计时
在每个阶段开始前记录时间戳，完成后计算耗时。最终在报告中输出计时摘要。

### scene 模式（逐 segment 闭环）
对每个 segment：
1. **生成草稿** → 写入 `segments/segXX/draft.txt`
2. **机械预检**（在调用 reviewer 之前）：
   ```powershell
   python storyboard_agent_workspace.py validate-episode --episode-dir "{episode_dir}" --pre-check --content-file "{episode_dir}/segments/segXX/draft.txt"
   ```
   预检失败 → 修复格式/时长/cut_id 问题 → 重新预检。预检通过后才进 reviewer。
3. **Reviewer 审核** → 写入 `segments/segXX/review.md`（必须是真实 reviewer JSON）
4. **精准修复**：只重写 reviewer 指出的 hard issue 所在的时间段/组，不重写无关内容。
5. **复审**：修复后必须再次使用 reviewer 复审，不能只跑格式校验。
6. **写 final** → `segments/segXX/final.txt`

所有 segment 完成后：
7. 组装整集 `final.txt`
8. 机械预检整集：
   ```powershell
   python storyboard_agent_workspace.py validate-episode --episode-dir "{episode_dir}" --pre-check
   ```
9. 整集 reviewer 审核 → `review.txt`
10. 精准修复 + 复审（如有 hard issues）

### single 模式
1. 生成整集草稿
2. 机械预检（--pre-check --content-file 指向草稿）
3. Reviewer 审核
4. 精准修复 + 复审
5. 写 final.txt

## 第三步：写出全部要求文件
按 TASK.md 的 Required Outputs 列表写出所有文件。

## 第四步：运行完整校验
```powershell
python storyboard_agent_workspace.py validate-episode --episode-dir "{episode_dir}"
```
如果校验失败，按报错修复后重新校验。修复两轮仍无法通过则标记 needs_review。

## 第五步：报告
完成后输出：
- 集号、status（done/needs_review）、reviewer pass 状态、剩余 hard issues 数
- 计时摘要：各阶段耗时（生成/预检/审核/修复/复审/校验）

## 约束
- 只读写 `{episode_dir}` 目录下的文件。
- 不要调用外部 API 或其他 CLI。
- 最终稿必须是自然分镜文本，不能输出 JSON 或调试标记。
- 遵守当前 skill 的时长合同：竖屏每组 10-15 秒；横屏按当前横屏 TASK/skill 合同执行。
- 禁止模板化批量稿（如"空间先被交代出来""人物面部肌肉随局势绷紧"等）。
- 修复时只改 reviewer 指出的组，不重写无关组。
```

### 校验与收集（dispatcher 收尾）

收集前必须先确认每集已完成真实 reviewer：

- 查看每集 `review.txt`，确认它是按当前 run 指定 reviewer 对照原剧本和 `final.txt` 生成的审核 JSON。
- 查看 `status.json`，确认 `reviewer_source` 为当前 run 指定 reviewer（竖屏默认 `storyboard-reviewer`，横屏默认 `storyboard-horizontal-reviewer`），且 `reviewer_pass`、`reviewer_issues_count`、`reviewer_warnings_count` 与 `review.txt` 一致。
- 如果发现 `review.txt` 是占位、空 issues 伪通过、只来自脚本校验、或没有真实审稿过程，必须停止收集，重新审核该 episode。
- 只有真实 reviewer 通过或明确标记 `needs_review` 的 episode，才能进入收集；不能把未审核 episode 包装成 `done`。

所有 worker 完成后：

1. 整轮校验：
```powershell
$failed=@()
Get-ChildItem .\agent_runs\<run-name>\episodes -Directory | Sort-Object Name | ForEach-Object {
  python .\storyboard_agent_workspace.py validate-episode --episode-dir $_.FullName
  if ($LASTEXITCODE -ne 0) { $failed += $_.Name }
}
if ($failed.Count -gt 0) { throw "Validation failed: $($failed -join ', ')" }
```

2. 收集结果：
```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

### Python / 脚本边界

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

### 质量底线

最终分镜必须是自然中文分镜文本，不要输出 JSON、调试标记或其他非分镜正文内容。

禁止模板化批量稿，尤其是这类表达：

- "空间先被交代出来"
- "镜头从场景布局转向在场人物"
- "视线关系落在当前冲突中心"
- "人物面部肌肉随局势绷紧"
- "眉头和嘴角随情绪细微变化"

普通空间 / 环境交代镜头通常 2 秒；只有原剧本明确存在连续动作时才可到 3 秒。不能用 3 秒环境镜头批量凑组时长。

### 参考层

- Seedance 风格参考层：`agent_skills/seedance-prompt-profile/SKILL.md`，只用于选择性参考官方模板结构，不得替代主生成规则。
- 当前竖屏主生成规则：`agent_skills/storyboard-generator/SKILL.md`。
- 竖屏复杂情况参考层：`agent_skills/storyboard-generator/REFERENCE.md`，只用于查阅，不是 active skill。
- 横屏任务只使用横屏 generator/reviewer skill，不套用竖屏主 SKILL。

### 资产表阶段

分镜全部完成后，如需生成生图资产表，读 `agent_skills/asset-extractor/SKILL.md`。

资产阶段调度：
- 默认 3 集 / worker，稳定后可 4 集 / worker。
- 多集项目必须先创建 `agent_runs/<run-name>/asset_bible.md` 固定跨集人物/场景/道具设定。
- 每个 worker 逐集闭环：生成 `assets.md` → 检查五类表和中英双语提示词 → 转换 `assets.xlsx` → 下一集。
- 多个 worker 不并发写 `asset_bible.md`。
