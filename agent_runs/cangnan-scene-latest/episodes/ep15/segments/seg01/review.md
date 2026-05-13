{
  "pass": true,
  "summary": "seg01保留挖掘机损毁、强酸原因、违约金压力和宋子昂递文件逼迫的剧情，格式与台词承载通过。",
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
      "evidence": "工头对陆凡说“十台挖掘机全拉缸了！引擎废了！”，江若晴追问并保留“今天必须推平主干道”和“违约金高达一个亿”，强酸油箱原因也被保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "9.5-12.5秒承载江若晴约18字情绪台词，3秒内约6字/秒；12.5-15秒切到陆凡和工头反应，不存在超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首列明陆凡、江若晴、工头、宋子昂、律师团和迈巴赫位置，宋子昂已在车门旁可用，再走向施工空地并递文件。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "所有现场台词均写成工头对陆凡、江若晴对工头、工头对江若晴、江若晴对陆凡的明确对象。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对象。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "文件在组首由宋子昂持有，8-12秒递到陆凡胸前，陆凡12-14秒没有接文件，道具归属清楚。",
      "fix_instruction": "若不通过，应补充文件递出、接取或未接的可见状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有宋子昂入场、嘲讽、递文件和陆凡冷眼反应，14秒内强节拍可表演。",
      "fix_instruction": "若不通过，应拆分入场和递文件对白。"
    }
  ],
  "issues": [],
  "warnings": []
}
