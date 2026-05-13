{
  "pass": true,
  "summary": "seg02 已按横屏 reviewer 对照剧本 3-2 审查，门外音、突然入室、护壶对峙、清明警告和黑水禁忌均保留，未发现 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "拐杖声先以门板震动和门外左侧走廊承载，爷爷隔门问“屋里哪来的水声？是不是管子漏了？”时使用门外过肩中景，声音来源明确。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "爷爷从画面左侧门口入场，天天在右侧护壶，6-12秒固定双人中景保持左压右的逼问轴线。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留爷爷不理解释、盯住透明水壶、眼神短暂清明以及台词“清水养它，脏水害它。”，天天紧张冒汗也符合原剧本。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "天天试探句约10字安排4秒，爷爷警告句约19字安排6秒，均留出严肃停顿和人物反应时间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "爷爷在门外不可见时先用拐杖声和门板震动承载，随后2.5-6秒显示他停在门口，关键人物可用性完整。",
      "fix_instruction": "若不通过，应增加门外爷爷或拐杖的可见载体。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "透明水壶从小桌旁被天天抱进怀里，3-6秒明确双臂护住壶口，后续逼问时仍在她胸前。",
      "fix_instruction": "若不通过，应补充天天拿起或护住水壶的动作过渡。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "过肩固定用于压迫视线，轻微推近用于爷爷眼神清明，双人固定用于台词和反应，运镜都服务剧情。",
      "fix_instruction": "若不通过，应删除空泛运动，改为说明固定或推近如何服务视线和口型。"
    },
    {
      "group": "第4组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天始终在画面右侧面向画左，爷爷始终在画面左侧面向画右，警告段未发生无过渡换边。",
      "fix_instruction": "若不通过，应补充换边过渡或保持左右站位一致。"
    }
  ],
  "issues": [],
  "warnings": []
}
