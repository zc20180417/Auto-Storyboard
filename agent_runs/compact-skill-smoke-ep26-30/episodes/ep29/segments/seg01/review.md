{
  "pass": true,
  "summary": "seg01按会议室、街头、大厅三处物理空间拆成6组，原剧本关键台词、道具状态和人物关系均保留，时间与口型承载通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组"],
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
      "type": "dialogue_pacing",
      "evidence": "赵朵朵开场台词约16字承载在3.5秒，约4.6字/秒；高管甲担忧台词约14字承载在3.5秒，约4.0字/秒；赵朵朵拍板台词约13字承载在3.5秒并配合拍桌动作，未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首明确集团大厦入口、劳斯莱斯、赵朵朵和助理在车门侧，李翠花和王大强在垃圾桶旁，整组只发生在省城街头入口外。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保安拦住两人、李翠花向赵朵朵哭喊认错、赵朵朵要求给救助站打电话并赶发布会，均按原剧本顺序保留。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "evidence": "记者采访和慈善承诺均写为自然短剧画面，没有出现模板编号、参考图、模型自动处理、字幕卡点或非短剧工程词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部赵朵朵仍在主位、众人等待继续部署，第2组组首仍在同一会议室并明确赵朵朵转向全国地图，人物和道具状态连续。",
      "fix_instruction": "若不通过，应在第1组尾或第2组组首补清赵朵朵与地图、赵大雷和高管的位置关系。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含爬近被拦、保安呵斥、李翠花哭喊、赵朵朵吩咐助理和离开五个节拍，总时长13秒，各对白段字秒比均低于6.5，动作链有3秒承载。",
      "fix_instruction": "若不通过，应拆分街头冲突，或压缩非关键反应，保留保安阻拦和赵朵朵冷漠处理。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "交易所大厅、人声鼎沸、巨大电子屏、桂姨抹泪、赵大雷傻笑、老首富夸奖和赵朵朵回应好戏刚开场均被保留。",
      "fix_instruction": "若不通过，应恢复原剧本中证券交易所见证上市的关键人物和台词顺序。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "记者两次提问均明确对赵朵朵追问，赵朵朵两次回答均明确对记者们说道，没有假对象或心声口型混用。",
      "fix_instruction": "若不通过，应把所有现场对白改成具体人物对具体人物或记者群体说话。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "劳斯莱斯、垃圾桶和破旧编织袋在组首和动作段中位置清楚，李翠花抓起编织袋、王大强拖着瘸腿靠近入口，为第4组被保安拦下提供连续起点。",
      "fix_instruction": "若不通过，应补充两名乞丐从垃圾桶旁向大厦入口移动的可见过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
