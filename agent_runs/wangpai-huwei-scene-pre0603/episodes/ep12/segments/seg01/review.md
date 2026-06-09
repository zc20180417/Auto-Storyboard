{
  "pass": true,
  "summary": "ep12 seg01 已对照原剧本和竖屏生成规则审核，10组均通过，档案库查证、会议室救人和秦越对峙均按原剧本顺序保留。",
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
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰VO“下雨”通过耳机响起时，许知夏嘴唇闭合只抬眼；门外陌生男声VO隔着门出现，并用门缝下皮鞋影子作为可见载体。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "踢桌、桌面撞偏黑衣人、夺刀、割开束缚、扶起老人分为5个时间段，复杂动作链没有压进单个镜头。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "秦越自我介绍台词安排在10-15秒，共约27字/5秒=5.4字/秒，未超过6.5硬上限。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "evidence": "许知夏从第6组起持续把转让协议藏在身后，第10组仍握着协议并脚尖转向安全通道，没有让关键协议丢失。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "备用卡刷门、旧项目资料、盛远一期资金流文件夹、转让协议中的赵明海和启元资本、许知夏低声确认背后之手均按原剧本保留。",
      "fix_instruction": "若不通过，应恢复文件夹名称、协议关键信息和许知夏发现启元资本的台词。"
    },
    {
      "group": "第3组",
      "type": "format",
      "result": "pass",
      "evidence": "第3组标题含EP12-G03，10秒4镜，时间段0-2.5、2.5-5、5-7、7-10连续，字段完整。",
      "fix_instruction": "若不通过，应修正cut_id、时间段连续性或镜头数。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "顾北辰踢桌、撞偏黑衣人、夺刀、割绑、扶老人跑按顺序分段；黑衣人只被桌面阻隔，没有替顾北辰执行救人动作。",
      "fix_instruction": "若不通过，应拆开踢桌、夺刀、割绑和扶人动作，避免多主动作同镜。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾老人已被扶起，第5组组首承接为顾北辰扶着老人站在会议室门口，随后推向司机；刀仍在顾北辰手中且刀尖朝下。",
      "fix_instruction": "若不通过，应在第4组尾或第5组首补清老人手腕已解绑、顾北辰扶人和刀的状态。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏两段反击均明确对秦越说道，秦越“商场只看结果”也明确对许知夏说道，未发明假对象。",
      "fix_instruction": "若不通过，应补足每句真人对白的真实对象。"
    },
    {
      "group": "第10组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰VO通过耳机指路，许知夏嘴唇闭合，只用视线和脚尖转向右后方安全通道承载反应。",
      "fix_instruction": "若不通过，应把顾北辰台词改为耳机VO，并明确许知夏闭口和可见反应。"
    },
    {
      "group": "第1组至第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、参考图、模板编号、自动分镜、固定尾部风格、JSON或调试标签，均为自然中文分镜。",
      "fix_instruction": "若不通过，应删除污染词和工程占位内容。"
    }
  ],
  "issues": [],
  "warnings": []
}
