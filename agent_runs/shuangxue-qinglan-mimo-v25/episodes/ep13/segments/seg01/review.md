{
  "pass": true,
  "summary": "第1-2组审核通过：沈清与周美娟的账单对质场景，台词忠实、节奏合理、空间连续。",
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
      "evidence": "第1组35字有效台词/9秒=3.9字/秒，符合普通对白4.5字/秒目标。情绪对白'解释每一笔钱的去向'等按5.2字/秒估算，仍在合理范围。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "第1组组首空间锁定明确列出周家正屋客厅、长桌、三位人物位置和朝向，单一物理空间无跨场景。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留原剧本全部台词和动作：周美娟的'医药费'强辩、沈清的'你敢提吃药'冷笑、扔塑料袋动作均完整呈现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第1组全部为画面内真人开口对白，每句均写明'A对B说道'，无心声/画外音/电话音混用。",
      "fix_instruction": "无需修改，口型和声音承载正确。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾衔接写明沈清手指按账单、周美娟眼神闪躲身体后仰、周桂兰低头攥衣角；第2组组首空间锁定完全承接这些状态。",
      "fix_instruction": "无需修改，组间状态连续。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第2组每个时间段只承载一个主动作：0-3秒周美娟心虚开口，3-7秒周美娟拔高声调，7-9.5秒沈清冷笑反问，9.5-12秒沈清扔塑料袋。无动作过载。",
      "fix_instruction": "无需修改，动作原子性合格。"
    }
  ],
  "issues": [],
  "warnings": []
}
