# Storyboard Agent Context

## Workspace
- Project root: `G:\Auto-Storyboard`
- Prompt source: `G:\Auto-Storyboard\6688竖屏古装分镜prompt.txt`
- Final output directory: `G:\Auto-Storyboard\outputs_agent_jiaqianyi_dalao_baohong_scene`
- Episodes in this run: `40`
- Generation mode: `scene`
- Generation Skill: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
- Review Skill: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`

## Core Rules
- 你是竖屏古装短剧分镜生产 agent。
- 生成和审核规则全部以两个标准 `SKILL.md` 为准，不要在任务文件里重新解释规则。
- 生成和审核必须在同一个 agent 会话内完成，避免“换会话越修越歪”。
- `single` 模式：整集一次生成，再整集审核一次。
- `scene` 模式：按场景标题拆段生成，再组装整集并审核。
- 审核后只修硬错误；不要每次全量重写。
- 每集最终产出 `final.txt` 和 `status.json`。
- 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
- 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；这次由当前 CLI agent 自己完成文本生成和审核。
- 最终 `final.txt` 必须是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
