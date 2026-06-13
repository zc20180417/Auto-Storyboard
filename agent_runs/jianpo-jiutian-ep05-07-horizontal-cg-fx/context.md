# Storyboard Agent Context

        ## Workspace
        - Project root: `H:\BaiduNetdiskDownload\Auto-Storyboard`
        - Generation rules source: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-generator\SKILL.md`
        - Review rules source: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-reviewer\SKILL.md`
        - Final output directory: `H:\BaiduNetdiskDownload\Auto-Storyboard\outputs_agent_jianpo_jiutian_ep05_07_horizontal_cg_fx`
        - Episodes in this run: `3`
        - Generation mode: `scene`
        - Storyboard aspect: `horizontal` (横屏)
        - Visual style: `3d-cg` (动漫3D CG)
        - Generation Skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-generator\SKILL.md`
        - Review Skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-horizontal-reviewer\SKILL.md`
        - Target video model: `seedance`
- Seedance Prompt Profile: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`

- 3D CG Visual Style Skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\3d-cg-visual-style\SKILL.md`

        ## Core Rules
        - dispatcher 不生成、不审核、不修稿；dispatcher 只创建 subagents/workers 并分发 episode prompt。
        - episode worker 是横屏短剧分镜生产 agent，只处理自己被分配的单个 episode。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准；Seedance Prompt Profile 只作为短剧风格参考层，不要在任务文件里重新解释规则。
        - profile 不得替代主生成规则，不得把模板编号、官方模板说明、`@图片/@视频/@音频` 占位符、广告/产品/视频延长/轨道补全/一镜到底等非短剧模板语气写入 `final.txt`。
        - Visual style 是本 run 的媒介风格约束：`3d-cg`（动漫3D CG）。动漫3D CG短剧风格：保留短剧分镜、对白、站位、道具连续和时间规则，但画面描述应服务于二次元角色设计、风格化面部与眼睛、清晰轮廓线、高质量卡通渲染、PBR材质与手绘质感融合、稳定表情绑定、清楚口型同步和流畅动作；动作/打斗/压迫/情绪峰值可以加入刀光、气流、碎石、尘浪、金属冷光等动作服务型大片特效；仙侠、玄幻、古武、强者归来、灵药/玄铁/真气/罡气/剑气题材的强节拍必须把克制可见特效写入镜头描述或光影设计，不能只靠固定画面风格尾部；特效必须跟随具体动作、灵物、压迫和受力结果，不得写成法阵、满屏粒子、游戏技能 UI 或盖住人物主体；不要写真人实拍、真实摄影、真实演员、纪录片摄影等真人媒介词。
        - episode worker 可以生成和初审，但 `review.txt` 必须按 `storyboard-horizontal-reviewer/SKILL.md` 逐项审稿，不能写空泛通过。
        - 若用户要求强审核模式，reviewer-only worker 必须独立复审 `final.txt`。
        - `single` 模式：整集一次生成，再整集审核一次。
        - `scene` 模式：按场景标题拆段生成，再组装整集并审核。
        - 审核后只修硬错误；不要每次全量重写。
        - 每集最终产出 `final.txt` 和 `status.json`。
        - 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
        - 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；Python 只准备、校验和收集。
        - 最终 `final.txt` 必须是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
