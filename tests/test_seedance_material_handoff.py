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


HORIZONTAL_FINAL_TEXT = """=== [cut_id: EP01-G01] 第1组：鼎火确认（总时长：8秒，镜头数：2个） ===

**人物**：甲
**场景**：炼丹厢房，白天
**道具/关键视觉资产**：元鼎、贴鼎灵火
**画面风格**：横屏16:9，高质量国漫3D CG，写实材质＋克制卡通轮廓；亚洲骨相、适度动漫五官、可信PBR与少量手绘纹理、东方低饱和色盘、电影级布光。
**视觉峰值/特效重点**：beat：灵火从鼎底沿鼎壁贴行，照亮鼎足后收回火种。
**组间承接**：本组开场；甲在画面左侧面向右侧元鼎，右手停在鼎耳上方，元鼎位于中右景地火位，鼎口未开；画外无人，室内冷白日光与低弱炉鸣保持。
**横屏构图/调度**：16:9左侧留甲的操作空间，中右侧固定元鼎，前景留地火与鼎足，视线轴由甲指尖指向鼎口。

1-1
**镜头描述**：稳定中景，甲抬手从画左引出细薄灵火，火种沿地面贴近元鼎底部并顺鼎壁向上爬行，停在鼎耳下方；甲始终面向元鼎，口型清楚地说“起火”。
**光影设计**：冷白日光为环境主光，灵火的暖色只照亮鼎足、下腹和甲的手缘，青铜与暗紫金材质有克制反射。
**本镜估算时长**：4秒

1-2
**镜头描述**：镜头沿灵火路径低角度贴地推进并在鼎耳处急停；火焰从鼎壁回卷至鼎底火种，炉鸣变细，甲的手停在原位确认火候。
**光影设计**：火光收束后厢房恢复低饱和冷暖对比，鼎纹只留局部呼吸光，不遮挡甲的脸和手。
**本镜估算时长**：4秒

**组尾衔接**：甲仍在画面左侧面向元鼎，右手停在鼎耳上方；元鼎在中右地火位，灵火已回到鼎底并保持弱燃，局部鼎纹余光未灭；轴线和声场不变，最后是低角度中近景。
**运镜强化词**：从甲的指尖横向跟随灵火贴地推进，沿鼎壁上行后急停鼎耳，再反向回卷落回鼎底。
**Seedance执行提示补充**：严格表现来源→形态→路径→作用对象→反馈→收束→声音；灵火不得瞬移或变成无来源能量球，原生音频保留起火、炉鸣和收束细响。
**--neg**：灵火跳到鼎外；元鼎从三足变成四足；强光遮住甲的口型；灵火收束后无火种余态
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
            self.assertEqual(
                set(package),
                {
                    "schema_version", "profile", "model", "project", "episode_id",
                    "generation_ready", "submit_allowed", "blocking_issues",
                    "source_integrity", "stale_if_any_source_hash_changes", "cuts",
                },
            )
            self.assertEqual(
                set(package["cuts"][0]["request_draft"]),
                {
                    "model", "video_task_type", "prompt", "duration", "ratio",
                    "resolution", "fps", "generateAudio", "referenceImageSlots",
                    "referenceVideos", "referenceAudios",
                },
            )
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


class HorizontalXianxiaMaterialHandoffTests(unittest.TestCase):
    PROFILE_ID = "seedance-2.5-horizontal-xianxia-3d-cg"

    def make_episode(self, root: Path) -> Path:
        episode_dir = root / "episodes/ep01"
        episode_dir.mkdir(parents=True)
        (episode_dir / "final.txt").write_text(HORIZONTAL_FINAL_TEXT, encoding="utf-8")
        identity = {
            "identity_schema_version": 1,
            "video_profile": self.PROFILE_ID,
            "video_profile_contract_version": 1,
            "provider_contract_version": 1,
            "provider_task_mapping": {"field": "omni_reference_task_type", "value": "reference"},
            "storyboard_aspect": "horizontal",
            "visual_style": "3d-cg",
            "visual_style_preset": "realistic-material-restrained-anime-outline",
            "visual_style_preset_version": 1,
            "visual_style_preset_sha256": "1" * 64,
            "project_pack_id": "dandao-xiantu",
            "project_pack_version": 1,
            "project_pack_sha256": "2" * 64,
            "generator_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-generator",
            "reviewer_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
            "workflow_audit": {"schema_version": 1, "files": []},
            "resolved_workflow_hash": "3" * 64,
        }
        write_json(
            episode_dir / "episode.json",
            {
                "episode_id": "ep01",
                "series_title": "丹道仙途",
                "video_profile": self.PROFILE_ID,
                "video_profile_contract_version": 1,
                "provider_contract_version": 1,
                "provider_task_mapping": {"field": "omni_reference_task_type", "value": "reference"},
                "video_resolution": "720p",
                "video_aspect_ratio": "16:9",
                "video_fps": 24,
                "generate_audio": True,
                "video_task_type": "multimodal_generation",
                "reviewer_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
            },
        )
        write_json(
            episode_dir / "storyboard_index.json",
            {
                "schema_version": 2,
                "workflow_identity": identity,
                "project": "丹道仙途",
                "episode_id": "EP01",
                "source_hashes": {"final_txt_sha256": handoff.sha256_file(episode_dir / "final.txt")},
                "cuts": [
                    {
                        "cut_id": "EP01-G01",
                        "group_index": 1,
                        "title": "门口确认",
                        "scene": ["客厅，白天"],
                        "characters": ["甲"],
                        "props": ["钥匙"],
                        "duration_sec": 8,
                    }
                ],
            },
        )
        write_json(
            episode_dir / "asset_bindings.json",
            {
                "project": "丹道仙途",
                "episode_id": "EP01",
                "workflow_identity": identity,
                "bindings": [
                    {
                        "binding_id": "EP01_BIND_001",
                        "cut_id": "EP01-G01",
                        "asset_id": "PROP_YUANDING_BASE",
                        "state_id": "yuanding_alchemy_active",
                        "asset_type": "prop",
                        "binding_role": "prop_reference",
                        "reference_priority": "primary",
                        "use_for_video": "yes",
                        "required_for_generation": "yes",
                        "source": "asset_bible",
                        "note": "元鼎结构与炼丹激活态",
                    }
                ],
            },
        )
        return episode_dir

    def activate_material(self, episode_dir: Path, *, authorization: str = "confirmed") -> None:
        requirements_path, local_path = handoff.export_material_handoff(episode_dir)
        material_path = episode_dir / "materials/yuanding.png"
        material_path.parent.mkdir()
        material_path.write_bytes(b"stable-yuanding-reference")
        file_hash = handoff.sha256_file(material_path)
        local_payload = json.loads(local_path.read_text(encoding="utf-8"))
        local_payload["materials"][0].update(
            {
                "source": {"kind": "local_file", "path": "materials/yuanding.png"},
                "mime_type": "image/png",
                "sha256": file_hash,
                "authorization": {"status": authorization, "note": "测试素材"},
            }
        )
        write_json(local_path, local_payload)
        write_json(
            episode_dir / handoff.ARK_SYNC_RESULTS_FILE,
            {
                "schema_version": 2,
                "authority": "manjuweb",
                "profile": self.PROFILE_ID,
                "project": "丹道仙途",
                "episode_id": "EP01",
                "source_hashes": {
                    "material_requirements_sha256": handoff.sha256_file(requirements_path),
                    "local_materials_sha256": handoff.sha256_file(local_path),
                },
                "materials": [
                    {
                        "material_key": "yuanding_alchemy_active",
                        "media_type": "image",
                        "sha256": file_hash,
                        "ark_asset_id": "asset://asset-yuanding-contract-test",
                        "ark_status": "active",
                    }
                ],
            },
        )

    def mark_storyboard_and_assets_valid(self, episode_dir: Path) -> None:
        audit_keys = handoff.HORIZONTAL_REVIEW_COVERAGE_KEYS
        (episode_dir / "script.txt").write_text("甲抬起钥匙确认。\n", encoding="utf-8")
        write_json(
            episode_dir / "review.txt",
            {
                "pass": True,
                "summary": "逐项对照 script 与 final 完成审核",
                "source_status": "available",
                "checked_groups": ["第1组"],
                "audit_coverage": {key: "checked" for key in audit_keys},
                "spot_checks": [
                    {"group": "EP01-G01", "type": "script_fidelity", "evidence": "对白与动作一致"},
                    {"group": "EP01-G01", "type": "timing_math", "evidence": "4秒整数时间轴"},
                    {"group": "EP01-G01", "type": "native_audio", "evidence": "声源与动作对应"},
                ],
                "semantic_checks": [
                    {
                        "group": "EP01-G01", "type": "script_fidelity", "result": "pass",
                        "evidence": "钥匙动作和末态完整", "fix_instruction": "无需修复",
                    },
                    {
                        "group": "EP01-G01", "type": "horizontal_composition", "result": "pass",
                        "evidence": "人物、门与钥匙的横屏关系明确", "fix_instruction": "无需修复",
                    },
                    {
                        "group": "EP01-G01", "type": "native_audio", "result": "pass",
                        "evidence": "钥匙拟音与抬手动作同步", "fix_instruction": "无需修复",
                    },
                ],
                "issues": [],
                "warnings": [],
            },
        )
        write_json(
            episode_dir / "status.json",
            {
                "status": "done",
                "reviewer_source": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
                "reviewer_pass": True,
                "reviewer_issues_count": 0,
                "reviewer_warnings_count": 0,
            },
        )
        write_json(
            episode_dir / "asset_status.json",
            {
                "status": "done",
                "reviewer_source": "asset-reviewer",
                "reviewer_pass": True,
                "reviewer_issues_count": 0,
                "reviewer_warnings_count": 0,
            },
        )
        (episode_dir / "assets.md").write_text("# Assets\n\n元鼎基础资产\n", encoding="utf-8")
        (episode_dir / "assets.xlsx").write_bytes(b"test-workbook-contract")
        write_json(
            episode_dir / "asset_review.json",
            {"pass": True, "issues": [], "warnings": [], "summary": "逐项审核通过"},
        )
        validator_path = ROOT / "agent_skills/asset-extractor/scripts/validate-assets.mjs"
        write_json(
            episode_dir / "asset_validation.json",
            {
                "schema_version": 1,
                "validator": "validate-assets.mjs",
                "validator_sha256": handoff.sha256_file(validator_path),
                "valid": True,
                "source_hashes": {
                    "final_sha256": handoff.sha256_file(episode_dir / "final.txt"),
                    "assets_sha256": handoff.sha256_file(episode_dir / "assets.md"),
                    "workbook_sha256": handoff.sha256_file(episode_dir / "assets.xlsx"),
                    "storyboardIndex_sha256": handoff.sha256_file(episode_dir / "storyboard_index.json"),
                    "review_sha256": handoff.sha256_file(episode_dir / "asset_review.json"),
                    "bindings_sha256": handoff.sha256_file(episode_dir / "asset_bindings.json"),
                    "status_sha256": handoff.sha256_file(episode_dir / "asset_status.json"),
                },
                "issues": [],
            },
        )

    def test_v2_serializes_active_image_video_and_audio_with_provider_roles(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            bindings_path = episode_dir / "asset_bindings.json"
            bindings = json.loads(bindings_path.read_text(encoding="utf-8"))
            bindings["bindings"].extend(
                [
                    {
                        **bindings["bindings"][0],
                        "binding_id": "EP01_BIND_002",
                        "asset_id": "REF_ALCHEMY_MOTION",
                        "state_id": "BASE",
                        "media_type": "video",
                        "binding_role": "composition_reference",
                        "note": "炼丹动作与运镜参考",
                    },
                    {
                        **bindings["bindings"][0],
                        "binding_id": "EP01_BIND_003",
                        "asset_id": "REF_FURNACE_AUDIO",
                        "state_id": "BASE",
                        "media_type": "audio",
                        "binding_role": "composition_reference",
                        "note": "炉火与鼎鸣声音参考",
                    },
                ]
            )
            write_json(bindings_path, bindings)
            requirements_path, local_path = handoff.export_material_handoff(episode_dir)
            local = json.loads(local_path.read_text(encoding="utf-8"))
            material_specs = {
                ("yuanding_alchemy_active", "image"): ("materials/yuanding.png", "image/png", b"image-ref"),
                ("REF_ALCHEMY_MOTION", "video"): ("materials/alchemy.mp4", "video/mp4", b"video-ref"),
                ("REF_FURNACE_AUDIO", "audio"): ("materials/furnace.wav", "audio/wav", b"audio-ref"),
            }
            sync_materials = []
            for item in local["materials"]:
                key = (item["material_key"], item["media_type"])
                relative, mime, content = material_specs[key]
                file_path = episode_dir / relative
                file_path.parent.mkdir(exist_ok=True)
                file_path.write_bytes(content)
                digest = handoff.sha256_file(file_path)
                item.update(
                    {
                        "source": {"kind": "local_file", "path": relative},
                        "mime_type": mime,
                        "sha256": digest,
                        "authorization": {"status": "confirmed", "note": "测试素材"},
                    }
                )
                sync_materials.append(
                    {
                        "material_key": item["material_key"],
                        "media_type": item["media_type"],
                        "sha256": digest,
                        "ark_asset_id": f"asset://asset-{item['media_type']}-contract-test",
                        "ark_status": "active",
                    }
                )
            write_json(local_path, local)
            write_json(
                episode_dir / handoff.ARK_SYNC_RESULTS_FILE,
                {
                    "schema_version": 2,
                    "authority": "manjuweb",
                    "profile": self.PROFILE_ID,
                    "project": "丹道仙途",
                    "episode_id": "EP01",
                    "source_hashes": {
                        "material_requirements_sha256": handoff.sha256_file(requirements_path),
                        "local_materials_sha256": handoff.sha256_file(local_path),
                    },
                    "materials": sync_materials,
                },
            )
            self.mark_storyboard_and_assets_valid(episode_dir)

            package = handoff.build_generation_package(episode_dir)

            self.assertTrue(package["generation_ready"], package["blocking_issues"])
            references = package["cuts"][0]["provider_request"]["content"][1:]
            self.assertEqual(
                {(item["type"], item["role"]) for item in references},
                {
                    ("image_url", "reference_image"),
                    ("video_url", "reference_video"),
                    ("audio_url", "reference_audio"),
                },
            )

    def test_v2_schema_can_be_valid_before_materials_are_active(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            handoff.export_material_handoff(episode_dir)

            validation = handoff.validate_material_handoff(episode_dir)

            self.assertTrue(validation["handoff_schema_valid"], validation["issues"])
            self.assertFalse(validation["generation_ready"])
            self.assertIn("missing ark_sync_results.json", validation["generation_blockers"])

    def test_v2_serializes_provider_reference_request_without_internal_fields(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            self.activate_material(episode_dir)
            self.mark_storyboard_and_assets_valid(episode_dir)

            package = handoff.build_generation_package(episode_dir)

            self.assertEqual(package["schema_version"], 2)
            self.assertEqual(package["profile"], self.PROFILE_ID)
            self.assertTrue(package["handoff_schema_valid"], package["blocking_issues"])
            self.assertTrue(package["generation_ready"], package["blocking_issues"])
            self.assertFalse(package["submit_allowed"])
            self.assertIn("ManJuWeb consumer contract", " ".join(package["submission_blockers"]))
            self.assertEqual(package["workflow_identity"]["project_pack_id"], "dandao-xiantu")
            self.assertTrue(package["readiness"]["layers"]["storyboard_valid"]["valid"])
            self.assertTrue(package["readiness"]["layers"]["asset_contract_valid"]["valid"])
            self.assertTrue(package["readiness"]["layers"]["handoff_schema_valid"]["valid"])
            self.assertTrue(package["readiness"]["layers"]["generation_ready"]["valid"])
            self.assertFalse(package["readiness"]["layers"]["submit_allowed"]["valid"])

            request = package["cuts"][0]["provider_request"]
            self.assertEqual(request["model"], handoff.MODEL_ID)
            self.assertEqual(request["omni_reference_task_type"], "reference")
            self.assertEqual(request["ratio"], "16:9")
            self.assertEqual(request["resolution"], "720p")
            self.assertEqual(request["duration"], 8)
            self.assertIs(request["generate_audio"], True)
            self.assertNotIn("fps", request)
            self.assertNotIn("video_task_type", request)
            self.assertEqual(request["content"][0]["type"], "text")
            self.assertEqual(request["content"][1]["role"], "reference_image")
            self.assertEqual(
                request["content"][1]["image_url"]["url"],
                "asset://asset-yuanding-contract-test",
            )

            prompt = package["cuts"][0]["submission_prompt"]
            self.assertEqual(request["content"][0]["text"], prompt)
            self.assertTrue(prompt.startswith("【人物资产】"))
            self.assertLess(prompt.index("【人物资产】"), prompt.index("【场景资产】"))
            self.assertLess(prompt.index("【场景资产】"), prompt.index("【道具与关键视觉资产】"))
            self.assertIn("【整体画风说明】", prompt)
            self.assertIn("写实材质＋克制卡通轮廓", prompt)
            self.assertIn("【组间空间衔接】", prompt)
            self.assertIn("【连续时间轴】", prompt)
            self.assertIn("0-4秒", prompt)
            self.assertNotIn("一句话概述", prompt)
            self.assertNotIn("【视觉峰值与特效重点】", prompt)
            self.assertNotIn("【特效、运镜与原生音频执行】", prompt)
            self.assertNotIn("运镜强化词", prompt)
            self.assertNotIn("Seedance执行提示补充", prompt)
            material = package["cuts"][0]["material_inputs"][0]
            self.assertEqual(material["reference_token"], "@图片1")
            self.assertEqual(material["asset_type"], "prop")
            self.assertEqual(material["source_binding_role"], "prop_reference")

    def test_submission_prompt_groups_all_asset_types_and_keeps_vfx_semantics(self):
        prompt = handoff.build_submission_prompt(
            HORIZONTAL_FINAL_TEXT,
            [
                {
                    "reference_token": "@图片1",
                    "material_key": "CHAR_A_BASE",
                    "asset_type": "character",
                    "source_binding_role": "character_reference",
                    "note": "甲的人物资产",
                    "provides": ["face", "hair", "body_identity"],
                    "excludes": ["wardrobe", "action", "camera_motion"],
                },
                {
                    "reference_token": "@图片2",
                    "material_key": "SCENE_ROOM_BASE",
                    "asset_type": "scene",
                    "source_binding_role": "scene_reference",
                    "note": "炼丹厢房空镜",
                    "provides": ["space_layout", "materials", "lighting_state"],
                    "excludes": ["character_identity", "action", "camera_motion"],
                },
                {
                    "reference_token": "@图片3",
                    "material_key": "PROP_YUANDING_BASE",
                    "asset_type": "prop",
                    "source_binding_role": "prop_reference",
                    "note": "元鼎激活态",
                    "provides": ["appearance", "material", "condition"],
                    "excludes": ["character_identity", "action", "camera_motion"],
                },
            ],
            duration=8,
        )
        self.assertTrue(prompt.startswith("【人物资产】"))
        self.assertLess(prompt.index("@图片1"), prompt.index("【整体画风说明】"))
        self.assertLess(prompt.index("【整体画风说明】"), prompt.index("【组间空间衔接】"))
        self.assertIn("只参考脸型、发型、体态与身份稳定特征", prompt)
        self.assertIn("来源→形态→路径→作用对象→反馈→收束→声音", prompt)
        self.assertIn("0-4秒", prompt)
        self.assertIn("4-8秒", prompt)
        self.assertNotIn("一句话概述", prompt)
        self.assertNotIn("视觉峰值与特效重点", prompt)
        self.assertNotIn("特效、运镜与原生音频执行", prompt)

    def test_unconfirmed_authorization_allows_local_generation_shape_but_never_submission(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            self.activate_material(episode_dir, authorization="unconfirmed")
            self.mark_storyboard_and_assets_valid(episode_dir)

            package = handoff.build_generation_package(episode_dir)

            self.assertTrue(package["generation_ready"], package["blocking_issues"])
            self.assertFalse(package["submit_allowed"])
            self.assertTrue(any("authorization" in issue for issue in package["submission_blockers"]))

    def test_untrusted_consumer_evidence_file_cannot_unblock_submission(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            self.activate_material(episode_dir)
            self.mark_storyboard_and_assets_valid(episode_dir)
            write_json(
                episode_dir / "manjuweb_consumer_evidence.json",
                {
                    "authenticated": True,
                    "nonce": "replayed-user-authored-value",
                    "submit_allowed": True,
                },
            )

            package = handoff.build_generation_package(episode_dir)

            self.assertTrue(package["generation_ready"])
            self.assertFalse(package["submit_allowed"])
            self.assertTrue(any("Unit 6B" in issue for issue in package["submission_blockers"]))

    def test_v2_rejects_non_integer_or_out_of_range_duration(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            index_path = episode_dir / "storyboard_index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["cuts"][0]["duration_sec"] = 4.5
            write_json(index_path, index)
            handoff.export_material_handoff(episode_dir)

            validation = handoff.validate_material_handoff(episode_dir)

            self.assertFalse(validation["handoff_schema_valid"])
            self.assertTrue(any("integer" in issue for issue in validation["schema_blockers"]))

    def test_readiness_layers_report_first_blocker_without_claiming_workflow_validation(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            handoff.export_material_handoff(episode_dir)

            readiness = handoff.summarize_workflow_readiness(episode_dir)

            self.assertFalse(readiness["layers"]["storyboard_valid"]["valid"])
            self.assertFalse(readiness["layers"]["asset_contract_valid"]["valid"])
            self.assertTrue(readiness["layers"]["handoff_schema_valid"]["valid"])
            self.assertFalse(readiness["layers"]["generation_ready"]["valid"])
            self.assertFalse(readiness["layers"]["submit_allowed"]["valid"])
            self.assertEqual(readiness["first_blocker"]["layer"], "storyboard_valid")
            self.assertFalse(readiness["workflow_validated"])

    def test_machine_and_human_readiness_reports_share_the_same_state(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            handoff.export_material_handoff(episode_dir)

            json_path, report_path = handoff.write_workflow_readiness(episode_dir)

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            report = report_path.read_text(encoding="utf-8")
            self.assertEqual(payload["first_blocker"]["layer"], "storyboard_valid")
            for name, layer in payload["layers"].items():
                self.assertIn(f"{name}: `{layer['state']}`", report)
            self.assertIn(payload["first_blocker"]["reason"], report)


if __name__ == "__main__":
    unittest.main()
