{
  "pass": true,
  "summary": "第01集规则修正版保留临终托付、会议室现金流危机、许知夏带合同出发、赵明海通风报信和山路黑车逼近悬念；连续事件链合并后未漏剧情，台词指向、空间锁定、道具归属和视频执行稳定性通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组"],
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "许振南交代许氏危险、保险柜钥匙、当年的事和心电监护仪长音均保留，顾北辰红眼接钥匙与原剧本一致。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "许知夏“通知法务复核合同。赵明海那边，别让他单独碰财务章。”约29字给5秒，字秒比约5.8，低于6.5硬上限。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "evidence": "第5组组尾顾北辰在驾驶位、许知夏带合同和资料到车旁，第6组组首直接承接为车门旁上车，随后进入车内驶离，属于同一连续上车链条。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "evidence": "商务车驶入盘山路，许知夏在后排翻合同，顾北辰在驾驶位看后视镜，两辆黑车从后方跟上，人物位置和车辆关系清楚。"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "顾北辰提醒拿稳合同、许知夏追问、急弯逼近、顾北辰说坐稳按时间段分开，每段只有一个主动作或一句短对白。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许振南三句遗言均明确写为对顾北辰说道，钥匙交到顾北辰掌心，现场口型承载清楚。",
      "fix_instruction": "若不通过，应恢复许振南对顾北辰的明确对白对象和钥匙交接。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "盛远合同在许知夏手边，财务章在赵明海面前，组尾也保持同一归属，未把财务章误交给许知夏。",
      "fix_instruction": "若不通过，应把合同和财务章位置改回会议桌上的原始归属。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "顾北辰拎豆浆进门、许知夏转头、顾北辰问哪位是许总、董事甲嘲弄、顾北辰看空椅子构成连续入场和羞辱节拍，14秒有足够动作和台词容量。",
      "fix_instruction": "若不通过，应删去空表情停顿或拆出不属于同一入场链条的内容。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "快步下楼、助理递资料、法务复核、盯住赵明海、顾北辰提醒上车和安全带均与原剧本顺序一致。",
      "fix_instruction": "若不通过，应恢复门口出发前的助理资料和顾北辰安全带提醒。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵明海对手机里的秦越压低声音说“她出发了。司机临时换的，不碍事。”秦越本人未出现在窗边，电话音不会误成现场人物口型。",
      "fix_instruction": "若不通过，应明确秦越只存在于手机听筒或画外电话音。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "许知夏察觉沉默、顾北辰故作轻松、黑车加速左右压近、许知夏抓扶手惊问分段清楚，没有把撞击、问话和转向压进同一镜头。",
      "fix_instruction": "若不通过，应拆开黑车压近、车身晃动和许知夏反应。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终组只包含自然分镜、光影、组尾衔接和视频禁止项，没有模型说明词、模板编号、参考图或工程占位符。",
      "fix_instruction": "若不通过，应删除所有非分镜正文的模型提示污染。"
    }
  ],
  "issues": [],
  "warnings": []
}
