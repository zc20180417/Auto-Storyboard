{
  "pass": true,
  "summary": "两组均无硬错误，食堂场景空间锁定完整，邱瑞震怒段落节奏有力。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "邱瑞问7字/2秒短台词豁免，小王答10字/2秒=5字/秒，小王报信13字/2秒=6.5字/秒（warning），节奏可控。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均保持督导组驻地食堂单一物理空间，组首空间锁定完整，无跨场景硬切。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "邱瑞冷笑、拍桌、查封账目、调取记录等台词和动作全部保留，无删减。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "邱瑞与小王均在组首空间锁定中拥有明确位置和朝向。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾小王递报告，第2组组首小王手中仍拿报告，状态连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "蛋壳碎裂转译为特写镜头中手指捏碎蛋壳的可见细节；低声、沉声通过演员语气和表情体现。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "小王报信13字/2秒=6.5字/秒，偏快但可接受",
      "evidence": "台词'组长，郑建国昨晚跳楼了。'共13字，镜头时长2秒，字秒比6.5",
      "fix": "可酌情延长至3秒使语速更舒缓"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "邱瑞命令13字/2秒=6.5字/秒、果断12字/2秒=6字/秒，偏快但可接受",
      "evidence": "连续命令台词字秒比分别为6.5和6.0",
      "fix": "如节奏过赶，可各延长1秒"
    }
  ]
}

