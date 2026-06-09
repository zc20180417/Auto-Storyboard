{
  "pass": true,
  "summary": "第1组（闯入被截）14秒5镜头，闯入→蹲下→隔离→律师警告→周建国反驳，同一事件链连续推进，台词节奏偏快但在范围内。",
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
      "evidence": "律师24字/4秒=6.0字/秒（偏快但在6.5内），周建国18字/3秒=6.0字/秒（情绪喊话可接受）。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "evidence": "闯入、蹲下、隔离、律师警告、周建国反驳各占独立时间段，每个时间段一个主动作。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "周建国带周美娟赵强闯入、律师警告寻衅滋事录像取证、周建国反驳家事，均完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "5个时间段属于同一闯入事件链的连续阶段，每个时间段只承载一个主动作，总时长14秒合理。",
      "fix_instruction": "无需修改，事件链密度合理。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "单一物理空间（宴会厅门口内侧），组首空间锁定列出所有5位在场人物及其位置和朝向。",
      "fix_instruction": "无需修改，空间锁定完整。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "律师对周建国说道、周建国对律师喊道，对话指向明确，无假对象。",
      "fix_instruction": "无需修改，对话指向正确。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "律师台词6.0字/秒、周建国台词6.0字/秒，偏快但未超6.5硬上限。",
      "evidence": "24字/4秒=6.0字/秒，18字/3秒=6.0字/秒",
      "fix": "可考虑延长至15秒降低密度。"
    }
  ]
}