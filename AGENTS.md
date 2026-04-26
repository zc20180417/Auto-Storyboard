# Auto Storyboard Agent 入口

本项目的生产主流程是“文件工作区式 Agent 工作流”。

## 先读这些文件

1. `README.md`
2. `README_AGENT_WORKFLOW.md`
3. `agent_skills/storyboard-generator/SKILL.md`
4. `agent_skills/storyboard-reviewer/SKILL.md`

## 核心规则

- 不要让 Python 调用 Codex CLI、Qwen CLI、Claude Code、Kimi Code 或任何模型 CLI。
- Python 只负责准备工作区、做客观 clean-format 校验、收集结果。
- 分镜生成、审核、局部修复必须在当前 agent 会话内完成。
- 生产默认优先使用 `scene` 模式；只有短集、简单集才用 `single`。
- 最终分镜必须是自然中文分镜文本；不要输出 JSON、`<<<GROUP>>>`、`SHOT` 或其他机器标签。
- 每集任务保持独立。并发按“集”拆，不要把多集合并进一个 agent 上下文。
- 处理某个集数范围时，不要改写无关集数或无关输出。

## 常用命令

创建生产工作区：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Force
```

校验单集：

```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\<run-name>\episodes\ep01
```

收集最终输出：

```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

## 当前生产参考

- 最新已验证工作区：`agent_runs/youyuanzhai6-scene`
- 最新已验证输出：`outputs_agent_youyuanzhai6_scene`
- 当前主提示词：`6688竖屏古装分镜prompt.txt`

旧 GUI/API 文件已归档到 `legacy/`。除非用户明确要求恢复旧流程，否则不要使用归档文件。
