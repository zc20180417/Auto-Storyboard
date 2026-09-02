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
HORIZONTAL_XIANXIA_PROFILE_ID = "seedance-2.5-horizontal-xianxia-3d-cg"
SUPPORTED_PROFILE_IDS = {PROFILE_ID, HORIZONTAL_XIANXIA_PROFILE_ID}
MODEL_ID = "doubao-seedance-2-5-260628"

REQUIREMENTS_FILE = "seedance_material_requirements.json"
LOCAL_MATERIALS_FILE = "seedance_local_materials.json"
ARK_SYNC_RESULTS_FILE = "ark_sync_results.json"
GENERATION_PACKAGE_FILE = "seedance_generation_package.json"
SUBMISSION_PROMPTS_FILE = "seedance_submission_prompts.md"
READINESS_FILE = "workflow_readiness.json"
READINESS_REPORT_FILE = "workflow_readiness.md"
ASSET_VALIDATION_FILE = "asset_validation.json"

HORIZONTAL_REVIEW_COVERAGE_KEYS = {
    "script_fidelity", "format", "timing_math", "dialogue_pacing", "dialogue_direction",
    "horizontal_composition", "screen_direction", "blocking_continuity",
    "handoff_continuity", "prop_continuity", "physical_continuity",
    "generation_density", "camera_motion", "xianxia_vfx_provenance",
    "native_audio", "audio_mouth_sync", "visual_style",
    "material_boundary", "prompt_pollution",
}

MEDIA_LIMITS = {"image": 30, "video": 10, "audio": 10}
TOTAL_MATERIAL_LIMIT = 50
MEDIA_TOKEN_PREFIX = {"image": "图片", "video": "视频", "audio": "音频"}
# Version 2 is the asset-first, timeline-only prompt contract.  The previous
# version exposed separate visual-peak, camera, and execution sections; those
# duplicated instructions already present in the timeline and made the model
# choose between competing descriptions.
SUBMISSION_PROMPT_CONTRACT_VERSION = 2

# The logical asset type comes from the asset-extractor binding table.  The
# binding role is only a fallback because older tables did not always retain
# ``asset_type`` in the compiled requirement.  Keep these labels stable: they
# are the human-facing grouping shown before the timeline in a Seedance
# submission prompt.
ASSET_CATEGORY_LABELS = {
    "character": "人物资产",
    "character_identity": "人物资产",
    "costume": "人物资产",
    "costume_state": "人物资产",
    "scene": "场景资产",
    "scene_environment": "场景资产",
    "composition": "场景资产",
    "composition_reference": "场景资产",
    "prop": "道具与关键视觉资产",
    "prop_identity": "道具与关键视觉资产",
    "effect": "道具与关键视觉资产",
}

REFERENCE_PROVIDES_ZH = {
    "face": "脸型",
    "hair": "发型",
    "age": "年龄段",
    "body_identity": "体态与身份稳定特征",
    "wardrobe": "服装",
    "accessories": "配饰",
    "condition": "当前状态",
    "space_layout": "空间布局",
    "materials": "材质",
    "lighting_state": "光线状态",
    "appearance": "外观",
    "material": "材质",
    "composition": "构图关系",
    "blocking": "站位调度",
    "screen_direction": "画面方向",
}

REFERENCE_EXCLUDES_ZH = {
    "character_identity": "人物身份",
    "face_identity": "脸部身份",
    "wardrobe": "服装",
    "action": "动作",
    "camera_motion": "运镜",
    "identity_details": "身份细节",
    "dialogue": "对白",
    "audio": "声音",
}

GROUP_PROMPT_FIELDS = (
    "人物",
    "场景",
    "道具/关键视觉资产",
    "道具",
    "组间承接",
    "横屏构图/调度",
    "镜头描述",
    "光影设计",
    "本镜估算时长",
    "组尾衔接",
    "画面风格",
    "--neg",
)
# These labels remain in the parser regex solely as migration boundaries for
# old masters; they are never emitted or copied into a new submission prompt.
GROUP_PROMPT_FIELD_RE = re.compile(
    r"(?m)^\s*(?:\*\*)?(?P<label>道具/关键视觉资产|视觉峰值/特效重点|Seedance执行提示补充|"
    r"横屏构图/调度|本镜估算时长|一句话概述|镜头描述|光影设计|组间承接|组尾衔接|"
    r"画面风格|运镜强化词|人物|场景|道具|--neg)"
    r"(?:\*\*)?\s*[：:]\s*"
)
SHOT_LINE_RE = re.compile(r"(?m)^\s*(?P<group>\d+)\s*-\s*(?P<shot>\d+)\s*$")

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


def _handoff_schema_version(profile: str) -> int:
    return 2 if profile == HORIZONTAL_XIANXIA_PROFILE_ID else SCHEMA_VERSION


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
    profile = _profile_for_episode(episode_dir)
    if profile not in SUPPORTED_PROFILE_IDS:
        raise ValueError(
            "episode video_profile must be one of: " + ", ".join(sorted(SUPPORTED_PROFILE_IDS))
        )

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
        media_type = "image"
        if profile == HORIZONTAL_XIANXIA_PROFILE_ID:
            media_type = str(binding.get("media_type") or "image").strip().lower()
            if media_type not in MEDIA_LIMITS:
                raise ValueError(
                    f"binding {requirement_id} has unsupported media_type {media_type or '<empty>'}"
                )

        asset_type = str(binding.get("asset_type") or "").strip().lower()
        if not asset_type:
            asset_type = {
                "character_reference": "character",
                "costume_reference": "costume",
                "scene_reference": "scene",
                "prop_reference": "prop",
                "composition_reference": "composition",
            }.get(binding_role, "composition")

        requirements.append(
            {
                "requirement_id": requirement_id,
                "cut_id": cut_id,
                "material_key": material_key,
                "media_type": media_type,
                "asset_type": asset_type,
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
    payload = {
        "schema_version": _handoff_schema_version(profile),
        "profile": profile,
        "project": project,
        "episode_id": episode_id,
        "source_hashes": {
            "storyboard_index_sha256": sha256_file(index_path),
            "asset_bindings_sha256": sha256_file(bindings_path),
        },
        "requirements": requirements,
    }
    if profile == HORIZONTAL_XIANXIA_PROFILE_ID:
        workflow_identity = index.get("workflow_identity")
        if not isinstance(workflow_identity, dict):
            raise ValueError("horizontal xianxia storyboard_index.json must include workflow_identity")
        if bindings.get("workflow_identity") != workflow_identity:
            raise ValueError("asset_bindings.json workflow_identity must match storyboard_index.json")
        payload["workflow_identity"] = workflow_identity
    return payload


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

    payload = {
        "schema_version": requirements.get("schema_version", SCHEMA_VERSION),
        "project": requirements.get("project", ""),
        "episode_id": requirements.get("episode_id", ""),
        "materials": materials,
    }
    if requirements.get("profile") == HORIZONTAL_XIANXIA_PROFILE_ID:
        payload = {
            "schema_version": 2,
            "profile": HORIZONTAL_XIANXIA_PROFILE_ID,
            "project": payload["project"],
            "episode_id": payload["episode_id"],
            "materials": payload["materials"],
        }
    return payload


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


def _group_field_value(block: str, label: str) -> str:
    """Return one group-level field, including wrapped continuation lines.

    The storyboard master is intentionally human-readable and has evolved
    between runs (bold labels, Chinese/ASCII colons, and wrapped hero bullets).
    Parsing by the next labelled field keeps the compiler deterministic without
    imposing a second JSON-shaped prompt format on workers.
    """
    aliases = {"道具/关键视觉资产": {"道具/关键视觉资产", "道具"}}
    wanted = aliases.get(label, {label})
    matches = list(GROUP_PROMPT_FIELD_RE.finditer(block))
    for index, match in enumerate(matches):
        if match.group("label") not in wanted:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        value = block[match.end():end]
        value = re.sub(r"(?m)^\s*===\s*第\d+组结束\s*===\s*$", "", value)
        return value.strip()
    return ""


def _asset_category(requirement: dict[str, Any]) -> str:
    asset_type = str(requirement.get("asset_type") or "").strip().lower()
    role = str(requirement.get("source_binding_role") or requirement.get("role") or "").strip().lower()
    return ASSET_CATEGORY_LABELS.get(asset_type) or ASSET_CATEGORY_LABELS.get(role) or "场景资产"


def _zh_reference_terms(values: Any, mapping: dict[str, str]) -> list[str]:
    if not isinstance(values, (list, tuple)):
        return []
    result: list[str] = []
    for value in values:
        key = str(value).strip()
        if not key:
            continue
        translated = mapping.get(key, key)
        if translated not in result:
            result.append(translated)
    return result


def _asset_prompt_line(item: dict[str, Any]) -> str:
    token = str(item.get("reference_token") or "").strip()
    category = _asset_category(item)
    asset_type = str(item.get("asset_type") or "").strip() or "未标注类型"
    material_key = str(item.get("material_key") or "").strip() or "未命名素材"
    note = str(item.get("note") or "").strip()
    label = note or material_key
    provides = _zh_reference_terms(item.get("provides"), REFERENCE_PROVIDES_ZH)
    excludes = _zh_reference_terms(item.get("excludes"), REFERENCE_EXCLUDES_ZH)
    provides_text = "、".join(provides) or "该素材已明确的静态外观"
    excludes_text = "、".join(excludes) or "动作、连续性和未明确的动态属性"
    return (
        f"- {token}｜{label}（逻辑键：{material_key}；类型：{asset_type}；{category}）："
        f"只参考{provides_text}；不参考{excludes_text}。"
    )


HORIZONTAL_OVERALL_STYLE_PROMPT = (
    "横屏16:9、720p，高质量国漫3D CG；整体画风为‘写实材质＋克制卡通轮廓’：亚洲骨相、"
    "适度动漫五官与稳定口型，可信PBR材质叠加少量手绘纹理，轮廓线清晰但克制稳定，"
    "东方低饱和色盘，以石青、黛青、灰绿、赭石、旧金、玉白建立统一世界；电影级布光和自然景深，"
    "景别按信息量和主体可读性自主选择，保持脸、手、发型体块、衣缘、关键器物和左右空间关系可读。"
    "仙侠特效必须遵循‘来源→形态→路径→作用对象→反馈→收束→声音’的完整语义链，"
    "有剧情来源、照明反馈和结果状态，不压制特效本身也不遮挡主体；原生音频保留对白口型、"
    "必要环境底噪、动作拟音和特效声；无字幕、无配乐。"
)


def _parse_shot_duration(segment: str) -> int | None:
    duration_text = _group_field_value(segment, "本镜估算时长")
    match = re.search(r"(?<!\d)(\d+)\s*秒", duration_text)
    if match:
        return int(match.group(1))
    # Legacy drafts sometimes put only a 0-4s range in the shot heading/body.
    ranges = re.findall(r"(?<!\d)(\d+)\s*[-–—]\s*(\d+)\s*秒", segment)
    if ranges:
        start, end = (int(value) for value in ranges[-1])
        if end > start:
            return end - start
    return None


def _extract_prompt_shots(block: str) -> list[dict[str, Any]]:
    """Extract shot prose from the current horizontal master.

    Bare ``N-M`` labels are the current contract.  A small legacy fallback is
    retained so an already-bound older package can be recompiled while workers
    migrate; it never changes the final.txt contract itself.
    """
    matches = list(SHOT_LINE_RE.finditer(block))
    shots: list[dict[str, Any]] = []
    if matches:
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
            segment = block[match.end():end]
            description = _group_field_value(segment, "镜头描述")
            lighting = _group_field_value(segment, "光影设计")
            if description:
                shots.append(
                    {
                        "label": f"{match.group('group')}-{match.group('shot')}",
                        "description": description,
                        "lighting": lighting,
                        "duration": _parse_shot_duration(segment),
                    }
                )
        return shots

    legacy_re = re.compile(r"(?m)^\s*(?:\*\*)?镜头\s*(?P<label>[^：:\n]+)[：:]\s*(?P<head>.*)$")
    legacy_matches = list(legacy_re.finditer(block))
    for index, match in enumerate(legacy_matches):
        end = legacy_matches[index + 1].start() if index + 1 < len(legacy_matches) else len(block)
        segment = block[match.end():end]
        description = _group_field_value(segment, "镜头描述")
        if not description:
            description = (match.group("head") + " " + segment).strip()
        shots.append(
            {
                "label": match.group("label").strip(),
                "description": description,
                "lighting": _group_field_value(segment, "光影设计"),
                "duration": _parse_shot_duration(segment),
            }
        )
    return shots


def _timeline_lines(
    block: str,
    expected_duration: int | None,
    *,
    strict: bool = False,
) -> list[str]:
    """Compile shot prose into one gap-free integer-second timeline.

    ``strict=True`` is the v2 Seedance 2.5 path: a malformed master is an
    error, never something to repair silently at submission time.  The
    non-strict branch remains available for migration tooling that needs to
    inspect an older bound package without changing its historical behavior.
    """
    shots = _extract_prompt_shots(block)
    if not shots:
        if strict:
            raise ValueError("timeline-only prompt contains no parseable shots")
        return [
            f"0-{expected_duration}秒：按母版中已写明的连续镜头执行。"
            if expected_duration
            else "按母版中已写明的连续镜头执行。"
        ]

    durations = [int(item["duration"]) if item.get("duration") is not None else None for item in shots]
    if strict:
        if expected_duration is None:
            raise ValueError("timeline-only prompt requires an explicit cut duration")
        if (
            isinstance(expected_duration, bool)
            or not isinstance(expected_duration, int)
            or not 4 <= expected_duration <= 30
        ):
            raise ValueError("timeline-only prompt expected duration must be an integer from 4 through 30")
        missing = [item["label"] for item in shots if item.get("duration") is None]
        if missing:
            raise ValueError(
                "timeline-only prompt requires an explicit integer 本镜估算时长 for "
                + ", ".join(str(label) for label in missing)
            )
        if any(int(value or 0) <= 0 for value in durations):
            raise ValueError("timeline-only prompt shot durations must be positive integers")
        if expected_duration is not None and sum(int(value or 0) for value in durations) != expected_duration:
            raise ValueError(
                "timeline-only prompt shot durations sum to "
                f"{sum(int(value or 0) for value in durations)} seconds, "
                f"but the cut declares {expected_duration} seconds"
            )

    if expected_duration is not None:
        known_total = sum(value for value in durations if value is not None)
        missing = [index for index, value in enumerate(durations) if value is None]
        if missing:
            remaining = max(expected_duration - known_total, len(missing))
            base, extra = divmod(remaining, len(missing))
            for offset, index in enumerate(missing):
                durations[index] = max(1, base + (1 if offset < extra else 0))
        delta = expected_duration - sum(int(value or 0) for value in durations)
        if not strict:
            # Valid masters already add up.  For a legacy draft, put a small
            # rounding/remainder correction on the final shot so the prompt
            # still has one gap-free 0..group_duration timeline.
            if durations:
                durations[-1] = max(1, int(durations[-1] or 1) + delta)
    else:
        durations = [int(value or 1) for value in durations]

    lines: list[str] = []
    cursor = 0
    for shot, duration in zip(shots, durations):
        end = cursor + int(duration)
        line = f"{cursor}-{end}秒（镜头{shot['label']}）：{shot['description']}"
        if shot.get("lighting"):
            line += f"；光影设计：{shot['lighting']}"
        lines.append(line)
        cursor = end
    return lines


def _compact_negative_prompt(value: str) -> str:
    value = re.sub(r"^\s*--neg\s*[：:]?\s*", "", value.strip(), flags=re.IGNORECASE)
    parts: list[str] = []
    for raw in re.split(r"[；;\n]+", value):
        item = re.sub(r"^\s*[-*]\s*", "", raw).strip(" ，,。")
        if item and item not in parts:
            parts.append(item)
    return "；".join(parts[:5])


def build_submission_prompt(
    group_block: str,
    material_inputs: list[dict[str, Any]],
    *,
    duration: int | None = None,
    strict_timeline: bool = False,
) -> str:
    """Compile the asset-first, timeline-only prompt for the provider call.

    The master may still contain legacy group-level fields while a run is being
    migrated.  They are deliberately ignored here: visual events, sound and
    execution constraints live in the shot timeline.  Camera movement is left
    to Seedance 2.5 unless the master explicitly carries a constraint needed
    for story/axis/continuity, so the model receives one authoritative
    description rather than duplicated camera instructions.
    The v2 package path opts into strict compilation explicitly.  Keeping the
    direct helper's default non-strict preserves its migration/inspection use
    for older bound masters; callers that are about to submit a new package
    must pass ``strict_timeline=True`` so malformed or mismatched shot
    durations raise instead of being silently redistributed.
    """
    grouped: dict[str, list[dict[str, Any]]] = {
        "人物资产": [],
        "场景资产": [],
        "道具与关键视觉资产": [],
    }
    for item in material_inputs:
        grouped.setdefault(_asset_category(item), []).append(item)

    lines: list[str] = []
    for category in ("人物资产", "场景资产", "道具与关键视觉资产"):
        lines.append(f"【{category}】")
        if grouped[category]:
            lines.extend(_asset_prompt_line(item) for item in grouped[category])
        else:
            lines.append("- 本组暂无已绑定的该类素材；不得凭空补入资产。")
        lines.append("")

    lines.extend(
        [
            "【整体画风说明】",
            HORIZONTAL_OVERALL_STYLE_PROMPT,
        ]
    )
    lines.append("")

    handoff = _group_field_value(group_block, "组间承接")
    lines.extend(
        [
            "【组间空间衔接】",
            "上一组世界末态／本组开场空间锚点："
            + (handoff or "当前组为开场，按母版已建立的空间事实起镜。"),
            "连续性真源是文字世界状态和当前镜头明确末态；尾帧仅作可选局部参考。"
            "继承人物位置、朝向、视线、动作停点、画外在场者、关键道具归属与状态、"
            "VFX持续/收束状态、轴线、机位、光线和声场；状态不可确认时先用稳定的空间重建镜头恢复关系，不猜测。",
            "",
        ]
    )

    composition = _group_field_value(group_block, "横屏构图/调度")
    if composition:
        lines.extend(["【横屏空间与调度】", composition, ""])

    lines.append("【连续时间轴】")
    lines.extend(_timeline_lines(group_block, duration, strict=strict_timeline))
    lines.append("")

    tail = _group_field_value(group_block, "组尾衔接")
    if tail:
        lines.extend(["【组尾世界状态】", tail, ""])

    negative = _compact_negative_prompt(_group_field_value(group_block, "--neg"))
    lines.extend(
        [
            "【负面约束（--neg）】",
            negative or "只避免本组明确的动作、空间、道具或特效连续性错误。",
        ]
    )
    return "\n".join(lines).strip()


def _validate_material_handoff_v1(
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


def _validate_material_handoff_v2(
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
    schema_blockers: list[str] = []
    generation_blockers: list[str] = []
    submission_blockers: list[str] = []

    for path in (final_path, index_path, bindings_path, requirements_path, local_path):
        if not path.is_file():
            schema_blockers.append(f"missing {path.name}")
    if schema_blockers:
        return {
            "handoff_schema_valid": False,
            "generation_ready": False,
            "submit_allowed": False,
            "schema_blockers": schema_blockers,
            "generation_blockers": [],
            "submission_blockers": ["local handoff schema is invalid"],
            "issues": schema_blockers + ["local handoff schema is invalid"],
            "ready_materials": {},
        }

    try:
        index = _read_json(index_path)
        bindings = _read_json(bindings_path)
        requirements = _read_json(requirements_path)
        local_registry = _read_json(local_path)
    except Exception as exc:
        schema_blockers.append(f"invalid handoff JSON: {exc}")
        return {
            "handoff_schema_valid": False,
            "generation_ready": False,
            "submit_allowed": False,
            "schema_blockers": schema_blockers,
            "generation_blockers": [],
            "submission_blockers": ["local handoff schema is invalid"],
            "issues": schema_blockers + ["local handoff schema is invalid"],
            "ready_materials": {},
        }

    metadata = _episode_metadata(episode_dir)
    if _profile_for_episode(episode_dir) != HORIZONTAL_XIANXIA_PROFILE_ID:
        schema_blockers.append(f"episode video_profile must be {HORIZONTAL_XIANXIA_PROFILE_ID}")
    expected_metadata = {
        "provider_contract_version": 1,
        "provider_task_mapping": {"field": "omni_reference_task_type", "value": "reference"},
        "video_resolution": "720p",
        "video_aspect_ratio": "16:9",
        "generate_audio": True,
        "video_task_type": "multimodal_generation",
    }
    for field, expected in expected_metadata.items():
        if metadata.get(field) != expected:
            schema_blockers.append(
                f"episode {field} mismatch: actual={metadata.get(field)!r}; expected={expected!r}"
            )

    final_sha256 = sha256_file(final_path)
    final_content = final_path.read_text(encoding="utf-8", errors="replace")
    group_blocks = _extract_group_blocks(final_content)
    if index.get("source_hashes", {}).get("final_txt_sha256") != final_sha256:
        schema_blockers.append("storyboard_index.json is stale for current final.txt; re-export it")
    workflow_identity = index.get("workflow_identity")
    if index.get("schema_version") != 2 or not isinstance(workflow_identity, dict):
        schema_blockers.append("horizontal xianxia storyboard_index.json must use schema_version=2 with workflow_identity")
    elif not SHA256_RE.fullmatch(str(workflow_identity.get("resolved_workflow_hash") or "")):
        schema_blockers.append("storyboard workflow_identity resolved_workflow_hash must be a SHA-256 digest")
    elif bindings.get("workflow_identity") != workflow_identity:
        schema_blockers.append("asset_bindings.json workflow_identity does not match storyboard_index.json")

    expected_requirement_hashes = {
        "storyboard_index_sha256": sha256_file(index_path),
        "asset_bindings_sha256": sha256_file(bindings_path),
    }
    if requirements.get("source_hashes") != expected_requirement_hashes:
        schema_blockers.append("seedance_material_requirements.json is stale; re-export it")
    try:
        if requirements != compile_material_requirements(episode_dir):
            schema_blockers.append(
                "seedance_material_requirements.json does not match current logical bindings; re-export it"
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        schema_blockers.append(f"cannot recompile logical material requirements: {exc}")
    if requirements.get("schema_version") != 2 or requirements.get("profile") != HORIZONTAL_XIANXIA_PROFILE_ID:
        schema_blockers.append("material requirements must use horizontal xianxia schema_version=2")
    if requirements.get("workflow_identity") != workflow_identity:
        schema_blockers.append("material requirements workflow_identity does not match storyboard index")
    if local_registry.get("schema_version") != 2 or local_registry.get("profile") != HORIZONTAL_XIANXIA_PROFILE_ID:
        schema_blockers.append("local materials must use horizontal xianxia schema_version=2")
    for payload_name, payload in (("requirements", requirements), ("local materials", local_registry), ("bindings", bindings)):
        if payload.get("project") != index.get("project") or payload.get("episode_id") != index.get("episode_id"):
            schema_blockers.append(f"{payload_name} project/episode_id does not match storyboard index")

    valid_cut_ids: set[str] = set()
    for cut in index.get("cuts", []):
        if not isinstance(cut, dict):
            schema_blockers.append("storyboard index cuts must contain objects")
            continue
        cut_id = str(cut.get("cut_id") or "")
        valid_cut_ids.add(cut_id)
        duration = cut.get("duration_sec")
        if isinstance(duration, bool) or not isinstance(duration, int):
            schema_blockers.append(f"cut {cut_id} duration must be an integer from 4 through 30")
        elif not 4 <= duration <= 30:
            schema_blockers.append(f"cut {cut_id} duration must be from 4 through 30 seconds")
        else:
            try:
                _timeline_lines(group_blocks.get(int(cut.get("group_index") or 0), ""), duration, strict=True)
            except (TypeError, ValueError) as exc:
                schema_blockers.append(f"cut {cut_id} timeline is not a strict integer timeline: {exc}")

    requirement_items = [item for item in requirements.get("requirements", []) if isinstance(item, dict)]
    requirement_ids: set[str] = set()
    all_requirement_pairs: set[tuple[str, str]] = set()
    required_pairs: set[tuple[str, str]] = set()
    for item in requirement_items:
        requirement_id = str(item.get("requirement_id") or "")
        if not requirement_id or requirement_id in requirement_ids:
            schema_blockers.append(f"duplicate or missing requirement_id: {requirement_id or '<empty>'}")
        requirement_ids.add(requirement_id)
        if item.get("cut_id") not in valid_cut_ids:
            schema_blockers.append(f"requirement {requirement_id} references unknown cut_id")
        media_type = str(item.get("media_type") or "")
        if media_type not in MEDIA_LIMITS:
            schema_blockers.append(f"requirement {requirement_id} has unsupported media_type")
        pair = (str(item.get("material_key") or ""), media_type)
        all_requirement_pairs.add(pair)
        if item.get("required") is True:
            required_pairs.add(pair)

    local_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    verified_hashes: dict[tuple[str, str], str] = {}
    authorization_confirmed: dict[tuple[str, str], bool] = {}
    for item in local_registry.get("materials", []):
        if not isinstance(item, dict):
            schema_blockers.append("seedance_local_materials.json contains a non-object material")
            continue
        key = (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        if not all(key) or key in local_by_key:
            schema_blockers.append(f"duplicate or incomplete local material key: {key}")
            continue
        local_by_key[key] = item
        if key not in all_requirement_pairs:
            schema_blockers.append(f"local material {key[0]} has no logical requirement")
        forbidden_ark_fields = sorted(
            field for field in item if field.startswith("ark_") or field in {"arkAssetId", "assetId"}
        )
        if forbidden_ark_fields:
            schema_blockers.append(
                f"material {key[0]} contains ManJuWeb-owned fields: {', '.join(forbidden_ark_fields)}"
            )
        source = item.get("source") if isinstance(item.get("source"), dict) else {}
        optional_missing = key not in required_pairs and source.get("kind") == "missing"
        if not optional_missing:
            integrity_hash, integrity_error = _material_file_integrity(local_path, item)
            if integrity_error:
                generation_blockers.append(f"material {key[0]}: {integrity_error}")
            elif integrity_hash:
                verified_hashes[key] = integrity_hash
            mime_type = str(item.get("mime_type") or "").lower()
            if not mime_type.startswith(f"{key[1]}/"):
                generation_blockers.append(
                    f"material {key[0]} mime_type {mime_type or '<empty>'} does not match {key[1]}"
                )
        authorization = item.get("authorization") if isinstance(item.get("authorization"), dict) else {}
        authorization_confirmed[key] = authorization.get("status") == "confirmed"
        if not optional_missing and not authorization_confirmed[key]:
            submission_blockers.append(f"material {key[0]} authorization is not confirmed")
    for key in sorted(all_requirement_pairs):
        if key not in local_by_key:
            generation_blockers.append(f"material {key[0]} is missing from seedance_local_materials.json")

    sync_results: dict[str, Any] = {}
    if sync_path.is_file():
        try:
            sync_results = _read_json(sync_path)
        except Exception as exc:
            generation_blockers.append(f"invalid ark_sync_results.json: {exc}")
    else:
        generation_blockers.append("missing ark_sync_results.json")
    expected_sync_hashes = {
        "material_requirements_sha256": sha256_file(requirements_path),
        "local_materials_sha256": sha256_file(local_path),
    }
    if sync_results:
        if sync_results.get("schema_version") != 2:
            generation_blockers.append("Ark sync results schema_version must be 2")
        if sync_results.get("authority") != "manjuweb":
            generation_blockers.append("ark_sync_results.json authority must be manjuweb")
        if sync_results.get("profile") != HORIZONTAL_XIANXIA_PROFILE_ID:
            generation_blockers.append("Ark sync results profile mismatch")
        if sync_results.get("source_hashes") != expected_sync_hashes:
            generation_blockers.append("ark_sync_results.json is stale or belongs to another handoff")

    sync_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    ready_materials: dict[str, dict[str, Any]] = {}
    for item in sync_results.get("materials", []) if sync_results else []:
        if not isinstance(item, dict):
            generation_blockers.append("ark_sync_results.json contains a non-object material")
            continue
        key = (str(item.get("material_key") or ""), str(item.get("media_type") or ""))
        if not all(key) or key in sync_by_key:
            generation_blockers.append(f"duplicate or incomplete Ark sync material key: {key}")
            continue
        sync_by_key[key] = item
        local_hash = verified_hashes.get(key)
        declared_hash = str(item.get("sha256") or "").lower()
        ark_asset_id = str(item.get("ark_asset_id") or "")
        if local_hash and declared_hash != local_hash:
            generation_blockers.append(f"Ark sync hash mismatch for material {key[0]}")
        if (
            local_hash
            and declared_hash == local_hash
            and item.get("ark_status") == "active"
            and ARK_ASSET_ID_RE.fullmatch(ark_asset_id)
        ):
            ready_materials[f"{key[1]}:{key[0]}"] = item
        elif item.get("ark_status") == "active" and not ARK_ASSET_ID_RE.fullmatch(ark_asset_id):
            generation_blockers.append(f"material {key[0]} has invalid active Ark asset ID")
    for key in required_pairs:
        if f"{key[1]}:{key[0]}" not in ready_materials:
            generation_blockers.append(f"required material {key[0]} is not Active in ManJuWeb Ark results")

    for cut_id in sorted(valid_cut_ids):
        ready_keys = {
            f"{item.get('media_type')}:{item.get('material_key')}"
            for item in requirement_items
            if item.get("cut_id") == cut_id
            and f"{item.get('media_type')}:{item.get('material_key')}" in ready_materials
        }
        if not ready_keys:
            generation_blockers.append(f"cut {cut_id} has no Active multimodal material")
        counts = {media_type: 0 for media_type in MEDIA_LIMITS}
        for ready_key in ready_keys:
            counts[ready_key.split(":", 1)[0]] += 1
        for media_type, limit in MEDIA_LIMITS.items():
            if counts[media_type] > limit:
                generation_blockers.append(
                    f"cut {cut_id} has {counts[media_type]} {media_type} materials; limit is {limit}"
                )
        if sum(counts.values()) > TOTAL_MATERIAL_LIMIT:
            generation_blockers.append(
                f"cut {cut_id} has {sum(counts.values())} materials; total limit is {TOTAL_MATERIAL_LIMIT}"
            )

    submission_blockers.append(
        "missing authenticated ManJuWeb consumer contract/preflight evidence; Unit 6B is not complete"
    )
    current_integrity = {
        "final_txt_sha256": final_sha256,
        "storyboard_index_sha256": sha256_file(index_path),
        "asset_bindings_sha256": sha256_file(bindings_path),
        "material_requirements_sha256": sha256_file(requirements_path),
        "local_materials_sha256": sha256_file(local_path),
        "ark_sync_results_sha256": sha256_file(sync_path) if sync_path.is_file() else "",
    }
    if check_existing_package and package_path.is_file():
        try:
            package = _read_json(package_path)
            if package.get("source_integrity") != current_integrity:
                generation_blockers.append("seedance_generation_package.json is stale; re-export it")
        except Exception as exc:
            generation_blockers.append(f"invalid seedance_generation_package.json: {exc}")

    schema_blockers = list(dict.fromkeys(schema_blockers))
    generation_blockers = list(dict.fromkeys(generation_blockers))
    submission_blockers = list(dict.fromkeys(submission_blockers))
    handoff_schema_valid = not schema_blockers
    generation_ready = handoff_schema_valid and not generation_blockers
    submit_allowed = generation_ready and not submission_blockers
    issues = schema_blockers + generation_blockers + submission_blockers
    return {
        "handoff_schema_valid": handoff_schema_valid,
        "generation_ready": generation_ready,
        "submit_allowed": submit_allowed,
        "schema_blockers": schema_blockers,
        "generation_blockers": generation_blockers,
        "submission_blockers": submission_blockers,
        "issues": issues,
        "ready_materials": ready_materials,
        "source_integrity": current_integrity,
        "index": index,
        "requirements": requirements,
        "local_registry": local_registry,
        "sync_results": sync_results,
    }


def validate_material_handoff(
    episode_dir: Path,
    *,
    check_existing_package: bool = True,
) -> dict[str, Any]:
    if _profile_for_episode(episode_dir) == HORIZONTAL_XIANXIA_PROFILE_ID:
        return _validate_material_handoff_v2(
            episode_dir,
            check_existing_package=check_existing_package,
        )
    return _validate_material_handoff_v1(
        episode_dir,
        check_existing_package=check_existing_package,
    )


def _build_generation_package_v1(episode_dir: Path) -> dict[str, Any]:
    validation = _validate_material_handoff_v1(episode_dir, check_existing_package=False)
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


def _provider_reference_content(item: dict[str, Any]) -> dict[str, Any]:
    media_type = str(item["media_type"])
    field = f"{media_type}_url"
    return {
        "type": field,
        "role": f"reference_{media_type}",
        field: {"url": item["ark_asset_id"]},
    }


def _build_generation_package_v2(episode_dir: Path) -> dict[str, Any]:
    validation = _validate_material_handoff_v2(episode_dir, check_existing_package=False)
    final_path = episode_dir / "final.txt"
    content = final_path.read_text(encoding="utf-8", errors="replace") if final_path.is_file() else ""
    group_blocks = _extract_group_blocks(content)
    index = validation.get("index") if isinstance(validation.get("index"), dict) else {}
    requirements = validation.get("requirements") if isinstance(validation.get("requirements"), dict) else {}
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
        material_inputs: list[dict[str, Any]] = []
        seen_materials: set[str] = set()
        for requirement in cut_requirements:
            lookup_key = f"{requirement.get('media_type')}:{requirement.get('material_key')}"
            sync_item = ready_materials.get(lookup_key)
            if not isinstance(sync_item, dict) or lookup_key in seen_materials:
                continue
            seen_materials.add(lookup_key)
            material_inputs.append(
                {
                    "reference_token": "",
                    "material_key": requirement.get("material_key"),
                    "media_type": requirement.get("media_type"),
                    "asset_type": requirement.get("asset_type"),
                    "role": requirement.get("role"),
                    "source_binding_role": requirement.get("source_binding_role"),
                    "asset_id": requirement.get("asset_id"),
                    "state_id": requirement.get("state_id"),
                    "note": requirement.get("note"),
                    "ark_asset_id": sync_item.get("ark_asset_id"),
                    "sha256": sync_item.get("sha256"),
                    "provides": requirement.get("provides", []),
                    "excludes": requirement.get("excludes", []),
                }
            )

        counters = {media_type: 0 for media_type in MEDIA_LIMITS}
        for item in material_inputs:
            media_type = str(item.get("media_type") or "image")
            counters[media_type] += 1
            token = f"@{MEDIA_TOKEN_PREFIX[media_type]}{counters[media_type]}"
            item["reference_token"] = token
            # ``token`` remains as a compatibility alias for existing clients;
            # new consumers should use the explicit reference_token field.
            item["token"] = token

        cut_blockers = [
            issue
            for issue in validation.get("schema_blockers", []) + validation.get("generation_blockers", [])
            if cut_id in issue or issue.startswith("missing ") or "stale" in issue
        ]
        try:
            prompt = build_submission_prompt(
                group_blocks.get(group_index, ""),
                material_inputs,
                duration=cut.get("duration_sec") if isinstance(cut.get("duration_sec"), int) else None,
                strict_timeline=True,
            )
        except ValueError as exc:
            # Do not repair a malformed timeline at the last handoff step.  A
            # blocked cut remains inspectable, but its provider text must not
            # claim a timeline different from final.txt.
            prompt = ""
            cut_blockers.append(f"cut {cut_id} timeline compilation blocked: {exc}")
        provider_content = [{"type": "text", "text": prompt}]
        provider_content.extend(_provider_reference_content(item) for item in material_inputs)
        if not material_inputs:
            cut_blockers.append(f"cut {cut_id} has no serialized Active reference content")
        duration = cut.get("duration_sec")
        provider_request = {
            "model": MODEL_ID,
            "content": provider_content,
            "omni_reference_task_type": "reference",
            "ratio": "16:9",
            "resolution": "720p",
            "duration": duration,
            "generate_audio": True,
        }
        cuts.append(
            {
                "cut_id": cut_id,
                "group_index": group_index,
                "duration_sec": duration,
                "generation_ready": not cut_blockers and bool(material_inputs),
                "blocking_issues": list(dict.fromkeys(cut_blockers)),
                "material_inputs": material_inputs,
                "submission_prompt": prompt,
                "provider_request": provider_request,
            }
        )

    material_generation_ready = (
        bool(cuts)
        and validation.get("generation_ready") is True
        and all(cut["generation_ready"] for cut in cuts)
    )
    readiness = summarize_workflow_readiness(
        episode_dir,
        handoff_validation=validation,
        material_generation_ready=material_generation_ready,
    )
    submission_blockers = list(validation.get("submission_blockers", []))
    package_generation_ready = readiness["layers"]["generation_ready"]["valid"]
    package_submit_allowed = readiness["layers"]["submit_allowed"]["valid"]
    workflow_identity = index.get("workflow_identity", {}) if isinstance(index, dict) else {}
    return {
        "schema_version": 2,
        "submission_prompt_contract_version": SUBMISSION_PROMPT_CONTRACT_VERSION,
        "profile": HORIZONTAL_XIANXIA_PROFILE_ID,
        "provider_contract_version": 1,
        "model": MODEL_ID,
        "project": index.get("project", "") if isinstance(index, dict) else "",
        "episode_id": index.get("episode_id", "") if isinstance(index, dict) else "",
        "workflow_identity": workflow_identity,
        "readiness": readiness,
        "handoff_schema_valid": validation.get("handoff_schema_valid") is True,
        "generation_ready": package_generation_ready,
        "submit_allowed": package_submit_allowed,
        "schema_blockers": list(validation.get("schema_blockers", [])),
        "generation_blockers": list(validation.get("generation_blockers", [])),
        "submission_blockers": submission_blockers,
        "blocking_issues": list(dict.fromkeys(validation.get("issues", []))),
        "source_integrity": validation.get("source_integrity", {}),
        "stale_if_any_source_hash_changes": True,
        "cuts": cuts,
    }


def _layer(valid: bool, blockers: list[str], evidence: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "valid": bool(valid),
        "state": "passed" if valid else "blocked",
        "blockers": list(dict.fromkeys(blockers)),
        "evidence": evidence or {},
    }


def _storyboard_readiness(episode_dir: Path) -> dict[str, Any]:
    blockers: list[str] = []
    try:
        from storyboard_agent_workspace import validate_review_artifacts

        blockers.extend(
            f"storyboard reviewer evidence invalid: {issue}"
            for issue in validate_review_artifacts(episode_dir)
        )
    except Exception as exc:
        blockers.append(f"storyboard reviewer evidence validation failed: {exc}")
    final_path = episode_dir / "final.txt"
    index_path = episode_dir / "storyboard_index.json"
    status_path = episode_dir / "status.json"
    review_path = episode_dir / "review.txt"
    if not final_path.is_file():
        blockers.append("missing final.txt")
    if not index_path.is_file():
        blockers.append("missing storyboard_index.json")
    if not status_path.is_file():
        blockers.append("missing storyboard status.json")
    if not review_path.is_file():
        blockers.append("missing storyboard review.txt")
    status: dict[str, Any] = {}
    review: dict[str, Any] = {}
    index: dict[str, Any] = {}
    for path, label in ((status_path, "status.json"), (review_path, "review.txt"), (index_path, "storyboard_index.json")):
        if not path.is_file():
            continue
        try:
            payload = _read_json(path)
        except Exception as exc:
            blockers.append(f"invalid {label}: {exc}")
            continue
        if path == status_path:
            status = payload
        elif path == review_path:
            review = payload
        else:
            index = payload
    expected_reviewer = "seedance-2-5-horizontal-xianxia-3d-cg-reviewer"
    if status:
        if status.get("status") != "done":
            blockers.append("storyboard status is not done")
        if status.get("reviewer_source") != expected_reviewer:
            blockers.append("storyboard reviewer_source mismatch")
        if status.get("reviewer_pass") is not True or status.get("reviewer_issues_count") != 0:
            blockers.append("storyboard reviewer gate did not pass")
    if review:
        if review.get("pass") is not True or review.get("issues") != []:
            blockers.append("storyboard review.txt did not pass")
        if not review.get("summary") or not review.get("source_status"):
            blockers.append("storyboard review lacks source/summary evidence")
        checked_groups = review.get("checked_groups")
        if not isinstance(checked_groups, list) or not checked_groups:
            blockers.append("storyboard review lacks checked_groups evidence")
        audit_coverage = review.get("audit_coverage")
        if not isinstance(audit_coverage, dict) or any(
            audit_coverage.get(key) != "checked" for key in HORIZONTAL_REVIEW_COVERAGE_KEYS
        ):
            blockers.append("storyboard review audit_coverage is incomplete")
        if not isinstance(review.get("spot_checks"), list) or len(review["spot_checks"]) < 3:
            blockers.append("storyboard review requires at least three spot_checks")
        semantic_checks = review.get("semantic_checks")
        if not isinstance(semantic_checks, list) or not semantic_checks:
            blockers.append("storyboard review lacks semantic_checks evidence")
        elif any(item.get("result") == "issue" for item in semantic_checks if isinstance(item, dict)):
            blockers.append("storyboard semantic review contains hard issues")
        if not isinstance(review.get("warnings"), list):
            blockers.append("storyboard review warnings must be an array")
        if status:
            if status.get("reviewer_warnings_count") != len(review.get("warnings", [])):
                blockers.append("storyboard status warning count mismatches review.txt")
            if status.get("reviewer_issues_count") != len(review.get("issues", [])):
                blockers.append("storyboard status issue count mismatches review.txt")
    if final_path.is_file() and index:
        if index.get("source_hashes", {}).get("final_txt_sha256") != sha256_file(final_path):
            blockers.append("storyboard_index.json is stale for current final.txt")
    return _layer(
        not blockers,
        blockers,
        {
            "final_txt_sha256": sha256_file(final_path) if final_path.is_file() else "",
            "storyboard_index_sha256": sha256_file(index_path) if index_path.is_file() else "",
            "review_sha256": sha256_file(review_path) if review_path.is_file() else "",
            "status_sha256": sha256_file(status_path) if status_path.is_file() else "",
        },
    )


def _asset_readiness(episode_dir: Path) -> dict[str, Any]:
    blockers: list[str] = []
    status_path = episode_dir / "asset_status.json"
    validation_path = episode_dir / ASSET_VALIDATION_FILE
    if not status_path.is_file():
        blockers.append("missing asset_status.json")
    if not validation_path.is_file():
        blockers.append(f"missing {ASSET_VALIDATION_FILE}; run validate-assets.mjs")
    status: dict[str, Any] = {}
    validation: dict[str, Any] = {}
    if status_path.is_file():
        try:
            status = _read_json(status_path)
        except Exception as exc:
            blockers.append(f"invalid asset_status.json: {exc}")
    if validation_path.is_file():
        try:
            validation = _read_json(validation_path)
        except Exception as exc:
            blockers.append(f"invalid {ASSET_VALIDATION_FILE}: {exc}")
    if status:
        if not (
            status.get("status") == "done"
            and status.get("reviewer_source") == "asset-reviewer"
            and status.get("reviewer_pass") is True
            and status.get("reviewer_issues_count") == 0
        ):
            blockers.append("asset reviewer gate did not pass")
    if validation:
        if (
            validation.get("schema_version") != 1
            or validation.get("validator") != "validate-assets.mjs"
            or validation.get("valid") is not True
            or validation.get("issues") != []
        ):
            blockers.append("asset mechanical validation did not pass")
        validator_path = Path(__file__).resolve().parent / "agent_skills/asset-extractor/scripts/validate-assets.mjs"
        if not validator_path.is_file() or validation.get("validator_sha256") != sha256_file(validator_path):
            blockers.append("asset validator evidence is stale")
        source_map = {
            "final_sha256": episode_dir / "final.txt",
            "assets_sha256": episode_dir / "assets.md",
            "workbook_sha256": episode_dir / "assets.xlsx",
            "storyboardIndex_sha256": episode_dir / "storyboard_index.json",
            "review_sha256": episode_dir / "asset_review.json",
            "bindings_sha256": episode_dir / "asset_bindings.json",
            "status_sha256": status_path,
        }
        for field, path in source_map.items():
            if not path.is_file() or validation.get("source_hashes", {}).get(field) != sha256_file(path):
                blockers.append(f"asset validation is stale for {path.name}")
    return _layer(
        not blockers,
        blockers,
        {
            "asset_status_sha256": sha256_file(status_path) if status_path.is_file() else "",
            "asset_validation_sha256": sha256_file(validation_path) if validation_path.is_file() else "",
        },
    )


def summarize_workflow_readiness(
    episode_dir: Path,
    *,
    handoff_validation: dict[str, Any] | None = None,
    material_generation_ready: bool | None = None,
) -> dict[str, Any]:
    resolved_workflow_hash = ""
    index_path = episode_dir / "storyboard_index.json"
    if index_path.is_file():
        try:
            index = _read_json(index_path)
            workflow_identity = index.get("workflow_identity")
            if isinstance(workflow_identity, dict):
                resolved_workflow_hash = str(workflow_identity.get("resolved_workflow_hash") or "")
        except Exception:
            pass
    storyboard = _storyboard_readiness(episode_dir)
    assets = _asset_readiness(episode_dir)
    handoff = handoff_validation or validate_material_handoff(
        episode_dir,
        check_existing_package=False,
    )
    handoff_layer = _layer(
        handoff.get("handoff_schema_valid") is True,
        list(handoff.get("schema_blockers", [])),
        {"source_integrity": handoff.get("source_integrity", {})},
    )
    if material_generation_ready is None:
        material_generation_ready = handoff.get("generation_ready") is True
    generation_blockers = []
    if not storyboard["valid"]:
        generation_blockers.append("storyboard_valid is blocked")
    if not assets["valid"]:
        generation_blockers.append("asset_contract_valid is blocked")
    if not handoff_layer["valid"]:
        generation_blockers.append("handoff_schema_valid is blocked")
    generation_blockers.extend(handoff.get("generation_blockers", []))
    generation_valid = (
        storyboard["valid"]
        and assets["valid"]
        and handoff_layer["valid"]
        and bool(material_generation_ready)
        and not handoff.get("generation_blockers", [])
    )
    generation = _layer(generation_valid, generation_blockers)
    submission_blockers = []
    if not generation_valid:
        submission_blockers.append("generation_ready is blocked")
    submission_blockers.extend(handoff.get("submission_blockers", []))
    submission = _layer(generation_valid and not submission_blockers, submission_blockers)
    layers = {
        "storyboard_valid": storyboard,
        "asset_contract_valid": assets,
        "handoff_schema_valid": handoff_layer,
        "generation_ready": generation,
        "submit_allowed": submission,
    }
    first_blocker = None
    for name, layer in layers.items():
        if not layer["valid"]:
            first_blocker = {
                "layer": name,
                "reason": layer["blockers"][0] if layer["blockers"] else "unknown blocker",
            }
            break
    return {
        "schema_version": 1,
        "profile": _profile_for_episode(episode_dir),
        "resolved_workflow_hash": resolved_workflow_hash,
        "layers": layers,
        "first_blocker": first_blocker,
        "workflow_validated": False,
        "validation_scope": "contract-prototype-only",
    }


def write_workflow_readiness(episode_dir: Path) -> tuple[Path, Path]:
    payload = summarize_workflow_readiness(episode_dir)
    json_path = episode_dir / READINESS_FILE
    report_path = episode_dir / READINESS_REPORT_FILE
    _write_json(json_path, payload)
    lines = [
        "# Workflow Readiness",
        "",
        f"- profile: `{payload['profile']}`",
        f"- workflow_validated: `{str(payload['workflow_validated']).lower()}`",
        f"- validation_scope: `{payload['validation_scope']}`",
        "",
        "## Layers",
        "",
    ]
    for name, layer in payload["layers"].items():
        lines.append(f"- {name}: `{layer['state']}`")
        for blocker in layer["blockers"]:
            lines.append(f"  - blocker: {blocker}")
    if payload["first_blocker"]:
        lines.extend(
            [
                "",
                "## First blocker",
                "",
                f"- layer: `{payload['first_blocker']['layer']}`",
                f"- reason: {payload['first_blocker']['reason']}",
            ]
        )
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return json_path, report_path


def build_generation_package(episode_dir: Path) -> dict[str, Any]:
    if _profile_for_episode(episode_dir) == HORIZONTAL_XIANXIA_PROFILE_ID:
        return _build_generation_package_v2(episode_dir)
    return _build_generation_package_v1(episode_dir)


def write_generation_package(episode_dir: Path, output_path: Path | None = None) -> Path:
    path = output_path or (episode_dir / GENERATION_PACKAGE_FILE)
    package = build_generation_package(episode_dir)
    _write_json(path, package)
    if package.get("profile") == HORIZONTAL_XIANXIA_PROFILE_ID:
        lines = [
            "# Seedance 2.5 横屏仙侠提交提示词",
            "",
            "> 本文件由受哈希保护的 generation package 确定性编译。"
            "只有对应 cut 的真实素材已绑定并通过门禁后，提示词中的 @图片/@视频/@音频 token 才可提交。",
            "> 提示词合同：资产前置 + 整体画风 + 空间衔接 + 连续时间轴；特效、声音和执行约束只写在时间轴中，镜头运动由 Seedance 2.5 按实际动作与构图自主选择，除非剧情/连续性需要锁定。",
            "",
        ]
        for cut in package.get("cuts", []):
            if not isinstance(cut, dict):
                continue
            lines.extend(
                [
                    f"## {cut.get('cut_id') or 'unknown-cut'}",
                    "",
                    str(cut.get("submission_prompt") or "").strip(),
                    "",
                ]
            )
        (episode_dir / SUBMISSION_PROMPTS_FILE).write_text(
            "\n".join(lines).rstrip() + "\n",
            encoding="utf-8",
        )
    return path
