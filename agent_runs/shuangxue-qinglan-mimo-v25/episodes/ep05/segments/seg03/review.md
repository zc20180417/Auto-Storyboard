{
  "pass": true,
  "summary": "客厅对峙场景4组格式正确，台词忠实，对话指向清楚，短组用于承载戏剧节拍。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "沈清22字除以5秒等于4.4字每秒，刘美娟22字除以5.5秒等于4字每秒，单speaker均在合理范围内。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清25字除以4秒等于6.25字每秒，周建国14字除以4秒等于3.5字每秒，单speaker均在合理范围内。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "赵强电话台词（账上的钱千万别动，明天还有一笔要进来，稳住）完整保留，周建国举杯动作保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾沈清手指碗张嘴欲言，下一组组首沈清声音提高说出赡养费台词，状态自然衔接。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾周建国站着暴怒，下一组组首周建国站着手中握酒杯，状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾周建国酒杯举在半空，下一组组首周建国酒杯仍举在半空，状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵强电话音有手机贴在耳边的可见载体，且有捂嘴动作，正确承载电话音。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组砸碗加质问加刘美娟反驳，3个强节拍在13秒内合理分布。第2组赡养费揭穿加周建国暴怒，2个强节拍在8秒内合理。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
