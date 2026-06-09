{
  "pass": true,
  "summary": "第1组格式正确，台词忠实，空间单一，对话指向清楚。",
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
      "evidence": "沈清7字除以5秒等于1.4字每秒，周建国18字除以5秒等于3.6字每秒，均在合理范围内。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组发生在周家正屋客厅，单一物理空间，无跨场景。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清问（周叔，我妈呢？）、周建国回答（她老了嫌吵）、沈清转身朝后厨走去，关键台词和动作完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周建国问道，周建国对沈清说道，对话指向明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈清、周建国、刘美娟均在组首空间锁定中有明确位置和朝向。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只有一个主动作：全景宴会、刘美娟敬酒、沈清扫视、沈清问周建国。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
