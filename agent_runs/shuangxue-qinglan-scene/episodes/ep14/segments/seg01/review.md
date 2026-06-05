{
  "pass": true,
  "summary": "seg01 保留周美娟和赵强否认证据、沈清转向周桂兰取卡的关键剧情，格式和道具连续性通过。",
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
      "type": "script_fidelity",
      "evidence": "原剧本中周美娟的“银行记录算什么”“也许是别人填错了号码”、赵强的两句附和和沈清的“不见棺材不掉泪”均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "旧银行卡先在周桂兰贴身处，6-10秒由周桂兰取出并递给沈清，组尾明确旧银行卡已经在沈清手里。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组 9-12秒承载赵强和沈清两句短对白，约24字/3秒，按争吵快节奏略紧但未超过硬上限，且两句为连续交锋。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周美娟、赵强、沈清的现场对白均写明对沈清或对两人的真实对象，没有假对象。",
      "fix_instruction": "若后续改写，应继续保留每句真人对白的说话对象。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "沈清走到周桂兰身边、询问、周桂兰递卡分为三个时间段，递卡是单一主动作链。",
      "fix_instruction": "若加入其他动作，不要把抢卡或冲突动作并入递卡镜头。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项仅针对旧银行卡归属和赵强抢卡风险，包含旧银行卡、沈清、周桂兰、赵强等本组锚点。",
      "fix_instruction": "若删改视频禁止项，应保留本组关键道具归属约束。"
    }
  ],
  "issues": [],
  "warnings": []
}
