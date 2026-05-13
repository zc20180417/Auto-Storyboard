{
  "pass": true,
  "summary": "seg05四组保留押解、面包车闯入、徐虎劫车、挟持江若晴和逃离收尾，审核通过。",
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
      "type": "space_locking",
      "evidence": "乡政府大院、警车、大楼、大门、赵大江、警察、陆凡、江若晴均在组首明确，车辆闯入有空间来源。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "徐虎持刀冲出逼退警察、喊快上车、赵大江趁乱钻进面包车均保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "江若晴求救约14字用3.5秒承载，陆凡怒喊8字用2秒承载，均低于6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "徐虎和打手在组首锁定为车内不可见位置，随后通过车门打开冲下车参与动作。",
      "fix_instruction": "若不通过，应补徐虎和打手在车内的可揭示位置。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "挟持、江若晴求救、陆凡喝止、推进车内和车辆起步拆成5段，13秒内没有压缩关键台词。",
      "fix_instruction": "若不通过，应把车辆起步拆到下一组。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部面包车开始冲向大门，第4组组首锁定车头朝大门外并继续逃离。",
      "fix_instruction": "若不通过，应补车头朝向和大门破损状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
