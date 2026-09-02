import copy
import hashlib
import json
import subprocess
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import seedance_probe_evidence as probe


FIXTURES = ROOT / "tests/fixtures/dandao-xiantu"
PROTOCOL = ROOT / "tests/fixtures/seedance25/probe-evidence/protocol-contract-v1.json"
RUBRIC = ROOT / "tests/fixtures/seedance25/probe-evidence/qa-rubric-v1.json"
TRUSTED_VERIFIER = lambda attempt: True


def canonical_hash(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def valid_attempt(category: str, episode_id: str, attempt_number: int = 1) -> dict:
    now = datetime(2026, 9, 1, 4, 0, tzinfo=timezone.utc)
    dependency_snapshot = {
        "resolved_workflow_hash": "1" * 64,
        "package_sha256": "2" * 64,
        "request_sha256": "3" * 64,
        "materials_sha256": "4" * 64,
        "provider_contract_version": 1,
        "manjuweb_schema_version": 2,
        "protocol_sha256": hashlib.sha256(PROTOCOL.read_bytes()).hexdigest(),
        "rubric_sha256": hashlib.sha256(RUBRIC.read_bytes()).hexdigest(),
        "provenance_sha256": hashlib.sha256((FIXTURES / "provenance.json").read_bytes()).hexdigest(),
        "episode_fixture_sha256": hashlib.sha256(
            (FIXTURES / f"ep{episode_id[-3:]}.txt").read_bytes()
        ).hexdigest(),
    }
    category_checks = {
        "ordinary-alchemy": ["alchemy_state_chain"],
        "failed-alchemy-rewind": ["rewind_five_stage_chain", "rewind_boundary"],
        "yuanding-ability-reveal": ["yuanding_revival_state", "ability_scope_unchanged"],
    }
    common = [
        "character_face_identity",
        "yuanding_geometry_scale",
        "material_style_stability",
        "horizontal_action_readability",
        "dialogue_lipsync_object",
        "native_audio_source_peak",
    ]
    checks = []
    for check_id in common + category_checks[category]:
        checks.append(
            {
                "check_id": check_id,
                "required": True,
                "result": "pass",
                "time_range": "0.0-4.0s",
                "observation": f"直接观察到 {check_id} 符合冻结标准",
                "threshold": "无结构漂移、无越界、声画峰值同帧",
                "material_refs": [{"material_key": "PROP_YUANDING_BASE", "sha256": "4" * 64}],
                "rubric_version": "dandao-xiantu-alchemy-probe-v1",
                "reviewer": {"id": "reviewer-pseudonym", "role": "probe_reviewer"},
                "reviewed_at": now.isoformat(),
                "result_media_sha256": "5" * 64,
            }
        )
    attempt = {
        "schema_version": 1,
        "attempt_id": f"attempt-{attempt_number:02d}",
        "attempt_number": attempt_number,
        "category": category,
        "episode_id": episode_id,
        "state": "accepted",
        "validation_batch": {
            "batch_id": "batch-20260901-a",
            "registered_at": (now - timedelta(hours=1)).isoformat(),
            "max_attempts_per_category": 2,
            "max_total_cost_units": 6,
            "timeout_seconds": 900,
            "stop_conditions": ["budget_exhausted", "accepted", "authorization_revoked"],
        },
        "actual_cost_units": 1,
        "dependencies": dependency_snapshot,
        "dependency_hash": canonical_hash(dependency_snapshot),
        "external_authenticity": {
            "authority": "manjuweb",
            "authenticated": True,
            "signature_valid": True,
            "nonce": f"nonce-{category}-{attempt_number}",
            "request_digest": "3" * 64,
            "environment": {
                "region": "cn-beijing",
                "model": "doubao-seedance-2-5-260628",
                "account_pseudonym": "acct-test-a",
                "consumer_deployment_id": "manjuweb-test-v1",
                "consumer_contract_id": "seedance25-v2",
                "observed_at": now.isoformat(),
                "expires_at": (now + timedelta(hours=24)).isoformat(),
            },
            "task_id": f"task-redacted-{category}-{attempt_number}",
        },
        "result_media": {
            "locator": f"controlled://seedance-probes/{category}/attempt-{attempt_number:02d}.mp4",
            "sha256": "5" * 64,
            "byte_count": 1024,
            "mime_type": "video/mp4",
            "downloaded_at": now.isoformat(),
        },
        "mechanical_qa": {
            "decoded": True,
            "width": 1280,
            "height": 720,
            "ratio": "16:9",
            "duration_seconds": 4,
            "fps": 24,
            "audio_stream": True,
            "validator_version": 1,
            "checked_at": now.isoformat(),
            "result_media_sha256": "5" * 64,
        },
        "material_sufficiency": [
            {
                "dimension": dimension,
                "result": "pass",
                "material_refs": [{"material_key": f"REF_{dimension}", "sha256": "4" * 64}],
                "observable_time_range": "0.0-4.0s",
            }
            for dimension in ("character_face", "yuanding_structure_scale", "costume", "scene", "critical_state")
        ],
        "semantic_qa": {
            "rubric_id": "dandao-xiantu-alchemy-probe-v1",
            "revision": 1,
            "checks": checks,
        },
        "signoff": {
            "decision": "accepted",
            "signer": {"id": "signer-pseudonym", "role": "probe_signer"},
            "authority_source": "validation-batch-approval",
            "decided_at": now.isoformat(),
            "rubric_version": "dandao-xiantu-alchemy-probe-v1",
            "reason": "全部 required QA pass",
            "result_media_sha256": "5" * 64,
        },
        "retention": {
            "classification": "controlled-validation-media",
            "rights_holder": "project-owner-pseudonym",
            "allowed_model_use": "seedance-validation-only",
            "retention_until": "2026-12-01T00:00:00+00:00",
            "access_roles": ["run_owner", "probe_reviewer", "probe_signer"],
            "deletion_owner": "run_owner",
        },
        "transition_audit": [
            {"from": None, "to": "prepared", "actor": {"id": "operator", "role": "operator"}, "at": now.isoformat()},
            {"from": "prepared", "to": "submitted", "actor": {"id": "manju", "role": "manjuweb"}, "at": now.isoformat()},
            {"from": "submitted", "to": "provider_running", "actor": {"id": "manju", "role": "manjuweb"}, "at": now.isoformat()},
            {"from": "provider_running", "to": "download_pending", "actor": {"id": "manju", "role": "manjuweb"}, "at": now.isoformat()},
            {"from": "download_pending", "to": "semantic_qa_pending", "actor": {"id": "media", "role": "media_validator"}, "at": now.isoformat()},
            {"from": "semantic_qa_pending", "to": "signoff_pending", "actor": {"id": "reviewer", "role": "probe_reviewer"}, "at": now.isoformat()},
            {"from": "signoff_pending", "to": "accepted", "actor": {"id": "signer", "role": "probe_signer"}, "at": now.isoformat()},
        ],
    }
    attempt["validation_batch_hash"] = canonical_hash(attempt["validation_batch"])
    return attempt


class ProbeFixtureProvenanceTests(unittest.TestCase):
    def test_repository_episode_fixtures_are_complete_and_hash_bound(self):
        result = probe.validate_fixture_provenance(FIXTURES / "provenance.json")
        self.assertTrue(result["valid"], result["issues"])
        self.assertEqual(result["episode_ids"], ["EP003", "EP005", "EP028"])
        self.assertTrue(result["source_file_verified"])

    def test_fixture_hash_drift_duplicate_or_overlap_fails_closed(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for path in FIXTURES.iterdir():
                (tmp_path / path.name).write_bytes(path.read_bytes())
            (tmp_path / "ep003.txt").write_text("第003集《场景摘录》\n场3-3\n", encoding="utf-8")
            drift = probe.validate_fixture_provenance(tmp_path / "provenance.json")
            self.assertFalse(drift["valid"])
            self.assertTrue(any("sha256" in issue or "line_count" in issue for issue in drift["issues"]))

            provenance = json.loads((FIXTURES / "provenance.json").read_text(encoding="utf-8"))
            provenance["episodes"][1]["episode_id"] = "EP003"
            provenance["episodes"][1]["start_line"] = 100
            provenance["episodes"][1]["end_line"] = 140
            (tmp_path / "provenance.json").write_text(json.dumps(provenance), encoding="utf-8")
            duplicate = probe.validate_fixture_provenance(tmp_path / "provenance.json")
            self.assertFalse(duplicate["valid"])
            self.assertTrue(any("duplicate" in issue or "overlap" in issue for issue in duplicate["issues"]))

    def test_optional_raw_source_verification_detects_source_hash_drift(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.txt"
            source.write_text("第005集《测试》\n正文\n第006集《下一集》\n", encoding="utf-8")
            fixture = tmp_path / "ep001.txt"
            fixture.write_text("第005集《测试》\n正文\n", encoding="utf-8")
            source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
            fixture_hash = hashlib.sha256(fixture.read_bytes()).hexdigest()
            provenance = {
                "schema_version": 1,
                "extraction_contract_version": 1,
                "source": {"logical_name": "source.txt", "sha256": source_hash, "line_count": 3},
                "episodes": [
                    {
                        "episode_id": "EP005", "fixture": "ep001.txt", "title_heading": "第005集《测试》",
                        "start_line": 1, "end_line": 2, "next_episode_heading_line": 3,
                        "line_count": 2, "byte_count": fixture.stat().st_size, "sha256": fixture_hash,
                        "target_scene": "正文", "probe_category": "ordinary-alchemy", "observable_scope": "测试"
                    }
                ],
            }
            provenance_path = tmp_path / "provenance.json"
            provenance_path.write_text(json.dumps(provenance), encoding="utf-8")
            self.assertTrue(probe.validate_fixture_provenance(
                provenance_path, source_path=source, require_complete_probe_set=False
            )["valid"])
            source.write_text("已变化", encoding="utf-8")
            result = probe.validate_fixture_provenance(
                provenance_path, source_path=source, require_complete_probe_set=False
            )
            self.assertFalse(result["valid"])
            self.assertTrue(any("source sha256" in issue for issue in result["issues"]))

    def test_self_consistent_scene_fragment_cannot_claim_complete_episode(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            fixture = tmp_path / "ep005.txt"
            fixture.write_text("第005集《片段》\n场5-5\n正文\n", encoding="utf-8")
            content = fixture.read_bytes()
            provenance = {
                "schema_version": 1,
                "extraction_contract_version": 1,
                "source": {"logical_name": "fake.txt", "sha256": "a" * 64, "line_count": 3},
                "episodes": [{
                    "episode_id": "EP005", "fixture": "ep005.txt", "title_heading": "第005集《片段》",
                    "start_line": 1, "end_line": 3, "next_episode_heading_line": 4,
                    "line_count": 3, "byte_count": len(content), "sha256": hashlib.sha256(content).hexdigest(),
                    "target_scene": "场5-5", "probe_category": "ordinary-alchemy", "observable_scope": "片段"
                }],
            }
            provenance_path = tmp_path / "provenance.json"
            provenance_path.write_text(json.dumps(provenance), encoding="utf-8")
            result = probe.validate_fixture_provenance(provenance_path)
            self.assertFalse(result["valid"])
            self.assertFalse(result["source_file_verified"])

    def test_source_verification_rejects_nonblank_truncated_episode_tail(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.txt"
            source.write_text("第005集《测试》\n正文\n被遗漏的本集结尾\n第006集《下一集》\n", encoding="utf-8")
            fixture = tmp_path / "ep005.txt"
            fixture.write_text("第005集《测试》\n正文\n", encoding="utf-8")
            content = fixture.read_bytes()
            provenance = {
                "schema_version": 1, "extraction_contract_version": 1,
                "source": {"logical_name": "source.txt", "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "line_count": 4},
                "episodes": [{
                    "episode_id": "EP005", "fixture": "ep005.txt", "title_heading": "第005集《测试》",
                    "start_line": 1, "end_line": 2, "next_episode_heading_line": 4,
                    "line_count": 2, "byte_count": len(content), "sha256": hashlib.sha256(content).hexdigest(),
                    "target_scene": "正文", "probe_category": "ordinary-alchemy", "observable_scope": "测试",
                }],
            }
            provenance_path = tmp_path / "provenance.json"
            provenance_path.write_text(json.dumps(provenance), encoding="utf-8")
            result = probe.validate_fixture_provenance(
                provenance_path, source_path=source, require_complete_probe_set=False
            )
            self.assertFalse(result["valid"])
            self.assertTrue(any("tail is truncated" in issue for issue in result["issues"]))


class ProbeEvidenceProtocolTests(unittest.TestCase):
    def test_probe_episode_directory_matches_prepare_workspace_numbering(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            expected = run_dir / "episodes" / "ep03"
            expected.mkdir(parents=True)

            self.assertEqual(probe._probe_episode_dir(run_dir, "EP003"), expected)

    def test_probe_status_writes_machine_and_human_reports_from_one_payload(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            write_json = lambda path, payload: path.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            write_json(
                run_dir / "workflow_readiness.json",
                {
                    "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
                    "layers": {"storyboard_valid": {"valid": False, "state": "blocked"}},
                    "first_blocker": {"layer": "storyboard_valid", "reason": "not produced"},
                },
            )
            json_path, report_path, payload = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC
            )
            self.assertTrue(json_path.is_file())
            self.assertTrue(report_path.is_file())
            self.assertFalse(payload["workflow_validated"])
            self.assertTrue(any(
                "trusted ManJuWeb authenticity verifier" in issue
                for issue in payload["blocking_issues"]
            ))
            self.assertIn(payload["claim"], report_path.read_text(encoding="utf-8"))

    def test_run_status_requires_all_three_current_episode_readiness_files(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            for episode_id in ("ep03", "ep05"):
                episode_dir = run_dir / "episodes" / episode_id
                episode_dir.mkdir(parents=True)
                (episode_dir / "workflow_readiness.json").write_text(
                    json.dumps({
                        "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
                        "resolved_workflow_hash": "1" * 64,
                        "layers": {
                            name: {"valid": True, "state": "passed"}
                            for name in (
                                "storyboard_valid", "asset_contract_valid",
                                "handoff_schema_valid", "generation_ready",
                            )
                        },
                    }),
                    encoding="utf-8",
                )

            _, _, payload = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC
            )

            self.assertFalse(payload["workflow_validated"])
            self.assertTrue(any(
                "missing current workflow readiness for yuanding-ability-reveal/EP028" in issue
                for issue in payload["blocking_issues"]
            ))

    def test_run_status_renders_nonempty_category_failure_types(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            category_dir = run_dir / "probes" / "ordinary-alchemy" / "attempt-01"
            category_dir.mkdir(parents=True)
            attempt = valid_attempt("ordinary-alchemy", "EP005")
            (category_dir / "attempt.json").write_text(
                json.dumps(attempt, ensure_ascii=False), encoding="utf-8"
            )
            (category_dir.parent / "manifest.json").write_text(
                json.dumps({
                    "schema_version": 1,
                    "category": "ordinary-alchemy",
                    "latest_attempt_id": "attempt-01",
                    "promoted_attempt_id": "attempt-01",
                    "promotion_audit": [{
                        "attempt_id": "attempt-01",
                        "actor": {"id": "owner", "role": "run_owner"},
                        "at": "2026-09-01T05:00:00+00:00",
                    }],
                }),
                encoding="utf-8",
            )

            _, report_path, _ = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC
            )

            # The public writer resolves current dependencies from actual episode
            # packages; this fixture intentionally has none, but must still render
            # the non-empty category result without crashing.
            self.assertTrue((run_dir / "probes/probe_status.md").is_file())
            report = report_path.read_text(encoding="utf-8")
            self.assertIn("failure_types:", report)
            self.assertIn("promoted_state=", report)
            self.assertIn("mechanical_qa=", report)

    def test_run_status_preserves_history_when_submit_allowed_is_currently_blocked(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            for episode_id in ("ep03", "ep05", "ep28"):
                episode_dir = run_dir / "episodes" / episode_id
                episode_dir.mkdir(parents=True)
                (episode_dir / "workflow_readiness.json").write_text(
                    json.dumps({
                        "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
                        "resolved_workflow_hash": "1" * 64,
                        "layers": {
                            "storyboard_valid": {"valid": True, "state": "passed"},
                            "asset_contract_valid": {"valid": True, "state": "passed"},
                            "handoff_schema_valid": {"valid": True, "state": "passed"},
                            "generation_ready": {"valid": True, "state": "passed"},
                            "submit_allowed": {"valid": True, "state": "passed", "blockers": []},
                        },
                    }),
                    encoding="utf-8",
                )

            _, report_path, payload = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC,
                readiness_resolver=lambda episode_dir: {
                    **json.loads((episode_dir / "workflow_readiness.json").read_text(encoding="utf-8")),
                    "layers": {
                        **json.loads((episode_dir / "workflow_readiness.json").read_text(encoding="utf-8"))["layers"],
                        "submit_allowed": {
                            "valid": False, "state": "blocked",
                            "blockers": ["external preflight expired"],
                        },
                    },
                },
            )

            self.assertEqual(len(payload["readiness"]["episodes"]), 3)
            self.assertFalse(any("current readiness layer is blocked" in issue for issue in payload["blocking_issues"]))
            self.assertFalse(any(
                "current readiness layer is blocked: submit_allowed" in issue
                for issue in payload["blocking_issues"]
            ))
            self.assertFalse(any(
                "stale current workflow readiness" in issue
                for issue in payload["blocking_issues"]
            ))
            self.assertIn("submit_allowed: `blocked`", report_path.read_text(encoding="utf-8"))

    def test_run_status_markdown_includes_readiness_blockers(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            for episode_id in ("ep03", "ep05", "ep28"):
                episode_dir = run_dir / "episodes" / episode_id
                episode_dir.mkdir(parents=True)
                readiness = {
                    "schema_version": 1,
                    "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
                    "resolved_workflow_hash": "1" * 64,
                    "layers": {
                        "storyboard_valid": {
                            "valid": False, "state": "blocked",
                            "blockers": ["review evidence is stale"],
                        },
                    },
                    "first_blocker": {
                        "layer": "storyboard_valid",
                        "reason": "review evidence is stale",
                    },
                }
                (episode_dir / "workflow_readiness.json").write_text(
                    json.dumps(readiness), encoding="utf-8"
                )

            _, report_path, _ = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC,
                readiness_resolver=lambda episode_dir: json.loads(
                    (episode_dir / "workflow_readiness.json").read_text(encoding="utf-8")
                ),
            )

            report = report_path.read_text(encoding="utf-8")
            self.assertIn("blocker: review evidence is stale", report)
            self.assertIn("first_blocker: `storyboard_valid`", report)

    def test_run_status_blocks_when_a_required_current_readiness_layer_fails(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            for episode_id in ("ep03", "ep05", "ep28"):
                episode_dir = run_dir / "episodes" / episode_id
                episode_dir.mkdir(parents=True)
                layers = {
                    name: {"valid": True, "state": "passed"}
                    for name in (
                        "storyboard_valid", "asset_contract_valid",
                        "handoff_schema_valid", "generation_ready",
                    )
                }
                if episode_id == "ep05":
                    layers["asset_contract_valid"] = {"valid": False, "state": "blocked"}
                (episode_dir / "workflow_readiness.json").write_text(
                    json.dumps({
                        "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
                        "resolved_workflow_hash": "1" * 64,
                        "layers": layers,
                    }),
                    encoding="utf-8",
                )

            _, _, payload = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC
            )

            self.assertFalse(payload["workflow_validated"])
            self.assertIn(
                "ordinary-alchemy current readiness layer is blocked: asset_contract_valid",
                payload["blocking_issues"],
            )
            self.assertTrue(any(
                "stale current workflow readiness" in issue
                for issue in payload["blocking_issues"]
            ))

    def test_workspace_workflow_status_run_dir_uses_fail_closed_probe_report(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "storyboard_agent_workspace.py"),
                    "workflow-status",
                    "--run-dir",
                    str(run_dir),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("workflow_validated=false", result.stdout)
            self.assertTrue((run_dir / "probes/probe_status.json").is_file())
            self.assertTrue((run_dir / "probes/probe_status.md").is_file())

    def test_valid_attempt_has_complete_mechanical_semantic_signoff_and_authenticity_evidence(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005")
        result = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC, authenticity_verifier=TRUSTED_VERIFIER)
        self.assertTrue(result["valid"], result["issues"])
        self.assertTrue(result["accepted"])

    def test_fail_or_not_reviewable_required_qa_blocks_acceptance(self):
        for outcome in ("fail", "not_reviewable"):
            with self.subTest(outcome=outcome):
                attempt = valid_attempt("failed-alchemy-rewind", "EP003")
                attempt["semantic_qa"]["checks"][0]["result"] = outcome
                result = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC, authenticity_verifier=TRUSTED_VERIFIER)
                self.assertFalse(result["valid"])
                self.assertFalse(result["accepted"])
                self.assertTrue(any(outcome in issue for issue in result["issues"]))

    def test_mechanical_media_and_material_sufficiency_fail_closed(self):
        attempt = valid_attempt("yuanding-ability-reveal", "EP028")
        attempt["mechanical_qa"]["width"] = 720
        attempt["mechanical_qa"]["audio_stream"] = False
        attempt["material_sufficiency"][0]["result"] = "not_reviewable"
        result = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC, authenticity_verifier=TRUSTED_VERIFIER)
        self.assertFalse(result["valid"])
        self.assertTrue(any("1280x720" in issue for issue in result["issues"]))
        self.assertTrue(any("audio" in issue for issue in result["issues"]))
        self.assertTrue(any("not_reviewable" in issue for issue in result["issues"]))

    def test_dependency_staleness_and_authenticity_mismatch_block_attempt(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005")
        current = dict(attempt["dependencies"])
        current["package_sha256"] = "9" * 64
        stale = probe.validate_attempt(
            attempt,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies=current,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(stale["valid"])

        invalid_digest = valid_attempt("ordinary-alchemy", "EP005")
        invalid_digest["dependencies"]["resolved_workflow_hash"] = None
        invalid_digest["dependency_hash"] = canonical_hash(invalid_digest["dependencies"])
        invalid_result = probe.validate_attempt(
            invalid_digest,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(invalid_result["valid"])
        self.assertTrue(any(
            "resolved_workflow_hash must be a lowercase SHA-256 digest" in issue
            for issue in invalid_result["issues"]
        ))
        self.assertTrue(stale["stale"])

        attempt = valid_attempt("ordinary-alchemy", "EP005")
        attempt["external_authenticity"]["authenticated"] = False
        attempt["external_authenticity"]["request_digest"] = "8" * 64
        invalid = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC, authenticity_verifier=TRUSTED_VERIFIER)
        self.assertFalse(invalid["valid"])
        self.assertTrue(any("authenticated" in issue or "digest" in issue for issue in invalid["issues"]))

    def test_lifecycle_roles_and_budget_limits_are_enforced(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005", attempt_number=3)
        attempt["transition_audit"][-1]["actor"]["role"] = "operator"
        result = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC, authenticity_verifier=TRUSTED_VERIFIER)
        self.assertFalse(result["valid"])
        self.assertTrue(any("budget" in issue for issue in result["issues"]))
        self.assertTrue(any("probe_signer" in issue for issue in result["issues"]))

    def test_expired_environment_blocks_current_submission_but_preserves_historical_acceptance(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005")
        now = datetime(2026, 9, 3, tzinfo=timezone.utc)
        result = probe.validate_attempt(
            attempt,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            now=now,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertTrue(result["accepted"])
        self.assertFalse(result["current_submit_allowed"])
        self.assertTrue(any("expired" in issue for issue in result["current_blockers"]))

    def test_attempt_requires_trusted_authenticity_verifier_and_monotonic_timeline(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005")
        unverified = probe.validate_attempt(attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC)
        self.assertFalse(unverified["accepted"])
        self.assertTrue(any("authenticity verifier" in issue for issue in unverified["issues"]))

        attempt["transition_audit"][2]["at"] = "2026-09-02T04:00:00+00:00"
        attempt["transition_audit"][3]["at"] = "2026-09-01T04:00:00+00:00"
        reversed_time = probe.validate_attempt(
            attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(reversed_time["accepted"])
        self.assertTrue(any("monotonic" in issue for issue in reversed_time["issues"]))

        premature_qa = valid_attempt("ordinary-alchemy", "EP005")
        premature_qa["result_media"]["downloaded_at"] = "2026-09-01T00:00:00+00:00"
        premature_qa["mechanical_qa"]["checked_at"] = "2026-09-01T00:00:00+00:00"
        for check in premature_qa["semantic_qa"]["checks"]:
            check["reviewed_at"] = "2026-09-01T00:00:00+00:00"
        premature = probe.validate_attempt(
            premature_qa, protocol_path=PROTOCOL, rubric_path=RUBRIC,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(premature["accepted"])
        self.assertTrue(any("download_pending" in issue for issue in premature["issues"]))

    def test_malformed_budget_writes_blocked_status_instead_of_crashing(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            category_dir = run_dir / "probes" / "ordinary-alchemy" / "attempt-01"
            category_dir.mkdir(parents=True)
            attempt = valid_attempt("ordinary-alchemy", "EP005")
            attempt["validation_batch"]["max_total_cost_units"] = "not-a-number"
            attempt["validation_batch_hash"] = canonical_hash(attempt["validation_batch"])
            (category_dir / "attempt.json").write_text(json.dumps(attempt), encoding="utf-8")
            (category_dir.parent / "manifest.json").write_text(json.dumps({
                "schema_version": 1,
                "category": "ordinary-alchemy",
                "latest_attempt_id": "attempt-01",
                "promoted_attempt_id": "attempt-01",
                "promotion_audit": [{
                    "attempt_id": "attempt-01",
                    "actor": {"id": "owner", "role": "run_owner"},
                    "at": "2026-09-01T05:00:00+00:00",
                }],
            }), encoding="utf-8")

            json_path, _, payload = probe.write_probe_run_status(
                run_dir, protocol_path=PROTOCOL, rubric_path=RUBRIC
            )

            self.assertTrue(json_path.is_file())
            self.assertFalse(payload["workflow_validated"])
            self.assertTrue(any("max_total_cost_units" in issue for issue in payload["blocking_issues"]))

    def test_result_media_change_invalidates_qa_and_signoff_bindings(self):
        attempt = valid_attempt("ordinary-alchemy", "EP005")
        attempt["result_media"]["sha256"] = "9" * 64
        result = probe.validate_attempt(
            attempt, protocol_path=PROTOCOL, rubric_path=RUBRIC,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(result["accepted"])
        self.assertTrue(any("result" in issue for issue in result["issues"]))

    def test_promotion_is_explicit_and_newer_failed_attempt_does_not_replace_it(self):
        accepted = valid_attempt("ordinary-alchemy", "EP005", 1)
        failed = copy.deepcopy(accepted)
        failed["attempt_id"] = "attempt-02"
        failed["attempt_number"] = 2
        failed["state"] = "provider_failed"
        failed["validation_batch"]["batch_id"] = "batch-20260901-b"
        failed["validation_batch_hash"] = canonical_hash(failed["validation_batch"])
        failed["transition_audit"] = failed["transition_audit"][:4]
        failed["transition_audit"][-1] = {
            "from": "provider_running", "to": "provider_failed",
            "actor": {"id": "manju", "role": "manjuweb"},
            "at": "2026-09-01T04:00:00+00:00",
        }
        manifest = {
            "schema_version": 1,
            "category": "ordinary-alchemy",
            "latest_attempt_id": "attempt-02",
            "promoted_attempt_id": "attempt-01",
            "promotion_audit": [
                {
                    "attempt_id": "attempt-01",
                    "actor": {"id": "owner", "role": "run_owner"},
                    "at": "2026-09-01T05:00:00+00:00",
                }
            ],
        }
        result = probe.validate_category_manifest(
            manifest,
            {"attempt-01": accepted, "attempt-02": failed},
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies=accepted["dependencies"],
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertTrue(result["valid"], result["issues"])
        self.assertEqual(result["promoted_attempt_id"], "attempt-01")
        self.assertEqual(result["latest_attempt_id"], "attempt-02")

    def test_non_promoted_failed_attempt_must_still_have_valid_audit_evidence(self):
        accepted = valid_attempt("ordinary-alchemy", "EP005", 1)
        failed = copy.deepcopy(accepted)
        failed["attempt_id"] = "attempt-02"
        failed["attempt_number"] = 2
        failed["state"] = "provider_failed"
        failed["transition_audit"] = failed["transition_audit"][:4]
        failed["transition_audit"][-1] = {
            "from": "provider_running", "to": "provider_failed",
            "actor": {"id": "unauthorized", "role": "probe_reviewer"},
            "at": "2026-09-01T04:00:00+00:00",
        }
        manifest = {
            "schema_version": 1,
            "category": "ordinary-alchemy",
            "latest_attempt_id": "attempt-02",
            "promoted_attempt_id": "attempt-01",
            "promotion_audit": [
                {
                    "attempt_id": "attempt-01",
                    "actor": {"id": "owner", "role": "run_owner"},
                    "at": "2026-09-01T05:00:00+00:00",
                }
            ],
        }
        result = probe.validate_category_manifest(
            manifest,
            {"attempt-01": accepted, "attempt-02": failed},
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies=accepted["dependencies"],
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(result["valid"])
        self.assertTrue(any("provider_failed requires role" in issue for issue in result["issues"]))

    def test_category_rejects_aggregate_cost_over_preregistered_budget(self):
        first = valid_attempt("ordinary-alchemy", "EP005", 1)
        second = valid_attempt("ordinary-alchemy", "EP005", 2)
        for attempt in (first, second):
            attempt["validation_batch"]["max_total_cost_units"] = 1
            attempt["validation_batch_hash"] = canonical_hash(attempt["validation_batch"])
        manifest = {
            "schema_version": 1,
            "category": "ordinary-alchemy",
            "latest_attempt_id": "attempt-02",
            "promoted_attempt_id": "attempt-01",
            "promotion_audit": [{
                "attempt_id": "attempt-01", "actor": {"id": "owner", "role": "run_owner"},
                "at": "2026-09-01T05:00:00+00:00",
            }],
        }
        result = probe.validate_category_manifest(
            manifest,
            {"attempt-01": first, "attempt-02": second},
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies=first["dependencies"],
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(result["valid"])
        self.assertTrue(any("total cost budget" in issue for issue in result["issues"]))

        first["actual_cost_units"] = float("nan")
        nan_result = probe.validate_attempt(
            first, protocol_path=PROTOCOL, rubric_path=RUBRIC,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(nan_result["valid"])
        self.assertTrue(any("actual_cost_units" in issue for issue in nan_result["issues"]))

    def test_three_promoted_categories_and_cross_probe_signoff_are_required(self):
        category_specs = {
            "ordinary-alchemy": "EP005",
            "failed-alchemy-rewind": "EP003",
            "yuanding-ability-reveal": "EP028",
        }
        categories = {}
        for category, episode_id in category_specs.items():
            attempt = valid_attempt(category, episode_id)
            manifest = {
                "schema_version": 1,
                "category": category,
                "latest_attempt_id": "attempt-01",
                "promoted_attempt_id": "attempt-01",
                "promotion_audit": [
                    {"attempt_id": "attempt-01", "actor": {"id": "owner", "role": "run_owner"}, "at": "2026-09-01T05:00:00+00:00"}
                ],
            }
            categories[category] = {"manifest": manifest, "attempts": {"attempt-01": attempt}}
        cross_checks = []
        rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
        for check_id in rubric["required_cross_probe_checks"]:
            cross_checks.append({"check_id": check_id, "result": "pass", "evidence": "三条视频并排复核一致"})
        cross_signoff = {
            "rubric_id": rubric["rubric_id"],
            "checks": cross_checks,
            "signer": {"id": "cross-signer", "role": "probe_signer"},
            "decision": "accepted",
            "decided_at": "2026-09-01T06:00:00+00:00",
        }
        current_dependencies = {
            category: entry["attempts"]["attempt-01"]["dependencies"]
            for category, entry in categories.items()
        }
        cross_signoff["promoted_attempts"] = [
            {
                "category": category,
                "attempt_id": entry["attempts"]["attempt-01"]["attempt_id"],
                "result_media_sha256": entry["attempts"]["attempt-01"]["result_media"]["sha256"],
                "dependency_hash": entry["attempts"]["attempt-01"]["dependency_hash"],
            }
            for category, entry in categories.items()
        ]

        summary = probe.summarize_probe_run(
            categories,
            cross_probe_signoff=cross_signoff,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=current_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertTrue(summary["workflow_validated"], summary["blocking_issues"])
        self.assertEqual(summary["validation_scope"], "dandao-xiantu/alchemy")
        self.assertIn("预注册预算内各取得一个合格样本", summary["claim"])

        early_cross = copy.deepcopy(cross_signoff)
        early_cross["decided_at"] = "2026-09-01T04:00:00+00:00"
        early_summary = probe.summarize_probe_run(
            categories,
            cross_probe_signoff=early_cross,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=current_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(early_summary["workflow_validated"])
        self.assertTrue(any("cannot predate category promotions" in issue for issue in early_summary["blocking_issues"]))

        missing = dict(categories)
        missing.pop("yuanding-ability-reveal")
        blocked = probe.summarize_probe_run(
            missing,
            cross_probe_signoff=cross_signoff,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=current_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(blocked["workflow_validated"])
        self.assertTrue(any("yuanding-ability-reveal" in issue for issue in blocked["blocking_issues"]))

        replayed = copy.deepcopy(categories)
        for entry in replayed.values():
            entry["attempts"]["attempt-01"]["external_authenticity"]["nonce"] = "same-nonce"
        replayed_summary = probe.summarize_probe_run(
            replayed,
            cross_probe_signoff=cross_signoff,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=current_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(replayed_summary["workflow_validated"])
        self.assertTrue(any("replayed" in issue for issue in replayed_summary["blocking_issues"]))

        stale_dependencies = copy.deepcopy(current_dependencies)
        stale_dependencies["ordinary-alchemy"]["package_sha256"] = "9" * 64
        stale_summary = probe.summarize_probe_run(
            categories,
            cross_probe_signoff=cross_signoff,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=stale_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(stale_summary["workflow_validated"])
        self.assertTrue(any("stale" in issue for issue in stale_summary["blocking_issues"]))

        incomplete_dependencies = {"ordinary-alchemy": current_dependencies["ordinary-alchemy"]}
        incomplete = probe.summarize_probe_run(
            categories,
            cross_probe_signoff=cross_signoff,
            protocol_path=PROTOCOL,
            rubric_path=RUBRIC,
            current_dependencies_by_category=incomplete_dependencies,
            authenticity_verifier=TRUSTED_VERIFIER,
        )
        self.assertFalse(incomplete["workflow_validated"])
        self.assertTrue(any("all three categories" in issue for issue in incomplete["blocking_issues"]))


if __name__ == "__main__":
    unittest.main()
