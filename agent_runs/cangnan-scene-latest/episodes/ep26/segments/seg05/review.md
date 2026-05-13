{
  "pass": true,
  "summary": "已审核26-5直升机空投段，走天上疑问、商会储备局解释、材料落地和工头确认均完整。",
  "checked_groups": [
    "第1组",
    "第2组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "江若晴“走天上？你什么意思？”、轰鸣声、捂嘴震惊、十几架直升机和陆凡储备局解释均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "工头两句台词分别约16字/3.5秒和约16字/3.5秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首列明工地空地、陆凡、江若晴、工头、直升机和吊挂集装箱，后续空投动作有明确可用对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "轰鸣声作为天空方向的外部声音出现，并配合人物抬头反应，没有误写成人物口型。",
      "fix_instruction": "如不通过，应补充声音来源和人物听见后的可见反应。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内空投下降、箱体落地、工头识别特种水泥和确认开工四个节拍分配明确。",
      "fix_instruction": "如不通过，应把识别材料和确认开工拆成两个镜头或延长工头反应。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "工头在第2组组首位于工人队伍前排，后续冲到箱体旁并发言之前可见。",
      "fix_instruction": "如不通过，应在组首或镜头前半段补足工头入场。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "未出现参考图、模板编号、自动分镜或视频延长等工程词。",
      "fix_instruction": "如不通过，应删除污染表达并保留直升机可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
