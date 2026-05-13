{
  "pass": true,
  "summary": "seg05保留审问龙天傲位置、矿洞炸药信息、陆凡夺通讯器、江若晴警觉工人风险和陆凡赶往矿洞。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "陆凡问“龙天傲在哪？”，毒刺交代矿洞工程炸药和炸断地下水脉，陆凡打晕毒刺并夺通讯器，均与原剧本一致。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "evidence": "江若晴台词约21字用4秒，约5.25字/秒；陆凡台词约21字用4秒，约5.25字/秒，情绪紧急但未超过6.5字/秒。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "evidence": "第9组尾部陆凡手持通讯器、江若晴脸色发白，第10组组首直接复述该状态，毒刺昏倒位置也连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "战术通讯器先挂在毒刺胸前背心上，11-14秒陆凡打晕毒刺后从背心上夺过，归属转移可见。",
      "fix_instruction": "若缺少转移，应补写陆凡从毒刺身上夺过通讯器。"
    },
    {
      "group": "第10组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "江若晴对陆凡发抖说道工人风险，陆凡对江若晴果断下令拉响警报并说明去矿洞，对话对象明确。",
      "fix_instruction": "若对象不清，应补为“江若晴对陆凡说道”和“陆凡对江若晴说道”。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "工人风险台词、陆凡命令、转身冲出三类强节拍分4段14秒，未把矿洞赶赴动作与长台词挤在同一短段。",
      "fix_instruction": "若过载，应把陆凡出门作为独立尾部动作段。"
    }
  ],
  "issues": [],
  "warnings": []
}
