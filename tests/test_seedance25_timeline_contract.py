import unittest
from pathlib import Path

import storyboard_agent_workspace as saw
import seedance_material_handoff as handoff


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "seedance25" / "timeline-only-horizontal-xianxia.txt"


class Seedance25TimelineOnlyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.content = FIXTURE.read_text(encoding="utf-8")

    def test_fixture_passes_profile_structure_without_explicit_camera_plan(self):
        self.assertEqual(
            saw.validate_clean_storyboard_format(
                self.content,
                video_profile=saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
            ),
            [],
        )
        self.assertEqual(
            saw.validate_horizontal_output_structure_contract(self.content, timeline_only=True),
            [],
        )
        self.assertEqual(
            saw.validate_horizontal_camera_motion_contract(
                self.content,
                visual_style="3d-cg",
                timeline_only=True,
            ),
            [],
        )

    def test_timeline_only_camera_validation_does_not_turn_model_autonomy_into_a_quota(self):
        static_content = self.content.replace(
            "灵火沿元鼎外壁下腹的三道铸纹向上贴行",
            "灵火稳定贴在元鼎下方",
        ).replace(
            "灵火从鼎纹上端回收至鼎腹下方火槽",
            "灵火保持在鼎腹下方火槽",
        )
        self.assertEqual(
            saw.validate_horizontal_camera_motion_contract(
                static_content,
                visual_style="3d-cg",
                timeline_only=True,
            ),
            [],
        )

    def test_standalone_camera_field_remains_a_format_error(self):
        with_camera_field = self.content.replace(
            "**组尾衔接**：方平仍在画面左侧",
            "**运镜强化词**：固定中景即可。\n**组尾衔接**：方平仍在画面左侧",
            1,
        )
        issues = saw.validate_horizontal_output_structure_contract(
            with_camera_field,
            timeline_only=True,
        )
        self.assertTrue(any("运镜强化词" in issue for issue in issues), issues)

    def test_effect_and_style_checks_remain_independent_of_camera_words(self):
        self.assertEqual(
            saw.validate_horizontal_visual_style_contract(self.content, visual_style="3d-cg"),
            [],
        )
        self.assertEqual(
            saw.validate_effect_placement(
                self.content,
                visual_style="3d-cg",
                effect_required="auto",
                timeline_only=True,
            ),
            [],
        )

    def test_strict_submission_timeline_is_gap_free_and_keeps_vfx_semantics(self):
        first_group = handoff._extract_group_blocks(self.content)[1]
        prompt = handoff.build_submission_prompt(
            first_group,
            [
                {
                    "reference_token": "@图片1",
                    "material_key": "CHAR_FANGPING_BASE",
                    "asset_type": "character",
                    "source_binding_role": "character_reference",
                    "provides": ["face", "hair"],
                    "excludes": ["action"],
                },
                {
                    "reference_token": "@图片2",
                    "material_key": "SCENE_DANFANG_BASE",
                    "asset_type": "scene",
                    "source_binding_role": "scene_reference",
                    "provides": ["space_layout", "materials"],
                    "excludes": ["action"],
                },
                {
                    "reference_token": "@图片3",
                    "material_key": "PROP_YUANDING_BASE",
                    "asset_type": "prop",
                    "source_binding_role": "prop_reference",
                    "provides": ["appearance", "material", "condition"],
                    "excludes": ["action"],
                },
            ],
            duration=12,
            strict_timeline=True,
        )

        self.assertLess(prompt.index("【人物资产】"), prompt.index("【场景资产】"))
        self.assertLess(prompt.index("【场景资产】"), prompt.index("【道具与关键视觉资产】"))
        self.assertIn("0-3秒（镜头1-1）", prompt)
        self.assertIn("3-7秒（镜头1-2）", prompt)
        self.assertIn("7-12秒（镜头1-3）", prompt)
        self.assertIn("来源是指尖", prompt)
        self.assertIn("沿元鼎外壁下腹的三道铸纹向上贴行", prompt)
        self.assertIn("形态收束为稳定的短火舌", prompt)
        self.assertIn("景别按信息量和主体可读性自主选择", prompt)
        self.assertNotIn("优先中景与中近景", prompt)
        self.assertNotIn("视觉峰值/特效重点", prompt)
        self.assertNotIn("运镜强化词", prompt)
        self.assertNotIn("Seedance执行提示补充", prompt)

    def test_strict_submission_timeline_rejects_mismatched_total(self):
        first_group = handoff._extract_group_blocks(self.content)[1]
        with self.assertRaisesRegex(ValueError, "sum to 12 seconds.*declares 11 seconds"):
            handoff.build_submission_prompt(
                first_group,
                [],
                duration=11,
                strict_timeline=True,
            )


if __name__ == "__main__":
    unittest.main()
