{
  "pass": true,
  "summary": "seg01共3组，对峙场景完整，台词忠实，口型节奏合规，空间连续性良好。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组 0-3秒：'不许去！大半夜折腾老人，你安的什么心！'15字÷3秒=5.0字/秒，合规。3-5秒：'滚开！好狗不挡道！'7字÷2秒=3.5字/秒，快速斥责命令可接受。5-8秒：周建国入场台词12字÷3秒=4.0字/秒。8-10秒：8字÷2秒=4.0字/秒。均在合规范围。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组单一物理空间杂物间门口，组首空间锁定列出沈清、周建国、刘美娟三人位置和朝向，与第1组组尾状态连续。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组完整保留沈清推开刘美娟、拉周桂兰离开、周建国暴怒威胁、沈清头也不回回应等关键动作和台词，忠于原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内对白，写明'A对B说道'格式，无心声/画外音混用。",
      "fix_instruction": "无需修复，口型承载正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组12秒4个时间段，每个时间段只承载一个主动作或一个连续对话节拍，强节拍数合理。",
      "fix_instruction": "无需修复，密度合理。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组首空间锁定与第2组组尾衔接一致：沈清手中仍握银行卡、刘美娟位于门口、周建国站在门外。",
      "fix_instruction": "无需修复，状态连续。"
    }
  ],
  "issues": [],
  "warnings": []
}
