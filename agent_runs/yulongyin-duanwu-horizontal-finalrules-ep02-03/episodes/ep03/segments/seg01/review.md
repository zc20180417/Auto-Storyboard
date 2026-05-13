{
  "pass": true,
  "summary": "seg01 passed: bedroom feeding, naming, and water-mist beats preserve the script while keeping kettle, lid, naming state, and mouth-sync continuity clear.",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "prop_continuity": "checked",
    "physical_continuity": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "evidence": "第1组把门闩虚扣、走到书桌、取馒头、开盖、掰碎投喂拆成4个镜头，没有把锁门/走位/取物/开盖/投喂/台词塞进同一镜头。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组命名前使用“小龙”，命名台词“以后就叫你云宝吧”之后才写“刚被命名的云宝”，没有提前污染称呼。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "第4组心声“凉凉的，就像真正的雨一样。如果是大暴雨就好了”明确写天天嘴唇闭合不做口型，声音来源与画面口型分离。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "水壶始终竖直放在桌面，壶盖先被拧开并放在右侧桌面，馒头渣从壶口落入，没有出现液体容器姿态矛盾。",
      "fix_instruction": "若不通过，应补清容器姿态、支撑点、盖子来源和开合过渡。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本的命名台词完整保留，且命名前后“小龙/云宝”状态清楚。",
      "fix_instruction": "若不通过，应把命名前称呼统一为小龙，命名台词之后再使用云宝。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第4组从壶盖放在右侧桌面，过渡到天天拿起壶盖并虚拧半圈，组尾承接的壶盖状态由镜头内动作建立。",
      "fix_instruction": "若不通过，应在镜头描述中补充拿起、盖回或虚拧动作，不能让盖子凭空恢复。"
    }
  ],
  "issues": [],
  "warnings": []
}
