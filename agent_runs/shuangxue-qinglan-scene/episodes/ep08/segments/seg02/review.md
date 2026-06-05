{
  "pass": true,
  "summary": "seg02保留刘美娟取钱/ATM狡辩、沈清举老年机反驳和柜员确认手机银行转账，证据链清楚。",
  "checked_groups": ["第1组", "第2组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中刘美娟强词夺理、沈清举起老年机质问一分钟内网银转账和不会拼音的台词均完整保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "柜员“并不是取现，系统显示全是通过手机银行转账的。”约23个有效字给4秒，约5.75字/秒，属于可接受偏快说明。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第3组组尾写沈清持有流水账单和老年机，第4组组首延续同一归属，刘美娟仍在画面右侧偏后。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟对周桂兰狡辩，沈清对刘美娟质问，现场对白对象明确且没有假对象。",
      "fix_instruction": "若不通过，应补足每句对白对象。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "老年机从沈清口袋取出并一直在沈清右手，流水账单仍在左手，证据道具未跳变。",
      "fix_instruction": "若不通过，应写清老年机从沈清口袋取出后的归属。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "ATM借口、柜员查电脑说明、刘美娟被打脸反应、慌张否认四段动作分开，单段没有多个顺序主动作。",
      "fix_instruction": "若不通过，应拆开柜员查电脑和刘美娟反应。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只推进ATM借口被系统记录驳倒这一证据链，13秒内台词和反应容量足够。",
      "fix_instruction": "若不通过，应压缩刘美娟反应或拆成短余波组。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无Seedance说明、模板编号、参考图、占位符、广告语或批量模板句。",
      "fix_instruction": "若不通过，应删除所有工程说明和模板词。"
    }
  ],
  "issues": [],
  "warnings": []
}
