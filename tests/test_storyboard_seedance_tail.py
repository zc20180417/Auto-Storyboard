import unittest

import storyboard_agent_workspace as saw


MINIMAL_GROUP_WITHOUT_TAIL = """=== [cut_id: EP01-G01] 第1组：村口对峙（总时长：10秒，镜头数：1个） ===

**人物**：林远
**场景**：槐树村村口
**道具**：成绩单

组首空间锁定（仅作空间连续性约束，不作为独立镜头生成）：槐树村村口，林远位于画面中央，面向镜头，手中持有成绩单。

0-10秒：
镜头描述：中景，林远抬眼看向前方，手指收紧成绩单，对面前众人说道：“我会回来。”
光影设计：自然日光从斜上方洒落，面部清晰。

组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。

=== 第1组结束 ===
"""


class SeedanceTailTests(unittest.TestCase):
    def test_append_vertical_seedance_tail_adds_default_tail_before_group_end(self):
        result = saw.append_vertical_seedance_tail_to_groups(MINIMAL_GROUP_WITHOUT_TAIL)

        self.assertIn(saw.VERTICAL_SEEDANCE_STYLE_LINE, result)
        self.assertIn(saw.VERTICAL_SEEDANCE_NEGATIVE_LINE, result)
        self.assertLess(result.index(saw.VERTICAL_SEEDANCE_STYLE_LINE), result.index("=== 第1组结束 ==="))
        self.assertLess(result.index(saw.VERTICAL_SEEDANCE_NEGATIVE_LINE), result.index("=== 第1组结束 ==="))

    def test_append_vertical_seedance_tail_does_not_duplicate_existing_tail(self):
        with_tail = MINIMAL_GROUP_WITHOUT_TAIL.replace(
            "=== 第1组结束 ===",
            f"{saw.VERTICAL_SEEDANCE_STYLE_LINE}\n\n{saw.VERTICAL_SEEDANCE_NEGATIVE_LINE}\n\n=== 第1组结束 ===",
        )

        result = saw.append_vertical_seedance_tail_to_groups(with_tail)

        self.assertEqual(result.count(saw.VERTICAL_SEEDANCE_STYLE_LINE), 1)
        self.assertEqual(result.count(saw.VERTICAL_SEEDANCE_NEGATIVE_LINE), 1)

    def test_append_vertical_seedance_tail_merges_video_negative_hints(self):
        with_hint = MINIMAL_GROUP_WITHOUT_TAIL.replace(
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。",
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。\n\n视频禁止项：成绩单消失，人物换位",
        )

        result = saw.append_vertical_seedance_tail_to_groups(with_hint)

        self.assertNotIn("视频禁止项：", result)
        self.assertIn(f"{saw.VERTICAL_SEEDANCE_NEGATIVE_LINE}，成绩单消失，人物换位", result)

    def test_clean_validator_accepts_specific_video_negative_hints(self):
        with_hint = MINIMAL_GROUP_WITHOUT_TAIL.replace(
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。",
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。\n\n视频禁止项：成绩单消失，林远提前离场，周桂兰进入屋内",
        )

        self.assertEqual(saw.validate_clean_storyboard_format(with_hint), [])

    def test_clean_validator_rejects_placeholder_video_negative_hints(self):
        with_hint = MINIMAL_GROUP_WITHOUT_TAIL.replace(
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。",
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。\n\n视频禁止项：本组关键道具消失，人物错误",
        )

        issues = saw.validate_clean_storyboard_format(with_hint)

        self.assertTrue(any("模板占位或泛泛词" in issue for issue in issues))

    def test_clean_validator_rejects_too_many_video_negative_hints(self):
        with_hint = MINIMAL_GROUP_WITHOUT_TAIL.replace(
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。",
            "组尾衔接：该组以林远握紧成绩单的状态自然收尾。不强制静止。\n\n视频禁止项：A消失，B换位，C提前离开，D进入屋内，E抢动作，F场景变形",
        )

        issues = saw.validate_clean_storyboard_format(with_hint)

        self.assertTrue(any("视频禁止项超过" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
