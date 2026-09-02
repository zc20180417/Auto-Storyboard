import hashlib
import json
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "agent_skills/asset-extractor/scripts/validate-assets.mjs"
CONVERTER = ROOT / "agent_skills/asset-extractor/scripts/assets-md-to-xlsx.mjs"
PRODUCER_SPECS = (
    ("asset_extractor_skill", "agent_skills/asset-extractor/SKILL.md"),
    ("asset_reviewer_skill", "agent_skills/asset-reviewer/SKILL.md"),
    ("asset_converter", "agent_skills/asset-extractor/scripts/assets-md-to-xlsx.mjs"),
    ("asset_validator", "agent_skills/asset-extractor/scripts/validate-assets.mjs"),
)


FINAL_TEXT = """=== [cut_id: EP01-G01] 第1组：丹房（总时长：4秒，镜头数：1） ===

**人物：** 方平
**场景：** 炼丹房，夜
**道具：** 元鼎

**镜头1：固定中景（0-4秒）**

0-4秒：方平守在元鼎前。

=== 第1组结束 ===
"""


ASSETS_MD = """# 《丹道仙途 ep01》资产增量与使用索引

## 一、本集复用资产索引
| 使用ID | episode_id | cut_ids | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|---|---|
| EP01_USE_SCENE_001 | EP01 | EP01-G01 | SCENE_DANFANG_BASE | BASE | scene | asset_bible | 第1组 | 主场景 | no | 已有 |

## 二、本集新增资产状态
| state_id | episode_id | cut_ids | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 三、本集新增基础资产
| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|

## 四、本集关键道具与场景状态
| state_id | episode_id | cut_ids | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|---|---|

## 五、本集不建议入库元素
| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 短暂站立动作 | 第1组 | 属于表演动作 |

## 六、本集分镜资产绑定索引
| binding_id | episode_id | cut_id | asset_id | state_id | asset_type | binding_role | reference_priority | use_for_video | required_for_generation | source | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EP01_BIND_001 | EP01 | EP01-G01 | SCENE_DANFANG_BASE | BASE | scene | scene_reference | primary | yes | yes | asset_bible | 主场景 |
"""


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def workflow_identity() -> dict:
    audit_path = "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md"
    identity = {
        "identity_schema_version": 1,
        "video_profile": "seedance-2.5-horizontal-xianxia-3d-cg",
        "video_profile_contract_version": 1,
        "provider_contract_version": 1,
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
        "workflow_audit": {
            "schema_version": 1,
            "files": [
                {
                    "role": "profile_skill",
                    "path": audit_path,
                    "sha256": sha256_bytes((ROOT / audit_path).read_bytes()),
                }
            ],
        },
    }
    canonical = json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    identity["resolved_workflow_hash"] = sha256_bytes(canonical.encode("utf-8"))
    return identity


def asset_evidence(episode_dir: Path, index_path: Path) -> dict:
    evidence = {
        "asset_evidence_schema_version": 1,
        "asset_contract_version": 2,
        "source_hashes": {
            "final_txt_sha256": sha256_bytes((episode_dir / "final.txt").read_bytes()),
            "storyboard_index_sha256": sha256_bytes(index_path.read_bytes()),
            "assets_md_sha256": sha256_bytes((episode_dir / "assets.md").read_bytes()),
        },
        "producer_files": [
            {
                "role": role,
                "path": relative,
                "sha256": sha256_bytes((ROOT / relative).read_bytes()),
            }
            for role, relative in PRODUCER_SPECS
        ],
    }
    canonical = json.dumps(evidence, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    evidence["asset_evidence_hash"] = sha256_bytes(canonical.encode("utf-8"))
    return evidence


class AssetIdentityContractTests(unittest.TestCase):
    def make_episode(self, base: Path, *, with_identity: bool = True) -> Path:
        episode_dir = base / "episodes/ep01"
        episode_dir.mkdir(parents=True)
        (episode_dir / "final.txt").write_text(FINAL_TEXT, encoding="utf-8")
        (episode_dir / "assets.md").write_text(ASSETS_MD, encoding="utf-8")
        (episode_dir / "assets.xlsx").write_bytes(b"contract-fixture")
        identity = workflow_identity()
        index = {
            "project": "丹道仙途",
            "episode_id": "EP01",
            "source_hashes": {"final_txt_sha256": sha256_bytes((episode_dir / "final.txt").read_bytes())},
            "cuts": [{"cut_id": "EP01-G01", "group_index": 1, "title": "丹房", "duration_sec": 4}],
        }
        if with_identity:
            index.update({"schema_version": 2, "workflow_identity": identity})
            write_json(
                episode_dir / "episode.json",
                {
                    "video_profile": identity["video_profile"],
                    "video_profile_contract_version": identity["video_profile_contract_version"],
                    "provider_contract_version": identity["provider_contract_version"],
                    "storyboard_aspect": identity["storyboard_aspect"],
                    "visual_style": identity["visual_style"],
                    "visual_style_preset": identity["visual_style_preset"],
                    "visual_style_preset_version": identity["visual_style_preset_version"],
                    "visual_style_preset_sha256": identity["visual_style_preset_sha256"],
                    "project_pack_id": identity["project_pack_id"],
                    "project_pack_version": identity["project_pack_version"],
                    "project_pack_sha256": identity["project_pack_sha256"],
                    "generator_skill_name": identity["generator_skill_name"],
                    "reviewer_skill_name": identity["reviewer_skill_name"],
                },
            )
        index_path = episode_dir / "storyboard_index.json"
        write_json(index_path, index)
        evidence = asset_evidence(episode_dir, index_path)
        bindings = {
            "project": "丹道仙途",
            "episode_id": "EP01",
            "bindings": [
                {
                    "binding_id": "EP01_BIND_001",
                    "cut_id": "EP01-G01",
                    "asset_id": "SCENE_DANFANG_BASE",
                    "state_id": "BASE",
                    "asset_type": "scene",
                    "binding_role": "scene_reference",
                    "reference_priority": "primary",
                    "use_for_video": "yes",
                    "required_for_generation": "yes",
                    "source": "asset_bible",
                    "note": "主场景",
                }
            ],
        }
        status = {
            "status": "done",
            "reviewer_source": "asset-reviewer",
            "reviewer_pass": True,
            "reviewer_issues_count": 0,
            "reviewer_warnings_count": 0,
            "hard_issues_remaining": [],
            "bible_update_candidates": [],
        }
        if with_identity:
            bindings.update({"workflow_identity": identity, "asset_evidence": evidence})
            status.update({"workflow_identity": identity, "asset_evidence": evidence})
        write_json(episode_dir / "asset_bindings.json", bindings)
        write_json(episode_dir / "asset_status.json", status)
        review = {
            "pass": True,
            "issues": [],
            "warnings": [],
            "checked_tables": [
                "本集复用资产索引", "本集新增资产状态", "本集新增基础资产",
                "本集关键道具与场景状态", "本集不建议入库元素", "本集分镜资产绑定索引",
            ],
            "audit_coverage": {
                key: "checked"
                for key in (
                    "asset_coverage", "asset_selection", "bible_consistency", "registry_structure",
                    "duplicate_control", "state_modeling", "category_boundary", "prompt_fidelity",
                    "bilingual_consistency", "time_range_accuracy", "cut_binding_accuracy",
                    "binding_completeness", "video_reference_readiness", "visual_style_consistency", "xlsx_readiness",
                    "workflow_identity_consistency",
                )
            },
            "spot_checks": [{"table": "a", "type": "a", "evidence": "a"}] * 3,
            "semantic_checks": [
                {"table": "a", "type": check_type, "result": "pass", "evidence": "已核对", "fix_instruction": "无"}
                for check_type in (
                    "unnecessary_regeneration", "state_should_be_variant", "bible_conflict",
                    "prompt_hallucination", "time_range_error", "cut_id_not_found", "unnecessary_video_reference",
                )
            ],
        }
        write_json(episode_dir / "asset_review.json", review)
        return episode_dir

    def validate(self, episode_dir: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["node", str(VALIDATOR), str(episode_dir)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            encoding="utf-8",
        )

    def test_new_index_requires_matching_identity_and_current_asset_evidence(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            result = self.validate(episode_dir)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            validation = json.loads((episode_dir / "asset_validation.json").read_text(encoding="utf-8"))
            self.assertTrue(validation["valid"])
            self.assertRegex(validation["validator_sha256"], r"^[0-9a-f]{64}$")

    def test_converter_copies_index_identity_and_deterministic_asset_evidence(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            result = subprocess.run(
                [
                    "node",
                    str(CONVERTER),
                    str(episode_dir / "assets.md"),
                    str(episode_dir / "assets.xlsx"),
                    "--mode=episode",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            index = json.loads((episode_dir / "storyboard_index.json").read_text(encoding="utf-8"))
            bindings = json.loads((episode_dir / "asset_bindings.json").read_text(encoding="utf-8"))
            status = json.loads((episode_dir / "asset_status.json").read_text(encoding="utf-8"))
            self.assertEqual(bindings["workflow_identity"], index["workflow_identity"])
            self.assertEqual(status["workflow_identity"], index["workflow_identity"])
            self.assertEqual(status["asset_evidence"], bindings["asset_evidence"])
            self.assertRegex(bindings["asset_evidence"]["asset_evidence_hash"], r"^[0-9a-f]{64}$")
            self.assertEqual(self.validate(episode_dir).returncode, 0)

    def test_identity_tampering_and_source_staleness_fail_closed(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp))
            bindings_path = episode_dir / "asset_bindings.json"
            bindings = json.loads(bindings_path.read_text(encoding="utf-8"))
            bindings["workflow_identity"]["project_pack_version"] = 99
            write_json(bindings_path, bindings)
            tampered = self.validate(episode_dir)
            self.assertNotEqual(tampered.returncode, 0)
            self.assertIn("workflow_identity", tampered.stderr)

            episode_dir = self.make_episode(Path(tmp) / "fresh")
            (episode_dir / "final.txt").write_text(FINAL_TEXT + "\n变化", encoding="utf-8")
            stale = self.validate(episode_dir)
            self.assertNotEqual(stale.returncode, 0)
            self.assertIn("stale", stale.stderr)

    def test_legacy_index_does_not_require_v2_asset_identity(self):
        with TemporaryDirectory() as tmp:
            episode_dir = self.make_episode(Path(tmp), with_identity=False)
            result = self.validate(episode_dir)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
