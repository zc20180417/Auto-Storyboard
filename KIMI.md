# Kimi Code 入口

先读 `AGENTS.md`。生产主流程写在 `README_AGENT_WORKFLOW.md`。

重要规则：不要让 Python 调用 Kimi Code、Codex CLI、Qwen CLI、Claude Code 或其他模型 CLI。请直接在 `prepare-agent.ps1` 创建的文件工作区里完成生成、审核和修复。

## Kimi Code 分发模式

本流程兼容 Kimi Code 原生 Agent 工具。`prepare-agent.ps1` 创建的工作区与 CLI 无关，以下是用 Kimi Code 特性完成分发生产的规则。

### 你是 dispatcher

当用户要求处理某个 run（如 `agent_runs/youyuanzhai6-scene`）时，你的角色是 dispatcher：

1. 先读 `agent_runs/<run-name>/NEXT_STEPS.md` 获取该 run 的剧集列表和输出目录。
2. 读 `agent_runs/<run-name>/context.md` 获取生成/审核 skill 路径和模式。
3. 用 Agent 工具（`run_in_background: true`）派发后台 worker，每个 worker 处理 1-2 集。

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
2. 读 `script.txt`（和 `segments/segXX/script.txt`，如果有）。
3. 读 `agent_skills/storyboard-generator/SKILL.md` 和 `agent_skills/storyboard-reviewer/SKILL.md`。
4. 使用 generator skill 生成分镜草稿。
5. 使用 reviewer skill 做真实审核（输出原始 JSON 到 `review.txt` 或 `segments/segXX/review.md`）。
6. 只修 reviewer 指出的 hard issues，不做无关重写。
7. 写出该模式要求的全部文件（见 TASK.md）。
8. 运行 `python storyboard_agent_workspace.py validate-episode --episode-dir <episode_dir>` 直到通过，或无法修复时标记 `needs_review`。
9. 完成后简要报告：哪一集、pass 还是 needs_review、剩余 issues 数。

**关键：** `review.txt` 和 `segments/segXX/review.md` 必须是 storyboard-reviewer 返回的真实原始 JSON。不能写占位文本、不能伪造 review。validate-episode 会检查 reviewer 证据。

### Worker prompt 模板

派发 worker 时，使用以下结构的 prompt（替换 `{episode_dir}` 等变量）：

```
你是分镜生产 worker agent。你只负责处理一集（或多集 batch 中的当前一集）。

## 工作目录
Episode 目录：{episode_dir}

## 执行顺序铁律（严禁跳过或颠倒）
1. 必须先写出 `draft.txt`（或逐 segment 写出 `segments/segXX/draft.txt`）。
2. 必须先用 storyboard-reviewer 审核 draft，写出 `review.md`（含真实 JSON）。
3. 必须根据 review 修复后写出 `final.txt`。
4. 最后才运行 `validate-episode` 校验。

**严禁在 draft.txt 不存在时运行校验命令。**

## 第一步：读入所有规则和输入
1. 读 `{episode_dir}/TASK.md` 了解 mode 和所需输出。
2. 读 `agent_skills/storyboard-generator/SKILL.md`。
3. 读 `agent_skills/storyboard-reviewer/SKILL.md`。
4. 读 `{episode_dir}/script.txt`（和 segments 下的分段剧本，如有）。

## 第二步：按 TASK.md 的 Mode 执行
- scene 模式：逐 segment 生成→审核→修复，再组装整集 final.txt 并做整集审核。
- single 模式：整集生成→整集审核→修复。

## 第三步：写出全部要求文件
按 TASK.md 的 Required Outputs 列表写出所有文件。

## 第四步：运行校验
```powershell
python storyboard_agent_workspace.py validate-episode --episode-dir "{episode_dir}"
```
如果校验失败，按报错修复后重新校验。修复两轮仍无法通过则标记 needs_review。

## 第五步：报告
完成后只输出：集号、status（done/needs_review）、reviewer pass 状态、剩余 hard issues 数。

## 约束
- 只读写 `{episode_dir}` 目录下的文件。
- 不要调用外部 API 或其他 CLI。
- 最终稿必须是自然分镜文本，不能输出 JSON 或调试标记。
- 禁止模板化批量稿（如"空间先被交代出来""人物面部肌肉随局势绷紧"等）。
```

### 超时与调度注意事项

Kimi Code 后台 worker 有 **15 分钟（900 秒）硬超时**。根据已验证的经验：
- **短集（1 segment，<2000 字符）**：通常 5-10 分钟可完成，可用 2 集/worker。
- **长集或多 segment 集**：建议只用 **1 集/worker**，避免超时中断。
- **超时兜底**：若 worker 超时终止，dispatcher 应先检查该 episode 目录下 `final.txt` 和 `status.json` 是否已存在。若已存在且 `validate-episode` 能通过，则视为完成，无需重发。

### 校验与收集（dispatcher 收尾）

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

### 资产表阶段

分镜全部完成后，如需生成生图资产表，读 `agent_skills/asset-extractor/SKILL.md`。

资产阶段调度：
- 默认 3 集 / worker，稳定后可 4 集 / worker。
- 多集项目必须先创建 `agent_runs/<run-name>/asset_bible.md` 固定跨集人物/场景/道具设定。
- 每个 worker 逐集闭环：生成 `assets.md` → 检查五类表和中英双语提示词 → 转换 `assets.xlsx` → 下一集。
- 多个 worker 不并发写 `asset_bible.md`。
