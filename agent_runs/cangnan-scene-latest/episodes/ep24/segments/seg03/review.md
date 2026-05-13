{
  "pass": true,
  "summary": "seg03保留起爆器被控制、排爆拆除和陆凡周长海对峙威胁的主线，单空间和道具状态连续。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "起爆器被夺、民警用对讲机通知排爆组、炸弹红灯闪烁后被安全拆除，三项关键动作均在同组内按原顺序呈现。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组四段对白总量分散在0-15秒，周长海两句威胁各用4秒左右，陆凡收尾用4秒，未出现台词过快。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首写明炸弹红灯已熄灭、周长海跪伏受控、陆凡站在画面右侧，承接第1组拆弹完成后的同一工地空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "民警对讲机台词由画面内民警现场开口承载，对讲机作为可见载体出现，没有误写成无来源声音。",
      "fix_instruction": "若不通过，应补对讲机载体或改写声音来源。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "周长海关于全省经济命脉和股市崩盘的两句威胁未删改，陆凡今天先去公安局的回应保留。",
      "fix_instruction": "若不通过，应恢复原台词顺序和原文。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组主要是跪地对峙台词，没有额外押送、拆弹或新道具操作叠加，15秒容量合理。",
      "fix_instruction": "若不通过，应拆出台词或减少非关键动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
