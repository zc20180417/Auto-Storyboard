{
  "pass": true,
  "summary": "seg01 草稿已按原剧本完成夜市检查、流言余波和医院母子对话，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
      "evidence": "原剧本中夜市管理翻看肉、问“这批肉今天进的？”，许安答“凌晨三点拿的”，夜市管理乙确认保鲜和处理干净，林小满说明天天现穿现烤；第1组按同一顺序保留这些检查动作和台词。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组 3-8.5秒承载夜市管理甲 23 个有效字左右的解释台词，5.5 秒内字秒比约 4.2，并有记录夹动作支撑；第3组其他台词均在 0.5 秒粒度时间段内，没有超过 6.5 字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组是韩彪威胁和许安反击的短句对峙，总时长 8 秒，属于单句反应和短承接例外；两个时间段 0-4秒、4-8秒连续，标题镜头数 2 个与实际一致。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组切到医院病房，组首只锁定韩秀兰、病房门、床头柜和输液架；许安先在 0-3.5秒明确入场并放下保温盒，再参与对话，人物可用性成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩彪对许安说话、唐婶对韩彪回呛、夜市管理甲对许安和林小满说明、夜市管理乙对路人甲说明，所有现场对白都有真实对象。",
      "fix_instruction": "若后续修改，应继续保留每句现场对白的说话对象，不能改成无对象喊话。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部管理乙持检查记录夹站在摊前，第3组组首继续保留管理甲、管理乙、检查记录夹、许安和林小满的摊前站位，随后才写管理人员离开。",
      "fix_instruction": "若不通过，应在第2组组尾或第3组组首补足检查记录夹和管理人员位置。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本里管理人员离开后，新客犹豫、路人乙和路人甲低声观望、林小满说“通过了也没用，他们还是怕”、许安说“流言比火快”；第4组逐项保留。",
      "fix_instruction": "若不通过，应补回被漏掉的路人观望台词或林小满、许安的原句。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组只承载韩秀兰说明医生来过和治疗可延后、许安不想拖、韩秀兰劝他先站稳这三个情绪节拍，11 秒内没有叠加额外事件或道具操作。",
      "fix_instruction": "若不通过，应拆分治疗延期说明和母亲劝说，不要新增无关动作。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第8组全部为许安和韩秀兰在病房内的现场开口对白，没有心声、旁白、电话音或门外音被错误写成口型。",
      "fix_instruction": "若后续加入旁白或心声，应写明嘴唇闭合、不做口型，并说明声音来源。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有出现 Seedance 自动、参考模板、模板编号、@图片、首帧尾帧、视频延长等工程词，也没有使用禁用模板化句式。",
      "fix_instruction": "若出现模板或模型说明词，应改成自然画面动作和声音描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
