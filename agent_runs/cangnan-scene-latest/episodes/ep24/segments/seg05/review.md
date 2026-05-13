{
  "pass": true,
  "summary": "seg05保留周长海跪地崩溃、经侦车带走以及红点狙击的片尾悬念，动作与时长匹配。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "手机滑落、周长海跪进泥水、几千亿帝国台词和陆凡商会纠察专车台词均按原剧本顺序保留。"
    },
    {
      "group": "第2组",
      "type": "timing_math",
      "evidence": "第2组总时长12秒，时间段为0-3、3-8、8-12秒，连续且最后结束于标题总时长；全景警车入场压缩为3秒。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "第3组12秒承载悬崖边、红点锁定、陆凡低声判断和侧翻躲麻醉弹，四个节拍清楚，没有额外对白或道具堆叠。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周长海对陆凡喃喃说道，陆凡对周长海说道，两句现场对白对象明确。",
      "fix_instruction": "若不通过，应补足台词对象或说明自语状态。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部周长海跪地失神，陆凡居高临下；第2组首复述周长海跪在泥水里、陆凡在右侧，经侦车灯光从山路靠近。",
      "fix_instruction": "若不通过，应补周长海姿态和经侦车来源。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "红色激光点锁定心脏、陆凡说狙击手、侧方翻滚、麻醉弹击中原站立地面，片尾悬念完整保留。",
      "fix_instruction": "若不通过，应恢复红点位置、台词和麻醉弹落点。"
    }
  ],
  "issues": [],
  "warnings": []
}
