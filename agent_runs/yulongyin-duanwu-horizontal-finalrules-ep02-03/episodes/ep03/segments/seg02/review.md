{
  "pass": true,
  "summary": "seg02 passed: door sound, half-latched door, kettle holding, grandfather warning, and black-water taboo are coherent and physically continuous.",
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
      "type": "handoff_continuity",
      "evidence": "第1组承接上一段水壶竖直、壶盖半拧、门闩虚扣的已建立状态，并把爷爷作为本组首次由门外拐杖声接近。"
    },
    {
      "group": "第2组",
      "type": "physical_continuity",
      "evidence": "第2组门闩先因连续推门从半截扣槽滑脱，房门才被推开，明确不是破门或撞门。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留爷爷“清水养它，脏水害它”和“端午前，绝不能让它碰外面那些黑水”两句关键信息。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "门外拐杖声和爷爷门外问话都有清楚来源，天天在门内屏住呼吸，没有错误开口。",
      "fix_instruction": "若不通过，应补充门外声源、门板载体和屋内人物反应。"
    },
    {
      "group": "第2组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "第2组写清半虚扣门闩被震松、门缝扩大、爷爷从左侧进入；老人动作强度符合普通推门，不是暴力破门。",
      "fix_instruction": "若不通过，应改为普通进入或紧张闯入的合理强度，补充门闩滑脱过程。"
    },
    {
      "group": "第3组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "第3组黑水只通过台词成为禁忌信息，没有主动生成黑水画面，也没有夸张腐蚀或怪物化。",
      "fix_instruction": "若不通过，应删除未建立的黑水画面，或把黑水写成真实克制的来源、路径、影响、结果。"
    }
  ],
  "issues": [],
  "warnings": []
}
