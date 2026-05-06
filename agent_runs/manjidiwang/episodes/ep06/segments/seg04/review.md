{
  "pass": true,
  "summary": "两组均无硬错误，办公室场景空间锁定完整，苏长明阴毒表情转译到位。",
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
      "evidence": "李长庚报信15字/3秒=5字/秒，苏长明问账目7字/2秒短台词豁免，节奏合理。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均保持集团总裁办公室单一物理空间，人物位置前后一致。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "督导组查封、空壳公司注销、推责朱天和等关键剧情信息全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏长明与李长庚均在组首空间锁定中拥有明确位置、身体朝向和可见状态。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾苏长明问账目，第2组组首李长庚低头回答，对话状态自然连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "眼神阴毒转译为死死盯视、嘴角冷硬等可见表情；冷酷转译为眼镜片冷光反射。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "苏长明讽刺13字/2秒=6.5字/秒，偏快但可接受",
      "evidence": "台词'邱瑞这只老狗，嗅觉真灵。'共13字，镜头时长2秒，字秒比6.5",
      "fix": "可酌情延长至3秒"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "苏长明阴毒13字/2秒=6.5字/秒，偏快但可接受",
      "evidence": "台词'该给朱天和找点麻烦了。'共13字，镜头时长2秒，字秒比6.5",
      "fix": "可酌情延长至3秒"
    }
  ]
}

