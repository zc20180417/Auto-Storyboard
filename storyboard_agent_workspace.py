#!/usr/bin/env python3
"""Prepare and collect file-native storyboard agent workspaces.

This script does not call a model API or launch an agent CLI. It creates a
transparent file workspace that Codex, Qwen Code, or another agent can operate
on directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import textwrap
import zipfile
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

from batch_generate_storyboards import (
    EpisodeInput,
    build_episode_inputs,
    build_episode_inputs_from_paths,
    extract_episode_number,
    extract_series_title,
    find_prompt_file,
    load_review_skill_text,
    make_output_path,
    read_script_text,
    read_utf8_text,
    sanitize_filename_part,
    split_episode_collection_text,
    split_episode_into_segments,
    chinese_numeral_to_int,
)
from seedance_material_handoff import (
    GENERATION_PACKAGE_FILE,
    HORIZONTAL_REVIEW_COVERAGE_KEYS,
    export_material_handoff,
    validate_material_handoff,
    write_generation_package,
    write_workflow_readiness,
)
from seedance_probe_evidence import write_probe_run_status


DEFAULT_AGENT_RUNS_DIR = "agent_runs"
DEFAULT_AGENT_OUTPUT_DIR = "outputs_agent"
PROJECT_AGENT_SKILLS_DIR = "agent_skills"
SEEDANCE_PROMPT_PROFILE_PATH = "agent_skills/seedance-prompt-profile/SKILL.md"
SEEDANCE25_LIVE_VERTICAL_PROFILE_PATH = "agent_skills/seedance-2-5-live-vertical/SKILL.md"
SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE_PATH = "agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/SKILL.md"
CG_VISUAL_STYLE_SKILL_PATH = "agent_skills/3d-cg-visual-style/SKILL.md"
STORYBOARD_QUALITY_POLICY_PATH = "agent_skills/storyboard-quality-policy.json"
PROJECT_PACK_REGISTRY_PATH = "agent_skills/project-packs/registry.json"
AGENT_WORKSPACE_VERSION = 2
VERTICAL_REVIEW_CONTRACT_VERSION = 4
VERTICAL_REVIEW_FACTS_SCHEMA_VERSION = 1
SIMPLE_BATCH_MAX_SCRIPT_CHARS = 2500
SIMPLE_BATCH_MAX_SEGMENTS = 1
MAX_EPISODES_PER_WORKER_BATCH = 2

DEFAULT_VIDEO_PROFILE = "seedance-2.0"
SEEDANCE25_LIVE_VERTICAL_PROFILE = "seedance-2.5-live-vertical"
SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE = "seedance-2.5-horizontal-xianxia-3d-cg"
REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET = "realistic-material-restrained-anime-outline"

VIDEO_PROFILE_CONFIG = {
    DEFAULT_VIDEO_PROFILE: {
        "label": "Seedance 2.0 兼容流程",
        "target_video_model": "seedance",
        "profile_skill_path": SEEDANCE_PROMPT_PROFILE_PATH,
        "supported_aspects": ("vertical", "horizontal"),
        "supported_visual_styles": tuple(),
        "supported_modes": ("single", "scene"),
        "generator_dir": None,
        "reviewer_dir": None,
        "generator_name": None,
        "reviewer_name": None,
        "duration_min_seconds": 6,
        "duration_max_seconds": 15,
        "timeline_granularity_seconds": 0.5,
        "aspect_ratio": None,
        "supported_resolutions": tuple(),
        "default_resolution": None,
        "fps": None,
        "generate_audio": None,
        "video_task_type": None,
        "requires_multimodal_materials": False,
        "minimum_material_inputs": 0,
        "allowed_multimodal_material_types": tuple(),
        "forbidden_video_task_modes": tuple(),
        "collection_tail_mode": "legacy",
        "collection_tail_lines": tuple(),
        "base_negative_line": None,
        "profile_role": "reference",
        "contract_version": 1,
        "provider_contract_version": None,
        "provider_task_mapping": None,
        "capabilities": {
            "auto_export_index": False,
            "vertical_review_facts": False,
            "material_handoff_schema": None,
            "visual_style_presets": False,
            "project_packs": False,
        },
    },
    SEEDANCE25_LIVE_VERTICAL_PROFILE: {
        "label": "Seedance 2.5 真人竖屏短剧",
        "target_video_model": "doubao-seedance-2-5-260628",
        "profile_skill_path": SEEDANCE25_LIVE_VERTICAL_PROFILE_PATH,
        "supported_aspects": ("vertical",),
        "supported_visual_styles": ("live-action",),
        "supported_modes": ("single", "scene"),
        "generator_dir": "seedance-2-5-live-vertical-generator",
        "reviewer_dir": "seedance-2-5-live-vertical-reviewer",
        "generator_name": "seedance-2-5-live-vertical-generator",
        "reviewer_name": "seedance-2-5-live-vertical-reviewer",
        "duration_min_seconds": 4,
        "duration_max_seconds": 30,
        "timeline_granularity_seconds": 1,
        "aspect_ratio": "9:16",
        "supported_resolutions": ("480p", "720p"),
        "default_resolution": "720p",
        "fps": 24,
        "generate_audio": True,
        "video_task_type": "multimodal_generation",
        "requires_multimodal_materials": True,
        "minimum_material_inputs": 1,
        "allowed_multimodal_material_types": ("image", "video", "audio"),
        "forbidden_video_task_modes": (
            "text_only_generation",
            "reference_generation",
            "first_last_frame_generation",
            "keyframe_generation",
            "video_edit",
            "video_extend",
            "track_completion",
        ),
        "collection_tail_mode": "seedance-2.5-live-vertical",
        "collection_tail_lines": (
            "画面风格：真人实拍竖屏短剧，真实摄影，自然光影，电影感浅景深，真实材质，表演自然，人物口型清楚",
            "声音设计：生成与画面同步的现场对白、环境音和必要音效，无字幕，无配乐",
        ),
        "base_negative_line": "",
        "profile_role": "hard-contract",
        "contract_version": 2,
        "provider_contract_version": 1,
        "provider_task_mapping": None,
        "capabilities": {
            "auto_export_index": True,
            "vertical_review_facts": True,
            "material_handoff_schema": "v1-live-vertical",
            "visual_style_presets": False,
            "project_packs": False,
        },
    },
    SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE: {
        "label": "Seedance 2.5 横屏仙侠 3D CG 动漫",
        "target_video_model": "doubao-seedance-2-5-260628",
        "profile_skill_path": SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE_PATH,
        "supported_aspects": ("horizontal",),
        "supported_visual_styles": ("3d-cg",),
        "supported_modes": ("single",),
        "generator_dir": "seedance-2-5-horizontal-xianxia-3d-cg-generator",
        "reviewer_dir": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
        "generator_name": "seedance-2-5-horizontal-xianxia-3d-cg-generator",
        "reviewer_name": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
        "duration_min_seconds": 4,
        "duration_max_seconds": 30,
        "timeline_granularity_seconds": 1,
        "aspect_ratio": "16:9",
        "supported_resolutions": ("720p",),
        "default_resolution": "720p",
        "fps": 24,
        "generate_audio": True,
        "video_task_type": "multimodal_generation",
        "requires_multimodal_materials": True,
        "minimum_material_inputs": 1,
        "allowed_multimodal_material_types": ("image", "video", "audio"),
        "forbidden_video_task_modes": (
            "text_only_generation",
            "first_last_frame_generation",
            "keyframe_generation",
            "video_edit",
            "video_extend",
            "track_completion",
        ),
        "collection_tail_mode": "seedance-2.5-horizontal-xianxia-3d-cg",
        "collection_tail_lines": tuple(),
        "base_negative_line": "",
        "profile_role": "hard-contract",
        "contract_version": 1,
        "provider_contract_version": 1,
        "provider_task_mapping": {
            "field": "omni_reference_task_type",
            "value": "reference",
        },
        "capabilities": {
            "auto_export_index": True,
            "vertical_review_facts": False,
            "material_handoff_schema": "v2-provider-reference",
            "visual_style_presets": True,
            "project_packs": True,
        },
    },
}

VISUAL_STYLE_PRESET_CONFIG = {
    REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET: {
        "id": REALISTIC_MATERIAL_RESTRAINED_ANIME_OUTLINE_PRESET,
        "version": 1,
        "name": "写实材质＋克制卡通轮廓",
        "description": "亚洲骨相与适度动漫五官，可信 PBR 材质融合少量手绘纹理，轮廓稳定克制，东方低饱和色盘。",
        "compatible_video_profiles": (SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,),
        "compatible_visual_styles": ("3d-cg",),
    },
}

SEEDANCE25_FORBIDDEN_TASK_MODE_TERMS = {
    "text_only_generation": ("纯文本生成", "文生视频", "text_only_generation", "text_to_video"),
    "reference_generation": (
        "多模态参考生成",
        "普通参考生成",
        "素材参考生成",
        "参考图生成",
        "参考视频生成",
        "参考生成",
        "reference_generation",
    ),
    "first_last_frame_generation": (
        "首尾帧生成",
        "首帧参考",
        "尾帧参考",
        "首尾帧",
        "first_last_frame_generation",
    ),
    "keyframe_generation": ("关键帧生成", "关键帧模式", "keyframe_generation"),
    "video_edit": ("视频编辑", "编辑视频", "video_edit"),
    "video_extend": ("视频延长", "延长视频", "视频续写", "video_extend"),
    "track_completion": ("轨道补全", "track_completion"),
}


def video_profile_config(video_profile: str) -> dict:
    try:
        return VIDEO_PROFILE_CONFIG[video_profile]
    except KeyError as exc:
        raise ValueError(f"unsupported video profile: {video_profile}") from exc


def compatible_visual_style_presets(video_profile: str) -> list[dict]:
    video_profile_config(video_profile)
    return [
        dict(preset)
        for preset in VISUAL_STYLE_PRESET_CONFIG.values()
        if video_profile in preset["compatible_video_profiles"]
    ]


def resolved_visual_style_preset(video_profile: str, preset_id: str | None) -> dict | None:
    if not preset_id:
        return None
    try:
        preset = VISUAL_STYLE_PRESET_CONFIG[preset_id]
    except KeyError as exc:
        choices = ", ".join(item["id"] for item in compatible_visual_style_presets(video_profile)) or "none"
        raise ValueError(
            f"visual style preset {preset_id} is unknown; compatible presets for {video_profile}: {choices}"
        ) from exc
    if video_profile not in preset["compatible_video_profiles"]:
        raise ValueError(f"visual style preset {preset_id} is not compatible with video profile {video_profile}")
    return dict(preset)


def visual_style_preset_snapshot(video_profile: str, preset_id: str | None) -> dict | None:
    preset = resolved_visual_style_preset(video_profile, preset_id)
    if preset is None:
        return None
    canonical = json.dumps(preset, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        **preset,
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }


def project_pack_snapshot(
    *,
    project_root: Path,
    video_profile: str,
    aspect: str,
    visual_style: str,
    mode: str,
    visual_style_preset: str | None,
    project_pack_id: str | None,
) -> dict | None:
    if not project_pack_id:
        return None
    profile = video_profile_config(video_profile)
    if not profile["capabilities"]["project_packs"]:
        raise ValueError(
            f"project pack incompatible video profile: actual={video_profile}; allowed=profiles with project_packs capability"
        )
    registry_path = (project_root / PROJECT_PACK_REGISTRY_PATH).resolve()
    if not registry_path.is_file():
        raise ValueError(f"project pack registry missing: {registry_path}")
    registry = read_json(registry_path)
    entry = registry.get("packs", {}).get(project_pack_id)
    if not isinstance(entry, dict):
        allowed = ",".join(sorted(registry.get("packs", {}).keys())) or "none"
        raise ValueError(f"unknown project pack: actual={project_pack_id}; allowed={allowed}")
    pack_path = (project_root / entry["path"]).resolve()
    if not pack_path.is_file():
        raise ValueError(f"project pack file missing: {pack_path}")
    pack = read_json(pack_path)
    if pack.get("id") != project_pack_id or pack.get("version") != entry.get("version"):
        raise ValueError(
            "project pack registry mismatch: "
            f"actual={pack.get('id')}@{pack.get('version')}; "
            f"required={project_pack_id}@{entry.get('version')}"
        )
    checks = (
        ("video profile", video_profile, pack.get("compatible_video_profiles", [])),
        ("aspect", aspect, pack.get("supported_aspects", [])),
        ("visual style", visual_style, pack.get("supported_visual_styles", [])),
        ("mode", mode, pack.get("supported_modes", [])),
    )
    for label, actual, allowed_values in checks:
        if actual not in allowed_values:
            allowed = ",".join(allowed_values) or "none"
            raise ValueError(
                f"project pack {project_pack_id} incompatible {label}: actual={actual}; allowed={allowed}"
            )
    required_preset = pack.get("required_visual_style_preset")
    if visual_style_preset and visual_style_preset != required_preset:
        raise ValueError(
            "project pack preset conflict: "
            f"actual={visual_style_preset}; required={required_preset}; project_pack={project_pack_id}; "
            f"use --visual-style-preset {required_preset} or omit it"
        )
    file_paths = [pack_path, (project_root / pack["entry_skill"]).resolve()]
    file_paths.extend((project_root / path).resolve() for path in pack.get("references", []))
    loaded_files = []
    for path in file_paths:
        if not path.is_file():
            raise ValueError(f"project pack resource missing: {path}")
        loaded_files.append(
            {
                "path": str(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    stable_loaded_files = [
        {
            "path": path.relative_to(project_root.resolve()).as_posix(),
            "sha256": item["sha256"],
        }
        for path, item in zip(file_paths, loaded_files)
    ]
    canonical = json.dumps(stable_loaded_files, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "id": project_pack_id,
        "version": pack["version"],
        "name": pack["name"],
        "path": str(pack_path),
        "entry_skill_path": str((project_root / pack["entry_skill"]).resolve()),
        "required_visual_style_preset": required_preset,
        "loaded_files": loaded_files,
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }


def resolved_workspace_config(
    *,
    video_profile: str,
    aspect: str,
    visual_style: str,
    resolution: str | None,
    mode: str,
    visual_style_preset: str | None,
    project_pack_id: str | None = None,
    project_root: Path | None = None,
) -> dict:
    resolved_project_root = (project_root or Path(__file__).resolve().parent).resolve()
    pack = project_pack_snapshot(
        project_root=resolved_project_root,
        video_profile=video_profile,
        aspect=aspect,
        visual_style=visual_style,
        mode=mode,
        visual_style_preset=visual_style_preset,
        project_pack_id=project_pack_id,
    )
    effective_preset = (
        pack["required_visual_style_preset"]
        if pack and not visual_style_preset
        else visual_style_preset
    )
    selection_error = validate_video_profile_selection(
        video_profile=video_profile,
        aspect=aspect,
        visual_style=visual_style,
        resolution=resolution,
        mode=mode,
        visual_style_preset=effective_preset,
    )
    if selection_error:
        raise ValueError(selection_error)
    profile = video_profile_config(video_profile)
    preset = visual_style_preset_snapshot(video_profile, effective_preset)
    return {
        "video_profile": video_profile,
        "video_profile_contract_version": profile["contract_version"],
        "provider_contract_version": profile["provider_contract_version"],
        "storyboard_aspect": aspect,
        "visual_style": visual_style,
        "visual_style_preset": preset["id"] if preset else None,
        "visual_style_preset_version": preset["version"] if preset else None,
        "visual_style_preset_sha256": preset["sha256"] if preset else None,
        "visual_style_preset_source": (
            "explicit" if visual_style_preset else "project_pack" if pack else "none"
        ),
        "project_pack_id": pack["id"] if pack else None,
        "project_pack_version": pack["version"] if pack else None,
        "project_pack_path": pack["path"] if pack else None,
        "project_pack_sha256": pack["sha256"] if pack else None,
        "project_pack_source": "explicit" if pack else "none",
        "video_resolution": resolved_video_resolution(video_profile, resolution),
        "video_aspect_ratio": profile["aspect_ratio"],
        "expected_output_fps": profile["fps"],
        "generate_audio": profile["generate_audio"],
        "video_task_type": profile["video_task_type"],
        "provider_task_mapping": profile["provider_task_mapping"],
        "mode": mode,
        "capabilities": dict(profile["capabilities"]),
    }


def resolved_video_resolution(video_profile: str, requested_resolution: str | None = None) -> str | None:
    cfg = video_profile_config(video_profile)
    resolution = requested_resolution or cfg["default_resolution"]
    supported = cfg["supported_resolutions"]
    if resolution and resolution not in supported:
        choices = ", ".join(supported) if supported else "none"
        raise ValueError(
            f"video profile {video_profile} does not support resolution {resolution}; "
            f"supported: {choices}"
        )
    return resolution


def validate_video_profile_selection(
    *,
    video_profile: str,
    aspect: str,
    visual_style: str,
    resolution: str | None = None,
    mode: str | None = None,
    visual_style_preset: str | None = None,
) -> str | None:
    cfg = video_profile_config(video_profile)
    if aspect not in cfg["supported_aspects"]:
        return (
            f"video profile {video_profile} only supports aspect(s) {','.join(cfg['supported_aspects'])}; "
            f"incompatible aspect: actual={aspect}; allowed={','.join(cfg['supported_aspects'])}"
        )
    styles = cfg["supported_visual_styles"]
    if styles and visual_style not in styles:
        return (
            f"video profile {video_profile} only supports visual style(s) {','.join(styles)}; "
            f"incompatible visual style: actual={visual_style}; allowed={','.join(styles)}"
        )
    modes = cfg["supported_modes"]
    if mode is not None and mode not in modes:
        return f"video profile {video_profile} incompatible mode: actual={mode}; allowed={','.join(modes)}"
    try:
        resolved_video_resolution(video_profile, resolution)
        preset = resolved_visual_style_preset(video_profile, visual_style_preset)
    except ValueError as exc:
        message = str(exc)
        if "resolution" in message:
            actual = resolution or cfg["default_resolution"] or "none"
            allowed = ",".join(cfg["supported_resolutions"]) or "none"
            return f"video profile {video_profile} incompatible resolution: actual={actual}; allowed={allowed}"
        return message
    if preset and visual_style not in preset["compatible_visual_styles"]:
        return (
            f"visual style preset {preset['id']} incompatible visual style: "
            f"actual={visual_style}; allowed={','.join(preset['compatible_visual_styles'])}"
        )
    return None


VISUAL_STYLE_CONFIG = {
    "live-action": {
        "label": "真人实拍",
        "style_line": "画面风格：浅景深，电影质感，4K画质，真人实拍风格，细节丰富，无字幕，无配乐",
        "negative_line": "--neg 模糊，低分辨率，扭曲，变形，卡通，油画，3D渲染，塑料感，西方人面孔，面部融合，过曝，色彩失真，伪影，叠加字幕，硬字幕，烧录字幕，后期添加的文字，水印，logo，标题文字，片名，演职员表，背景音乐，配乐，BGM，叠加文字，画面外文字",
        "task_guidance": (
            "默认真人实拍短剧风格：写真实摄影可执行画面、自然光影、真实材质、真实人物口型；"
            "不要写成卡通、动画、3D渲染或塑料玩具质感。"
        ),
        "asset_guidance": (
            "资产提示词使用真人短剧定妆照、真实空镜、真实道具材质口径；"
            "避免卡通、3D渲染、塑料感。"
        ),
    },
    "3d-cg": {
        "label": "动漫3D CG",
        "style_line": "画面风格：横屏16:9，高质量国漫3D CG，写实材质＋克制卡通轮廓；亚洲骨相与适度动漫五官，可信PBR材质叠加少量手绘纹理，稳定克制轮廓线，东方低饱和色盘，电影级布光，自然景深，表情绑定细腻，口型同步清楚，动作流畅；仙侠特效在实际时间轴中写清来源、形态、路径、作用对象、反馈、收束和声音，主体始终清楚，无字幕，无配乐",
        "negative_line": "--neg 模糊，低分辨率，扭曲，变形，低多边形，廉价游戏建模，塑料玩具感，面部僵硬，表情死板，眼神空洞，口型错位，穿模，骨骼错位，手指畸形，材质粗糙，贴图拉伸，轮廓线抖动，过曝，色彩失真，伪影，叠加字幕，硬字幕，烧录字幕，后期添加的文字，水印，logo，标题文字，片名，演职员表，背景音乐，配乐，BGM，叠加文字，画面外文字",
        "task_guidance": (
            "动漫3D CG短剧风格：保留短剧分镜、对白、站位、道具连续和时间规则，但画面描述应服务于"
            "二次元角色设计、风格化面部与眼睛、清晰轮廓线、高质量卡通渲染、PBR材质与手绘质感融合、"
            "稳定表情绑定、清楚口型同步和流畅动作；关键视觉事件直接写入实际时间轴，"
            "不能只靠固定画面风格尾部；特效必须跟随具体人物、动作、道具、空间、环境、心理、权力或信息落点，"
            "并在时间轴中写清来源、形态、路径、作用对象、反馈、收束和声音；"
            "不得写成法阵、满屏粒子、游戏技能 UI 或盖住人物主体；"
            "不要写真人实拍、真实摄影、真实演员、纪录片摄影等真人媒介词。"
        ),
        "asset_guidance": (
            "资产提示词使用动漫3D角色模型设定、二次元脸型和眼睛、发型体块、清晰轮廓线、"
            "PBR材质与手绘质感融合的场景/道具口径；人物资产强调角色比例、表情绑定友好特征、"
            "发型体块、服装材质和可复用模型状态；场景资产仍为空镜。"
        ),
    },
}


def visual_style_config(visual_style: str) -> dict[str, str]:
    try:
        return VISUAL_STYLE_CONFIG[visual_style]
    except KeyError as exc:
        raise ValueError(f"unsupported visual style: {visual_style}") from exc

STORYBOARD_ASPECT_CONFIG = {
    "vertical": {
        "label": "竖屏",
        "generator_dir": "storyboard-generator",
        "reviewer_dir": "storyboard-reviewer",
        "generator_name": "storyboard-generator",
        "reviewer_name": "storyboard-reviewer",
        "generator_description": (
            "Generate vertical Chinese costume-drama storyboard prompts from episode scripts. "
            "Use when converting short-drama scripts into natural grouped storyboard output."
        ),
        "reviewer_description": (
            "Review vertical storyboard drafts against the source script, natural format, timing, "
            "space locking, and dialogue-direction rules. Use after storyboard generation."
        ),
    },
    "horizontal": {
        "label": "横屏",
        "generator_dir": "storyboard-horizontal-generator",
        "reviewer_dir": "storyboard-horizontal-reviewer",
        "generator_name": "storyboard-horizontal-generator",
        "reviewer_name": "storyboard-horizontal-reviewer",
        "generator_description": (
            "Generate 16:9 horizontal Chinese short-drama storyboard prompts from episode scripts. "
            "Use when converting short-drama scripts into spatially blocked horizontal storyboard output."
        ),
        "reviewer_description": (
            "Review 16:9 horizontal storyboard drafts against the source script, natural format, timing, "
            "screen direction, spatial blocking, and dialogue-direction rules. Use after horizontal storyboard generation."
        ),
    },
}


def storyboard_aspect_config(aspect: str) -> dict[str, str]:
    try:
        return STORYBOARD_ASPECT_CONFIG[aspect]
    except KeyError as exc:
        raise ValueError(f"unsupported storyboard aspect: {aspect}") from exc


def storyboard_workflow_config(aspect: str, video_profile: str = DEFAULT_VIDEO_PROFILE) -> dict[str, str]:
    aspect_cfg = dict(storyboard_aspect_config(aspect))
    profile_cfg = video_profile_config(video_profile)
    for key in ("generator_dir", "reviewer_dir", "generator_name", "reviewer_name"):
        override = profile_cfg.get(key)
        if override:
            aspect_cfg[key] = override
    if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
        aspect_cfg["generator_description"] = (
            "Generate live-action 9:16 Chinese vertical short-drama storyboards for Seedance 2.5, "
            "with integer-second staging, native audio, and script-faithful continuity."
        )
        aspect_cfg["reviewer_description"] = (
            "Review Seedance 2.5 live-action vertical short-drama storyboards against the script, "
            "profile timing, audio, space, continuity, and generation-density contracts."
        )
    elif video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
        aspect_cfg["generator_description"] = (
            "Generate 16:9 xianxia anime 3D CG storyboards for Seedance 2.5, "
            "with integer-second staging, native audio, horizontal blocking, and reference-ready continuity."
        )
        aspect_cfg["reviewer_description"] = (
            "Review Seedance 2.5 horizontal xianxia anime 3D CG storyboards against the script, "
            "profile timing, horizontal composition, VFX provenance, native audio, and continuity contracts."
        )
    return aspect_cfg


VERTICAL_REVIEWER_SOURCES = frozenset(
    {
        STORYBOARD_ASPECT_CONFIG["vertical"]["reviewer_name"],
        VIDEO_PROFILE_CONFIG[SEEDANCE25_LIVE_VERTICAL_PROFILE]["reviewer_name"],
    }
)


def is_vertical_v2_reviewer(reviewer_source: str | None, review_contract_version: int) -> bool:
    return reviewer_source in VERTICAL_REVIEWER_SOURCES and review_contract_version >= 2


def is_vertical_v3_reviewer(reviewer_source: str | None, review_contract_version: int) -> bool:
    return reviewer_source in VERTICAL_REVIEWER_SOURCES and review_contract_version >= 3


def is_vertical_v4_reviewer(reviewer_source: str | None, review_contract_version: int) -> bool:
    return reviewer_source in VERTICAL_REVIEWER_SOURCES and review_contract_version >= 4


def resolved_vertical_review_contract_version(video_profile: str) -> int:
    if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
        return VERTICAL_REVIEW_CONTRACT_VERSION
    return 2


def write_utf8(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: dict) -> None:
    write_utf8(path, json.dumps(payload, ensure_ascii=False, indent=2))


def episode_id_for_cut_contract(episode_dir: Path) -> str:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
            raw = str(meta.get("episode_id") or episode_dir.name)
        except Exception:
            raw = episode_dir.name
    else:
        raw = episode_dir.name

    match = re.search(r"(\d+)", raw)
    if match:
        return f"EP{int(match.group(1)):02d}"
    return re.sub(r"[^A-Za-z0-9_-]+", "_", raw).strip("_").upper()


def _desired_cut_id(episode_id: str, group_index: int) -> str:
    return f"{episode_id}-G{group_index:02d}"


def _strip_heading_cut_id(heading: str) -> str:
    heading = re.sub(r"\s*\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*", " ", heading, count=1)
    heading = re.sub(r"\s*[（(]\s*cut_id\s*[:：]\s*[A-Z0-9_-]+\s*[）)]", "", heading)
    heading = re.sub(r"([（(])\s*cut_id\s*[:：]\s*[A-Z0-9_-]+\s*[，,]\s*", r"\1", heading)
    heading = re.sub(r"\s*[，,]\s*cut_id\s*[:：]\s*[A-Z0-9_-]+", "", heading)
    heading = re.sub(r"\s{2,}", " ", heading)
    return heading


def _ensure_heading_cut_id(heading: str, desired_cut_id: str) -> str:
    clean_heading = _strip_heading_cut_id(heading)
    return re.sub(
        r"^(\ufeff?\s*===\s*)",
        rf"\1[cut_id: {desired_cut_id}] ",
        clean_heading,
        count=1,
    )


def ensure_storyboard_cut_ids(content: str, episode_id: str) -> tuple[str, list[str]]:
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content, []

    parts: list[str] = []
    changes: list[str] = []
    cursor = 0
    for index, group_match in enumerate(group_matches, start=1):
        heading = group_match.group(0)
        desired_cut_id = _desired_cut_id(episode_id, index)
        updated_heading = _ensure_heading_cut_id(heading, desired_cut_id)
        parts.append(content[cursor:group_match.start()])
        parts.append(updated_heading)
        cursor = group_match.end()
        if updated_heading != heading:
            changes.append(f"第{index}组->{desired_cut_id}")

    parts.append(content[cursor:])
    return "".join(parts), changes


def validate_storyboard_cut_ids(content: str, episode_id: str) -> list[str]:
    issues: list[str] = []
    seen: set[str] = set()
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches, start=1):
        heading = group_match.group(0)
        cut_matches = list(CUT_ID_RE.finditer(heading))
        desired = _desired_cut_id(episode_id, index)
        if not cut_matches:
            issues.append(f"第{index}组缺少 cut_id；应为 {desired}。")
            continue
        if len(cut_matches) > 1:
            issues.append(f"第{index}组包含多个 cut_id；只允许一个，应为 {desired}。")
        cut_id = cut_matches[0].group("cut_id")
        if cut_id != desired:
            issues.append(f"第{index}组 cut_id={cut_id}，应为 {desired}。")
        if cut_id in seen:
            issues.append(f"cut_id 重复：{cut_id}。")
        seen.add(cut_id)
    return issues


def resolve_source_episodes(source: Path) -> list[EpisodeInput]:
    source = source.resolve()
    if source.is_dir():
        paths = sorted(
            path
            for pattern in ("*.docx", "*.txt")
            for path in source.glob(pattern)
            if path.is_file()
        )
        return build_episode_inputs_from_paths(paths)

    if not source.is_file():
        raise FileNotFoundError(f"source not found: {source}")

    text = read_script_text(source)
    try:
        split_episodes = split_episode_collection_text(text, source.stem)
    except ValueError:
        split_episodes = []

    if split_episodes:
        return [
            EpisodeInput(
                source_path=source,
                episode_number=item.episode_number,
                display_name=item.display_name,
                series_title=item.series_title,
                script_text=item.script_text,
            )
            for item in split_episodes
        ]

    episode_number = extract_episode_number(text, source.stem)
    return [
        EpisodeInput(
            source_path=source,
            episode_number=episode_number,
            display_name=source.stem,
            series_title=extract_series_title(source.stem),
            script_text=text,
        )
    ]


def make_episode_id(episode: EpisodeInput, sequence_index: int) -> str:
    episode_number = episode.episode_number or sequence_index
    return f"ep{episode_number:02d}"


def make_agent_context(
    *,
    project_root: Path,
    generation_rules_source: Path,
    reviewer_rules_source: Path,
    out_dir: Path,
    episodes_count: int,
    generator_skill_path: Path,
    reviewer_skill_path: Path,
    seedance_profile_path: Path,
    aspect: str,
    mode: str,
    cg_visual_style_skill_path: Path | None = None,
    visual_style: str = "live-action",
    video_profile: str = DEFAULT_VIDEO_PROFILE,
    video_resolution: str | None = None,
    visual_style_preset: str | None = None,
    project_pack: dict | None = None,
) -> str:
    aspect_cfg = storyboard_workflow_config(aspect, video_profile)
    aspect_label = aspect_cfg["label"]
    reviewer_skill_name = aspect_cfg["reviewer_name"]
    style_cfg = visual_style_config(visual_style)
    visual_style_label = style_cfg["label"]
    profile_cfg = video_profile_config(video_profile)
    preset = visual_style_preset_snapshot(video_profile, visual_style_preset)
    resolution = resolved_video_resolution(video_profile, video_resolution)
    model_profile_items = [
        f"- Video profile: `{video_profile}` ({profile_cfg['label']})",
        f"- Target video model: `{profile_cfg['target_video_model']}`",
        f"- Seedance Prompt Profile: `{seedance_profile_path}`",
    ]
    if resolution:
        model_profile_items.append(f"- Video resolution: `{resolution}`")
    if preset:
        model_profile_items.extend(
            [
                f"- Visual style preset: `{preset['id']}` ({preset['name']})",
                f"- Visual style preset version: `{preset['version']}`",
                f"- Visual style preset SHA-256: `{preset['sha256']}`",
            ]
        )
    if project_pack:
        model_profile_items.extend(
            [
                f"- Project pack: `{project_pack['id']}` ({project_pack['name']})",
                f"- Project pack version: `{project_pack['version']}`",
                f"- Project pack SHA-256: `{project_pack['sha256']}`",
                f"- Project pack entry skill: `{project_pack['entry_skill_path']}`",
            ]
        )
    if profile_cfg["aspect_ratio"]:
        model_profile_items.append(f"- Aspect ratio parameter: `{profile_cfg['aspect_ratio']}`")
    if profile_cfg["fps"]:
        model_profile_items.append(f"- Output FPS: `{profile_cfg['fps']}`")
    if profile_cfg["generate_audio"] is not None:
        model_profile_items.append(
            f"- Native audio generation: `{str(profile_cfg['generate_audio']).lower()}`"
        )
    if profile_cfg["video_task_type"]:
        model_profile_items.extend(
            [
                f"- Video task type: `{profile_cfg['video_task_type']}` (only)",
                "- Requires actual multimodal materials: "
                f"`{str(profile_cfg['requires_multimodal_materials']).lower()}`; "
                f"minimum `{profile_cfg['minimum_material_inputs']}` image/video/audio input",
                "- Allowed multimodal material types: `"
                + "`, `".join(profile_cfg["allowed_multimodal_material_types"])
                + "`",
                "- Forbidden video task modes: `"
                + "`, `".join(profile_cfg["forbidden_video_task_modes"])
                + "`",
            ]
        )
    model_profile_items.extend(
        [
            f"- Group duration contract: `{profile_cfg['duration_min_seconds']}-{profile_cfg['duration_max_seconds']}` seconds",
            f"- Model-facing timeline granularity: `{profile_cfg['timeline_granularity_seconds']}` second(s)",
        ]
    )
    model_profile_block = textwrap.indent("\n".join(model_profile_items), "        ")
    if profile_cfg["provider_task_mapping"]:
        profile_rule = (
            "Seedance 2.5 横屏仙侠 profile 是模型硬合同；内部任务仍为 `multimodal_generation`，"
            "provider 创建请求由编译器映射为至少一项 reference content 加 "
            "`omni_reference_task_type=reference`；24 fps 只用于结果验收，不进入创建请求"
        )
        prompt_surface_rule = (
            "`final.txt` 保持资产无关的分镜母版，不虚构素材编号或 `@图片/@视频/@音频`；"
            "只有下游拿到真实且已授权的图片/视频/音频绑定后才可编译 provider reference content；"
            "不得回退到纯文本、首尾帧/关键帧、视频编辑、视频延长或轨道补全"
        )
    elif profile_cfg["profile_role"] == "hard-contract":
        profile_rule = (
            "Seedance 2.5 profile 是模型硬合同；唯一视频任务是 `multimodal_generation`，"
            "它只覆盖模型特定的时长、时间轴、参数、音频、素材职责和尾部规则，"
            "原剧本忠实、空间锁定、连续性、可拍性和真实审核仍以生成/审核 Skill 为准"
        )
        prompt_surface_rule = (
            "`final.txt` 保持资产无关的分镜母版，不手写虚构的 `@图片/@视频/@音频`；"
            "只有下游拿到至少一项真实图片/视频/音频素材绑定后，才按 profile 写入素材序号与职责；"
            "这些都是多模态输入素材，不是独立的参考生成模式；不得回退到纯文本，也不得切换到参考生成、"
            "首尾帧/关键帧、视频编辑、视频延长或轨道补全"
        )
    else:
        profile_rule = "Seedance Prompt Profile 只作为短剧风格参考层"
        prompt_surface_rule = (
            "profile 不得替代主生成规则，不得把模板编号、官方模板说明、`@图片/@视频/@音频` 占位符、"
            "广告/产品/视频延长/轨道补全/一镜到底等非短剧模板语气写入 `final.txt`"
        )
    visual_style_block = ""
    if visual_style == "3d-cg":
        visual_style_block = textwrap.indent(
            f"- 3D CG Visual Style Skill: `{cg_visual_style_skill_path}`",
            "        ",
        )

    return textwrap.dedent(
        f"""
        # Storyboard Agent Context

        ## Workspace
        - Project root: `{project_root}`
        - Generation rules source: `{generation_rules_source}`
        - Review rules source: `{reviewer_rules_source}`
        - Final output directory: `{out_dir}`
        - Episodes in this run: `{episodes_count}`
        - Generation mode: `{mode}`
        - Storyboard aspect: `{aspect}` ({aspect_label})
        - Visual style: `{visual_style}` ({visual_style_label})
        - Generation Skill: `{generator_skill_path}`
        - Review Skill: `{reviewer_skill_path}`
{model_profile_block}
{visual_style_block}

        ## Core Rules
        - dispatcher 不生成、不审核、不修稿；dispatcher 只创建 subagents/workers 并分发 episode prompt。
        - episode worker 是{aspect_label}短剧分镜生产 agent，只处理自己被分配的单个 episode。
        - 生成和审核规则全部以两个标准 `SKILL.md` 为准；{profile_rule}，不要在任务文件里重新解释规则。
        - 同一 worker、同一 run 的标准 Skill 和 profile 在启动时完整读取一次；文件未变化时在审核、修复复审和同 batch 第二集复用，逐集只重读 TASK、剧本、当前 final、机械事实和连续边界。
        - Project pack 只有在上方明确列出时才启用；启用后必须读取它的 entry skill 与 loaded files，未列出时不得按剧名或内容猜测项目包。
        - {prompt_surface_rule}。
        - Visual style 是本 run 的媒介风格约束：`{visual_style}`（{visual_style_label}）。{style_cfg["task_guidance"]}
        - episode worker 可以生成和初审，但 `review.txt` 必须按 `{reviewer_skill_name}/SKILL.md` 逐项审稿，不能写空泛通过。
        - 若用户要求强审核模式，reviewer-only worker 必须独立复审 `final.txt`。
        - `single` 模式：整集一次生成，再整集审核一次。
        - `scene` 模式：按场景标题拆段生成，再组装整集并审核。
        - 审核后只修硬错误；不要每次全量重写。
        - 每集最终产出 `final.txt` 和 `status.json`。
        - 如果硬错误无法修完，也要保留最好的 `final.txt`，并在 `status.json` 标记 `needs_review`。
        - 不要调用 DeepSeek/Qwen API 批处理脚本生成正文；Python 只准备、校验和收集。
        - 最终 `final.txt` 必须是自然分镜格式，不输出 JSON、调试标记或其他非分镜正文内容。
        """
    ).strip()


def make_episode_task(
    *,
    run_dir: Path,
    episode_dir: Path,
    episode: EpisodeInput,
    episode_id: str,
    output_name: str,
    generator_skill_path: Path,
    reviewer_skill_path: Path,
    seedance_profile_path: Path,
    aspect: str,
    mode: str,
    cg_visual_style_skill_path: Path | None = None,
    visual_style: str = "live-action",
    video_profile: str = DEFAULT_VIDEO_PROFILE,
    video_resolution: str | None = None,
    visual_style_preset: str | None = None,
    project_pack: dict | None = None,
) -> str:
    rel_root = episode_dir.relative_to(run_dir)
    aspect_cfg = storyboard_workflow_config(aspect, video_profile)
    aspect_label = aspect_cfg["label"]
    reviewer_skill_name = aspect_cfg["reviewer_name"]
    style_cfg = visual_style_config(visual_style)
    visual_style_label = style_cfg["label"]
    profile_cfg = video_profile_config(video_profile)
    preset = visual_style_preset_snapshot(video_profile, visual_style_preset)
    review_contract_version = (
        resolved_vertical_review_contract_version(video_profile)
        if aspect == "vertical"
        else None
    )
    resolution = resolved_video_resolution(video_profile, video_resolution)
    video_task_input_lines = ""
    if profile_cfg["video_task_type"]:
        video_task_input_lines = "\n".join(
            [
                f"- Video task type: `{profile_cfg['video_task_type']}` (the only supported task)",
                "- Multimodal material requirement: at least "
                f"`{profile_cfg['minimum_material_inputs']}` actual image/video/audio input before a model call; "
                "the storyboard master alone is not generation-ready",
                "- Forbidden video task modes: `"
                + "`, `".join(profile_cfg["forbidden_video_task_modes"])
                + "`",
            ]
        )
    if aspect == "horizontal":
        if video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
            aspect_contract_line = "Use the dedicated Seedance 2.5 timeline-only wrapper defined by the selected generator. 关键视觉事件必须直接进入实际时间轴，特效、声音、物理约束和生成易错点不得另起说明；不设独立峰值字段，不预设景别或运镜数量。不要写 `**一句话概述**`、`**视觉峰值/特效重点**`、`**运镜强化词**`、`**Seedance执行提示补充**` 或旧横屏字段；不再使用一句话概述或重复执行字段。Keep assets under 9 per group; if more are genuinely needed, split only at a stable state boundary."
        else:
            # Preserve the generic horizontal workflow.  Its visual-peak,
            # camera-summary, and execution fields are still part of that
            # skill; only the dedicated Seedance 2.5 xianxia profile is
            # timeline-only.
            aspect_contract_line = "Horizontal outputs must be generated as polished, Seedance-ready deliverables on the first pass, not rough drafts waiting for a separate rewrite. Use the current horizontal Seedance wrapper: `**人物**`, `**场景**`, `**道具/关键视觉资产**`, `**视觉峰值/特效重点**`, `**组间承接**`, `**横屏构图/调度**`, bare `N-M` shot-number lines, then each shot with `**镜头描述**`, `**光影设计**`, `**本镜估算时长**`, followed by `**组尾衔接**`, `**画面风格**`, `**运镜强化词**`, `**Seedance执行提示补充**`, and `**--neg**`. Do not write `**镜头号**：N-M`; do not use the old horizontal `组首空间锁定` or per-shot `运镜设计` fields. Keep assets under 9 per group; if the script requires more, split the group instead of deleting key story elements."
        if profile_cfg["timeline_granularity_seconds"] == 1 and profile_cfg["duration_max_seconds"] == 30:
            group_timing_line = (
                "Horizontal groups use bare `N-M` shot numbers and integer-second `**本镜估算时长**：X秒`; "
                "each group's shot durations must sum to an explicit integer total from 4 through 30 seconds. "
                "Do not inherit the older 6-15 second or 0.5-second timeline contract. Split only at a real space, "
                "goal, cast, dramatic-beat, information-landing, or reaction-landing boundary."
            )
        else:
            group_timing_line = "Horizontal groups use bare `N-M` shot numbers and `**本镜估算时长**：X秒` per shot; each group's estimated shot durations must sum to the integer group total. Prefer integer shot durations; use 0.5 seconds only for short reactions, prop inserts, or action aftershocks. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds. Do not compress key dialogue meaning just to fit the 15-second cap; split shots or groups instead."
        asset_id_contract_line = "- Horizontal final.txt may preserve user-provided asset IDs in `**人物**`, `**场景**`, and `**道具/关键视觉资产**`, such as `天天图8`; do not invent asset IDs, and do not write `参考图`, `首帧参考`, `尾帧参考`, `@图片`, `@视频`, or upload/call instructions."
        boundary_input_line = ""
        boundary_workflow_phrase = ""
        vertical_review_evidence_line = ""
    else:
        aspect_contract_line = "Vertical outputs follow the vertical generator skill contract; do not apply horizontal camera-motion fields unless the run aspect is horizontal."
        if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
            group_timing_line = (
                "Group-internal model-facing time ranges must use integer-second boundaries and the group total must be an integer second. "
                "The hard model range is 4-30 seconds. For one continuous cluster with the same main space, conflict goal, and cast, prefer one staged "
                "16-30 second group when the combined duration stays within 30 seconds. Use 8-15 seconds for an independent block that cannot merge "
                "across a real space/goal/cast break or a distinct dramatic beat, information landing, reaction landing, or scripted pause; use 4-7 seconds only for a genuine short beat."
            )
        else:
            group_timing_line = "Group-internal time ranges may use 0.5-second boundaries, and the group total must be an integer second. Default groups should be 10-15 seconds; only justified short beats may be 6-9 seconds; never exceed 15 seconds."
        asset_id_contract_line = "- Do not put asset IDs in `final.txt`; asset binding belongs to the asset extraction stage."
        boundary_input_line = "- Cross-episode boundary: `boundary_context.md` when present. If it marks a continuous boundary, compare its previous-episode tail with this episode's first group during generation and review."
        boundary_workflow_phrase = ", `boundary_context.md` when present"
        if review_contract_version is not None and review_contract_version >= 4:
            vertical_review_evidence_line = (
                f"For vertical review contract v{review_contract_version}, run pre-check first so Python writes `review_facts.json`. "
                "That file is only an exact-content binding: copy its compact `mechanical_evidence` object exactly, then independently review "
                "the script and every group in the current final. Reviewer JSON must contain one model-authored `group_reviews` entry per group, "
                "with a concise natural-language semantic finding and concrete evidence. Python must not generate dialogue, handoff, camera-motion, "
                "or space-lock review conclusions, and v4 must not use `semantic_coverage` or script-generated checked/pass lists. Report detailed "
                "exceptions in semantic_checks/issues/warnings and include `issue_instances_total` plus `affected_groups` as defined by "
                f"`{reviewer_skill_name}/SKILL.md`. For a continuous boundary, pre-check also binds the actual predecessor final hash; if that "
                "file is missing or later changes, wait or re-review instead of reusing stale evidence."
            )
        elif review_contract_version is not None and review_contract_version >= 3:
            vertical_review_evidence_line = (
                f"For vertical review contract v{review_contract_version}, run pre-check first so Python writes `review_facts.json`. "
                "Reviewer JSON must copy its compact `mechanical_evidence` object exactly, list every semantically reviewed item in compact `semantic_coverage`, "
                "and include `issue_instances_total` plus `affected_groups` as defined by "
                f"`{reviewer_skill_name}/SKILL.md`. Do not repeat full `dialogue_checks`, `handoff_checks`, or `camera_motion_checks` arrays in v3; "
                "the reviewer still checks their semantic correctness and reports only exceptions in semantic_checks/issues/warnings. For a continuous boundary, "
                "pre-check also binds the actual predecessor final hash; if that file is missing or later changes, wait or re-review instead of reusing stale evidence."
            )
        else:
            vertical_review_evidence_line = f"Reviewer JSON must include complete `dialogue_checks`, `handoff_checks`, `camera_motion_checks`, `issue_instances_total`, and `affected_groups` as defined by `{reviewer_skill_name}/SKILL.md`."
    if aspect == "vertical" and review_contract_version is not None and review_contract_version >= 3:
        review_preparation_clause = "Run pre-check to generate `review_facts.json`, then"
        review_current_inputs = "`script.txt`, current `final.txt`, `review_facts.json` and the active boundary"
        rereview_preparation_clause = "Run pre-check again and"
    else:
        review_preparation_clause = "Run pre-check, then"
        review_current_inputs = "`script.txt` and current `final.txt`"
        rereview_preparation_clause = "Run pre-check again and"
    review_facts_output_line = (
        "- `review_facts.json` (generated by pre-check; mechanical content binding only; never hand-write)"
        if aspect == "vertical" and review_contract_version is not None and review_contract_version >= 3
        else ""
    )
    profile_read_phrase = "the selected Seedance prompt profile"
    if profile_cfg["provider_task_mapping"]:
        profile_input_line = (
            f"- Seedance prompt profile: `{seedance_profile_path}`，这是 `{video_profile}` 的模型硬合同；"
            "内部唯一任务是 `multimodal_generation`，provider 请求必须含至少一项 reference content，"
            "并由编译器写入 `omni_reference_task_type=reference`；24 fps 只做结果验收，不作为创建参数"
        )
        profile_constraint = (
            "the Seedance 2.5 profile overrides older timing and task clauses; its internal task is "
            "multimodal_generation while the provider serializer maps real bound materials to reference content; "
            "it forbids text-only, first/last-frame, keyframe, edit, extend, and track-completion modes and never "
            "permits invented material IDs"
        )
    elif profile_cfg["profile_role"] == "hard-contract":
        profile_input_line = (
            f"- Seedance prompt profile: `{seedance_profile_path}`，这是 `{video_profile}` 的模型硬合同；"
            "模型特定的唯一多模态生成任务、时长、整数时间轴、参数分离、原生音频、素材职责和尾部规则以它为准"
        )
        profile_constraint = (
            "the Seedance 2.5 profile overrides only model-specific clauses inherited from older Seedance contracts; "
            "its only task is multimodal_generation and it forbids text-only/reference/keyframe/edit/extend/track-completion modes; "
            "it does not weaken script fidelity, spatial continuity, filmability, or reviewer evidence"
        )
    else:
        profile_input_line = f"- Seedance prompt profile: `{seedance_profile_path}`，只作为短剧风格参考层，不得复制模板正文、模板编号、官方占位符或非短剧模板语气到 `final.txt`"
        profile_constraint = "Seedance Prompt Profile is only a reference layer"
    visual_style_input_line = ""
    visual_style_workflow_phrase = ""
    # The dedicated Seedance 2.5 xianxia profile owns its visual preset and
    # timeline-only contract. Do not load the generic 3D-CG skill as an extra
    # context source: it still contains legacy hero/camera-field guidance for
    # generic horizontal runs and can reintroduce those constraints.
    if visual_style == "3d-cg" and video_profile != SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
        visual_style_input_line = f"\n- 3D CG visual style skill: `{cg_visual_style_skill_path}`，只作为 3D CG 媒介风格参考层，不得替代主生成和审核规则"
        visual_style_workflow_phrase = ", the 3D CG visual style skill"
    preset_input_line = ""
    if preset:
        preset_input_line = (
            f"\n- Visual style preset: `{preset['id']}` ({preset['name']}), version `{preset['version']}`, "
            f"SHA-256 `{preset['sha256']}`"
        )
    project_pack_input_lines = "- Project pack: not enabled; do not infer one from the title or script."
    project_pack_workflow_phrase = ""
    if project_pack:
        project_pack_input_lines = "\n".join(
            [
                f"- Project pack: `{project_pack['id']}` ({project_pack['name']}), version `{project_pack['version']}`, SHA-256 `{project_pack['sha256']}`",
                f"- Project pack entry skill: `{project_pack['entry_skill_path']}`",
                "- Project pack authoritative files: "
                + ", ".join(f"`{item['path']}`" for item in project_pack["loaded_files"]),
            ]
        )
        project_pack_workflow_phrase = ", the explicit project pack and all of its authoritative files"
    if aspect == "horizontal":
        if visual_style == "3d-cg":
            if video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
                style_delivery_line = (
                    "横屏 final.txt 每组必须直接写入 3D CG 版 `**画面风格**` 和 `**--neg**`："
                    "正向包含高质量动漫3D CG短剧风格、二次元角色设计、风格化面部与眼睛、清晰轮廓线、"
                    "高质量卡通渲染、PBR材质与手绘质感融合、电影级布光、自然景深；"
                    "不得写真人实拍、真实摄影、真实演员；负向不得包含 `3D渲染`、`CG感`、`动画感`、`卡通`、`动漫`、`二次元`。"
                    "不预设运镜，也不设运镜数量指标：Seedance 2.5 会根据主体、动作、构图、空间关系和节奏自行选择合理运动；对白、状态确认和安静反应可用稳定镜头承载口型。"
                    "只有剧情、轴线、复杂位移或连续性确实需要锁定镜头行为时，才在对应时间轴补充最少必要约束，不要为凑数量让全组炫技运动。"
                    "关键视觉事件必须直接进入实际时间轴中的镜头描述、光影、特效和声音，不设独立峰值字段；"
                    "下游提交提示词会按人物资产、场景资产、道具与关键视觉资产分类前置，补上完整整体画风和组间空间衔接，不再使用一句话概述或重复执行字段。"
                )
            else:
                style_delivery_line = (
                    "横屏 final.txt 每组必须直接写入 3D CG 版 `**画面风格**` 和 `**--neg**`："
                    "正向包含高质量动漫3D CG短剧风格、二次元角色设计、风格化面部与眼睛、清晰轮廓线、"
                    "高质量卡通渲染、PBR材质与手绘质感融合、电影级布光、自然景深；"
                    "不得写真人实拍、真实摄影、真实演员；负向不得包含 `3D渲染`、`CG感`、`动画感`、`卡通`、`动漫`、`二次元`。"
                    "3D CG 横屏每组至少安排 1 个有明确路径或落点的可见运镜，例如横向跟拍、前景掠过、半环绕、贴地推进、低角度推近、焦点转移或急停落点；"
                    "对白密集段仍保留稳定镜头承载口型，不要全组炫技运动。"
                    "视觉峰值不只来自打斗，也要判断关键道具显影、身份揭示、权力压场、危险进入、环境异变、心理冲击、信息落点；"
                    "beat/hero 级视觉峰值必须进入镜头描述、光影设计、运镜强化词或 Seedance 执行提示补充，不能只靠固定画面风格尾部。"
                )
        else:
            style_delivery_line = (
                "横屏 final.txt 每组必须直接写入真人实拍版 `**画面风格**` 和 `**--neg**`；"
                "收集阶段不会为横屏追加固定尾部。"
            )
    else:
        if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
            style_delivery_line = (
                "收集阶段会追加 Seedance 2.5 专属真人短剧画面/声音尾部；不会追加旧版大包通用 `--neg`。"
                "worker 只在确有本组剧情风险时写 2-5 条具体 `视频禁止项`，收集时才转换为聚焦负面词。"
            )
        else:
            style_delivery_line = (
                "收集阶段会按该风格追加每组固定 `画面风格` 和基础 `--neg`；"
                "worker 不要在 `final.txt` 每组重复写固定尾部。"
            )

    if mode == "scene":
        inputs = "- Segment scripts: `segments/seg*/script.txt`"
        outputs = textwrap.dedent(
            f"""
            - `segments/segXX/draft.txt`
            - `segments/segXX/review.md` (only when this episode has more than one segment;
              with a single segment the episode-level `review.txt` already covers the same
              groups, so writing both is duplicated work)
            - `segments/segXX/final.txt`
            - `final.txt`
            {review_facts_output_line}
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            f"""
            1. At worker start, read `../../context.md`, both standard `SKILL.md` files, {profile_read_phrase}{visual_style_workflow_phrase}{project_pack_workflow_phrase}, `script.txt`{boundary_workflow_phrase}, and each segment script. Keep immutable skills in the worker context; do not reread them during review or focused re-review unless the path or file changed.
            2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/final.txt`. With more than one segment also write `segments/segXX/review.md`, scoped to that segment's own groups — cross-segment handoffs and whole-episode review binding/coverage belong to step 4, not repeated per segment. With a single segment, skip `review.md` and review once in step 4.
            3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. {group_timing_line}
            4. {review_preparation_clause} reread {review_current_inputs} only; review once using `{reviewer_skill_name}` and write the raw reviewer JSON to `review.txt`.
            5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. {rereview_preparation_clause} re-run `{reviewer_skill_name}` against the current final after repairs.
            6. Write `status.json` with reviewer metadata, then run validation. Validation is txt-only by default; storyboard index JSON/XLSX export is opt-in and not part of the current required output.
            7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.
            """
        ).strip()
    else:
        inputs = "- Segment scripts: not used in `single` mode."
        outputs = textwrap.dedent(
            f"""
            - `final.txt`
            {review_facts_output_line}
            - `review.txt`
            - `status.json`
            """
        ).strip()
        workflow = textwrap.dedent(
            f"""
            1. At worker start, read `../../context.md`, both standard `SKILL.md` files, {profile_read_phrase}{visual_style_workflow_phrase}{project_pack_workflow_phrase}, and `script.txt`{boundary_workflow_phrase}. Keep immutable skills in the worker context; do not reread them during review or focused re-review unless the path or file changed.
            2. Generate the full episode directly into `final.txt`. Every group heading must include a stable `cut_id` in the form `EPxx-GNN`, for example `=== [cut_id: EP02-G01] 第1组：标题（总时长：12秒，镜头数：4个） ===`. {group_timing_line}
            3. {review_preparation_clause} reread {review_current_inputs} only; review the full episode once using the review skill and write `review.txt`.
            4. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups.
            5. {rereview_preparation_clause} re-run `{reviewer_skill_name}` after repairs and update `review.txt`.
            6. Write `status.json` with reviewer metadata, then run validation. Validation is txt-only by default; storyboard index JSON/XLSX export is opt-in and not part of the current required output.
            7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.
            """
        ).strip()
    return f"""# Task: {episode.display_name}

Mode: `{mode}`
Aspect: `{aspect}` ({aspect_label})

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `{generator_skill_path}`
- Review skill: `{reviewer_skill_path}`
- Vertical review contract: `{f'v{review_contract_version}' if review_contract_version is not None else 'not applicable'}`
- Video profile: `{video_profile}` ({profile_cfg['label']})
- Target video model: `{profile_cfg['target_video_model']}`
{video_task_input_lines}
- Video parameters: ratio `{profile_cfg['aspect_ratio'] or 'profile-default'}`, resolution `{resolution or 'profile-default'}`, fps `{profile_cfg['fps'] or 'profile-default'}`, generate_audio `{str(profile_cfg['generate_audio']).lower() if profile_cfg['generate_audio'] is not None else 'profile-default'}`
- Visual style: `{visual_style}` ({visual_style_label})
{profile_input_line}
{visual_style_input_line}
{preset_input_line}
{project_pack_input_lines}
- Full episode script: `script.txt`
{boundary_input_line}
{inputs}

## Required Outputs
{outputs}

{make_production_focus_block(aspect=aspect, video_profile=video_profile)}

## Visual Style Contract
- 本 run 的视觉风格是 `{visual_style}`（{visual_style_label}）。
- {style_cfg["task_guidance"]}
- {style_delivery_line}
- `视频禁止项` 仍只写本组剧情错误，不要混入通用画质词或媒介风格词。

## Workflow
{workflow}

Pre-check command (run before calling {reviewer_skill_name} to catch mechanical issues early):

```powershell
python "{Path(__file__).resolve()}" validate-episode --episode-dir "{episode_dir}" --pre-check
```

For segment-level pre-check (scene mode, validate a segment draft before review):

```powershell
python "{Path(__file__).resolve()}" validate-episode --episode-dir "{episode_dir}" --pre-check --content-file "{episode_dir}/segments/segXX/draft.txt"
```

Full validation command (run after review.txt and status.json are written):

```powershell
python "{Path(__file__).resolve()}" validate-episode --episode-dir "{episode_dir}"
```

`status.json` requirements:

- `episode_id`: `{episode_id}`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `{output_name}`
- `summary`: short Chinese summary
- `hard_issues_remaining`: copy unresolved hard issues from the real reviewer result
- `warnings`: copy or summarize warnings from the real reviewer result
- `reviewer_source`: must be `{reviewer_skill_name}`
- `reviewer_pass`: copy the boolean `pass` from `review.txt` after `review.txt` exists
- `reviewer_issues_count`: copy `len(review.txt.issues)` after `review.txt` exists
- `reviewer_warnings_count`: copy `len(review.txt.warnings)` after `review.txt` exists

Do not prefill `reviewer_pass=true` or issue/warning counts before writing the real `review.txt`.

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `{reviewer_skill_name}`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.
Reviewer JSON must include non-empty `checked_groups` and full `audit_coverage` fields as required by `{reviewer_skill_name}/SKILL.md`.
Reviewer JSON must also include at least 3 `spot_checks` items with `group`, `type`, and `evidence`.
Reviewer JSON must include at least 3 `semantic_checks` items with `group`, `type`, `result`, `evidence`, and `fix_instruction`; `result` must be `pass`, `warning`, or `issue`.
{vertical_review_evidence_line}
If `pass=true`, `issues` must be empty and no `semantic_checks` item may use `result=issue`; if `pass=false`, `issues` must contain the blocking hard issue.
Template/model-term pollution must use `prompt_pollution` as the issue/warning `rule` or semantic check `type`.
`status.json` reviewer fields must stay consistent with `review.txt`.
`final.txt` cut_id contract:

- Every group heading must include exactly one `cut_id`.
- Use the current episode id and group number: `EP01-G01`, `EP01-G02`, ... for ep01; `EP30-G01`, ... for ep30.
- Preferred heading format: `=== [cut_id: EPxx-GNN] 第N组：标题（总时长：XX秒，镜头数：X个） ===`.
{asset_id_contract_line}

## Important Constraints
- Rules live in the two standard `SKILL.md` files; {profile_constraint}. Do not duplicate or reinterpret them here.
- {aspect_contract_line}
- Work only inside `{rel_root}`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
""".strip()


def make_production_focus_block(
    *,
    aspect: str,
    video_profile: str = DEFAULT_VIDEO_PROFILE,
) -> str:
    if aspect != "vertical":
        return ""
    policy_version = storyboard_quality_policy_version()
    if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
        timing_focus = (
            "- 先按内部表演节奏精确估时，再把模型可见时间轴整理成整数秒边界；"
            "同场、同目标、同批人物的连续流程在总时长不超过 30 秒时优先合为 16-30 秒长组；"
            "8-15 秒用于确有空间/目标/人物断点、独立戏剧节拍、信息落点、反应落点或原剧本明确停顿的独立块，4-7 秒只用于真实短节拍。"
        )
    else:
        timing_focus = "- 不要为凑满 10 秒硬塞动作、对白或停顿；短承接和单句反应允许保留 6-9 秒。"
    return textwrap.dedent(
        f"""
        ## Production Focus
        - 组首空间锁定等于本组第一帧，只写当前可生成状态，不写前情回顾。
        - 每个时间段默认只承载一个主动作目标；同一主体、空间、目标且顺序和结果清楚的紧凑动作链可在 2-3 秒完成，不按动词数量机械拆分。
        - 每镜可合理运镜也可固定机位，不设数量指标；运镜必须写清动机、主体、路径和落点，并与动作、竖屏构图和连续性兼容。
        - 高冲击打断后先稳定打断/反应，放下道具、跨位移、保护站位、团圆确认等归位动作另起时间段或另组。
        {timing_focus}
        - 保护动作写清挡在谁前面，非主动作人物只写站位和轻反应，不抢主动作。
        - 关键道具写清归属、位置和状态变化，组尾必须能接到下一组。
        - `视频禁止项` 只写 2-5 个具体剧情错误，必须锚定本组或本集上下文；完整规则仍以 generator/reviewer skill 和 quality policy 为准（policy: `{policy_version}`）。
        """
    ).strip()


def make_agent_prompt(episode_dir: Path) -> str:
    return textwrap.dedent(
        f"""
        You are a storyboard production agent running inside a prepared file workspace.

        Start by reading `TASK.md`.
        Complete the task end-to-end for this episode.
        Write all required files.
        Run the validation command from `TASK.md`.
        When finished, leave the final answer concise and point to `final.txt` and `status.json`.

        Episode workspace: `{episode_dir}`
        """
    ).strip()


def make_standard_skill_md(*, name: str, description: str, title: str, body: str) -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
        f"# {title}\n\n"
        f"{body.strip()}\n"
    )


def ensure_project_agent_skills(
    *,
    project_root: Path,
    prompt_path: Path | None,
    review_skill_path: Path | None,
    aspect: str,
    video_profile: str = DEFAULT_VIDEO_PROFILE,
) -> tuple[Path, Path, Path, Path]:
    aspect_cfg = storyboard_workflow_config(aspect, video_profile)
    skills_root = project_root / PROJECT_AGENT_SKILLS_DIR
    generator_skill_dir = skills_root / aspect_cfg["generator_dir"]
    reviewer_skill_dir = skills_root / aspect_cfg["reviewer_dir"]
    generator_skill_dir.mkdir(parents=True, exist_ok=True)
    reviewer_skill_dir.mkdir(parents=True, exist_ok=True)

    generator_skill_path = generator_skill_dir / "SKILL.md"
    reviewer_skill_path = reviewer_skill_dir / "SKILL.md"
    if prompt_path is not None:
        prompt_text = read_utf8_text(prompt_path)
        write_utf8(
            generator_skill_path,
            make_standard_skill_md(
                name=aspect_cfg["generator_name"],
                description=aspect_cfg["generator_description"],
                title="Storyboard Generator",
                body=prompt_text,
            ),
        )
        generation_rules_source = prompt_path.resolve()
    elif generator_skill_path.is_file():
        generation_rules_source = generator_skill_path.resolve()
    else:
        raise FileNotFoundError(
            f"Generation skill not found: {generator_skill_path}. "
            f"Create agent_skills/{aspect_cfg['generator_dir']}/SKILL.md or pass --prompt explicitly."
        )

    if review_skill_path is not None:
        review_skill_text = read_utf8_text(review_skill_path.resolve())
        write_utf8(
            reviewer_skill_path,
            make_standard_skill_md(
                name=aspect_cfg["reviewer_name"],
                description=aspect_cfg["reviewer_description"],
                title="Storyboard Reviewer",
                body=review_skill_text,
            ),
        )
        reviewer_rules_source = review_skill_path.resolve()
    elif reviewer_skill_path.is_file():
        reviewer_rules_source = reviewer_skill_path.resolve()
    else:
        if aspect != "vertical":
            raise FileNotFoundError(
                f"Review skill not found: {reviewer_skill_path}. "
                f"Create agent_skills/{aspect_cfg['reviewer_dir']}/SKILL.md or pass --review-skill explicitly."
            )
        review_skill_text = load_review_skill_text(None)
        write_utf8(
            reviewer_skill_path,
            make_standard_skill_md(
                name=aspect_cfg["reviewer_name"],
                description=aspect_cfg["reviewer_description"],
                title="Storyboard Reviewer",
                body=review_skill_text,
            ),
        )
        reviewer_rules_source = reviewer_skill_path.resolve()

    return (
        generator_skill_path.resolve(),
        reviewer_skill_path.resolve(),
        generation_rules_source,
        reviewer_rules_source,
    )


def is_simple_worker_batch_candidate(task: dict) -> bool:
    if "script_chars" not in task or "segments" not in task:
        return False
    try:
        script_chars = int(task.get("script_chars") or 0)
        segments = int(task.get("segments") or 0)
    except (TypeError, ValueError):
        return False
    return (
        script_chars <= SIMPLE_BATCH_MAX_SCRIPT_CHARS
        and segments <= SIMPLE_BATCH_MAX_SEGMENTS
    )


SCRIPT_SCENE_HEADING_RE = re.compile(
    r"(?m)^\s*场(?:次[^\s：:]*)?[0-9一二三四五六七八九十百千万零〇两-]*\s*[：:]?\s*"
    r"(?P<interior>(?:内景|外景|内景/外景|外景/内景)[^\n]*?)\s*[-－]\s*(?P<time>[^\n（(人物：:]*)"
)

# Second source dialect: `1-1 跨海大桥 日 外出场角色：...`, i.e. a numbered scene id
# followed by place, then time, then interior/exterior. Neither SCRIPT_SCENE_HEADING_RE
# (which requires the 场次N：内景 XXX - 时间 form) nor batch_generate_storyboards'
# SCENE_HEADING_RE (which requires a `/` between time and 内/外) matches it, so scripts in
# this dialect produced zero scene boundaries and silently disabled cross-episode
# continuity for the whole run.
SCRIPT_NUMBERED_SCENE_HEADING_RE = re.compile(
    r"(?m)^[﻿ \t#]*\d{1,3}\s*[-－—]\s*\d{1,3}\s+(?P<body>[^\n]+)$"
)
# Longer time words first: alternation is first-match, so 夜晚 must precede 夜.
SCRIPT_SCENE_TIME_INTERIOR_RE = re.compile(
    r"(?P<time>清晨|傍晚|黄昏|黎明|凌晨|深夜|夜晚|晚上|白天|午后|中午|下午|上午|日|夜|晨|晚)"
    r"\s*(?P<interior>内外|外内|内|外)"
)


def _normalized_scene_place(place: str) -> str:
    return re.sub(r"[\s/＆&、，,]+", "|", place).strip("|").lower()


def _numbered_scene_boundaries(script_text: str) -> list[tuple[int, dict[str, str]]]:
    """Parse the `NN-MM 地点 时间 内/外` source dialect."""
    scenes: list[tuple[int, dict[str, str]]] = []
    for match in SCRIPT_NUMBERED_SCENE_HEADING_RE.finditer(script_text):
        # `出场角色：` is glued straight onto the interior marker (`... 日 外出场角色：林知意`),
        # so cut it off before looking for the time/interior pair.
        body = match.group("body").split("出场角色")[0]
        hits = list(SCRIPT_SCENE_TIME_INTERIOR_RE.finditer(body))
        if not hits:
            continue
        # Take the last pair so a place name containing a time word (e.g. 日料店) does not
        # truncate the place.
        hit = hits[-1]
        place = body[: hit.start()].strip()
        if not place:
            continue
        normalized_place = _normalized_scene_place(place)
        if not normalized_place:
            continue
        scenes.append(
            (
                match.start(),
                {
                    "heading": match.group(0).strip(),
                    "place": place,
                    "normalized_place": normalized_place,
                    "time": hit.group("time").strip(),
                },
            )
        )
    return scenes


def _script_scene_boundaries(script_text: str) -> list[dict[str, str]]:
    scenes: list[tuple[int, dict[str, str]]] = []
    for match in SCRIPT_SCENE_HEADING_RE.finditer(script_text):
        raw_place = match.group("interior").strip()
        place = re.sub(r"^(?:内景|外景|内景/外景|外景/内景)\s*", "", raw_place).strip()
        normalized_place = _normalized_scene_place(place)
        if not normalized_place:
            continue
        scenes.append(
            (
                match.start(),
                {
                    "heading": match.group(0).strip(),
                    "place": place,
                    "normalized_place": normalized_place,
                    "time": match.group("time").strip(),
                },
            )
        )
    scenes.extend(_numbered_scene_boundaries(script_text))
    scenes.sort(key=lambda item: item[0])
    return [scene for _offset, scene in scenes]


def build_source_continuity_links(episodes: list[EpisodeInput]) -> list[dict[str, object]]:
    """Identify adjacent episodes whose source boundary stays in the same scene."""
    links: list[dict[str, object]] = []
    for index in range(len(episodes) - 1):
        previous_scenes = _script_scene_boundaries(episodes[index].script_text)
        current_scenes = _script_scene_boundaries(episodes[index + 1].script_text)
        if not previous_scenes or not current_scenes:
            continue
        previous_scene = previous_scenes[-1]
        current_scene = current_scenes[0]
        previous_places = set(previous_scene["normalized_place"].split("|"))
        current_places = set(current_scene["normalized_place"].split("|"))
        if not (previous_places & current_places):
            continue
        links.append(
            {
                "previous_index": index,
                "current_index": index + 1,
                "previous_scene": previous_scene,
                "current_scene": current_scene,
                "time_conflict": bool(
                    previous_scene["time"]
                    and current_scene["time"]
                    and previous_scene["time"] != current_scene["time"]
                ),
            }
        )
    return links


def build_worker_batches(tasks: list[dict]) -> list[list[dict]]:
    batches: list[list[dict]] = []
    index = 0
    while index < len(tasks):
        current = tasks[index]
        next_task = tasks[index + 1] if index + 1 < len(tasks) else None
        if (
            next_task is not None
            and (
                (
                    current.get("continuity_with_next") is True
                    and next_task.get("continuous_from_previous") is True
                )
                or (
                    is_simple_worker_batch_candidate(current)
                    and is_simple_worker_batch_candidate(next_task)
                    and current.get("continuous_from_previous") is not True
                    and next_task.get("continuous_from_previous") is not True
                )
            )
        ):
            batches.append([current, next_task])
            index += MAX_EPISODES_PER_WORKER_BATCH
        else:
            batches.append([current])
            index += 1
    return batches


def format_worker_batch_label(batch: list[dict]) -> str:
    return ", ".join(f"`{task['episode_id']}`" for task in batch)


def worker_batch_weight(batch: list[dict]) -> int:
    """Scheduling weight for a batch: the largest script it contains.

    Deliberately just `script_chars`. Measured against a finished 20-episode run, script
    length alone correlated 0.841 with the number of storyboard groups an episode actually
    produced -- the real unit of worker effort. A hand-weighted blend of character count,
    scene count and action-verb density scored 0.801 on the same data, i.e. worse. Revisit
    with more runs before adding signals.
    """
    weights = []
    for task in batch:
        try:
            weights.append(int(task.get("script_chars") or 0))
        except (TypeError, ValueError):
            weights.append(0)
    return max(weights) if weights else 0


def format_worker_batch_weight(batch: list[dict]) -> str:
    return f"~{worker_batch_weight(batch)} chars"


def format_worker_batch_prompts(batch: list[dict]) -> str:
    return ", ".join(f"`{task['prompt_file']}`" for task in batch)


def enrich_tasks_for_worker_batching(tasks: list[dict]) -> None:
    for index, task in enumerate(tasks):
        if "script_chars" not in task:
            script_path = Path(task["episode_dir"]) / "script.txt"
            if script_path.exists():
                task["script_chars"] = len(read_utf8_text(script_path))
            else:
                task["script_chars"] = SIMPLE_BATCH_MAX_SCRIPT_CHARS + 1
        if (
            task.get("continuous_from_previous") is True
            and not task.get("depends_on_episode")
            and index > 0
        ):
            task["depends_on_episode"] = tasks[index - 1]["episode_id"]


def write_runner_scripts(
    *,
    run_dir: Path,
    agent: str,
    parallelism: int,
    model: str | None,
) -> None:
    manifest = read_json(run_dir / "manifest.json")
    tasks = manifest["episodes"]
    enrich_tasks_for_worker_batching(tasks)
    worker_batches = build_worker_batches(tasks)

    for stale in ("run_codex_parallel.ps1", "run_qwen_parallel.ps1"):
        stale_path = run_dir / stale
        if stale_path.exists():
            stale_path.unlink()

    task_lines = []
    initial_worker_lines = []
    pending_prompt_lines = []
    worker_plan_lines = []
    for index, task in enumerate(tasks, start=1):
        task_lines.append(
            f"- `{task['episode_id']}`: dispatch `{task['prompt_file']}` to one worker. "
            f"Worker writes only under `{task['episode_dir']}`."
        )
        pending_prompt_lines.append(f"- `{task['prompt_file']}`")
    for index, batch in enumerate(worker_batches, start=1):
        dependency = batch[0].get("depends_on_episode")
        dependency_label = f" [wait for `{dependency}`]" if dependency else " [ready]"
        worker_plan_lines.append(
            f"- batch {index}{dependency_label}: {format_worker_batch_label(batch)} "
            f"({format_worker_batch_weight(batch)}) -> {format_worker_batch_prompts(batch)}"
        )
    ready_batches = [batch for batch in worker_batches if not batch[0].get("depends_on_episode")]
    # Start the heaviest ready batches first. Batch *numbering* stays in source order so the
    # plan reads top to bottom, but the opening wave is picked by weight: on a measured
    # 20-episode run the three heaviest episodes landed last and ate 29% of wall clock with
    # no remaining work to overlap them against.
    ready_batches = sorted(ready_batches, key=worker_batch_weight, reverse=True)
    for worker_index, batch in enumerate(ready_batches[:parallelism], start=1):
        initial_worker_lines.append(
            f"- worker {worker_index}: {format_worker_batch_label(batch)} "
            f"({format_worker_batch_weight(batch)}) -> {format_worker_batch_prompts(batch)}"
        )

    codex_model_arg = f" -m {model}" if model else ""
    sample_task = tasks[0] if tasks else None
    codex_example = ""
    qwen_example = ""
    kimi_example = ""
    claude_example = ""
    if sample_task:
        claude_example = (
            f'In Claude Code, dispatch with the Agent tool (`run_in_background: true`) using the prompt '
            f'from `{sample_task["prompt_file"]}`. Do not launch any model CLI.'
        )
        codex_example = (
            f'codex exec --skip-git-repo-check --sandbox workspace-write --cd "{run_dir}"'
            f'{codex_model_arg} - < "{sample_task["prompt_file"]}"'
        )
        qwen_example = f'qwen < "{sample_task["prompt_file"]}"'
        kimi_example = (
            f'Open Kimi Code in the workspace and use the Agent tool with the prompt '
            f'from `{sample_task["prompt_file"]}`.'
        )
    tasks_markdown = "\n".join(task_lines)

    if agent == "claude":
        worker_capability = "Claude Code Agent tools (run_in_background)"
    elif agent == "kimi":
        worker_capability = "Kimi Code Agent tools"
    elif agent == "qwen":
        worker_capability = "Qwen worker/subagent tools"
    else:
        worker_capability = "Codex subagents/workers"

    manual_cli_blocks = []
    if agent == "claude":
        # Claude Code dispatches through the Agent tool, never a model CLI, so the
        # Codex/Qwen command lines below would be actively wrong guidance here.
        if claude_example:
            manual_cli_blocks.append(f"Claude Code dispatch:\n\n{claude_example}")
    else:
        if codex_example:
            manual_cli_blocks.append(f"Codex example:\n\n```powershell\n{codex_example}\n```")
        if qwen_example:
            manual_cli_blocks.append(f"Qwen example:\n\n```powershell\n{qwen_example}\n```")
        if agent == "kimi" and kimi_example:
            manual_cli_blocks.append(f"Kimi Code example:\n\n{kimi_example}")
    manual_cli_section = "\n\n".join(manual_cli_blocks)

    write_utf8(
        run_dir / "NEXT_STEPS.md",
        f"""# Dispatcher Instructions

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, Kimi Code, Claude Code, or any model process.

Do not treat this file as a production task list.
Give `DISPATCH_PROMPT.md` to the host agent. The host agent is a dispatcher only and must not write episode files itself.

## Hard Stop

- Main thread is the dispatcher, not a storyboard production worker.
- Main thread must not directly process any episode.
- Main thread must not open `episodes/ep*/script.txt` and start writing storyboard content.
- Main thread must not write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
- Main thread's only job is to create subagents/workers and dispatch episode prompts.
- If the current environment cannot create subagents/workers, or needs user authorization before creating them, immediately stop and reply `NEED_USER_DISPATCH` with the pending prompt list.
- Do not downgrade to sequential main-thread episode processing.

## Required Dispatch

Use {worker_capability}.
Run up to {parallelism} workers in parallel.
Worker batches are generated dynamically from episode complexity.
Simple batch threshold: <= {SIMPLE_BATCH_MAX_SCRIPT_CHARS} script chars and <= {SIMPLE_BATCH_MAX_SEGMENTS} segment.
Batch size limit: {MAX_EPISODES_PER_WORKER_BATCH} episodes per worker.
When one worker handles two episodes, it must fully finish generation, review, repair, and validation for the first episode before starting the second.
Never merge reviews or outputs across episodes.

Dynamic worker batches:

{chr(10).join(worker_plan_lines) if worker_plan_lines else "- No episodes found."}

Initial worker wave:

{chr(10).join(initial_worker_lines) if initial_worker_lines else "- No episodes found."}

When any worker finishes, dispatch any unfinished batch marked `[ready]`, or a blocked batch only after its dependency episode has `status=done`, a current `final.txt`, and passed validation. Do not occupy a worker slot waiting for an unfinished predecessor; fill it with another ready independent batch.

## Episode Tasks

{tasks_markdown}

## Pending Prompt List

{chr(10).join(pending_prompt_lines) if pending_prompt_lines else "- No episodes found."}

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

{manual_cli_section}

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\\COLLECT_RESULTS.ps1
```
""",
    )

    write_utf8(
        run_dir / "DISPATCH_PROMPT.md",
        f"""# Auto-Storyboard Dispatcher Prompt

You are the dispatcher, not a storyboard production worker.

Your only tasks:
1. Read this file.
2. Create subagents/workers for the episode prompts below.
3. Wait for workers to finish, then run collection and summary checks.

## Absolute Prohibitions

- Do not directly generate any storyboard body in the main thread.
- Do not process `ep01`, `ep02`, `ep03`, or any other episode in the main thread.
- Do not open `episodes/ep*/script.txt` and begin production work.
- Do not write `episodes/ep*/draft.txt`, `episodes/ep*/final.txt`, `episodes/ep*/review.txt`, or `episodes/ep*/status.json` from the main thread.
- Do not sequentially process all episodes yourself.
- If you cannot create subagents/workers, immediately output `NEED_USER_DISPATCH` and list the prompt paths below.
- Do not downgrade to sequential main-thread episode processing.

## Worker Dispatch

Use {worker_capability}.
Run up to {parallelism} workers in parallel.
Worker batches are generated dynamically from episode complexity.
Simple batch threshold: <= {SIMPLE_BATCH_MAX_SCRIPT_CHARS} script chars and <= {SIMPLE_BATCH_MAX_SEGMENTS} segment.
Batch size limit: {MAX_EPISODES_PER_WORKER_BATCH} episodes per worker.
When one worker handles two episodes, it must complete the first episode's generation, real review, hard-issue repair, re-review, and validation before starting the second.

Dynamic worker batches:

{chr(10).join(worker_plan_lines) if worker_plan_lines else "- No episodes found."}

Initial worker wave:

{chr(10).join(initial_worker_lines) if initial_worker_lines else "- No episodes found."}

All episode prompts:

{chr(10).join(pending_prompt_lines) if pending_prompt_lines else "- No episodes found."}

Never dispatch a batch marked `[wait for epXX]` until that predecessor has `status=done`, a current `final.txt`, and passed validation. Keep worker slots on ready independent batches instead of starting a blocked worker that can only wait.

## After Workers Finish

After workers finish writing `final.txt`, `review.txt`, and `status.json` in each episode directory, run:

```powershell
.\\COLLECT_RESULTS.ps1
```

If any episode is unfinished or validation fails, dispatch only that episode's `agent_prompt.md` to a worker for focused repair.
""",
    )

    write_utf8(
        run_dir / "RUN_THIS.ps1",
        textwrap.dedent(
            f"""
            $ErrorActionPreference = 'Stop'
            Write-Error "Disabled by design: Python-generated launchers do not start agent CLIs. Read NEXT_STEPS.md. To collect finished files, run .\\COLLECT_RESULTS.ps1."
            exit 2
            """
        ).strip(),
    )
    write_utf8(
        run_dir / "COLLECT_RESULTS.ps1",
        textwrap.dedent(
            f"""
            param(
                [switch]$ExportIndex
            )

            $ErrorActionPreference = 'Stop'
            $cmdArgs = @(
                "{Path(__file__).resolve()}",
                "collect",
                "--run-dir",
                "{run_dir}"
            )
            if ($ExportIndex) {{
                $cmdArgs += "--export-index"
            }}
            python @cmdArgs
            """
        ).strip(),
    )


CLEAN_GROUP_RE = re.compile(
    r"(?m)^\ufeff?\s*===\s*(?:\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*)?"
    r"第(?P<num>[0-9一二三四五六七八九十百千万零〇两]+)组(?!结束)(?P<rest>.*?)$"
)
CUT_ID_RE = re.compile(r"cut_id\s*[:：]\s*(?P<cut_id>[A-Z0-9_-]+)")
CLEAN_LEGACY_SHOT_RE = re.compile(r"(?m)^\s*(?:\*\*)?(?P<group>\d{1,3})-(?P<shot>\d{1,2})(?:\*\*)?(?:\s|\[|$)")
CLEAN_SHOT_TIME_RANGE_RE = re.compile(
    r"(?:时间段[：:]\s*)?(?P<start>\d{1,3}(?:\.\d+)?)\s*[-－—–到至]\s*(?P<end>\d{1,3}(?:\.\d+)?)\s*秒"
)
CLEAN_SHOT_TIME_RANGE_LINE_RE = re.compile(
    r"(?m)^\s*(?:时间段[：:]\s*)?(?P<start>\d{1,3}(?:\.\d+)?)\s*[-－—–到至]\s*(?P<end>\d{1,3}(?:\.\d+)?)\s*秒[：:]?\s*$"
)
CLEAN_SHOT_SECONDS_RE = re.compile(r"(?:\*\*)?本镜估算时长(?:\*\*)?[：:]\s*(?P<seconds>\d{1,3}(?:\.\d+)?)\s*秒")
CLEAN_GROUP_TOTAL_RE = re.compile(r"总时长[：:]\s*(?P<seconds>\d{1,3}(?:\.\d+)?)\s*秒")
CLEAN_GROUP_SHOTS_RE = re.compile(r"镜头数[：:]\s*(?P<shots>\d{1,3})\s*个")
MACHINE_TAG_RE = re.compile(r"(?m)^\ufeff?\s*<<<(?:GROUP|GROUP_END|SHOT|SHOT_END)\b.*?>>>\s*$")
VERTICAL_SEEDANCE_STYLE_LINE = VISUAL_STYLE_CONFIG["live-action"]["style_line"]
VERTICAL_SEEDANCE_NEGATIVE_LINE = VISUAL_STYLE_CONFIG["live-action"]["negative_line"]
GROUP_END_MARKER_RE = re.compile(
    r"(?m)^\s*===\s*第[0-9一二三四五六七八九十百千万零〇两]+组结束\s*===\s*$"
)
VIDEO_NEGATIVE_HINT_RE = re.compile(r"(?m)^\s*(?:视频禁止项|剧情负面约束)[：:]\s*(?P<value>.+?)\s*$")
VIDEO_NEGATIVE_HINT_SPLIT_RE = re.compile(r"[，,、；;]")
DEFAULT_STORYBOARD_QUALITY_POLICY = {
    "storyboard_rule_version": "storyboard-quality-policy-default-v1",
    "video_negative_constraints": {
        "max_items": 5,
        "placeholder_terms": [],
        "generic_terms": [],
        "anchor_labels": ["人物", "道具", "场景"],
        "context_anchor_stop_terms": [],
    },
}
_STORYBOARD_QUALITY_POLICY_CACHE: dict | None = None
REQUIRED_AUDIT_COVERAGE_KEYS = (
    "script_fidelity",
    "dialogue_direction",
    "timing_math",
    "dialogue_pacing",
    "space_locking",
    "format",
    "character_availability",
    "handoff_continuity",
    "filmability",
)
CROSS_EPISODE_COVERAGE_KEY = "cross_episode_continuity"
VERTICAL_V2_AUDIT_COVERAGE_KEYS = (
    "audio_mouth_sync",
    "generation_density",
    "action_atomicity",
    "video_negative_constraints",
    "prompt_pollution",
    "prop_continuity",
    "camera_motion_reasonableness",
    "cross_episode_continuity",
)
SEEDANCE25_AUDIT_COVERAGE_KEYS = ("multimodal_task_scope",)
HORIZONTAL_AUDIT_COVERAGE_KEYS = (
    "horizontal_composition",
    "screen_direction",
    "blocking_continuity",
    "camera_motion",
    "audio_mouth_sync",
    "generation_density",
    "narrative_progression",
    "asset_scope",
    "prop_continuity",
    "physical_continuity",
    "visual_peak",
    "special_effects",
    "genre_style",
    "prompt_pollution",
)
HORIZONTAL_CAMERA_MOTION_VAGUE_PATTERNS = (
    "镜头缓慢移动增强氛围",
    "镜头横移展示空间",
    "镜头推进制造电影感",
    "横移展示空间",
    "展示空间",
    "推进制造电影感",
    "增强电影感",
    "增强氛围",
    "更有动感",
)
HORIZONTAL_CAMERA_MOTION_ACTIVE_PATTERNS = (
    "低角度推近",
    "轻推近",
    "推近",
    "推进",
    "后拉",
    "拉开",
    "横向跟拍",
    "跟拍",
    "平移",
    "横移",
    "摇向",
    "前景掠过",
    "掠过",
    "半环绕",
    "环绕",
    "贴地推进",
    "焦点转移",
    "急停落点",
    "手持",
    "移动",
)
HORIZONTAL_EFFECT_BODY_MARKERS = (
    "冷光",
    "暗金",
    "空气波纹",
    "风压",
    "衣摆",
    "尘浪",
    "碎石",
    "裂纹",
    "裂光",
    "刀光",
    "微光",
    "波纹",
    "烟雾",
    "气流",
    "冲击",
    "震开",
    "火星",
    "高光",
    "边光",
    "特效",
)
HORIZONTAL_EFFECT_TAIL_MARKERS = (
    "动作服务型特效",
    "动作服务型大片特效",
    "特效",
    "冷冽刀光",
    "刀光",
    "气流压迫",
    "碎石悬浮",
    "贴地冲击尘浪",
    "金属裂纹冷光",
)
HORIZONTAL_STYLE_TAIL_CONCRETE_EFFECT_MARKERS = (
    "动作服务型特效",
    "动作服务型大片特效",
    "冷冽刀光",
    "刀光",
    "气流压迫",
    "碎石悬浮",
    "贴地冲击尘浪",
    "金属裂纹冷光",
)
HORIZONTAL_EFFECT_BAD_TERMS = (
    "满屏粒子",
    "巨大法阵",
    "魔法阵",
    "法术光球",
    "技能 UI",
    "技能UI",
    "光束吞没",
    "过曝光束",
    "遮脸光效",
    "特效盖住主体",
    "吞没人物",
)
HORIZONTAL_HERO_WEAK_TERMS = (
    "短促",
    "短亮",
    "极弱",
    "范围很小",
    "低范围",
    "一闪即灭",
    "只贴着",
    "收束成细线",
    "微弱气流",
    "细小冷光",
)
HORIZONTAL_HERO_MATERIAL_TERMS = (
    "透明壳",
    "透明护体",
    "护体壳",
    "护体外壳",
    "外层护体",
    "护层",
    "琉璃",
    "金属裂光",
    "暗金纹路",
    "压缩冲击面",
    "冲击面",
    "折射",
    "裂纹",
    "纹路",
    "光屑",
)
HORIZONTAL_HERO_DIRECTION_TERMS = (
    "从",
    "沿",
    "向",
    "左",
    "右",
    "上",
    "下",
    "前方",
    "后方",
    "凹陷",
    "外推",
    "扩开",
    "压向",
    "半弧",
    "路径",
)
HORIZONTAL_HERO_ENVIRONMENT_TERMS = (
    "火光",
    "火盆",
    "烛火",
    "尘粒",
    "尘浪",
    "尘环",
    "衣袖",
    "地面",
    "青石",
    "桌面",
    "人群",
    "裂纹",
    "伏低",
    "震动",
    "后缩",
)
HORIZONTAL_HERO_RESULT_TERMS = (
    "停住",
    "截停",
    "后退",
    "倒飞",
    "断裂",
    "塌陷",
    "破散",
    "沉默",
    "低头",
    "安心",
    "下坠",
    "裂开",
    "收束",
    "确认",
)
HORIZONTAL_HERO_IMPACT_BURST_TERMS = (
    "爆发帧",
    "冲击帧",
    "爆点",
    "撞击瞬间",
    "破防瞬间",
    "断裂瞬间",
    "亮核",
    "压缩光核",
    "爆开",
    "爆裂",
)
HORIZONTAL_HERO_IMPACT_EXPANSION_TERMS = (
    "扩散路径",
    "向外扩",
    "外扩",
    "扩开",
    "扫开",
    "半弧",
    "穿过",
    "推进",
    "沿",
    "引导线",
)
HORIZONTAL_HERO_IMPACT_AFTERSHOCK_TERMS = (
    "余波",
    "收束",
    "残光",
    "压暗",
    "伏低",
    "回落",
    "主光",
    "体积光",
    "屏幕边缘轻微震颤",
    "画面边缘轻微震颤",
)
HORIZONTAL_HERO_SCENE_SCALE_TERMS = (
    "全场",
    "场景",
    "空间",
    "前景",
    "背景",
    "屏幕边缘",
    "画面边缘",
    "主光",
    "体积光",
    "火盆",
    "烛火",
    "火光",
    "地面",
    "青石",
    "桌面",
    "尘粒",
    "尘浪",
    "尘环",
    "衣袖",
    "人群",
    "众人",
    "半圈",
    "一圈",
)
HORIZONTAL_HERO_CONTACT_RISK_PATTERNS = (
    re.compile(r"掌心贴上[^，。；;\n]{0,16}(?:腕|拳|手|臂|骨)"),
    re.compile(r"手掌贴[^，。；;\n]{0,16}(?:腕|拳|手|臂|骨)"),
    re.compile(r"贴上[^，。；;\n]{0,16}(?:腕骨|拳腕|手腕|前臂)"),
    re.compile(r"(?:抓住|锁住|截住)[^，。；;\n]{0,16}(?:手腕|腕骨|拳腕|前臂)"),
    re.compile(r"真实肢体贴合"),
)
HORIZONTAL_HERO_CONTACT_SAFETY_TERMS = (
    "半寸",
    "隔空",
    "能量间隙",
    "外层护体壳",
    "护体壳",
    "护体外壳",
    "压缩冲击面",
    "相对位置",
    "不真实贴合",
    "防穿模",
)
HORIZONTAL_HERO_GENERIC_VFX_TERMS = (
    "冷白光球",
    "光球",
    "能量球",
    "白烟团",
    "白烟",
    "烟团",
    "电纹贴图",
    "电纹",
    "能量爆开",
    "白光爆开",
    "圆形护盾",
    "完整圆形",
)
HORIZONTAL_NEGATIVE_OVER_SUPPRESS_TERMS = (
    "强光效",
    "大片特效",
    "强能量",
    "强特效",
    "粒子",
    "光效",
    "满屏粒子",
    "过曝光效",
    "遮脸光效",
    "特效盖住主体",
    "魔法阵",
    "廉价仙侠宣传片感",
)
HORIZONTAL_CAMERA_MOTION_STABLE_PATTERNS = (
    "固定机位",
    "固定双人",
    "固定中景",
    "固定过肩",
    "稳定过肩",
    "稳定双人",
    "稳定中景",
    "承载台词",
    "承载口型",
    "固定",
)
HORIZONTAL_SPACE_LOCK_PROCESS_PATTERNS = (
    re.compile(r"(正在|正从|正向)"),
    re.compile(r"(从[^，。；;\n]{0,24}(?:走来|走向|跑来|跑向|冲来|冲向|挤入|爬向|逼近))"),
    re.compile(r"(走来|走向|走到|站到|跑来|跑向|冲来|冲向|冲进|冲入|挤入|爬行|爬向|逼近)"),
    re.compile(r"(进入画面|进入场景|推门进入|从门口进入)"),
    re.compile(r"(拿起|放下|递给|接过|抢过|按下|打开|关上|推开|拉开|转身|回头)"),
)
LOW_QUALITY_TEMPLATE_PATTERNS = (
    "空间先被交代出来",
    "镜头从场景布局转向在场人物",
    "视线关系落在当前冲突中心",
    "人物面部肌肉随局势绷紧",
    "眉头和嘴角随情绪细微变化",
    "现场冲突继续推进",
)
SCENE_ESTABLISHING_RE = re.compile(
    # Alt 1: natural format "0-3秒：\n镜头描述：全景..." (time-before-description)
    r"(?m)^\s*(?P<start2>\d{1,3}(?:\.\d+)?)\s*[-－—–到至]\s*(?P<end2>\d{1,3}(?:\.\d+)?)\s*秒\s*[：:]?\s*\n"
    r"\s*(?:\*\*)?镜头描述(?:\*\*)?[：:][^\n]*(?:空间先被交代出来|场景布局|环境|全景|旧工业环境)"
    r"|"
    # Alt 2: original format (description-then-time)
    r"(?:\*\*)?镜头描述(?:\*\*)?[：:][^\n]*(?:空间先被交代出来|场景布局|环境|全景|旧工业环境)[\s\S]{0,160}?"
    r"(?:(?:时间段[：:]\s*)?(?P<start>\d{1,3}(?:\.\d+)?)\s*[-－—–到至]\s*(?P<end>\d{1,3}(?:\.\d+)?)\s*秒|"
    r"(?:\*\*)?本镜估算时长(?:\*\*)?[：:]\s*(?P<seconds>\d{1,3}(?:\.\d+)?)\s*秒)"
)
DIALOGUE_QUOTE_RE = re.compile(r"[“\"]([^”\"]+)[”\"]")
DIALOGUE_PUNCT_RE = re.compile(r"[，。！？、；：,.!?;:\s“”\"'（）()《》【】\[\]—…]")
EMOTIONAL_DIALOGUE_MARKERS = (
    "喊",
    "怒",
    "吼",
    "质问",
    "反问",
    "哭",
    "哭喊",
    "哽咽",
    "发飙",
    "崩溃",
    "冷笑",
    "讥讽",
    "咬牙",
    "厉声",
    "急切",
    "急促",
    "紧急",
    "反讽",
    "嘲讽",
    "爽点",
)
SLOW_DIALOGUE_MARKERS = (
    "缓慢",
    "停顿",
    "哽咽",
    "一字一顿",
    "虚弱",
    "无力",
    "低声艰难",
    "气若游丝",
    "喘着气",
)
NECESSARY_LONG_ACTION_MARKERS = (
    "走到",
    "跑到",
    "冲到",
    "穿过",
    "翻过",
    "爬到",
    "蹲下",
    "跪下",
    "站起身",
    "坐下",
    "转身离开",
    "推开门",
    "抱起",
    "放下",
    "搬起",
    "拖着",
    "背起",
)
AUTO_MULTISHOT_MARKERS = (
    "连续短句交锋",
    "连续对话节拍",
    "快速短句交锋",
    "短促交锋",
    "快速问答",
    "来回对话",
)
MODEL_META_PROMPT_PATTERNS = (
    "Seedance 可",
    "由 Seedance",
    "Seedance 自动",
    "Seedance自动",
    "自动正反打",
    "自动分镜",
    "人物图",
    "场景图",
    "环境图",
    "资产核对",
    "资产数量说明",
    "上传说明",
)
HORIZONTAL_OUTPUT_FIELD_PATTERNS = (
    "道具/关键视觉资产",
    "组间承接",
    "本镜估算时长",
)
HORIZONTAL_XIANXIA_DEPRECATED_FIELDS = (
    "视觉峰值/特效重点",
    "运镜强化词",
    "Seedance执行提示补充",
    "Seedance 执行提示补充",
    "一句话概述",
)
HORIZONTAL_FIELD_LINE_RE = re.compile(
    r"(?m)^\s*(?:\*\*)?(?:人物|场景|道具/关键视觉资产|视觉峰值/特效重点|组间承接|横屏构图/调度|"
    r"镜头描述|光影设计|本镜估算时长|组尾衔接|画面风格|运镜强化词|Seedance执行提示补充|"
    r"Seedance 执行提示补充|--neg)(?:\*\*)?(?:\s*[：:]|\s+)"
)
HORIZONTAL_VISUAL_PEAK_HERO_FIELDS = ("主视觉镜头", "峰值类型", "主视觉事件", "结果反馈")
HORIZONTAL_MAIN_VISUAL_SHOT_RE = re.compile(r"(?<!\d)(?P<shot>\d{1,3}-\d{1,2})(?!\d)")
REVIEWER_ALLOWED_SEMANTIC_RESULTS = {"pass", "warning", "issue"}
REVIEWER_PROMPT_POLLUTION_MARKERS = LOW_QUALITY_TEMPLATE_PATTERNS + MODEL_META_PROMPT_PATTERNS + (
    "由模型自动",
    "模型会处理",
    "本段用于",
    "规则要求",
    "参考图",
    "人物图",
    "场景图",
    "环境图",
    "资产核对",
    "资产数量说明",
    "上传说明",
    "参考官方模板",
    "参考模板",
    "模板编号",
    "官方模板编号",
    "官方模板标题",
    "@图片",
    "@视频",
    "@音频",
    "首帧参考",
    "尾帧参考",
    "视频延长",
    "轨道补全",
    "一镜到底",
    "MV 卡点",
    "萌宠",
    "变装模板",
)


def strip_machine_tags(content: str) -> str:
    """Remove legacy machine protocol tags from user-facing storyboard text."""
    return re.sub(r"\n{3,}", "\n\n", MACHINE_TAG_RE.sub("", content)).strip()


def normalize_clean_storyboard_numbering(content: str) -> tuple[str, list[str]]:
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content, []

    parts: list[str] = []
    changes: list[str] = []
    cursor = 0
    for index, group_match in enumerate(group_matches, start=1):
        block_start = group_match.start()
        block_end = group_matches[index].start() if index < len(group_matches) else len(content)
        old_raw = group_match.group("num")
        old_number = _group_number(old_raw)
        block = content[block_start:block_end]

        block, heading_count = re.subn(
            r"(?m)^(\s*===\s*(?:\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*)?)第[0-9一二三四五六七八九十百千万零〇两]+组",
            rf"\1第{index}组",
            block,
            count=1,
        )
        block = re.sub(
            r"(?m)^(\s*===\s*)第[0-9一二三四五六七八九十百千万零〇两]+组结束",
            rf"\1第{index}组结束",
            block,
        )

        shot_counter = 0

        def replace_shot(match: re.Match) -> str:
            nonlocal shot_counter
            shot_counter += 1
            return f"{match.group(1)}{index}-{shot_counter}{match.group(3)}"

        block = re.sub(
            r"(?m)^(\s*)\d{1,3}-(\d{1,2})(\s*(?:\[.*\])?\s*)$",
            replace_shot,
            block,
        )

        if heading_count and old_number != index:
            changes.append(f"第{old_number or old_raw}组->{index}组")
        parts.append(content[cursor:block_start])
        parts.append(block)
        cursor = block_end

    parts.append(content[cursor:])
    return "".join(parts), changes


def _group_number(value: str) -> int | None:
    if value.isdigit():
        return int(value)
    return chinese_numeral_to_int(value)


def _parse_seconds(value: str) -> float:
    return float(value)


def _format_seconds(value: float) -> str:
    if abs(value - round(value)) < 1e-6:
        return str(int(round(value)))
    return f"{value:g}"


def _is_half_second(value: float) -> bool:
    return abs(value * 2 - round(value * 2)) < 1e-6


def _matches_time_granularity(value: float, granularity_seconds: float) -> bool:
    if granularity_seconds <= 0:
        raise ValueError("timeline granularity must be positive")
    return abs(value / granularity_seconds - round(value / granularity_seconds)) < 1e-6


def _time_granularity_issue(label: str, granularity_seconds: float) -> str:
    if abs(granularity_seconds - 1) < 1e-6:
        return f"{label} 时间点必须使用整数秒边界。"
    return f"{label} 时间点必须使用 {_format_seconds(granularity_seconds)} 秒粒度。"


def _is_integer_second(value: float) -> bool:
    return abs(value - round(value)) < 1e-6


def _json_seconds(value: float) -> int | float:
    return int(round(value)) if _is_integer_second(value) else round(value, 1)


def _extract_time_range_durations(
    time_matches: list[re.Match],
    *,
    timeline_granularity_seconds: float = 0.5,
) -> tuple[list[float], list[str]]:
    durations: list[float] = []
    issues: list[str] = []
    previous_end: float | None = None

    for index, match in enumerate(time_matches):
        start = _parse_seconds(match.group("start"))
        end = _parse_seconds(match.group("end"))
        duration = end - start
        label = f"{_format_seconds(start)}-{_format_seconds(end)}秒"
        durations.append(duration)
        if (
            not _matches_time_granularity(start, timeline_granularity_seconds)
            or not _matches_time_granularity(end, timeline_granularity_seconds)
        ):
            issues.append(_time_granularity_issue(label, timeline_granularity_seconds))
        if duration <= 0:
            issues.append(f"{label} 时间段结束秒数必须大于开始秒数。")
        if index == 0 and abs(start) > 1e-6:
            issues.append(f"{label} 时间段应从 0 秒开始。")
        if previous_end is not None and abs(start - previous_end) > 1e-6:
            issues.append(
                f"{label} 时间段起点={_format_seconds(start)}秒，"
                f"但上一镜结束={_format_seconds(previous_end)}秒。"
            )
        previous_end = end

    return durations, issues


def _extract_legacy_shot_durations(
    block: str,
    shot_matches: list[re.Match],
    *,
    timeline_granularity_seconds: float = 0.5,
) -> tuple[list[float], list[str]]:
    durations: list[float] = []
    issues: list[str] = []

    for index, shot_match in enumerate(shot_matches):
        shot_label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
        shot_start = shot_match.end()
        shot_end = shot_matches[index + 1].start() if index + 1 < len(shot_matches) else len(block)
        shot_block = block[shot_start:shot_end]

        seconds_match = CLEAN_SHOT_SECONDS_RE.search(shot_block)
        if seconds_match:
            seconds = _parse_seconds(seconds_match.group("seconds"))
            durations.append(seconds)
            if not _matches_time_granularity(seconds, timeline_granularity_seconds):
                if abs(timeline_granularity_seconds - 1) < 1e-6:
                    issues.append(f"{shot_label} 本镜估算时长必须使用整数秒。")
                else:
                    issues.append(
                        f"{shot_label} 本镜估算时长必须使用 "
                        f"{_format_seconds(timeline_granularity_seconds)} 秒粒度。"
                    )
        else:
            issues.append(f"{shot_label} 缺少时间段，例如：0-4秒：。")

    return durations, issues


def _effective_dialogue_chars(text: str) -> int:
    quoted = "".join(DIALOGUE_QUOTE_RE.findall(text))
    return len(DIALOGUE_PUNCT_RE.sub("", quoted))


def _has_any_marker(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def _iter_storyboard_shots(content: str) -> list[tuple[int | None, str, float, str]]:
    shots: list[tuple[int | None, str, float, str]] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches):
        group_number = _group_number(group_match.group("num"))
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        if time_matches:
            for shot_index, time_match in enumerate(time_matches):
                start = _parse_seconds(time_match.group("start"))
                end = _parse_seconds(time_match.group("end"))
                shot_start = time_match.end()
                shot_end = time_matches[shot_index + 1].start() if shot_index + 1 < len(time_matches) else len(block)
                label = f"第{group_number or '?'}组 {_format_seconds(start)}-{_format_seconds(end)}秒"
                shots.append((group_number, label, end - start, block[shot_start:shot_end]))
            continue

        legacy_shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))
        for shot_index, shot_match in enumerate(legacy_shot_matches):
            shot_label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
            shot_start = shot_match.end()
            shot_end = legacy_shot_matches[shot_index + 1].start() if shot_index + 1 < len(legacy_shot_matches) else len(block)
            shot_block = block[shot_start:shot_end]
            seconds_match = CLEAN_SHOT_SECONDS_RE.search(shot_block)
            if seconds_match:
                shots.append((group_number, shot_label, _parse_seconds(seconds_match.group("seconds")), shot_block))

    return shots


def validate_dialogue_pacing_floor(content: str) -> list[str]:
    issues: list[str] = []
    for _group_number, shot_label, seconds, shot_text in _iter_storyboard_shots(content):
        if seconds <= 0:
            continue

        chars = _effective_dialogue_chars(shot_text)
        if chars == 0:
            continue

        cps = chars / seconds
        if cps > 6.5:
            issues.append(
                f"{shot_label} 台词节奏过快；有效字数 {chars}，镜头 {_format_seconds(seconds)} 秒，"
                f"字秒比 {cps:.1f}，超过 6.5 字/秒硬上限。"
            )

    return issues


def is_horizontal_episode_dir(episode_dir: Path) -> bool:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
        except Exception:
            meta = {}
        aspect = meta.get("storyboard_aspect")
        if isinstance(aspect, str):
            return aspect.strip().lower() == "horizontal"

    task_path = episode_dir / "TASK.md"
    if task_path.is_file():
        task_text = task_path.read_text(encoding="utf-8", errors="replace")
        return "Aspect: `horizontal`" in task_text or "storyboard_aspect=horizontal" in task_text

    return False


def _horizontal_field_value(block: str, label: str) -> str | None:
    if label == "--neg":
        pattern = re.compile(r"(?m)^\s*(?:\*\*)?--neg(?:\*\*)?(?:\s*[：:])?\s*(?P<value>.*?)\s*$")
    else:
        pattern = re.compile(rf"(?m)^\s*(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[：:]\s*(?P<value>.*?)\s*$")
    match = pattern.search(block)
    return match.group("value").strip() if match else None


def _horizontal_field_block(block: str, label: str) -> str | None:
    if label == "--neg":
        pattern = re.compile(r"(?m)^\s*(?:\*\*)?--neg(?:\*\*)?(?:\s*[：:])?\s*(?P<value>.*?)\s*$")
    else:
        pattern = re.compile(rf"(?m)^\s*(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[：:]\s*(?P<value>.*?)\s*$")
    match = pattern.search(block)
    if not match:
        return None

    following = block[match.end() :]
    next_field = HORIZONTAL_FIELD_LINE_RE.search(following)
    end = match.end() + next_field.start() if next_field else len(block)
    return block[match.start() : end].strip()


def _horizontal_shot_block_has_field(shot_block: str, label: str) -> bool:
    return re.search(rf"(?m)^\s*(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*[：:]", shot_block) is not None


def _collect_horizontal_handoff_process_markers(text: str) -> list[str]:
    matches: list[str] = []
    for pattern in HORIZONTAL_SPACE_LOCK_PROCESS_PATTERNS:
        for hit in pattern.findall(text):
            value = hit if isinstance(hit, str) else "".join(hit)
            if value and value not in matches:
                matches.append(value)
            if len(matches) >= 3:
                return matches
    return matches


def validate_horizontal_output_structure_contract(
    content: str,
    *,
    timeline_only: bool = False,
) -> list[str]:
    issues: list[str] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    required_fields = (
        "人物",
        "场景",
        "道具/关键视觉资产",
        "组间承接",
        "横屏构图/调度",
        "组尾衔接",
        "画面风格",
        "--neg",
    )
    if not timeline_only:
        required_fields = required_fields[:-1] + (
            "视觉峰值/特效重点",
            "运镜强化词",
            "Seedance执行提示补充",
            "--neg",
        )

    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        if timeline_only:
            for deprecated in HORIZONTAL_XIANXIA_DEPRECATED_FIELDS:
                if re.search(
                    rf"(?m)^\s*(?:\*\*)?{re.escape(deprecated)}(?:\*\*)?\s*[：:]",
                    block,
                ):
                    issues.append(
                        f"第{group_number}组仍包含已废弃字段 `{deprecated}`；"
                        "请把其中真正的动作、特效、运镜、声音或约束移入连续时间轴，删除独立说明字段。"
                    )

        for field in required_fields:
            value = _horizontal_field_value(block, field)
            if value is None:
                issues.append(f"第{group_number}组缺少横屏新结构字段 `{field}`。")
            elif not value:
                issues.append(f"第{group_number}组横屏新结构字段 `{field}` 为空。")

        if timeline_only:
            negative_value = (_horizontal_field_value(block, "--neg") or "").strip()
            if negative_value and negative_value not in {"无", "无。"}:
                negative_items = [
                    item.strip().strip("。")
                    for item in re.split(r"[，,、；;]", negative_value)
                    if item.strip().strip("。")
                ]
                if len(negative_items) > 5:
                    issues.append(
                        f"第{group_number}组 `--neg` 包含 {len(negative_items)} 项，超过 5 项；"
                        "只保留本组最具体的失败风险，避免负面词压制目标特效。"
                    )

        if re.search(r"(?m)^\s*(?:\*\*)?组首空间锁定", block):
            issues.append(f"第{group_number}组仍使用旧字段 `组首空间锁定`；横屏新结构应改用 `组间承接`。")
        if re.search(r"(?m)^\s*(?:\*\*)?运镜设计(?:\*\*)?\s*[：:]", block):
            if timeline_only:
                issues.append(
                    f"第{group_number}组仍使用旧字段 `运镜设计`；"
                    "删除该独立字段；若剧情或连续性确实需要锁定镜头行为，再把最少必要约束写入对应镜头描述。"
                )
            else:
                issues.append(f"第{group_number}组仍使用旧字段 `运镜设计`；横屏新结构应使用组级 `运镜强化词`。")
        if _horizontal_field_value(block, "道具") is not None and _horizontal_field_value(block, "道具/关键视觉资产") is None:
            issues.append(f"第{group_number}组仍使用旧字段 `道具`；横屏新结构应写 `道具/关键视觉资产`。")

        people = _horizontal_field_value(block, "人物") or ""
        scene = _horizontal_field_value(block, "场景") or ""
        props = _horizontal_field_value(block, "道具/关键视觉资产") or ""
        asset_count = len(_split_list_field(people)) + (1 if scene and scene not in {"无", "无明确"} else 0) + len(_split_list_field(props))
        if asset_count > 9:
            issues.append(f"第{group_number}组人物、场景、道具/关键视觉资产合计约 {asset_count} 项，超过横屏资产上限 9 项。")

        handoff = _horizontal_field_value(block, "组间承接") or ""
        if handoff in {"延续上一组", "承接上一组", "同上"}:
            issues.append(f"第{group_number}组 `组间承接` 过于空泛；需写清人物视线、方向、关键道具或轴线。")
        process_markers = _collect_horizontal_handoff_process_markers(handoff)
        if process_markers:
            issues.append(
                f"第{group_number}组 `组间承接` 包含过程动作 `{ ' / '.join(process_markers) }`；"
                "承接应优先写静态结果状态，动作推进放入后续 `镜头描述`。"
            )

        if re.search(r"(?m)^\s*(?:\*\*)?镜头号(?:\*\*)?\s*[：:]", block):
            issues.append(
                f"第{group_number}组使用了 `镜头号：` 字段；横屏镜头号必须单独占一行，"
                f"例如 `{group_number}-1`。"
            )

        shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))
        if not shot_matches:
            issues.append(f"第{group_number}组缺少横屏镜头号，例如 `{group_number}-1`。")
            continue

        for shot_index, shot_match in enumerate(shot_matches):
            shot_label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
            shot_start = shot_match.end()
            shot_end = shot_matches[shot_index + 1].start() if shot_index + 1 < len(shot_matches) else len(block)
            shot_block = block[shot_start:shot_end]
            for field in ("镜头描述", "光影设计", "本镜估算时长"):
                if not _horizontal_shot_block_has_field(shot_block, field):
                    issues.append(f"第{group_number}组 {shot_label} 缺少横屏镜头字段 `{field}`。")

    return issues


def _horizontal_negative_over_suppression_hits(neg_text: str) -> list[str]:
    hits: list[str] = []
    for raw_item in re.split(r"[，,、；;]", neg_text):
        item = raw_item.strip().strip("`")
        if not item:
            continue
        normalized = re.sub(r"\s+", "", item)
        if normalized in HORIZONTAL_NEGATIVE_OVER_SUPPRESS_TERMS and item not in hits:
            hits.append(item)
    return hits


def validate_horizontal_visual_style_contract(content: str, *, visual_style: str) -> list[str]:
    issues: list[str] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if visual_style != "3d-cg":
        return issues

    live_action_markers = ("真人实拍", "真实摄影", "真实演员", "纪录片摄影")
    required_style_markers = ("3D CG", "动漫3D", "二次元", "风格化面部", "清晰轮廓线", "高质量卡通渲染", "PBR")
    forbidden_neg_markers = ("3D渲染", "CG感", "动画感", "卡通", "二次元", "动漫")

    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        style_text = _horizontal_field_value(block, "画面风格") or ""
        neg_text = _horizontal_field_value(block, "--neg") or ""
        live_hits = [marker for marker in live_action_markers if marker in style_text]
        if live_hits:
            issues.append(
                f"第{group_number}组是 3D CG 横屏 run，但 `画面风格` 包含真人媒介词 `{ ' / '.join(live_hits) }`。"
            )
        if not any(marker in style_text for marker in required_style_markers):
            issues.append(
                f"第{group_number}组是 3D CG 横屏 run，但 `画面风格` 缺少动漫3D CG/二次元角色/清晰轮廓线/高质量卡通渲染/PBR 等媒介锚点。"
            )
        fixed_tail_hits = [marker for marker in HORIZONTAL_STYLE_TAIL_CONCRETE_EFFECT_MARKERS if marker in style_text]
        if fixed_tail_hits:
            issues.append(
                f"fixed_style_effect_tail: 第{group_number}组 `画面风格` 固定尾部包含具体特效词 "
                f"`{ ' / '.join(fixed_tail_hits[:5]) }`；具体特效应进入实际发生的镜头时间轴，"
                "并在需要时写清镜头运动和声音，不要只藏在固定画风尾部。"
            )
        neg_hits = [marker for marker in forbidden_neg_markers if marker in neg_text]
        if neg_hits:
            issues.append(
                f"第{group_number}组是 3D CG 横屏 run，但 `--neg` 否定目标媒介 `{ ' / '.join(neg_hits) }`。"
            )
        over_suppress_hits = _horizontal_negative_over_suppression_hits(neg_text)
        if over_suppress_hits:
            issues.append(
                f"negative_prompt_over_suppresses_vfx: 第{group_number}组 3D CG `--neg` 使用 "
                f"`{ ' / '.join(over_suppress_hits[:6]) }` 等泛泛强特效负面词，可能压制目标仙侠表现；"
                "应只禁错误形态，例如无来源满屏粒子、过曝吞没人物面部、遮挡口型的强光、"
                "特效盖住主体动作路径、魔法阵贴图或廉价页游特效。"
            )

    return issues


def _horizontal_shot_effect_body_text(shot_text: str) -> str:
    lines: list[str] = []
    for label in ("镜头描述", "光影设计"):
        value = _horizontal_field_value(shot_text, label)
        if value:
            lines.append(value)
    return "\n".join(lines)


def _positive_term_hits(text: str, terms: tuple[str, ...]) -> list[str]:
    hits: list[str] = []
    negation_pattern = re.compile(r"(不|不要|不得|不能|禁止|避免|无|不出现|不形成|不生成|不做)")
    for term in terms:
        start = 0
        while True:
            index = text.find(term, start)
            if index == -1:
                break
            prefix = text[max(0, index - 32) : index].strip()
            clause_prefix = re.split(r"[，,；;。.\n]", prefix)[-1]
            if not negation_pattern.search(clause_prefix):
                hits.append(term)
                break
            start = index + len(term)
    return hits


def _positive_bad_effect_hits(text: str) -> list[str]:
    return _positive_term_hits(text, HORIZONTAL_EFFECT_BAD_TERMS)


def _horizontal_shot_blocks_by_label(block: str) -> dict[str, str]:
    shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))
    shot_blocks: dict[str, str] = {}
    for index, shot_match in enumerate(shot_matches):
        label = f"{shot_match.group('group')}-{shot_match.group('shot')}"
        start = shot_match.start()
        end = shot_matches[index + 1].start() if index + 1 < len(shot_matches) else len(block)
        shot_blocks[label] = block[start:end]
    return shot_blocks


def _horizontal_visual_peak_field_value(visual_peak_block: str, field: str) -> str | None:
    pattern = re.compile(rf"(?m)^\s*[-*]?\s*{re.escape(field)}\s*[：:]\s*(?P<value>.*?)\s*$")
    match = pattern.search(visual_peak_block)
    return match.group("value").strip() if match else None


def _visual_peak_layer_count(text: str) -> int:
    layers = (
        HORIZONTAL_HERO_MATERIAL_TERMS,
        HORIZONTAL_HERO_DIRECTION_TERMS,
        HORIZONTAL_HERO_ENVIRONMENT_TERMS,
        HORIZONTAL_HERO_RESULT_TERMS,
    )
    return sum(1 for terms in layers if any(term in text for term in terms))


def _visual_peak_impact_curve_count(text: str) -> int:
    curve_layers = (
        HORIZONTAL_HERO_IMPACT_BURST_TERMS,
        HORIZONTAL_HERO_IMPACT_EXPANSION_TERMS,
        HORIZONTAL_HERO_IMPACT_AFTERSHOCK_TERMS,
    )
    return sum(1 for terms in curve_layers if any(term in text for term in terms))


def _visual_peak_scene_scale_count(text: str) -> int:
    return sum(1 for term in HORIZONTAL_HERO_SCENE_SCALE_TERMS if term in text)


def validate_visual_peak_contract(content: str, *, visual_style: str = "live-action") -> list[str]:
    issues: list[str] = []
    if visual_style != "3d-cg":
        return issues

    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        visual_peak = (_horizontal_field_value(block, "视觉峰值/特效重点") or "").strip()
        if not re.match(r"(?i)^\s*hero\s*[：:：，,、\s-]?", visual_peak):
            continue

        visual_peak_block = _horizontal_field_block(block, "视觉峰值/特效重点") or ""
        field_values: dict[str, str] = {}
        for field in HORIZONTAL_VISUAL_PEAK_HERO_FIELDS:
            value = _horizontal_visual_peak_field_value(visual_peak_block, field)
            if not value:
                issues.append(
                    f"visual_peak_hero_missing_field: 第{group_number}组声明为 `hero`，但 `视觉峰值/特效重点` "
                    f"缺少 `{field}`；没有主视觉镜头或结果反馈时应降为 `beat` 或重写 hero。"
                )
                continue
            field_values[field] = value

        main_shot_value = field_values.get("主视觉镜头")
        if not main_shot_value:
            continue

        referenced_shots = [match.group("shot") for match in HORIZONTAL_MAIN_VISUAL_SHOT_RE.finditer(main_shot_value)]
        if not referenced_shots:
            issues.append(
                f"visual_peak_hero_missing_main_shot: 第{group_number}组声明为 `hero`，"
                "`主视觉镜头` 必须写实际镜头号，例如 `N-2`。"
            )
            continue

        available_shots = {f"{match.group('group')}-{match.group('shot')}" for match in CLEAN_LEGACY_SHOT_RE.finditer(block)}
        for shot_label in referenced_shots:
            if shot_label not in available_shots:
                issues.append(
                    f"visual_peak_hero_bad_main_shot: 第{group_number}组声明为 `hero`，但 `主视觉镜头` 引用了 "
                    f"`{shot_label}`；可用镜头号为 `{ ' / '.join(sorted(available_shots)) or '无' }`。"
                )

        shot_blocks = _horizontal_shot_blocks_by_label(block)
        main_visual_text = "\n".join(
            [
                visual_peak_block,
                *(shot_blocks.get(shot_label, "") for shot_label in referenced_shots),
                _horizontal_field_value(block, "运镜强化词") or "",
                _horizontal_field_value(block, "Seedance执行提示补充") or "",
            ]
        )
        layer_count = _visual_peak_layer_count(main_visual_text)
        impact_curve_count = _visual_peak_impact_curve_count(main_visual_text)
        scene_scale_count = _visual_peak_scene_scale_count(main_visual_text)

        weak_hits = [term for term in HORIZONTAL_HERO_WEAK_TERMS if term in main_visual_text]
        if weak_hits and layer_count < 3:
            issues.append(
                f"visual_peak_too_small: 第{group_number}组声明为 `hero`，但主视觉镜头主要依赖 "
                f"`{ ' / '.join(weak_hits[:5]) }` 等降强度描述，且缺少明确材质、方向、环境反馈和结果收束；"
                "应降为 `beat`，或补主视觉材质、受力方向、环境反馈和结果收束。"
            )

        if impact_curve_count < 2:
            issues.append(
                f"hero_no_impact_curve: 第{group_number}组声明为 `hero`，但主视觉缺少爆发帧、扩散路径、"
                "余波收束中的大多数阶段；应写清触发前压迫、爆发帧/冲击帧、特效扩散路径、场景级反馈和余波收束。"
            )

        if scene_scale_count < 1:
            issues.append(
                f"vfx_scale_too_local: 第{group_number}组声明为 `hero`，但主视觉停留在局部光点或局部材质反应，"
                "没有触达全场主光、屏幕/画面边缘、火盆/烛火、地面/桌面、尘粒/衣袖或人群反应等场景级反馈。"
            )

        contact_risk = any(pattern.search(main_visual_text) for pattern in HORIZONTAL_HERO_CONTACT_RISK_PATTERNS)
        contact_safe = any(term in main_visual_text for term in HORIZONTAL_HERO_CONTACT_SAFETY_TERMS)
        if contact_risk and not contact_safe:
            issues.append(
                f"contact_staging_risk: 第{group_number}组 `hero` 主视觉涉及近身真实贴合，但没有写清半寸能量间隙、"
                "外层护体壳受力或防穿模约束；应把特效放在可见间隙、护盾外壳、道具表面或地面反馈上。"
            )

        generic_hits = _positive_term_hits(main_visual_text, HORIZONTAL_HERO_GENERIC_VFX_TERMS)
        if generic_hits and layer_count < 4:
            issues.append(
                f"generic_vfx_form: 第{group_number}组 `hero` 主视觉可能退化为普通能量球/白烟/电纹 `{ ' / '.join(generic_hits[:5]) }`，"
                "但缺少受力方向、附着对象、材质和环境反馈；应写成压缩冲击面、护体壳裂纹、道具表面纹路或地面/火光反馈。"
            )

    return issues


def _effect_required_from_visual_peak(block: str) -> tuple[str, str]:
    visual_peak = (_horizontal_field_value(block, "视觉峰值/特效重点") or "").strip()
    match = re.match(r"(?i)^\s*(hero|beat|atmosphere)\s*[：:：，,、\s-]?", visual_peak)
    if not match:
        return "无", "none"
    peak_level = match.group(1).lower()
    if peak_level == "hero":
        return "hero", "strong"
    if peak_level == "beat":
        return "beat", "subtle"
    return "atmosphere", "none"


def validate_effect_placement(
    content: str,
    *,
    visual_style: str = "live-action",
    effect_required: str = "none",
    timeline_only: bool = False,
) -> list[str]:
    issues: list[str] = []
    if visual_style != "3d-cg":
        return issues
    if effect_required not in {"none", "subtle", "strong", "auto"}:
        issues.append(f"effect_required must be one of none/subtle/strong/auto, got `{effect_required}`.")
        return issues

    if not timeline_only:
        issues.extend(validate_visual_peak_contract(content, visual_style=visual_style))

    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        shots = [
            _horizontal_shot_effect_body_text(shot_text)
            for current_group, _shot_label, _seconds, shot_text in _iter_storyboard_shots(content)
            if current_group == _group_number(raw_group)
        ]
        body_text = "\n".join(
            [
                *shots,
                _horizontal_field_value(block, "运镜强化词") or "",
                _horizontal_field_value(block, "Seedance执行提示补充") or "",
            ]
        )
        bad_hits = _positive_bad_effect_hits(body_text)
        if bad_hits:
            issues.append(
                f"effect_overdone: 第{group_number}组正文特效过度或遮挡主体 `{ ' / '.join(bad_hits) }`；"
                "3D CG 特效必须服务动作、受力或道具状态，不能吞没人物、遮脸或变成游戏技能 UI。"
            )

        if timeline_only:
            # The timeline-only profile has no group-level effect declaration;
            # effects are judged from the actual shot prose and reviewer
            # semantics, never from a duplicated strength label.
            group_effect_required = "none"
            visual_peak_level = "timeline"
        else:
            visual_peak_level, group_effect_required = (
                _effect_required_from_visual_peak(block) if effect_required == "auto" else (effect_required, effect_required)
            )
        if group_effect_required == "none":
            continue

        body_hits = [term for term in HORIZONTAL_EFFECT_BODY_MARKERS if term in body_text]
        if not body_hits:
            style_text = _horizontal_field_value(block, "画面风格") or ""
            style_hits = [term for term in HORIZONTAL_EFFECT_TAIL_MARKERS if term in style_text]
            severity = "hard" if group_effect_required == "strong" else "warning"
            if style_hits:
                issues.append(
                    f"effect_only_in_tail: 第{group_number}组已声明为 `{visual_peak_level}`，映射为 `{group_effect_required}` 特效需求，"
                    f"但特效只出现在固定 `画面风格` 尾部 `{ ' / '.join(style_hits[:4]) }`，没有进入镜头正文、光影、运镜或 Seedance 执行提示；severity={severity}。"
                )
                continue
            issues.append(
                f"effect_missing_body: 第{group_number}组已声明为 `{visual_peak_level}`，映射为 `{group_effect_required}` 特效需求，"
                f"但镜头正文、光影、运镜和 Seedance 执行提示都没有承载可见特效；severity={severity}。"
            )

    return issues


def validate_horizontal_camera_motion_contract(
    content: str,
    *,
    visual_style: str = "live-action",
    timeline_only: bool = False,
) -> list[str]:
    # The dedicated Seedance 2.5 xianxia profile intentionally leaves camera
    # choice to the model.  The storyboard still has to describe the subject,
    # action, spatial relationship, and timing clearly, but it must not be
    # rejected merely because a worker did not prescribe a camera move (or did
    # not spell out a subject/path/landing triplet).  Deprecated standalone
    # camera fields are handled by validate_horizontal_output_structure_contract.
    if timeline_only:
        return []

    issues: list[str] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        motion_text = "" if timeline_only else (_horizontal_field_value(block, "运镜强化词") or "")
        if not timeline_only:
            if _horizontal_field_value(block, "运镜强化词") is None:
                issues.append(f"第{group_number}组缺少横屏必填字段 `运镜强化词`。")
                continue
            if not motion_text:
                issues.append(f"第{group_number}组 `运镜强化词` 为空；需概括本组镜头运动策略和服务目的。")
                continue
            if any(pattern in motion_text for pattern in HORIZONTAL_CAMERA_MOTION_VAGUE_PATTERNS):
                issues.append(
                    f"第{group_number}组 `运镜强化词` 过于空泛：`{motion_text}`；"
                    "需写清视线带入、动作驱动、前景遮挡、推近对象、摇向终点或急停落点。"
                )

        shots = [
            (shot_label, seconds, shot_text)
            for current_group, shot_label, seconds, shot_text in _iter_storyboard_shots(content)
            if current_group == _group_number(raw_group)
        ]

        # The legacy generic horizontal 3D-CG workflow retains its older
        # group-level motion requirement.  Keep this branch separate so the
        # timeline-only profile cannot accidentally inherit it.
        if len(shots) < 3:
            continue

        active_count = sum(
            any(pattern in shot_text for pattern in HORIZONTAL_CAMERA_MOTION_ACTIVE_PATTERNS)
            for _shot_label, _seconds, shot_text in shots
        )
        active_motion_text = "\n".join([motion_text, *(shot_text for _shot_label, _seconds, shot_text in shots)])
        if (
            visual_style == "3d-cg"
            and not any(pattern in active_motion_text for pattern in HORIZONTAL_CAMERA_MOTION_ACTIVE_PATTERNS)
        ):
            issues.append(
                f"第{group_number}组是 3D CG 横屏，但缺少可见运镜；"
                "至少安排 1 个有明确路径或落点的横向跟拍、前景掠过、半环绕、贴地推进、低角度推近、焦点转移或急停落点，"
                "避免整组只用固定机位或稳定中景。"
            )

        stable_count = sum(
            any(pattern in shot_text or pattern in motion_text for pattern in HORIZONTAL_CAMERA_MOTION_STABLE_PATTERNS)
            for _shot_label, _seconds, shot_text in shots
        )
        has_dialogue = any(DIALOGUE_QUOTE_RE.search(shot_text) for _shot_label, _seconds, shot_text in shots)
        if has_dialogue and active_count >= 3 and stable_count == 0:
            examples = "；".join(shot_label for shot_label, _seconds, _shot_text in shots[:3])
            issues.append(
                f"第{group_number}组有 {len(shots)} 个镜头，其中 {active_count} 个呈现明显运动且没有稳定镜头；"
                f"对白组需要至少一个固定中景、稳定过肩或可承载口型的近中景。示例镜头：{examples}"
            )

        first_shot_label, first_seconds, first_shot_text = shots[0]
        if (
            first_seconds >= 3
            and re.search(r"(全景|环境|空镜|建立|村口|河床|道路|院子|大厅|广场)", first_shot_text)
            and not any(pattern in first_shot_text or pattern in motion_text for pattern in HORIZONTAL_CAMERA_MOTION_ACTIVE_PATTERNS)
        ):
            issues.append(
                f"第{group_number}组 {first_shot_label} 是 {_format_seconds(first_seconds)} 秒横屏建立镜头，"
                "但缺少高位掠过、横向平移、摇向、轻推或人物动作驱动等信息动机，容易变成静止空镜。"
            )

    return issues


def load_storyboard_quality_policy() -> dict:
    global _STORYBOARD_QUALITY_POLICY_CACHE
    if _STORYBOARD_QUALITY_POLICY_CACHE is not None:
        return _STORYBOARD_QUALITY_POLICY_CACHE

    policy_path = Path(__file__).resolve().parent / STORYBOARD_QUALITY_POLICY_PATH
    if policy_path.is_file():
        policy = read_json(policy_path)
    else:
        policy = DEFAULT_STORYBOARD_QUALITY_POLICY

    if not isinstance(policy.get("video_negative_constraints"), dict):
        policy = DEFAULT_STORYBOARD_QUALITY_POLICY

    _STORYBOARD_QUALITY_POLICY_CACHE = policy
    return policy


def storyboard_quality_policy_version() -> str:
    version = load_storyboard_quality_policy().get("storyboard_rule_version")
    return str(version).strip() if version else "unknown"


def _string_list_from_policy(value: object, fallback: list[str]) -> list[str]:
    if not isinstance(value, list):
        return fallback
    result = [str(item).strip() for item in value if str(item).strip()]
    return result if result else fallback


def _video_negative_policy() -> dict:
    policy = load_storyboard_quality_policy().get("video_negative_constraints")
    if isinstance(policy, dict):
        return policy
    return DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]


def _video_negative_max_items() -> int:
    max_items = _video_negative_policy().get("max_items")
    if isinstance(max_items, int) and max_items > 0:
        return max_items
    return int(DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]["max_items"])


def _video_negative_placeholder_terms() -> list[str]:
    fallback = DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]["placeholder_terms"]
    return _string_list_from_policy(_video_negative_policy().get("placeholder_terms"), fallback)


def _video_negative_generic_terms() -> list[str]:
    fallback = DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]["generic_terms"]
    return _string_list_from_policy(_video_negative_policy().get("generic_terms"), fallback)


def _video_negative_context_anchor_stop_terms() -> set[str]:
    fallback = DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]["context_anchor_stop_terms"]
    terms = _string_list_from_policy(_video_negative_policy().get("context_anchor_stop_terms"), fallback)
    return {term for term in terms if len(term) >= 2}


def _add_anchor_term(anchors: set[str], value: object) -> None:
    term = str(value).strip()
    if not term or term in {"无", "无明确"}:
        return
    term = re.sub(r"[（(].*?[）)]", "", term).strip()
    if len(term) >= 2:
        anchors.add(term)
    if "车" in term:
        anchors.add("车辆")


def _scene_anchor_terms(scene: str) -> list[str]:
    terms: list[str] = []
    for part in re.split(r"[，,、/；;\s]+", scene):
        cleaned = re.sub(
            r"^(?:同一[处条个]?|晴天|日间|白天|夜晚|夜间|雪夜|雪天|阴天|雨天|日景|夜景)+",
            "",
            part.strip(),
        )
        cleaned = re.sub(r"^(?:内|外)\s*", "", cleaned).strip()
        if len(cleaned) >= 2:
            terms.append(cleaned)
    return terms


def _video_negative_anchor_labels() -> list[str]:
    return _string_list_from_policy(
        _video_negative_policy().get("anchor_labels"),
        DEFAULT_STORYBOARD_QUALITY_POLICY["video_negative_constraints"]["anchor_labels"],
    )


def _video_negative_anchor_terms(block: str) -> set[str]:
    # Labels come from the policy file rather than a hardcoded tuple. `anchor_labels` used to
    # be dead config: it was declared in storyboard-quality-policy.json but no accessor ever
    # read it, so editing it silently did nothing.
    anchors: set[str] = set()
    for label in _video_negative_anchor_labels():
        values = _extract_bold_meta(block, label)
        if isinstance(values, list):
            for value in values:
                _add_anchor_term(anchors, value)
        elif isinstance(values, str) and values:
            _add_anchor_term(anchors, values)
            for term in _scene_anchor_terms(values):
                _add_anchor_term(anchors, term)
    return anchors


def _video_negative_context_text(block: str) -> str:
    without_hints = VIDEO_NEGATIVE_HINT_RE.sub("", block)
    return re.sub(
        r"(?m)^\s*\*\*(?:人物|场景|道具|道具/关键视觉资产)\*\*\s*[：:]",
        "",
        without_hints,
    )


def _video_negative_item_has_context_anchor(item: str, context: str) -> bool:
    normalized_item = re.sub(r"\s+", "", item)
    stop_terms = _video_negative_context_anchor_stop_terms()
    for length in range(min(8, len(normalized_item)), 1, -1):
        for start in range(0, len(normalized_item) - length + 1):
            token = normalized_item[start:start + length]
            if any(token == term or token in term or term in token for term in stop_terms):
                continue
            if token in context:
                return True
    return False


def _video_negative_item_has_anchor(
    item: str,
    anchors: set[str],
    block: str,
    episode_anchors: set[str],
) -> bool:
    """An item must name something concrete from this group, or a 人物/道具 from the episode.

    AGENTS.md allows anchoring to "本集全文已出现的人物/道具", but the previous implementation
    matched any 2-character fragment of the item against the entire final.txt. With a 2-char
    floor essentially every Chinese phrase found a match somewhere, so the anchor rule had no
    teeth. Episode-wide anchoring now requires an actual 人物/道具/场景 name drawn from some
    group's metadata, which is what the rule was always meant to mean.
    """
    return (
        any(anchor and anchor in item for anchor in anchors)
        or _video_negative_item_has_context_anchor(item, _video_negative_context_text(block))
        or any(anchor and anchor in item for anchor in episode_anchors)
    )


def _validate_video_negative_hint_items(
    *,
    group_number: int,
    hint_items: list[str],
    block: str,
    episode_anchors: set[str],
) -> list[str]:
    issues: list[str] = []
    max_items = _video_negative_max_items()
    if len(hint_items) > max_items:
        issues.append(
            f"第{group_number}组视频禁止项超过{max_items}个，"
            "请只保留本组最关键的具体剧情错误。"
        )

    anchors = _video_negative_anchor_terms(block)
    placeholder_terms = _video_negative_placeholder_terms()
    generic_terms = _video_negative_generic_terms()
    bad_items = [
        item
        for item in hint_items
        if any(term in item for term in placeholder_terms)
        or item in generic_terms
        or (
            any(term in item for term in generic_terms)
            and not _video_negative_item_has_anchor(item, anchors, block, episode_anchors)
        )
    ]
    if bad_items:
        issues.append(
            f"第{group_number}组视频禁止项仍是模板占位或泛泛词：{', '.join(bad_items)}。"
            "请改成本组具体人物、道具和动作。"
        )

    unanchored_items = [
        item
        for item in hint_items
        if not _video_negative_item_has_anchor(item, anchors, block, episode_anchors)
    ]
    if unanchored_items:
        issues.append(
            f"第{group_number}组视频禁止项缺少本组具体人物、道具或场景锚点："
            f"{', '.join(unanchored_items)}。请使用本组人物名、关键道具名或场景名。"
        )
    return issues


def validate_clean_storyboard_format(
    content: str,
    *,
    video_profile: str = DEFAULT_VIDEO_PROFILE,
) -> list[str]:
    issues: list[str] = []
    profile_cfg = video_profile_config(video_profile)
    timeline_granularity = float(profile_cfg["timeline_granularity_seconds"])
    duration_min = float(profile_cfg["duration_min_seconds"])
    duration_max = float(profile_cfg["duration_max_seconds"])
    if MACHINE_TAG_RE.search(content):
        issues.append("最终分镜中仍包含三尖括号机器标签，请删除这些标签。")
    if video_profile in {
        SEEDANCE25_LIVE_VERTICAL_PROFILE,
        SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
    }:
        for task_mode, terms in SEEDANCE25_FORBIDDEN_TASK_MODE_TERMS.items():
            hits = [term for term in terms if term in content]
            if hits:
                issues.append(
                    "Seedance 2.5 profile 唯一支持 `multimodal_generation`；"
                    f"分镜正文命中不支持的任务模式 `{task_mode}`（`{hits[0]}`）。"
                    "图片、视频、音频只能作为实际多模态输入素材，不得切换为其他任务模式。"
                )
        if "4K画质" in content:
            issues.append("Seedance 2.5 分镜母版不得用 `4K画质` 冒充分辨率参数；分辨率由 video_profile.json/API 参数控制。")
        if re.search(r"(?i)\b1080p\b", content):
            issues.append("当前 Seedance 2.5 profile 未启用 1080p；不要把未启用分辨率写进分镜正文。")
        if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
            # The live-action vertical profile keeps its historical worker
            # contract: workers write focused 视频禁止项 and the collector
            # converts them into the final --neg line/tail.
            if VERTICAL_SEEDANCE_NEGATIVE_LINE in content:
                issues.append("Seedance 2.5 分镜母版包含旧版大包 `--neg`；请删除并仅保留本组聚焦 `视频禁止项`。")
            elif re.search(r"(?m)^\s*--neg(?:\s|$)", content):
                issues.append("Seedance 2.5 分镜母版不要直接写 `--neg`；请改成 2-5 个本组聚焦 `视频禁止项`，由收集阶段转换。")
            for tail_line in video_profile_config(video_profile)["collection_tail_lines"]:
                if tail_line in content:
                    issues.append("Seedance 2.5 固定画面/声音尾部由收集阶段追加，worker 的 final.txt 不得预写固定尾部。")
                    break
        else:
            # The horizontal xianxia profile intentionally keeps a compact
            # per-group --neg field in final.txt.  Do not apply the vertical
            # migration warning above; its timeline-only output contract
            # validates the field and caps it at five focused items.
            pass

    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return issues + ["缺少自然分镜组标题，例如：=== [cut_id: EP01-G01] 第1组：...（总时长：XX秒，镜头数：X个） ==="]

    episode_anchors: set[str] = set()
    for _match_index, _group_match in enumerate(group_matches):
        _start = _group_match.end()
        _end = (
            group_matches[_match_index + 1].start()
            if _match_index + 1 < len(group_matches)
            else len(content)
        )
        episode_anchors |= _video_negative_anchor_terms(content[_start:_end])
    expected_group = 1
    for index, group_match in enumerate(group_matches):
        raw_group = group_match.group("num")
        group_number = _group_number(raw_group)
        if group_number is None:
            issues.append(f"第{expected_group}个组标题无法识别组号：{raw_group}")
            group_number = expected_group
        if group_number != expected_group:
            issues.append(f"组号不连续：期望第{expected_group}组，实际为第{group_number}组。")

        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]

        for hint_match in VIDEO_NEGATIVE_HINT_RE.finditer(block):
            hint_text = hint_match.group("value").strip().strip("，,、；;")
            if not hint_text or hint_text == "无":
                continue
            hint_items = [
                item.strip()
                for item in VIDEO_NEGATIVE_HINT_SPLIT_RE.split(hint_text)
                if item.strip()
            ]
            issues.extend(
                _validate_video_negative_hint_items(
                    group_number=group_number,
                    hint_items=hint_items,
                    block=block,
                    episode_anchors=episode_anchors,
                )
            )

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        legacy_shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))

        if time_matches:
            seconds, time_issues = _extract_time_range_durations(
                time_matches,
                timeline_granularity_seconds=timeline_granularity,
            )
            shot_count = len(time_matches)
        else:
            seconds, time_issues = _extract_legacy_shot_durations(
                block,
                legacy_shot_matches,
                timeline_granularity_seconds=timeline_granularity,
            )
            shot_count = len(legacy_shot_matches)
        issues.extend(time_issues)
        if not time_matches and not legacy_shot_matches:
            issues.append(f"第{group_number}组缺少时间段，例如 0-4秒：。")
        if not time_matches:
            for shot_index, shot_match in enumerate(legacy_shot_matches, start=1):
                shot_group = int(shot_match.group("group"))
                shot_number = int(shot_match.group("shot"))
                if shot_group != group_number:
                    issues.append(f"第{group_number}组内出现跨组镜头编号：{shot_group}-{shot_number}。")
                if shot_number != shot_index:
                    issues.append(
                        f"第{group_number}组镜头编号不连续：期望 {group_number}-{shot_index}，实际 {shot_group}-{shot_number}。"
                    )

        if len(seconds) != shot_count:
            issues.append(
                f"第{group_number}组镜头数量与时间段数量不一致：镜头{shot_count}个，时长{len(seconds)}个。"
            )
        total_match = CLEAN_GROUP_TOTAL_RE.search(group_match.group("rest"))
        shots_match = CLEAN_GROUP_SHOTS_RE.search(group_match.group("rest"))
        seconds_sum = sum(seconds)
        if total_match and seconds:
            declared_total = _parse_seconds(total_match.group("seconds"))
            final_end = None
            if time_matches:
                final_end = _parse_seconds(time_matches[-1].group("end"))
            if not _is_integer_second(declared_total):
                issues.append(f"第{group_number}组标题总时长必须是整数秒。")
            if abs(declared_total - seconds_sum) > 1e-6:
                issues.append(
                    f"第{group_number}组标题总时长={_format_seconds(declared_total)}秒，"
                    f"但镜头时长相加={_format_seconds(seconds_sum)}秒。"
                )
            if final_end is not None and abs(final_end - declared_total) > 1e-6:
                issues.append(
                    f"第{group_number}组最后时间段结束于{_format_seconds(final_end)}秒，"
                    f"应等于标题总时长{_format_seconds(declared_total)}秒。"
                )
        if seconds and not (duration_min <= seconds_sum <= duration_max):
            issues.append(
                f"第{group_number}组镜头时长相加={_format_seconds(seconds_sum)}秒，"
                f"不在 `{video_profile}` 支持的{_format_seconds(duration_min)}-"
                f"{_format_seconds(duration_max)}秒范围内。"
            )
        if shots_match:
            declared_shots = int(shots_match.group("shots"))
            if declared_shots != shot_count:
                issues.append(f"第{group_number}组标题镜头数={declared_shots}，实际镜头数={shot_count}。")

        expected_group += 1

    return issues


def _append_vertical_seedance_tail_to_block(
    block: str,
    *,
    visual_style: str = "live-action",
    video_profile: str = DEFAULT_VIDEO_PROFILE,
) -> str:
    negative_hints: list[str] = []

    def remove_negative_hint(match: re.Match[str]) -> str:
        value = match.group("value").strip().strip("，,、；;")
        if value and value != "无":
            negative_hints.append(value)
        return ""

    block = VIDEO_NEGATIVE_HINT_RE.sub(remove_negative_hint, block)
    profile_cfg = video_profile_config(video_profile)
    if profile_cfg["collection_tail_mode"] == "legacy":
        style_cfg = visual_style_config(visual_style)
        tail_lines = [style_cfg["style_line"]]
        base_negative_line = style_cfg["negative_line"]
    else:
        tail_lines = list(profile_cfg["collection_tail_lines"])
        base_negative_line = str(profile_cfg["base_negative_line"] or "")

    additions = [line for line in tail_lines if line not in block]
    if negative_hints:
        negative_items = "，".join(negative_hints)
        negative_line = f"{base_negative_line}，{negative_items}" if base_negative_line else f"--neg {negative_items}"
    else:
        negative_line = base_negative_line
    if negative_line:
        has_negative_line = (
            base_negative_line in block
            if base_negative_line
            else re.search(r"(?m)^\s*--neg(?:\s|$)", block) is not None
        )
        if not has_negative_line:
            additions.append(negative_line)
    if not additions:
        return block

    tail = "\n\n".join(additions) + "\n\n"
    end_match = GROUP_END_MARKER_RE.search(block)
    if end_match:
        return block[: end_match.start()] + tail + block[end_match.start():]
    return block.rstrip() + "\n\n" + tail.rstrip() + "\n"


def append_vertical_seedance_tail_to_groups(
    content: str,
    *,
    visual_style: str = "live-action",
    video_profile: str = DEFAULT_VIDEO_PROFILE,
) -> str:
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    if not group_matches:
        return content

    parts: list[str] = []
    cursor = 0
    for index, group_match in enumerate(group_matches):
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        parts.append(content[cursor:block_start])
        parts.append(
            _append_vertical_seedance_tail_to_block(
                content[block_start:block_end],
                visual_style=visual_style,
                video_profile=video_profile,
            )
        )
        cursor = block_end
    parts.append(content[cursor:])
    return "".join(parts)


def episode_visual_style(episode_dir: Path) -> str:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
        except Exception:
            meta = {}
        value = meta.get("visual_style")
        if isinstance(value, str) and value.strip() in VISUAL_STYLE_CONFIG:
            return value.strip()

    task_path = episode_dir / "TASK.md"
    if task_path.is_file():
        task_text = task_path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"Visual style:\s*`(?P<value>[^`]+)`", task_text)
        if match and match.group("value") in VISUAL_STYLE_CONFIG:
            return match.group("value")

    return "live-action"


def episode_video_profile(episode_dir: Path) -> str:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
        except Exception:
            meta = {}
        value = meta.get("video_profile")
        if isinstance(value, str) and value.strip() in VIDEO_PROFILE_CONFIG:
            return value.strip()

    task_path = episode_dir / "TASK.md"
    if task_path.is_file():
        task_text = task_path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"Video profile:\s*`(?P<value>[^`]+)`", task_text)
        if match and match.group("value") in VIDEO_PROFILE_CONFIG:
            return match.group("value")

    return DEFAULT_VIDEO_PROFILE


def validate_episode_video_profile_contract(episode_dir: Path) -> list[str]:
    """Validate the episode-level machine contract for strict video profiles."""
    video_profile = episode_video_profile(episode_dir)
    if video_profile not in {SEEDANCE25_LIVE_VERTICAL_PROFILE, SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE}:
        return []

    meta_path = episode_dir / "episode.json"
    if not meta_path.is_file():
        return ["Seedance 2.5 episode 缺少 episode.json，无法确认 multimodal_generation 唯一任务合同。"]
    try:
        meta = read_json(meta_path)
    except Exception as exc:
        return [f"Seedance 2.5 episode.json 无法解析：{exc}"]

    profile_cfg = video_profile_config(video_profile)
    expected_scalars = {
        "video_profile_contract_version": profile_cfg["contract_version"],
        "video_task_type": profile_cfg["video_task_type"],
        "requires_multimodal_materials": profile_cfg["requires_multimodal_materials"],
        "minimum_material_inputs": profile_cfg["minimum_material_inputs"],
    }
    if video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
        expected_scalars.update(
            {
                "provider_contract_version": profile_cfg["provider_contract_version"],
                "provider_task_mapping": profile_cfg["provider_task_mapping"],
                "storyboard_aspect": "horizontal",
                "visual_style": "3d-cg",
                "video_aspect_ratio": profile_cfg["aspect_ratio"],
                "video_resolution": profile_cfg["default_resolution"],
                "video_fps": profile_cfg["fps"],
                "generate_audio": profile_cfg["generate_audio"],
            }
        )
    expected_lists = {
        "allowed_multimodal_material_types": list(profile_cfg["allowed_multimodal_material_types"]),
        "forbidden_video_task_modes": list(profile_cfg["forbidden_video_task_modes"]),
    }
    issues: list[str] = []
    for key, expected in expected_scalars.items():
        if meta.get(key) != expected:
            issues.append(f"episode.json `{key}` 必须为 `{expected}`。")
    for key, expected in expected_lists.items():
        if meta.get(key) != expected:
            issues.append(f"episode.json `{key}` 必须与 Seedance 2.5 profile 机器合同一致。")
    if video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
        run_dir = episode_dir.parent.parent
        manifest_path = run_dir / "manifest.json"
        try:
            manifest = read_json(manifest_path) if manifest_path.is_file() else {}
            project_root = Path(manifest.get("project_root") or Path(__file__).resolve().parent)
            preset = visual_style_preset_snapshot(video_profile, meta.get("visual_style_preset"))
            pack = project_pack_snapshot(
                project_root=project_root,
                video_profile=video_profile,
                aspect="horizontal",
                visual_style="3d-cg",
                mode=manifest.get("mode") or "single",
                visual_style_preset=meta.get("visual_style_preset"),
                project_pack_id=meta.get("project_pack_id"),
            )
            derived = {
                "visual_style_preset_version": preset["version"] if preset else None,
                "visual_style_preset_sha256": preset["sha256"] if preset else None,
                "project_pack_version": pack["version"] if pack else None,
                "project_pack_sha256": pack["sha256"] if pack else None,
            }
            for key, expected in derived.items():
                if meta.get(key) != expected:
                    issues.append(f"episode.json `{key}` 与当前 resolved workflow 不一致。")
        except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            issues.append(f"episode.json resolved workflow 无法验证：{exc}")
    return issues


def validate_storyboard_quality_floor(content: str, *, allow_horizontal_output_fields: bool = False) -> list[str]:
    issues: list[str] = []
    for pattern in LOW_QUALITY_TEMPLATE_PATTERNS:
        if pattern in content:
            issues.append(f"最终分镜包含模板化镜头描述：`{pattern}`，请改为贴合剧本现场的具体动作、道具和人物站位。")
    pollution_patterns = MODEL_META_PROMPT_PATTERNS
    if not allow_horizontal_output_fields:
        pollution_patterns = pollution_patterns + HORIZONTAL_OUTPUT_FIELD_PATTERNS
    for pattern in pollution_patterns:
        if pattern in content:
            issues.append(
                f"最终分镜正文包含模型说明词 `{pattern}`，应改成自然画面描述，"
                "不要在 prompt 中指挥视频模型自动分镜。"
            )
    for match in SCENE_ESTABLISHING_RE.finditer(content):
        if match.group("start2") is not None:
            seconds = _parse_seconds(match.group("end2")) - _parse_seconds(match.group("start2"))
        elif match.group("seconds"):
            seconds = _parse_seconds(match.group("seconds"))
        else:
            seconds = _parse_seconds(match.group("end")) - _parse_seconds(match.group("start"))
        if seconds > 3:
            issues.append(
                f"普通空间/环境交代镜头标为{_format_seconds(seconds)}秒；生产规则要求通常2秒，"
                "只有原剧本明确连续动作时才可到3秒。"
            )
    issues.extend(validate_dialogue_pacing_floor(content))
    return issues


def validate_physical_plausibility_floor(content: str) -> list[str]:
    issues: list[str] = []
    lines = content.splitlines()
    leak_or_pour_terms = ("流出", "洒出", "倒出", "外溢", "倾泻", "泼出", "倒掉", "流到")
    safe_container_terms = ("高于水面", "斜立", "竖立", "扶住", "扶稳", "托住", "留在壶底", "留在杯底", "盖子拧紧")
    for index in range(len(lines)):
        window = "\n".join(lines[index : index + 3])
        if not any(term in window for term in ("水壶", "水杯", "杯子", "瓶子", "药瓶", "油桶", "水桶", "碗")):
            continue
        has_risky_orientation = any(
            term in window
            for term in ("平放", "倒置", "倒扣", "壶口朝下", "杯口朝下", "瓶口朝下", "口朝下", "壶口朝向", "杯口朝向", "瓶口朝向")
        )
        has_open_or_entry = any(term in window for term in ("壶口", "杯口", "瓶口", "碗口", "开口", "拧开", "爬进", "进入"))
        has_retained_liquid = any(term in window for term in ("清水", "水仍", "水还", "水留", "水在", "液体", "壶口内有清水", "杯口内有水", "瓶口内有水"))
        if not (has_risky_orientation and has_open_or_entry and has_retained_liquid):
            continue
        if any(term in window for term in leak_or_pour_terms):
            continue
        if any(term in window for term in safe_container_terms):
            continue
        issues.append(
            "物理可行性风险：有液体的容器被写成平放/倒置/开口朝向目标，但同段仍暗示液体留在容器内；"
            "请写清容器竖立或斜立、开口高于液面、有人扶稳，或明确液体正在流出/倒出。"
        )
        break
    return issues


def _required_audit_coverage_keys(
    reviewer_source: str | None = None,
    review_contract_version: int = 1,
) -> tuple[str, ...]:
    if reviewer_source == VIDEO_PROFILE_CONFIG[SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE]["reviewer_name"]:
        return tuple(sorted(HORIZONTAL_REVIEW_COVERAGE_KEYS))
    if reviewer_source == "storyboard-horizontal-reviewer":
        base_keys = tuple(key for key in REQUIRED_AUDIT_COVERAGE_KEYS if key != "space_locking")
        return base_keys + HORIZONTAL_AUDIT_COVERAGE_KEYS
    if is_vertical_v2_reviewer(reviewer_source, review_contract_version):
        keys = REQUIRED_AUDIT_COVERAGE_KEYS + VERTICAL_V2_AUDIT_COVERAGE_KEYS
        if reviewer_source == VIDEO_PROFILE_CONFIG[SEEDANCE25_LIVE_VERTICAL_PROFILE]["reviewer_name"]:
            keys += SEEDANCE25_AUDIT_COVERAGE_KEYS
        return keys
    return REQUIRED_AUDIT_COVERAGE_KEYS


def _episode_has_boundary_context(episode_dir: Path) -> bool:
    return (episode_dir / "boundary_context.md").is_file()


def _episode_review_contract_version(episode_dir: Path) -> int:
    meta_path = episode_dir / "episode.json"
    if not meta_path.is_file():
        return 1
    try:
        value = read_json(meta_path).get("vertical_review_contract_version", 1)
        return int(value or 1)
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return 1


def _read_review_json(
    path: Path,
    *,
    reviewer_source: str | None = None,
    review_contract_version: int = 1,
    require_numeric_evidence: bool = True,
    boundary_present: bool | None = None,
) -> tuple[dict | None, str | None]:
    """Parse and schema-check a reviewer JSON artifact.

    require_numeric_evidence=False drops episode-level mechanical evidence from the required
    keys. Used for segment reviews in a multi-segment episode: the assembled episode review
    already binds to `review_facts.json`, so repeating the same evidence per segment adds no
    verification, only tokens. V2 artifacts keep their legacy detailed arrays. V3 artifacts
    use compact `mechanical_evidence` plus item-label-only `semantic_coverage`. V4 keeps only
    deterministic content binding in `mechanical_evidence`; the reviewer itself authors one
    natural-language `group_reviews` entry for every group.

    boundary_present says whether this episode has a `boundary_context.md`. False requires
    `audit_coverage.cross_episode_continuity` to be `not_applicable`; True keeps the
    `checked` requirement; None leaves the key unconstrained for callers that cannot tell.
    """
    if not path.is_file():
        return None, f"missing review file: {path.name}"

    raw = path.read_text(encoding="utf-8-sig", errors="replace").strip()
    if not raw:
        return None, f"empty review file: {path.name}"

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, f"{path.name} must contain raw storyboard reviewer JSON: {exc}"

    if not isinstance(payload, dict):
        return None, f"{path.name} must contain a JSON object"

    required_types = {
        "pass": bool,
        "summary": str,
        "checked_groups": list,
        "audit_coverage": dict,
        "spot_checks": list,
        "semantic_checks": list,
        "issues": list,
        "warnings": list,
    }
    if is_vertical_v2_reviewer(reviewer_source, review_contract_version):
        required_types.update(
            {
                "issue_instances_total": int,
                "affected_groups": list,
            }
        )
        if require_numeric_evidence and is_vertical_v4_reviewer(
            reviewer_source, review_contract_version
        ):
            required_types["mechanical_evidence"] = dict
            required_types["group_reviews"] = list
        elif require_numeric_evidence and is_vertical_v3_reviewer(
            reviewer_source, review_contract_version
        ):
            required_types["mechanical_evidence"] = dict
            required_types["semantic_coverage"] = dict
        elif require_numeric_evidence:
            required_types.update(
                {
                    "dialogue_checks": list,
                    "handoff_checks": list,
                    "camera_motion_checks": list,
                }
            )
    for key, expected_type in required_types.items():
        if not isinstance(payload.get(key), expected_type):
            return None, f"{path.name} missing reviewer field `{key}` with type {expected_type.__name__}"

    summary = payload["summary"].strip()
    if not summary:
        return None, f"{path.name} reviewer summary is empty"
    placeholder_markers = (
        "占位",
        "placeholder",
        "待脚本校验",
        "客观格式",
        "clean-format",
        "clean format",
    )
    if any(marker.lower() in summary.lower() for marker in placeholder_markers):
        return None, f"{path.name} looks like a placeholder review, not storyboard reviewer output"
    if payload["pass"] is True and payload["issues"]:
        return None, f"{path.name} has pass=true but issues is not empty"
    if payload["pass"] is False and not payload["issues"]:
        return None, f"{path.name} has pass=false but issues is empty"

    checked_groups = payload["checked_groups"]
    if not checked_groups or not all(isinstance(item, str) and item.strip() for item in checked_groups):
        return None, f"{path.name} missing non-empty checked_groups list"

    audit_coverage = payload["audit_coverage"]
    for key in _required_audit_coverage_keys(reviewer_source, review_contract_version):
        if key == CROSS_EPISODE_COVERAGE_KEY and is_vertical_v3_reviewer(
            reviewer_source, review_contract_version
        ):
            # Without `boundary_context.md` the reviewer has no predecessor state to compare
            # against, so demanding "checked" here only forces a claim it cannot substantiate.
            # Scoped to v3+ so already-delivered v2 runs keep validating unchanged.
            # boundary_present None means the caller cannot tell, so accept either value.
            if boundary_present is False:
                if audit_coverage.get(key) != "not_applicable":
                    return None, (
                        f"{path.name} audit_coverage `{key}` must be `not_applicable` "
                        "when this episode has no boundary_context.md"
                    )
                continue
            if boundary_present is None:
                if audit_coverage.get(key) not in {"checked", "not_applicable"}:
                    return None, f"{path.name} audit_coverage missing `{key}`"
                continue
        if audit_coverage.get(key) != "checked":
            return None, f"{path.name} audit_coverage missing `{key}`"

    spot_checks = payload["spot_checks"]
    if len(spot_checks) < 3:
        return None, f"{path.name} must include at least 3 reviewer spot_checks"
    for index, item in enumerate(spot_checks, start=1):
        if not isinstance(item, dict):
            return None, f"{path.name} spot_checks[{index}] must be an object"
        if not item.get("group") or not item.get("type") or not item.get("evidence"):
            return None, f"{path.name} spot_checks[{index}] missing group/type/evidence"

    semantic_checks = payload["semantic_checks"]
    if len(semantic_checks) < 3:
        return None, f"{path.name} must include at least 3 reviewer semantic_checks"
    for index, item in enumerate(semantic_checks, start=1):
        if not isinstance(item, dict):
            return None, f"{path.name} semantic_checks[{index}] must be an object"
        for key in ("group", "type", "result", "evidence", "fix_instruction"):
            if not item.get(key):
                return None, f"{path.name} semantic_checks[{index}] missing {key}"
        if item["result"] not in REVIEWER_ALLOWED_SEMANTIC_RESULTS:
            return None, (
                f"{path.name} semantic_checks[{index}] result must be one of "
                f"{', '.join(sorted(REVIEWER_ALLOWED_SEMANTIC_RESULTS))}"
            )
        if payload["pass"] is True and item["result"] == "issue":
            return None, f"{path.name} has pass=true but semantic_checks[{index}] result=issue"
        semantic_text = "\n".join(
            str(item.get(key, ""))
            for key in ("type", "evidence", "fix_instruction")
        )
        if (
            item.get("result") in {"warning", "issue"}
            and item.get("type") != "prompt_pollution"
            and any(marker in semantic_text for marker in REVIEWER_PROMPT_POLLUTION_MARKERS)
        ):
            return None, (
                f"{path.name} semantic_checks[{index}] describes prompt pollution "
                "but type is not `prompt_pollution`"
            )

    for collection_name in ("issues", "warnings"):
        for index, item in enumerate(payload[collection_name], start=1):
            if not isinstance(item, dict):
                return None, f"{path.name} {collection_name}[{index}] must be an object"
            rule = item.get("rule")
            review_text = "\n".join(
                str(item.get(key, ""))
                for key in ("rule", "problem", "evidence", "fix")
            )
            if any(marker in review_text for marker in REVIEWER_PROMPT_POLLUTION_MARKERS) and rule != "prompt_pollution":
                return None, (
                    f"{path.name} {collection_name}[{index}] describes prompt pollution "
                    "but rule is not `prompt_pollution`"
                )

    if is_vertical_v2_reviewer(reviewer_source, review_contract_version):
        if payload["issue_instances_total"] < len(payload["issues"]):
            return None, f"{path.name} issue_instances_total cannot be smaller than issues length"
        if not all(isinstance(item, str) and item.strip() for item in payload["affected_groups"]):
            return None, f"{path.name} affected_groups must contain non-empty group labels"

        if is_vertical_v3_reviewer(reviewer_source, review_contract_version):
            mechanical_evidence = payload.get("mechanical_evidence")
            if mechanical_evidence is not None:
                final_sha256 = mechanical_evidence.get("final_sha256")
                if not isinstance(final_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", final_sha256):
                    return None, f"{path.name} mechanical_evidence.final_sha256 must be a lowercase SHA-256"
                count_keys = ["group_count"]
                if not is_vertical_v4_reviewer(reviewer_source, review_contract_version):
                    count_keys.extend(
                        ["dialogue_shot_count", "handoff_count", "camera_motion_shot_count"]
                    )
                for key in count_keys:
                    value = mechanical_evidence.get(key)
                    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                        return None, f"{path.name} mechanical_evidence.{key} must be a non-negative integer"
                previous_episode_id = mechanical_evidence.get("previous_episode_id")
                previous_final_sha256 = mechanical_evidence.get("previous_final_sha256")
                if (previous_episode_id is None) != (previous_final_sha256 is None):
                    return None, f"{path.name} mechanical_evidence predecessor binding is incomplete"
                if previous_episode_id is not None and (
                    not isinstance(previous_episode_id, str) or not previous_episode_id.strip()
                ):
                    return None, f"{path.name} mechanical_evidence.previous_episode_id must be non-empty"
                if previous_final_sha256 is not None and (
                    not isinstance(previous_final_sha256, str)
                    or not re.fullmatch(r"[0-9a-f]{64}", previous_final_sha256)
                ):
                    return None, f"{path.name} mechanical_evidence.previous_final_sha256 must be a lowercase SHA-256"
            if is_vertical_v4_reviewer(reviewer_source, review_contract_version):
                if "semantic_coverage" in payload:
                    return None, (
                        f"{path.name} v4 must not use script-generated `semantic_coverage`; "
                        "the reviewer must author `group_reviews`"
                    )
                group_reviews = payload.get("group_reviews")
                if group_reviews is not None:
                    normalized_groups: list[str] = []
                    for index, item in enumerate(group_reviews, start=1):
                        if not isinstance(item, dict):
                            return None, f"{path.name} group_reviews[{index}] must be an object"
                        missing = [key for key in ("group", "result", "evidence") if not str(item.get(key, "")).strip()]
                        if missing:
                            return None, (
                                f"{path.name} group_reviews[{index}] missing " + "/".join(missing)
                            )
                        if item.get("result") not in REVIEWER_ALLOWED_SEMANTIC_RESULTS:
                            return None, f"{path.name} group_reviews[{index}] has invalid result"
                        normalized_groups.append(_normalize_review_label(item.get("group")))
                    if len(normalized_groups) != len(set(normalized_groups)):
                        return None, f"{path.name} group_reviews contains duplicate group labels"
                    if payload["pass"] is True and any(
                        item.get("result") == "issue" for item in group_reviews if isinstance(item, dict)
                    ):
                        return None, f"{path.name} has pass=true but group_reviews contains an issue"
                    if payload["pass"] is False and not any(
                        item.get("result") == "issue" for item in group_reviews if isinstance(item, dict)
                    ):
                        return None, f"{path.name} has pass=false but group_reviews contains no issue"
            else:
                semantic_coverage = payload.get("semantic_coverage")
                if semantic_coverage is not None:
                    for key in (
                        "dialogue_shots_checked",
                        "handoffs_checked",
                        "camera_motion_shots_checked",
                    ):
                        labels = semantic_coverage.get(key)
                        if not isinstance(labels, list) or not all(
                            isinstance(label, str) and label.strip() for label in labels
                        ):
                            return None, f"{path.name} semantic_coverage.{key} must be a list of labels"
                        normalized = [_normalize_review_label(label) for label in labels]
                        if len(normalized) != len(set(normalized)):
                            return None, f"{path.name} semantic_coverage.{key} contains duplicate labels"

        check_contracts = {
            "dialogue_checks": (
                "shot", "chars", "seconds", "chars_per_second", "mouth_duration",
                "speech_type", "result", "evidence",
            ),
            "handoff_checks": (
                "from", "to", "characters", "props", "doors_vehicles",
                "time_light", "result", "evidence",
            ),
            "camera_motion_checks": (
                "shot", "motivation", "subject", "path", "endpoint",
                "action_compatibility", "result",
            ),
        }
        for collection_name, keys in check_contracts.items():
            entries = payload.get(collection_name)
            if entries is None:
                # Optional when require_numeric_evidence is False; still shape-checked below
                # whenever the review actually supplies the array.
                continue
            if not isinstance(entries, list):
                return None, f"{path.name} {collection_name} must be a list"
            for index, item in enumerate(entries, start=1):
                if not isinstance(item, dict):
                    return None, f"{path.name} {collection_name}[{index}] must be an object"
                missing = [key for key in keys if item.get(key) in (None, "")]
                if missing:
                    return None, (
                        f"{path.name} {collection_name}[{index}] missing "
                        + "/".join(missing)
                    )
                if item.get("result") not in REVIEWER_ALLOWED_SEMANTIC_RESULTS:
                    return None, f"{path.name} {collection_name}[{index}] has invalid result"

    return payload, None


def _storyboard_review_passed(payload: dict | None) -> bool:
    return (
        payload is not None
        and payload.get("pass") is True
        and isinstance(payload.get("issues"), list)
        and len(payload["issues"]) == 0
    )


def _storyboard_group_labels(content: str) -> list[str]:
    labels: list[str] = []
    for group_match in CLEAN_GROUP_RE.finditer(content):
        group_number = _group_number(group_match.group("num"))
        if group_number is not None:
            labels.append(f"第{group_number}组")
    return labels


VERTICAL_CAMERA_MOTION_TERM_RE = re.compile(
    r"缓推|推近|推进|缓拉|拉远|跟拍|跟随|横移|平移|环绕|半环绕|甩镜|摇镜|"
    r"上升|下降|升起|降下|手持跟随|贴地移动|贴地推进|绕行跟随"
)
VERTICAL_CAMERA_MOTION_ANCHOR_RE = re.compile(
    r"摄影机|本镜|机位|镜头(?:从|沿|向|跟|缓|轻|横|平|环|推|拉|摇|甩|贴|绕)"
)
VERTICAL_CAMERA_MOTION_DIRECTIONAL_RE = re.compile(
    r"(?:摄影机|本镜|机位|镜头)(?:从|沿|向|朝|往)[^。\n；;，,]{0,24}(?:推|拉|摇|升|降)"
    r"|(?:摄影机|本镜|机位|镜头)(?:缓慢?|轻微?|平稳)?(?:推|拉|摇|升|降)(?:近|远|向|到|起|下|高|低)"
)


def _vertical_camera_motion_shot_labels(content: str) -> list[str]:
    labels: list[str] = []
    for _group_number, shot_label, _seconds, shot_text in _iter_storyboard_shots(content):
        has_named_motion = (
            VERTICAL_CAMERA_MOTION_TERM_RE.search(shot_text)
            and VERTICAL_CAMERA_MOTION_ANCHOR_RE.search(shot_text)
        )
        if has_named_motion or VERTICAL_CAMERA_MOTION_DIRECTIONAL_RE.search(shot_text):
            labels.append(shot_label)
    return labels


def _normalize_review_label(value: object) -> str:
    return re.sub(r"\s+", "", str(value or ""))


def build_vertical_semantic_coverage(
    content: str,
    *,
    require_cross_episode_boundary: bool = False,
) -> dict:
    """Return compact item labels that a v3 reviewer must explicitly cover."""
    groups = _storyboard_group_labels(content)
    dialogue_labels = [
        shot_label
        for _group_number, shot_label, _seconds, shot_text in _iter_storyboard_shots(content)
        if _effective_dialogue_chars(shot_text)
    ]
    handoff_labels = [f"{left}->{right}" for left, right in zip(groups, groups[1:])]
    if require_cross_episode_boundary and groups:
        handoff_labels.insert(0, f"上一集实际末组->{groups[0]}")
    return {
        "dialogue_shots_checked": dialogue_labels,
        "handoffs_checked": handoff_labels,
        "camera_motion_shots_checked": _vertical_camera_motion_shot_labels(content),
    }


def build_vertical_review_facts(
    content: str,
    *,
    review_contract_version: int,
    require_cross_episode_boundary: bool = False,
    previous_episode_id: str | None = None,
    previous_final_content: str | None = None,
) -> dict:
    """Build compact deterministic facts for the semantic reviewer.

    These facts intentionally cover only machine-verifiable scope. They bind a
    review to the exact final text; the reviewer still owns script fidelity,
    spatial continuity, dialogue interpretation, camera judgment and filmability.
    V3 retains legacy semantic-item counts for already-created runs. V4 deliberately
    omits them so regex detection cannot masquerade as semantic review coverage.
    """
    mechanical_evidence = {
        "final_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        "group_count": len(_storyboard_group_labels(content)),
    }
    if review_contract_version < 4:
        coverage = build_vertical_semantic_coverage(
            content,
            require_cross_episode_boundary=require_cross_episode_boundary,
        )
        mechanical_evidence.update(
            {
                "dialogue_shot_count": len(coverage["dialogue_shots_checked"]),
                "handoff_count": len(coverage["handoffs_checked"]),
                "camera_motion_shot_count": len(coverage["camera_motion_shots_checked"]),
            }
        )
    if require_cross_episode_boundary:
        if not previous_episode_id or previous_final_content is None:
            raise ValueError("cross-episode review facts require the actual previous final")
        mechanical_evidence["previous_episode_id"] = previous_episode_id
        mechanical_evidence["previous_final_sha256"] = hashlib.sha256(
            previous_final_content.encode("utf-8")
        ).hexdigest()
    return {
        "schema_version": VERTICAL_REVIEW_FACTS_SCHEMA_VERSION,
        "review_contract_version": review_contract_version,
        "mechanical_evidence": mechanical_evidence,
    }


def load_previous_final_binding(
    episode_dir: Path,
) -> tuple[str | None, str | None, list[str]]:
    """Load the declared predecessor final without allowing paths outside this run."""
    boundary_path = episode_dir / "boundary_context.md"
    if not boundary_path.is_file():
        return None, None, []
    boundary_text = boundary_path.read_text(encoding="utf-8-sig", errors="replace")
    episode_match = re.search(r"(?m)^[ \t]*previous_episode:[ \t]*(?P<episode>.+?)[ \t]*$", boundary_text)
    if not episode_match:
        return None, None, ["boundary_context.md missing `previous_episode` declaration"]
    declared_episode_id = episode_match.group("episode").strip().strip('"\'')
    if not declared_episode_id:
        return None, None, ["boundary_context.md previous_episode must be non-empty"]
    match = re.search(r"(?m)^[ \t]*previous_final:[ \t]*(?P<path>.+?)[ \t]*$", boundary_text)
    if not match:
        return None, None, ["boundary_context.md missing `previous_final` declaration"]
    declared = match.group("path").strip().strip('"\'')
    target = (episode_dir / declared).resolve()
    episodes_root = episode_dir.parent.resolve()
    try:
        target.relative_to(episodes_root)
    except ValueError:
        return None, None, ["boundary_context.md previous_final must stay inside this run's episodes directory"]
    if target.parent.parent != episodes_root:
        return None, None, ["boundary_context.md previous_final must belong to a direct sibling episode directory"]
    if target.parent == episode_dir.resolve():
        return None, None, ["boundary_context.md previous_final cannot point to the current episode"]
    if target.name != "final.txt" or not target.is_file():
        return None, None, [f"boundary previous final is missing: {target}"]
    if target.parent.name != declared_episode_id:
        return None, None, [
            "boundary_context.md previous_episode does not match the declared previous_final directory"
        ]
    meta_path = episode_dir / "episode.json"
    if not meta_path.is_file():
        return None, None, ["cross-episode v3/v4 review requires episode.json dependency metadata"]
    try:
        meta = read_json(meta_path)
    except (OSError, json.JSONDecodeError) as exc:
        return None, None, [f"episode.json dependency metadata is invalid: {exc}"]
    if not isinstance(meta, dict):
        return None, None, ["episode.json dependency metadata must be a JSON object"]
    depends_on_episode = meta.get("depends_on_episode")
    if not isinstance(depends_on_episode, str) or not depends_on_episode.strip():
        return None, None, ["episode.json missing `depends_on_episode` for cross-episode review"]
    if depends_on_episode.strip() != declared_episode_id:
        return None, None, [
            "boundary_context.md previous_episode does not match episode.json depends_on_episode"
        ]
    return target.parent.name, target.read_text(encoding="utf-8", errors="replace"), []


def build_vertical_review_facts_for_episode(
    episode_dir: Path,
    content: str,
    *,
    review_contract_version: int,
) -> tuple[dict | None, list[str]]:
    require_boundary = _episode_has_boundary_context(episode_dir)
    previous_episode_id: str | None = None
    previous_final_content: str | None = None
    if require_boundary:
        previous_episode_id, previous_final_content, issues = load_previous_final_binding(episode_dir)
        if issues:
            return None, issues
    return (
        build_vertical_review_facts(
            content,
            review_contract_version=review_contract_version,
            require_cross_episode_boundary=require_boundary,
            previous_episode_id=previous_episode_id,
            previous_final_content=previous_final_content,
        ),
        [],
    )


def validate_vertical_review_facts_file(
    episode_dir: Path,
    content: str,
    *,
    review_contract_version: int,
    require_cross_episode_boundary: bool = False,
) -> list[str]:
    facts_path = episode_dir / "review_facts.json"
    if not facts_path.is_file():
        return ["missing review facts: run validate-episode --pre-check before reviewer"]
    try:
        actual = read_json(facts_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"review_facts.json is invalid: {exc}"]
    expected, binding_issues = build_vertical_review_facts_for_episode(
        episode_dir,
        content,
        review_contract_version=review_contract_version,
    )
    if binding_issues:
        return binding_issues
    if actual != expected:
        return ["review_facts.json is stale or does not match current final.txt; rerun pre-check"]
    return []


def validate_vertical_review_evidence(
    payload: dict,
    content: str,
    review_name: str,
    *,
    require_cross_episode_boundary: bool = False,
    review_contract_version: int = 2,
    previous_episode_id: str | None = None,
    previous_final_content: str | None = None,
) -> list[str]:
    """Verify that vertical reviewer evidence covers the actual draft, not generic claims."""
    issues: list[str] = []

    if review_contract_version >= 3:
        expected = build_vertical_review_facts(
            content,
            review_contract_version=review_contract_version,
            require_cross_episode_boundary=require_cross_episode_boundary,
            previous_episode_id=previous_episode_id,
            previous_final_content=previous_final_content,
        )["mechanical_evidence"]
        actual = payload.get("mechanical_evidence")
        if actual != expected:
            issues.append(
                f"{review_name} mechanical_evidence does not match current final.txt/review_facts.json"
            )
        if review_contract_version >= 4:
            expected_groups = [_normalize_review_label(label) for label in _storyboard_group_labels(content)]
            actual_groups = [
                _normalize_review_label(item.get("group"))
                for item in payload.get("group_reviews", [])
                if isinstance(item, dict)
            ]
            missing_groups = [label for label in expected_groups if label not in actual_groups]
            unexpected_groups = [label for label in actual_groups if label not in expected_groups]
            if missing_groups:
                issues.append(
                    f"{review_name} group_reviews missing groups: {', '.join(missing_groups[:5])}"
                )
            if unexpected_groups:
                issues.append(
                    f"{review_name} group_reviews references unknown groups: {', '.join(unexpected_groups[:5])}"
                )
            if len(actual_groups) != len(expected_groups):
                issues.append(
                    f"{review_name} group_reviews must contain exactly one model-authored review per group"
                )
        else:
            expected_coverage = build_vertical_semantic_coverage(
                content,
                require_cross_episode_boundary=require_cross_episode_boundary,
            )
            actual_coverage = payload.get("semantic_coverage")
            if actual_coverage != expected_coverage:
                issues.append(
                    f"{review_name} semantic_coverage does not list every dialogue shot, handoff, and camera-motion shot"
                )
        if require_cross_episode_boundary:
            groups = _storyboard_group_labels(content)
            first_group = _normalize_review_label(groups[0]) if groups else ""
            has_boundary_semantic_check = any(
                isinstance(item, dict)
                and item.get("type") == "cross_episode_continuity"
                and _normalize_review_label(item.get("group")) == first_group
                and item.get("result") in {"pass", "warning"}
                and bool(str(item.get("evidence", "")).strip())
                for item in payload.get("semantic_checks", [])
            )
            if not has_boundary_semantic_check:
                issues.append(
                    f"{review_name} missing cross_episode_continuity semantic evidence for {first_group}"
                )
    else:
        expected_dialogue: dict[str, tuple[int, float]] = {}
        for _group_number, shot_label, seconds, shot_text in _iter_storyboard_shots(content):
            chars = _effective_dialogue_chars(shot_text)
            if chars:
                expected_dialogue[_normalize_review_label(shot_label)] = (chars, seconds)
        actual_dialogue: dict[str, dict] = {}
        for item in payload.get("dialogue_checks", []):
            actual_dialogue[_normalize_review_label(item.get("shot"))] = item
        missing_dialogue = sorted(set(expected_dialogue) - set(actual_dialogue))
        if missing_dialogue:
            issues.append(f"{review_name} dialogue_checks missing shots: {', '.join(missing_dialogue[:5])}")
        for label, (expected_chars, expected_seconds) in expected_dialogue.items():
            item = actual_dialogue.get(label)
            if item is None:
                continue
            try:
                chars = int(item.get("chars"))
                seconds = float(item.get("seconds"))
                cps = float(item.get("chars_per_second"))
            except (TypeError, ValueError):
                issues.append(f"{review_name} dialogue_checks `{label}` has non-numeric timing evidence")
                continue
            expected_cps = expected_chars / expected_seconds if expected_seconds else 0.0
            if chars != expected_chars or abs(seconds - expected_seconds) > 0.05 or abs(cps - expected_cps) > 0.15:
                issues.append(
                    f"{review_name} dialogue_checks `{label}` does not match final text "
                    f"({expected_chars} chars/{_format_seconds(expected_seconds)}s/{expected_cps:.1f} cps)"
                )

        groups = _storyboard_group_labels(content)
        expected_handoffs = {
            (_normalize_review_label(left), _normalize_review_label(right))
            for left, right in zip(groups, groups[1:])
        }
        actual_handoffs = {
            (_normalize_review_label(item.get("from")), _normalize_review_label(item.get("to")))
            for item in payload.get("handoff_checks", [])
        }
        missing_handoffs = sorted(expected_handoffs - actual_handoffs)
        if missing_handoffs:
            rendered = ", ".join(f"{left}->{right}" for left, right in missing_handoffs[:5])
            issues.append(f"{review_name} handoff_checks missing transitions: {rendered}")
        if require_cross_episode_boundary:
            first_group = _normalize_review_label(groups[0]) if groups else ""
            has_boundary_check = any(
                right == first_group and ("上一集" in left or re.search(r"ep\d+", left, re.IGNORECASE))
                for left, right in actual_handoffs
            )
            if not has_boundary_check:
                issues.append(f"{review_name} handoff_checks missing previous-episode boundary to {first_group}")

        expected_motion = {_normalize_review_label(label) for label in _vertical_camera_motion_shot_labels(content)}
        actual_motion = {
            _normalize_review_label(item.get("shot"))
            for item in payload.get("camera_motion_checks", [])
        }
        missing_motion = sorted(expected_motion - actual_motion)
        if missing_motion:
            issues.append(f"{review_name} camera_motion_checks missing shots: {', '.join(missing_motion[:5])}")
        unexpected_motion = sorted(actual_motion - expected_motion)
        if unexpected_motion:
            issues.append(f"{review_name} camera_motion_checks references shots without detected motion: {', '.join(unexpected_motion[:5])}")

    issue_groups = {
        _normalize_review_label(item.get("group"))
        for item in payload.get("issues", [])
        if isinstance(item, dict) and item.get("group")
    }
    affected_groups = {_normalize_review_label(item) for item in payload.get("affected_groups", [])}
    missing_affected = sorted(issue_groups - affected_groups)
    if missing_affected:
        issues.append(f"{review_name} affected_groups missing issue groups: {', '.join(missing_affected)}")

    return issues


def _split_list_field(value: str) -> list[str]:
    value = value.strip()
    if not value or value in {"无", "无明确"}:
        return []
    return [
        item.strip()
        for item in re.split(r"[、,，/]+", value)
        if item.strip()
    ]


def _extract_bold_meta(block: str, label: str) -> list[str] | str:
    field_label = label
    if label == "道具":
        field_label = r"(?:道具|道具/关键视觉资产)"
    else:
        field_label = re.escape(label)
    pattern = re.compile(rf"(?m)^\s*\*\*{field_label}\*\*\s*[：:]\s*(?P<value>.+?)\s*$")
    match = pattern.search(block)
    if not match:
        if label == "场景":
            scene_match = re.search(r"(?m)^\s*【场景】\s*(?P<value>.+?)\s*$", block)
            return scene_match.group("value").strip() if scene_match else ""
        if label in {"人物", "道具"}:
            subject_match = re.search(r"(?m)^\s*【主体】\s*(?P<value>.+?)\s*$", block)
            if subject_match:
                subject_value = subject_match.group("value")
                field_name = "人物" if label == "人物" else "关键道具"
                field_match = re.search(rf"{field_name}\s*[：:]\s*(?P<value>.*?)(?:[；;。]|$)", subject_value)
                if field_match:
                    return _split_list_field(field_match.group("value"))
        return [] if label in {"人物", "道具"} else ""
    value = match.group("value").strip()
    if label in {"人物", "道具"}:
        return _split_list_field(value)
    return value


def validate_vertical_space_lock_contract(content: str) -> list[str]:
    """Enforce per-character position and camera-relative orientation in vertical first frames."""
    issues: list[str] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    position_re = re.compile(r"画面(?:左|右|中央|中间)|前景|背景|画幅(?:左|右|中央)")
    orientation_re = re.compile(r"面向镜头|背对镜头|侧对镜头")
    for index, group_match in enumerate(group_matches):
        group_number = _group_number(group_match.group("num")) or index + 1
        block_start = group_match.end()
        block_end = group_matches[index + 1].start() if index + 1 < len(group_matches) else len(content)
        block = content[block_start:block_end]
        characters = _extract_bold_meta(block, "人物")
        if not isinstance(characters, list) or not characters:
            continue
        lock_match = re.search(
            r"(?m)^\s*组首空间锁定[^：:\n]*[：:]\s*(?P<value>.+?)\s*$",
            block,
        )
        if not lock_match:
            continue
        lock_value = lock_match.group("value")
        clauses = [clause.strip() for clause in re.split(r"[；;。]", lock_value) if clause.strip()]
        for character in characters:
            sound_only_re = re.compile(
                rf"{re.escape(character)}[^。\n]{{0,12}}(?:画外音|电话音|广播音|旁白|心声)"
            )
            if sound_only_re.search(block):
                continue
            matching_clauses = [clause for clause in clauses if character in clause]
            if not matching_clauses:
                issues.append(f"第{group_number}组 组首空间锁定缺少人物 `{character}`。")
                continue
            # Prefer the clause where this character is the subject. Taking the first clause
            # that merely mentions the name lets a protective or relative reference in someone
            # else's clause ("左手护着林知意") hijack the lock, so the character's own clause is
            # never examined and every check below runs against the wrong text.
            subject_clauses = [
                candidate
                for candidate in matching_clauses
                if re.match(rf"\s*{re.escape(character)}", candidate)
                or re.search(rf"{re.escape(character)}\s*位于", candidate)
            ]
            clause = subject_clauses[0] if subject_clauses else matching_clauses[0]
            # Two ways a clause stops being a per-character lock:
            #   1. an explicit conjunction (`甲和乙位于画面左侧`)
            #   2. a second character carrying its own `位于` position phrase, which is what
            #      happens when people are separated by `，` instead of `；` -- both names then
            #      match the same clause and inherit one position/orientation pair, so the
            #      per-character checks below pass vacuously.
            # A bare name without `位于` is a relative reference (`乙位于画面右侧、甲前方半步`)
            # and stays legal.
            grouped_people = [
                name
                for name in characters
                if name != character
                and re.search(
                    rf"(?:{re.escape(character)}\s*[、和与及]"
                    rf"|{re.escape(name)}\s*[、和与及]"
                    rf"|{re.escape(name)}\s*位于)",
                    clause,
                )
            ]
            if grouped_people:
                issues.append(
                    f"第{group_number}组 组首空间锁定把 `{character}` 与 "
                    f"`{grouped_people[0]}` 合在同一分句；请逐人锁定，"
                    "每个人物之间用 `；` 分隔（`，` 不算分句分隔）。"
                )
            # A character physically carried by / attached to another present character has no
            # independent frame position: it is fully determined by the carrier, who does
            # carry one ("萧凡位于画面中央...；林知意伏在萧凡背上"). Demanding a separate 画面X
            # for them is unsatisfiable without inventing a contradictory position. Anchors to
            # scenery ("靠在墙上") are not exempt -- those still need their own position.
            other_names = "|".join(
                re.escape(name) for name in characters if name != character
            )
            carrier_pattern = rf"(?:伏|趴|靠|依偎|躺|骑|蜷|缩)在\s*(?:他|她|它|其{'|' + other_names if other_names else ''})"
            attached_to_person = bool(
                re.search(carrier_pattern + r"[^，。；]{0,6}(?:背|怀|身|腿|肩|臂|膝)", clause)
            )
            if not attached_to_person and not position_re.search(clause):
                issues.append(
                    f"第{group_number}组 `{character}` 缺少画面位置；"
                    "只接受 画面左/画面右/画面中央/画面中间/画幅左/画幅右/画幅中央/前景/背景"
                    "（可加“侧”，如 画面左侧）；`左侧`、`屏幕左`、`镜头左侧` 不算。"
                )
            if not orientation_re.search(clause):
                issues.append(
                    f"第{group_number}组 `{character}` 缺少相对镜头朝向；"
                    "面向门口/车头/对方不能替代面向、背对或侧对镜头。"
                )
    return issues


def _extract_group_title(heading_rest: str) -> str:
    rest = re.sub(r"===\s*$", "", heading_rest).strip()
    rest = re.sub(r"^[：:]\s*", "", rest).strip()
    rest = re.split(r"[（(]\s*(?:cut_id|总时长|镜头数)", rest, maxsplit=1)[0].strip()
    rest = re.sub(r"[，,]?\s*\[cut_id\s*[:：]\s*[A-Z0-9_-]+\]\s*", "", rest)
    rest = CUT_ID_RE.sub("", rest)
    rest = re.sub(r"[（(]\s*[，,]\s*$", "", rest).strip()
    return rest or "未命名分镜组"


def _workflow_audit_path(path: Path, project_root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(project_root.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(
            f"workflow audit file is outside project root: file={resolved}; project_root={project_root.resolve()}"
        ) from exc


def _workflow_audit_file(*, role: str, path: Path, project_root: Path) -> dict:
    resolved = path.resolve()
    if not resolved.is_file():
        raise ValueError(f"workflow audit file missing: role={role}; path={resolved}")
    return {
        "role": role,
        "path": _workflow_audit_path(resolved, project_root),
        "sha256": hashlib.sha256(resolved.read_bytes()).hexdigest(),
    }


def build_resolved_workflow_identity(episode_dir: Path) -> dict | None:
    """Resolve the versioned files actually loaded by the strict horizontal xianxia workflow."""
    episode_path = episode_dir / "episode.json"
    if not episode_path.is_file():
        return None
    episode = read_json(episode_path)
    if episode.get("video_profile") != SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE:
        return None

    run_dir = episode_dir.parent.parent
    manifest_path = run_dir / "manifest.json"
    manifest = read_json(manifest_path) if manifest_path.is_file() else {}
    project_root = Path(manifest.get("project_root") or Path(__file__).resolve().parent).resolve()
    profile_cfg = video_profile_config(SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE)
    expected_preset = visual_style_preset_snapshot(
        SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
        episode.get("visual_style_preset"),
    )
    expected_pack = project_pack_snapshot(
        project_root=project_root,
        video_profile=SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
        aspect=episode.get("storyboard_aspect"),
        visual_style=episode.get("visual_style"),
        mode=manifest.get("mode") or "single",
        visual_style_preset=episode.get("visual_style_preset"),
        project_pack_id=episode.get("project_pack_id"),
    )
    profile_path = Path(
        episode.get("seedance_profile_path")
        or manifest.get("seedance_profile_path")
        or project_root / profile_cfg["profile_skill_path"]
    ).resolve()
    profile_dir = profile_path.parent
    workflow_cfg = storyboard_workflow_config("horizontal", SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE)
    generator_path = Path(
        manifest.get("generator_skill_path")
        or project_root / PROJECT_AGENT_SKILLS_DIR / workflow_cfg["generator_dir"] / "SKILL.md"
    ).resolve()
    reviewer_path = Path(
        manifest.get("reviewer_skill_path")
        or project_root / PROJECT_AGENT_SKILLS_DIR / workflow_cfg["reviewer_dir"] / "SKILL.md"
    ).resolve()
    cg_path = Path(
        manifest.get("cg_visual_style_skill_path")
        or project_root / CG_VISUAL_STYLE_SKILL_PATH
    ).resolve()

    audit_specs = [
        ("profile_skill", profile_path),
        ("model_contract", profile_dir / "references" / "model-contract.md"),
        ("visual_preset_reference", profile_dir / "references" / "visual-presets.md"),
        ("xianxia_vfx_grammar", profile_dir / "references" / "xianxia-vfx-grammar.md"),
        ("native_audio_contract", profile_dir / "references" / "native-audio.md"),
        ("segment_handoff_contract", profile_dir / "references" / "segment-handoff.md"),
        ("generator_skill", generator_path),
        ("reviewer_skill", reviewer_path),
        ("3d_cg_visual_style", cg_path),
    ]

    project_pack_path_value = expected_pack["path"] if expected_pack else None
    if project_pack_path_value:
        project_pack_path = Path(project_pack_path_value).resolve()
        project_pack = read_json(project_pack_path)
        audit_specs.extend(
            [
                ("project_pack_registry", project_root / PROJECT_PACK_REGISTRY_PATH),
                ("project_pack_manifest", project_pack_path),
                ("project_pack_skill", (project_root / project_pack["entry_skill"]).resolve()),
            ]
        )
        audit_specs.extend(
            (
                f"project_pack_reference:{Path(reference).name}",
                (project_root / reference).resolve(),
            )
            for reference in project_pack.get("references", [])
        )

    audit_files = [
        _workflow_audit_file(role=role, path=path, project_root=project_root)
        for role, path in audit_specs
    ]
    identity = {
        "identity_schema_version": 1,
        "video_profile": episode.get("video_profile"),
        "video_profile_contract_version": profile_cfg["contract_version"],
        "provider_contract_version": profile_cfg["provider_contract_version"],
        "provider_task_mapping": profile_cfg["provider_task_mapping"],
        "storyboard_aspect": episode.get("storyboard_aspect"),
        "visual_style": episode.get("visual_style"),
        "visual_style_preset": episode.get("visual_style_preset"),
        "visual_style_preset_version": expected_preset["version"] if expected_preset else None,
        "visual_style_preset_sha256": expected_preset["sha256"] if expected_preset else None,
        "project_pack_id": episode.get("project_pack_id"),
        "project_pack_version": expected_pack["version"] if expected_pack else None,
        "project_pack_sha256": expected_pack["sha256"] if expected_pack else None,
        "generator_skill_name": episode.get("generator_skill_name") or workflow_cfg["generator_name"],
        "reviewer_skill_name": episode.get("reviewer_skill_name") or workflow_cfg["reviewer_name"],
        "workflow_audit": {
            "schema_version": 1,
            "files": audit_files,
        },
    }
    canonical = json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    identity["resolved_workflow_hash"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return identity


def build_storyboard_index_payload(
    *,
    content: str,
    episode_dir: Path,
    project: str | None = None,
    source_final_sha256: str | None = None,
) -> dict:
    episode_id = episode_id_for_cut_contract(episode_dir)
    if project is None:
        try:
            project = read_json(episode_dir / "episode.json").get("series_title") or episode_dir.parent.parent.name
        except Exception:
            project = episode_dir.parent.parent.name

    cuts: list[dict] = []
    group_matches = list(CLEAN_GROUP_RE.finditer(content))
    running_start = 0.0
    for index, group_match in enumerate(group_matches, start=1):
        block_start = group_match.end()
        block_end = group_matches[index].start() if index < len(group_matches) else len(content)
        block = content[block_start:block_end]
        heading = group_match.group(0)
        cut_match = CUT_ID_RE.search(heading)
        cut_id = cut_match.group("cut_id") if cut_match else _desired_cut_id(episode_id, index)

        time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
        if time_matches:
            durations, _ = _extract_time_range_durations(time_matches)
            duration_sec = sum(value for value in durations if value > 0)
        else:
            duration_match = CLEAN_GROUP_TOTAL_RE.search(group_match.group("rest"))
            duration_sec = _parse_seconds(duration_match.group("seconds")) if duration_match else 0.0

        cuts.append(
            {
                "cut_id": cut_id,
                "group_index": index,
                "title": _extract_group_title(group_match.group("rest")),
                "scene": _extract_bold_meta(block, "场景"),
                "characters": _extract_bold_meta(block, "人物"),
                "props": _extract_bold_meta(block, "道具"),
                "duration_sec": _json_seconds(duration_sec),
                "group_start_sec": _json_seconds(running_start),
                "group_end_sec": _json_seconds(running_start + duration_sec),
                "source_group_label": f"第{index}组",
            }
        )
        running_start += duration_sec

    payload = {
        "project": project,
        "episode_id": episode_id,
        "source_hashes": {
            "final_txt_sha256": source_final_sha256
            or hashlib.sha256(content.encode("utf-8")).hexdigest(),
        },
        "cuts": cuts,
    }
    workflow_identity = build_resolved_workflow_identity(episode_dir)
    if workflow_identity is not None:
        payload = {
            "schema_version": 2,
            "workflow_identity": workflow_identity,
            **payload,
        }
    return payload


def write_simple_xlsx(path: Path, sheet_name: str, rows: list[list[object]]) -> None:
    """Write a minimal XLSX file without adding a third-party runtime dependency."""

    def column_name(number: int) -> str:
        name = ""
        while number:
            number, rem = divmod(number - 1, 26)
            name = chr(65 + rem) + name
        return name

    def cell_xml(value: object, row_index: int, col_index: int) -> str:
        ref = f"{column_name(col_index)}{row_index}"
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return f'<c r="{ref}"><v>{value}</v></c>'
        text = xml_escape("" if value is None else str(value))
        return f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>'

    sheet_rows = []
    for row_index, row in enumerate(rows, start=1):
        cells = "".join(cell_xml(value, row_index, col_index) for col_index, value in enumerate(row, start=1))
        sheet_rows.append(f'<row r="{row_index}">{cells}</row>')

    dimension = f"A1:{column_name(max(len(row) for row in rows) if rows else 1)}{max(len(rows), 1)}"
    worksheet_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<dimension ref="{dimension}"/><sheetData>{"".join(sheet_rows)}</sheetData></worksheet>'
    )
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheets><sheet name="{xml_escape(sheet_name)}" sheetId="1" r:id="rId1"/></sheets></workbook>'
    )
    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '</Types>'
    )
    root_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '</Relationships>'
    )
    workbook_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
        '</Relationships>'
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml)
        archive.writestr("_rels/.rels", root_rels_xml)
        archive.writestr("xl/workbook.xml", workbook_xml)
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml)
        archive.writestr("xl/worksheets/sheet1.xml", worksheet_xml)


def write_storyboard_index_files(episode_dir: Path, content: str | None = None) -> tuple[Path, Path]:
    final_path = episode_dir / "final.txt"
    if content is None:
        content = final_path.read_text(encoding="utf-8", errors="replace")
    payload = build_storyboard_index_payload(
        content=content,
        episode_dir=episode_dir,
        source_final_sha256=hashlib.sha256(final_path.read_bytes()).hexdigest(),
    )
    json_path = episode_dir / "storyboard_index.json"
    xlsx_path = episode_dir / "storyboard_index.xlsx"
    write_json(json_path, payload)

    rows: list[list[object]] = [
        [
            "project",
            "episode_id",
            "cut_id",
            "group_index",
            "title",
            "scene",
            "characters",
            "props",
            "duration_sec",
            "source_group_label",
        ]
    ]
    for cut in payload["cuts"]:
        rows.append(
            [
                payload["project"],
                payload["episode_id"],
                cut["cut_id"],
                cut["group_index"],
                cut["title"],
                cut["scene"],
                "、".join(cut["characters"]),
                "、".join(cut["props"]),
                cut["duration_sec"],
                cut["source_group_label"],
            ]
        )
    write_simple_xlsx(xlsx_path, "storyboard_index", rows)
    return json_path, xlsx_path


def remove_storyboard_index_files(episode_dir: Path) -> None:
    for name in ("storyboard_index.json", "storyboard_index.xlsx"):
        path = episode_dir / name
        if path.exists():
            path.unlink()


def _validate_review_checked_groups(payload: dict, content: str, review_name: str) -> list[str]:
    expected = _storyboard_group_labels(content)
    if not expected:
        return []
    checked = {item.strip() for item in payload.get("checked_groups", []) if isinstance(item, str)}
    missing = [label for label in expected if label not in checked]
    if missing:
        return [f"{review_name} checked_groups missing reviewed groups: {', '.join(missing[:8])}"]
    return []


def _status_reviewer_metadata(status_payload: dict) -> dict | None:
    nested = status_payload.get("reviewer")
    if isinstance(nested, dict):
        return {
            "source": nested.get("source"),
            "pass": nested.get("pass"),
            "issues_count": nested.get("issues_count", nested.get("hard_issues_count")),
            "warnings_count": nested.get("warnings_count"),
        }

    if any(key in status_payload for key in ("reviewer_pass", "reviewer_issues_count", "reviewer_source")):
        return {
            "source": status_payload.get("reviewer_source"),
            "pass": status_payload.get("reviewer_pass"),
            "issues_count": status_payload.get("reviewer_issues_count"),
            "warnings_count": status_payload.get("reviewer_warnings_count"),
        }

    return None


def _expected_reviewer_source(episode_dir: Path) -> str:
    meta_path = episode_dir / "episode.json"
    if meta_path.is_file():
        try:
            meta = read_json(meta_path)
        except Exception:
            meta = {}
        reviewer_source = meta.get("reviewer_source") or meta.get("reviewer_skill_name")
        if isinstance(reviewer_source, str) and reviewer_source.strip():
            return reviewer_source.strip()
    return "storyboard-reviewer"


def validate_review_artifacts(episode_dir: Path) -> list[str]:
    """Require evidence that the configured storyboard reviewer ran; clean format is not review."""
    issues: list[str] = []
    expected_reviewer_source = _expected_reviewer_source(episode_dir)
    review_contract_version = _episode_review_contract_version(episode_dir)
    boundary_present = _episode_has_boundary_context(episode_dir)

    review_payload, review_error = _read_review_json(
        episode_dir / "review.txt",
        reviewer_source=expected_reviewer_source,
        review_contract_version=review_contract_version,
        boundary_present=boundary_present,
    )
    if review_error:
        issues.append(review_error)
    elif review_payload is not None:
        final_path = episode_dir / "final.txt"
        if final_path.is_file():
            final_content = final_path.read_text(encoding="utf-8", errors="replace")
            requires_boundary = _episode_has_boundary_context(episode_dir)
            issues.extend(_validate_review_checked_groups(review_payload, final_content, "review.txt"))
            if is_vertical_v2_reviewer(expected_reviewer_source, review_contract_version):
                previous_episode_id: str | None = None
                previous_final_content: str | None = None
                binding_issues: list[str] = []
                if is_vertical_v3_reviewer(expected_reviewer_source, review_contract_version):
                    issues.extend(
                        validate_vertical_review_facts_file(
                            episode_dir,
                            final_content,
                            review_contract_version=review_contract_version,
                            require_cross_episode_boundary=requires_boundary,
                        )
                    )
                    if requires_boundary:
                        previous_episode_id, previous_final_content, binding_issues = load_previous_final_binding(
                            episode_dir
                        )
                if not binding_issues:
                    issues.extend(
                        validate_vertical_review_evidence(
                            review_payload,
                            final_content,
                            "review.txt",
                            require_cross_episode_boundary=requires_boundary,
                            review_contract_version=review_contract_version,
                            previous_episode_id=previous_episode_id,
                            previous_final_content=previous_final_content,
                        )
                    )

    status_path = episode_dir / "status.json"
    status_payload: dict | None = None
    if not status_path.is_file():
        issues.append("missing status.json with reviewer metadata")
    else:
        try:
            status_payload = read_json(status_path)
        except Exception as exc:
            issues.append(f"status.json is not valid JSON: {exc}")

    if status_payload is not None:
        metadata = _status_reviewer_metadata(status_payload)
        if metadata is None:
            issues.append(
                "status.json missing reviewer metadata: add reviewer_source, "
                "reviewer_pass, reviewer_issues_count, and reviewer_warnings_count"
            )
        else:
            if metadata.get("source") != expected_reviewer_source:
                issues.append(f"status.json reviewer_source must be `{expected_reviewer_source}`")
            if not isinstance(metadata.get("pass"), bool):
                issues.append("status.json reviewer_pass must be a boolean")
            if not isinstance(metadata.get("issues_count"), int):
                issues.append("status.json reviewer_issues_count must be an integer")
            if not isinstance(metadata.get("warnings_count"), int):
                issues.append("status.json reviewer_warnings_count must be an integer")

            if review_payload is not None:
                review_pass = review_payload["pass"]
                review_issues_count = len(review_payload["issues"])
                review_warnings_count = len(review_payload["warnings"])
                if metadata.get("pass") != review_pass:
                    issues.append("status.json reviewer_pass does not match review.txt pass")
                if metadata.get("issues_count") != review_issues_count:
                    issues.append("status.json reviewer_issues_count does not match review.txt issues length")
                if metadata.get("warnings_count") != review_warnings_count:
                    issues.append("status.json reviewer_warnings_count does not match review.txt warnings length")

                status = status_payload.get("status")
                if status == "done" and (not review_pass or review_issues_count):
                    issues.append(f"status.json cannot be `done` when {expected_reviewer_source} reports hard issues")
                if status == "done" and status_payload.get("hard_issues_remaining"):
                    issues.append("status.json cannot be `done` with hard_issues_remaining")

    segments_dir = episode_dir / "segments"
    if segments_dir.is_dir():
        segment_dirs = [
            path
            for path in sorted(segments_dir.iterdir())
            if path.is_dir() and (path / "script.txt").is_file()
        ]
        # A single-segment episode's segment review is, by construction, a review of the
        # same groups as the episode review: identical dialogue_checks, handoff_checks and
        # camera_motion_checks written twice. Measured on a real run the duplicate review
        # cost more bytes than the storyboard it reviewed. Require it only when there is
        # more than one segment; still validate it when a worker writes it anyway.
        segment_review_required = len(segment_dirs) > 1
        for segment_dir in segment_dirs:
            review_path = segment_dir / "review.md"
            if not segment_review_required and not review_path.is_file():
                continue
            segment_payload, segment_error = _read_review_json(
                review_path,
                reviewer_source=expected_reviewer_source,
                review_contract_version=review_contract_version,
                require_numeric_evidence=False,
                boundary_present=boundary_present,
            )
            if segment_error:
                issues.append(f"{segment_dir.name}: {segment_error}")
            elif segment_payload is not None:
                segment_final = segment_dir / "final.txt"
                segment_draft = segment_dir / "draft.txt"
                review_target = segment_final if segment_final.is_file() else segment_draft
                if review_target.is_file():
                    target_content = review_target.read_text(encoding="utf-8", errors="replace")
                    for issue in _validate_review_checked_groups(segment_payload, target_content, "review.md"):
                        issues.append(f"{segment_dir.name}: {issue}")
                    # Numeric evidence is optional here (the episode review covers it), but
                    # a partial or invented array is worse than none: validate in full
                    # whenever the segment review actually claims any of it.
                    claims_numeric = any(
                        segment_payload.get(key)
                        for key in ("dialogue_checks", "handoff_checks", "camera_motion_checks")
                    )
                    if claims_numeric and is_vertical_v2_reviewer(
                        expected_reviewer_source, review_contract_version
                    ):
                        for issue in validate_vertical_review_evidence(
                            segment_payload,
                            target_content,
                            "review.md",
                        ):
                            issues.append(f"{segment_dir.name}: {issue}")

    return issues


def prepare_workspace(args: argparse.Namespace) -> int:
    project_root = Path.cwd().resolve()
    source = args.source.resolve()
    prompt_path = find_prompt_file(project_root, args.prompt).resolve() if args.prompt else None
    aspect = args.aspect
    visual_style = args.visual_style
    video_profile = getattr(args, "video_profile", DEFAULT_VIDEO_PROFILE)
    requested_resolution = getattr(args, "video_resolution", None)
    visual_style_preset = getattr(args, "visual_style_preset", None)
    project_pack_id = getattr(args, "project_pack_id", None)
    try:
        workspace_config = resolved_workspace_config(
            video_profile=video_profile,
            aspect=aspect,
            visual_style=visual_style,
            resolution=requested_resolution,
            mode=args.mode,
            visual_style_preset=visual_style_preset,
            project_pack_id=project_pack_id,
            project_root=project_root,
        )
    except ValueError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2
    profile_cfg = video_profile_config(video_profile)
    visual_style_preset = workspace_config["visual_style_preset"]
    preset = visual_style_preset_snapshot(video_profile, visual_style_preset)
    project_pack = project_pack_snapshot(
        project_root=project_root,
        video_profile=video_profile,
        aspect=aspect,
        visual_style=visual_style,
        mode=args.mode,
        visual_style_preset=visual_style_preset,
        project_pack_id=project_pack_id,
    )
    video_resolution = workspace_config["video_resolution"]
    episodes = resolve_source_episodes(source)
    if not episodes:
        print("[error] no episodes found", file=sys.stderr)
        return 1

    run_id = args.run_name or datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = (args.workspace_dir / run_id).resolve()
    out_dir = args.out_dir.resolve()
    if run_dir.exists() and not args.force:
        print(f"[error] run directory already exists: {run_dir}", file=sys.stderr)
        return 1
    if run_dir.exists() and args.force:
        workspace_root = args.workspace_dir.resolve()
        if run_dir == workspace_root or workspace_root not in run_dir.parents:
            print(f"[error] refusing to clear unexpected run directory: {run_dir}", file=sys.stderr)
            return 1
        shutil.rmtree(run_dir)

    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "episodes").mkdir(exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    aspect_cfg = storyboard_workflow_config(aspect, video_profile)
    generator_skill_path, reviewer_skill_path, generation_rules_source, reviewer_rules_source = ensure_project_agent_skills(
        project_root=project_root,
        prompt_path=prompt_path,
        review_skill_path=args.review_skill,
        aspect=aspect,
        video_profile=video_profile,
    )
    seedance_profile_path = (project_root / profile_cfg["profile_skill_path"]).resolve()
    if not seedance_profile_path.is_file():
        print(f"[error] Seedance prompt profile not found: {seedance_profile_path}", file=sys.stderr)
        return 1
    cg_visual_style_skill_path: Path | None = None
    if visual_style == "3d-cg":
        cg_visual_style_skill_path = (project_root / CG_VISUAL_STYLE_SKILL_PATH).resolve()
        if not cg_visual_style_skill_path.is_file():
            print(f"[error] 3D CG visual style skill not found: {cg_visual_style_skill_path}", file=sys.stderr)
            return 1

    write_utf8(run_dir / "context.md", make_agent_context(
        project_root=project_root,
        generation_rules_source=generation_rules_source,
        reviewer_rules_source=reviewer_rules_source,
        out_dir=out_dir,
        episodes_count=len(episodes),
        generator_skill_path=generator_skill_path,
        reviewer_skill_path=reviewer_skill_path,
        seedance_profile_path=seedance_profile_path,
        cg_visual_style_skill_path=cg_visual_style_skill_path,
        visual_style=visual_style,
        aspect=aspect,
        mode=args.mode,
        video_profile=video_profile,
        video_resolution=video_resolution,
        visual_style_preset=visual_style_preset,
        project_pack=project_pack,
    ))
    profile_contract = {
        "profile_id": video_profile,
        "contract_version": profile_cfg["contract_version"],
        "provider_contract_version": profile_cfg["provider_contract_version"],
        "label": profile_cfg["label"],
        "target_video_model": profile_cfg["target_video_model"],
        "profile_skill_path": str(seedance_profile_path),
        "storyboard_aspect": aspect,
        "visual_style": visual_style,
        "visual_style_preset": preset["id"] if preset else None,
        "visual_style_preset_version": preset["version"] if preset else None,
        "visual_style_preset_sha256": preset["sha256"] if preset else None,
        "aspect_ratio": profile_cfg["aspect_ratio"],
        "resolution": video_resolution,
        "supported_resolutions": list(profile_cfg["supported_resolutions"]),
        "fps": profile_cfg["fps"],
        "generate_audio": profile_cfg["generate_audio"],
        "video_task_type": profile_cfg["video_task_type"],
        "requires_multimodal_materials": profile_cfg["requires_multimodal_materials"],
        "minimum_material_inputs": profile_cfg["minimum_material_inputs"],
        "allowed_multimodal_material_types": list(profile_cfg["allowed_multimodal_material_types"]),
        "forbidden_video_task_modes": list(profile_cfg["forbidden_video_task_modes"]),
        "duration_min_seconds": profile_cfg["duration_min_seconds"],
        "duration_max_seconds": profile_cfg["duration_max_seconds"],
        "timeline_granularity_seconds": profile_cfg["timeline_granularity_seconds"],
        "collection_tail_mode": profile_cfg["collection_tail_mode"],
        "provider_task_mapping": profile_cfg["provider_task_mapping"],
        "capabilities": dict(profile_cfg["capabilities"]),
        "project_pack_id": project_pack["id"] if project_pack else None,
        "project_pack_version": project_pack["version"] if project_pack else None,
        "project_pack_path": project_pack["path"] if project_pack else None,
        "project_pack_sha256": project_pack["sha256"] if project_pack else None,
    }
    write_json(run_dir / "video_profile.json", profile_contract)
    manifest: dict = {
        "version": AGENT_WORKSPACE_VERSION,
        "storyboard_rule_version": storyboard_quality_policy_version(),
        "storyboard_quality_policy_path": str((project_root / STORYBOARD_QUALITY_POLICY_PATH).resolve()),
        "run_id": run_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "project_root": str(project_root),
        "source": str(source),
        "prompt_path": str(prompt_path) if prompt_path else None,
        "generation_rules_source": str(generation_rules_source),
        "reviewer_rules_source": str(reviewer_rules_source),
        "generator_skill_path": str(generator_skill_path),
        "reviewer_skill_path": str(reviewer_skill_path),
        "seedance_profile_path": str(seedance_profile_path),
        "video_profile_path": str(run_dir / "video_profile.json"),
        "video_profile": video_profile,
        "video_profile_contract_version": profile_cfg["contract_version"],
        "provider_contract_version": profile_cfg["provider_contract_version"],
        "storyboard_aspect": aspect,
        "target_video_model": profile_cfg["target_video_model"],
        "video_resolution": video_resolution,
        "video_aspect_ratio": profile_cfg["aspect_ratio"],
        "video_fps": profile_cfg["fps"],
        "generate_audio": profile_cfg["generate_audio"],
        "video_task_type": profile_cfg["video_task_type"],
        "requires_multimodal_materials": profile_cfg["requires_multimodal_materials"],
        "minimum_material_inputs": profile_cfg["minimum_material_inputs"],
        "allowed_multimodal_material_types": list(profile_cfg["allowed_multimodal_material_types"]),
        "forbidden_video_task_modes": list(profile_cfg["forbidden_video_task_modes"]),
        "group_duration_min_seconds": profile_cfg["duration_min_seconds"],
        "group_duration_max_seconds": profile_cfg["duration_max_seconds"],
        "timeline_granularity_seconds": profile_cfg["timeline_granularity_seconds"],
        "visual_style": visual_style,
        "visual_style_preset": preset["id"] if preset else None,
        "visual_style_preset_version": preset["version"] if preset else None,
        "visual_style_preset_sha256": preset["sha256"] if preset else None,
        "provider_task_mapping": profile_cfg["provider_task_mapping"],
        "profile_capabilities": dict(profile_cfg["capabilities"]),
        "project_pack_id": project_pack["id"] if project_pack else None,
        "project_pack_version": project_pack["version"] if project_pack else None,
        "project_pack_path": project_pack["path"] if project_pack else None,
        "project_pack_sha256": project_pack["sha256"] if project_pack else None,
        "cg_visual_style_skill_path": str(cg_visual_style_skill_path) if cg_visual_style_skill_path else None,
        "out_dir": str(out_dir),
        "agent": args.agent,
        "mode": args.mode,
        "parallelism": args.parallelism,
        "episodes": [],
    }

    continuity_links = build_source_continuity_links(episodes) if aspect == "vertical" else []
    continuity_by_current = {int(link["current_index"]): link for link in continuity_links}
    continuity_by_previous = {int(link["previous_index"]): link for link in continuity_links}
    episode_ids = [make_episode_id(episode, index) for index, episode in enumerate(episodes, start=1)]

    for index, episode in enumerate(episodes, start=1):
        zero_index = index - 1
        episode_id = episode_ids[zero_index]
        episode_dir = run_dir / "episodes" / episode_id
        episode_dir.mkdir(parents=True, exist_ok=True)
        output_path = make_output_path(out_dir, episode, index, model=args.output_model_suffix)

        write_utf8(episode_dir / "script.txt", episode.script_text)
        boundary_link = continuity_by_current.get(zero_index)
        if boundary_link is not None:
            previous_index = int(boundary_link["previous_index"])
            previous_episode = episodes[previous_index]
            previous_scene = boundary_link["previous_scene"]
            current_scene = boundary_link["current_scene"]
            # Built from a flush template, not textwrap.dedent(f"..."): the interpolated
            # script excerpts contain unindented lines, so dedent found a common prefix of ""
            # and left the metadata lines indented by 16 spaces. load_previous_final_binding
            # anchors on `^previous_episode:`, so every generated boundary file failed to
            # parse. That stayed invisible while no boundary file was ever generated.
            boundary_text = "\n".join(
                [
                    "# Cross-Episode Boundary Context",
                    "",
                    "continuous_from_previous: true",
                    f"previous_episode: {episode_ids[previous_index]}",
                    f"current_episode: {episode_id}",
                    f"previous_final: ../{episode_ids[previous_index]}/final.txt",
                    f"previous_scene: {previous_scene['heading']}",
                    f"current_scene: {current_scene['heading']}",
                    f"source_time_conflict: {str(bool(boundary_link['time_conflict'])).lower()}",
                    "",
                    "## Previous Episode Source Tail",
                    "",
                    previous_episode.script_text[-1600:].strip(),
                    "",
                    "## Current Episode Source Head",
                    "",
                    episode.script_text[:1600].strip(),
                    "",
                    "## Required Use",
                    "",
                    "Generate the current first group from the previous episode's last visible "
                    "state. When both episodes are assigned to one worker, finish and validate "
                    "the previous episode first, then replace source-only assumptions with the "
                    "actual previous `final.txt` last group. Preserve time/light, positions, "
                    "posture, props, doors/vehicles, and ongoing sound unless the source "
                    "supplies a visible transition.",
                ]
            ).strip()
            write_utf8(episode_dir / "boundary_context.md", boundary_text)
        episode_meta = {
            "episode_id": episode_id,
            "storyboard_rule_version": storyboard_quality_policy_version(),
            "storyboard_quality_policy_path": str((project_root / STORYBOARD_QUALITY_POLICY_PATH).resolve()),
            "episode_number": episode.episode_number,
            "display_name": episode.display_name,
            "series_title": episode.series_title,
            "source_path": str(episode.source_path),
            "output_path": str(output_path),
            "storyboard_aspect": aspect,
            "visual_style": visual_style,
            "visual_style_preset": preset["id"] if preset else None,
            "visual_style_preset_version": preset["version"] if preset else None,
            "visual_style_preset_sha256": preset["sha256"] if preset else None,
            "video_profile": video_profile,
            "video_profile_contract_version": profile_cfg["contract_version"],
            "provider_contract_version": profile_cfg["provider_contract_version"],
            "provider_task_mapping": profile_cfg["provider_task_mapping"],
            "profile_capabilities": dict(profile_cfg["capabilities"]),
            "project_pack_id": project_pack["id"] if project_pack else None,
            "project_pack_version": project_pack["version"] if project_pack else None,
            "project_pack_path": project_pack["path"] if project_pack else None,
            "project_pack_sha256": project_pack["sha256"] if project_pack else None,
            "seedance_profile_path": str(seedance_profile_path),
            "target_video_model": profile_cfg["target_video_model"],
            "video_resolution": video_resolution,
            "video_aspect_ratio": profile_cfg["aspect_ratio"],
            "video_fps": profile_cfg["fps"],
            "generate_audio": profile_cfg["generate_audio"],
            "video_task_type": profile_cfg["video_task_type"],
            "requires_multimodal_materials": profile_cfg["requires_multimodal_materials"],
            "minimum_material_inputs": profile_cfg["minimum_material_inputs"],
            "allowed_multimodal_material_types": list(profile_cfg["allowed_multimodal_material_types"]),
            "forbidden_video_task_modes": list(profile_cfg["forbidden_video_task_modes"]),
            "group_duration_min_seconds": profile_cfg["duration_min_seconds"],
            "group_duration_max_seconds": profile_cfg["duration_max_seconds"],
            "timeline_granularity_seconds": profile_cfg["timeline_granularity_seconds"],
            "generator_skill_name": aspect_cfg["generator_name"],
            "reviewer_skill_name": aspect_cfg["reviewer_name"],
            "reviewer_source": aspect_cfg["reviewer_name"],
            "vertical_review_contract_version": (
                resolved_vertical_review_contract_version(video_profile)
                if aspect == "vertical"
                else None
            ),
            "continuous_from_previous": boundary_link is not None,
            "continuity_with_next": zero_index in continuity_by_previous,
            "depends_on_episode": episode_ids[int(boundary_link["previous_index"])] if boundary_link else None,
        }
        write_json(episode_dir / "episode.json", episode_meta)

        segments = []
        if args.mode == "scene":
            segments_dir = episode_dir / "segments"
            segments_dir.mkdir(exist_ok=True)
            segments = split_episode_into_segments(episode)
            for segment in segments:
                seg_dir = segments_dir / f"seg{segment.index:02d}"
                seg_dir.mkdir(exist_ok=True)
                write_utf8(seg_dir / "script.txt", segment.script_text)
                write_json(
                    seg_dir / "segment.json",
                    {
                        "index": segment.index,
                        "total": segment.total,
                        "title": segment.title,
                    },
                )

        task_text = make_episode_task(
            run_dir=run_dir,
            episode_dir=episode_dir,
            episode=episode,
            episode_id=episode_id,
            output_name=output_path.name,
            generator_skill_path=generator_skill_path,
            reviewer_skill_path=reviewer_skill_path,
            seedance_profile_path=seedance_profile_path,
            cg_visual_style_skill_path=cg_visual_style_skill_path,
            visual_style=visual_style,
            aspect=aspect,
            mode=args.mode,
            video_profile=video_profile,
            video_resolution=video_resolution,
            visual_style_preset=visual_style_preset,
            project_pack=project_pack,
        )
        write_utf8(episode_dir / "TASK.md", task_text)
        prompt_file = episode_dir / "agent_prompt.md"
        write_utf8(prompt_file, make_agent_prompt(episode_dir))

        manifest["episodes"].append(
            {
                **episode_meta,
                "episode_dir": str(episode_dir),
                "task_file": str(episode_dir / "TASK.md"),
                "prompt_file": str(prompt_file),
                "last_message_file": str(episode_dir / "agent-last-message.txt"),
                "agent_log_file": str(episode_dir / "agent-stdout.log"),
                "script_chars": len(episode.script_text),
                "segments": len(segments),
                "segment_titles": [segment.title for segment in segments],
                "continuous_from_previous": boundary_link is not None,
                "continuity_with_next": zero_index in continuity_by_previous,
            }
        )

    write_json(run_dir / "manifest.json", manifest)
    write_utf8(
        run_dir / "AGENTS.md",
        textwrap.dedent(
            """
            # Storyboard Agent Run Instructions

            This directory is an agent-native workspace. Each `episodes/epXX` folder is an independent task.

            ## Dispatcher Hard Stop

            If this run contains 2 or more episodes, the host/main agent is a dispatcher only.

            Dispatcher must:
            - Create subagents/workers and dispatch `episodes/epXX/agent_prompt.md`.
            - Run up to the configured worker limit in parallel.
            - Stop with `NEED_USER_DISPATCH` and list prompt paths if worker creation is unavailable or requires user authorization.

            Dispatcher must not:
            - Directly generate storyboard body text.
            - Sequentially process multiple episodes in the main thread.
            - Open `episodes/ep*/script.txt` and begin production work.
            - Write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
            - Downgrade to main-thread sequential production when subagents/workers are unavailable.

            Agents must:
            - Read the task files instead of relying on hidden state.
            - Write durable outputs to files.
            - Run validation before marking a task done.
            - Preserve drafts and review notes even when the final status is `needs_review`.
            """
        ).strip(),
    )
    write_runner_scripts(run_dir=run_dir, agent=args.agent, parallelism=args.parallelism, model=args.model)

    print(f"[done] agent workspace: {run_dir}")
    print(f"[next] read: {run_dir / 'DISPATCH_PROMPT.md'}")
    print("[next] dispatch episode agents outside Python; then run .\\COLLECT_RESULTS.ps1")
    return 0


def validate_episode(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    episode_id = episode_id_for_cut_contract(episode_dir)
    pre_check = getattr(args, "pre_check", False)
    content_file = getattr(args, "content_file", None)

    if content_file is not None:
        target_path = content_file.resolve()
        if not target_path.is_file():
            print(f"[error] content file not found: {target_path}", file=sys.stderr)
            return 1
    else:
        target_path = episode_dir / "final.txt"
        if not target_path.is_file():
            print(f"[error] final.txt not found: {target_path}", file=sys.stderr)
            return 1

    content = target_path.read_text(encoding="utf-8", errors="replace")
    if args.fix_metadata:
        fix_messages: list[str] = []
        cleaned = strip_machine_tags(content)
        if cleaned != content:
            content = cleaned
            fix_messages.append("removed legacy machine tags")
        content, numbering_changes = normalize_clean_storyboard_numbering(content)
        if numbering_changes:
            fix_messages.append("renumbered " + "; ".join(numbering_changes[:8]))
        content, cut_id_changes = ensure_storyboard_cut_ids(content, episode_id)
        if cut_id_changes:
            fix_messages.append("normalized cut_id " + "; ".join(cut_id_changes[:8]))
        if fix_messages:
            write_utf8(target_path, content)
            print("[fixed] " + " | ".join(fix_messages))

    video_profile = episode_video_profile(episode_dir)
    video_profile_contract_issues = validate_episode_video_profile_contract(episode_dir)
    clean_issues = validate_clean_storyboard_format(content, video_profile=video_profile)
    cut_id_issues = validate_storyboard_cut_ids(content, episode_id)
    horizontal_run = is_horizontal_episode_dir(episode_dir)
    seedance_horizontal_timeline_only = video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE
    review_contract_version = _episode_review_contract_version(episode_dir)
    manages_review_facts = (
        pre_check
        and content_file is None
        and not horizontal_run
        and review_contract_version >= 3
    )
    prepared_review_facts: dict | None = None
    review_facts_input_issues: list[str] = []
    if manages_review_facts:
        prepared_review_facts, review_facts_input_issues = build_vertical_review_facts_for_episode(
            episode_dir,
            content,
            review_contract_version=review_contract_version,
        )
    quality_issues = validate_storyboard_quality_floor(content, allow_horizontal_output_fields=horizontal_run)
    if horizontal_run:
        horizontal_motion_issues = validate_horizontal_camera_motion_contract(
            content,
            visual_style=episode_visual_style(episode_dir),
            timeline_only=seedance_horizontal_timeline_only,
        )
        horizontal_output_structure_issues = validate_horizontal_output_structure_contract(
            content,
            timeline_only=seedance_horizontal_timeline_only,
        )
        horizontal_visual_style_issues = validate_horizontal_visual_style_contract(
            content,
            visual_style=episode_visual_style(episode_dir),
        )
        horizontal_special_effect_issues = validate_effect_placement(
            content,
            visual_style=episode_visual_style(episode_dir),
            effect_required="auto",
            timeline_only=seedance_horizontal_timeline_only,
        )
        physical_plausibility_issues = validate_physical_plausibility_floor(content)
    else:
        horizontal_motion_issues = []
        horizontal_output_structure_issues = []
        horizontal_visual_style_issues = []
        horizontal_special_effect_issues = []
        physical_plausibility_issues = []
    if not horizontal_run and review_contract_version >= 2:
        vertical_space_lock_issues = validate_vertical_space_lock_contract(content)
    else:
        vertical_space_lock_issues = []
    if pre_check:
        review_issues: list[str] = []
        review_pass_issues: list[str] = []
    else:
        review_issues = validate_review_artifacts(episode_dir)
        expected_reviewer_source = _expected_reviewer_source(episode_dir)
        review_payload, review_error = _read_review_json(
            episode_dir / "review.txt",
            reviewer_source=expected_reviewer_source,
            review_contract_version=_episode_review_contract_version(episode_dir),
            boundary_present=_episode_has_boundary_context(episode_dir),
        )
        review_pass_issues = []
        if review_error is None and not _storyboard_review_passed(review_payload):
            review_pass_issues.append("storyboard_reviewer: reviewer_not_passed")
    issues = (
        video_profile_contract_issues
        + clean_issues
        + cut_id_issues
        + quality_issues
        + horizontal_motion_issues
        + horizontal_output_structure_issues
        + horizontal_visual_style_issues
        + horizontal_special_effect_issues
        + physical_plausibility_issues
        + vertical_space_lock_issues
        + review_facts_input_issues
        + review_issues
        + review_pass_issues
    )
    report_lines = ["# Episode Validation", ""]
    if issues:
        if manages_review_facts:
            (episode_dir / "review_facts.json").unlink(missing_ok=True)
        report_lines.append("status: failed")
        report_lines.append("")
        if video_profile_contract_issues:
            report_lines.append("## Video Profile Contract")
            report_lines.extend(f"- {issue}" for issue in video_profile_contract_issues)
            report_lines.append("")
        if clean_issues:
            report_lines.append("## Clean Format")
            report_lines.extend(f"- {issue}" for issue in clean_issues)
            report_lines.append("")
        if cut_id_issues:
            report_lines.append("## Cut ID Contract")
            report_lines.extend(f"- {issue}" for issue in cut_id_issues)
            report_lines.append("")
        if quality_issues:
            report_lines.append("## Quality Floor")
            report_lines.extend(f"- {issue}" for issue in quality_issues)
            report_lines.append("")
        if horizontal_motion_issues:
            report_lines.append("## Horizontal Camera Motion")
            report_lines.extend(f"- {issue}" for issue in horizontal_motion_issues)
            report_lines.append("")
        if horizontal_output_structure_issues:
            report_lines.append("## Horizontal Output Structure")
            report_lines.extend(f"- {issue}" for issue in horizontal_output_structure_issues)
            report_lines.append("")
        if horizontal_visual_style_issues:
            report_lines.append("## Horizontal Visual Style")
            report_lines.extend(f"- {issue}" for issue in horizontal_visual_style_issues)
            report_lines.append("")
        if horizontal_special_effect_issues:
            report_lines.append("## Horizontal Special Effects")
            report_lines.extend(f"- {issue}" for issue in horizontal_special_effect_issues)
            report_lines.append("")
        if physical_plausibility_issues:
            report_lines.append("## Physical Plausibility")
            report_lines.extend(f"- {issue}" for issue in physical_plausibility_issues)
            report_lines.append("")
        if vertical_space_lock_issues:
            report_lines.append("## Vertical Space Lock")
            report_lines.extend(f"- {issue}" for issue in vertical_space_lock_issues)
            report_lines.append("")
        if review_facts_input_issues:
            report_lines.append("## Review Facts Input")
            report_lines.extend(f"- {issue}" for issue in review_facts_input_issues)
            report_lines.append("")
        if review_issues:
            report_lines.append("## Storyboard Reviewer Evidence")
            report_lines.extend(f"- {issue}" for issue in review_issues)
            report_lines.append("")
        if review_pass_issues:
            report_lines.append("## Storyboard Reviewer Pass")
            report_lines.extend(f"- {issue}" for issue in review_pass_issues)
        write_utf8(episode_dir / "protocol_report.md", "\n".join(report_lines))
        print(f"[failed] {len(issues)} validation issue(s)")
        for issue in issues:
            print(f"- {issue}")
        return 1

    report_lines.append("status: passed")
    report_lines.append("")
    if manages_review_facts:
        assert prepared_review_facts is not None
        write_json(
            episode_dir / "review_facts.json",
            prepared_review_facts,
        )
        report_lines.append("- review_facts: generated and bound to current final.txt")
    if video_profile == SEEDANCE25_LIVE_VERTICAL_PROFILE:
        report_lines.append("- video_profile_contract: multimodal_generation-only passed")
    report_lines.append("- clean_format: passed")
    report_lines.append("- cut_id_contract: passed")
    report_lines.append("- quality_floor: passed")
    if horizontal_run:
        report_lines.append("- horizontal_camera_motion: passed")
        report_lines.append("- horizontal_output_structure: passed")
        report_lines.append("- horizontal_visual_style: passed")
        report_lines.append("- horizontal_special_effects: passed")
        report_lines.append("- physical_plausibility: passed")
    elif review_contract_version >= 2:
        report_lines.append("- vertical_space_lock: passed")
    if not pre_check:
        report_lines.append("- review_evidence: passed")
        report_lines.append("- storyboard_reviewer: passed")
        should_export_index = (
            getattr(args, "export_index", False)
            or video_profile_config(video_profile)["capabilities"]["auto_export_index"]
        )
        if should_export_index:
            write_storyboard_index_files(episode_dir, content)
            if video_profile_config(video_profile)["capabilities"]["auto_export_index"]:
                report_lines.append("- storyboard_index_export: passed (required by active profile)")
            else:
                report_lines.append("- storyboard_index_export: passed")
        else:
            remove_storyboard_index_files(episode_dir)
            report_lines.append("- storyboard_index_export: skipped (txt-only)")
    else:
        report_lines.append("- review_evidence: skipped (pre-check)")
        report_lines.append("- storyboard_reviewer: skipped (pre-check)")
    write_utf8(episode_dir / "protocol_report.md", "\n".join(report_lines))
    print("[passed] pre-check" if pre_check else "[passed] episode validation")
    return 0


def collect_run(args: argparse.Namespace) -> int:
    run_dir = args.run_dir.resolve()
    manifest = read_json(run_dir / "manifest.json")
    out_dir = Path(manifest["out_dir"]).resolve()
    if args.out_dir:
        out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    requested_export_index = bool(getattr(args, "export_index", False))

    summary_lines = ["# Agent Run Summary", ""]
    copied = 0
    failed = 0
    for item in manifest["episodes"]:
        episode_dir = Path(item["episode_dir"])
        final_path = episode_dir / "final.txt"
        status_path = episode_dir / "status.json"
        output_path = out_dir / Path(item["output_path"]).name
        summary_lines.append(f"## {item['episode_id']} {item['display_name']}")
        if not final_path.is_file():
            failed += 1
            summary_lines.append("- status: missing final.txt")
            summary_lines.append("")
            continue

        content = strip_machine_tags(final_path.read_text(encoding="utf-8", errors="replace"))
        content, changes = normalize_clean_storyboard_numbering(content)
        episode_contract_id = episode_id_for_cut_contract(episode_dir)
        content, cut_id_changes = ensure_storyboard_cut_ids(content, episode_contract_id)
        changes.extend(cut_id_changes)
        video_profile = episode_video_profile(episode_dir)
        export_index = (
            requested_export_index
            or video_profile_config(video_profile)["capabilities"]["auto_export_index"]
        )
        clean_issues = validate_clean_storyboard_format(content, video_profile=video_profile)
        cut_id_issues = validate_storyboard_cut_ids(content, episode_contract_id)
        horizontal_run = is_horizontal_episode_dir(episode_dir)
        seedance_horizontal_timeline_only = video_profile == SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE
        quality_issues = validate_storyboard_quality_floor(content, allow_horizontal_output_fields=horizontal_run)
        if horizontal_run:
            horizontal_motion_issues = validate_horizontal_camera_motion_contract(
                content,
                visual_style=episode_visual_style(episode_dir),
                timeline_only=seedance_horizontal_timeline_only,
            )
            horizontal_output_structure_issues = validate_horizontal_output_structure_contract(
                content,
                timeline_only=seedance_horizontal_timeline_only,
            )
            horizontal_visual_style_issues = validate_horizontal_visual_style_contract(
                content,
                visual_style=episode_visual_style(episode_dir),
            )
            horizontal_special_effect_issues = validate_effect_placement(
                content,
                visual_style=episode_visual_style(episode_dir),
                effect_required="auto",
                timeline_only=seedance_horizontal_timeline_only,
            )
            physical_plausibility_issues = validate_physical_plausibility_floor(content)
        else:
            horizontal_motion_issues = []
            horizontal_output_structure_issues = []
            horizontal_visual_style_issues = []
            horizontal_special_effect_issues = []
            physical_plausibility_issues = []
        if not horizontal_run and _episode_review_contract_version(episode_dir) >= 2:
            vertical_space_lock_issues = validate_vertical_space_lock_contract(content)
        else:
            vertical_space_lock_issues = []
        review_issues = validate_review_artifacts(episode_dir)
        issues = (
            clean_issues
            + cut_id_issues
            + quality_issues
            + horizontal_motion_issues
            + horizontal_output_structure_issues
            + horizontal_visual_style_issues
            + horizontal_special_effect_issues
            + physical_plausibility_issues
            + vertical_space_lock_issues
            + review_issues
        )
        review_payload, review_error = _read_review_json(
            episode_dir / "review.txt",
            reviewer_source=_expected_reviewer_source(episode_dir),
            review_contract_version=_episode_review_contract_version(episode_dir),
            boundary_present=_episode_has_boundary_context(episode_dir),
        )
        review_passed = review_error is None and _storyboard_review_passed(review_payload)
        status = "unknown"
        if status_path.is_file():
            try:
                status = read_json(status_path).get("status", "unknown")
            except Exception:
                status = "invalid status.json"
        if issues:
            failed += 1
            summary_lines.append(f"- status: {status}, validation_failed")
            summary_lines.extend(f"- clean_format: {issue}" for issue in clean_issues[:8])
            summary_lines.extend(f"- cut_id_contract: {issue}" for issue in cut_id_issues[:8])
            summary_lines.extend(f"- quality_floor: {issue}" for issue in quality_issues[:8])
            summary_lines.extend(f"- horizontal_camera_motion: {issue}" for issue in horizontal_motion_issues[:8])
            summary_lines.extend(f"- vertical_space_lock: {issue}" for issue in vertical_space_lock_issues[:8])
            summary_lines.extend(f"- horizontal_output_structure: {issue}" for issue in horizontal_output_structure_issues[:8])
            summary_lines.extend(f"- horizontal_visual_style: {issue}" for issue in horizontal_visual_style_issues[:8])
            summary_lines.extend(f"- horizontal_special_effects: {issue}" for issue in horizontal_special_effect_issues[:8])
            summary_lines.extend(f"- physical_plausibility: {issue}" for issue in physical_plausibility_issues[:8])
            summary_lines.extend(f"- storyboard_reviewer: {issue}" for issue in review_issues[:8])
            summary_lines.append("- copied: skipped because validation failed")
            summary_lines.append("- existing_output: not modified")
            summary_lines.append("")
            continue
        if status != "done" or not review_passed:
            failed += 1
            summary_lines.append(f"- status: {status}, reviewer_not_passed")
            if review_error:
                summary_lines.append(f"- review_evidence: failed: {review_error}")
            else:
                summary_lines.append("- review_evidence: passed")
                summary_lines.append("- storyboard_reviewer: failed")
            summary_lines.append("- copied: skipped because status is not done or storyboard reviewer did not pass")
            summary_lines.append("- existing_output: not modified")
            summary_lines.append("")
            continue

        output_content = content
        if not horizontal_run:
            output_content = append_vertical_seedance_tail_to_groups(
                output_content,
                visual_style=episode_visual_style(episode_dir),
                video_profile=video_profile,
            )

        write_utf8(output_path, output_content)
        if export_index:
            index_json_path, index_xlsx_path = write_storyboard_index_files(episode_dir, content)
            index_output_json = out_dir / f"{output_path.stem}_index.json"
            index_output_xlsx = out_dir / f"{output_path.stem}_index.xlsx"
            shutil.copy2(index_json_path, index_output_json)
            shutil.copy2(index_xlsx_path, index_output_xlsx)
        else:
            remove_storyboard_index_files(episode_dir)
            for suffix in ("_index.json", "_index.xlsx"):
                stale_output = out_dir / f"{output_path.stem}{suffix}"
                if stale_output.exists():
                    stale_output.unlink()
        copied += 1
        summary_lines.append(
            f"- status: {status}, clean_format_passed, quality_floor_passed, "
            f"review_evidence_passed, storyboard_reviewer_passed"
        )
        if changes:
            summary_lines.append(f"- clean_numbering_fixed: {'; '.join(changes[:8])}")
        summary_lines.append(f"- copied: `{output_path}`")
        if export_index:
            summary_lines.append(f"- storyboard_index_json: `{index_output_json}`")
            summary_lines.append(f"- storyboard_index_xlsx: `{index_output_xlsx}`")
        else:
            summary_lines.append("- storyboard_index: skipped (txt-only)")
        summary_lines.append("")

    summary_lines.append(f"Copied: {copied}")
    summary_lines.append(f"Validation/collection failures: {failed}")
    write_utf8(run_dir / "SUMMARY.md", "\n".join(summary_lines))
    print(f"[done] copied {copied} final file(s) to {out_dir}")
    print(f"[summary] {run_dir / 'SUMMARY.md'}")
    return 1 if failed else 0


def export_storyboard_index(args: argparse.Namespace) -> int:
    targets: list[Path] = []
    if args.episode_dir:
        targets.append(args.episode_dir.resolve())
    if args.run_dir:
        run_dir = args.run_dir.resolve()
        manifest_path = run_dir / "manifest.json"
        if manifest_path.is_file():
            manifest = read_json(manifest_path)
            targets.extend(Path(item["episode_dir"]) for item in manifest.get("episodes", []))
        else:
            targets.extend(sorted(path for path in (run_dir / "episodes").iterdir() if path.is_dir()))

    if not targets:
        print("[error] pass --episode-dir or --run-dir", file=sys.stderr)
        return 2

    exported = 0
    failed = 0
    for episode_dir in targets:
        final_path = episode_dir / "final.txt"
        if not final_path.is_file():
            print(f"[skip] missing final.txt: {episode_dir}", file=sys.stderr)
            failed += 1
            continue
        content = final_path.read_text(encoding="utf-8", errors="replace")
        if args.fix_metadata:
            content = strip_machine_tags(content)
            content, _ = normalize_clean_storyboard_numbering(content)
            content, _ = ensure_storyboard_cut_ids(content, episode_id_for_cut_contract(episode_dir))
            write_utf8(final_path, content)

        cut_issues = validate_storyboard_cut_ids(content, episode_id_for_cut_contract(episode_dir))
        if cut_issues:
            print(f"[failed] {episode_dir}", file=sys.stderr)
            for issue in cut_issues:
                print(f"- {issue}", file=sys.stderr)
            failed += 1
            continue
        json_path, xlsx_path = write_storyboard_index_files(episode_dir, content)
        print(f"[exported] {json_path}")
        print(f"[exported] {xlsx_path}")
        exported += 1

    print(f"[done] exported {exported} storyboard index file set(s)")
    return 1 if failed else 0


def export_seedance_material_requirements(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    final_path = episode_dir / "final.txt"
    if not final_path.is_file():
        print(f"[error] missing final.txt: {episode_dir}", file=sys.stderr)
        return 2
    if episode_video_profile(episode_dir) not in {
        SEEDANCE25_LIVE_VERTICAL_PROFILE,
        SEEDANCE25_HORIZONTAL_XIANXIA_PROFILE,
    }:
        print(
            "[error] episode video profile does not support Seedance material handoff",
            file=sys.stderr,
        )
        return 2

    index_path = episode_dir / "storyboard_index.json"
    if not index_path.is_file():
        print(
            "[error] missing storyboard_index.json; run a full validate-episode first",
            file=sys.stderr,
        )
        return 2
    try:
        index_payload = read_json(index_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[error] invalid storyboard_index.json: {exc}", file=sys.stderr)
        return 2
    current_final_sha256 = hashlib.sha256(final_path.read_bytes()).hexdigest()
    if index_payload.get("source_hashes", {}).get("final_txt_sha256") != current_final_sha256:
        print(
            "[error] storyboard_index.json is stale; rerun full validate-episode",
            file=sys.stderr,
        )
        return 2
    asset_status_path = episode_dir / "asset_status.json"
    if not asset_status_path.is_file():
        print(
            "[error] missing asset_status.json; complete asset-reviewer and validate-assets first",
            file=sys.stderr,
        )
        return 2
    try:
        asset_status = read_json(asset_status_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[error] invalid asset_status.json: {exc}", file=sys.stderr)
        return 2
    if not (
        asset_status.get("status") == "done"
        and asset_status.get("reviewer_source") == "asset-reviewer"
        and asset_status.get("reviewer_pass") is True
        and asset_status.get("reviewer_issues_count") == 0
    ):
        print(
            "[error] asset_status.json has not passed the asset-reviewer gate",
            file=sys.stderr,
        )
        return 2
    try:
        requirements_path, local_materials_path = export_material_handoff(episode_dir)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    print(f"[exported] {requirements_path}")
    print(f"[exported] {local_materials_path}")
    return 0


def validate_seedance_materials(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    result = validate_material_handoff(episode_dir)
    if result["generation_ready"]:
        print("[passed] Seedance materials are generation-ready")
        return 0
    print("[not-ready] generation_ready=false")
    for issue in result["issues"]:
        print(f"- {issue}")
    return 1


def export_seedance_package(args: argparse.Namespace) -> int:
    episode_dir = args.episode_dir.resolve()
    output_path = args.output.resolve() if args.output else episode_dir / GENERATION_PACKAGE_FILE
    try:
        package_path = write_generation_package(episode_dir, output_path)
        package = read_json(package_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    print(f"[exported] {package_path}")
    if package.get("generation_ready") is True:
        print("[passed] generation_ready=true")
        if package.get("submit_allowed") is not True:
            print("[blocked] submit_allowed=false")
            for issue in package.get("submission_blockers", []):
                print(f"- {issue}")
            return 1
        return 0
    print("[not-ready] generation_ready=false")
    for issue in package.get("blocking_issues", []):
        print(f"- {issue}")
    return 1


def workflow_status(args: argparse.Namespace) -> int:
    if getattr(args, "run_dir", None) is not None:
        run_dir = args.run_dir.resolve()
        repo_root = Path(__file__).resolve().parent
        protocol_path = repo_root / "tests/fixtures/seedance25/probe-evidence/protocol-contract-v1.json"
        rubric_path = repo_root / "tests/fixtures/seedance25/probe-evidence/qa-rubric-v1.json"
        try:
            json_path, report_path, payload = write_probe_run_status(
                run_dir,
                protocol_path=protocol_path,
                rubric_path=rubric_path,
            )
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"[error] {exc}", file=sys.stderr)
            return 1
        print(f"[exported] {json_path}")
        print(f"[exported] {report_path}")
        if payload.get("workflow_validated") is True:
            print("[passed] workflow_validated=true")
            return 0
        print("[blocked] workflow_validated=false")
        for issue in payload.get("blocking_issues", []):
            print(f"- {issue}")
        return 1

    episode_dir = args.episode_dir.resolve()
    try:
        json_path, report_path = write_workflow_readiness(episode_dir)
        payload = read_json(json_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    print(f"[exported] {json_path}")
    print(f"[exported] {report_path}")
    first_blocker = payload.get("first_blocker")
    if first_blocker:
        print(f"[blocked] {first_blocker['layer']}: {first_blocker['reason']}")
        return 1
    print("[passed] all local readiness layers passed")
    return 0


def run_workspace(args: argparse.Namespace) -> int:
    print(
        "[error] disabled by design: Python must not launch agent CLIs. "
        "Open NEXT_STEPS.md and dispatch agents directly; use collect afterward.",
        file=sys.stderr,
    )
    return 2


def list_compatible_presets_command(args: argparse.Namespace) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    presets = compatible_visual_style_presets(args.video_profile)
    if not presets:
        print(f"No compatible visual style presets for {args.video_profile}.")
        return 0
    for preset in presets:
        print(f"{preset['id']}\t{preset['name']}\t{preset['description']}")
    return 0


def preview_workspace_config_command(args: argparse.Namespace) -> int:
    try:
        config = resolved_workspace_config(
            video_profile=args.video_profile,
            aspect=args.aspect,
            visual_style=args.visual_style,
            resolution=args.video_resolution,
            mode=args.mode,
            visual_style_preset=args.visual_style_preset,
            project_pack_id=args.project_pack_id,
            project_root=Path(__file__).resolve().parent,
        )
    except ValueError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2
    print(json.dumps(config, ensure_ascii=False, indent=2))
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare/collect CLI-agent storyboard workspaces.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Create a file-native agent workspace.")
    prepare.add_argument("--source", type=Path, required=True, help="Script file, collection docx, or directory.")
    prepare.add_argument("--prompt", type=Path, default=None, help="Generation prompt file.")
    prepare.add_argument("--review-skill", type=Path, default=None, help="Review skill file.")
    prepare.add_argument("--workspace-dir", type=Path, default=Path(DEFAULT_AGENT_RUNS_DIR))
    prepare.add_argument("--out-dir", type=Path, default=Path(DEFAULT_AGENT_OUTPUT_DIR))
    prepare.add_argument("--run-name", default=None)
    prepare.add_argument("--agent", choices=["codex", "qwen", "kimi", "claude"], default="codex")
    prepare.add_argument("--model", default=None, help="Optional CLI model override.")
    prepare.add_argument("--output-model-suffix", default="agent-cli")
    prepare.add_argument(
        "--video-profile",
        choices=sorted(VIDEO_PROFILE_CONFIG.keys()),
        default=DEFAULT_VIDEO_PROFILE,
        help=(
            "Target-video contract. The default preserves the existing Seedance 2.0 workflow; "
            "seedance-2.5-live-vertical enables the independent live-action 9:16 profile."
        ),
    )
    prepare.add_argument(
        "--video-resolution",
        choices=["480p", "720p"],
        default=None,
        help="Optional profile resolution override. Seedance 2.5 live vertical defaults to 720p.",
    )
    prepare.add_argument(
        "--visual-style",
        choices=sorted(VISUAL_STYLE_CONFIG.keys()),
        default="live-action",
        help="Visual medium style. Use 3d-cg for anime-style 3D CG short-drama workflows; default keeps the existing live-action short-drama style.",
    )
    prepare.add_argument(
        "--visual-style-preset",
        default=None,
        help="Optional named visual-style preset compatible with the selected video profile.",
    )
    prepare.add_argument(
        "--project-pack-id",
        default=None,
        help="Optional explicit project-pack ID; project packs are never inferred from titles.",
    )
    prepare.add_argument(
        "--aspect",
        choices=["vertical", "horizontal"],
        default="vertical",
        help="Storyboard aspect workflow. Use horizontal for the separate 16:9 horizontal generator/reviewer skills.",
    )
    # Keep in sync with prepare-agent.ps1 -Parallelism and the CLAUDE.md worker cap.
    prepare.add_argument("--parallelism", type=int, default=5)
    prepare.add_argument(
        "--mode",
        choices=["single", "scene"],
        default="single",
        help="single=generate/review a full episode; scene=split by scene and assemble.",
    )
    prepare.add_argument("--force", action="store_true")
    prepare.set_defaults(func=prepare_workspace)

    list_presets = subparsers.add_parser(
        "list-compatible-presets",
        help="List visual-style presets compatible with a video profile.",
    )
    list_presets.add_argument(
        "--video-profile",
        choices=sorted(VIDEO_PROFILE_CONFIG.keys()),
        required=True,
    )
    list_presets.set_defaults(func=list_compatible_presets_command)

    preview = subparsers.add_parser(
        "preview-workspace-config",
        help="Resolve workspace identity without creating files or directories.",
    )
    preview.add_argument("--video-profile", choices=sorted(VIDEO_PROFILE_CONFIG.keys()), required=True)
    preview.add_argument("--video-resolution", choices=["480p", "720p"], default=None)
    preview.add_argument("--visual-style", choices=sorted(VISUAL_STYLE_CONFIG.keys()), required=True)
    preview.add_argument("--visual-style-preset", default=None)
    preview.add_argument("--project-pack-id", default=None)
    preview.add_argument("--aspect", choices=["vertical", "horizontal"], required=True)
    preview.add_argument("--mode", choices=["single", "scene"], required=True)
    preview.set_defaults(func=preview_workspace_config_command)

    validate = subparsers.add_parser("validate-episode", help="Validate one episode final.txt.")
    validate.add_argument("--episode-dir", type=Path, required=True)
    validate.add_argument("--fix-metadata", action="store_true")
    validate.add_argument("--pre-check", action="store_true", help="Only run format/timing/quality checks; skip review artifact validation. Use to catch mechanical issues before calling the LLM reviewer.")
    validate.add_argument("--content-file", type=Path, default=None, help="Validate this file instead of final.txt (use with --pre-check to validate a draft).")
    validate.add_argument("--export-index", action="store_true", help="Also export storyboard_index.json/xlsx after full validation. Seedance 2.5 exports it automatically; other profiles default to txt-only.")
    validate.set_defaults(func=validate_episode)

    collect = subparsers.add_parser("collect", help="Collect final files from an agent run.")
    collect.add_argument("--run-dir", type=Path, required=True)
    collect.add_argument("--out-dir", type=Path, default=None)
    collect.add_argument("--export-index", action="store_true", help="Also collect storyboard index JSON/XLSX files. Seedance 2.5 collects them automatically; other profiles default to txt-only.")
    collect.set_defaults(func=collect_run)

    export_index = subparsers.add_parser("export-storyboard-index", help="Export storyboard_index.json/xlsx for episode cuts.")
    export_index.add_argument("--episode-dir", type=Path, default=None)
    export_index.add_argument("--run-dir", type=Path, default=None)
    export_index.add_argument("--fix-metadata", action="store_true")
    export_index.set_defaults(func=export_storyboard_index)

    export_materials = subparsers.add_parser(
        "export-seedance-material-requirements",
        help="Compile Seedance 2.5 logical material requirements and a local-material template.",
    )
    export_materials.add_argument("--episode-dir", type=Path, required=True)
    export_materials.set_defaults(func=export_seedance_material_requirements)

    validate_materials = subparsers.add_parser(
        "validate-seedance-materials",
        help="Validate local material hashes, ManJuWeb Ark results, limits, and readiness.",
    )
    validate_materials.add_argument("--episode-dir", type=Path, required=True)
    validate_materials.set_defaults(func=validate_seedance_materials)

    export_package = subparsers.add_parser(
        "export-seedance-package",
        help="Export a hash-bound Seedance 2.5 generation package.",
    )
    export_package.add_argument("--episode-dir", type=Path, required=True)
    export_package.add_argument("--output", type=Path, default=None)
    export_package.set_defaults(func=export_seedance_package)

    status = subparsers.add_parser(
        "workflow-status",
        help="Write machine and human readiness reports from current local evidence.",
    )
    status_targets = status.add_mutually_exclusive_group(required=True)
    status_targets.add_argument("--episode-dir", type=Path)
    status_targets.add_argument("--run-dir", type=Path)
    status.set_defaults(func=workflow_status)

    run = subparsers.add_parser("run", help="Disabled: Python does not launch agent CLIs.")
    run.add_argument("--run-dir", type=Path, required=True)
    run.set_defaults(func=run_workspace)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
