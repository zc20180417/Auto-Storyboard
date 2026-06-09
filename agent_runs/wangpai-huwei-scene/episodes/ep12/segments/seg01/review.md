{
  "pass": true,
  "summary": "ep12 seg01 已覆盖地下档案库查证、会议室救人、秦越亮明身份和顾北辰耳机指路，空间切换、台词和关键道具连续性通过审核。",
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
      "type": "audio_mouth_sync",
      "evidence": "顾北辰的“下雨”作为耳机声出现，许知夏扫描动作停住且嘴唇闭合；门外陌生男声隔门出现，有皮鞋影子作为声音来源锚点。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "翻桌、夺刀、割开束缚、拉起搭档母亲分别占用0-3秒、3-6秒、6-10秒、10-14秒，没有把多段动作塞进单一镜头。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "许知夏关于赵明海抵押许氏技术和非法收购核心项目的质问约32个有效字，安排在4-10秒6秒内，字秒比约5.3，未超过硬上限。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "秦越关于许父拿到东西、一死了之、把许知夏推到台前当诱饵，以及顾北辰一定会救她的挑拨台词均保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "备用卡开门、盛远一期资金流文件夹、转让协议和手机扫描的前置状态都清楚，协议从档案夹转到许知夏手中。",
      "fix_instruction": "如不通过，应补齐协议从文件夹中取出的过程和手机位置。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组继承上一集会议室硬盘接入电脑的状态，屏幕从解密完成转为空白文件，能直接触发第4组救人动作。",
      "fix_instruction": "如不通过，应补电脑、硬盘和周振邦站位。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "周振邦对讲机下令、顾北辰推老人到门口、司机接走、保镖晚到分段呈现，救人撤离没有跨到档案库线。",
      "fix_instruction": "如不通过，应拆出撤离或保镖入场动作。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越和两名保镖先由档案库门进入，再与许知夏对话；许知夏组首已有协议和耳机，行为可用性完整。",
      "fix_instruction": "如不通过，应先写秦越入场再写自我介绍。"
    },
    {
      "group": "第9组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏对秦越反击，秦越对许知夏抛出旧仓库真相，现场对白对象明确。",
      "fix_instruction": "如不通过，应明确每句现场对白的对象。"
    },
    {
      "group": "第11组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰以耳机声指向安全通道，许知夏嘴唇闭合并用视线回应，顾北辰没有在档案库现场现身。",
      "fix_instruction": "如不通过，应改为耳机声并标明许知夏闭口。"
    },
    {
      "group": "第11组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "安全通道组的禁止项锚定顾北辰耳机声、转让协议、秦越、安全通道和保镖位置，数量4条且具体。",
      "fix_instruction": "如不通过，应替换泛泛负面词为本组特定人物和道具风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
