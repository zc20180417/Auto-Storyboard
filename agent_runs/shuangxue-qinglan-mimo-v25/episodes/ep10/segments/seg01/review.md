{
  "pass": true,
  "summary": "第10集10-1段分镜通过审核，台词指向明确、空间单一、时间节奏合格。",
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
      "type": "dialogue_pacing",
      "evidence": "第1组14秒，各段台词字秒比均在6.5以内：刘美娟16字/2.5秒=6.4、沈清12字/2.5秒=4.8、刘美娟19字/3秒=6.33、赵强16字/3秒=5.33、沈清18字/3秒=6.0。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首空间锁定与第1组组尾衔接一致：沈清手持银行流水单、刘美娟站在原位心虚、周桂兰在左侧偏后。同场景无空间跳变。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "刘美娟挡赵强前的急中生智、沈清冷漠反驳、赵强附和、沈清追问收益等关键台词和动作均完整保留，说话对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面人物现场开口对白，每句写明说话人和对象，无心声/画外音混用。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组为连续对白交锋节拍，每段只承载一个说话人的对白或反应，无动作过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾：沈清手持流水单、刘美娟站原位。第2组组首：沈清持流水单、刘美娟眼神躲闪。状态连续。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
