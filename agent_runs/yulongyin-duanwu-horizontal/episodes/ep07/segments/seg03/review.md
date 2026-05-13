{
  "pass": true,
  "summary": "祠堂门前冲突段已完成审核，强拆威胁、爷爷护门、村民劝说和被架开均忠于剧本。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "爷爷在画面左中部门前，胡永贵和拿铁棍手下在画面右侧，村民退在背景两边，左右阵营清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "爷爷对胡永贵怒吼，胡永贵对爷爷冷笑回击，村民甲对爷爷劝说，所有现场对白都有真实对象。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留爷爷“钱能买命，买不了天公降雨！”、胡永贵挥手、手下强行将爷爷架开，剧情因果未改。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "胡永贵、爷爷、手下、村民均在组首空间锁定中出现或作为背景可见，发声和行动人物可用。",
      "fix_instruction": "若不通过，应把关键说话人和被说话对象补入组首空间锁定。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "爷爷、胡永贵、村民甲三句对白分别用3秒、3.5秒、3秒承载，均未超过6.5字/秒硬上限。",
      "fix_instruction": "若不通过，应延长对应台词镜头或拆出反应镜头。"
    },
    {
      "group": "第3组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "手下从胡永贵右后方上前，把爷爷从左侧木门前拖向右侧，木门暴露的空间结果可见。",
      "fix_instruction": "若不通过，应补充手下上前方向、爷爷被拖离门前的位置变化。"
    }
  ],
  "issues": [],
  "warnings": []
}
