{
  "pass": true,
  "summary": "ep03 单段分镜保留办公室试探、车库查车和周氏谋划三条剧情线，时间轴、空间切换、台词指向和心声闭口承载均符合竖屏 scene 规则。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵明海试探句约24字给5秒，约4.8字/秒；许知夏反击句约26字给5秒，约5.2字/秒，符合情绪对白速度且未靠普通停顿凑时长。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS写明嘴唇闭合不做口型，声音为内心声；画面以手电、油管切口和指腹检查承载推理信息。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "赵明海向周振邦汇报山路失败、司机不简单、刹车被剪还能控车等关键信息均保留，周振邦对司机搅黄两辆车的嘲讽台词未改写。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "办公室外走廊单独成组，组首明确赵明海已退到走廊内，避免办公室到走廊的物理空间混入上一组。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏OS以嘴唇闭合、不做口型承载，随后赵明海和许知夏的现场对白均明确对话对象。",
      "fix_instruction": "若后续改稿让许知夏开口说出OS，应改回内心声并补嘴唇闭合。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只包含许知夏入场询问、顾北辰起身拍灰、顾北辰回答三个强节拍，13秒内可表演。",
      "fix_instruction": "若增加证物展示或新追问，应拆到下一组，避免车库查车段过载。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏两段质问都写为对顾北辰说道/问道，顾北辰回答也写明对许知夏说道，没有假对象。",
      "fix_instruction": "若删去对话对象，应补回人物对象。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "油管截段在第5组收进口袋，第6至第8组组首持续锚定仍在顾北辰口袋里，许知夏没有拿走证物。",
      "fix_instruction": "若需要许知夏拿到证物，必须补递出或拿取动作。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "红酒杯、命令归属和许知夏不在场三个禁止项均锚定本组风险，没有泛泛词或模板占位。",
      "fix_instruction": "若禁止项超过5个或变成通用画质词，应删除并保留本组剧情错误。"
    },
    {
      "group": "第11组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周振邦OS被拆入6秒短收尾组，写明嘴唇闭合不做口型，避免第10组台词与心声同段过载。",
      "fix_instruction": "若合并回第10组，应重新分配至少满足字秒比的时长或保留独立短组。"
    },
    {
      "group": "第1组",
      "type": "format",
      "result": "pass",
      "evidence": "组标题含EP03-G01 cut_id，时间段0-12秒连续，镜头数4个与实际时间段一致，字段完整。",
      "fix_instruction": "若后续调整时间段，应同步修改标题总时长和镜头数。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部赵明海退到门外，第4组首为办公室外走廊且办公室门半开，人物位置连续。",
      "fix_instruction": "若改成赵明海仍在办公室内拨电话，应合并或重写组首状态。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、参考模板、@图片或自动分镜等工程词，结尾只保留自然分镜描述。",
      "fix_instruction": "若出现模板或模型说明词，应改写为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
