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

如需动漫 3D CG 短剧风格，保留竖屏/横屏和视频模型设置不变，额外指定视觉风格：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -VisualStyle 3d-cg `
  -Force
```

默认 `-VisualStyle live-action`，继续使用真人实拍短剧口径。

如需独立的 Seedance 2.5 真人竖屏短剧合同，显式选择 profile：

```powershell
.\prepare-agent.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Aspect vertical `
  -VisualStyle live-action `
  -VideoProfile seedance-2.5-live-vertical `
  -VideoResolution 720p `
  -Force
```

也可以使用固定入口，避免重复填写 profile、竖屏和真人参数；它不改变原 `prepare-agent.ps1` 的 Seedance 2.0 默认值：

```powershell
.\prepare-agent-seedance25.ps1 scene <run-name> `
  -Source .\split_scripts\<episode-folder> `
  -OutDir .\outputs_agent_<name> `
  -Force
```

该 profile 固定目标模型 `doubao-seedance-2-5-260628`，使用 9:16、24fps、原生音频、4-30 秒整数时间轴；当前只开放 480p/720p，默认 720p。唯一视频任务是 `multimodal_generation`，真实模型调用必须至少绑定 1 项图片、视频或音频素材；分镜母版本身不等于生成就绪。纯文本、参考生成、首尾帧/关键帧、视频编辑、视频延长/续写和轨道补全全部禁用。它会切换到独立生成器、审核器和收集尾部，且不会追加旧版大包通用 `--neg`。不传 `-VideoProfile` 时仍走原有 `seedance-2.0` 默认流程。

如需 Seedance 2.5 横屏 3D CG 仙侠动漫，使用独立入口（首期只支持 `single`）：

```powershell
.\prepare-agent-dandao-xiantu.ps1 single <run-name> `
  -Source .\tests\fixtures\dandao-xiantu `
  -OutDir .\outputs_agent_<name> `
  -Force
```

该入口固定 `seedance-2.5-horizontal-xianxia-3d-cg`、`horizontal`、`3d-cg`、`16:9`、720p、4-30 秒整数时长、原生音频和 `realistic-material-restrained-anime-outline` 画风，并显式加载 `dandao-xiantu` 项目包的炼丹/灵火/丹药/元鼎/回溯规则。其 v2 provider package 使用 reference content 映射，不在创建请求中发送 `fps`；24 fps 只用于结果媒体验收。没有经过认证的 ManJuWeb/CPA consumer 证据和授权 Active 素材时，状态必须保持 `submit_allowed=false`，不能把离线 fixture 当成真实视频验证。详见 [横屏仙侠操作状态](docs/seedance25-operator-status.md)、[真实探针协议](docs/seedance25-real-probe-protocol.md) 和 [v2 素材交接合同](docs/seedance-material-handoff-v2.md)。

Seedance 2.5 校验会自动保留并收集 `storyboard_index.json` / `storyboard_index.xlsx`。资产表审核通过后，可编译素材交接清单；ManJuWeb 回写真实 Ark 结果后，再生成受哈希保护的可调用包：

```powershell
python .\storyboard_agent_workspace.py export-seedance-material-requirements --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py validate-seedance-materials --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py export-seedance-package --episode-dir <episode-dir>
```

Auto-Storyboard 不保存 Ark 状态，ManJuWeb 是 Ark `assetId` 和状态的唯一权威来源。完整边界见 [Seedance 2.5 素材交接合同](docs/seedance-material-handoff-v1.md)。

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
- `-VideoProfile seedance-2.5-live-vertical` 只支持 `vertical` + `live-action` + `multimodal_generation`，读取独立的 `seedance-2-5-live-vertical-generator` / `seedance-2-5-live-vertical-reviewer` / `seedance-2-5-live-vertical`；没有真实多模态素材时不得回退到其他任务模式。
- 横屏读取 `agent_skills/storyboard-horizontal-generator` / `agent_skills/storyboard-horizontal-reviewer`；横屏最终分镜仍是自然分镜正文，横屏 reviewer 输出 raw JSON 审核结果。
- `-VisualStyle 3d-cg` 会切换生成提示、收集尾部和资产提示词口径为动漫 3D CG；它不是新题材，不改变剧情忠实度、时长、站位、道具连续和 reviewer 门禁。
- 新剧本格式不稳定时，先人工/agent 识别集数边界，再写专用拆分脚本。

## 其他说明

- GUI/API 旧流程已归档，见 [legacy/gui_api/README_GUI.md](legacy/gui_api/README_GUI.md) 和 [legacy/gui_api/README_AUTOMATION.md](legacy/gui_api/README_AUTOMATION.md)。
- 当前生产主流程以 [README_AGENT_WORKFLOW.md](README_AGENT_WORKFLOW.md) 为准。
