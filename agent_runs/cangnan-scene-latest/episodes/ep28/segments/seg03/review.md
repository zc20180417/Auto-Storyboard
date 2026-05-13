{
  "pass": true,
  "summary": "seg03保留陆凡破窗入场、怒斥毒刺、毒刺下令和陆凡翻滚借办公桌掩护。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "character_availability",
      "evidence": "组首写明战术绳索从窗外垂下、陆凡位于窗外雨幕中，随后3-6秒破窗入场，先入场后喊话。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“把你的手拿开！”约7字用3秒，毒刺“动手！”约2字与收手转向动作共同占3秒，没有超速或拖慢。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "两名安保精英冲上前、陆凡战术翻滚、利用厚重实木办公桌作为掩体、几人瞬间缠斗均按原剧本保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本段均为现场开口对白，陆凡对毒刺喊话、毒刺对外籍安保精英喊话，声音来源明确。",
      "fix_instruction": "若改为画外音，应写明声音来源并避免画面人物错误口型。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "两名队员冲上前、陆凡翻滚到办公桌后、缠斗爆发分为3段11秒，复合动作链有4秒承载。",
      "fix_instruction": "若翻滚和缠斗同段过短，应延长翻滚段或拆组。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组结尾陆凡挡在江若晴前方、毒刺下令；第6组组首延续陆凡、江若晴、毒刺和门口队员的位置关系。",
      "fix_instruction": "若不连续，应补出毒刺、江若晴和队员在组首的具体位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
