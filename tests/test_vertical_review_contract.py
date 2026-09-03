import argparse
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

PREVIOUS_CONTENT = "上一集实际末组：乙在停车场画面右侧，右手持有钥匙，车门关闭。\n"


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


def valid_v3_payload(content=CONTENT, *, require_cross_episode_boundary=False):
    payload = valid_payload()
    for key in ("dialogue_checks", "handoff_checks", "camera_motion_checks"):
        payload.pop(key)
    payload["audit_coverage"] = {
        key: "checked"
        for key in saw._required_audit_coverage_keys(
            "seedance-2-5-live-vertical-reviewer",
            3,
        )
    }
    # Without a boundary input there is no predecessor state to compare against, so v3
    # requires this key to say so instead of claiming a check it could not perform.
    if not require_cross_episode_boundary:
        payload["audit_coverage"][saw.CROSS_EPISODE_COVERAGE_KEY] = "not_applicable"
    payload["mechanical_evidence"] = saw.build_vertical_review_facts(
        content,
        review_contract_version=3,
        require_cross_episode_boundary=require_cross_episode_boundary,
        previous_episode_id="ep00" if require_cross_episode_boundary else None,
        previous_final_content=PREVIOUS_CONTENT if require_cross_episode_boundary else None,
    )["mechanical_evidence"]
    payload["semantic_coverage"] = saw.build_vertical_semantic_coverage(
        content,
        require_cross_episode_boundary=require_cross_episode_boundary,
    )
    if require_cross_episode_boundary:
        payload["semantic_checks"].append(
            {
                "group": "第1组",
                "type": "cross_episode_continuity",
                "result": "pass",
                "evidence": "已对照上一集实际末组的人物、钥匙、车门和日光状态。",
                "fix_instruction": "失败时按上一集实际末态局部修正第1组首帧。",
            }
        )
    return payload


def valid_v4_payload(content=CONTENT, *, require_cross_episode_boundary=False):
    payload = valid_payload()
    for key in ("dialogue_checks", "handoff_checks", "camera_motion_checks"):
        payload.pop(key)
    payload["audit_coverage"] = {
        key: "checked"
        for key in saw._required_audit_coverage_keys(
            "seedance-2-5-live-vertical-reviewer",
            4,
        )
    }
    if not require_cross_episode_boundary:
        payload["audit_coverage"][saw.CROSS_EPISODE_COVERAGE_KEY] = "not_applicable"
    payload["mechanical_evidence"] = saw.build_vertical_review_facts(
        content,
        review_contract_version=4,
        require_cross_episode_boundary=require_cross_episode_boundary,
        previous_episode_id="ep00" if require_cross_episode_boundary else None,
        previous_final_content=PREVIOUS_CONTENT if require_cross_episode_boundary else None,
    )["mechanical_evidence"]
    payload["group_reviews"] = [
        {
            "group": "第1组",
            "result": "pass",
            "evidence": "甲对乙现场说出原台词，钥匙从甲右手可见地交到乙右手，跟拍不遮挡交接。",
        },
        {
            "group": "第2组",
            "result": "pass",
            "evidence": "乙延续右手持钥匙并打开车门，人物、道具和日间光线承接自然。",
        },
    ]
    if require_cross_episode_boundary:
        payload["semantic_checks"].append(
            {
                "group": "第1组",
                "type": "cross_episode_continuity",
                "result": "pass",
                "evidence": "已对照上一集实际末组的人物、钥匙、车门和日光状态。",
                "fix_instruction": "失败时按上一集实际末态局部修正第1组首帧。",
            }
        )
    return payload


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

    def test_camera_motion_detection_accepts_plain_directional_push_and_pan(self):
        for phrase in ("镜头向右摇到乙身上", "镜头从甲推到乙身上"):
            with self.subTest(phrase=phrase):
                content = CONTENT.replace(
                    "摄影机从甲的左后侧跟拍到两人之间",
                    phrase,
                    1,
                )
                self.assertEqual(saw._vertical_camera_motion_shot_labels(content), ["第1组 0-2秒"])

    def test_camera_motion_detection_does_not_treat_character_push_as_camera_motion(self):
        content = CONTENT.replace(
            "摄影机从甲的左后侧跟拍到两人之间",
            "镜头向右是关闭的车门，甲推开车门",
            1,
        )

        self.assertEqual(saw._vertical_camera_motion_shot_labels(content), [])

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

    def test_v3_compact_evidence_matches_without_legacy_arrays(self):
        payload = valid_v3_payload()

        self.assertNotIn("dialogue_checks", payload)
        self.assertEqual(
            saw.validate_vertical_review_evidence(
                payload,
                CONTENT,
                "review.txt",
                review_contract_version=3,
            ),
            [],
        )

    def test_v3_json_schema_requires_compact_mechanical_evidence(self):
        payload = valid_v3_payload()
        payload.pop("mechanical_evidence")
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
            )

        self.assertIn("mechanical_evidence", error)

    def test_v3_json_schema_requires_compact_semantic_coverage(self):
        payload = valid_v3_payload()
        payload.pop("semantic_coverage")
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
            )

        self.assertIn("semantic_coverage", error)

    def test_v4_uses_model_authored_group_reviews_without_script_semantic_coverage(self):
        payload = valid_v4_payload()

        self.assertNotIn("semantic_coverage", payload)
        self.assertEqual(
            set(payload["mechanical_evidence"]),
            {"final_sha256", "group_count"},
        )
        self.assertEqual(
            saw.validate_vertical_review_evidence(
                payload,
                CONTENT,
                "review.txt",
                review_contract_version=4,
            ),
            [],
        )

    def test_v4_json_schema_requires_model_authored_group_reviews(self):
        payload = valid_v4_payload()
        payload.pop("group_reviews")
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=4,
            )

        self.assertIn("group_reviews", error)

    def test_v4_rejects_script_generated_semantic_coverage(self):
        payload = valid_v4_payload()
        payload["semantic_coverage"] = saw.build_vertical_semantic_coverage(CONTENT)
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=4,
            )

        self.assertIn("must not use script-generated", error)

    def test_v4_group_reviews_must_cover_every_actual_group(self):
        payload = valid_v4_payload()
        payload["group_reviews"] = payload["group_reviews"][:1]

        issues = saw.validate_vertical_review_evidence(
            payload,
            CONTENT,
            "review.txt",
            review_contract_version=4,
        )

        self.assertTrue(any("group_reviews missing groups" in issue for issue in issues))

    def test_v4_failed_review_must_mark_an_issue_in_model_authored_group_reviews(self):
        payload = valid_v4_payload()
        payload["pass"] = False
        payload["issues"] = [
            {
                "severity": "hard",
                "group": "第2组",
                "rule": "prop_continuity",
                "problem": "钥匙跳手。",
                "evidence": "第1组组尾在乙手中，第2组首帧写在甲手中。",
                "fix": "修正第2组首帧钥匙归属。",
            }
        ]
        payload["issue_instances_total"] = 1
        payload["affected_groups"] = ["第2组"]
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.txt"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            _result, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=4,
            )

        self.assertIn("group_reviews contains no issue", error)

    def test_v4_review_facts_contain_no_semantic_candidate_counts(self):
        facts = saw.build_vertical_review_facts(CONTENT, review_contract_version=4)

        self.assertEqual(
            set(facts["mechanical_evidence"]),
            {"final_sha256", "group_count"},
        )
        self.assertNotIn("semantic_coverage", facts)

    def test_v3_segment_review_does_not_require_episode_mechanical_evidence(self):
        payload = valid_v3_payload()
        payload.pop("mechanical_evidence")
        payload.pop("semantic_coverage")
        with TemporaryDirectory() as tmp:
            review = Path(tmp) / "review.md"
            review.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            parsed, error = saw._read_review_json(
                review,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
                require_numeric_evidence=False,
            )

        self.assertIsNone(error)
        self.assertIsNotNone(parsed)

    def test_v3_boundary_requires_explicit_semantic_evidence(self):
        payload = valid_v3_payload(require_cross_episode_boundary=True)
        payload["semantic_checks"] = [
            item
            for item in payload["semantic_checks"]
            if item["type"] != "cross_episode_continuity"
        ]

        issues = saw.validate_vertical_review_evidence(
            payload,
            CONTENT,
            "review.txt",
            require_cross_episode_boundary=True,
            review_contract_version=3,
            previous_episode_id="ep00",
            previous_final_content=PREVIOUS_CONTENT,
        )

        self.assertTrue(any("missing cross_episode_continuity" in issue for issue in issues))

    def test_v3_boundary_rejects_wrong_coverage_label_and_semantic_group(self):
        payload = valid_v3_payload(require_cross_episode_boundary=True)
        payload["semantic_coverage"]["handoffs_checked"][0] = "上一集->第2组"
        issues = saw.validate_vertical_review_evidence(
            payload,
            CONTENT,
            "review.txt",
            require_cross_episode_boundary=True,
            review_contract_version=3,
            previous_episode_id="ep00",
            previous_final_content=PREVIOUS_CONTENT,
        )
        self.assertTrue(any("semantic_coverage" in issue for issue in issues))

        payload = valid_v3_payload(require_cross_episode_boundary=True)
        boundary_check = next(
            item for item in payload["semantic_checks"] if item["type"] == "cross_episode_continuity"
        )
        boundary_check["group"] = "第2组"
        issues = saw.validate_vertical_review_evidence(
            payload,
            CONTENT,
            "review.txt",
            require_cross_episode_boundary=True,
            review_contract_version=3,
            previous_episode_id="ep00",
            previous_final_content=PREVIOUS_CONTENT,
        )
        self.assertTrue(any("missing cross_episode_continuity" in issue for issue in issues))

    def test_v2_full_validation_does_not_create_or_require_review_facts(self):
        with TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "episodes" / "ep01"
            episode_dir.mkdir(parents=True)
            saw.write_utf8(episode_dir / "final.txt", CONTENT)
            saw.write_json(episode_dir / "review.txt", valid_payload())
            saw.write_json(
                episode_dir / "status.json",
                {
                    "status": "done",
                    "hard_issues_remaining": [],
                    "reviewer_source": "storyboard-reviewer",
                    "reviewer_pass": True,
                    "reviewer_issues_count": 0,
                    "reviewer_warnings_count": 0,
                },
            )
            saw.write_json(
                episode_dir / "episode.json",
                {
                    "episode_id": "ep01",
                    "reviewer_source": "storyboard-reviewer",
                    "vertical_review_contract_version": 2,
                },
            )

            precheck_result = saw.validate_episode(
                argparse.Namespace(
                    episode_dir=episode_dir,
                    fix_metadata=False,
                    pre_check=True,
                    content_file=None,
                    export_index=False,
                )
            )
            self.assertEqual(precheck_result, 0)
            self.assertFalse((episode_dir / "review_facts.json").exists())

            validate_result = saw.validate_episode(
                argparse.Namespace(
                    episode_dir=episode_dir,
                    fix_metadata=False,
                    pre_check=False,
                    content_file=None,
                    export_index=False,
                )
            )
            self.assertEqual(validate_result, 0)
            self.assertFalse((episode_dir / "review_facts.json").exists())

    def test_v3_multisegment_artifacts_do_not_require_episode_evidence_per_segment(self):
        with TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "episodes" / "ep01"
            episode_dir.mkdir(parents=True)
            saw.write_utf8(episode_dir / "final.txt", CONTENT)
            saw.write_json(episode_dir / "review.txt", valid_v3_payload())
            saw.write_json(
                episode_dir / "review_facts.json",
                saw.build_vertical_review_facts(CONTENT, review_contract_version=3),
            )
            saw.write_json(
                episode_dir / "status.json",
                {
                    "status": "done",
                    "hard_issues_remaining": [],
                    "reviewer_source": "seedance-2-5-live-vertical-reviewer",
                    "reviewer_pass": True,
                    "reviewer_issues_count": 0,
                    "reviewer_warnings_count": 0,
                },
            )
            saw.write_json(
                episode_dir / "episode.json",
                {
                    "episode_id": "ep01",
                    "reviewer_source": "seedance-2-5-live-vertical-reviewer",
                    "vertical_review_contract_version": 3,
                },
            )
            segment_review = valid_v3_payload()
            segment_review.pop("mechanical_evidence")
            segment_review.pop("semantic_coverage")
            for segment_id in ("seg01", "seg02"):
                segment_dir = episode_dir / "segments" / segment_id
                segment_dir.mkdir(parents=True)
                saw.write_utf8(segment_dir / "script.txt", "测试分段")
                saw.write_utf8(segment_dir / "final.txt", CONTENT)
                saw.write_json(segment_dir / "review.md", segment_review)

            self.assertEqual(saw.validate_review_artifacts(episode_dir), [])

    def test_v3_evidence_rejects_stale_final_hash(self):
        payload = valid_v3_payload()
        changed = CONTENT.replace("打开车门", "拉开车门", 1)

        issues = saw.validate_vertical_review_evidence(
            payload,
            changed,
            "review.txt",
            review_contract_version=3,
        )

        self.assertTrue(any("mechanical_evidence" in issue for issue in issues))

    def test_review_facts_file_must_match_current_final(self):
        with TemporaryDirectory() as tmp:
            episode_dir = Path(tmp)
            facts = saw.build_vertical_review_facts(CONTENT, review_contract_version=3)
            saw.write_json(episode_dir / "review_facts.json", facts)

            self.assertEqual(
                saw.validate_vertical_review_facts_file(
                    episode_dir,
                    CONTENT,
                    review_contract_version=3,
                ),
                [],
            )
            self.assertTrue(
                saw.validate_vertical_review_facts_file(
                    episode_dir,
                    CONTENT + "\n",
                    review_contract_version=3,
                )
            )

    def test_boundary_binding_rejects_mismatched_episode_and_out_of_run_path(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            episode_dir = run_dir / "episodes" / "ep01"
            wrong_previous_dir = run_dir / "episodes" / "ep02"
            outside_dir = run_dir / "outside"
            episode_dir.mkdir(parents=True)
            wrong_previous_dir.mkdir(parents=True)
            outside_dir.mkdir(parents=True)
            (wrong_previous_dir / "final.txt").write_text(PREVIOUS_CONTENT, encoding="utf-8")
            (outside_dir / "final.txt").write_text(PREVIOUS_CONTENT, encoding="utf-8")
            saw.write_json(
                episode_dir / "episode.json",
                {"episode_id": "ep01", "depends_on_episode": "ep00"},
            )

            (episode_dir / "boundary_context.md").write_text(
                "previous_final: ../ep02/final.txt\n",
                encoding="utf-8",
            )
            _episode_id, _content, missing_episode_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("missing `previous_episode`" in issue for issue in missing_episode_issues))

            (episode_dir / "boundary_context.md").write_text(
                "previous_episode: ep02\n",
                encoding="utf-8",
            )
            _episode_id, _content, missing_final_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("missing `previous_final`" in issue for issue in missing_final_issues))

            (episode_dir / "boundary_context.md").write_text(
                "previous_episode: ep00\nprevious_final: ../ep02/final.txt\n",
                encoding="utf-8",
            )
            _episode_id, _content, mismatch_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("does not match" in issue for issue in mismatch_issues))

            (episode_dir / "boundary_context.md").write_text(
                "previous_episode: ep02\nprevious_final: ../ep02/final.txt\n",
                encoding="utf-8",
            )
            _episode_id, _content, dependency_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("depends_on_episode" in issue for issue in dependency_issues))

            (episode_dir / "boundary_context.md").write_text(
                "previous_episode: outside\nprevious_final: ../../outside/final.txt\n",
                encoding="utf-8",
            )
            _episode_id, _content, outside_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("must stay inside" in issue for issue in outside_issues))

            (episode_dir / "final.txt").write_text(CONTENT, encoding="utf-8")
            (episode_dir / "boundary_context.md").write_text(
                "previous_episode: ep01\nprevious_final: final.txt\n",
                encoding="utf-8",
            )
            _episode_id, _content, self_issues = saw.load_previous_final_binding(episode_dir)
            self.assertTrue(any("cannot point to the current episode" in issue for issue in self_issues))

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

    def _write_v3_review(self, tmp, coverage_value):
        path = Path(tmp) / "review.txt"
        payload = valid_v3_payload()
        payload["audit_coverage"][saw.CROSS_EPISODE_COVERAGE_KEY] = coverage_value
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return path

    def test_v3_without_boundary_rejects_claimed_cross_episode_check(self):
        # The old gate required "checked" unconditionally, so a standalone episode could
        # only pass by claiming a cross-episode check it had no input for.
        with TemporaryDirectory() as tmp:
            path = self._write_v3_review(tmp, "checked")
            _payload, error = saw._read_review_json(
                path,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
                boundary_present=False,
            )
            self.assertIsNotNone(error)
            self.assertIn("not_applicable", error)

    def test_v3_without_boundary_accepts_not_applicable(self):
        with TemporaryDirectory() as tmp:
            path = self._write_v3_review(tmp, "not_applicable")
            _payload, error = saw._read_review_json(
                path,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
                boundary_present=False,
            )
            self.assertIsNone(error)

    def test_v3_with_boundary_still_requires_checked(self):
        with TemporaryDirectory() as tmp:
            path = self._write_v3_review(tmp, "not_applicable")
            _payload, error = saw._read_review_json(
                path,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=3,
                boundary_present=True,
            )
            self.assertIsNotNone(error)
            self.assertIn("cross_episode_continuity", error)

    def test_v2_without_boundary_keeps_legacy_checked_requirement(self):
        # Already-delivered v2 runs must keep validating exactly as before.
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "review.txt"
            payload = valid_payload()
            payload["audit_coverage"] = {
                key: "checked"
                for key in saw._required_audit_coverage_keys(
                    "seedance-2-5-live-vertical-reviewer",
                    2,
                )
            }
            path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
            _payload, error = saw._read_review_json(
                path,
                reviewer_source="seedance-2-5-live-vertical-reviewer",
                review_contract_version=2,
                boundary_present=False,
            )
            self.assertIsNone(error)

    def _space_lock(self, lock_value, characters="甲、乙"):
        return (
            "=== [cut_id: EP01-G01] 第1组：对峙（总时长：6秒，镜头数：1个） ===\n\n"
            f"**人物**：{characters}\n**场景**：路肩\n**道具**：无\n\n"
            "组首空间锁定（仅作空间连续性约束，不作为独立镜头生成）："
            f"{lock_value}\n\n"
            "0-6秒：\n镜头描述：中景，甲对乙说话。\n光影设计：日间自然光。\n\n"
            "组尾衔接：乙在画面右侧。\n\n=== 第1组结束 ===\n"
        )

    def test_space_lock_rejects_comma_separated_characters(self):
        # `，` is not a clause separator, so both names matched one clause and inherited a
        # single position/orientation pair -- the per-character checks passed vacuously.
        content = self._space_lock("甲位于画面左侧，侧对镜头，乙位于画面右侧，侧对镜头")

        issues = saw.validate_vertical_space_lock_contract(content)

        self.assertTrue(issues)
        self.assertIn("合在同一分句", issues[0])

    def test_space_lock_allows_protective_reference_to_another_character(self):
        # The carrier clause names 乙; 乙 still has its own subject clause and must be judged
        # on that one, not on the first clause its name happens to appear in.
        content = self._space_lock(
            "甲位于画面中央，侧对镜头，左手护着乙退到身后；乙位于画面左后方，侧对镜头"
        )

        self.assertEqual(saw.validate_vertical_space_lock_contract(content), [])

    def test_space_lock_exempts_character_carried_by_another(self):
        content = self._space_lock(
            "甲位于画面中央，侧对镜头，背着乙；乙伏在他背上，侧对镜头，脸朝画右"
        )

        self.assertEqual(saw.validate_vertical_space_lock_contract(content), [])

    def test_space_lock_still_requires_position_when_leaning_on_scenery(self):
        content = self._space_lock("甲位于画面中央，侧对镜头；乙靠在墙上，侧对镜头")

        issues = saw.validate_vertical_space_lock_contract(content)

        self.assertTrue(issues)
        self.assertIn("缺少画面位置", issues[0])

    def test_space_lock_carried_character_still_needs_orientation(self):
        content = self._space_lock("甲位于画面中央，侧对镜头，背着乙；乙伏在他背上，脸朝画右")

        issues = saw.validate_vertical_space_lock_contract(content)

        self.assertTrue(issues)
        self.assertIn("缺少相对镜头朝向", issues[0])

    def test_space_lock_position_error_lists_accepted_vocabulary(self):
        # The accepted position words appear nowhere else, so this message is the only place
        # a worker can learn them in one pass.
        content = self._space_lock("甲位于左侧，侧对镜头；乙位于右侧，侧对镜头")

        issues = saw.validate_vertical_space_lock_contract(content)

        self.assertTrue(issues)
        self.assertIn("画面左", issues[0])
        self.assertIn("画幅中央", issues[0])


if __name__ == "__main__":
    unittest.main()
