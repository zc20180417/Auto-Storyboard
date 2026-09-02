import json
import shutil
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import storyboard_agent_workspace as saw


FINAL_TEXT = """=== [cut_id: EP01-G01] 第1组：丹房起火（总时长：4秒，镜头数：1） ===

**人物：** 方平
**场景：** 炼丹房，夜
**道具：** 元鼎

**镜头1：固定中景（0-4秒）**

0-4秒：方平守在元鼎前，灵火贴着鼎腹稳定燃烧。

=== 第1组结束 ===
"""


class StoryboardIndexIdentityContractTests(unittest.TestCase):
    def make_project_and_episode(self, base: Path, *, profile: str = saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE):
        project_root = base / "project"
        run_dir = base / "agent_runs" / "identity-test"
        episode_dir = run_dir / "episodes" / "ep01"
        episode_dir.mkdir(parents=True)

        source_paths = [
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/model-contract.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/visual-presets.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/xianxia-vfx-grammar.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/native-audio.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/segment-handoff.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-generator/SKILL.md",
            "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-reviewer/SKILL.md",
            "agent_skills/3d-cg-visual-style/SKILL.md",
            "agent_skills/project-packs/registry.json",
            "agent_skills/project-packs/dandao-xiantu/pack.json",
            "agent_skills/project-packs/dandao-xiantu/SKILL.md",
            "agent_skills/project-packs/dandao-xiantu/references/alchemy-system.md",
            "agent_skills/project-packs/dandao-xiantu/references/yuanding-visual-bible.md",
        ]
        for relative in source_paths:
            destination = project_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)

        manifest = {
            "project_root": str(project_root),
            "mode": "single",
            "generator_skill_path": str(project_root / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-generator/SKILL.md"),
            "reviewer_skill_path": str(project_root / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg-reviewer/SKILL.md"),
            "cg_visual_style_skill_path": str(project_root / "agent_skills/3d-cg-visual-style/SKILL.md"),
        }
        (run_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        preset = saw.visual_style_preset_snapshot(
            saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
            saw.REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET,
        )
        pack = saw.project_pack_snapshot(
            project_root=project_root,
            video_profile=saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
            aspect="horizontal",
            visual_style="3d-cg",
            mode="single",
            visual_style_preset=saw.REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET,
            project_pack_id="dandao-xiantu",
        )
        episode = {
            "episode_id": "ep01",
            "series_title": "丹道仙途",
            "video_profile": profile,
            "video_profile_contract_version": 1,
            "provider_contract_version": 1,
            "provider_task_mapping": {"field": "omni_reference_task_type", "value": "reference"},
            "profile_capabilities": {"auto_export_index": True},
            "storyboard_aspect": "horizontal",
            "visual_style": "3d-cg",
            "visual_style_preset": saw.REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET,
            "visual_style_preset_version": 1,
            "visual_style_preset_sha256": preset["sha256"],
            "project_pack_id": "dandao-xiantu",
            "project_pack_version": 1,
            "project_pack_path": str(project_root / "agent_skills/project-packs/dandao-xiantu/pack.json"),
            "project_pack_sha256": pack["sha256"],
            "seedance_profile_path": str(project_root / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md"),
            "generator_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-generator",
            "reviewer_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
        }
        (episode_dir / "episode.json").write_text(json.dumps(episode), encoding="utf-8")
        (episode_dir / "final.txt").write_text(FINAL_TEXT, encoding="utf-8")
        return project_root, episode_dir

    def test_new_profile_index_contains_complete_resolved_workflow_identity(self):
        with TemporaryDirectory() as tmp:
            _, episode_dir = self.make_project_and_episode(Path(tmp))

            payload = saw.build_storyboard_index_payload(content=FINAL_TEXT, episode_dir=episode_dir)

            self.assertEqual(payload["schema_version"], 2)
            identity = payload["workflow_identity"]
            self.assertEqual(identity["identity_schema_version"], 1)
            self.assertEqual(identity["video_profile"], saw.SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE)
            self.assertEqual(identity["video_profile_contract_version"], 1)
            self.assertEqual(identity["provider_contract_version"], 1)
            self.assertEqual(identity["storyboard_aspect"], "horizontal")
            self.assertEqual(identity["visual_style"], "3d-cg")
            self.assertEqual(identity["visual_style_preset"], saw.REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET)
            self.assertEqual(identity["project_pack_id"], "dandao-xiantu")
            self.assertRegex(identity["resolved_workflow_hash"], r"^[0-9a-f]{64}$")
            roles = {item["role"] for item in identity["workflow_audit"]["files"]}
            self.assertEqual(
                roles,
                {
                    "profile_skill",
                    "model_contract",
                    "visual_preset_reference",
                    "xianxia_vfx_grammar",
                    "native_audio_contract",
                    "segment_handoff_contract",
                    "generator_skill",
                    "reviewer_skill",
                    "3d_cg_visual_style",
                    "project_pack_registry",
                    "project_pack_manifest",
                    "project_pack_skill",
                    "project_pack_reference:alchemy-system.md",
                    "project_pack_reference:yuanding-visual-bible.md",
                },
            )
            for item in identity["workflow_audit"]["files"]:
                self.assertFalse(Path(item["path"]).is_absolute())
                self.assertRegex(item["sha256"], r"^[0-9a-f]{64}$")

    def test_loaded_file_changes_hash_but_unloaded_file_does_not(self):
        with TemporaryDirectory() as tmp:
            project_root, episode_dir = self.make_project_and_episode(Path(tmp))
            original = saw.build_resolved_workflow_identity(episode_dir)["resolved_workflow_hash"]
            loaded_path = project_root / "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/native-audio.md"
            loaded_path.write_text(loaded_path.read_text(encoding="utf-8") + "\n测试变化\n", encoding="utf-8")
            changed = saw.build_resolved_workflow_identity(episode_dir)["resolved_workflow_hash"]
            self.assertNotEqual(changed, original)

            unloaded = project_root / "agent_skills/provisional-unused.md"
            unloaded.write_text("未加载模块", encoding="utf-8")
            unchanged = saw.build_resolved_workflow_identity(episode_dir)["resolved_workflow_hash"]
            self.assertEqual(unchanged, changed)

    def test_each_audited_file_invalidates_the_resolved_hash(self):
        with TemporaryDirectory() as tmp:
            project_root, episode_dir = self.make_project_and_episode(Path(tmp))
            identity = saw.build_resolved_workflow_identity(episode_dir)
            baseline = identity["resolved_workflow_hash"]

            for item in identity["workflow_audit"]["files"]:
                path = project_root / item["path"]
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b"\n ")
                    changed = saw.build_resolved_workflow_identity(episode_dir)["resolved_workflow_hash"]
                    self.assertNotEqual(changed, baseline, item["path"])
                finally:
                    path.write_bytes(original)

    def test_episode_contract_rejects_tampered_pack_snapshot(self):
        with TemporaryDirectory() as tmp:
            _, episode_dir = self.make_project_and_episode(Path(tmp))
            episode = json.loads((episode_dir / "episode.json").read_text(encoding="utf-8"))
            episode["project_pack_version"] = 99
            (episode_dir / "episode.json").write_text(json.dumps(episode), encoding="utf-8")

            issues = saw.validate_episode_video_profile_contract(episode_dir)

            self.assertTrue(any("project_pack_version" in issue for issue in issues), issues)

    def test_final_hash_remains_bound_and_legacy_index_is_not_forced_to_v2(self):
        with TemporaryDirectory() as tmp:
            _, episode_dir = self.make_project_and_episode(Path(tmp), profile=saw.DEFAULT_VIDEO_PROFILE)
            episode = json.loads((episode_dir / "episode.json").read_text(encoding="utf-8"))
            episode["video_profile_contract_version"] = 1
            (episode_dir / "episode.json").write_text(json.dumps(episode), encoding="utf-8")

            payload = saw.build_storyboard_index_payload(content=FINAL_TEXT, episode_dir=episode_dir)

            self.assertNotIn("schema_version", payload)
            self.assertNotIn("workflow_identity", payload)
            self.assertEqual(payload["source_hashes"]["final_txt_sha256"], saw.hashlib.sha256(FINAL_TEXT.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    unittest.main()
