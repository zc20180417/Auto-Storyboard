{
  "pass": true,
  "summary": "第1组格式正确，台词忠实，厨房空间单一，音画分离正确。",
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
      "evidence": "沈清4字除以3秒等于1.3字每秒，周桂兰9字除以2秒等于4.5字每秒，沈清19字除以4秒等于4.75字每秒，均在合理范围内。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组发生在周家厨房，单一物理空间，组首锁定周桂兰在灶台旁弓腰端碗。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "周桂兰吃剩鱼骨头、沈清夺筷子喊（妈！别吃了！）、沈清说（外面吃鲍鱼海参）、端碗走出，关键动作和台词完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周桂兰喊道，周桂兰对沈清说道，沈清对周桂兰说道，对话指向明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "缺口的碗从周桂兰手中到沈清端起，筷子从周桂兰手中掉落，道具状态变化清楚。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只有一个主动作：全景厨房、特写筷子、冲进夺筷子、周桂兰反应、沈清哽咽端碗走。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
