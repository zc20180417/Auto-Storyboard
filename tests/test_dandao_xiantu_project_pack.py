import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import storyboard_agent_workspace as saw


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_SCRIPT = ROOT / "storyboard_agent_workspace.py"
PACK_ID = "dandao-xiantu"
PROFILE_ID = saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE
PRESET_ID = saw.REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET


class DandaoXiantuProjectPackTests(unittest.TestCase):
    def test_registry_and_pack_are_versioned_default_off_and_isolated(self):
        registry = json.loads((ROOT / "agent_skills/project-packs/registry.json").read_text(encoding="utf-8"))
        pack = json.loads((ROOT / "agent_skills/project-packs/dandao-xiantu/pack.json").read_text(encoding="utf-8"))

        self.assertEqual(registry["schema_version"], 1)
        self.assertEqual(registry["packs"][PACK_ID]["version"], 1)
        self.assertEqual(pack["id"], PACK_ID)
        self.assertEqual(pack["version"], 1)
        self.assertEqual(pack["compatible_video_profiles"], [PROFILE_ID])
        self.assertEqual(pack["required_visual_style_preset"], PRESET_ID)
        self.assertFalse(pack["enabled_by_default"])
        self.assertIn("元鼎", registry["packs"][PACK_ID]["exclusive_markers"])

    def test_pack_snapshot_binds_all_authoritative_files(self):
        snapshot = saw.project_pack_snapshot(
            project_root=ROOT,
            video_profile=PROFILE_ID,
            aspect="horizontal",
            visual_style="3d-cg",
            mode="single",
            visual_style_preset=PRESET_ID,
            project_pack_id=PACK_ID,
        )

        self.assertEqual(snapshot["id"], PACK_ID)
        self.assertEqual(snapshot["version"], 1)
        self.assertRegex(snapshot["sha256"], r"^[0-9a-f]{64}$")
        loaded = {Path(item["path"]).name for item in snapshot["loaded_files"]}
        self.assertEqual(loaded, {"pack.json", "SKILL.md", "alchemy-system.md", "yuanding-visual-bible.md"})
        for item in snapshot["loaded_files"]:
            self.assertRegex(item["sha256"], r"^[0-9a-f]{64}$")

    def test_pack_applies_required_preset_when_omitted_and_rejects_conflict(self):
        config = saw.resolved_workspace_config(
            video_profile=PROFILE_ID,
            aspect="horizontal",
            visual_style="3d-cg",
            resolution="720p",
            mode="single",
            visual_style_preset=None,
            project_pack_id=PACK_ID,
            project_root=ROOT,
        )
        self.assertEqual(config["project_pack_id"], PACK_ID)
        self.assertEqual(config["visual_style_preset"], PRESET_ID)
        self.assertEqual(config["visual_style_preset_source"], "project_pack")

        with self.assertRaisesRegex(ValueError, "actual=.*required=.*dandao-xiantu"):
            saw.resolved_workspace_config(
                video_profile=PROFILE_ID,
                aspect="horizontal",
                visual_style="3d-cg",
                resolution="720p",
                mode="single",
                visual_style_preset="non-matching-preset",
                project_pack_id=PACK_ID,
                project_root=ROOT,
            )

    def test_title_does_not_enable_pack_without_explicit_option(self):
        config = saw.resolved_workspace_config(
            video_profile=PROFILE_ID,
            aspect="horizontal",
            visual_style="3d-cg",
            resolution="720p",
            mode="single",
            visual_style_preset=PRESET_ID,
            project_pack_id=None,
            project_root=ROOT,
        )
        self.assertIsNone(config["project_pack_id"])

    def test_prepare_propagates_pack_identity_and_hash(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "丹道仙途-ep01.txt"
            source.write_text("第1集\n场1 内景 静室 - 日\n人物：方平\n方平：开炉。", encoding="utf-8")
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
                    "pack-propagation",
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
                    "--project-pack-id",
                    PACK_ID,
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            run_dir = tmp_path / "agent_runs" / "pack-propagation"
            manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
            episode = json.loads((run_dir / "episodes/ep01/episode.json").read_text(encoding="utf-8"))
            context = (run_dir / "context.md").read_text(encoding="utf-8")
            task = (run_dir / "episodes/ep01/TASK.md").read_text(encoding="utf-8")

            for payload in (manifest, episode):
                self.assertEqual(payload["project_pack_id"], PACK_ID)
                self.assertEqual(payload["project_pack_version"], 1)
                self.assertRegex(payload["project_pack_sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(payload["visual_style_preset"], PRESET_ID)
            self.assertIn(PACK_ID, context)
            self.assertIn(PACK_ID, task)
            self.assertIn("yuanding-visual-bible.md", task)

    def test_project_terms_are_absent_from_generic_profile_and_vfx_files(self):
        generic_files = (
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md",
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/visual-presets.md",
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/xianxia-vfx-grammar.md",
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/native-audio.md",
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-generator/SKILL.md",
            ROOT / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-reviewer/SKILL.md",
        )
        for path in generic_files:
            text = path.read_text(encoding="utf-8")
            for term in ("方平", "元鼎", "落阳宗", "每日九次"):
                self.assertNotIn(term, text, f"project term leaked into {path}")


if __name__ == "__main__":
    unittest.main()
