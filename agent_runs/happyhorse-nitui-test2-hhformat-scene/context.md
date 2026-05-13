# Storyboard Agent Context

        ## Workspace
        - Project root: `G:\Auto-Storyboard`
        - Generation rules source: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
        - Review rules source: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
        - Final output directory: `G:\Auto-Storyboard\outputs_agent_happyhorse_nitui_test2_hhformat`
        - Episodes in this run: `2`
        - Generation mode: `scene`
        - Generation Skill: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
        - Review Skill: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
        - Target video model: `happyhorse`
- HappyHorse Prompt Profile: `G:\Auto-Storyboard\agent_skills\happyhorse-prompt-profile\SKILL.md`
- AI Video Prompt Skill: `G:\Auto-Storyboard\agent_skills\ai-video-prompt\SKILL.md`
- Seedance Prompt Profile: `G:\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`

        ## Core Rules
        - dispatcher 不生成、不审核、不修稿；dispatcher 只创建 subagents/workers 并分发 episode prompt。
        - episode worker 是竖屏短剧分镜生产 agent，只处理自己被分配的单个 episode。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准；HappyHorse / Seedance Prompt Profile 与 AI Video Prompt Skill 只作为 HappyHorse 目标模型下的短剧风格参考层，不要在任务文件里重新解释规则。
        - profile 不得替代主生成规则，不得把模板编号、官方模板说明、`@图片/@视频/@音频` 占位符、广告/产品/视频延长/轨道补全/一镜到底等非短剧模板语气写入 `final.txt`。
        - episode worker 可以生成和初审，但 `review.txt` 必须按 `storyboard-reviewer/SKILL.md` 逐项审稿，不能写空泛通过。
        - 若用户要求强审核模式，reviewer-only worker 必须独立复审 `final.txt`。
        - `single` 模式：整集一次生成，再整集审核一次。
        - `scene` 模式：按场景标题拆段生成，再组装整集并审核。
        - 审核后只修硬错误；不要每次全量重写。
        - 每集最终产出 `final.txt` 和 `status.json`。
        - 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
        - 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；Python 只准备、校验和收集。
        - 最终 `final.txt` 必须是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
