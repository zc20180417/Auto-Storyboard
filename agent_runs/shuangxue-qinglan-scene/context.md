# Storyboard Agent Context

        ## Workspace
        - Project root: `H:\BaiduNetdiskDownload\Auto-Storyboard`
        - Generation rules source: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
        - Review rules source: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
        - Final output directory: `H:\BaiduNetdiskDownload\Auto-Storyboard\outputs_agent_shuangxue_qinglan_scene`
        - Episodes in this run: `30`
        - Generation mode: `scene`
        - Storyboard aspect: `vertical` (竖屏)
        - Generation Skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
        - Review Skill: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
        - Target video model: `seedance`
- Seedance Prompt Profile: `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_skills\seedance-prompt-profile\SKILL.md`

        ## Core Rules
        - dispatcher 不生成、不审核、不修稿；dispatcher 只创建 subagents/workers 并分发 episode prompt。
        - episode worker 是竖屏短剧分镜生产 agent，只处理自己被分配的单个 episode。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准；Seedance Prompt Profile 只作为短剧风格参考层，不要在任务文件里重新解释规则。
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

## Series Bible / 人物小传

### 剧本背景年代设定与核心人物小传

#### 一、 时代背景设定
**【现代/当代都市】**
*   **社会背景**：故事发生在高度信息化的现代都市。智能手机、手机银行APP转账、云端视频备份、自动取款机（ATM）等科技元素是推动剧情和揭露真相的重要工具。
*   **商业与法律环境**：具备成熟的现代商业与法律体系，如创业公司“A轮融资”、CEO职位设定、税务局查账、经侦大队介入、法院强制腾房执行令以及规范的银行流水追溯机制。

---

#### 二、 核心人物小传

**1. 沈清（女，约28岁）**
*   **身份**：创业公司CEO、周桂兰的亲生女儿。
*   **外貌气质**：干练利落，常穿职业装，眼神锐利且充满压迫感，自带上位者的气场。
*   **性格特点**：杀伐果断、逻辑缜密、极度护短。对敌人冷酷无情，对母亲则充满极尽的温柔与愧疚。
*   **核心驱动力（原动力）**：**“绝不让母亲再受一丝委屈”**。早年因忙于创业未能陪伴母亲，在得知母亲被继父一家敲骨吸髓般虐待后，陷入极度的愤怒与自责。这份愧疚化作了她手撕反派、夺回一切的绝对力量。

**2. 周桂兰（女，约58岁）**
*   **身份**：沈清的亲生母亲，周建国的妻子（后离婚）。
*   **外貌气质**：前期面容沧桑、双手满是冻疮，穿着单薄起球的旧衣；后期在女儿的赡养下恢复气血，气质温婉从容。
*   **性格特点**：传统、隐忍、讨好型人格。前期为了家庭和睦，甚至为了不拖累女儿，选择打碎牙齿往肚子里咽；但在看清周家人的恶毒嘴脸后，最终彻底清醒并与其决裂。
*   **记忆点**：缺口的破瓷碗、腿部用胶布绑着的老花镜、贴身缝在内衣口袋里的遗嘱。

**3. 周建国（男，约62岁）**
*   **身份**：周桂兰的现任丈夫（倒插门），沈清的继父。
*   **性格特点**：极度虚伪、爹味十足、贪婪成性。表面上装作大义凛然的“一家之主”，满嘴“家和万事兴”，背地里却是个借高利贷挥霍、纵容亲生女儿偷窃老伴养老钱的无耻之徒。
*   **核心结局**：被揭穿倒插门与老赖身份，失去老家祖宅，沦为街头捡破烂的流浪汉，终在雪地中悔恨痛哭。

**4. 刘美娟/周美娟（女，约30岁）**
*   **身份**：周建国的亲生女儿，赵强之妻。
*   **性格特点**：贪慕虚荣、目光短浅、嚣张跋扈。心安理得地吸血继母，把沈清打来的赡养费当成自己的提款机，甚至在东窗事发时仍妄图撒泼耍赖逃避制裁。
*   **记忆点**：手腕上用继母赡养费买的古法金镯子、名牌包。

**5. 赵强（男，约32岁）**
*   **身份**：刘美娟的丈夫，强盛建材经营部老板。
*   **性格特点**：外强中干、欺软怕硬、唯利是图。仗着有点小生意自视甚高，实则是个敢做假账洗钱、偷税漏税的法盲。在沈清的绝对实力（查税、查账）面前，瞬间暴露出懦弱的本性。
*   **核心结局**：因偷税漏税及职务侵占被判有期徒刑五年。

**6. 小雨（女，10岁）**
*   **身份**：刘美娟与赵强的女儿。
*   **角色功能**：全剧开篇的“反差锚点”。她盛大的十岁生日Party（吃帝王蟹、买昂贵洋娃娃）与周桂兰在杂物间喝冷粥吃剩菜形成了强烈的视觉与心理冲击，是彻底点燃沈清怒火的导火索。






