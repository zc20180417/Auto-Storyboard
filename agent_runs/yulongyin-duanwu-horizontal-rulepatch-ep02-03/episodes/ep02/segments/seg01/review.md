{
  "pass": true,
  "summary": "seg01 三组保留裂缝失光、回家取水和父亲闪回，横屏结构、时长、道具连续性和项目专属称谓均可通过。",
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
      "evidence": "第1组保留陶笛冰凉触感、小爪松开坠回黑暗、天天两句原台词和青蓝光熄灭，没有提前让小龙完整出现。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组写清天天起身时右手扫过陶笛但没有拿走，组尾也说明陶笛和裂缝留在河床方向，道具归属没有跳变。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组爸爸只出现在闪回里并现场说出两句台词，回到现实时没有让爸爸画外继续发声，声音来源清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "小龙只以半透明小爪和青蓝微光出现，符合项目包正式现身前只露局部反应的要求。",
      "fix_instruction": "若不通过，应删除完整小龙形象，只保留小爪、微光、影子或天天反应。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "裂缝和陶笛保持在画面左后方，天天朝画面右上方旧屋方向跑，救援路线清楚。",
      "fix_instruction": "若不通过，应补充天天奔跑方向、裂缝留置方向和村路参照物。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "爸爸两句台词分别由 5 秒和 4 秒镜头承载，有效字秒比低于 6.5，且现实动作没有挤压闪回对白。",
      "fix_instruction": "若不通过，应拆分闪回台词或延长承载镜头，不能删改父亲叮嘱。"
    }
  ],
  "issues": [],
  "warnings": []
}
