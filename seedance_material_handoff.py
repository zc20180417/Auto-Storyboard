"""Deterministic Seedance 2.5 material handoff and package compilation.

This module never uploads to Ark and never calls a model. Auto-Storyboard owns
logical requirements and local-file integrity; ManJuWeb owns Ark upload state
and returns ``ark_sync_results.json``.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import re
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
PROFILE_ID = "seedance-2.5-live-vertical"
MODEL_ID = "doubao-seedance-2-5-260628"

REQUIREMENTS_FILE = "seedance_material_requirements.json"
LOCAL_MATERIALS_FILE = "seedance_local_materials.json"
ARK_SYNC_RESULTS_FILE = "ark_sync_results.json"
GENERATION_PACKAGE_FILE = "seedance_generation_package.json"

MEDIA_LIMITS = {"image": 30, "video": 10, "audio": 10}
TOTAL_MATERIAL_LIMIT = 50
MEDIA_TOKEN_PREFIX = {"image": "图片", "video": "视频", "audio": "音频"}

ROLE_CONTRACTS: dict[str, dict[str, Any]] = {
    "scene_reference": {
        "role": "scene_environment",
        "provides": ["space_layout", "materials", "lighting_state"],
        "excludes": ["character_identity", "action", "camera_motion"],
    },
    "character_reference": {
        "role": "character_identity",
        "provides": ["face", "hair", "age", "body_identity"],
        "excludes": ["wardrobe", "action", "camera_motion"],
    },
    "costume_reference": {
        "role": "costume_state",
        "provides": ["wardrobe", "accessories", "condition"],
        "excludes": ["face_identity", "action", "camera_motion"],
    },
    "prop_reference": {
        "role": "prop_identity",
        "provides": ["appearance", "material", "condition"],
        "excludes": ["character_identity", "action", "camera_motion"],
    },
    "composition_reference": {
        "role": "composition_reference",
        "provides": ["composition", "blocking", "screen_direction"],
        "excludes": ["identity_details", "dialogue", "audio"],
    },
}

PRIORITY_VALUES = {"primary": 100, "supporting": 50, "background": 10}
ARK_ASSET_ID_RE = re.compile(r"^asset://asset-[a-z0-9-]+$", re.IGNORECASE)
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
GROUP_HEADING_RE = re.compile(
    r"^===\s*\[cut_id:\s*[A-Za-z0-9-]+\]\s*第(?P<group>\d+)组[：:].*?===\s*$",
    re.MULTILINE,
)


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return payload


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _profile_for_episode(episode_dir: Path) -> str:
    return str(_episode_metadata(episode_dir).get("video_profile") or "").strip()


def _episode_metadata(episode_dir: Path) -> dict[str, Any]:
    metadata_path = episode_dir / "episode.json"
    if not metadata_path.is_file():
        return {}
    try:
        return _read_json(metadata_path)
    except Exception:
        return {}


def _material_key(binding: dict[str, Any]) -> str:
    state_id = str(binding.get("state_id") or "").strip()
    asset_id = str(binding.get("asset_id") or "").strip()
    if state_id and state_id.upper() != "BASE":
        return state_id
    return asset_id


def compile_material_requirements(episode_dir: Path) -> dict[str, Any]:
    index_path = episode_dir / "storyboard_index.json"
    bindings_path = episode_dir / "asset_bindings.json"
    if not index_path.is_file():
        raise ValueError("missing storyboard_index.json")
    if not bindings_path.is_file():
        raise ValueError("missing asset_bindings.json")
    if _profile_for_episode(episode_dir) != PROFILE_ID:
        raise ValueError(f"episode video_profile must be {PROFILE_ID}")

    index = _read_json(index_path)
    bindings = _read_json(bindings_path)
    project = str(index.get("project") or bindings.get("project") or "").strip()
    if not project:
        raise ValueError("storyboard_index.json/asset_bindings.json is missing project")
    binding_project = str(bindings.get("project") or "").strip()
    if binding_project and binding_project != project:
        raise ValueError(
            f"asset_bindings.json project {binding_project} does not match {project}"
        )
    episode_id = str(index.get("episode_id") or "").strip()
    if not episode_id:
        raise ValueError("storyboard_index.json is missing episode_id")
    binding_episode_id = str(bindings.get("episode_id") or "").strip()
    if binding_episode_id and binding_episode_id != episode_id:
        raise ValueError(
            f"asset_bindings.json episode_id {binding_episode_id} does not match {episode_id}"
        )

    valid_cut_ids = {
        str(cut.get("cut_id") or "").strip()
        for cut in index.get("cuts", [])
        if isinstance(cut, dict)
    }
    requirements: list[dict[str, Any]] = []
    seen_requirement_ids: set[str] = set()
    for position, binding in enumerate(bindings.get("bindings", []), start=1):
        if not isinstance(binding, dict):
            raise ValueError(f"asset_bindings.json binding {position} must be an object")
        cut_id = str(binding.get("cut_id") or "").strip()
        if cut_id not in valid_cut_ids:
            raise ValueError(f"binding {position} references unknown cut_id {cut_id or '<empty>'}")
        binding_role = str(binding.get("binding_role") or "").strip()
        role_contract = ROLE_CONTRACTS.get(binding_role)
        if role_contract is None:
            raise ValueError(f"binding {position} has unsupported binding_role {binding_role or '<empty>'}")
        material_key = _material_key(binding)
        if not material_key:
            raise ValueError(f"binding {position} is missing asset_id/state_id")

        requirement_id = str(binding.get("binding_id") or f"{episode_id}_REQ_{position:03d}").strip()
        if requirement_id in seen_requirement_ids:
            raise ValueError(f"duplicate requirement/binding id: {requirement_id}")
        seen_requirement_ids.add(requirement_id)

        requirement_mode = str(binding.get("required_for_generation") or "no").strip().lower()
        if requirement_mode not in {"yes", "no", "conditional"}:
            raise ValueError(
                f"binding {requirement_id} has invalid required_for_generation {requirement_mode}"
            )
        use_for_video = str(binding.get("use_for_video") or "").strip().lower()
        if use_for_video not in {"yes", "no", "conditional"}:
            raise ValueError(f"binding {requirement_id} has invalid use_for_video {use_for_video}")
        if use_for_video == "no":
            if requirement_mode == "yes":
                raise ValueError(
                    f"binding {requirement_id} cannot require a material when use_for_video=no"
                )
            continue
        reference_priority = str(binding.get("reference_priority") or "supporting").strip().lower()
        if reference_priority not in PRIORITY_VALUES:
            raise ValueError(
                f"binding {requirement_id} has invalid reference_priority {reference_priority}"
            )

        requirements.append(
            {
                "requirement_id": requirement_id,
                "cut_id": cut_id,
                "material_key": material_key,
                "media_type": "image",
                "role": role_contract["role"],
                "required": requirement_mode == "yes",
                "requirement_mode": requirement_mode,
                "priority": PRIORITY_VALUES[reference_priority],
                "provides": list(role_contract["provides"]),
                "excludes": list(role_contract["excludes"]),
                "asset_id": str(binding.get("asset_id") or "").strip(),
                "state_id": str(binding.get("state_id") or "BASE").strip() or "BASE",
                "source_binding_role": binding_role,
                "source": str(binding.get("source") or "").strip(),
                "note": str(binding.get("note") or "").strip(),
            }
        )

    requirements.sort(key=lambda item: (item["cut_id"], -item["priority"], item["requirement_id"]))
    if not requirements:
        raise ValueError(
            "asset_bindings.json has no video-eligible material bindings; "
            "at least one use_for_video=yes/conditional binding is required"
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "profile": PROFILE_ID,
        "project": project,
        "episode_id": episode_id,
        "source_hashes": {
            "storyboard_index_sha256": sha256_file(index_path),
            "asset_bindings_sha256": sha256_file(bindings_path),
        },
        "requirements": requirements,
    }


def _local_material_template(
    requirements: dict[str, Any],
    existing: dict[str, Any] | None,
) -> dict[str, Any]:
    if existing and (
        existing.get("project") != requirements.get("project")
        or existing.get("episode_id") != requirements.get("episode_id")
    ):
        existing = None
    existing_entries: dict[tuple[str, str], dict[str, Any]] = {}
    if existing:
        for item in existing.get("materials", []):
            if isinstance(item, dict):
                key = (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
                if all(key):
                    existing_entries[key] = item

    required_pairs = sorted(
        {
            (str(item["material_key"]), str(item["media_type"]))
            for item in requirements.get("requirements", [])
            if isinstance(item, dict)
        }
    )
    materials: list[dict[str, Any]] = []
    for material_key, media_type in required_pairs:
        existing_item = existing_entries.get((material_key, media_type))
        if existing_item:
            materials.append(existing_item)
            continue
        materials.append(
            {
                "material_key": material_key,
                "media_type": media_type,
                "source": {"kind": "missing"},
                "mime_type": "",
                "sha256": "",
                "authorization": {"status": "unconfirmed", "note": ""},
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "project": requirements.get("project", ""),
        "episode_id": requirements.get("episode_id", ""),
        "materials": materials,
    }


def export_material_handoff(episode_dir: Path) -> tuple[Path, Path]:
    requirements = compile_material_requirements(episode_dir)
    requirements_path = episode_dir / REQUIREMENTS_FILE
    local_path = episode_dir / LOCAL_MATERIALS_FILE
    existing_local = _read_json(local_path) if local_path.is_file() else None
    local_template = _local_material_template(requirements, existing_local)
    _write_json(requirements_path, requirements)
    _write_json(local_path, local_template)
    return requirements_path, local_path


def _resolve_material_file(registry_path: Path, source: dict[str, Any]) -> Path | None:
    raw_path = str(source.get("path") or "").strip()
    if not raw_path:
        return None
    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = registry_path.parent / candidate
    return candidate.resolve()


def _material_file_integrity(
    registry_path: Path,
    material: dict[str, Any],
) -> tuple[str | None, str | None]:
    declared_hash = str(material.get("sha256") or "").strip().lower()
    if not SHA256_RE.fullmatch(declared_hash):
        return None, "sha256 must be 64 lowercase hexadecimal characters"
    source = material.get("source")
    if not isinstance(source, dict):
        return None, "source must be an object"
    source_kind = str(source.get("kind") or "").strip()
    if source_kind == "local_file":
        file_path = _resolve_material_file(registry_path, source)
        if file_path is None or not file_path.is_file():
            return None, f"local file is missing: {source.get('path') or '<empty>'}"
        actual_hash = sha256_file(file_path)
        if actual_hash != declared_hash:
            return None, f"local file sha256 mismatch: expected {declared_hash}, got {actual_hash}"
        return actual_hash, None
    if source_kind == "public_url":
        url = str(source.get("url") or "").strip()
        if not url.startswith("https://"):
            return None, "public_url must use https://"
        return declared_hash, None
    if source_kind == "missing":
        return None, "material source is missing"
    return None, f"unsupported source kind: {source_kind or '<empty>'}"


def _extract_group_blocks(content: str) -> dict[int, str]:
    matches = list(GROUP_HEADING_RE.finditer(content))
    result: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        result[int(match.group("group"))] = content[match.start():end].strip()
    return result


def validate_material_handoff(
    episode_dir: Path,
    *,
    check_existing_package: bool = True,
) -> dict[str, Any]:
    final_path = episode_dir / "final.txt"
    index_path = episode_dir / "storyboard_index.json"
    bindings_path = episode_dir / "asset_bindings.json"
    requirements_path = episode_dir / REQUIREMENTS_FILE
    local_path = episode_dir / LOCAL_MATERIALS_FILE
    sync_path = episode_dir / ARK_SYNC_RESULTS_FILE
    package_path = episode_dir / GENERATION_PACKAGE_FILE
    issues: list[str] = []

    for path in (final_path, index_path, bindings_path, requirements_path, local_path):
        if not path.is_file():
            issues.append(f"missing {path.name}")
    if issues:
        return {"generation_ready": False, "issues": issues, "ready_materials": {}}

    if _profile_for_episode(episode_dir) != PROFILE_ID:
        issues.append(f"episode video_profile must be {PROFILE_ID}")

    try:
        index = _read_json(index_path)
        requirements = _read_json(requirements_path)
        local_registry = _read_json(local_path)
    except Exception as exc:
        return {
            "generation_ready": False,
            "issues": [f"invalid handoff JSON: {exc}"],
            "ready_materials": {},
        }

    expected_requirement_hashes = {
        "storyboard_index_sha256": sha256_file(index_path),
        "asset_bindings_sha256": sha256_file(bindings_path),
    }
    final_sha256 = sha256_file(final_path)
    if index.get("source_hashes", {}).get("final_txt_sha256") != final_sha256:
        issues.append("storyboard_index.json is stale for current final.txt; re-export it")
    if requirements.get("source_hashes") != expected_requirement_hashes:
        issues.append("seedance_material_requirements.json is stale; re-export it")
    try:
        expected_requirements = compile_material_requirements(episode_dir)
        if requirements != expected_requirements:
            issues.append(
                "seedance_material_requirements.json does not match current logical bindings; re-export it"
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        issues.append(f"cannot recompile logical material requirements: {exc}")
    if requirements.get("schema_version") != SCHEMA_VERSION:
        issues.append(f"material requirements schema_version must be {SCHEMA_VERSION}")
    if requirements.get("profile") != PROFILE_ID:
        issues.append(f"material requirements profile must be {PROFILE_ID}")
    if requirements.get("episode_id") != index.get("episode_id"):
        issues.append("material requirements episode_id does not match storyboard_index.json")
    if requirements.get("project") != index.get("project"):
        issues.append("material requirements project does not match storyboard_index.json")
    if local_registry.get("schema_version") != SCHEMA_VERSION:
        issues.append(f"local materials schema_version must be {SCHEMA_VERSION}")
    if local_registry.get("episode_id") != index.get("episode_id"):
        issues.append("local materials episode_id does not match storyboard_index.json")
    if local_registry.get("project") != index.get("project"):
        issues.append("local materials project does not match storyboard_index.json")

    metadata = _episode_metadata(episode_dir)
    video_resolution = str(metadata.get("video_resolution") or "720p").strip()
    if video_resolution not in {"480p", "720p"}:
        issues.append(f"episode video_resolution is unsupported: {video_resolution or '<empty>'}")

    requirement_items = [item for item in requirements.get("requirements", []) if isinstance(item, dict)]
    requirement_ids: set[str] = set()
    valid_cut_ids = {
        str(item.get("cut_id") or "")
        for item in index.get("cuts", [])
        if isinstance(item, dict)
    }
    for item in requirement_items:
        requirement_id = str(item.get("requirement_id") or "")
        if not requirement_id or requirement_id in requirement_ids:
            issues.append(f"duplicate or missing requirement_id: {requirement_id or '<empty>'}")
        requirement_ids.add(requirement_id)
        if item.get("cut_id") not in valid_cut_ids:
            issues.append(f"requirement {requirement_id} references unknown cut_id")
        if item.get("media_type") not in MEDIA_LIMITS:
            issues.append(f"requirement {requirement_id} has unsupported media_type")

    all_requirement_pairs = {
        (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        for item in requirement_items
    }
    required_pairs = {
        (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        for item in requirement_items
        if bool(item.get("required"))
    }

    local_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    verified_hashes: dict[tuple[str, str], str] = {}
    for item in local_registry.get("materials", []):
        if not isinstance(item, dict):
            issues.append("seedance_local_materials.json contains a non-object material")
            continue
        key = (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        if not all(key) or key in local_by_key:
            issues.append(f"duplicate or incomplete local material key: {key}")
            continue
        if key not in all_requirement_pairs:
            issues.append(f"local material {key[0]} has no logical requirement")
        forbidden_ark_fields = sorted(
            field
            for field in item
            if field.startswith("ark_") or field in {"arkAssetId", "assetId"}
        )
        if forbidden_ark_fields:
            issues.append(
                f"material {key[0]} contains ManJuWeb-owned fields: {', '.join(forbidden_ark_fields)}"
            )
        local_by_key[key] = item
        source = item.get("source")
        source_kind = str(source.get("kind") or "") if isinstance(source, dict) else ""
        optional_and_missing = key not in required_pairs and source_kind == "missing"
        authorization = item.get("authorization")
        auth_status = (
            str(authorization.get("status") or "").strip()
            if isinstance(authorization, dict)
            else ""
        )
        if auth_status != "confirmed" and not optional_and_missing:
            issues.append(f"material {key[0]} authorization is not confirmed")
        if not optional_and_missing:
            integrity_hash, integrity_error = _material_file_integrity(local_path, item)
            if integrity_error:
                issues.append(f"material {key[0]}: {integrity_error}")
            elif integrity_hash:
                verified_hashes[key] = integrity_hash

        mime_type = str(item.get("mime_type") or "").strip().lower()
        if not optional_and_missing and not mime_type.startswith(f"{key[1]}/"):
            guessed = ""
            source = item.get("source")
            if isinstance(source, dict) and source.get("kind") == "local_file":
                guessed = mimetypes.guess_type(str(source.get("path") or ""))[0] or ""
            issues.append(
                f"material {key[0]} mime_type {mime_type or '<empty>'} does not match {key[1]}"
                + (f" (guessed {guessed})" if guessed else "")
            )

    for key in sorted(all_requirement_pairs):
        if key not in local_by_key:
            issues.append(
                f"material {key[0]} is missing from seedance_local_materials.json"
            )

    sync_results: dict[str, Any] = {}
    if sync_path.is_file():
        try:
            sync_results = _read_json(sync_path)
        except Exception as exc:
            issues.append(f"invalid ark_sync_results.json: {exc}")
    else:
        issues.append("missing ark_sync_results.json")

    expected_sync_hashes = {
        "material_requirements_sha256": sha256_file(requirements_path),
        "local_materials_sha256": sha256_file(local_path),
    }
    if sync_results and sync_results.get("source_hashes") != expected_sync_hashes:
        issues.append("ark_sync_results.json is stale or belongs to another handoff")
    if sync_results and sync_results.get("schema_version") != SCHEMA_VERSION:
        issues.append(f"Ark sync results schema_version must be {SCHEMA_VERSION}")
    if sync_results and sync_results.get("authority") != "manjuweb":
        issues.append("ark_sync_results.json authority must be manjuweb")
    if sync_results and sync_results.get("episode_id") != index.get("episode_id"):
        issues.append("Ark sync results episode_id does not match storyboard_index.json")
    if sync_results and sync_results.get("project") != index.get("project"):
        issues.append("Ark sync results project does not match storyboard_index.json")

    sync_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    asset_id_hashes: dict[str, str] = {}
    for item in sync_results.get("materials", []) if sync_results else []:
        if not isinstance(item, dict):
            issues.append("ark_sync_results.json contains a non-object material")
            continue
        key = (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        if not all(key) or key in sync_by_key:
            issues.append(f"duplicate or incomplete Ark sync material key: {key}")
            continue
        sync_by_key[key] = item
        declared_hash = str(item.get("sha256") or "").lower()
        local_hash = verified_hashes.get(key)
        if local_hash and declared_hash != local_hash:
            issues.append(f"Ark sync hash mismatch for material {key[0]}")
        ark_asset_id = str(item.get("ark_asset_id") or "").strip()
        ark_status = str(item.get("ark_status") or "").strip().lower()
        if ark_status == "active" and not ARK_ASSET_ID_RE.fullmatch(ark_asset_id):
            issues.append(f"material {key[0]} has invalid active Ark asset ID")
        if ark_asset_id:
            prior_hash = asset_id_hashes.get(ark_asset_id)
            if prior_hash and prior_hash != declared_hash:
                issues.append(f"Ark asset ID {ark_asset_id} is bound to multiple file hashes")
            asset_id_hashes[ark_asset_id] = declared_hash

    ready_materials: dict[str, dict[str, Any]] = {}
    for key in required_pairs:
        sync_item = sync_by_key.get(key)
        if not sync_item or str(sync_item.get("ark_status") or "").lower() != "active":
            issues.append(f"required material {key[0]} is not Active in ManJuWeb Ark results")

    for key, sync_item in sync_by_key.items():
        if (
            key in verified_hashes
            and str(sync_item.get("sha256") or "").lower() == verified_hashes[key]
            and str(sync_item.get("ark_status") or "").lower() == "active"
            and ARK_ASSET_ID_RE.fullmatch(str(sync_item.get("ark_asset_id") or ""))
        ):
            ready_materials[f"{key[1]}:{key[0]}"] = sync_item

    for cut_id in sorted(valid_cut_ids):
        cut_requirements = [item for item in requirement_items if item.get("cut_id") == cut_id]
        ready_keys = {
            f"{item.get('media_type')}:{item.get('material_key')}"
            for item in cut_requirements
            if f"{item.get('media_type')}:{item.get('material_key')}" in ready_materials
        }
        if not ready_keys:
            issues.append(f"cut {cut_id} has no Active multimodal material")
        counts = {media_type: 0 for media_type in MEDIA_LIMITS}
        for ready_key in ready_keys:
            media_type = ready_key.split(":", 1)[0]
            counts[media_type] += 1
        for media_type, limit in MEDIA_LIMITS.items():
            if counts[media_type] > limit:
                issues.append(
                    f"cut {cut_id} has {counts[media_type]} {media_type} materials; limit is {limit}"
                )
        if sum(counts.values()) > TOTAL_MATERIAL_LIMIT:
            issues.append(
                f"cut {cut_id} has {sum(counts.values())} materials; total limit is {TOTAL_MATERIAL_LIMIT}"
            )

    current_integrity = {
        "final_txt_sha256": final_sha256,
        "storyboard_index_sha256": sha256_file(index_path),
        "material_requirements_sha256": sha256_file(requirements_path),
        "local_materials_sha256": sha256_file(local_path),
        "ark_sync_results_sha256": sha256_file(sync_path) if sync_path.is_file() else "",
    }
    if check_existing_package and package_path.is_file():
        try:
            package = _read_json(package_path)
            package_integrity = package.get("source_integrity")
            if not isinstance(package_integrity, dict) or any(
                package_integrity.get(key) != value for key, value in current_integrity.items()
            ):
                issues.append("seedance_generation_package.json is stale; re-export it")
        except Exception as exc:
            issues.append(f"invalid seedance_generation_package.json: {exc}")

    return {
        "generation_ready": not issues,
        "issues": issues,
        "ready_materials": ready_materials,
        "source_integrity": current_integrity,
        "index": index,
        "requirements": requirements,
        "local_registry": local_registry,
        "sync_results": sync_results,
    }


def build_generation_package(episode_dir: Path) -> dict[str, Any]:
    validation = validate_material_handoff(episode_dir, check_existing_package=False)
    metadata = _episode_metadata(episode_dir)
    video_resolution = str(metadata.get("video_resolution") or "720p").strip()
    final_path = episode_dir / "final.txt"
    content = final_path.read_text(encoding="utf-8", errors="replace") if final_path.is_file() else ""
    group_blocks = _extract_group_blocks(content)
    index = validation.get("index") if isinstance(validation.get("index"), dict) else {}
    requirements = (
        validation.get("requirements")
        if isinstance(validation.get("requirements"), dict)
        else {"requirements": []}
    )
    ready_materials = validation.get("ready_materials", {})
    requirement_items = [
        item for item in requirements.get("requirements", []) if isinstance(item, dict)
    ]

    cuts: list[dict[str, Any]] = []
    for cut in index.get("cuts", []) if isinstance(index, dict) else []:
        if not isinstance(cut, dict):
            continue
        cut_id = str(cut.get("cut_id") or "")
        group_index = int(cut.get("group_index") or 0)
        cut_requirements = sorted(
            [item for item in requirement_items if item.get("cut_id") == cut_id],
            key=lambda item: (-int(item.get("priority") or 0), str(item.get("requirement_id") or "")),
        )
        selected: list[tuple[dict[str, Any], dict[str, Any]]] = []
        seen_materials: set[str] = set()
        for requirement in cut_requirements:
            lookup_key = f"{requirement.get('media_type')}:{requirement.get('material_key')}"
            sync_item = ready_materials.get(lookup_key)
            if not isinstance(sync_item, dict) or lookup_key in seen_materials:
                continue
            seen_materials.add(lookup_key)
            selected.append((requirement, sync_item))

        counters = {media_type: 0 for media_type in MEDIA_LIMITS}
        material_inputs: list[dict[str, Any]] = []
        prompt_lines: list[str] = []
        for requirement, sync_item in selected:
            media_type = str(requirement.get("media_type"))
            counters[media_type] += 1
            token = f"@{MEDIA_TOKEN_PREFIX[media_type]}{counters[media_type]}"
            material_inputs.append(
                {
                    "token": token,
                    "material_key": requirement.get("material_key"),
                    "media_type": media_type,
                    "role": requirement.get("role"),
                    "ark_asset_id": sync_item.get("ark_asset_id"),
                    "sha256": sync_item.get("sha256"),
                    "provides": requirement.get("provides", []),
                    "excludes": requirement.get("excludes", []),
                }
            )
            prompt_lines.append(
                f"- {token}（{requirement.get('role')}）：提供 "
                f"{', '.join(requirement.get('provides', [])) or 'specified reference'}；"
                f"不参考 {', '.join(requirement.get('excludes', [])) or 'unspecified attributes'}。"
            )

        base_prompt = group_blocks.get(group_index, "")
        prompt = base_prompt
        if prompt_lines:
            prompt = f"{base_prompt}\n\n多模态素材职责：\n" + "\n".join(prompt_lines)
        cut_issues = [
            issue
            for issue in validation.get("issues", [])
            if cut_id in issue or issue.startswith("missing ") or "stale" in issue
        ]
        if not material_inputs:
            cut_issues.append(f"cut {cut_id} has no compiled Active material input")
        cut_ready = not cut_issues and bool(material_inputs)
        reference_image_slots = [
            {
                "type": "ark",
                "assetId": item["ark_asset_id"],
                "name": item["material_key"],
                "source": "trusted-material",
                "entryMode": "uploaded",
                "status": "active",
            }
            for item in material_inputs
            if item["media_type"] == "image"
        ]
        cuts.append(
            {
                "cut_id": cut_id,
                "group_index": group_index,
                "duration_sec": cut.get("duration_sec"),
                "generation_ready": cut_ready,
                "blocking_issues": list(dict.fromkeys(cut_issues)),
                "material_inputs": material_inputs,
                "request_draft": {
                    "model": MODEL_ID,
                    "video_task_type": "multimodal_generation",
                    "prompt": prompt,
                    "duration": cut.get("duration_sec"),
                    "ratio": "9:16",
                    "resolution": video_resolution,
                    "fps": 24,
                    "generateAudio": True,
                    "referenceImageSlots": reference_image_slots,
                    "referenceVideos": [],
                    "referenceAudios": [],
                },
            }
        )

    package_ready = bool(cuts) and validation.get("generation_ready") is True and all(
        cut["generation_ready"] for cut in cuts
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "profile": PROFILE_ID,
        "model": MODEL_ID,
        "project": index.get("project", "") if isinstance(index, dict) else "",
        "episode_id": index.get("episode_id", "") if isinstance(index, dict) else "",
        "generation_ready": package_ready,
        "submit_allowed": package_ready,
        "blocking_issues": list(dict.fromkeys(validation.get("issues", []))),
        "source_integrity": validation.get("source_integrity", {}),
        "stale_if_any_source_hash_changes": True,
        "cuts": cuts,
    }


def write_generation_package(episode_dir: Path, output_path: Path | None = None) -> Path:
    path = output_path or (episode_dir / GENERATION_PACKAGE_FILE)
    _write_json(path, build_generation_package(episode_dir))
    return path
