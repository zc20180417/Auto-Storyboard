import unittest

import storyboard_agent_workspace as saw


STATIC_HORIZONTAL_GROUP = """=== [cut_id: EP01-G01] 第1组：祠堂对峙（总时长：12秒，镜头数：3个） ===

**人物**：林远、周桂兰
**场景**：林家祠堂
**道具/关键视觉资产**：族谱、木桌
**视觉峰值/特效重点**：无，本组以对白/过渡/稳定表演为主。
**组间承接**：开场无上一组，林远站在画面左侧，周桂兰站在右侧，族谱压在前景木桌中央。
**横屏构图/调度**：16:9 画面左侧是林远，右侧是周桂兰，前景木桌隔开两人，族谱位于画面中央。

1-1
**镜头描述**：固定中景，林远看向周桂兰，手按住族谱说道：“这不是你的东西。”
**光影设计**：祠堂天窗冷光落在族谱上。
**本镜估算时长**：4秒

1-2
**镜头描述**：稳定过肩，周桂兰低头看族谱，抬眼回望林远说道：“你凭什么？”
**光影设计**：背景烛火保持稳定。
**本镜估算时长**：4秒

1-3
**镜头描述**：固定双人中景，两人隔桌对峙，族谱保持在前景中央。
**光影设计**：冷光和烛光分隔两侧人物。
**本镜估算时长**：4秒

**组尾衔接**：该组以两人隔桌对峙、族谱仍压在木桌中央的状态收尾。
**画面风格**：横屏16:9构图，高质量动漫3D CG短剧风格，二次元角色设计，风格化面部与眼睛，清晰轮廓线，高质量卡通渲染，PBR材质与手绘质感融合，细腻表情绑定，电影级布光，景深自然，无字幕。
**运镜强化词**：固定中景承载台词，保持轴线稳定。
**Seedance执行提示补充**：口型同步清楚，族谱位置稳定。
**--neg** 模糊，低分辨率，低多边形，廉价游戏建模，穿模，骨骼错位，水印，logo，字幕

=== 第1组结束 ===
"""


MOTIVATED_HORIZONTAL_GROUP = STATIC_HORIZONTAL_GROUP.replace(
    "固定中景，林远看向周桂兰",
    "低角度沿木桌边缘轻推近，林远看向周桂兰",
).replace(
    "**运镜强化词**：固定中景承载台词，保持轴线稳定。",
    "**运镜强化词**：先沿前景族谱低角度推近林远手掌，再以稳定过肩承载对白，最后焦点转移落回族谱。",
)


STRONG_EFFECT_ONLY_IN_TAIL_GROUP = """=== [cut_id: EP01-G01] 第1组：决定性动作（总时长：6秒，镜头数：1个） ===

**人物**：角色A、角色B
**场景**：大厅
**道具/关键视觉资产**：关键道具
**视觉峰值/特效重点**：hero：角色A的决定性动作造成关键道具边缘冷光、角色B后退和众人态度突变。
**组间承接**：角色A站在左侧，角色B站在右侧，关键道具位于两人之间。
**横屏构图/调度**：16:9 横屏构图，角色A在左，角色B在右，关键道具压住画面中线。

1-1
**镜头描述**：角色A做出决定性动作，角色B被迫后退，众人态度突变。
**光影设计**：室内烛光稳定，人物面部清楚。
**本镜估算时长**：6秒

**组尾衔接**：角色B后退半步，关键道具仍在画面中央。
**画面风格**：横屏16:9构图，高质量动漫3D CG短剧风格，动作服务型大片特效，冷冽刀光，气流压迫。
**运镜强化词**：低角度推近关键道具落点。
**Seedance执行提示补充**：动作和后退关系清楚。
**--neg** 模糊，水印，logo，字幕

=== 第1组结束 ===
"""


STRONG_EFFECT_IN_BODY_GROUP = STRONG_EFFECT_ONLY_IN_TAIL_GROUP.replace(
    "**镜头描述**：角色A做出决定性动作，角色B被迫后退，众人态度突变。",
    "**镜头描述**：角色A做出决定性动作，关键道具边缘短促冷光沿桌面掠过，角色B被气流震得后退，众人态度突变。",
).replace(
    "**光影设计**：室内烛光稳定，人物面部清楚。",
    "**光影设计**：冷光只贴住关键道具边缘，角色A和角色B面部清楚，口型不被遮挡。",
)


STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP = STRONG_EFFECT_IN_BODY_GROUP.replace(
    "**视觉峰值/特效重点**：hero：角色A的决定性动作造成关键道具边缘冷光、角色B后退和众人态度突变。",
    "\n".join(
        [
            "**视觉峰值/特效重点**：hero：角色A的决定性动作造成关键道具边缘冷光、角色B后退和众人态度突变。",
            "- 主视觉镜头：1-1",
            "- 峰值类型：道具显影 / 权力压场",
            "- 主视觉事件：关键道具边缘冷光沿桌面掠过，角色B被气流震得后退。",
            "- 结果反馈：众人态度突变，关键道具保持在画面中心。",
        ]
    ),
)


HERO_WITH_WRONG_MAIN_SHOT_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "- 主视觉镜头：1-1",
    "- 主视觉镜头：2-1",
)


WEAK_HERO_SMALL_VFX_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**镜头描述**：角色A做出决定性动作，关键道具边缘短促冷光沿桌面掠过，角色B被气流震得后退，众人态度突变。",
    "**镜头描述**：角色A做出决定性动作，掌前只有短促冷光一闪即灭，微弱气流低范围散开，角色B轻微后退。",
).replace(
    "**光影设计**：冷光只贴住关键道具边缘，角色A和角色B面部清楚，口型不被遮挡。",
    "**光影设计**：细小冷光短亮后收束成细线，人物面部清楚。",
).replace(
    "- 主视觉事件：关键道具边缘冷光沿桌面掠过，角色B被气流震得后退。",
    "- 主视觉事件：掌前短促冷光一闪即灭，微弱气流低范围散开。",
)


CONTACT_RISK_HERO_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**镜头描述**：角色A做出决定性动作，关键道具边缘短促冷光沿桌面掠过，角色B被气流震得后退，众人态度突变。",
    "**镜头描述**：角色A掌心贴上角色B腕骨，冷光沿腕骨扩开，角色B被迫停住。",
).replace(
    "- 主视觉事件：关键道具边缘冷光沿桌面掠过，角色B被气流震得后退。",
    "- 主视觉事件：角色A掌心贴上角色B腕骨，冷光沿腕骨扩开。",
)


CONTACT_SAFE_HERO_GROUP = CONTACT_RISK_HERO_GROUP.replace(
    "角色A掌心贴上角色B腕骨，冷光沿腕骨扩开，角色B被迫停住。",
    "角色A左掌停在角色B拳腕前方半寸，掌心与拳腕之间形成冷白压缩冲击面，角色B拳臂外层护体壳被顶出凹陷，尘粒从两人之间低位外推，角色B被迫停住。",
).replace(
    "角色A掌心贴上角色B腕骨，冷光沿腕骨扩开。",
    "角色A左掌停在角色B拳腕前方半寸，掌心与拳腕之间形成冷白压缩冲击面，角色B拳臂外层护体壳被顶出凹陷。",
)


GENERIC_VFX_FORM_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**镜头描述**：角色A做出决定性动作，关键道具边缘短促冷光沿桌面掠过，角色B被气流震得后退，众人态度突变。",
    "**镜头描述**：角色A抬手，冷白光球在掌前爆开，周围白烟和电纹扩散，角色B被迫后退。",
).replace(
    "- 主视觉事件：关键道具边缘冷光沿桌面掠过，角色B被气流震得后退。",
    "- 主视觉事件：冷白光球在掌前爆开，周围白烟和电纹扩散。",
)


HERO_WITH_IMPACT_CURVE_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**镜头描述**：角色A做出决定性动作，关键道具边缘短促冷光沿桌面掠过，角色B被气流震得后退，众人态度突变。",
    (
        "**镜头描述**：角色A抬掌前半拍压低全场火光，爆发帧中关键道具边缘形成压缩光核，"
        "冷白裂光沿桌面扩散路径向右扫开，桌面尘粒和火盆主光被压暗半秒，屏幕边缘轻微震颤，"
        "体积光余波收束到角色B后退和众人沉默。"
    ),
).replace(
    "**光影设计**：冷光只贴住关键道具边缘，角色A和角色B面部清楚，口型不被遮挡。",
    (
        "**光影设计**：高规格国漫番剧级战斗特效，主光由火盆暖光转为压缩光核短促主导；"
        "慢动作冲击帧里裂光只沿道具边缘和桌面展开，体积光余波压暗全场主光半秒，不遮挡人物脸和口型。"
    ),
).replace(
    "- 主视觉事件：关键道具边缘冷光沿桌面掠过，角色B被气流震得后退。",
    (
        "- 主视觉事件：爆发帧中关键道具边缘形成压缩光核，裂光沿桌面扩散路径向右扫开，"
        "触发镜头、冲击镜头和余波展示镜头形成连续爆点曲线。"
    ),
).replace(
    "- 结果反馈：众人态度突变，关键道具保持在画面中心。",
    "- 结果反馈：火盆主光被压暗半秒，屏幕边缘轻微震颤后余波收束，角色B后退，众人沉默。",
)


BROAD_NEGATIVE_PROMPT_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**--neg** 模糊，水印，logo，字幕",
    "**--neg** 模糊，水印，logo，字幕，强光效，大片特效，强能量，粒子，光效，满屏粒子，过曝光效，遮脸光效，特效盖住主体，魔法阵，廉价仙侠宣传片感",
)


PRECISE_NEGATIVE_PROMPT_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**--neg** 模糊，水印，logo，字幕",
    "**--neg** 模糊，水印，logo，字幕，无来源满屏粒子，过曝吞没人物面部，遮挡口型的强光，特效盖住主体动作路径，魔法阵贴图，廉价页游特效",
)


OVERDONE_EFFECT_GROUP = """=== [cut_id: EP01-G02] 第2组：过度光效（总时长：5秒，镜头数：1个） ===

**人物**：角色A、角色B
**场景**：大厅
**道具/关键视觉资产**：关键道具
**视觉峰值/特效重点**：hero：抬手动作造成过度光效失控，用于测试 validator 禁止光污染。
**组间承接**：角色A站在画面左侧，角色B退到右侧墙边。
**横屏构图/调度**：16:9 横屏构图，左侧角色A压住画面重心，右侧角色B贴墙。

2-1
**镜头描述**：角色A抬手，满屏粒子和巨大法阵吞没人物。
**光影设计**：过曝光束遮住角色A脸部。
**本镜估算时长**：5秒

**组尾衔接**：角色B被光效压到墙边。
**画面风格**：横屏16:9构图，高质量动漫3D CG短剧风格，二次元角色设计，清晰轮廓线。
**运镜强化词**：低角度推近角色A抬手动作。
**Seedance执行提示补充**：人物主体清楚。
**--neg** 模糊，水印，logo，字幕

=== 第2组结束 ===
"""


NEGATED_OVERDONE_EFFECT_GROUP = STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP.replace(
    "**光影设计**：冷光只贴住关键道具边缘，角色A和角色B面部清楚，口型不被遮挡。",
    "**光影设计**：冷光只贴住关键道具边缘，不形成满屏粒子；角色A和角色B面部清楚，口型不被遮挡。",
).replace(
    "**Seedance执行提示补充**：动作和后退关系清楚。",
    "**Seedance执行提示补充**：动作和后退关系清楚，不要生成法阵、光球、技能UI、满屏粒子或遮脸光效。",
)


class HorizontalCameraMotionContractTests(unittest.TestCase):
    def test_horizontal_3d_cg_rejects_all_static_camera_plan(self):
        issues = saw.validate_horizontal_camera_motion_contract(STATIC_HORIZONTAL_GROUP, visual_style="3d-cg")

        self.assertTrue(any("3D CG 横屏" in issue and "缺少可见运镜" in issue for issue in issues))

    def test_horizontal_live_action_keeps_static_dialogue_group_allowed(self):
        issues = saw.validate_horizontal_camera_motion_contract(STATIC_HORIZONTAL_GROUP, visual_style="live-action")

        self.assertFalse(any("3D CG 横屏" in issue for issue in issues))

    def test_horizontal_3d_cg_accepts_motivated_camera_plan(self):
        issues = saw.validate_horizontal_camera_motion_contract(MOTIVATED_HORIZONTAL_GROUP, visual_style="3d-cg")

        self.assertEqual(issues, [])

    def test_horizontal_output_structure_requires_visual_peak_field(self):
        missing_field_group = STATIC_HORIZONTAL_GROUP.replace(
            "**视觉峰值/特效重点**：无，本组以对白/过渡/稳定表演为主。\n",
            "",
        )

        issues = saw.validate_horizontal_output_structure_contract(missing_field_group)

        self.assertTrue(any("视觉峰值/特效重点" in issue for issue in issues))

    def test_required_strong_effect_cannot_exist_only_in_tail(self):
        issues = saw.validate_effect_placement(
            STRONG_EFFECT_ONLY_IN_TAIL_GROUP,
            visual_style="3d-cg",
            effect_required="strong",
        )

        self.assertTrue(any("effect_only_in_tail" in issue for issue in issues))

    def test_declared_hero_effect_only_in_tail_fails_in_auto_mode(self):
        issues = saw.validate_effect_placement(
            STRONG_EFFECT_ONLY_IN_TAIL_GROUP,
            visual_style="3d-cg",
            effect_required="auto",
        )

        self.assertTrue(any("effect_only_in_tail" in issue and "`hero`" in issue for issue in issues))

    def test_declared_hero_requires_main_visual_shot_fields(self):
        issues = saw.validate_visual_peak_contract(
            STRONG_EFFECT_IN_BODY_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("visual_peak_hero_missing_field" in issue and "主视觉镜头" in issue for issue in issues))

    def test_declared_hero_accepts_main_visual_shot_fields(self):
        issues = saw.validate_visual_peak_contract(
            STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP,
            visual_style="3d-cg",
        )

        self.assertFalse(any("visual_peak_hero" in issue for issue in issues))

    def test_declared_hero_main_visual_shot_must_belong_to_same_group(self):
        issues = saw.validate_visual_peak_contract(
            HERO_WITH_WRONG_MAIN_SHOT_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("visual_peak_hero_bad_main_shot" in issue and "`2-1`" in issue for issue in issues))

    def test_declared_hero_rejects_small_local_vfx(self):
        issues = saw.validate_visual_peak_contract(
            WEAK_HERO_SMALL_VFX_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("visual_peak_too_small" in issue for issue in issues))

    def test_declared_hero_rejects_contact_staging_risk(self):
        issues = saw.validate_visual_peak_contract(
            CONTACT_RISK_HERO_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("contact_staging_risk" in issue for issue in issues))

    def test_declared_hero_accepts_contact_with_energy_gap_and_outer_shell(self):
        issues = saw.validate_visual_peak_contract(
            CONTACT_SAFE_HERO_GROUP,
            visual_style="3d-cg",
        )

        self.assertFalse(any("contact_staging_risk" in issue for issue in issues))

    def test_declared_hero_rejects_generic_energy_ball_form(self):
        issues = saw.validate_visual_peak_contract(
            GENERIC_VFX_FORM_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("generic_vfx_form" in issue for issue in issues))

    def test_declared_hero_rejects_missing_impact_curve(self):
        issues = saw.validate_visual_peak_contract(
            STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("hero_no_impact_curve" in issue for issue in issues))

    def test_declared_hero_accepts_impact_curve_and_scene_scale(self):
        issues = saw.validate_visual_peak_contract(
            HERO_WITH_IMPACT_CURVE_GROUP,
            visual_style="3d-cg",
        )

        self.assertFalse(any("hero_no_impact_curve" in issue or "vfx_scale_too_local" in issue for issue in issues))

    def test_3d_cg_negative_prompt_rejects_over_suppressing_vfx_terms(self):
        issues = saw.validate_horizontal_visual_style_contract(
            BROAD_NEGATIVE_PROMPT_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("negative_prompt_over_suppresses_vfx" in issue for issue in issues))

    def test_3d_cg_negative_prompt_allows_precise_bad_form_terms(self):
        issues = saw.validate_horizontal_visual_style_contract(
            PRECISE_NEGATIVE_PROMPT_GROUP,
            visual_style="3d-cg",
        )

        self.assertFalse(any("negative_prompt_over_suppresses_vfx" in issue for issue in issues))

    def test_fixed_style_tail_cannot_list_concrete_effect_markers(self):
        issues = saw.validate_horizontal_visual_style_contract(
            STRONG_EFFECT_ONLY_IN_TAIL_GROUP,
            visual_style="3d-cg",
        )

        self.assertTrue(any("fixed_style_effect_tail" in issue and "冷冽刀光" in issue for issue in issues))

    def test_effect_not_required_keeps_clean_dialogue_group_allowed(self):
        issues = saw.validate_effect_placement(
            STATIC_HORIZONTAL_GROUP,
            visual_style="3d-cg",
            effect_required="none",
        )

        self.assertFalse(any("effect_only_in_tail" in issue or "effect_missing_body" in issue for issue in issues))

    def test_declared_no_visual_peak_does_not_require_effect_in_auto_mode(self):
        issues = saw.validate_effect_placement(
            STATIC_HORIZONTAL_GROUP,
            visual_style="3d-cg",
            effect_required="auto",
        )

        self.assertFalse(any("effect_only_in_tail" in issue or "effect_missing_body" in issue for issue in issues))

    def test_required_strong_effect_passes_when_body_carries_effect(self):
        issues = saw.validate_effect_placement(
            STRONG_EFFECT_IN_BODY_WITH_HERO_FIELDS_GROUP,
            visual_style="3d-cg",
            effect_required="strong",
        )

        self.assertFalse(any("effect_only_in_tail" in issue or "effect_missing_body" in issue for issue in issues))

    def test_overdone_effect_fails_without_genre_keyword_detection(self):
        issues = saw.validate_effect_placement(
            OVERDONE_EFFECT_GROUP,
            visual_style="3d-cg",
            effect_required="none",
        )

        self.assertTrue(any("effect_overdone" in issue for issue in issues))

    def test_negative_overdone_effect_instruction_does_not_fail(self):
        issues = saw.validate_effect_placement(
            NEGATED_OVERDONE_EFFECT_GROUP,
            visual_style="3d-cg",
            effect_required="strong",
        )

        self.assertFalse(any("effect_overdone" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
