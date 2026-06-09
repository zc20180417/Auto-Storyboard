{
  "pass": true,
  "summary": "ep11 seg01 已覆盖安全屋准备、盛远大厅入局和会议室假盘验真，台词、空间、道具与撤离暗号均与原剧本一致。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
      "evidence": "许知夏关于法务、媒体和九点十五分定时投递的长台词约55个有效字，安排在4-13秒的9秒对白段内，字秒比约6.1，未超过6.5硬上限。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组只发生在盛远集团大楼门口，顾北辰在车外、司机在驾驶座内，车窗对话和司机点头均未跨入大厅空间。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏以耳机声出现且顾北辰嘴唇闭合，顾北辰内心声也明确嘴唇闭合，没有把VO或OS写成现场开口。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "黑色硬盘包在顾北辰手中，硬盘从包中取出、放到桌上、推向周振邦一侧，再由黑衣人接入电脑，关键道具转移路径完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留顾北辰制作假盘、许知夏说明进入盛远地下查档案和录音笔位置的关键台词与动作。",
      "fix_instruction": "如不通过，应补回硬盘拆装、空壳芯片和许知夏原台词。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "顾北辰对许知夏说保护评价和撤离暗号，许知夏对顾北辰说并肩与你也一样，对象明确。",
      "fix_instruction": "如不通过，应把现场对白改成A对B说道并避免假对象。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "陌生男声作为画外音出现，顾北辰和许知夏嘴唇闭合，车灯作为外部局势锚点，没有现场误开口。",
      "fix_instruction": "如不通过，应明确陌生男声来源为画外音并标注画面人物闭口。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "大厅组包含入场扫视、耳机问答、前台递访客卡和顾北辰OS，均在同一大厅空间内按时间段分开，未把入局和会议室人质揭示压入同组。",
      "fix_instruction": "如不通过，应拆分大厅动作或把会议室内容另起组。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周振邦、顾北辰、两名黑衣人和搭档母亲都在组首拥有明确位置和身体朝向，人质状态与后续台词、压迫动作兼容。",
      "fix_instruction": "如不通过，应在组首补齐人物位置、朝向和人质绑缚状态。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "假盘验真组提供4条本组特有禁止项，均锚定硬盘、进度条、搭档母亲或周振邦，未使用泛泛模板词。",
      "fix_instruction": "如不通过，应替换为本组人物、道具和动作锚定的2-5条具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
