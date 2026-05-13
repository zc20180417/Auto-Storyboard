{
  "pass": true,
  "summary": "seg01 已对照第2集完整剧本审核，7组均保留关键台词、人物关系、道具动作和 HappyHorse 专属结构，未发现 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组"
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中林建国抄起墙角锄头要往外冲、张桂兰哭喊劝阻、林跃按住父亲肩膀并拿下锄头；分镜第2组按同一顺序呈现锄头归属变化，并保留张桂兰、林建国、林跃三段现场对白。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组把林跃递协议、愿意转让果园、请求通水、赵大强讥讽拆成4段共14秒；完整台词只在【音频】中承载，【运动】只写口型和身体反应，避免台词双写。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组始终在村委会办公室内，协议、印泥盒、笔和抽屉位置在【场景】与【主体】中锁定；林跃加极小字时用身体遮挡，未跨空间或新增未在场人物。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "第7组将林跃 OS 明确写为内心旁白，画面中的林跃嘴唇闭合、不做口型；赵大强与赵百川不在画面内，只以门内笑声和纸张声作为来源。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林家冷饭、窗外干涸田垄、林建国砸桌怒吼、张桂兰和林跃在场的关系均保留，未新增改变剧情的动作。",
      "fix_instruction": "无需修复；若后续改稿，应继续保留砸桌和怒吼作为本集开端冲突。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵百川对林跃假惺惺开口，林跃对赵百川恳求，赵大强对林跃嘲讽，对话对象清楚且没有发明虚假对象。",
      "fix_instruction": "无需修复；多人对话仍需在【音频】中逐句标明说话人与对象。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含取印泥盒、林跃犹豫、遮挡加小字、赵大强催促4个节拍，分配14秒且每段动作独立清楚，没有把按手印也挤入同一组。",
      "fix_instruction": "无需修复；不要把第6组按手印动作合并回第5组。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部林跃手掌压住协议末尾、印泥盒停在落款旁；第6组开头延续协议摊开、印泥盒打开，林跃手指靠近印泥，状态连续。",
      "fix_instruction": "无需修复；若调整组尾，应同步更新下一组【主体】中的道具归属。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全段使用【场景】【主体】【运动】【音频】【画面风格】外壳，没有出现 Seedance 默认字段、独立 --neg、参考图槽位或生产参数。",
      "fix_instruction": "无需修复；后续不要加入比例、分辨率、参考图、首帧尾帧等生产侧说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
