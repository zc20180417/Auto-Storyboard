# 自动分镜生产工具

本项目用于把短剧剧本自动转成视频分镜，默认支持竖屏短剧，也支持独立的 16:9 横屏分镜工作流。当前推荐的生产流程是 **Agent 工作流**：Python 只准备文件工作区、校验自然格式、收集结果；分镜生成、审核、局部修复由 Codex、Claude Code、Qwen Code 等 agent 在同一会话内完成。

## 推荐入口

详细流程见 [README_AGENT_WORKFLOW.md](README_AGENT_WORKFLOW.md)。

最常用命令：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Force
```

横屏分镜加 `-Aspect horizontal`，会使用独立横屏生成和审核 skill：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Aspect horizontal `
  -Force
```

agent 完成后收集结果：

```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

## 生产建议

- 默认用 `scene` 模式；只有短集、单场景、格式稳定时才用 `single`。
- 每集作为独立 agent 任务并发处理，推荐 3-5 个 worker。
- 不要让 Python 调用 Codex/Qwen/Claude CLI。
- 最终输出必须是自然分镜文本，不要机器标签，不要 JSON。
- 竖屏默认读取 `agent_skills/storyboard-generator` / `agent_skills/storyboard-reviewer`。
- 横屏读取 `agent_skills/storyboard-horizontal-generator` / `agent_skills/storyboard-horizontal-reviewer`；横屏最终分镜仍是自然分镜正文，横屏 reviewer 输出 raw JSON 审核结果。
- 新剧本格式不稳定时，先人工/agent 识别集数边界，再写专用拆分脚本。

## 其他说明

- GUI/API 旧流程已归档，见 [legacy/gui_api/README_GUI.md](legacy/gui_api/README_GUI.md) 和 [legacy/gui_api/README_AUTOMATION.md](legacy/gui_api/README_AUTOMATION.md)。
- 当前生产主流程以 [README_AGENT_WORKFLOW.md](README_AGENT_WORKFLOW.md) 为准。
