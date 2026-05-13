{
  "pass": true,
  "summary": "已对照第27集原剧本、竖屏生成规则和当前seg01分镜逐组审核，关键台词、人物关系、空间衔接、口型承载和时间轴均可交付。",
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "韩彪挖人台词约23字放在0-5.5秒，约4.2字/秒；韩彪质问约20字放在7.5-11.5秒，约5.0字/秒；许安回应约18字放在11.5-15秒，约5.1字/秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本中老周保货、街坊甲乙帮桌帮人、林小满反问、韩彪咬牙的台词和顺序均保留，未新增改变剧情的强动作或道具。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "组首锁定韩彪后厨单一物理空间，并明确韩彪、阿顺、关键帮工甲、帮工乙、马会各自位置和身体朝向，关键帮工甲扔围裙发生在时间段内。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "evidence": "本组承载马会冷嘲、韩彪回问、马会补刀、韩彪掀翻料盆并威胁众人四个连续强节拍，总时长15秒，最后威胁台词约29字用6.5秒并同步掀盆动作，表演容量可承载。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "许安的“最后一局，拼火候。”被写为画外音，画面中的许安明确嘴唇闭合不做口型，远处评选广播也有广播喇叭作为声音来源。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "评选前夜两边摊位对比、林小满担心排场、许安强调味道、韩彪带人嘲讽和林小满回击均按原剧本顺序呈现。",
      "fix_instruction": "无需修改；若后续改稿，应保持两边摊位对比和四句对白顺序不变。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩彪对许安挖人、许安对韩彪拒绝、韩彪对许安质问、许安对韩彪反击均写明真实对话对象，没有假对象或自语混用。",
      "fix_instruction": "无需修改；若后续拆分台词，仍需保留每句画面内对白的说话对象。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部韩彪退回一步、许安摊位被街坊护住，第4组组首复述许安摊位火候稳定、韩彪在自家灯牌前、阿顺在韩彪身后观察，街口状态连续。",
      "fix_instruction": "无需修改；若调整站位，应同步更新第3组组尾和第4组组首。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第5组关键帮工甲把围裙留在案板上，第6组组首继续写围裙在他手边，随后他抓起围裙甩到一旁并朝门口离开，道具归属有可见过渡。",
      "fix_instruction": "无需修改；若删去围裙动作，需要补足关键帮工离场的可见过渡。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载签子散落、帮工乙通报外车到、韩彪命令收拾、众人越忙越乱四个节拍，13秒内动作链清楚，没有把比赛现场转场硬塞进同一空间。",
      "fix_instruction": "无需修改；若加入更多比赛现场画面，应另起组或明确转场。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许安画外音与画面人物闭口状态匹配，远处广播作为环境声音保留来源，不存在现场开口和旁白混用。",
      "fix_instruction": "无需修改；若改成现场对白，应去掉画外音写法并让许安明确开口。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "各组正文未出现模型说明词、模板编号、占位符、工程说明或批量化空泛镜头描述。",
      "fix_instruction": "无需修改；后续改稿不得加入模型执行说明、模板来源或占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
