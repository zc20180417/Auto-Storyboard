{
  "pass": true,
  "summary": "seg05 保留陆凡撞开路障现身、倒计时对峙和血狼带人半包围逼近，结尾短动作组成立。",
  "checked_groups": ["第12组", "第13组", "第14组"],
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
      "group": "第12组",
      "type": "script_fidelity",
      "evidence": "越野车撞飞两道路障、急刹停下、陆凡推门下车并暴喝停引爆器，剧本动作和台词完整保留。"
    },
    {
      "group": "第13组",
      "type": "dialogue_pacing",
      "evidence": "周长海、陆凡、周长海、血狼四段交锋分配15秒，最长单段“在省城，我就是规矩！血狼，拦住他！”约17字用5秒，节奏不过快。"
    },
    {
      "group": "第14组",
      "type": "generation_density",
      "evidence": "第14组为8秒短动作余波，只表现血狼带五名精锐形成半包围和陆凡迎战反应，没有新增对白或复杂道具操作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第12组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡在组首位于黑色越野车驾驶位，先撞路障、停车、下车，再开口暴喝，出场顺序成立。",
      "fix_instruction": "若不通过，应在组首标明陆凡在车内或补充下车前不开口。"
    },
    {
      "group": "第13组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周长海对陆凡、陆凡对周长海、血狼对陆凡的现场对白对象全部明确。",
      "fix_instruction": "若不通过，应补齐每句对白对象。"
    },
    {
      "group": "第13组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "血狼组首手中持有计时器、短棍位于腰侧，12-15秒拔出短棍后第14组首复述短棍在手。",
      "fix_instruction": "若不通过，应补充短棍从腰侧拔出的过渡。"
    },
    {
      "group": "第14组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第13组尾血狼短棍在手、陆凡车旁对峙；第14组首复述两人位置并加入五名精锐逼近，连续清楚。",
      "fix_instruction": "若不通过，应在第14组首复述血狼、陆凡和短棍状态。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第14组",
      "rule": "generation_density",
      "problem": "8秒短组属于动作余波，成立但需交付时提示为短动作收尾。",
      "evidence": "第14组只承载半包围逼近和陆凡反应，无新增台词，符合6-9秒短动作余波例外。",
      "fix": "无需修复；若后续平台要求默认10秒，可与下一集开场动作合并。"
    }
  ]
}
