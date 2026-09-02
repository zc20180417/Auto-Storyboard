"""Offline contracts for Seedance 2.5 probe fixtures, attempts, QA, and promotion.

This module validates redacted evidence only. It does not submit provider tasks,
download media, call a model, or manufacture reviewer/signoff evidence.
"""

from __future__ import annotations

import hashlib
import json
import re
import argparse
import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ATTEMPT_ID_RE = re.compile(r"^attempt-(?P<number>\d{2,})$")
EPISODE_HEADING_RE = re.compile(r"^第(?P<number>\d{3})集《.+》$")

REQUIRED_CATEGORIES = {
    "ordinary-alchemy": "EP005",
    "failed-alchemy-rewind": "EP003",
    "yuanding-ability-reveal": "EP028",
}
DEPENDENCY_SHA_FIELDS = {
    "resolved_workflow_hash",
    "package_sha256",
    "request_sha256",
    "materials_sha256",
    "protocol_sha256",
    "rubric_sha256",
    "provenance_sha256",
    "episode_fixture_sha256",
}


def _validate_dependency_snapshot(
    dependencies: dict[str, Any],
    issues: list[str],
    *,
    prefix: str = "dependencies",
) -> None:
    for field in DEPENDENCY_SHA_FIELDS:
        value = dependencies.get(field)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            issues.append(f"{prefix}.{field} must be a lowercase SHA-256 digest")
    for field in ("provider_contract_version", "manjuweb_schema_version"):
        value = dependencies.get(field)
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            issues.append(f"{prefix}.{field} must be a positive integer")


def _probe_episode_dir(run_dir: Path, episode_id: str) -> Path:
    match = re.fullmatch(r"EP(?P<number>\d+)", episode_id)
    if not match:
        return run_dir / "episodes" / episode_id.lower()
    number = int(match.group("number"))
    candidates = (
        run_dir / "episodes" / f"ep{number:02d}",
        run_dir / "episodes" / episode_id.lower(),
    )
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return candidates[0]

ALLOWED_TRANSITIONS = {
    None: {"prepared"},
    "prepared": {"submit_blocked", "submitted"},
    "submit_blocked": {"prepared"},
    "submitted": {"provider_running", "provider_failed"},
    "provider_running": {"provider_failed", "download_pending"},
    "download_pending": {"download_pending", "mechanical_qa_failed", "semantic_qa_pending"},
    "semantic_qa_pending": {"signoff_pending", "rejected"},
    "signoff_pending": {"accepted", "rejected"},
    "accepted": {"stale"},
    "rejected": {"stale"},
    "provider_failed": {"stale"},
    "mechanical_qa_failed": {"stale"},
    "stale": set(),
}

TRANSITION_OWNER_ROLES = {
    "prepared": {"operator"},
    "submit_blocked": {"readiness_owner", "operator"},
    "submitted": {"manjuweb"},
    "provider_running": {"manjuweb"},
    "provider_failed": {"manjuweb", "operator"},
    "download_pending": {"manjuweb"},
    "mechanical_qa_failed": {"media_validator"},
    "semantic_qa_pending": {"media_validator"},
    "signoff_pending": {"probe_reviewer"},
    "accepted": {"probe_signer"},
    "rejected": {"probe_reviewer", "probe_signer"},
    "stale": {"validator"},
}

MATERIAL_SUFFICIENCY_DIMENSIONS = {
    "character_face",
    "yuanding_structure_scale",
    "costume",
    "scene",
    "critical_state",
}

FROZEN_DANDAO_SOURCE_SHA256 = "7dc05d7edd73e3ca603cf260d44ddb4c415b188bbef57a5d7c8c793f762bc5a3"
FROZEN_DANDAO_EPISODE_SHA256 = {
    "EP003": "af1800d932d26f48d440ade22adb382cc014705234da84bf28f28f52c9fb1c3f",
    "EP005": "d446e9869f8591b449607375ec4e0754647dc5241153ec283ba5f34df0dc5c7a",
    "EP028": "8bf7c3f294925f3f5c0289e358dbbcc38dd43e27c47cb54d968180df336bedf6",
}
FROZEN_DANDAO_EPISODE_BOUNDARIES = {
    "EP003": (87, 133, 135),
    "EP005": (181, 225, 227),
    "EP028": (1148, 1181, 1183),
}


def _read_object(path: Path) -> dict[str, Any]:
    def reject_non_finite(value: str) -> None:
        raise ValueError(f"non-finite JSON number is forbidden: {value}")

    payload = json.loads(
        path.read_text(encoding="utf-8-sig"), parse_constant=reject_non_finite
    )
    if not isinstance(payload, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return payload


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _canonical_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _file_sha256(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _parse_time(value: Any, label: str, issues: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        issues.append(f"{label} is missing")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        issues.append(f"{label} is not an ISO-8601 timestamp")
        return None
    if parsed.tzinfo is None:
        issues.append(f"{label} must include a timezone")
        return None
    return parsed.astimezone(timezone.utc)


def validate_fixture_provenance(
    provenance_path: Path,
    *,
    source_path: Path | None = None,
    require_source_verification: bool = True,
    require_complete_probe_set: bool = True,
) -> dict[str, Any]:
    issues: list[str] = []
    try:
        provenance = _read_object(provenance_path)
    except Exception as exc:
        return {
            "valid": False,
            "issues": [f"invalid provenance.json: {exc}"],
            "episode_ids": [],
            "source_file_verified": False,
        }
    if provenance.get("schema_version") != 1:
        issues.append("provenance schema_version must be 1")
    if provenance.get("extraction_contract_version") != 1:
        issues.append("extraction_contract_version must be 1")
    source = provenance.get("source") if isinstance(provenance.get("source"), dict) else {}
    if not source.get("logical_name"):
        issues.append("source.logical_name is missing")
    if not SHA256_RE.fullmatch(str(source.get("sha256") or "")):
        issues.append("source.sha256 must be lowercase SHA-256")
    if not isinstance(source.get("line_count"), int) or source.get("line_count", 0) <= 0:
        issues.append("source.line_count must be positive")

    episodes = provenance.get("episodes")
    if not isinstance(episodes, list) or not episodes:
        issues.append("provenance episodes must be a non-empty array")
        episodes = []
    episode_ids: list[str] = []
    categories: list[str] = []
    boundaries: list[tuple[int, int, str]] = []
    for index, episode in enumerate(episodes):
        label = f"episodes[{index}]"
        if not isinstance(episode, dict):
            issues.append(f"{label} must be an object")
            continue
        episode_id = str(episode.get("episode_id") or "")
        episode_ids.append(episode_id)
        if not re.fullmatch(r"EP\d{3}", episode_id):
            issues.append(f"{label}.episode_id must use EPnnn")
        category = str(episode.get("probe_category") or "")
        categories.append(category)
        expected_episode = REQUIRED_CATEGORIES.get(category)
        if expected_episode and expected_episode != episode_id:
            issues.append(f"{label} category {category} must use {expected_episode}")
        if category not in REQUIRED_CATEGORIES:
            issues.append(f"{label}.probe_category is unsupported: {category or '<empty>'}")

        start_line = episode.get("start_line")
        end_line = episode.get("end_line")
        next_heading = episode.get("next_episode_heading_line")
        if not all(isinstance(item, int) for item in (start_line, end_line, next_heading)):
            issues.append(f"{label} boundaries must be integers")
        elif not (1 <= start_line <= end_line < next_heading):
            issues.append(f"{label} boundaries are invalid or overlap the next heading")
        else:
            boundaries.append((start_line, end_line, episode_id))

        fixture_name = str(episode.get("fixture") or "")
        fixture_path = provenance_path.parent / fixture_name
        if not fixture_name or Path(fixture_name).name != fixture_name:
            issues.append(f"{label}.fixture must be a local filename")
            continue
        if not fixture_path.is_file():
            issues.append(f"{label} missing fixture: {fixture_name}")
            continue
        content = fixture_path.read_bytes()
        if not content:
            issues.append(f"{label} fixture is empty")
            continue
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            issues.append(f"{label} fixture must be UTF-8")
            continue
        lines = text.splitlines()
        expected_heading = str(episode.get("title_heading") or "")
        if not lines or lines[0] != expected_heading or not EPISODE_HEADING_RE.fullmatch(expected_heading):
            issues.append(f"{label} fixture does not begin with its full episode heading")
        headings = [line for line in lines if EPISODE_HEADING_RE.fullmatch(line)]
        if len(headings) != 1:
            issues.append(f"{label} fixture must contain exactly one complete episode heading")
        if episode.get("line_count") != len(lines):
            issues.append(f"{label} line_count mismatch")
        if episode.get("byte_count") != len(content):
            issues.append(f"{label} byte_count mismatch")
        if episode.get("sha256") != _sha256_bytes(content):
            issues.append(f"{label} sha256 mismatch")
        for field in ("target_scene", "observable_scope"):
            value = str(episode.get(field) or "")
            if not value:
                issues.append(f"{label}.{field} is missing")
            elif field == "target_scene" and value not in text:
                issues.append(f"{label}.target_scene is not present in the full episode fixture")

    if len(episode_ids) != len(set(episode_ids)):
        issues.append("duplicate episode_id in provenance")
    if len(categories) != len(set(categories)):
        issues.append("duplicate probe_category in provenance")
    if require_complete_probe_set and (
        set(categories) != set(REQUIRED_CATEGORIES) or len(categories) != len(REQUIRED_CATEGORIES)
    ):
        issues.append("provenance must contain exactly the three frozen probe categories")
    boundaries.sort()
    for prior, current in zip(boundaries, boundaries[1:]):
        if current[0] <= prior[1]:
            issues.append(f"episode source boundaries overlap: {prior[2]} and {current[2]}")

    structural_valid = not issues
    source_verified = False
    if source_path is not None:
        source_issues: list[str] = []
        if not source_path.is_file():
            source_issues.append("source file is missing")
        else:
            source_bytes = source_path.read_bytes()
            if _sha256_bytes(source_bytes) != source.get("sha256"):
                source_issues.append("source sha256 mismatch")
            try:
                source_text = source_bytes.decode("utf-8")
                source_lines = source_text.splitlines()
            except UnicodeDecodeError:
                source_lines = []
                source_issues.append("source file must be UTF-8")
            if len(source_lines) != source.get("line_count"):
                source_issues.append("source line_count mismatch")
            for episode in episodes:
                if not isinstance(episode, dict):
                    continue
                start = episode.get("start_line")
                end = episode.get("end_line")
                fixture = provenance_path.parent / str(episode.get("fixture") or "")
                if not isinstance(start, int) or not isinstance(end, int) or not fixture.is_file():
                    continue
                next_heading = episode.get("next_episode_heading_line")
                expected_heading = str(episode.get("title_heading") or "")
                if start > len(source_lines) or source_lines[start - 1] != expected_heading:
                    source_issues.append(
                        f"source start heading mismatch for {episode.get('episode_id')}"
                    )
                if not isinstance(next_heading, int) or next_heading > len(source_lines):
                    source_issues.append(
                        f"source next episode heading is missing for {episode.get('episode_id')}"
                    )
                elif not EPISODE_HEADING_RE.fullmatch(source_lines[next_heading - 1]):
                    source_issues.append(
                        f"source next_episode_heading_line is not an episode heading for {episode.get('episode_id')}"
                    )
                elif any(line.strip() for line in source_lines[end: next_heading - 1]):
                    source_issues.append(
                        f"source episode tail is truncated before next heading for {episode.get('episode_id')}"
                    )
                extracted = "\n".join(source_lines[start - 1 : end]).rstrip("\n") + "\n"
                fixture_text = fixture.read_text(encoding="utf-8").rstrip("\n") + "\n"
                if extracted != fixture_text:
                    source_issues.append(
                        f"source boundary extraction mismatch for {episode.get('episode_id')}"
                    )
            source_verified = not source_issues
        issues.extend(source_issues)
    elif require_source_verification:
        frozen_episode_hashes = {
            str(item.get("episode_id")): str(item.get("sha256"))
            for item in episodes
            if isinstance(item, dict)
        }
        frozen_boundaries = {
            str(item.get("episode_id")): (
                item.get("start_line"), item.get("end_line"), item.get("next_episode_heading_line")
            )
            for item in episodes
            if isinstance(item, dict)
        }
        if (
            source.get("sha256") == FROZEN_DANDAO_SOURCE_SHA256
            and frozen_episode_hashes == FROZEN_DANDAO_EPISODE_SHA256
            and frozen_boundaries == FROZEN_DANDAO_EPISODE_BOUNDARIES
            and set(categories) == set(REQUIRED_CATEGORIES)
        ):
            source_verified = True
        else:
            issues.append(
                "source verification is required for complete-episode provenance; "
                "fixture does not match the frozen dandao source manifest"
            )

    return {
        "valid": not issues,
        "structural_valid": structural_valid,
        "issues": issues,
        "episode_ids": episode_ids,
        "source_file_verified": source_verified,
    }


def _validate_lifecycle(attempt: dict[str, Any], issues: list[str]) -> None:
    audit = attempt.get("transition_audit")
    if not isinstance(audit, list) or not audit:
        issues.append("transition_audit must be non-empty")
        return
    prior_state: str | None = None
    prior_time: datetime | None = None
    for index, transition in enumerate(audit):
        if not isinstance(transition, dict):
            issues.append(f"transition_audit[{index}] must be an object")
            continue
        from_state = transition.get("from")
        to_state = transition.get("to")
        if from_state != prior_state:
            issues.append(f"transition_audit[{index}] from state does not match prior transition")
        if to_state not in ALLOWED_TRANSITIONS.get(from_state, set()):
            issues.append(f"illegal lifecycle transition: {from_state} -> {to_state}")
        actor = transition.get("actor") if isinstance(transition.get("actor"), dict) else {}
        role = actor.get("role")
        if role not in TRANSITION_OWNER_ROLES.get(to_state, set()):
            allowed = ", ".join(sorted(TRANSITION_OWNER_ROLES.get(to_state, set()))) or "none"
            issues.append(f"transition to {to_state} requires role {allowed}; got {role or '<empty>'}")
        transition_time = _parse_time(
            transition.get("at"), f"transition_audit[{index}].at", issues
        )
        if transition_time and prior_time and transition_time < prior_time:
            issues.append("transition_audit timestamps must be monotonic")
        if transition_time:
            prior_time = transition_time
        prior_state = to_state
    if prior_state != attempt.get("state"):
        issues.append("attempt state does not match final transition")


def _validate_mechanical_qa(attempt: dict[str, Any], issues: list[str]) -> None:
    media = attempt.get("result_media") if isinstance(attempt.get("result_media"), dict) else {}
    for field in ("locator", "sha256", "byte_count", "mime_type", "downloaded_at"):
        if not media.get(field):
            issues.append(f"result_media.{field} is missing")
    if media.get("locator") and not str(media["locator"]).startswith("controlled://"):
        issues.append("result_media.locator must be an immutable controlled locator")
    if media.get("sha256") and not SHA256_RE.fullmatch(str(media["sha256"])):
        issues.append("result_media.sha256 is invalid")
    if media.get("mime_type") and media.get("mime_type") != "video/mp4":
        issues.append("result media must be video/mp4")
    _parse_time(media.get("downloaded_at"), "result_media.downloaded_at", issues)

    qa = attempt.get("mechanical_qa") if isinstance(attempt.get("mechanical_qa"), dict) else {}
    if qa.get("result_media_sha256") != media.get("sha256"):
        issues.append("mechanical QA is not bound to result_media.sha256")
    if qa.get("decoded") is not True:
        issues.append("mechanical QA requires decoded=true")
    if qa.get("width") != 1280 or qa.get("height") != 720 or qa.get("ratio") != "16:9":
        issues.append("mechanical QA requires 1280x720 and ratio 16:9")
    duration = qa.get("duration_seconds")
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not 4 <= duration <= 30:
        issues.append("mechanical QA duration must be from 4 through 30 seconds")
    if qa.get("fps") != 24:
        issues.append("mechanical QA requires 24 fps")
    if qa.get("audio_stream") is not True:
        issues.append("mechanical QA requires an audio stream")
    if qa.get("validator_version") != 1:
        issues.append("mechanical QA validator_version must be 1")
    _parse_time(qa.get("checked_at"), "mechanical_qa.checked_at", issues)


def _validate_material_sufficiency(attempt: dict[str, Any], issues: list[str]) -> None:
    entries = attempt.get("material_sufficiency")
    if not isinstance(entries, list):
        issues.append("material_sufficiency must be an array")
        return
    by_dimension = {
        item.get("dimension"): item for item in entries if isinstance(item, dict) and item.get("dimension")
    }
    for dimension in MATERIAL_SUFFICIENCY_DIMENSIONS:
        item = by_dimension.get(dimension)
        if not item:
            issues.append(f"material_sufficiency missing {dimension}")
            continue
        if item.get("result") != "pass":
            issues.append(f"material_sufficiency {dimension} is {item.get('result') or '<empty>'}")
        if not item.get("material_refs") or not item.get("observable_time_range"):
            issues.append(f"material_sufficiency {dimension} lacks material/time evidence")


def _validate_semantic_qa(
    attempt: dict[str, Any],
    rubric: dict[str, Any],
    issues: list[str],
) -> None:
    semantic = attempt.get("semantic_qa") if isinstance(attempt.get("semantic_qa"), dict) else {}
    if semantic.get("rubric_id") != rubric.get("rubric_id"):
        issues.append("semantic QA rubric_id mismatch")
    if not isinstance(semantic.get("revision"), int) or semantic.get("revision", 0) < 1:
        issues.append("semantic QA revision must be positive")
    checks = semantic.get("checks") if isinstance(semantic.get("checks"), list) else []
    check_map = {item.get("check_id"): item for item in checks if isinstance(item, dict)}
    required = list(rubric.get("required_common_checks", []))
    required.extend(rubric.get("required_category_checks", {}).get(attempt.get("category"), []))
    allowed_results = set(rubric.get("allowed_results", []))
    result_media = attempt.get("result_media") if isinstance(attempt.get("result_media"), dict) else {}
    if len(checks) != len(check_map):
        issues.append("semantic QA contains duplicate check_id values")
    for check_id in required:
        check = check_map.get(check_id)
        if not check:
            issues.append(f"semantic QA missing required check {check_id}")
            continue
        result = check.get("result")
        if result not in allowed_results:
            issues.append(f"semantic QA {check_id} has invalid result")
        elif result != "pass":
            issues.append(f"semantic QA required check {check_id} is {result}")
        for field in (
            "time_range",
            "observation",
            "threshold",
            "material_refs",
            "rubric_version",
            "reviewer",
            "reviewed_at",
        ):
            if not check.get(field):
                issues.append(f"semantic QA {check_id} missing {field}")
        reviewer = check.get("reviewer") if isinstance(check.get("reviewer"), dict) else {}
        if reviewer.get("role") != "probe_reviewer" or not reviewer.get("id"):
            issues.append(f"semantic QA {check_id} requires probe_reviewer role")
        if check.get("rubric_version") != rubric.get("rubric_id"):
            issues.append(f"semantic QA {check_id} rubric_version mismatch")
        if check.get("result_media_sha256") != result_media.get("sha256"):
            issues.append(f"semantic QA {check_id} is not bound to result media")
        _parse_time(check.get("reviewed_at"), f"semantic QA {check_id}.reviewed_at", issues)


def _validate_signoff(attempt: dict[str, Any], rubric: dict[str, Any], issues: list[str]) -> None:
    signoff = attempt.get("signoff") if isinstance(attempt.get("signoff"), dict) else {}
    if signoff.get("decision") != "accepted":
        issues.append("accepted attempt requires accepted signoff decision")
    signer = signoff.get("signer") if isinstance(signoff.get("signer"), dict) else {}
    if signer.get("role") != "probe_signer" or not signer.get("id"):
        issues.append("accepted attempt requires an authorized probe_signer")
    if not signoff.get("authority_source"):
        issues.append("signoff authority_source is missing")
    if signoff.get("rubric_version") != rubric.get("rubric_id"):
        issues.append("signoff rubric_version mismatch")
    result_media = attempt.get("result_media") if isinstance(attempt.get("result_media"), dict) else {}
    if signoff.get("result_media_sha256") != result_media.get("sha256"):
        issues.append("signoff is not bound to result_media.sha256")
    _parse_time(signoff.get("decided_at"), "signoff.decided_at", issues)


def _validate_retention(attempt: dict[str, Any], issues: list[str]) -> None:
    retention = attempt.get("retention") if isinstance(attempt.get("retention"), dict) else {}
    for field in (
        "classification",
        "rights_holder",
        "allowed_model_use",
        "retention_until",
        "access_roles",
        "deletion_owner",
    ):
        if not retention.get(field):
            issues.append(f"retention.{field} is missing")
    _parse_time(retention.get("retention_until"), "retention.retention_until", issues)


def _validate_attempt_chronology(attempt: dict[str, Any], issues: list[str]) -> None:
    batch = attempt.get("validation_batch") if isinstance(attempt.get("validation_batch"), dict) else {}
    registered = _parse_time(batch.get("registered_at"), "chronology.batch.registered_at", issues)
    transition_times = [
        _parse_time(item.get("at"), f"chronology.transition[{index}]", issues)
        for index, item in enumerate(attempt.get("transition_audit", []))
        if isinstance(item, dict)
    ]
    transition_times = [item for item in transition_times if item is not None]
    transition_by_state = {
        item.get("to"): _parse_time(item.get("at"), f"chronology.transition.{item.get('to')}", issues)
        for item in attempt.get("transition_audit", [])
        if isinstance(item, dict)
    }
    if registered and transition_times and transition_times[0] < registered:
        issues.append("prepared transition cannot predate validation batch registration")

    media = attempt.get("result_media") if isinstance(attempt.get("result_media"), dict) else {}
    mechanical = attempt.get("mechanical_qa") if isinstance(attempt.get("mechanical_qa"), dict) else {}
    downloaded = _parse_time(media.get("downloaded_at"), "chronology.result downloaded_at", issues)
    mechanical_checked = _parse_time(mechanical.get("checked_at"), "chronology.mechanical checked_at", issues)
    if downloaded and mechanical_checked and mechanical_checked < downloaded:
        issues.append("mechanical QA cannot predate result download")
    download_pending = transition_by_state.get("download_pending")
    if downloaded and download_pending and downloaded < download_pending:
        issues.append("result download cannot predate download_pending transition")

    semantic = attempt.get("semantic_qa") if isinstance(attempt.get("semantic_qa"), dict) else {}
    reviewed_times = [
        _parse_time(item.get("reviewed_at"), f"chronology.semantic[{index}]", issues)
        for index, item in enumerate(semantic.get("checks", []))
        if isinstance(item, dict)
    ]
    reviewed_times = [item for item in reviewed_times if item is not None]
    if mechanical_checked and any(item < mechanical_checked for item in reviewed_times):
        issues.append("semantic QA cannot predate mechanical QA")
    semantic_pending = transition_by_state.get("semantic_qa_pending")
    if semantic_pending and any(item < semantic_pending for item in reviewed_times):
        issues.append("semantic QA cannot predate semantic_qa_pending transition")
    signoff = attempt.get("signoff") if isinstance(attempt.get("signoff"), dict) else {}
    signed = _parse_time(signoff.get("decided_at"), "chronology.signoff decided_at", issues)
    if signed and reviewed_times and signed < max(reviewed_times):
        issues.append("signoff cannot predate semantic QA")
    signoff_pending = transition_by_state.get("signoff_pending")
    if signed and signoff_pending and signed < signoff_pending:
        issues.append("signoff decision cannot predate signoff_pending transition")
    accepted_transition = transition_by_state.get("accepted")
    if signed and accepted_transition and accepted_transition < signed:
        issues.append("accepted transition cannot predate signoff decision")


def validate_attempt(
    attempt: dict[str, Any],
    *,
    protocol_path: Path,
    rubric_path: Path,
    current_dependencies: dict[str, Any] | None = None,
    now: datetime | None = None,
    authenticity_verifier: Callable[[dict[str, Any]], bool] | None = None,
) -> dict[str, Any]:
    protocol = _read_object(protocol_path)
    rubric = _read_object(rubric_path)
    issues: list[str] = []
    current_blockers: list[str] = []
    stale = False
    if attempt.get("schema_version") != 1:
        issues.append("attempt schema_version must be 1")
    attempt_id = str(attempt.get("attempt_id") or "")
    match = ATTEMPT_ID_RE.fullmatch(attempt_id)
    if not match:
        issues.append("attempt_id must use attempt-NN")
    elif attempt.get("attempt_number") != int(match.group("number")):
        issues.append("attempt_number does not match attempt_id")
    category = str(attempt.get("category") or "")
    expected_episode = protocol.get("categories", {}).get(category, {}).get("episode_id")
    if not expected_episode:
        issues.append(f"unsupported probe category: {category or '<empty>'}")
    elif attempt.get("episode_id") != expected_episode:
        issues.append(f"category {category} must use episode {expected_episode}")
    batch = attempt.get("validation_batch") if isinstance(attempt.get("validation_batch"), dict) else {}
    for field in (
        "batch_id",
        "registered_at",
        "max_attempts_per_category",
        "max_total_cost_units",
        "timeout_seconds",
        "stop_conditions",
    ):
        if not batch.get(field):
            issues.append(f"validation_batch.{field} is missing")
    max_attempts = batch.get("max_attempts_per_category")
    if isinstance(max_attempts, bool) or not isinstance(max_attempts, int) or max_attempts < 1:
        issues.append("validation_batch.max_attempts_per_category must be a positive integer")
    for field, minimum in (("max_total_cost_units", 0.0), ("timeout_seconds", 1.0)):
        value = batch.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)) or float(value) < minimum:
            issues.append(f"validation_batch.{field} must be a finite number")
    _parse_time(batch.get("registered_at"), "validation_batch.registered_at", issues)
    if attempt.get("validation_batch_hash") != _canonical_hash(batch):
        issues.append("validation_batch_hash does not match the preregistered batch")
    actual_cost = attempt.get("actual_cost_units")
    if (
        isinstance(actual_cost, bool)
        or not isinstance(actual_cost, (int, float))
        or not math.isfinite(float(actual_cost))
        or actual_cost < 0
    ):
        issues.append("actual_cost_units must be a non-negative number")
    if isinstance(attempt.get("attempt_number"), int) and isinstance(batch.get("max_attempts_per_category"), int):
        if attempt["attempt_number"] > batch["max_attempts_per_category"]:
            issues.append("attempt exceeds preregistered budget max_attempts_per_category")

    dependencies = attempt.get("dependencies") if isinstance(attempt.get("dependencies"), dict) else {}
    required_dependency_fields = {
        "resolved_workflow_hash",
        "package_sha256",
        "request_sha256",
        "materials_sha256",
        "provider_contract_version",
        "manjuweb_schema_version",
        "protocol_sha256",
        "rubric_sha256",
        "provenance_sha256",
        "episode_fixture_sha256",
    }
    for field in required_dependency_fields:
        if field not in dependencies:
            issues.append(f"dependencies.{field} is missing")
    _validate_dependency_snapshot(dependencies, issues)
    if dependencies.get("provider_contract_version") != protocol.get("provider_contract_version"):
        issues.append("provider_contract_version does not match protocol")
    if dependencies.get("manjuweb_schema_version") != protocol.get("manjuweb_schema_version"):
        issues.append("manjuweb_schema_version does not match protocol")
    if dependencies.get("protocol_sha256") != _file_sha256(protocol_path):
        issues.append("dependencies.protocol_sha256 is stale")
    if dependencies.get("rubric_sha256") != _file_sha256(rubric_path):
        issues.append("dependencies.rubric_sha256 is stale")
    if attempt.get("dependency_hash") != _canonical_hash(dependencies):
        issues.append("dependency_hash does not match dependencies")
    if current_dependencies is not None and current_dependencies != dependencies:
        stale = True
        issues.append("attempt dependencies are stale relative to current workflow/package/materials")

    authenticity = (
        attempt.get("external_authenticity")
        if isinstance(attempt.get("external_authenticity"), dict)
        else {}
    )
    if attempt.get("state") not in {"prepared", "submit_blocked"}:
        if authenticity_verifier is None:
            issues.append("external evidence has no trusted authenticity verifier")
        elif not authenticity_verifier(attempt):
            issues.append("external evidence failed trusted authenticity verification")
        if authenticity.get("authority") != "manjuweb":
            issues.append("external authenticity authority must be manjuweb")
        if authenticity.get("authenticated") is not True:
            issues.append("external evidence is not authenticated")
        if authenticity.get("signature_valid") is not True:
            issues.append("external evidence signature is invalid")
        if not authenticity.get("nonce") or not authenticity.get("task_id"):
            issues.append("external evidence nonce/task_id is missing")
        if authenticity.get("request_digest") != dependencies.get("request_sha256"):
            issues.append("external request digest does not match dependencies")
        environment = (
            authenticity.get("environment")
            if isinstance(authenticity.get("environment"), dict)
            else {}
        )
        for field in (
            "region",
            "model",
            "account_pseudonym",
            "consumer_deployment_id",
            "consumer_contract_id",
            "observed_at",
            "expires_at",
        ):
            if not environment.get(field):
                issues.append(f"external environment.{field} is missing")
        if environment.get("region") != "cn-beijing":
            issues.append("external environment region mismatch")
        if environment.get("model") != "doubao-seedance-2-5-260628":
            issues.append("external environment model mismatch")
        observed = _parse_time(environment.get("observed_at"), "environment.observed_at", issues)
        expires = _parse_time(environment.get("expires_at"), "environment.expires_at", issues)
        if observed and expires:
            max_expiry = observed + timedelta_hours(protocol.get("preflight_ttl_hours", 24))
            if expires > max_expiry:
                issues.append("environment evidence exceeds the 24-hour preflight TTL")
            effective_now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
            if effective_now > expires:
                current_blockers.append("environment/preflight evidence is expired")

    _validate_lifecycle(attempt, issues)
    accepted_state = attempt.get("state") == "accepted"
    if accepted_state:
        _validate_mechanical_qa(attempt, issues)
        _validate_material_sufficiency(attempt, issues)
        _validate_semantic_qa(attempt, rubric, issues)
        _validate_signoff(attempt, rubric, issues)
        _validate_retention(attempt, issues)
        _validate_attempt_chronology(attempt, issues)
    accepted = accepted_state and not issues
    current_submit_allowed = accepted and not current_blockers and not stale
    return {
        "valid": not issues,
        "accepted": accepted,
        "stale": stale or attempt.get("state") == "stale",
        "current_submit_allowed": current_submit_allowed,
        "issues": issues,
        "current_blockers": current_blockers,
    }


def timedelta_hours(hours: Any) -> timedelta:
    try:
        return timedelta(hours=float(hours))
    except (TypeError, ValueError):
        return timedelta(hours=24)


def validate_category_manifest(
    manifest: dict[str, Any],
    attempts: dict[str, dict[str, Any]],
    *,
    protocol_path: Path,
    rubric_path: Path,
    current_dependencies: dict[str, Any] | None = None,
    authenticity_verifier: Callable[[dict[str, Any]], bool] | None = None,
) -> dict[str, Any]:
    issues: list[str] = []
    if manifest.get("schema_version") != 1:
        issues.append("category manifest schema_version must be 1")
    category = str(manifest.get("category") or "")
    if category not in REQUIRED_CATEGORIES:
        issues.append(f"unsupported category: {category or '<empty>'}")
    parsed_numbers: dict[str, int] = {}
    attempt_results: dict[str, dict[str, Any]] = {}
    latest = str(manifest.get("latest_attempt_id") or "")
    promoted = str(manifest.get("promoted_attempt_id") or "")
    for attempt_id, attempt in attempts.items():
        match = ATTEMPT_ID_RE.fullmatch(attempt_id)
        if not match:
            issues.append(f"invalid attempt directory/id: {attempt_id}")
            continue
        parsed_numbers[attempt_id] = int(match.group("number"))
        if attempt.get("attempt_id") != attempt_id:
            issues.append(f"attempt payload id mismatch: {attempt_id}")
        if attempt.get("category") != category:
            issues.append(f"attempt category mismatch: {attempt_id}")
        attempt_results[attempt_id] = validate_attempt(
            attempt,
            protocol_path=protocol_path,
            rubric_path=rubric_path,
            current_dependencies=current_dependencies if attempt_id == promoted else None,
            authenticity_verifier=authenticity_verifier,
        )
    if not parsed_numbers:
        issues.append("category has no attempts")
    elif latest not in attempts or parsed_numbers.get(latest) != max(parsed_numbers.values()):
        issues.append("latest_attempt_id must name the highest immutable attempt number")
    if promoted not in attempts:
        issues.append("promoted_attempt_id must name an existing attempt")
    else:
        promoted_result = attempt_results.get(promoted, {})
        if not promoted_result.get("accepted") or promoted_result.get("stale"):
            issues.append("promoted_attempt_id must point to a current valid accepted attempt")
    promotion_audit = manifest.get("promotion_audit")
    if not isinstance(promotion_audit, list) or not promotion_audit:
        issues.append("promotion_audit must be non-empty")
    else:
        promotion = promotion_audit[-1] if isinstance(promotion_audit[-1], dict) else {}
        actor = promotion.get("actor") if isinstance(promotion.get("actor"), dict) else {}
        if promotion.get("attempt_id") != promoted:
            issues.append("latest promotion audit does not match promoted_attempt_id")
        if actor.get("role") != "run_owner":
            issues.append("promotion requires run_owner role")
        _parse_time(promotion.get("at"), "promotion_audit.at", issues)
        promotion_time = _parse_time(promotion.get("at"), "promotion chronology", issues)
        promoted_attempt = attempts.get(promoted, {})
        accepted_transitions = [
            _parse_time(item.get("at"), "promoted accepted transition", issues)
            for item in promoted_attempt.get("transition_audit", [])
            if isinstance(item, dict) and item.get("to") == "accepted"
        ]
        accepted_transitions = [item for item in accepted_transitions if item is not None]
        if promotion_time and accepted_transitions and promotion_time < accepted_transitions[-1]:
            issues.append("promotion cannot predate accepted attempt")
        if authenticity_verifier is None or not authenticity_verifier(
            {"evidence_type": "promotion", "category": category, "promotion": promotion}
        ):
            issues.append("promotion lacks trusted run-owner authorization verification")

    terminal_failures = [
        attempt.get("state")
        for attempt in attempts.values()
        if attempt.get("state")
        in {"provider_failed", "mechanical_qa_failed", "rejected", "stale"}
    ]
    batch_groups: dict[str, list[dict[str, Any]]] = {}
    for attempt in attempts.values():
        snapshot = attempt.get("validation_batch") if isinstance(attempt.get("validation_batch"), dict) else {}
        batch_groups.setdefault(str(snapshot.get("batch_id") or "<missing>"), []).append(attempt)
    for batch_id, grouped_attempts in batch_groups.items():
        snapshots = [attempt.get("validation_batch", {}) for attempt in grouped_attempts]
        if any(snapshot != snapshots[0] for snapshot in snapshots[1:]):
            issues.append(f"validation batch {batch_id} was rewritten after preregistration")
            continue
        finite_costs = [
            float(attempt["actual_cost_units"]) for attempt in grouped_attempts
            if isinstance(attempt.get("actual_cost_units"), (int, float))
            and not isinstance(attempt.get("actual_cost_units"), bool)
            and math.isfinite(float(attempt["actual_cost_units"]))
        ]
        max_cost = snapshots[0].get("max_total_cost_units")
        if isinstance(max_cost, (int, float)) and not isinstance(max_cost, bool) and math.isfinite(float(max_cost)) and sum(finite_costs) > float(max_cost):
            issues.append(f"validation batch {batch_id} exceeds preregistered total cost budget")
        if "accepted" in snapshots[0].get("stop_conditions", []):
            accepted_numbers = sorted(
                attempt.get("attempt_number") for attempt in grouped_attempts
                if attempt.get("state") == "accepted" and isinstance(attempt.get("attempt_number"), int)
            )
            if accepted_numbers and any(
                isinstance(attempt.get("attempt_number"), int)
                and attempt["attempt_number"] > accepted_numbers[0]
                for attempt in grouped_attempts
            ):
                issues.append(f"validation batch {batch_id} continued after accepted stop condition")
    attempt_issues = [
        f"{attempt_id}: {issue}"
        for attempt_id, result in attempt_results.items()
        for issue in result.get("issues", [])
    ]
    # Non-promoted failed attempts remain valid history, but their evidence must
    # still be structurally and authoritatively valid. A failed provider result
    # normally contributes no issues; malformed lifecycle/authenticity data must
    # never be hidden merely because the attempt is not promoted.
    issues.extend(attempt_issues)
    promoted_attempt = attempts.get(promoted, {}) if promoted in attempts else {}
    promoted_result = attempt_results.get(promoted, {})
    promoted_state = str(promoted_attempt.get("state") or "missing")
    return {
        "valid": not issues,
        "issues": issues,
        "category": category,
        "latest_attempt_id": latest,
        "promoted_attempt_id": promoted,
        "attempt_count": len(attempts),
        "failure_types": terminal_failures,
        "consumed_cost_units": sum(
            float(attempt.get("actual_cost_units", 0)) for attempt in attempts.values()
            if isinstance(attempt.get("actual_cost_units"), (int, float))
            and not isinstance(attempt.get("actual_cost_units"), bool)
            and math.isfinite(float(attempt.get("actual_cost_units", 0)))
        ),
        "promoted_valid": promoted in attempt_results and attempt_results[promoted].get("accepted") is True,
        "promoted_state": promoted_state,
        "mechanical_qa_state": (
            "passed" if promoted_state == "accepted"
            else "failed" if promoted_state == "mechanical_qa_failed"
            else "not_reached"
        ),
        "semantic_qa_state": (
            "passed" if promoted_state == "accepted"
            else "failed" if promoted_state == "rejected"
            else "not_reached"
        ),
        "signoff_state": "accepted" if promoted_state == "accepted" else "not_accepted",
        "stale": bool(promoted_result.get("stale")),
        "current_submit_allowed": bool(promoted_result.get("current_submit_allowed")),
        "current_blockers": list(promoted_result.get("current_blockers", [])),
    }


def summarize_probe_run(
    categories: dict[str, dict[str, Any]],
    *,
    cross_probe_signoff: dict[str, Any] | None,
    protocol_path: Path,
    rubric_path: Path,
    current_dependencies_by_category: dict[str, dict[str, Any]] | None = None,
    authenticity_verifier: Callable[[dict[str, Any]], bool] | None = None,
) -> dict[str, Any]:
    protocol = _read_object(protocol_path)
    rubric = _read_object(rubric_path)
    blocking: list[str] = []
    category_results: dict[str, dict[str, Any]] = {}
    nonces: set[str] = set()
    task_ids: set[str] = set()
    batch_snapshots: list[dict[str, Any]] = []
    batch_costs: dict[str, float] = {}
    total_cost = 0.0
    promoted_bindings: list[dict[str, str]] = []
    promotion_times: list[datetime] = []
    if authenticity_verifier is None:
        blocking.append("trusted ManJuWeb authenticity verifier is unavailable")
    if current_dependencies_by_category is None:
        blocking.append("current probe dependencies are unavailable")
    elif set(current_dependencies_by_category) != set(REQUIRED_CATEGORIES) or any(
        not isinstance(current_dependencies_by_category.get(category), dict)
        or not current_dependencies_by_category.get(category)
        for category in REQUIRED_CATEGORIES
    ):
        blocking.append("current probe dependencies must cover all three categories")
    for category in protocol.get("categories", {}):
        entry = categories.get(category)
        if not isinstance(entry, dict):
            blocking.append(f"missing required probe category: {category}")
            continue
        result = validate_category_manifest(
            entry.get("manifest", {}),
            entry.get("attempts", {}),
            protocol_path=protocol_path,
            rubric_path=rubric_path,
            current_dependencies=(current_dependencies_by_category or {}).get(category),
            authenticity_verifier=authenticity_verifier,
        )
        category_results[category] = result
        if not result["valid"] or not result["promoted_valid"]:
            blocking.extend(f"{category}: {issue}" for issue in result["issues"])
        for attempt in entry.get("attempts", {}).values():
            if not isinstance(attempt, dict):
                continue
            authenticity = attempt.get("external_authenticity") if isinstance(attempt.get("external_authenticity"), dict) else {}
            nonce = str(authenticity.get("nonce") or "")
            task_id = str(authenticity.get("task_id") or "")
            if nonce in nonces:
                blocking.append(f"replayed external nonce: {nonce}")
            if task_id in task_ids:
                blocking.append(f"reused provider task_id: {task_id}")
            if nonce:
                nonces.add(nonce)
            if task_id:
                task_ids.add(task_id)
            if isinstance(attempt.get("validation_batch"), dict):
                batch_snapshots.append(attempt["validation_batch"])
            if isinstance(attempt.get("actual_cost_units"), (int, float)) and not isinstance(attempt.get("actual_cost_units"), bool):
                cost = float(attempt["actual_cost_units"])
                if math.isfinite(cost):
                    total_cost += cost
                    snapshot = attempt.get("validation_batch") if isinstance(attempt.get("validation_batch"), dict) else {}
                    batch_id = str(snapshot.get("batch_id") or "<missing>")
                    batch_costs[batch_id] = batch_costs.get(batch_id, 0.0) + cost
        promoted_attempt = entry.get("attempts", {}).get(result.get("promoted_attempt_id"), {})
        if isinstance(promoted_attempt, dict):
            result_media = promoted_attempt.get("result_media") if isinstance(promoted_attempt.get("result_media"), dict) else {}
            promoted_bindings.append({
                "category": category,
                "attempt_id": str(promoted_attempt.get("attempt_id") or ""),
                "result_media_sha256": str(result_media.get("sha256") or ""),
                "dependency_hash": str(promoted_attempt.get("dependency_hash") or ""),
            })
        promotion_audit = entry.get("manifest", {}).get("promotion_audit", [])
        if isinstance(promotion_audit, list) and promotion_audit and isinstance(promotion_audit[-1], dict):
            promotion_time = _parse_time(
                promotion_audit[-1].get("at"), f"{category} promotion chronology", blocking
            )
            if promotion_time is not None:
                promotion_times.append(promotion_time)

    run_batches: dict[str, list[dict[str, Any]]] = {}
    for snapshot in batch_snapshots:
        run_batches.setdefault(str(snapshot.get("batch_id") or "<missing>"), []).append(snapshot)
    for batch_id, snapshots in run_batches.items():
        if any(snapshot != snapshots[0] for snapshot in snapshots[1:]):
            blocking.append(f"validation batch {batch_id} was rewritten across categories")
        else:
            max_cost = snapshots[0].get("max_total_cost_units")
            if isinstance(max_cost, (int, float)) and not isinstance(max_cost, bool) and math.isfinite(float(max_cost)) and batch_costs.get(batch_id, 0.0) > float(max_cost):
                blocking.append(f"validation batch {batch_id} exceeds run-level total cost budget")

    cross = cross_probe_signoff if isinstance(cross_probe_signoff, dict) else {}
    if cross.get("rubric_id") != rubric.get("rubric_id"):
        blocking.append("cross-probe signoff rubric mismatch")
    signer = cross.get("signer") if isinstance(cross.get("signer"), dict) else {}
    if signer.get("role") != "probe_signer" or cross.get("decision") != "accepted":
        blocking.append("cross-probe signoff requires accepted decision by probe_signer")
    if authenticity_verifier is None or not authenticity_verifier(
        {"evidence_type": "cross_probe_signoff", "signoff": cross}
    ):
        blocking.append("cross-probe signoff lacks trusted authorization verification")
    checks = cross.get("checks") if isinstance(cross.get("checks"), list) else []
    check_map = {item.get("check_id"): item for item in checks if isinstance(item, dict)}
    for check_id in rubric.get("required_cross_probe_checks", []):
        check = check_map.get(check_id)
        if not check or check.get("result") != "pass" or not check.get("evidence"):
            blocking.append(f"cross-probe check is missing or not pass: {check_id}")
    cross_decided = _parse_time(cross.get("decided_at"), "cross_probe_signoff.decided_at", blocking)
    if cross_decided and promotion_times and cross_decided < max(promotion_times):
        blocking.append("cross-probe signoff cannot predate category promotions")
    if cross.get("promoted_attempts") != promoted_bindings:
        blocking.append("cross-probe signoff is not bound to current promoted attempts")

    workflow_validated = not blocking and len(category_results) == len(protocol.get("categories", {}))
    if workflow_validated:
        claim = (
            "在预注册预算内各取得一个合格样本，验证范围为 "
            f"{protocol.get('validation_scope')}; 不声明统计稳定率或跨项目复用。"
        )
    else:
        claim = "合同原型完成，视频工作流未验证。"
    return {
        "schema_version": 1,
        "workflow_validated": workflow_validated,
        "validation_scope": protocol.get("validation_scope") if workflow_validated else "contract-prototype-only",
        "claim": claim,
        "blocking_issues": blocking,
        "categories": category_results,
        "budget": {
            "consumed_cost_units": total_cost,
            "registered_batches": {
                batch_id: {
                    "contract": snapshots[0],
                    "consumed_cost_units": batch_costs.get(batch_id, 0.0),
                }
                for batch_id, snapshots in run_batches.items()
            },
        },
    }


def load_probe_run(run_dir: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, Any] | None]:
    probes_dir = run_dir / "probes"
    categories: dict[str, Any] = {}
    for category in REQUIRED_CATEGORIES:
        category_dir = probes_dir / category
        if not category_dir.is_dir():
            continue
        manifest_path = category_dir / "manifest.json"
        attempts: dict[str, dict[str, Any]] = {}
        for attempt_dir in sorted(category_dir.glob("attempt-*")):
            attempt_path = attempt_dir / "attempt.json"
            if attempt_path.is_file():
                attempts[attempt_dir.name] = _read_object(attempt_path)
        categories[category] = {
            "manifest": _read_object(manifest_path) if manifest_path.is_file() else {},
            "attempts": attempts,
        }
    current_dependencies = resolve_current_dependencies(run_dir)
    cross_path = probes_dir / "cross_probe_signoff.json"
    cross_signoff = _read_object(cross_path) if cross_path.is_file() else None
    return categories, current_dependencies, cross_signoff


def resolve_current_dependencies(run_dir: Path) -> dict[str, dict[str, Any]]:
    repo_root = Path(__file__).resolve().parent
    protocol_path = repo_root / "tests/fixtures/seedance25/probe-evidence/protocol-contract-v1.json"
    rubric_path = repo_root / "tests/fixtures/seedance25/probe-evidence/qa-rubric-v1.json"
    provenance_path = repo_root / "tests/fixtures/dandao-xiantu/provenance.json"
    protocol = _read_object(protocol_path)
    resolved: dict[str, dict[str, Any]] = {}
    for category, episode_id in REQUIRED_CATEGORIES.items():
        episode_dir = _probe_episode_dir(run_dir, episode_id)
        package_path = episode_dir / "seedance_generation_package.json"
        script_path = episode_dir / "script.txt"
        if not package_path.is_file() or not script_path.is_file():
            continue
        package = _read_object(package_path)
        cuts = package.get("cuts") if isinstance(package.get("cuts"), list) else []
        provider_requests = [
            cut.get("provider_request") for cut in cuts
            if isinstance(cut, dict) and isinstance(cut.get("provider_request"), dict)
        ]
        material_inputs = [
            item
            for cut in cuts if isinstance(cut, dict)
            for item in cut.get("material_inputs", []) if isinstance(item, dict)
        ]
        workflow_identity = package.get("workflow_identity") if isinstance(package.get("workflow_identity"), dict) else {}
        resolved[category] = {
            "resolved_workflow_hash": workflow_identity.get("resolved_workflow_hash"),
            "package_sha256": _file_sha256(package_path),
            "request_sha256": _canonical_hash({"provider_requests": provider_requests}),
            "materials_sha256": _canonical_hash({"material_inputs": material_inputs}),
            "provider_contract_version": package.get("provider_contract_version"),
            "manjuweb_schema_version": protocol.get("manjuweb_schema_version"),
            "protocol_sha256": _file_sha256(protocol_path),
            "rubric_sha256": _file_sha256(rubric_path),
            "provenance_sha256": _file_sha256(provenance_path),
            "episode_fixture_sha256": _file_sha256(script_path),
        }
    return resolved


def write_probe_run_status(
    run_dir: Path,
    *,
    protocol_path: Path,
    rubric_path: Path,
    authenticity_verifier: Callable[[dict[str, Any]], bool] | None = None,
    readiness_resolver: Callable[[Path], dict[str, Any]] | None = None,
) -> tuple[Path, Path, dict[str, Any]]:
    load_issue = ""
    try:
        categories, current_dependencies, cross_signoff = load_probe_run(run_dir)
    except Exception as exc:
        categories, current_dependencies, cross_signoff = {}, {}, None
        load_issue = f"invalid probe evidence: {exc}"
    payload = summarize_probe_run(
        categories,
        cross_probe_signoff=cross_signoff,
        protocol_path=protocol_path,
        rubric_path=rubric_path,
        current_dependencies_by_category=current_dependencies or None,
        authenticity_verifier=authenticity_verifier,
    )
    if load_issue:
        payload["blocking_issues"].insert(0, load_issue)
        payload["workflow_validated"] = False
        payload["validation_scope"] = "contract-prototype-only"
        payload["claim"] = "合同原型完成，视频工作流未验证。"
    payload["resolved_identity"] = {}
    readiness_episodes: dict[str, Any] = {}
    readiness_hashes: set[str] = set()
    required_current_layers = {
        "storyboard_valid", "asset_contract_valid", "handoff_schema_valid", "generation_ready"
    }

    def historical_readiness_snapshot(readiness: dict[str, Any]) -> dict[str, Any]:
        layers = readiness.get("layers") if isinstance(readiness.get("layers"), dict) else {}
        return {
            "schema_version": readiness.get("schema_version"),
            "profile": readiness.get("profile"),
            "resolved_workflow_hash": readiness.get("resolved_workflow_hash"),
            "layers": {
                name: layers.get(name)
                for name in sorted(required_current_layers)
            },
        }
    for category, episode_id in REQUIRED_CATEGORIES.items():
        episode_dir = _probe_episode_dir(run_dir, episode_id)
        readiness_path = episode_dir / "workflow_readiness.json"
        if not readiness_path.is_file():
            payload["blocking_issues"].append(
                f"missing current workflow readiness for {category}/{episode_id}"
            )
            continue
        try:
            readiness = _read_object(readiness_path)
        except Exception as exc:
            payload["blocking_issues"].append(
                f"invalid current workflow readiness for {category}/{episode_id}: {exc}"
            )
            continue
        try:
            if readiness_resolver is None:
                from seedance_material_handoff import summarize_workflow_readiness

                current_readiness = summarize_workflow_readiness(episode_dir)
            else:
                current_readiness = readiness_resolver(episode_dir)
        except Exception as exc:
            payload["blocking_issues"].append(
                f"cannot recompute current workflow readiness for {category}/{episode_id}: {exc}"
            )
            continue
        if historical_readiness_snapshot(readiness) != historical_readiness_snapshot(current_readiness):
            payload["blocking_issues"].append(
                f"stale current workflow readiness for {category}/{episode_id}; rerun episode workflow-status"
            )
        readiness = current_readiness
        readiness_episodes[category] = readiness
        if readiness.get("profile") != "seedance-2.5-horizontal-xianxia-3d-cg":
            payload["blocking_issues"].append(
                f"{category} current readiness profile mismatch"
            )
        readiness_hash = str(readiness.get("resolved_workflow_hash") or "")
        if not SHA256_RE.fullmatch(readiness_hash):
            payload["blocking_issues"].append(
                f"{category} current readiness resolved_workflow_hash is missing or invalid"
            )
        else:
            readiness_hashes.add(readiness_hash)
            current_hash = str(current_dependencies.get(category, {}).get("resolved_workflow_hash") or "")
            if readiness_hash != current_hash:
                payload["blocking_issues"].append(
                    f"{category} current readiness identity does not match current package dependency"
                )
        layers = readiness.get("layers") if isinstance(readiness.get("layers"), dict) else {}
        for layer_name in required_current_layers:
            if not isinstance(layers.get(layer_name), dict) or layers[layer_name].get("valid") is not True:
                payload["blocking_issues"].append(
                    f"{category} current readiness layer is blocked: {layer_name}"
                )
        if not payload["resolved_identity"]:
            payload["resolved_identity"] = {
                "profile": readiness.get("profile"),
                "resolved_workflow_hash": readiness.get("resolved_workflow_hash"),
            }
    if len(readiness_hashes) > 1:
        payload["blocking_issues"].append(
            "current episode readiness files do not share one resolved workflow identity"
        )
    for category, episode_id in REQUIRED_CATEGORIES.items():
        package_path = _probe_episode_dir(run_dir, episode_id) / "seedance_generation_package.json"
        if not package_path.is_file():
            continue
        try:
            package = _read_object(package_path)
        except Exception:
            continue
        identity = package.get("workflow_identity") if isinstance(package.get("workflow_identity"), dict) else {}
        if identity:
            payload["resolved_identity"].update({
                "profile": identity.get("video_profile") or payload["resolved_identity"].get("profile"),
                "resolved_workflow_hash": identity.get("resolved_workflow_hash"),
                "visual_style_preset": identity.get("visual_style_preset"),
                "visual_style_preset_version": identity.get("visual_style_preset_version"),
                "visual_style_preset_sha256": identity.get("visual_style_preset_sha256"),
                "project_pack_id": identity.get("project_pack_id"),
                "project_pack_version": identity.get("project_pack_version"),
                "project_pack_sha256": identity.get("project_pack_sha256"),
            })
            break
    payload["readiness"] = {"episodes": readiness_episodes}
    if len(readiness_episodes) != len(REQUIRED_CATEGORIES) or any(
        "readiness" in issue for issue in payload["blocking_issues"]
    ):
        payload["workflow_validated"] = False
        payload["validation_scope"] = "contract-prototype-only"
        payload["claim"] = "合同原型完成，视频工作流未验证。"
    payload["owner"] = "run_owner" if payload["workflow_validated"] else "readiness_owner"
    payload["next_action"] = (
        "retain promoted evidence and monitor dependency/environment drift"
        if payload["workflow_validated"]
        else (payload["blocking_issues"][0] if payload["blocking_issues"] else "complete probe evidence")
    )
    probes_dir = run_dir / "probes"
    probes_dir.mkdir(parents=True, exist_ok=True)
    json_path = probes_dir / "probe_status.json"
    report_path = probes_dir / "probe_status.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Seedance Probe Status", "",
        f"- workflow_validated: `{str(payload['workflow_validated']).lower()}`",
        f"- validation_scope: `{payload['validation_scope']}`",
        f"- claim: {payload['claim']}",
        f"- owner: `{payload['owner']}`",
        f"- next_action: {payload['next_action']}", "", "## Categories", "",
    ]
    if payload["resolved_identity"]:
        lines[7:7] = [
            "## Resolved identity", "",
            f"- profile: `{payload['resolved_identity'].get('profile')}`",
            f"- resolved_workflow_hash: `{payload['resolved_identity'].get('resolved_workflow_hash')}`",
            f"- visual_style_preset: `{payload['resolved_identity'].get('visual_style_preset')}`",
            f"- visual_style_preset_version: `{payload['resolved_identity'].get('visual_style_preset_version')}`",
            f"- visual_style_preset_sha256: `{payload['resolved_identity'].get('visual_style_preset_sha256')}`",
            f"- project_pack_id: `{payload['resolved_identity'].get('project_pack_id')}`",
            f"- project_pack_version: `{payload['resolved_identity'].get('project_pack_version')}`",
            f"- project_pack_sha256: `{payload['resolved_identity'].get('project_pack_sha256')}`",
            "",
        ]
    for category in REQUIRED_CATEGORIES:
        result = payload["categories"].get(category)
        if result:
            lines.append(
                f"- {category}: latest=`{result['latest_attempt_id']}`, "
                f"promoted=`{result['promoted_attempt_id']}`, valid=`{str(result['valid']).lower()}`, "
                f"attempt_count=`{result['attempt_count']}`, "
                f"consumed_cost_units=`{result['consumed_cost_units']}`"
            )
            lines.append(
                f"  - promoted_state=`{result['promoted_state']}`, "
                f"mechanical_qa=`{result['mechanical_qa_state']}`, "
                f"semantic_qa=`{result['semantic_qa_state']}`, "
                f"signoff=`{result['signoff_state']}`, stale=`{str(result['stale']).lower()}`"
            )
            for blocker in result.get("current_blockers", []):
                lines.append(f"  - current_blocker: {blocker}")
            failure_types = result.get("failure_types", {})
            failure_counts = {
                name: failure_types.count(name)
                for name in sorted(set(failure_types))
            } if isinstance(failure_types, list) else failure_types
            lines.append(
                "  - failure_types: "
                + (", ".join(f"{name}={count}" for name, count in sorted(failure_counts.items())) or "none")
            )
        else:
            lines.append(f"- {category}: `missing`")
    if payload["blocking_issues"]:
        lines.extend(["", "## Blockers", ""])
        lines.extend(f"- {issue}" for issue in payload["blocking_issues"])
    lines.extend(["", "## Budget", "", f"- consumed_cost_units: `{payload['budget']['consumed_cost_units']}`"])
    if payload["budget"]["registered_batches"]:
        for batch_id, batch in payload["budget"]["registered_batches"].items():
            lines.append(
                f"- {batch_id}: consumed=`{batch['consumed_cost_units']}`, "
                f"max=`{batch['contract'].get('max_total_cost_units', 'unknown')}`"
            )
    else:
        lines.append("- registered_batches: `none`")
    lines.extend(["", "## Readiness", ""])
    for category, readiness in payload["readiness"]["episodes"].items():
        lines.append(f"- {category}:")
        for layer_name, layer in readiness.get("layers", {}).items():
            lines.append(f"  - {layer_name}: `{layer.get('state', 'unknown')}`")
            for blocker in layer.get("blockers", []):
                lines.append(f"    - blocker: {blocker}")
        first_blocker = readiness.get("first_blocker")
        if isinstance(first_blocker, dict):
            lines.append(
                f"  - first_blocker: `{first_blocker.get('layer', 'unknown')}` — "
                f"{first_blocker.get('reason', 'unknown blocker')}"
            )
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return json_path, report_path, payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate and report Seedance probe evidence")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument(
        "--protocol", type=Path,
        default=Path("tests/fixtures/seedance25/probe-evidence/protocol-contract-v1.json"),
    )
    parser.add_argument(
        "--rubric", type=Path,
        default=Path("tests/fixtures/seedance25/probe-evidence/qa-rubric-v1.json"),
    )
    args = parser.parse_args(argv)
    _, _, payload = write_probe_run_status(
        args.run_dir.resolve(),
        protocol_path=args.protocol.resolve(),
        rubric_path=args.rubric.resolve(),
    )
    print(payload["claim"])
    return 0 if payload["workflow_validated"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
