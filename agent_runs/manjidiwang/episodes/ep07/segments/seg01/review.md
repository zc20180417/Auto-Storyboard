{
  "pass": true,
  "summary": "seg01分镜忠于原剧本，空间锁定清晰，场景过渡自然，个别镜头语速偏快已调整",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "田立民'战投部群龙无首，必须速定新总监'14字/3秒=4.67字/秒，情绪对白接近5.2阈值；苏长明'我提议李长庚，他业务最熟'13字/2秒=6.5字/秒，普通对白偏快但在可接受范围。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "集团高层会议室单一物理空间，田立民主位、苏长明右侧、朱天和左侧，三人物理位置与身体朝向明确，组首空间锁定完整。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "苏长明'你这是阻碍集团正常运转'、朱天和'我保留意见，直接上报总部督导组'等关键台词完整保留，人物对峙关系与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "田立民主位、苏长明右侧席位均在组首空间锁定中有明确画面位置与身体朝向，两人说话前已在场。",
      "fix_instruction": "无需修复，本项检查通过。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾苏长明说完台词看向田立民，第2组组首朱天和已在左侧席位握笔，三人位置与第1组一致，会议场景连续。",
      "fix_instruction": "无需修复，本项检查通过。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'气氛剑拔弩张'已转译为三人身体前倾、视线对峙、手指叩桌等可见动作；'田立民脸色微变'转写为面部特写与下颌收紧。",
      "fix_instruction": "无需修复，本项检查通过。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "苏长明'我提议李长庚，他业务最熟'13字/2秒=6.5字/秒，普通对白偏快；苏长明'董事长思虑周全，我同意'12字/2秒=6.0字/秒，偏快但仍在6-7字/秒可接受区间。",
      "evidence": "第1组第2镜3-5秒、第4镜8-10秒",
      "fix": "已调整为2秒，保留动作同步完成，节奏更紧凑"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "田立民'天和副董，你的意见呢'12字/2秒=6.0字/秒，普通对白偏快但在可接受区间。",
      "evidence": "第2组第2镜2-4秒",
      "fix": "保持2秒，转头动作与台词同步完成"
    }
  ]
}