{
  "pass": true,
  "summary": "已对照第4集原剧本、竖屏生成规则和当前分镜逐组审核，台词、空间、道具和OS承载均可交付，无硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组"
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
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中林小满把店门钥匙塞给许安并说“我那铺子外头空着，你敢不敢摆？”，分镜0-3秒保留递钥匙动作和原句；许安3-6秒对林小满说“你不怕我连累你？”，说话对象和顺序未改。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "林小满“借。但有一句，既然干，就别半路缩回去。”安排在0-5秒，约18个有效字，字秒比约3.6；许安“行。”安排在5-8秒并同时承载攥紧钥匙动作，口型压力不超限。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "组首写明炭夹位于旧炭炉旁地面，4.5-10秒韩秀兰拿起炭夹递给许安，10-12秒许安接过炭夹，关键道具归属有可见过渡。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "原剧本“许安(OS): 韩彪，这回我自己来。”在6.5-9.5秒写为许安OS画外心声，明确画面中的许安嘴唇闭合、不做口型，声音来源和口型分离清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组-第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "饭馆门口段完整保留借铺外空地、担心连累、林小满不愿看韩彪得意、许安确认借地、林小满要求别半路缩回去、许安答应等关键台词和因果。",
      "fix_instruction": "无需修复；若后续调整，只能局部压缩反应镜头，不能改台词或借地因果。"
    },
    {
      "group": "第5组-第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安家里段保留旧炭炉、铁签、炭夹，韩秀兰关于父亲留下的炭炉、别把这口火做脏、守住味道和别学省料省货的提醒均按原顺序出现。",
      "fix_instruction": "无需修复；旧炭炉和炭夹不可替换为其他道具。"
    },
    {
      "group": "第8组-第9组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "街口空地段在第8组组首锁定铺子外侧、韩彪新店门头、旧炭炉和折叠桌位置，第9组组首延续炉子停在铺外、桌和小灯已支好的状态，空间没有跳变。",
      "fix_instruction": "无需修复；后续若增加动作，应继续保持炉子正对韩彪新店。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许安OS明确为画外心声，且画面中许安嘴唇闭合、不做口型；现场对白只有林小满对许安说“行，那就摆给他看。”",
      "fix_instruction": "无需修复；不得把OS改成许安现场开口对空气说话。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "warning",
      "evidence": "第5组有5个时间段，承载翻出旧炭炉、韩秀兰问话、许安回应、父亲留下炭炉和许安确认等信息；总时长13秒且每个对白段均有足够时长，当前不影响理解。",
      "fix_instruction": "可选优化为压缩11-13秒道具特写并并入前一镜，但不是硬性修复。"
    },
    {
      "group": "第1组-第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜未出现模型说明词、模板编号、参考图占位符、横屏专用字段或模板化批量描述；画面风格和负面词保持自然短剧约束。",
      "fix_instruction": "无需修复；不要加入模板编号、参考图、自动分镜或横屏字段。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "generation_density",
      "problem": "第5组为5个时间段，信息点较多但仍在13秒内清楚可演。",
      "evidence": "0-3.5秒旧炭炉和韩秀兰问话，3.5-6秒许安回应，6-9秒韩秀兰指出父亲留下，9-11秒许安确认，11-13秒道具特写，时间轴连续且对白字秒比未超限。",
      "fix": "如需进一步压缩，可将11-13秒道具特写并入9-11秒末尾；当前不阻断交付。"
    }
  ]
}
