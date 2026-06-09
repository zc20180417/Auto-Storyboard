{
  "pass": true,
  "summary": "第1组（母女温馨被打断）12秒5镜头，台词指向正确，画外音来源明确，空间单一，时间轴连续。",
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
      "evidence": "周桂兰11字/3秒=3.7字/秒，沈清10字/2.5秒=4.0字/秒，保安画外音14字/2秒=7.0字/秒（情绪喊话），周建国画外音11字/3秒=3.7字/秒。均在合理范围。"
    },
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "保安和周建国台词均通过画外音承载，明确写明声音来自门外，门板震动为可见载体。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "周桂兰哽咽台词、沈清轻拍回应、保安喊话、周建国骂声均完整保留，台词顺序与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "画外音承载正确，门板震动作为可见载体，周桂兰和沈清反应镜头不做口型。",
      "fix_instruction": "无需修改，音画分离正确。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "5个时间段各承载一个主动作或反应，属于同一事件链（温馨→打断）的自然推进。",
      "fix_instruction": "无需修改，密度合理。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "周桂兰台词、沈清回应、转头看门、保安画外音+门震动、周建国画外音+站起各占独立时间段，每个时间段一个主动作或一个连续对话节拍。",
      "fix_instruction": "无需修改，动作拆分清楚。"
    }
  ],
  "issues": [],
  "warnings": []
}