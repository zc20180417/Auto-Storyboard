{
  "pass": true,
  "summary": "seg05已对照原剧本完成审核，陆凡道谢、林夏指出货运道路问题、徐虎建材垄断、宋氏集团风险和陆凡OS决意均保留，无硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "第1组保留陆凡揉手腕并感谢林夏、林夏指出鱼干卖了但路烂货运不出、陆凡准备修路拓宽主干道。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-5秒承载林夏关于沙石和徐虎建材垄断的台词，5-8秒承载陆凡会会徐虎，8-12秒承载宋氏集团提醒，均未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组陆凡OS写成内心旁白，画面中陆凡嘴唇闭合不做口型，避免把心声误作现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组固定在水头村河滩，陆凡和林夏位置、朝向、手腕红印和远处道路均在组首交代清楚。",
      "fix_instruction": "若同组跨到村口或办公室，应拆组或明确转场。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林夏担忧沙石和徐虎建材垄断，陆凡冷笑说亲自会会徐虎，林夏提醒宋氏集团，台词顺序和人物关系未改变。",
      "fix_instruction": "若遗漏宋氏集团或徐虎垄断，应补回对应台词和反应。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组为8秒短组，只承载片尾心声和远方道路意象，属于片尾意象/短情绪收束，没有硬凑到10秒。",
      "fix_instruction": "若需要扩展，应只增加陆凡望路和林夏反应，不新增剧情动作。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "timing_math",
      "problem": "8秒短组低于默认10秒。",
      "evidence": "该组只承载陆凡OS和远方盘山公路意象，属于片尾意象和短情绪收束。",
      "fix": "整集终审确认短组理由成立即可。"
    }
  ]
}
