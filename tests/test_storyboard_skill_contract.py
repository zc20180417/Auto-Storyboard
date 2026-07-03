import unittest
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_SKILL = ROOT / "agent_skills" / "storyboard-generator" / "SKILL.md"
REVIEWER_SKILL = ROOT / "agent_skills" / "storyboard-reviewer" / "SKILL.md"
HORIZONTAL_GENERATOR_SKILL = ROOT / "agent_skills" / "storyboard-horizontal-generator" / "SKILL.md"
HORIZONTAL_TOPIC_PACKS = ROOT / "agent_skills" / "storyboard-horizontal-generator" / "TOPIC_PACKS.md"
CG_VISUAL_STYLE_SKILL = ROOT / "agent_skills" / "3d-cg-visual-style" / "SKILL.md"
CRAFT_PASS_SKILL = ROOT / "agent_skills" / "storyboard-craft-pass" / "SKILL.md"
QUALITY_POLICY = ROOT / "agent_skills" / "storyboard-quality-policy.json"
DIALOGUE_PROMPT = ROOT / "竖屏分镜规则_对话版.txt"
WORKSPACE_SCRIPT = ROOT / "storyboard_agent_workspace.py"


class StoryboardSkillContractTests(unittest.TestCase):
    def test_generator_has_front_loaded_production_priorities(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("## 生产优先级（先读此段）", text)
        self.assertIn("最终分镜首先服务“视频模型稳定执行”", text)
        self.assertIn("时间规则服务于视频可执行性", text)
        self.assertIn("12. 复杂动作、保护站位、关键道具、多人物调度组可写短 `视频禁止项`", text)
        self.assertIn("内部检查以下 6 项", text)

    def test_generator_uses_modern_video_execution_examples(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("示例 A：外部事件进入", text)
        self.assertIn("示例 B：保护站位和关键道具连续", text)
        self.assertIn("车队压住庆贺声", text)
        self.assertIn("林远挡到父母身前", text)
        self.assertNotIn("朝堂对峙", text)

    def test_video_negative_hints_are_limited_and_specific(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("每组写 2-5 个本组特有错误", generator_text)
        self.assertIn("不每组复制同一串通用词", generator_text)
        self.assertIn("模板中的 `视频禁止项` 只是占位示例", generator_text)
        self.assertNotIn("视频禁止项：成绩单消失、林远提前上车", generator_text)
        self.assertIn("`视频禁止项` 超过 5 个", reviewer_text)
        self.assertIn("泛泛词如“画面混乱/人物错误/道具错误”", reviewer_text)

    def test_video_negative_policy_is_externalized(self):
        policy = json.loads(QUALITY_POLICY.read_text(encoding="utf-8"))

        self.assertIn("storyboard_rule_version", policy)
        self.assertEqual(policy["video_negative_constraints"]["max_items"], 5)
        self.assertIn("人物换位", policy["video_negative_constraints"]["generic_terms"])
        self.assertIn("本组关键道具消失", policy["video_negative_constraints"]["placeholder_terms"])
        self.assertIn("context_anchor_stop_terms", policy["video_negative_constraints"])
        self.assertIn("人物", policy["video_negative_constraints"]["context_anchor_stop_terms"])

    def test_external_event_entry_rule_is_reviewed(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("外部事件进入规则", generator_text)
        self.assertIn("事件进入 → 关键人物/道具状态变化 → 主角或被影响者反应 → 对峙/台词", generator_text)
        self.assertIn("外部事件进入被压缩到不可执行", reviewer_text)
        self.assertIn("优先按动作阶段写成同组内多个时间段", generator_text)
        self.assertIn("不应仅因强节拍数量多而判错", reviewer_text)

    def test_continuous_event_chains_are_not_mechanically_split(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("强节拍是容量核算工具，不是自动拆组触发器", generator_text)
        self.assertIn("连续事件链", generator_text)
        self.assertIn("不要因为每一步都有状态变化就机械拆成多个 10-15 秒组", generator_text)
        self.assertIn("强节拍只用于判断容量，不用于机械拆组", generator_text)
        self.assertIn("不能只按数量判 hard issue", reviewer_text)
        self.assertNotIn("对白+外部事件+中等/长动作+道具操作 同组？→ 是则拆组", generator_text)

    def test_high_impact_interrupt_reposition_rule_is_reviewed(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("高冲击打断与归位规则", generator_text)
        self.assertIn("打断/反应", generator_text)
        self.assertIn("放下道具/跨位移/保护站位/团圆确认", generator_text)
        self.assertIn("高冲击打断后又压入归位动作", reviewer_text)

    def test_reviewer_template_includes_video_execution_coverage(self):
        text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("生产 reviewer 默认也应在 `audit_coverage` 中包含并检查", text)
        self.assertIn('"action_atomicity": "checked"', text)
        self.assertIn('"video_negative_constraints": "checked"', text)
        self.assertIn('"type": "action_atomicity"', text)
        self.assertIn('"type": "video_negative_constraints"', text)

    def test_generator_prevents_low_density_time_padding(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("先估每个剧情块的自然时长，再组合成 6-15 秒组", text)
        self.assertIn("10-15 秒是常规承载区间，不是填满目标", text)
        self.assertIn("12-15 秒长组准入", text)
        self.assertIn("至少满足以下两项", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("明显多数（约三分之二以上）", text)
        self.assertIn("低密度组必须压缩或合并", text)
        self.assertIn("看向、低头、停住、等待、仍、继续、状态延续", text)
        self.assertIn("连续流程动作合并", text)
        self.assertIn("联系后勤、准备保温箱、递出一箱、登记一行、复核无误", text)
        self.assertIn("设备到场、接线、压缩机恢复", text)

    def test_reviewer_flags_low_density_padding_and_fragmented_process_groups(self):
        text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("12-15 秒长组未过长组准入", text)
        self.assertIn("低密度撑时长", text)
        self.assertIn("相邻同场景同冲突的流程节点", text)
        self.assertIn("联系、准备、递出、登记、复核", text)
        self.assertIn("不应各自写成 10-15 秒组", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("按 `generation_density` 或 `dialogue_pacing` 判 hard issue", text)

    def test_dramatic_pause_is_not_a_padding_exception(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("停顿不是质感例外", generator_text)
        self.assertIn("不再提供有动机戏剧停顿例外", generator_text)
        self.assertIn("高冲击后的可见反应可以写入已有镜头", generator_text)
        self.assertIn("不豁免连续无台词铺垫", generator_text)
        self.assertIn("停顿不是合法 craft 例外", reviewer_text)
        self.assertIn("不能因为身份揭穿、重大证据落地或关系崩塌就自动放行", reviewer_text)
        self.assertNotIn("有动机戏剧停顿（极窄例外，默认不用）", generator_text)
        self.assertNotIn("1.5-2.5 秒", reviewer_text)

    def test_craft_pass_cannot_suggest_extra_time(self):
        text = CRAFT_PASS_SKILL.read_text(encoding="utf-8")

        self.assertIn("只替换，不加秒", text)
        self.assertIn("不得建议新增时间段、延长组时长", text)
        self.assertIn("不建议新增停顿或延长总时长", text)
        self.assertNotIn("1.5-2.5 秒", text)

    def test_dialogue_prompt_matches_rhythm_economy_contract(self):
        text = DIALOGUE_PROMPT.read_text(encoding="utf-8")

        self.assertIn("先估自然时长", text)
        self.assertIn("10-15 秒只是常规承载区间，不是填满目标", text)
        self.assertIn("低密度组必须压缩或合并", text)
        self.assertIn("12-15 秒长组准入", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("连续流程动作合并", text)
        self.assertIn("停顿不是质感例外", text)
        self.assertNotIn("有动机戏剧停顿（极窄例外，默认不用）", text)
        self.assertIn("组尾衔接只写连续性锚点", text)
        self.assertNotIn("默认 10-15 秒", text)
        self.assertNotIn("自然收尾", text)

    def test_cg_visual_style_skill_splits_vertical_collect_and_horizontal_inline_tail(self):
        text = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")

        self.assertIn("竖屏：收集阶段统一追加 3D CG 固定尾部", text)
        self.assertIn("横屏：`final.txt` 每组必须直接包含 3D CG 版", text)
        self.assertIn("不得沿用真人实拍尾部", text)

    def test_horizontal_3d_cg_base_negative_does_not_ban_target_medium(self):
        text = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        start = text.index("3D CG run 基础负面词：")
        end = text.index("3D CG run 不要把", start)
        base_negative_block = text[start:end]

        for forbidden in ("3D渲染", "CG感", "动画感", "卡通", "动漫", "二次元"):
            self.assertNotIn(forbidden, base_negative_block)

    def test_horizontal_3d_cg_generator_requires_motivated_camera_motion(self):
        text = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("3D CG 横屏运镜强化", text)
        self.assertIn("每组至少安排 1 个有明确路径或落点的可见运镜", text)
        self.assertIn("横向跟拍、前景掠过、半环绕、贴地推进、低角度推近、焦点转移、急停落点", text)
        self.assertIn("不能只写固定机位或稳定中景到底", text)

    def test_horizontal_reviewer_flags_static_3d_cg_camera_motion(self):
        text = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("3D CG 横屏组缺少可见运镜", text)
        self.assertIn("整组只用固定机位、稳定中景或静态构图", text)
        self.assertIn("没有横向跟拍、前景掠过、半环绕、贴地推进、低角度推近、焦点转移或急停落点", text)

    def test_3d_cg_visual_peak_effects_must_enter_storyboard_body(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        for text in (generator, visual_style):
            self.assertIn("视觉峰值", text)
            self.assertIn("不只来自打斗", text)
            self.assertIn("当前剧本", text)
            self.assertIn("强节拍", text)
            self.assertIn("镜头描述", text)
            self.assertIn("光影设计", text)
            self.assertIn("不能只靠固定", text)
            self.assertIn("不是固定触发词表", text)
            self.assertIn("来源", text)
            self.assertIn("路径", text)
            self.assertIn("反馈", text)
            self.assertIn("收束", text)

        self.assertIn("visual_peak", reviewer)
        self.assertIn("visual_peak_too_weak", reviewer)
        self.assertIn("不能只在固定 `画面风格` 尾部出现特效词", reviewer)
        self.assertIn("只靠固定 `画面风格` 尾部", reviewer)
        self.assertIn("special_effects", reviewer)

    def test_core_effect_validator_does_not_classify_genre_keywords(self):
        text = WORKSPACE_SCRIPT.read_text(encoding="utf-8")

        self.assertIn("effect_required", text)
        self.assertIn("validate_effect_placement", text)
        self.assertNotIn("HORIZONTAL_XIANXIA_TOPIC_MARKERS", text)
        self.assertNotIn("HORIZONTAL_SPECIAL_EFFECTS_HARD_STRONG_BEAT_TERMS", text)
        self.assertNotIn("玄铁", text)
        self.assertNotIn("真气", text)

    def test_workspace_runtime_uses_auto_visual_peak_effect_validation(self):
        text = WORKSPACE_SCRIPT.read_text(encoding="utf-8")

        self.assertIn('effect_required="auto"', text)
        self.assertIn("_effect_required_from_visual_peak", text)
        self.assertIn("hero", text)
        self.assertIn("beat", text)
        self.assertNotIn('horizontal_special_effect_issues = validate_effect_placement(\n            content,\n            visual_style=episode_visual_style(episode_dir),\n            effect_required="none"', text)

    def test_3d_cg_base_negative_line_keeps_visual_peak_negatives_conditional(self):
        script = WORKSPACE_SCRIPT.read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        start = generator.index("3D CG run 基础负面词：")
        end = generator.index("3D CG run 不要把", start)
        base_negative_block = generator[start:end]

        for forbidden in (
            "满屏粒子",
            "过曝光效",
            "遮脸光效",
            "特效盖住主体",
            "游戏技能UI",
            "法阵文字",
            "魔法阵",
            "廉价仙侠宣传片感",
        ):
            self.assertNotIn(forbidden, script.split('"negative_line": "', 2)[-1].split('",', 1)[0])
            self.assertNotIn(forbidden, base_negative_block)

        self.assertIn("视觉峰值特效条件负面", generator)
        self.assertIn("无来源满屏粒子", generator)
        self.assertIn("过曝吞没人物面部", generator)
        self.assertIn("条件负面", visual_style)

    def test_common_3d_cg_skill_delegates_xianxia_examples_to_topic_pack(self):
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        topic_packs = HORIZONTAL_TOPIC_PACKS.read_text(encoding="utf-8")

        self.assertNotIn("陆地出场 / 压迫特效", visual_style)
        self.assertIn("落地出场 / 压场特效", topic_packs)
        self.assertIn("## 仙侠 / 玄幻 / 古武 / 强者归来", topic_packs)
        self.assertIn("压迫建立 -> 触发 -> 主视觉爆点 -> 结果确认", topic_packs)
        self.assertIn("无来源大光球", topic_packs)
        self.assertIn("法阵文字", topic_packs)

    def test_horizontal_3d_cg_fixed_style_tail_stays_generic(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        script = WORKSPACE_SCRIPT.read_text(encoding="utf-8")
        start = generator.index("**画面风格**：按当前 run 的视觉风格填写。")
        end = generator.index("**运镜强化词**", start)
        style_contract = generator[start:end]

        self.assertIn("按本组 `视觉峰值/特效重点` 使用剧情服务型动漫 CG 特效", style_contract)
        self.assertIn("特效必须绑定动作、道具、身份、权力、环境、心理或信息落点", style_contract)
        self.assertIn("按本组视觉峰值/特效重点使用剧情服务型动漫 CG 特效", script)
        for forbidden in ("动作服务型大片特效", "冷冽刀光", "气流压迫", "碎石悬浮", "贴地冲击尘浪", "金属裂纹冷光"):
            self.assertNotIn(forbidden, style_contract)
        self.assertIn("**视觉峰值/特效重点**", generator)

    def test_horizontal_3d_cg_hero_requires_explicit_main_visual_contract(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        for text in (generator, reviewer):
            self.assertIn("主视觉镜头", text)
            self.assertIn("峰值类型", text)
            self.assertIn("主视觉事件", text)
            self.assertIn("结果反馈", text)
            self.assertIn("没有主视觉镜头", text)
            self.assertIn("降为 `beat`", text)

        self.assertIn("visual_peak_hero_missing_field", WORKSPACE_SCRIPT.read_text(encoding="utf-8"))
        self.assertIn("visual_peak_hero_bad_main_shot", WORKSPACE_SCRIPT.read_text(encoding="utf-8"))

    def test_horizontal_generator_hero_required_fields_match_reviewer(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("`hero` 必须写出主视觉镜头、峰值类型、主视觉事件和结果反馈", generator)
        self.assertIn("`hero` 必须包含 `主视觉镜头`、`峰值类型`、`主视觉事件`、`结果反馈`", reviewer)
        self.assertIn("建议包含 `主视觉承载方式`", reviewer)
        self.assertNotIn("主视觉承载方式`、`主视觉事件` 和 `结果反馈`", generator)
        self.assertNotIn("必须写清主视觉镜头、峰值类型、主视觉承载方式、主视觉事件和结果反馈", generator)
        self.assertNotIn("四行结构", generator)

    def test_horizontal_main_scene_blocks_recurring_subzones_and_named_background_speakers(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("主场景空间地图", generator)
        self.assertIn("同一主场景内反复出现的子区域必须统一命名", generator)
        self.assertIn("后续组必须复用同一个子区域名称", generator)
        self.assertIn("命名食客、命名群演或后续会发声的背景人物", generator)
        self.assertIn("首次个体化时必须写进 `**人物**`", generator)
        self.assertIn("入口/出口、固定交互点或高位、主要行动路线、固定停留点", generator)
        self.assertIn("不要只写“食客群体/群众/同事/路人”", generator)
        self.assertIn("从上一组尾部位置到本组开头位置必须有可见路线", generator)

        self.assertIn("同一物理主场景内的子区域命名漂移", reviewer)
        self.assertIn("命名食客、命名群演或后续会发声的背景人物没有在首次个体化时进入 `人物`", reviewer)
        self.assertIn("组间承接跳过位移路线", reviewer)

    def test_visual_peak_rules_control_weak_effect_language(self):
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        for text in (visual_style, reviewer):
            self.assertIn("极弱", text)
            self.assertIn("很小", text)
            self.assertIn("一闪即灭", text)
            self.assertIn("低范围", text)

        self.assertIn("不要反复用", visual_style)
        self.assertIn("visual_peak_too_weak", reviewer)
        self.assertIn("只有微光、细纹、一闪、极弱、很小或低范围", reviewer)

    def test_hero_visual_peak_requires_layered_feedback(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")

        for text in (generator, reviewer, visual_style):
            self.assertIn("hero 不是“有一个特效点”", text)
            self.assertIn("至少 3 层可见反馈", text)
            self.assertIn("主视觉形态", text)
            self.assertIn("人物/道具受力", text)
            self.assertIn("环境反馈", text)
            self.assertIn("运镜配合", text)
            self.assertIn("结果收束", text)

        self.assertIn("缺少 3 层反馈", reviewer)
        self.assertIn("visual_peak_too_weak", reviewer)

    def test_3d_cg_hero_vfx_rules_are_video_model_friendly(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        workspace = WORKSPACE_SCRIPT.read_text(encoding="utf-8")

        for text in (generator, visual_style):
            self.assertIn("主视觉承载方式", text)
            self.assertIn("隔空能量间隙", text)
            self.assertIn("外层护体壳", text)
            self.assertIn("压缩冲击面", text)
            self.assertIn("避免普通能量球和白烟化", text)
            self.assertIn("受力方向", text)
            self.assertIn("附着对象", text)
            self.assertIn("光影设计模板", text)
            self.assertIn("主光源", text)
            self.assertIn("特效光材质", text)
            self.assertIn("作用范围", text)
            self.assertIn("不要通过“极弱、很小、一闪即灭”", text)

        for issue_code in ("visual_peak_too_small", "contact_staging_risk", "generic_vfx_form"):
            self.assertIn(issue_code, reviewer)
            self.assertIn(issue_code, workspace)

        self.assertIn("真实肢体贴合", reviewer)
        self.assertIn("普通圆形能量球、白烟团、电纹贴图", reviewer)

    def test_3d_cg_hero_vfx_requires_impact_curve_and_scale(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        workspace = WORKSPACE_SCRIPT.read_text(encoding="utf-8")

        for text in (generator, visual_style):
            self.assertIn("爆发帧", text)
            self.assertIn("扩散路径", text)
            self.assertIn("场景级反馈", text)
            self.assertIn("余波收束", text)
            self.assertIn("强烈但有来源", text)
            self.assertIn("高规格国漫番剧级战斗特效", text)
            self.assertIn("慢动作冲击帧", text)
            self.assertIn("体积光余波", text)
            self.assertIn("屏幕边缘轻微震颤", text)
            self.assertIn("触发镜头", text)
            self.assertIn("冲击镜头", text)
            self.assertIn("余波展示镜头", text)

        for issue_code in ("hero_no_impact_curve", "vfx_scale_too_local", "negative_prompt_over_suppresses_vfx"):
            self.assertIn(issue_code, reviewer)
            self.assertIn(issue_code, workspace)

    def test_3d_cg_negative_prompts_do_not_suppress_strong_vfx(self):
        generator = HORIZONTAL_GENERATOR_SKILL.read_text(encoding="utf-8")
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        for text in (generator, visual_style, reviewer):
            self.assertIn("不要把“强光效、大片特效、强能量、粒子、光效”作为负面词", text)
            self.assertIn("只禁错误形态，不禁强度本身", text)
            self.assertIn("无来源满屏粒子", text)
            self.assertIn("过曝吞没人物面部", text)
            self.assertIn("遮挡口型的强光", text)

    def test_3d_cg_rules_do_not_leak_project_character_names(self):
        files = (
            HORIZONTAL_GENERATOR_SKILL,
            CG_VISUAL_STYLE_SKILL,
        )

        for path in files:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("冰清寒", text)
            self.assertNotIn("赵天宇", text)
            self.assertNotIn("太乙神芝", text)

    def test_3d_cg_visual_style_keeps_horizontal_and_vertical_contracts_separate(self):
        visual_style = CG_VISUAL_STYLE_SKILL.read_text(encoding="utf-8")

        self.assertIn("竖屏 run：保留竖屏主合同中的 `组首空间锁定`", visual_style)
        self.assertIn("横屏 run：不使用旧竖屏字段 `组首空间锁定`", visual_style)
        self.assertIn("`**组间承接**` 或 `**横屏构图/调度**`", visual_style)

    def test_horizontal_reviewer_special_effects_severity_is_explicit(self):
        reviewer = (ROOT / "agent_skills" / "storyboard-horizontal-reviewer" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("### visual_peak / special_effects 审核", reviewer)
        self.assertIn("Hard issue：当前剧本已判定需要强特效的动作", reviewer)
        self.assertIn("visual_peak_too_weak", reviewer)
        self.assertIn("Warning：身份揭示、竞价压制、强者压场", reviewer)


if __name__ == "__main__":
    unittest.main()
