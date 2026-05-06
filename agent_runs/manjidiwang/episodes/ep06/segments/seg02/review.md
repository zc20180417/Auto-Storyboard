{
  "pass": true,
  "summary": "三组均无硬错误，黑手伏击段落氛围紧张，空间锁定完整。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "龙建秋画外音14字/3秒=4.7字/秒，郑建国绝望11字/2秒=5.5字/秒，节奏合理。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组保持高层公寓落地窗前单一空间，黑手在阴影中拥有可生成位置。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "推下、坠落、擦鞋印等关键动作均保留，龙建秋电话台词完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "黑手在组首空间锁定中位于郑建国身后阴影中，拥有可生成位置。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾郑建国探身拉窗，与第2组组首郑建国上半身探出窗外兼容。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "烦躁转译为眉头紧皱、脸上泛红等可见表情；漆黑环境通过窗外微光表现。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "节奏",
      "problem": "推门并跌跌撞撞走向落地窗压缩至2秒，长动作展示偏快",
      "evidence": "2-4秒镜头包含推门与走向落地窗两个动作",
      "fix": "如条件允许可延长至3秒"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "郑建国绝望台词11字/2秒=5.5字/秒，情绪宣泄偏快",
      "evidence": "台词'龙爷……我跟你二十年……'共11字，镜头时长2秒",
      "fix": "可延长至3秒以配合绝望情绪的停顿感"
    }
  ]
}

