{
  "pass": true,
  "summary": "第4组通过审核，关键道具金镯子状态连续，动作拆段清楚，视频禁止项合理。",
  "checked_groups": ["第4组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周美娟7字÷2秒=3.5字/秒；赵强12字÷2.5秒=4.8字/秒；周美娟惨叫10字÷2.5秒=4.0字/秒；赵强赔笑14字÷4秒=3.5字/秒。均合理。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "金镯子从周美娟手腕→赵强撸下→赵强双手捧着→沈清纸巾垫着接过。每个状态变化都有可见过渡动作。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "4个时间段各承载一个主动作：护腕拒绝、站起扑去、撸镯子、递接镯子。赵强站起和扑去属于同一连续动作链。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项4条，均锚定本组具体人物和道具：金镯子消失、赵强未站起、沈清直接用手碰、手腕未掐红。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部：沈清目光锁定手腕、周美娟护腕后退、赵强地面抬头。第4组首：周美娟护腕后退、沈清视线盯手腕、赵强地面转头。连续无跳变。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金镯子状态从手腕→撸下→双手捧→纸巾接过，每步有可见过渡。纸巾从口袋掏出。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
