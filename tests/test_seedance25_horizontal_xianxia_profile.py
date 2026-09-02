import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import storyboard_agent_workspace as saw


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_SCRIPT = ROOT / "storyboard_agent_workspace.py"
PROFILE_ID = "seedance-2.5-horizontal-xianxia-3d-cg"
PRESET_ID = "realistic-material-restrained-anime-outline"


class Seedance25HorizontalXianxiaProfileTests(unittest.TestCase):
    def test_machine_contract_is_strict_horizontal_3d_cg_single(self):
        profile = saw.video_profile_config(PROFILE_ID)

        self.assertEqual(profile["target_video_model"], "doubao-seedance-2-5-260628")
        self.assertEqual(profile["supported_aspects"], ("horizontal",))
        self.assertEqual(profile["supported_visual_styles"], ("3d-cg",))
        self.assertEqual(profile["supported_modes"], ("single",))
        self.assertEqual(profile["duration_min_seconds"], 4)
        self.assertEqual(profile["duration_max_seconds"], 30)
        self.assertEqual(profile["timeline_granularity_seconds"], 1)
        self.assertEqual(profile["aspect_ratio"], "16:9")
        self.assertEqual(profile["supported_resolutions"], ("720p",))
        self.assertEqual(profile["default_resolution"], "720p")
        self.assertEqual(profile["fps"], 24)
        self.assertIs(profile["generate_audio"], True)
        self.assertEqual(profile["video_task_type"], "multimodal_generation")
        self.assertEqual(profile["provider_contract_version"], 1)
        self.assertEqual(profile["provider_task_mapping"], {
            "field": "omni_reference_task_type",
            "value": "reference",
        })
        self.assertEqual(profile["capabilities"]["material_handoff_schema"], "v2-provider-reference")
        self.assertIs(profile["capabilities"]["auto_export_index"], True)
        self.assertIs(profile["capabilities"]["vertical_review_facts"], False)
        self.assertIs(profile["capabilities"]["visual_style_presets"], True)
        self.assertIs(profile["capabilities"]["project_packs"], True)

    def test_selection_rejects_wrong_aspect_style_resolution_and_mode(self):
        valid = saw.validate_video_profile_selection(
            video_profile=PROFILE_ID,
            aspect="horizontal",
            visual_style="3d-cg",
            resolution="720p",
            mode="single",
            visual_style_preset=PRESET_ID,
        )
        self.assertIsNone(valid)

        invalid_cases = (
            ({"aspect": "vertical", "visual_style": "3d-cg", "resolution": "720p", "mode": "single"}, "aspect"),
            ({"aspect": "horizontal", "visual_style": "live-action", "resolution": "720p", "mode": "single"}, "visual style"),
            ({"aspect": "horizontal", "visual_style": "3d-cg", "resolution": "1080p", "mode": "single"}, "resolution"),
            ({"aspect": "horizontal", "visual_style": "3d-cg", "resolution": "720p", "mode": "scene"}, "mode"),
        )
        for kwargs, expected in invalid_cases:
            with self.subTest(expected=expected):
                issue = saw.validate_video_profile_selection(video_profile=PROFILE_ID, **kwargs)
                self.assertIsNotNone(issue)
                self.assertIn(expected, issue)
                self.assertIn("actual=", issue)
                self.assertIn("allowed=", issue)

    def test_named_preset_is_discoverable_and_compatible_only_with_new_profile(self):
        presets = saw.compatible_visual_style_presets(PROFILE_ID)

        self.assertEqual([item["id"] for item in presets], [PRESET_ID])
        self.assertEqual(presets[0]["name"], "写实材质＋克制卡通轮廓")
        self.assertTrue(presets[0]["description"])
        self.assertEqual(saw.resolved_visual_style_preset(PROFILE_ID, PRESET_ID)["id"], PRESET_ID)

        with self.assertRaisesRegex(ValueError, "not compatible"):
            saw.resolved_visual_style_preset(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE, PRESET_ID)

    def test_preview_resolves_config_without_writing_workspace(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "preview-workspace-config",
                    "--video-profile",
                    PROFILE_ID,
                    "--aspect",
                    "horizontal",
                    "--visual-style",
                    "3d-cg",
                    "--video-resolution",
                    "720p",
                    "--mode",
                    "single",
                    "--visual-style-preset",
                    PRESET_ID,
                ],
                cwd=tmp_path,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            preview = json.loads(result.stdout)
            self.assertEqual(preview["video_profile"], PROFILE_ID)
            self.assertEqual(preview["storyboard_aspect"], "horizontal")
            self.assertEqual(preview["visual_style"], "3d-cg")
            self.assertEqual(preview["visual_style_preset"], PRESET_ID)
            self.assertEqual(preview["video_resolution"], "720p")
            self.assertEqual(preview["mode"], "single")
            self.assertEqual(list(tmp_path.iterdir()), [])

    def test_list_compatible_presets_has_human_readable_output(self):
        result = subprocess.run(
            [
                sys.executable,
                str(WORKSPACE_SCRIPT),
                "list-compatible-presets",
                "--video-profile",
                PROFILE_ID,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            encoding="utf-8",
        )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn(PRESET_ID, result.stdout)
        self.assertIn("写实材质＋克制卡通轮廓", result.stdout)
        self.assertIn("PBR", result.stdout)

    def test_prepare_propagates_immutable_profile_and_preset_identity(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "ep01.txt"
            workspace = tmp_path / "agent_runs"
            source.write_text("第1集\n场1 内景 丹房 - 日\n人物：甲\n甲：开始。", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "prepare",
                    "--source",
                    str(source),
                    "--workspace-dir",
                    str(workspace),
                    "--out-dir",
                    str(tmp_path / "outputs"),
                    "--run-name",
                    "xianxia-profile-contract",
                    "--video-profile",
                    PROFILE_ID,
                    "--aspect",
                    "horizontal",
                    "--visual-style",
                    "3d-cg",
                    "--video-resolution",
                    "720p",
                    "--mode",
                    "single",
                    "--visual-style-preset",
                    PRESET_ID,
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            run_dir = workspace / "xianxia-profile-contract"
            profile = json.loads((run_dir / "video_profile.json").read_text(encoding="utf-8"))
            manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
            episode = json.loads((run_dir / "episodes" / "ep01" / "episode.json").read_text(encoding="utf-8"))
            context = (run_dir / "context.md").read_text(encoding="utf-8")
            task = (run_dir / "episodes" / "ep01" / "TASK.md").read_text(encoding="utf-8")

            for payload in (profile, manifest, episode):
                key = "profile_id" if payload is profile else "video_profile"
                self.assertEqual(payload[key], PROFILE_ID)
                self.assertEqual(payload["visual_style_preset"], PRESET_ID)
                self.assertEqual(payload["visual_style_preset_version"], 1)
                self.assertRegex(payload["visual_style_preset_sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(payload["provider_contract_version"], 1)
                self.assertEqual(payload["provider_task_mapping"]["value"], "reference")

            self.assertIn(PRESET_ID, context)
            self.assertIn(PRESET_ID, task)
            self.assertIn("4 through 30 seconds", task)
            self.assertIn("seedance-2-5-horizontal-xianxia-3d-cg-generator", task)
            self.assertIn("seedance-2-5-horizontal-xianxia-3d-cg-reviewer", task)

    def test_unsupported_scene_fails_before_workspace_creation(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "ep01.txt"
            workspace = tmp_path / "agent_runs"
            source.write_text("第1集\n测试。", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(WORKSPACE_SCRIPT),
                    "prepare",
                    "--source",
                    str(source),
                    "--workspace-dir",
                    str(workspace),
                    "--out-dir",
                    str(tmp_path / "outputs"),
                    "--run-name",
                    "must-not-exist",
                    "--video-profile",
                    PROFILE_ID,
                    "--aspect",
                    "horizontal",
                    "--visual-style",
                    "3d-cg",
                    "--mode",
                    "scene",
                    "--visual-style-preset",
                    PRESET_ID,
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )

            self.assertEqual(result.returncode, 2)
            self.assertIn("actual=scene", result.stderr)
            self.assertIn("allowed=single", result.stderr)
            self.assertFalse((workspace / "must-not-exist").exists())

    def test_old_profiles_keep_defaults_and_capabilities(self):
        legacy = saw.video_profile_config(saw.DEFAULT_VIDEO_PROFILE)
        live_vertical = saw.video_profile_config(saw.SEEDANCE25_LIVE_VERTICAL_PROFILE)

        self.assertEqual(saw.DEFAULT_VIDEO_PROFILE, "seedance-2.0")
        self.assertEqual(legacy["supported_modes"], ("single", "scene"))
        self.assertEqual(live_vertical["supported_modes"], ("single", "scene"))
        self.assertIs(live_vertical["capabilities"]["vertical_review_facts"], True)
        self.assertEqual(live_vertical["capabilities"]["material_handoff_schema"], "v1-live-vertical")
        self.assertEqual(saw.compatible_visual_style_presets(saw.DEFAULT_VIDEO_PROFILE), [])


if __name__ == "__main__":
    unittest.main()
