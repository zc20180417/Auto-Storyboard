{
  "pass": true,
  "summary": "seg04 已审核通过，沈清后退举高手机、赵强投降求饶、周桂兰戳破明天借口和沈清限时转账均保留。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "沈清后退举手机、威胁按下、赵强僵住、赵强求饶被拆为4段，每段只有一个主动作或对白块。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "周桂兰“明天？你刚才不是说账上没钱吗？”和沈清两句限时转账台词均按原文保留。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "evidence": "第9组组尾沈清举着显示110的手机、赵强双手举起，第10组组首直接继承该状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机从第8组沈清右手延续到第9组，沈清后退举高后仍持有，赵强没有抢到。",
      "fix_instruction": "若手机归属不清，应在组首、动作段和组尾都补沈清右手持有。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "周桂兰约15字给4.5秒，沈清约7字给3.5秒，最后约15字给6秒，均未超过6.5字/秒。",
      "fix_instruction": "若台词偏快，应延长对应对白段或拆成短组。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定赵强、沈清、周桂兰、手机和红色房产证复印件，且不禁止原剧本必须发生的后退举手机。",
      "fix_instruction": "若禁止项与剧情冲突，应删除或改成手机未被抢到等具体风险。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、官方模板说明、模型自动处理、参考图或占位符等污染内容。",
      "fix_instruction": "若出现模型或模板词，应全部删去并改成自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
