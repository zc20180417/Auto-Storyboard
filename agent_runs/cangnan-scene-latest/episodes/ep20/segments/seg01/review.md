{
  "pass": true,
  "summary": "seg01保留包厢狂欢、等待疯狗消息、美女甲问话、宋子昂残忍回应和铜门巨响后的喊保安，格式与时长均通过。",
  "checked_groups": ["第1组"],
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
      "evidence": "保留原剧本中宋子昂等待疯狗消息、美女甲询问、宋子昂说陆凡被打成废物、铜门巨响和喊保安的全部关键节点。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "7-12秒连续对话约28个有效字，用5秒承载，字秒比约5.6；12-15秒怒喊约11字，用3秒承载，未超过6.5硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首锁定包厢、沙发、音响、纯铜大门和三名在场人物位置朝向，后续门响发生在同一物理空间内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂和美女甲的现场对白均写明对谁说，门外怒喊明确是对门外发声。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对象。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内承载包厢状态、两轮短对白和门响反应，强节拍数量可控，没有额外新增剧情动作。",
      "fix_instruction": "若不通过，应拆出门响反应或压缩非关键狂欢动作。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有出现Seedance说明、模板编号、参考图、自动分镜或字幕工程词。",
      "fix_instruction": "若不通过，应删除污染词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
