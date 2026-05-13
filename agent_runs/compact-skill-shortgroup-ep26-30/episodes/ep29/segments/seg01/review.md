{
  "pass": true,
  "summary": "已对照 EP29 原剧本、竖屏 generator 规则和当前 segment 草稿逐组审核；草稿保留会议扩张、三年后街头冷遇、交易所答记者问的关键台词和动作，未发现阻断生产的 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "evidence": "原剧本中赵朵朵的“省城市场已经饱和，下一步进军全国。”、赵大雷的激动回应、高管甲对物流成本的担忧和赵朵朵拍板建车队均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组 0-4秒承载“三年内，我要在全国建十个分厂。”，16个有效字约4.0字/秒；6.5-10.5秒承载“大哥，车队你亲自去跑，招退伍兵。”，17个有效字约4.3字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "组首明确集团大厦入口台阶、赵朵朵、助理、保安、李翠花和王大强的位置；保安拦人、李翠花嚎哭、赵朵朵吩咐助理打电话均发生在同一物理空间内。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "evidence": "第6组只写记者提问、赵朵朵回答和交易所大厅反应，没有出现模板编号、参考图、自动分镜、模型说明词或占位符。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "会议室开场保留全国地图、主位关系和“进军全国”“建自己的车队”的决策信息，未改说话对象和因果。",
      "fix_instruction": "若不通过，应恢复被删台词，并按原剧本顺序拆回会议室同一冲突目标内。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为同一会议室内的扩张计划落点，包含指地图、齐声响应、指派赵大雷和赵大雷保证四个清晰节拍，14秒内可表演且未跨剧情目标。",
      "fix_instruction": "若不通过，应拆出赵大雷车队任务或延长承载时间，不能删减原台词。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首已说明赵朵朵在劳斯莱斯后排、助理在车门外、李翠花和王大强在垃圾桶旁，之后下车和抬头认出均有可见过程。",
      "fix_instruction": "若不通过，应在组首补第一帧位置，或在人物说话前补入场和揭示动作。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部两人朝赵朵朵倾过去，第4组首承接两人趴在路沿外侧、保安在入口栏杆旁；后续被拦、求救和赵朵朵离开连续成立。",
      "fix_instruction": "若不通过，应在第3组尾或第4组首补两人、保安和赵朵朵的具体位置状态。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "桂姨、赵大雷、老首富和赵朵朵的现场台词均面向赵朵朵、老首富或周围记者等真实对象，没有假对象对白。",
      "fix_instruction": "若不通过，应把对白对象改为真实在场人物或现场众人，不能写对空气、对道具说话。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "记者0-3.5秒提问“赵董，作为最年轻的女首富，有何感想？”约5.1字/秒；6-9秒追问“听说您要拿出百亿做慈善？”约4.3字/秒；赵朵朵两句短答分别由看向记者群、点头和亲友反应承载。",
      "fix_instruction": "若不通过，应增加正反打承载或拆组，不能压缩问句和答句。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文没有 Seedance 自动、参考官方模板、@图片、字幕贴片、广告口号或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明词和模板痕迹，改成可见动作、声音来源和光影描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
