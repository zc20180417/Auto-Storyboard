{
  "pass": true,
  "summary": "两组均无硬错误，节奏紧凑，台词与动作匹配良好。",
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
      "evidence": "建筑商问话12字/2秒=6字/秒（warning），郑建国嚣张9字/2秒=4.5字/秒，合并拍桌+起身+两句台词22字/4秒=5.5字/秒，均在可接受区间。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组保持高档会所包间单一物理空间，组首明确列出郑建国已起身、建筑商仍落座，与第1组组尾衔接兼容。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中郑建国大舌头、拍桌、起身、走向门口等动作及四句台词全部保留，无删减或新增剧情。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "郑建国与建筑商均在组首空间锁定中拥有明确位置、身体朝向和可见状态。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾郑建国走向门口，与第2组组首郑建国已起身面向门口兼容；建筑商位置前后一致。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "烟雾缭绕转译为桌上空酒瓶和烟灰缸的可见细节；大舌头、拍桌等均可拍。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "建筑商问话12字/2秒=6字/秒，偏快但可接受",
      "evidence": "台词'郑总，督导组那边有麻烦吗？'共12字，镜头时长2秒，字秒比6.0",
      "fix": "可酌情延长至3秒使语速更舒缓"
    },
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "节奏",
      "problem": "拍桌+起身+两句台词合并为一个4秒镜头，动作密度较高",
      "evidence": "第1组6-10秒包含拍桌、起身及22字台词",
      "fix": "如生成效果跳帧，可考虑拆分为两个镜头"
    }
  ]
}

