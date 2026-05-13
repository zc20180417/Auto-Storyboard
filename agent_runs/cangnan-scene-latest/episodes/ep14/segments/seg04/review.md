{
  "pass": true,
  "summary": "seg04 两组保留雨夜车场潜入、两名小弟对话、强酸倒入油箱、白烟和逃离，无硬问题。",
  "checked_groups": ["第7组", "第8组"],
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "组首明确临时车场、挖掘机、探照灯、小弟甲和小弟乙的位置及朝向，单一物理空间成立。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "小弟甲约17字用3.5秒，小弟乙约17字用3.5秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "塑料桶在小弟甲手中，油箱盖由小弟乙拧开，液体倒入后小弟甲盖紧油箱盖，道具归属与操作连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "大雨、挖掘机、黑雨衣、避开探照灯、十万报酬和强酸报废机器的台词均保留。",
      "fix_instruction": "若不通过，应恢复车场潜入和两句原台词。"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "刺鼻液体转译为油箱口液体、白烟、两人偏头和皱鼻梁等可见细节，不靠抽象气味承载剧情。",
      "fix_instruction": "若不通过，应把气味类信息改为白烟、动作和表情。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "开油箱、倒液体、白烟反应、盖紧喊撤、逃入树林分为5个节拍，13秒内动作链完整。",
      "fix_instruction": "若不通过，应拆出倒液体或逃离动作，避免强节拍过载。"
    }
  ],
  "issues": [],
  "warnings": []
}
