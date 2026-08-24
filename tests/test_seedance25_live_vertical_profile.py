import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import storyboard_agent_workspace as saw


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_SCRIPT = ROOT / "storyboard_agent_workspace.py"


def vertical_group(total: int, ranges: list[tuple[str, str]], *, hint: str | None = None) -> str:
    shots = []
    for start, end in ranges:
        shots.append(
            f"""{start}-{end}秒：
镜头描述：中景，甲位于客厅画面左侧，右手握住钥匙并看向画面右侧的门。
光影设计：日间窗光照亮甲的面部。"""
        )
    hint_line = f"\n\n视频禁止项：{hint}" if hint else ""
    return f"""=== [cut_id: EP01-G01] 第1组：握住钥匙（总时长：{total}秒，镜头数：{len(ranges)}个） ===

**人物**：甲
**场景**：客厅
**道具**：钥匙

组首空间锁定（仅作空间连续性约束，不作为独立镜头生成）：甲位于画面左侧，侧对镜头，脸朝画右，右手持有钥匙。

{chr(10).join(shots)}

组尾衔接：甲仍位于客厅画面左侧，右手持有钥匙。{hint_line}

=== 第1组结束 ===
"""


class Seedance25LiveVerticalProfileTests(unittest.TestCase):
    def test_profile_skills_lock_multimodal_only_scope(self):
        profile_skill = (ROOT / "agent_skills" / "seedance-2-5-live-vertical" / "SKILL.md").read_text(encoding="utf-8")
        model_contract = (
            ROOT / "agent_skills" / "seedance-2-5-live-vertical" / "references" / "model-contract.md"
        ).read_text(encoding="utf-8")
        generator_skill = (
            ROOT / "agent_skills" / "seedance-2-5-live-vertical-generator" / "SKILL.md"
        ).read_text(encoding="utf-8")
        reviewer_skill = (
            ROOT / "agent_skills" / "seedance-2-5-live-vertical-reviewer" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("video_task_type=multimodal_generation", profile_skill)
        self.assertIn("至少 1 项真实", profile_skill)
        self.assertIn("Task in scope: `multimodal_generation` only", model_contract)
        self.assertIn("唯一视频任务是 `multimodal_generation`", generator_skill)
        self.assertIn("multimodal_task_scope", reviewer_skill)

    def test_machine_contract_is_independent_and_official_model_specific(self):
        self.assertEqual(saw.DEFAULT_VIDEO_PROFILE, "seedance-2.0")
        legacy = saw.video_profile_config(saw.DEFAULT_VIDEO_PROFILE)
        profile = saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)

        self.assertEqual(legacy["duration_min_seconds"], 6)
        self.assertEqual(legacy["duration_max_seconds"], 15)
        self.assertEqual(legacy["timeline_granularity_seconds"], 0.5)
        self.assertEqual(legacy["collection_tail_mode"], "legacy")

        self.assertEqual(profile["target_video_model"], "doubao-seedance-2-5-260628")
        self.assertEqual(profile["supported_aspects"], ("vertical",))
        self.assertEqual(profile["supported_visual_styles"], ("live-action",))
        self.assertEqual(profile["duration_min_seconds"], 4)
        self.assertEqual(profile["duration_max_seconds"], 30)
        self.assertEqual(profile["timeline_granularity_seconds"], 1)
        self.assertEqual(profile["aspect_ratio"], "9:16")
        self.assertEqual(profile["supported_resolutions"], ("480p", "720p"))
        self.assertEqual(profile["default_resolution"], "720p")
        self.assertEqual(profile["fps"], 24)
        self.assertIs(profile["generate_audio"], True)
        self.assertEqual(profile["video_task_type"], "multimodal_generation")
        self.assertIs(profile["requires_multimodal_materials"], True)
        self.assertEqual(profile["minimum_material_inputs"], 1)
        self.assertEqual(profile["allowed_multimodal_material_types"], ("image", "video", "audio"))
        self.assertEqual(
            profile["forbidden_video_task_modes"],
            (
                "text_only_generation",
                "reference_generation",
                "first_last_frame_generation",
                "keyframe_generation",
                "video_edit",
                "video_extend",
                "track_completion",
            ),
        )
        self.assertEqual(profile["contract_version"], 2)

    def test_project_entrypoints_keep_seedance20_as_default(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        workflow = (ROOT / "README_AGENT_WORKFLOW.md").read_text(encoding="utf-8")

        self.assertIn("默认竖屏：`agent_skills/storyboard-generator/SKILL.md`", agents)
        self.assertIn("未标记该 profile 时按 aspect", claude)
        self.assertIn("不传 `-VideoProfile` 时仍走原有 `seedance-2.0` 默认流程", readme)
        self.assertIn("不显式选择时，旧 `seedance-2.0` 仍是默认值", workflow)
        self.assertIn('"reviewer_source": "storyboard-reviewer"', workflow)

    def test_profile_rejects_non_vertical_or_non_live_action_selection(self):
        self.assertIsNotNone(
            saw.validate_video_profile_selection(
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                aspect="horizontal",
                visual_style="live-action",
            )
        )
        self.assertIsNotNone(
            saw.validate_video_profile_selection(
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                aspect="vertical",
                visual_style="3d-cg",
            )
        )
        self.assertIsNone(
            saw.validate_video_profile_selection(
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                aspect="vertical",
                visual_style="live-action",
                resolution="480p",
            )
        )

    def test_seedance25_validator_accepts_4_and_30_second_integer_groups(self):
        four_seconds = vertical_group(4, [("0", "4")])
        thirty_seconds = vertical_group(30, [("0", "15"), ("15", "30")])

        self.assertEqual(
            saw.validate_clean_storyboard_format(
                four_seconds,
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
            ),
            [],
        )
        self.assertEqual(
            saw.validate_clean_storyboard_format(
                thirty_seconds,
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
            ),
            [],
        )

    def test_seedance25_validator_rejects_fractional_boundaries_and_out_of_range(self):
        fractional = vertical_group(4, [("0", "2.5"), ("2.5", "4")])
        too_short = vertical_group(3, [("0", "3")])
        too_long = vertical_group(31, [("0", "15"), ("15", "31")])

        fractional_issues = saw.validate_clean_storyboard_format(
            fractional,
            video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
        )
        self.assertTrue(any("整数秒边界" in issue for issue in fractional_issues))
        self.assertTrue(
            any("4-30秒范围" in issue for issue in saw.validate_clean_storyboard_format(
                too_short,
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
            ))
        )
        self.assertTrue(
            any("4-30秒范围" in issue for issue in saw.validate_clean_storyboard_format(
                too_long,
                video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
            ))
        )

    def test_legacy_validator_behavior_remains_default(self):
        legacy_half_second = vertical_group(6, [("0", "2.5"), ("2.5", "6")])
        legacy_too_short = vertical_group(4, [("0", "4")])

        self.assertEqual(saw.validate_clean_storyboard_format(legacy_half_second), [])
        self.assertTrue(
            any(
                "6-15秒范围" in issue
                for issue in saw.validate_clean_storyboard_format(legacy_too_short)
            )
        )

    def test_profile_sensitive_helpers_keep_legacy_default(self):
        self.assertEqual(
            saw.storyboard_workflow_config("horizontal")["reviewer_name"],
            "storyboard-horizontal-reviewer",
        )

    def test_metadata_free_historical_episode_still_falls_back_to_legacy_profile(self):
        with TemporaryDirectory() as tmp:
            self.assertEqual(saw.episode_video_profile(Path(tmp)), saw.DEFAULT_VIDEO_PROFILE)

    def test_seedance25_collection_tail_has_native_audio_and_no_legacy_negative_pack(self):
        content = vertical_group(8, [("0", "4"), ("4", "8")], hint="甲手中的钥匙消失")

        result = saw.append_vertical_seedance_tail_to_groups(
            content,
            video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
        )

        for line in saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)["collection_tail_lines"]:
            self.assertIn(line, result)
        self.assertIn("--neg 甲手中的钥匙消失", result)
        self.assertNotIn("视频禁止项", result)
        self.assertNotIn(saw.VERTICAL_SEEDANCE_NEGATIVE_LINE, result)
        self.assertNotIn("4K画质", result)

    def test_seedance25_master_rejects_legacy_tail_and_precomposed_negative_line(self):
        content = vertical_group(8, [("0", "4"), ("4", "8")])
        polluted = content.replace(
            "=== 第1组结束 ===",
            "画面风格：真人实拍风格，4K画质。\n\n--neg 人物错误，道具错误\n\n=== 第1组结束 ===",
        )

        issues = saw.validate_clean_storyboard_format(
            polluted,
            video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
        )

        self.assertTrue(any("4K画质" in issue for issue in issues))
        self.assertTrue(any("不要直接写 `--neg`" in issue for issue in issues))

    def test_seedance25_rejects_unsupported_task_modes_without_banning_story_reference_word(self):
        representative_terms = {
            "纯文本生成": "text_only_generation",
            "多模态参考生成": "reference_generation",
            "首尾帧生成": "first_last_frame_generation",
            "关键帧生成": "keyframe_generation",
            "视频编辑": "video_edit",
            "视频延长": "video_extend",
            "轨道补全": "track_completion",
        }
        base = vertical_group(4, [("0", "4")])
        for term, task_mode in representative_terms.items():
            with self.subTest(term=term):
                polluted = base.replace("镜头描述：", f"任务：{term}。\n镜头描述：", 1)
                issues = saw.validate_clean_storyboard_format(
                    polluted,
                    video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                )
                self.assertTrue(any(task_mode in issue for issue in issues), issues)

        ordinary_dialogue = base.replace(
            "镜头描述：中景，",
            "镜头描述：中景，甲对乙说：“请参考这份报告。”，",
            1,
        )
        issues = saw.validate_clean_storyboard_format(
            ordinary_dialogue,
            video_profile=saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
        )
        self.assertFalse(any("不支持的任务模式" in issue for issue in issues), issues)

    def test_seedance25_reviewer_uses_vertical_v2_evidence_contract(self):
        reviewer = saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)["reviewer_name"]
        keys = saw._required_audit_coverage_keys(reviewer, 2)

        self.assertIn("audio_mouth_sync", keys)
        self.assertIn("generation_density", keys)
        self.assertIn("multimodal_task_scope", keys)
        self.assertIn("camera_motion_reasonableness", keys)
        self.assertTrue(saw.is_vertical_v2_reviewer(reviewer, 2))

    def test_episode_metadata_cannot_switch_seedance25_to_another_task(self):
        with TemporaryDirectory() as tmp:
            episode_dir = Path(tmp)
            profile = saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)
            metadata = {
                "video_profile": saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                "video_profile_contract_version": profile["contract_version"],
                "video_task_type": "reference_generation",
                "requires_multimodal_materials": True,
                "minimum_material_inputs": 1,
                "allowed_multimodal_material_types": list(profile["allowed_multimodal_material_types"]),
                "forbidden_video_task_modes": list(profile["forbidden_video_task_modes"]),
            }
            (episode_dir / "episode.json").write_text(
                json.dumps(metadata, ensure_ascii=False),
                encoding="utf-8",
            )

            issues = saw.validate_episode_video_profile_contract(episode_dir)
            self.assertTrue(any("video_task_type" in issue for issue in issues), issues)

    def test_prepare_writes_profile_specific_skills_metadata_and_task_contract(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "ep01.txt"
            workspace_dir = tmp_path / "agent_runs"
            out_dir = tmp_path / "outputs"
            source.write_text(
                "第1集\n场1：内景 客厅 - 日\n人物：甲\n甲：你好。",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "prepare",
                    "--source",
                    str(source),
                    "--workspace-dir",
                    str(workspace_dir),
                    "--out-dir",
                    str(out_dir),
                    "--run-name",
                    "seedance25-profile-test",
                    "--mode",
                    "scene",
                    "--video-profile",
                    saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                    "--aspect",
                    "vertical",
                    "--visual-style",
                    "live-action",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
            run_dir = workspace_dir / "seedance25-profile-test"
            manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
            profile_contract = json.loads((run_dir / "video_profile.json").read_text(encoding="utf-8"))
            episode_dir = Path(manifest["episodes"][0]["episode_dir"])
            episode = json.loads((episode_dir / "episode.json").read_text(encoding="utf-8"))
            task = (episode_dir / "TASK.md").read_text(encoding="utf-8")
            context = (run_dir / "context.md").read_text(encoding="utf-8")

            self.assertEqual(manifest["video_profile"], saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)
            self.assertEqual(manifest["version"], 2)
            self.assertEqual(manifest["target_video_model"], "doubao-seedance-2-5-260628")
            self.assertEqual(manifest["video_resolution"], "720p")
            self.assertEqual(manifest["video_aspect_ratio"], "9:16")
            self.assertEqual(manifest["video_fps"], 24)
            self.assertIs(manifest["generate_audio"], True)
            self.assertEqual(manifest["video_task_type"], "multimodal_generation")
            self.assertIs(manifest["requires_multimodal_materials"], True)
            self.assertEqual(manifest["minimum_material_inputs"], 1)
            self.assertEqual(
                manifest["forbidden_video_task_modes"],
                list(saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)["forbidden_video_task_modes"]),
            )
            self.assertTrue(manifest["generator_skill_path"].endswith("seedance-2-5-live-vertical-generator\\SKILL.md"))
            self.assertTrue(manifest["reviewer_skill_path"].endswith("seedance-2-5-live-vertical-reviewer\\SKILL.md"))
            self.assertEqual(profile_contract["duration_min_seconds"], 4)
            self.assertEqual(profile_contract["duration_max_seconds"], 30)
            self.assertEqual(profile_contract["timeline_granularity_seconds"], 1)
            self.assertEqual(profile_contract["contract_version"], 2)
            self.assertEqual(profile_contract["video_task_type"], "multimodal_generation")
            self.assertIs(profile_contract["requires_multimodal_materials"], True)
            self.assertEqual(episode["reviewer_source"], "seedance-2-5-live-vertical-reviewer")
            self.assertEqual(episode["vertical_review_contract_version"], 3)
            self.assertEqual(episode["video_profile"], saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)
            self.assertEqual(episode["video_task_type"], "multimodal_generation")
            self.assertIs(episode["requires_multimodal_materials"], True)
            self.assertIn("Group-internal model-facing time ranges must use integer-second boundaries", task)
            self.assertIn("Target video model: `doubao-seedance-2-5-260628`", task)
            self.assertIn("Video task type: `multimodal_generation` (the only supported task)", task)
            self.assertIn("the storyboard master alone is not generation-ready", task)
            self.assertIn("Vertical review contract: `v3`", task)
            self.assertIn("`review_facts.json` (generated by pre-check; never hand-write)", task)
            self.assertIn("Video profile: `seedance-2.5-live-vertical`", context)
            self.assertIn("Native audio generation: `true`", context)
            self.assertIn("Video task type: `multimodal_generation` (only)", context)
            self.assertIn("Forbidden video task modes", context)

    def test_prepare_cli_accepts_explicit_legacy_profile_for_horizontal_and_3d_cg(self):
        cases = (
            ("horizontal", "live-action", "storyboard-horizontal-reviewer"),
            ("vertical", "3d-cg", "storyboard-reviewer"),
        )
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "ep01.txt"
            source.write_text(
                "第1集\n场1：内景 客厅 - 日\n人物：甲\n甲：你好。",
                encoding="utf-8",
            )

            for aspect, visual_style, expected_reviewer in cases:
                with self.subTest(aspect=aspect, visual_style=visual_style):
                    run_name = f"legacy-{aspect}-{visual_style}"
                    workspace_dir = tmp_path / "agent_runs"
                    result = subprocess.run(
                        [
                            sys.executable,
                            str(WORKSPACE_SCRIPT),
                            "prepare",
                            "--source",
                            str(source),
                            "--workspace-dir",
                            str(workspace_dir),
                            "--out-dir",
                            str(tmp_path / "outputs"),
                            "--run-name",
                            run_name,
                            "--mode",
                            "scene",
                            "--video-profile",
                            saw.DEFAULT_VIDEO_PROFILE,
                            "--aspect",
                            aspect,
                            "--visual-style",
                            visual_style,
                        ],
                        cwd=ROOT,
                        text=True,
                        capture_output=True,
                        encoding="utf-8",
                    )

                    self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
                    run_dir = workspace_dir / run_name
                    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
                    episode_dir = Path(manifest["episodes"][0]["episode_dir"])
                    episode = json.loads((episode_dir / "episode.json").read_text(encoding="utf-8"))
                    self.assertEqual(manifest["video_profile"], saw.DEFAULT_VIDEO_PROFILE)
                    self.assertEqual(episode["video_profile"], saw.DEFAULT_VIDEO_PROFILE)
                    self.assertEqual(episode["reviewer_source"], expected_reviewer)
                    self.assertEqual(
                        episode["vertical_review_contract_version"],
                        2 if aspect == "vertical" else None,
                    )

    def test_prepare_cli_rejects_incompatible_explicit_seedance25_profile(self):
        cases = (
            ("horizontal", "live-action"),
            ("vertical", "3d-cg"),
        )
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "ep01.txt"
            source.write_text(
                "第1集\n场1：内景 客厅 - 日\n人物：甲\n甲：你好。",
                encoding="utf-8",
            )

            for aspect, visual_style in cases:
                with self.subTest(aspect=aspect, visual_style=visual_style):
                    result = subprocess.run(
                        [
                            sys.executable,
                            str(WORKSPACE_SCRIPT),
                            "prepare",
                            "--source",
                            str(source),
                            "--workspace-dir",
                            str(tmp_path / "agent_runs"),
                            "--out-dir",
                            str(tmp_path / "outputs"),
                            "--run-name",
                            f"incompatible-{aspect}-{visual_style}",
                            "--video-profile",
                            saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                            "--aspect",
                            aspect,
                            "--visual-style",
                            visual_style,
                        ],
                        cwd=ROOT,
                        text=True,
                        capture_output=True,
                        encoding="utf-8",
                    )

                    output = result.stderr + result.stdout
                    self.assertEqual(result.returncode, 2, msg=output)
                    self.assertIn("only supports", output)

    def test_full_validation_and_collection_use_seedance25_contract(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            run_dir = tmp_path / "run"
            episode_dir = run_dir / "episodes" / "ep01"
            previous_episode_dir = run_dir / "episodes" / "ep00"
            out_dir = tmp_path / "outputs"
            episode_dir.mkdir(parents=True)
            previous_episode_dir.mkdir(parents=True)
            out_dir.mkdir()
            final_content = vertical_group(4, [("0", "4")])
            previous_final_content = "上一集实际末组：甲在客厅画面左侧，右手持有钥匙，日间窗光不变。\n"
            boundary_content = """# Cross-Episode Boundary Context

continuous_from_previous: true
previous_episode: ep00
current_episode: ep01
previous_final: ../ep00/final.txt
"""
            reviewer = "seedance-2-5-live-vertical-reviewer"
            review = {
                "pass": True,
                "summary": "已对照原剧本逐组核对 2.5 时间、空间、动作、声音和连续性。",
                "checked_groups": ["第1组"],
                "audit_coverage": {
                    key: "checked"
                    for key in saw._required_audit_coverage_keys(reviewer, 3)
                },
                "spot_checks": [
                    {"group": "第1组", "type": "timing_math", "evidence": "0-4秒为整数边界，总时长4秒。"},
                    {"group": "第1组", "type": "space_locking", "evidence": "甲在画面左侧并写明侧对镜头、脸朝画右。"},
                    {"group": "第1组", "type": "prop_continuity", "evidence": "钥匙从组首到组尾都在甲右手。"},
                ],
                "semantic_checks": [
                    {"group": "第1组", "type": "script_fidelity", "result": "pass", "evidence": "未新增剧情事实。", "fix_instruction": "失败时恢复原剧本事实。"},
                    {"group": "第1组", "type": "generation_density", "result": "pass", "evidence": "单一持钥匙状态，4秒短节拍可执行。", "fix_instruction": "失败时合并或拆分动作。"},
                    {"group": "第1组", "type": "audio_mouth_sync", "result": "pass", "evidence": "本组无对白或画外音。", "fix_instruction": "失败时补声音来源和口型。"},
                    {"group": "第1组", "type": "cross_episode_continuity", "result": "pass", "evidence": "已对照上一集实际末组的人物、钥匙、门和日光状态。", "fix_instruction": "失败时按上一集实际末态局部修正首帧。"},
                ],
                "mechanical_evidence": saw.build_vertical_review_facts(
                    final_content,
                    review_contract_version=3,
                    require_cross_episode_boundary=True,
                    previous_episode_id="ep00",
                    previous_final_content=previous_final_content,
                )["mechanical_evidence"],
                "semantic_coverage": saw.build_vertical_semantic_coverage(
                    final_content,
                    require_cross_episode_boundary=True,
                ),
                "issue_instances_total": 0,
                "affected_groups": [],
                "issues": [],
                "warnings": [],
            }
            status = {
                "episode_id": "ep01",
                "status": "done",
                "output_name": "ep01-seedance25-storyboard.txt",
                "summary": "2.5 profile smoke",
                "hard_issues_remaining": [],
                "warnings": [],
                "reviewer_source": reviewer,
                "reviewer_pass": True,
                "reviewer_issues_count": 0,
                "reviewer_warnings_count": 0,
            }
            episode_meta = {
                "episode_id": "ep01",
                "storyboard_aspect": "vertical",
                "visual_style": "live-action",
                "video_profile": saw.SEEDANCE25_LIVE_VERTICAL_PROFILE,
                "video_profile_contract_version": 2,
                "video_task_type": "multimodal_generation",
                "requires_multimodal_materials": True,
                "minimum_material_inputs": 1,
                "allowed_multimodal_material_types": ["image", "video", "audio"],
                "forbidden_video_task_modes": list(
                    saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)["forbidden_video_task_modes"]
                ),
                "reviewer_source": reviewer,
                "vertical_review_contract_version": 3,
                "depends_on_episode": "ep00",
            }
            output_path = out_dir / "ep01-seedance25-storyboard.txt"
            manifest = {
                "out_dir": str(out_dir),
                "episodes": [
                    {
                        "episode_id": "ep01",
                        "display_name": "ep01",
                        "episode_dir": str(episode_dir),
                        "output_path": str(output_path),
                    }
                ],
            }
            (episode_dir / "final.txt").write_text(final_content, encoding="utf-8")
            (episode_dir / "review.txt").write_text(json.dumps(review, ensure_ascii=False), encoding="utf-8")
            (episode_dir / "status.json").write_text(json.dumps(status, ensure_ascii=False), encoding="utf-8")
            (episode_dir / "episode.json").write_text(json.dumps(episode_meta, ensure_ascii=False), encoding="utf-8")
            (episode_dir / "boundary_context.md").write_text(boundary_content, encoding="utf-8")
            (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")

            missing_previous_result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "validate-episode",
                    "--episode-dir",
                    str(episode_dir),
                    "--pre-check",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertNotEqual(missing_previous_result.returncode, 0)
            self.assertIn("boundary previous final is missing", missing_previous_result.stdout)

            (previous_episode_dir / "final.txt").write_text(previous_final_content, encoding="utf-8")
            precheck_result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "validate-episode",
                    "--episode-dir",
                    str(episode_dir),
                    "--pre-check",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertEqual(precheck_result.returncode, 0, msg=precheck_result.stderr + precheck_result.stdout)
            review_facts_path = episode_dir / "review_facts.json"
            review_facts_text = review_facts_path.read_text(encoding="utf-8")
            review_facts = json.loads(review_facts_text)
            self.assertEqual(review_facts["mechanical_evidence"], review["mechanical_evidence"])
            self.assertEqual(review_facts["mechanical_evidence"]["handoff_count"], 1)
            self.assertEqual(
                review["semantic_coverage"]["handoffs_checked"],
                ["上一集实际末组->第1组"],
            )

            review_facts_path.unlink()
            missing_facts_result = subprocess.run(
                [sys.executable, str(WORKSPACE_SCRIPT), "validate-episode", "--episode-dir", str(episode_dir)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertNotEqual(missing_facts_result.returncode, 0)
            self.assertIn("missing review facts", missing_facts_result.stdout)

            review_facts_path.write_text(review_facts_text, encoding="utf-8")
            (episode_dir / "final.txt").write_text(
                final_content.replace("握住钥匙", "攥住钥匙", 1),
                encoding="utf-8",
            )
            stale_facts_result = subprocess.run(
                [sys.executable, str(WORKSPACE_SCRIPT), "validate-episode", "--episode-dir", str(episode_dir)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertNotEqual(stale_facts_result.returncode, 0)
            self.assertIn("review_facts.json is stale", stale_facts_result.stdout)
            (episode_dir / "final.txt").write_text(final_content, encoding="utf-8")

            (previous_episode_dir / "final.txt").write_text(
                previous_final_content + "上一集末态后来发生修改。\n",
                encoding="utf-8",
            )
            stale_previous_result = subprocess.run(
                [sys.executable, str(WORKSPACE_SCRIPT), "validate-episode", "--episode-dir", str(episode_dir)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertNotEqual(stale_previous_result.returncode, 0)
            self.assertIn("review_facts.json is stale", stale_previous_result.stdout)
            (previous_episode_dir / "final.txt").write_text(previous_final_content, encoding="utf-8")

            validate_result = subprocess.run(
                [sys.executable, str(WORKSPACE_SCRIPT), "validate-episode", "--episode-dir", str(episode_dir)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertEqual(validate_result.returncode, 0, msg=validate_result.stderr + validate_result.stdout)
            self.assertIn("[passed] episode validation", validate_result.stdout)

            collect_result = subprocess.run(
                [sys.executable, str(WORKSPACE_SCRIPT), "collect", "--run-dir", str(run_dir)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertEqual(collect_result.returncode, 0, msg=collect_result.stderr + collect_result.stdout)
            collected = output_path.read_text(encoding="utf-8")
            self.assertIn("声音设计：生成与画面同步的现场对白", collected)
            self.assertNotIn(saw.VERTICAL_SEEDANCE_NEGATIVE_LINE, collected)
            self.assertNotIn("4K画质", collected)

    def test_model_contract_reference_stays_in_sync_with_machine_profile(self):
        """model-contract.md 是人读快照，VIDEO_PROFILE_CONFIG 是机器真源。

        两者写的是同一份官方参数，必须一起改。只改文档不改配置（或反过来）
        以前不会被任何测试发现，这里把文档解析出来逐项对齐。
        """
        profile = saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)
        contract = (ROOT / "agent_skills" / "seedance-2-5-live-vertical" / "references" / "model-contract.md").read_text(
            encoding="utf-8"
        )

        self.assertIn(f"`{profile['target_video_model']}`", contract)
        self.assertIn(f"`{profile['video_task_type']}` only", contract)
        self.assertIn(f"`{profile['aspect_ratio']}`", contract)
        self.assertIn(
            f"integer seconds in `[{profile['duration_min_seconds']}, {profile['duration_max_seconds']}]`",
            contract,
        )
        self.assertIn(f"FPS: `{profile['fps']}`", contract)
        self.assertIn(f"Default resolution: `{profile['default_resolution']}`", contract)
        for resolution in profile["supported_resolutions"]:
            self.assertIn(f"`{resolution}`", contract)

        # 未启用的分辨率不得只在文档里被悄悄放开。
        for resolution in ("1080p", "2k", "4k", "4K"):
            self.assertNotIn(resolution, profile["supported_resolutions"])
            if resolution == "1080p":
                self.assertIn("1080p is intentionally not enabled", contract)

    def test_profile_declares_repo_boundary_for_material_binding(self):
        """2.5 要求真实多模态素材绑定，但本仓库的 asset_bindings.json 只有静态参考图角色。

        这个缺口必须是显式声明的，不能靠读者自己发现。
        """
        skill = (ROOT / "agent_skills" / "seedance-2-5-live-vertical" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("## 仓库边界", skill)
        self.assertIn("asset_bindings.json", skill)
        self.assertIn("不满足", skill)

        binding_roles = (ROOT / "agent_skills" / "asset-extractor" / "scripts" / "validate-assets.mjs").read_text(
            encoding="utf-8"
        )
        # 一旦 asset-extractor 真的支持了视频/音频素材角色，本边界声明就该重写。
        self.assertNotIn("video_material", binding_roles)
        self.assertNotIn("audio_material", binding_roles)


if __name__ == "__main__":
    unittest.main()
