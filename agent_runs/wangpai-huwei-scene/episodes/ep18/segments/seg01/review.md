{
  "pass": true,
  "summary": "seg01已对照第18集剧本完成审核，废仓取证、林晚身份、秦越围堵和大门关闭均完整保留，无阻断问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
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
      "evidence": "林元关于保险柜的长句拆成6-11秒和11-15秒两个台词段，分别承载藏柜经过和钥匙未知信息，未把整句压入单段。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "evidence": "秦越在组首已位于二层栏杆阴影内，9-13秒拍手现身前具备空间可用性，不是凭空出现。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "evidence": "顾北辰击中第一人、林元踹第二人、秦越逼近、顾北辰旧伤变慢分成四段，打斗主动作清楚。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "许知夏捡铁管砸秦越后背、顾北辰重拳、秦越冷笑并按遥控关门均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组只发生在废仓外，人物、汽车、铁门、手电筒和监控探头位置明确。",
      "fix_instruction": "如不通过，应把进入仓库动作移到下一组或补清外部空间状态。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏OS写明嘴唇闭合，林元现场对白均写清对许知夏和顾北辰说。",
      "fix_instruction": "如不通过，应改成OS闭口或明确真人对白对象。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "钥匙从许知夏衣服内袋取出并插入保险柜，存储卡从打开的柜内转到许知夏手中，旧照片留在柜内。",
      "fix_instruction": "如不通过，应补充钥匙、存储卡或旧照片的可见过渡。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林元说明林晚是姐姐且三年前死在秦越手里，秦越说林晚背叛启元该死，核心信息未改写。",
      "fix_instruction": "如不通过，应恢复林晚身份、死亡原因和秦越评价。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "六名手下现身、秦越索要存储卡和硬盘、许知夏拒绝、手下逼近分段承载，没有与正式打斗混在同组。",
      "fix_instruction": "如不通过，应把手下现身和第一波打斗拆开。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定林元、秦越手下、顾北辰、许知夏、秦越和存储卡，数量4条且聚焦打斗站位和关键道具。",
      "fix_instruction": "如不通过，应改为2-5条本组具体人物、道具或场景风险。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、参考图、模板编号、自动正反打或非短剧模板语气。",
      "fix_instruction": "如出现污染词，应删除并改成自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
