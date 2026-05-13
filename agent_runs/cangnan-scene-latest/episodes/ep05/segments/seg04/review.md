{
  "pass": true,
  "summary": "seg04已完成道路封堵段审核，拦路、亮刀、报官安排和录像反制均按原剧本保留。",
  "checked_groups": ["第8组", "第9组", "第10组", "第11组"],
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
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "第8组保留农用三轮车被迫停下、巨石堵路、黄毛打牌、陆凡请求让路和黄毛声称塌方。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "evidence": "第9组组首写刀藏在黄毛腰侧，3-7秒由黄毛拔出刀，刀的归属和出现过程清楚。"
    },
    {
      "group": "第11组",
      "type": "dialogue_pacing",
      "evidence": "第11组0-6秒约29字情绪对白，6秒承载低于6.5字/秒；后两句短对白分别4秒和3秒，节奏可表演。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第8组只发生在水头村土路，组首列出三轮车、村民、巨石、黄毛和陆凡位置。",
      "fix_instruction": "若新增村委或办公室画面，应拆组或明确屏幕/蒙太奇。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "陆凡质疑石头整齐、黄毛拔刀威胁、牛大春提醒徐虎的人均保留原词和顺序。",
      "fix_instruction": "若删掉牛大春提醒徐虎，应恢复该台词以保持人物关系。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第9组尾部牛大春拉住陆凡，第10组组首延续手搭在陆凡胳膊上的状态，再松手后退。",
      "fix_instruction": "若牛大春突然远离，应补充松手和后退动作。"
    },
    {
      "group": "第11组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡和黄毛在组首均位于土路对峙位置，牛大春已退到背景不承担台词，人物可用性清楚。",
      "fix_instruction": "若牛大春参与台词，应重新写入组首位置。"
    },
    {
      "group": "第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "道路段没有模型说明词、参考图占位、模板编号或字幕要求。",
      "fix_instruction": "若出现工程词或字幕说明，应删除并改为可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
