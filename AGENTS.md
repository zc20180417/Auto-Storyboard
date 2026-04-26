# Auto Storyboard Agent 入口

本文件用于固化已经验证过的“文件工作区式 Agent 工作流”，避免后续 agent 自作主张降级成脚本批量生成、伪造审核、或把多集合并到同一个上下文里。

如果本文件与项目脚本生成的 `NEXT_STEPS.md` / `TASK.md` 冲突，以当前 run 的 `NEXT_STEPS.md` / `TASK.md` 为准，因为它们是该工作区的具体任务书。

## 先读这些文件

1. `README.md`
2. `README_AGENT_WORKFLOW.md`
3. `agent_skills/storyboard-generator/SKILL.md`
4. `agent_skills/storyboard-reviewer/SKILL.md`

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
4. 使用 `storyboard-reviewer` 做真实审核。
5. 只修 reviewer 指出的 hard issues，不做无关重写。
6. 写出该模式要求的全部文件。
7. 运行 `TASK.md` 中的 `validate-episode` 命令直到通过，或在确实无法修复时标记 `needs_review`。

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

`review.txt` 和 `segments/segXX/review.md` 必须是真实审核结果，不能写占位文本、JSON、或伪造通过状态。`validate-episode` 只是客观格式校验和 reviewer 证据校验，不能替代真实审核。

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

校验单集：

```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\<run-name>\episodes\ep01
```

收集最终输出：

```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

## 当前生产参考

- 最新已验证 `scene` 工作区：`agent_runs/youyuanzhai6-scene`
- 最新已验证 `single` 工作区：`agent_runs/youyuanzhai-single`
- 当前主提示词：`6688竖屏古装分镜prompt.txt`

旧 GUI/API 文件已归档到 `legacy/`。除非用户明确要求恢复旧流程，否则不要使用归档文件。
