import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import seedance_material_handoff as handoff


FINAL_TEXT = """=== [cut_id: EP01-G01] 第1组：门口确认（总时长：4秒，镜头数：1） ===

**人物：** 甲
**场景：** 客厅，白天
**道具：** 钥匙

**组首空间锁定：** 甲在画面左侧，正面对镜头，右手握住钥匙。

**镜头1：固定中景，确认钥匙（0-4秒）**

0-4秒：甲抬起钥匙确认，动作结束时钥匙仍在右手。

**组尾衔接：** 甲保持站位和持物状态。

=== 第1组结束 ===
"""


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class SeedanceMaterialHandoffTests(unittest.TestCase):
    def make_episode(self, root: Path) -> Path:
        episode_dir = root / "episodes" / "ep01"
        episode_dir.mkdir(parents=True)
        (episode_dir / "final.txt").write_text(FINAL_TEXT, encoding="utf-8")
        write_json(
            episode_dir / "episode.json",
            {
                "episode_id": "ep01",
                "series_title": "测试剧",
                "video_profile": handoff.PROFILE_ID,
                "video_resolution": "480p",
            },
        )
        write_json(
            episode_dir / "storyboard_index.json",
            {
                "project": "测试剧",
                "episode_id": "EP01",
                "source_hashes": {
                    "final_txt_sha256": handoff.sha256_file(episode_dir / "final.txt"),
                },
                "cuts": [
                    {
                        "cut_id": "EP01-G01",
                        "group_index": 1,
                        "title": "门口确认",
                        "scene": ["客厅，白天"],
                        "characters": ["甲"],
                        "props": ["钥匙"],
                        "duration_sec": 4,
                    }
                ],
            },
        )
        write_json(
            episode_dir / "asset_bindings.json",
            {
                "project": "测试剧",
                "episode_id": "EP01",
                "bindings": [
                    {
                        "binding_id": "EP01_BIND_001",
                        "cut_id": "EP01-G01",
                        "asset_id": "CHAR_甲_BASE",
                        "state_id": "BASE",
                        "asset_type": "character",
                        "binding_role": "character_reference",
                        "reference_priority": "primary",
                        "use_for_video": "yes",
                        "required_for_generation": "yes",
                        "source": "asset_table",
                        "note": "甲的身份参考",
                    }
                ],
            },
        )
        return episode_dir

    def activate_material(self, episode_dir: Path) -> Path:
        requirements_path, local_path = handoff.export_material_handoff(episode_dir)
        material_path = episode_dir / "materials" / "char-a.png"
        material_path.parent.mkdir()
        material_path.write_bytes(b"not-a-real-png-but-stable-for-contract-tests")
        file_hash = handoff.sha256_file(material_path)
        local_payload = json.loads(local_path.read_text(encoding="utf-8"))
        local_payload["materials"][0].update(
            {
                "source": {"kind": "local_file", "path": "materials/char-a.png"},
                "mime_type": "image/png",
                "sha256": file_hash,
                "authorization": {"status": "confirmed", "note": "项目自有素材"},
            }
        )
        write_json(local_path, local_payload)
        write_json(
            episode_dir / handoff.ARK_SYNC_RESULTS_FILE,
            {
                "schema_version": 1,
                "authority": "manjuweb",
                "project": "测试剧",
                "episode_id": "EP01",
                "source_hashes": {
                    "material_requirements_sha256": handoff.sha256_file(requirements_path),
                    "local_materials_sha256": handoff.sha256_file(local_path),
                },
                "materials": [
                    {
                        "material_key": "CHAR_甲_BASE",
                        "media_type": "image",
                        "sha256": file_hash,
                        "ark_asset_id": "asset://asset-contract-test",
                        "ark_status": "active",
                    }
                ],
            },
        )
        return material_path

    def test_compiles_static_bindings_into_material_requirements_and_local_template(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))

            requirements_path, local_path = handoff.export_material_handoff(episode_dir)

            requirements = json.loads(requirements_path.read_text(encoding="utf-8"))
            requirement = requirements["requirements"][0]
            self.assertEqual(requirements["profile"], handoff.PROFILE_ID)
            self.assertEqual(requirement["cut_id"], "EP01-G01")
            self.assertEqual(requirement["material_key"], "CHAR_甲_BASE")
            self.assertEqual(requirement["media_type"], "image")
            self.assertEqual(requirement["role"], "character_identity")
            self.assertTrue(requirement["required"])
            self.assertIn("face", requirement["provides"])
            self.assertIn("action", requirement["excludes"])

            local_materials = json.loads(local_path.read_text(encoding="utf-8"))
            self.assertEqual(local_materials["materials"][0]["source"], {"kind": "missing"})
            self.assertNotIn("ark_status", local_materials["materials"][0])
            self.assertNotIn("ark_asset_id", local_materials["materials"][0])

    def test_cli_requires_a_passed_asset_reviewer_gate_before_export(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            command = [
                sys.executable,
                str(ROOT / "storyboard_agent_workspace.py"),
                "export-seedance-material-requirements",
                "--episode-dir",
                str(episode_dir),
            ]

            blocked = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(blocked.returncode, 2)
            self.assertIn("missing asset_status.json", blocked.stderr)

            write_json(
                episode_dir / "asset_status.json",
                {
                    "status": "done",
                    "reviewer_source": "asset-reviewer",
                    "reviewer_pass": True,
                    "reviewer_issues_count": 0,
                },
            )
            exported = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(exported.returncode, 0, msg=exported.stderr + exported.stdout)
            self.assertTrue((episode_dir / handoff.REQUIREMENTS_FILE).is_file())
            self.assertTrue((episode_dir / handoff.LOCAL_MATERIALS_FILE).is_file())

    def test_missing_materials_export_a_blocked_package(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            handoff.export_material_handoff(episode_dir)

            package = handoff.build_generation_package(episode_dir)

            self.assertFalse(package["generation_ready"])
            self.assertFalse(package["submit_allowed"])
            self.assertTrue(any("missing ark_sync_results.json" in issue for issue in package["blocking_issues"]))

    def test_active_manjuweb_result_builds_hash_bound_package_and_detects_staleness(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            material_path = self.activate_material(episode_dir)

            validation = handoff.validate_material_handoff(episode_dir)
            self.assertTrue(validation["generation_ready"], validation["issues"])

            package_path = handoff.write_generation_package(episode_dir)
            package = json.loads(package_path.read_text(encoding="utf-8"))
            self.assertTrue(package["generation_ready"])
            self.assertTrue(package["submit_allowed"])
            self.assertEqual(package["cuts"][0]["material_inputs"][0]["token"], "@图片1")
            self.assertIn("**人物：** 甲", package["cuts"][0]["request_draft"]["prompt"])
            self.assertNotEqual(
                package["cuts"][0]["request_draft"]["prompt"].strip(),
                "=== 第1组结束 ===",
            )
            self.assertEqual(package["cuts"][0]["request_draft"]["resolution"], "480p")
            self.assertTrue(package["cuts"][0]["request_draft"]["generateAudio"])
            self.assertEqual(
                package["cuts"][0]["request_draft"]["referenceImageSlots"],
                [
                    {
                        "type": "ark",
                        "assetId": "asset://asset-contract-test",
                        "name": "CHAR_甲_BASE",
                        "source": "trusted-material",
                        "entryMode": "uploaded",
                        "status": "active",
                    }
                ],
            )
            self.assertEqual(
                package["cuts"][0]["material_inputs"][0]["ark_asset_id"],
                "asset://asset-contract-test",
            )
            self.assertEqual(
                package["source_integrity"]["final_txt_sha256"],
                handoff.sha256_file(episode_dir / "final.txt"),
            )
            self.assertEqual(
                package["cuts"][0]["material_inputs"][0]["sha256"],
                hashlib.sha256(material_path.read_bytes()).hexdigest(),
            )

            (episode_dir / "final.txt").write_text(FINAL_TEXT + "\n最终稿发生变化。\n", encoding="utf-8")
            stale = handoff.validate_material_handoff(episode_dir)
            self.assertFalse(stale["generation_ready"])
            self.assertIn("storyboard_index.json is stale for current final.txt; re-export it", stale["issues"])
            self.assertIn("seedance_generation_package.json is stale; re-export it", stale["issues"])
            rebuilt = handoff.build_generation_package(episode_dir)
            self.assertFalse(rebuilt["generation_ready"])
            self.assertIn(
                "storyboard_index.json is stale for current final.txt; re-export it",
                rebuilt["blocking_issues"],
            )

    def test_requirement_hash_invalidates_when_asset_bindings_change(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            handoff.export_material_handoff(episode_dir)
            bindings_path = episode_dir / "asset_bindings.json"
            bindings = json.loads(bindings_path.read_text(encoding="utf-8"))
            bindings["bindings"][0]["note"] = "绑定说明已改变"
            write_json(bindings_path, bindings)

            validation = handoff.validate_material_handoff(episode_dir)

            self.assertFalse(validation["generation_ready"])
            self.assertIn("seedance_material_requirements.json is stale; re-export it", validation["issues"])

    def test_ignores_bindings_explicitly_disabled_for_video(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            bindings_path = episode_dir / "asset_bindings.json"
            bindings = json.loads(bindings_path.read_text(encoding="utf-8"))
            bindings["bindings"].append(
                {
                    "binding_id": "EP01_BIND_002",
                    "cut_id": "EP01-G01",
                    "asset_id": "PROP_UNUSED_BASE",
                    "state_id": "BASE",
                    "asset_type": "prop",
                    "binding_role": "prop_reference",
                    "reference_priority": "background",
                    "use_for_video": "no",
                    "required_for_generation": "no",
                    "source": "asset_table",
                    "note": "只用于资产记录",
                }
            )
            write_json(bindings_path, bindings)

            requirements_path, local_path = handoff.export_material_handoff(episode_dir)
            requirements = json.loads(requirements_path.read_text(encoding="utf-8"))
            local_materials = json.loads(local_path.read_text(encoding="utf-8"))

            self.assertEqual(len(requirements["requirements"]), 1)
            self.assertEqual(len(local_materials["materials"]), 1)
            self.assertEqual(requirements["requirements"][0]["material_key"], "CHAR_甲_BASE")


if __name__ == "__main__":
    unittest.main()
