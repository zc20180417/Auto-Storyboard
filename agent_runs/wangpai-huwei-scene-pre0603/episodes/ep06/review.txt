{
  "pass": true,
  "summary": "第06集分镜完整保留许知夏识破假视频、保险柜线索、周氏下令夜闯、顾北辰暗中制伏黑衣人和走廊互相试探，格式、时长、对白指向、动作拆分和音画分离均通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组", "第13组"],
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
      "type": "audio_mouth_sync",
      "evidence": "许知夏OS在6-10秒写明嘴唇闭合不做口型，屏幕画面和U盘作为可见载体保留，未把内心声写成现场开口。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本中许知夏质疑伪证链、顾北辰提到董事长私人保险柜、许知夏追问来源，分镜按0-14秒完整保留台词顺序和保险柜线索。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "周振邦命令两名黑衣人的台词约34字，2-9秒共7秒承载，约4.9字/秒，符合压低声音的情绪对白节奏。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "顾北辰按肩现身、内心声、肘击、补拳分别拆成四段，黑衣人甲倒地和黑衣人乙转身状态清楚，没有把两名黑衣人的处理混在一个时间段。"
    },
    {
      "group": "第13组",
      "type": "prompt_pollution",
      "evidence": "走廊试探和窗外黑影退出均为自然分镜正文，没有模型说明、参考图、模板编号或工程提示词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "顾北辰问许知夏、许知夏回顾北辰、顾北辰再评价许叔，画面内对白均有真实对象。",
      "fix_instruction": "若不通过，应补明每句现场对白的说话对象。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏OS明确写嘴唇闭合不做口型，顾北辰的“今晚不能走”是现场对许知夏说话。",
      "fix_instruction": "若不通过，应区分现场开口和内心声闭口。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载赵明海说明毁证、周振邦追问位置、赵明海判断保险柜三个对白节拍，总时长13秒，没有叠加进门或打斗动作。",
      "fix_instruction": "若不通过，应把毁证说明和保险柜判断拆成两个组。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "黑衣人甲乙在组首位于董事长办公室门口，顾北辰在办公室内深处阴影中，满足后续现身可用性。",
      "fix_instruction": "若不通过，应在组首或前半段补人物入场或隐藏位置。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第9组撬具落在黑衣人甲手边，第10组组首复述撬具落地；保险柜未被打开，黑衣人乙被反扣在柜门上，状态连续。",
      "fix_instruction": "若不通过，应补撬具和保险柜状态过渡。"
    },
    {
      "group": "第11组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "扎带捆人、翻出物证、拖到门外角落、整理衣领分别拆段，主动作清楚，未让黑衣人抢动作。",
      "fix_instruction": "若不通过，应把拖人和搜证拆开或减少同段动作。"
    },
    {
      "group": "第12组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第11组组尾两名黑衣人被捆在门外角落，第12组组首继续写他们在办公室门外暗处，顾北辰恢复散漫并端茶，能自然接到许知夏赶来。",
      "fix_instruction": "若不通过，应补门外角落、扎带和顾北辰站位。"
    },
    {
      "group": "第13组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第13组视频禁止项锚定顾北辰内心声、窗外黑影、衣袖划痕和许知夏，不含泛泛占位且不与正文矛盾。",
      "fix_instruction": "若不通过，应替换成与本组人物道具相关的具体禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
