# Claude Code 入口

先读 `AGENTS.md`。生产主流程写在 `README_AGENT_WORKFLOW.md`。

重要规则：不要让 Python 调用 Claude Code、Codex CLI、Qwen CLI、Kimi Code 或其他模型 CLI。请直接在 `prepare-agent.ps1` 创建的文件工作区里完成生成、审核和修复。

## 启动判定与红线（Claude Code 自动加载，必读）

`CLAUDE.md` 会被 Claude Code 自动注入上下文，`AGENTS.md` 不会——只有 agent 主动读取它才生效。因此以下红线即使没读 `AGENTS.md` 也必须遵守。完整规则仍以 `AGENTS.md` 为唯一真源，与当前 run 冲突时以该 run 的 `TASK.md` / `NEXT_STEPS.md` / `DISPATCH_PROMPT.md` 为准。

### 1. dispatcher 判定（对齐 AGENTS.md「启动前硬检查」）

- 任务包含 2 集以上 episode 时，本会话默认是 dispatcher。
- dispatcher 禁止亲自生产分镜正文，禁止顺序处理多集，禁止写入任何 `episodes/ep*/draft.txt`、`episodes/ep*/final.txt`、`episodes/ep*/review.txt`、`episodes/ep*/segments/**`、`episodes/ep*/status.json`。
- dispatcher 必须用 Agent 工具并发派发 worker：默认 **1 集 / worker**，未经用户明确批准不超过 **2 集 / worker**。
- 并发 worker 数以当前 run 的 `DISPATCH_PROMPT.md` / `NEXT_STEPS.md` 里的 `Run up to N workers in parallel` 为准（由 prepare 时的 `--parallelism` 决定，默认 5），但**任何情况下不得超过 5 个**。run 文件写的数大于 5 时按 5 执行。
- 如果当前环境不能创建 worker/subagent，或创建 worker 需要用户授权，必须**立即停止并向用户请求分发授权**，或按当前 run 的 `DISPATCH_PROMPT.md` 输出 `NEED_USER_DISPATCH` 和待分发 prompt 路径。**不得因为不能开 worker 就降级为主线程顺序产稿。**

### 2. skill 路由（对齐 AGENTS.md「先读这些文件」）

**先看 video profile，再看 aspect。** profile 路由优先于下面的竖屏/横屏默认。

- 当前 run 的 `TASK.md` / `context.md` 标记 `Video profile: seedance-2.5-live-vertical` 或 `video_profile=seedance-2.5-live-vertical` 时，generator 用 `agent_skills/seedance-2-5-live-vertical-generator/SKILL.md`，reviewer 用 `agent_skills/seedance-2-5-live-vertical-reviewer/SKILL.md`，并同时读模型硬合同 `agent_skills/seedance-2-5-live-vertical/SKILL.md`，`reviewer_source` = `seedance-2-5-live-vertical-reviewer`。该 profile 只允许 `vertical` + `live-action` + `multimodal_generation`，每组 4-30 整数秒、整数秒时间轴；**不要套用 2.0 的 6-15 秒、0.5 秒边界或固定大包 `--neg`**。
- 未标记该 profile 时按 aspect 走下面两条（即 `seedance-2.0` 兼容流程）。
- 默认竖屏：generator 用 `agent_skills/storyboard-generator/SKILL.md`，reviewer 用 `agent_skills/storyboard-reviewer/SKILL.md`，`status.json` 的 `reviewer_source` = `storyboard-reviewer`。
- 当前 run 的 `TASK.md` / `context.md` 标记 `Aspect: horizontal` 或 `storyboard_aspect=horizontal` 时，改用 `agent_skills/storyboard-horizontal-generator/SKILL.md` 和 `agent_skills/storyboard-horizontal-reviewer/SKILL.md`，`reviewer_source` = `storyboard-horizontal-reviewer`。
- 不要把横屏任务交给竖屏 skill，反之亦然；也不要把 2.5 profile 的 run 交给 2.0 的通用竖屏 skill。一切以 `TASK.md` 指定的 skill 为准。

### 3. 模式默认

- 用户或 `TASK.md` 未指定时，默认 `scene` 模式；只有短集、单场景、格式稳定时才用 `single`。

## Claude Code 分发模式

本流程兼容 Claude Code 原生 Agent 工具。`prepare-agent.ps1` 创建的工作区与 CLI 无关，以下是用 Claude Code 特性完成分发生产的规则。

### 你是 dispatcher

当用户要求处理某个 run（如 `agent_runs/youyuanzhai6-scene`）时，你的角色是 dispatcher：

1. 先读 `agent_runs/<run-name>/NEXT_STEPS.md` 获取该 run 的剧集列表和输出目录。
2. 读 `agent_runs/<run-name>/context.md` 获取生成/审核 skill 路径和模式。
3. 用 Agent 工具（`run_in_background: true`）并发派发后台 worker（每 worker 集数与并发上限见上方「dispatcher 判定」）。

### 调度规则（沿用 AGENTS.md）

- **质量单位是单集**，不是批次（调度数量见上方「dispatcher 判定」）。
- 只有单集很短、场景少、剧情密度低时才用 2 集 / worker；此时同一 worker 必须完整完成第一集（生成→审核→修复→校验）再处理第二集，不能合并审核、合并输出或互相引用上下文。
- 不要一次把全部集数派完；每次只派发空闲槽位数量的 worker，完成一个再补一个，滚动推进。

### Worker 必须做的事（每个 episode）

每个 worker agent 会收到自己的 episode 目录路径，必须：

1. 读 `TASK.md`（确认 mode 和所需输出文件）。
2. 读 `script.txt`（和 `segments/segXX/script.txt`，如果有）。
3. worker 启动时完整读一次 `TASK.md` 指定的 generator、reviewer 和 profile skill；同一 worker、同一 run 的文件未变化时，在审核、修复复审和双集 batch 的第二集直接复用，不重复加载。
4. 使用 generator skill 生成分镜草稿。
5. 使用 reviewer skill 做真实审核（输出原始 JSON 到 `review.txt` 或 `segments/segXX/review.md`）。
6. 只修 reviewer 指出的 hard issues，不做无关重写。
7. 写出该模式要求的全部文件（见 TASK.md）。
8. 运行 `python storyboard_agent_workspace.py validate-episode --episode-dir <episode_dir>` 直到通过，或无法修复时标记 `needs_review`。
9. 完成后简要报告：哪一集、pass 还是 needs_review、剩余 issues 数。

**关键：** `review.txt` 和 `segments/segXX/review.md` 必须是 `TASK.md` 指定 reviewer 返回的真实原始 JSON。不能写占位文本、不能伪造 review。validate-episode 会检查 reviewer 证据。

### Worker prompt 模板

派发 worker 时，使用以下结构的 prompt（替换 `{episode_dir}` 等变量）：

```
你是分镜生产 worker agent。你只负责处理一集（或多集 batch 中的当前一集）。

## 工作目录
Episode 目录：{episode_dir}

## 第一步：读入所有规则和输入
1. 读 `{episode_dir}/TASK.md` 了解 mode、aspect 和所需输出。
2. worker 首个 episode 完整读 `TASK.md` 指定的 generator skill，不按 aspect 猜测或覆盖 profile 路由；同 run 已加载且文件未变化时复用。
3. worker 首个 episode 完整读 `TASK.md` 指定的 reviewer skill；审核与修复复审不重复加载未变化的 skill。
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
