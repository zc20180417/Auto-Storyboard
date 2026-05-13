{
  "pass": true,
  "summary": "seg01 共3组，保留裂缝失光、回家取水、父亲陶笛闪回；陶笛现实/闪回归属清楚，无 hard issue。",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "script_fidelity",
      "evidence": "第1组保留陶笛冰凉触感、小爪松开、天天道歉、青蓝光熄灭和救援喊话。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组明确天天空手进堂屋，只拿起竖直水壶；陶笛没有无来源跟随到堂屋。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组爸爸两句台词只在闪回院子里由爸爸现场开口，切回现实后没有爸爸声音或口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "小龙正式现身前只出现局部小爪和青蓝微光，未出现完整云宝、小龙或卡通萌宠感。",
      "fix_instruction": "若不通过，应删除完整小龙形象，只保留小爪、微光和人物反应。"
    },
    {
      "group": "第2组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "水壶在取水阶段保持竖直且壶盖拧紧，没有提前开盖、倾倒或洒水。",
      "fix_instruction": "若不通过，应补充水壶姿态、壶盖状态和天天双手持有的动作。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "闪回陶笛被明确限定为回忆道具，现实组尾只写天天抱水壶冲出堂屋，不混淆现实持有状态。",
      "fix_instruction": "若不通过，应区分现实道具和闪回道具，删除现实中凭空持有陶笛的描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
