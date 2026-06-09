{
  "pass": true,
  "summary": "第1组清空客厅场景，台词节奏合格，空间锁定完整，对话指向正确。",
  "checked_groups": ["第1组"],
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
      "evidence": "周美娟台词16字/3.5秒=4.57字/秒，法警台词14字/2.5秒=5.6字/秒，赵强台词12字/5秒=2.4字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本三句台词完整保留，说话对象正确（周美娟对工人、法警对周美娟、赵强对沈清），关键动作（搬家具、抓名牌包）均已体现。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间周家客厅，组首锁定包含全部4名在场人物位置和朝向，未出现跨空间问题。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "三句台词均为画面内真人开口对白，无心声/画外音混用，对话指向明确。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "2个强节拍（搬运+对峙），时间段清晰，每段一个主动作，无过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作/对话节拍，无多动作挤入同一时间段。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}

