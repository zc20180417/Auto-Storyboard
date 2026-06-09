{
  "pass": true,
  "summary": "第5-6组审核通过，周美娟被捕和沈清嘲讽带走场景连续性良好。",
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
      "evidence": "警察指控23字/4.5秒=5.1字/秒，周美娟哭喊17字/3.5秒=4.9字/秒，警察驳斥25字/4秒=6.25字/秒，均未超过6.5硬上限。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "evidence": "第5组组尾两人均戴手铐，第6组组首手铐状态一致。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "警察台词和周美娟台词均完整保留，未删改关键内容。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作：警察宣读指控、周美娟哭喊、警察驳斥、手铐铐上。",
      "fix_instruction": "若不通过，应拆分时间段。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "9秒内3个强节拍各占独立时间段，无过载。",
      "fix_instruction": "若不通过，应拆分或弱化非关键动作。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手铐状态从第5组到第6组连续一致。",
      "fix_instruction": "若不通过，应补充手铐状态过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
