{
  "pass": true,
  "summary": "seg01 保留清房、名牌包争执、法警执行和赵强记仇，格式与节奏可交付。",
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
      "evidence": "周美娟约22字用4秒，约5.5字/秒；法警约18字用4秒，约4.5字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留工人搬沙发柜子、客厅空荡粉尘、周美娟护名牌包和法警要求配合执行。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组仍在周家客厅，组首复述赵强、沈清、周美娟、法警和工人的位置，承接第1组尾部。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "搬家具、客厅见底、周美娟喊话、法警回应分成四个时间段，每段主动作清楚。",
      "fix_instruction": "若不通过，应拆开搬运和对话，避免同一时间段塞入多段主动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵强对白写明对沈清咬牙说道，没有假对象或口型混用。",
      "fix_instruction": "若不通过，应补真实对话对象。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周美娟名牌包、法警、沈清、沙发柜子，数量4条且不与剧情矛盾。",
      "fix_instruction": "若不通过，应替换无锚点或泛泛禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
