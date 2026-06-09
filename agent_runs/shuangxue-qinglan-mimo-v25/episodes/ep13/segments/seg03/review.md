{
  "pass": true,
  "summary": "第5-6组审核通过：赵强打圆场败露和周建国拍桌打断场景，台词忠实、节奏合理、空间连续。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "第5组39字有效台词/12秒=3.25字/秒。6-9秒段18字/3秒=6字/秒，9-12秒段15字/3秒=5字/秒，均在6.5字/秒硬上限内。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组组首空间锁定承接第5组组尾状态：周建国手掌抬起即将落下、沈清右手仍前伸、赵强站在木椅旁，三人位置和朝向连续。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "第5组保留原剧本全部台词和动作：赵强打圆场、沈清逼问借用/欠条/还款记录、赵强结巴回应均完整，台词顺序和说话对象正确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第5组4个时间段各承载一个主动作或连续对话节拍：赵强上前打圆场、沈清冷漠追问、沈清逼视+赵强结巴、沈清伸手+赵强结巴。无动作过载。",
      "fix_instruction": "无需修改，动作原子性合格。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组组尾沈清右手前伸、赵强眼神闪躲、周建国手掌抬起；第6组组首周建国手掌抬起即将落下、沈清右手仍前伸，状态完全连续。",
      "fix_instruction": "无需修改，组间状态连续。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组强节拍：周建国拍桌怒喝、发火台词、沈清反问。3个节拍分布在9秒内，每个时间段一个主动作，属同一冲突升级事件链。",
      "fix_instruction": "无需修改，强节拍分布合理。"
    }
  ],
  "issues": [],
  "warnings": []
}
