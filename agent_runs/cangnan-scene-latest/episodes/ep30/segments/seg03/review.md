{
  "pass": true,
  "summary": "seg03保留调解队到场、报到、依法要求解散、龙天傲撤离及江若晴追问，审核通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "三辆白色中巴车、龙国商会纠纷调解字样、三十名制服调解员、执法记录仪、防暴盾和橡胶棍均保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "调解队长条例台词约39字给6秒，约6.5字/秒，处于硬上限但未超过；龙天傲“陆凡，算你狠！撤！”8字给3秒充足。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "evidence": "第4组为8秒短承接，承载撤离余波和两句短问答，属于短动作余波和承接反应，时间轴0-2、2-4、4-8连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "调解队长对陆凡报到，龙天傲对陆凡震惊发问，现场对象明确。",
      "fix_instruction": "若调解队长台词未指向陆凡，应补成对陆凡说道。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "调解队长按商会条例要求龙方解散，龙天傲咬牙撤走，手下后退并看向龙天傲，因果顺序正确。",
      "fix_instruction": "若撤离早于条例警告，应调整顺序。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾龙天傲走向越野车、调解队隔离秩序，第4组首黑车远去、调解员仍维持秩序，状态连续。",
      "fix_instruction": "若第4组忽略调解队或撤离状态，应补大门外秩序维持。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "timing_math",
      "problem": "第4组为8秒短组。",
      "evidence": "该组只承载撤离余波和江若晴、陆凡两句短问答，合并到第3组会造成条例警告、撤离、问答过载。",
      "fix": "保持短承接即可，交付时说明它是撤离后的短动作余波与反应。"
    }
  ]
}
