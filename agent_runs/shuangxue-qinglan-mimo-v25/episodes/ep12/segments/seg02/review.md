{
  "pass": true,
  "summary": "seg02 两组均通过审核，台词节奏、空间锁定、道具连续性均无硬伤。",
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
      "evidence": "周桂兰痛哭19字/3.5秒=5.43字/秒（情绪对白），周建国怒声20字/4秒=5.0字/秒（情绪对白），周建国拍桌14字/2.5秒=5.6字/秒（情绪对白），均在4.5-6.5范围内。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清怒斥18字/3.5秒=5.14，沈清死盯19字/3.5秒=5.43，周建国暴跳如雷18字/3.5秒=5.14，沈清不退缩17字/3.5秒=4.86，均在4.5-6.5范围内。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "周桂兰'为什么啊！那是清清给我留的活命钱啊！'完整保留，周建国'哭什么哭！你嫁进周家，吃喝拉撒哪样不花钱！'和'家里开销这么大，用你点钱怎么了！'完整保留，拍桌子动作保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内真人开口，写明了谁对谁说。周桂兰对周建国痛哭，周建国对周桂兰怒声，均指向明确。",
      "fix_instruction": "无需修改，口型和指向均正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组3个时间段，2个强节拍（周桂兰崩溃、周建国拍桌）。第2组4个时间段，2-3个强节拍（沈清怒斥连击、周建国暴怒反击）。每时间段只一个主动作，无过载。",
      "fix_instruction": "无需修改，强节拍密度合理。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "seg01组尾周桂兰站立发抖，seg02组首周桂兰站立双手握在胸前发抖，状态连续。委托书、周建国位置均连续。",
      "fix_instruction": "无需修改，组间状态衔接完整。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作或一个连续对话节拍。周建国暴跳如雷的台词和身体动作（挺直、握拳）在同一时间段内同步完成，不构成多主动作过载。",
      "fix_instruction": "无需修改，动作拆分清晰。"
    }
  ],
  "issues": [],
  "warnings": []
}
