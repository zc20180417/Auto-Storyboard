{
  "pass": true,
  "summary": "seg02 两组保留陆凡潜近、诱敌和制服守卫，动作链与空间锁定通过。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留陆凡借杂草潜近、两名持棍混混巡视、掷石砸铁桶和守卫甲警觉喊话。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "守卫甲9字台词分配3秒并含转头警觉动作，字秒比约3字/秒，有动作支撑。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "evidence": "第2组11秒承载转身、陆凡跃出、双拳击颈、守卫倒地和短句收尾，动作链连续不过载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确废弃木材厂外、杂草、铁桶和两名守卫位置，未跨物理空间。",
      "fix_instruction": "若不通过，应补齐守卫位置、朝向和铁桶位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾两名守卫朝铁桶方向移动，第2组首两人背对陆凡并注意铁桶方向，衔接一致。",
      "fix_instruction": "若不通过，应在第2组组首复述两名守卫被铁桶声引开。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "陆凡精准击中两人颈侧、守卫软倒和陆凡冷酷台词均保留。",
      "fix_instruction": "若不通过，应恢复击中颈侧、软倒和原台词。"
    }
  ],
  "issues": [],
  "warnings": []
}
