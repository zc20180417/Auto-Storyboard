{
  "pass": true,
  "summary": "seg02已完成真实横屏审核，拐杖声、闯入、逼问、清水脏水提示和端午黑水警告均按原剧本保留。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
  ],
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "门外拐杖声以走廊左侧拐杖敲地和天天门内反应承载，爷爷疑问对白明确对门内天天说，声音来源清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "爷爷在左侧对右侧的天天逼问，天天在右侧对左侧爷爷结巴解释，真人对白对象明确，没有自语或假对象。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "“清水养它，脏水害它。”和“爷爷，你认识它对不对？”均按原文和顺序保留，爷爷短暂清明与天天冷汗反应没有漏掉。"
    },
    {
      "group": "第4组",
      "type": "horizontal_composition",
      "evidence": "爷爷在左侧门口阴影、天天在右侧书桌旁抱壶，中间留出横向距离，端午黑水警告的压迫关系可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确走廊左侧、卧室门右侧和门内天天位置，门外到门内是连通门口空间，不是无标识跨场景。",
      "fix_instruction": "若不通过，应把门口与门内关系写成同一门槛空间，并补足声音来源。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从上组被天天抱起延续到胸前，爷爷拐杖从门口进入卧室后仍在手中，道具归属连续。",
      "fix_instruction": "若不通过，应补充天天抱起水壶或爷爷拐杖位置的过渡。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "“清水养它，脏水害它。”按一字一顿承载2.5秒，天天追问约10字承载3秒，没有超过6.5字/秒硬上限。",
      "fix_instruction": "若不通过，应延长对白镜头或拆分到相邻反应镜头。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载爷爷停在门口、警告台词和天天愣住三个节拍，11秒内没有过载。",
      "fix_instruction": "若不通过，应删去非剧本新增动作或拆开警告反应。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、占位符、自动分镜或其他工程说明词。",
      "fix_instruction": "若不通过，应将污染词替换为可见动作和自然声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
