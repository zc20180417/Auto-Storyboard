import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import storyboard_agent_workspace as saw


CONTENT = """=== [cut_id: EP01-G01] 第1组：递钥匙（总时长：6秒，镜头数：2个） ===

**人物**：甲、乙
**场景**：停车场
**道具**：钥匙

组首空间锁定（仅作空间连续性约束，不作为独立镜头生成）：甲位于画面左侧，侧对镜头，脸朝画右；乙位于画面右侧，侧对镜头，脸朝画左。

0-2秒：
镜头描述：中景，摄影机从甲的左后侧跟拍到两人之间，最终停在双手都位于竖屏中央的位置，甲对乙说道：“把钥匙给我。”
光影设计：日间自然光。

2-6秒：
镜头描述：近景，甲拔下钥匙递给乙，乙接住后把钥匙握在右手。
光影设计：日间自然光。

组尾衔接：乙位于画面右侧，右手持有钥匙。

=== 第1组结束 ===

=== [cut_id: EP01-G02] 第2组：开门（总时长：6秒，镜头数：1个） ===

**人物**：乙
**场景**：停车场
**道具**：钥匙、车门

组首空间锁定（仅作空间连续性约束，不作为独立镜头生成）：乙位于画面右侧，侧对镜头，脸朝画左，右手持有钥匙；车门处于关闭状态。

0-6秒：
镜头描述：中景，乙用右手钥匙打开车门。
光影设计：日间自然光。

组尾衔接：乙仍在车外，车门已经打开，钥匙仍在乙右手。

=== 第2组结束 ===
"""


def valid_payload():
    return {
        "pass": True,
        "summary": "已逐镜核对对白、运镜和组间接点。",
        "checked_groups": ["第1组", "第2组"],
        "audit_coverage": {
            key: "checked"
            for key in saw._required_audit_coverage_keys("storyboard-reviewer", 2)
        },
        "spot_checks": [
            {"group": "第1组", "type": "dialogue_pacing", "evidence": "5字对白用2秒。"},
            {"group": "第1组", "type": "camera_motion_reasonableness", "evidence": "跟拍有路径和落点。"},
            {"group": "第2组", "type": "handoff_continuity", "evidence": "钥匙由乙持有。"},
        ],
        "semantic_checks": [
            {"group": "第1组", "type": "dialogue_pacing", "result": "pass", "evidence": "5字/2秒。", "fix_instruction": "若失败则缩短或调整。"},
            {"group": "第1组", "type": "camera_motion_reasonableness", "result": "pass", "evidence": "摄影机跟随甲并落到双手。", "fix_instruction": "若失败则补路径和落点。"},
            {"group": "第2组", "type": "handoff_continuity", "result": "pass", "evidence": "乙在组首继续持钥匙。", "fix_instruction": "若失败则补道具归属。"},
        ],
        "dialogue_checks": [
            {
                "shot": "第1组 0-2秒",
                "chars": 5,
                "seconds": 2.0,
                "chars_per_second": 2.5,
                "mouth_duration": "甲现场开口2秒",
                "speech_type": "ordinary",
                "result": "pass",
                "evidence": "甲对乙说把钥匙给我。",
            }
        ],
        "handoff_checks": [
            {
                "from": "第1组",
                "to": "第2组",
                "characters": "乙保持在画面右侧。",
                "props": "钥匙继续由乙右手持有。",
                "doors_vehicles": "车门从关闭状态开始。",
                "time_light": "均为日间自然光。",
                "result": "pass",
                "evidence": "第1组组尾和第2组组首一致。",
            }
        ],
        "camera_motion_checks": [
            {
                "shot": "第1组 0-2秒",
                "motivation": "跟随甲靠近乙",
                "subject": "甲和双方手部",
                "path": "从甲左后侧到两人之间",
                "endpoint": "双手位于竖屏中央",
                "action_compatibility": "不遮挡口型和钥匙",
                "result": "pass",
            }
        ],
        "issue_instances_total": 0,
        "affected_groups": [],
        "issues": [],
        "warnings": [],
    }


class VerticalReviewContractTests(unittest.TestCase):
    def test_complete_evidence_matches_storyboard(self):
        self.assertEqual(
            saw.validate_vertical_review_evidence(valid_payload(), CONTENT, "review.txt"),
            [],
        )

    def test_missing_camera_motion_evidence_fails(self):
        payload = valid_payload()
        payload["camera_motion_checks"] = []

        issues = saw.validate_vertical_review_evidence(payload, CONTENT, "review.txt")

        self.assertTrue(any("camera_motion_checks missing shots" in issue for issue in issues))

    def test_camera_motion_detection_accepts_camera_path_without_photographer_word(self):
        content = CONTENT.replace(
            "摄影机从甲的左后侧跟拍到两人之间",
            "镜头从甲的左后侧跟随到两人之间",
            1,
        )

        labels = saw._vertical_camera_motion_shot_labels(content)

        self.assertEqual(labels, ["第1组 0-2秒"])

    def test_v2_json_schema_requires_structured_evidence(self):
        payload = valid_payload()
        payload.pop("dialogue_checks")
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="storyboard-reviewer",
                review_contract_version=2,
            )

        self.assertIn("dialogue_checks", error)

    def test_space_lock_rejects_grouped_people_and_object_only_orientation(self):
        bad = CONTENT.replace(
            "甲位于画面左侧，侧对镜头，脸朝画右；乙位于画面右侧，侧对镜头，脸朝画左。",
            "甲和乙位于画面左侧，面向车门。",
            1,
        )

        issues = saw.validate_vertical_space_lock_contract(bad)

        self.assertTrue(any("逐人锁定" in issue for issue in issues))
        self.assertTrue(any("相对镜头朝向" in issue for issue in issues))

    def test_space_lock_allows_relative_relation_inside_independent_clause(self):
        content = CONTENT.replace(
            "乙位于画面右侧，侧对镜头，脸朝画左。",
            "乙位于画面右侧、甲前方半步，侧对镜头，脸朝画左。",
            1,
        )

        self.assertEqual(saw.validate_vertical_space_lock_contract(content), [])


if __name__ == "__main__":
    unittest.main()
