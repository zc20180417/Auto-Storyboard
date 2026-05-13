{
  "pass": true,
  "summary": "seg02保留陆凡带民警堵截、铐住爆破手甲并逼问炸药位置的关键信息，审核未发现硬问题。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "陆凡带两名民警从支巷冲出，民警甲亮手电喊“站住！警察！”，两名爆破手被堵住去路。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "evidence": "民警乙对爆破手甲问“炸药在哪？”，爆破手甲对民警乙回答炸药位置和五分钟引爆，真实对话对象明确。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "“在……在承重柱上，还有五分钟引爆！”约18字给6秒，结巴状态也有足够承载时间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡、民警甲、民警乙和两名爆破手均在组首或前半段入场后再行动和说话。",
      "fix_instruction": "若不通过，应把陆凡和民警的支巷入场放在说话前，或在组首锁定其位置。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第3组尾爆破手已被控制，第4组首爆破手甲双手被民警乙控制，手铐扣上动作有可见过渡。",
      "fix_instruction": "若不通过，应补充手铐从民警乙手中到爆破手甲手腕的动作。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒分为铐人、逼问、供出炸药三段，强节拍数量清晰，没有同时挤入额外事件。",
      "fix_instruction": "若不通过，应拆出逼问或供述段，避免手铐动作和长供述互相挤压。"
    }
  ],
  "issues": [],
  "warnings": []
}
