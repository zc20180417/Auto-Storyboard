import unittest

import storyboard_agent_workspace as saw


STATIC_HORIZONTAL_GROUP = """=== [cut_id: EP01-G01] 第1组：祠堂对峙（总时长：12秒，镜头数：3个） ===

**人物**：林远、周桂兰
**场景**：林家祠堂
**道具/关键视觉资产**：族谱、木桌
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


if __name__ == "__main__":
    unittest.main()
