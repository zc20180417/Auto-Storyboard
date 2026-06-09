{
  "pass": true,
  "summary": "第2集seg01分镜稿忠实还原原剧本打手揭穿和举卡带母查账核心节拍，台词指向清晰，时空连续，无硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "dialogue_pacing",
      "evidence": "第1组各时间段字秒比：0-2.5秒 10字/2.5秒=4.0、2.5-4.5秒 7字/2秒=3.5、4.5-7秒 14字/2.5秒=5.6，均低于6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组组尾：沈清面向刘美娟站立、蛋糕砸在地上、周桂兰蹲在角落发抖。第2组组首：沈清位于画面中央、周桂兰仍蹲在角落发抖、刘美娟在右后方、蛋糕仍在地上。人物位置和状态连续。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "逐句核对原剧本：沈清转身扶起周桂兰→0-2秒；拿外套披上→2-4秒；沈清台词→2-4秒；刘美娟台词→4-6.5秒；沈清台词→6.5-10秒。台词原文、说话对象和顺序完全保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人开口对白，每句均写明说话对象。无心声、画外音或电话音承载。",
      "fix_instruction": "无需修改，口型和声音来源均正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组9秒4个时间段，强节拍数3个（举卡、对话交锋、举卡对峙），未超4个上限。每个时间段只承载一个主动作或一个连续对话节拍。",
      "fix_instruction": "无需修改，强节拍密度和时间段分配合理。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾：沈清举卡面向刘美娟、周桂兰蹲在角落发抖。第3组组首：沈清手持银行卡、周桂兰仍蹲在杂物堆旁发抖。状态连续。",
      "fix_instruction": "无需修改，组间状态连续。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "银行卡在第2组0-1秒掏出举起，6-9秒再次举起，第3组组首写明沈清手中持有。道具归属全程连续。",
      "fix_instruction": "无需修改，道具归属连续。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组4个时间段各承载一个主动作或一个台词。非主动作人物只写站位和轻反应。",
      "fix_instruction": "无需修改，动作原子性合格。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "场景简单、人物少、动作清楚，正文已写清站位和道具归属，无需额外视频禁止项。",
      "fix_instruction": "无需修改，视频禁止项按规则可省略。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "第2组6-9秒时间段字秒比6.3字/秒，接近6.5硬上限。",
      "evidence": "19字÷3秒=6.3字/秒。",
      "fix": "若口型验证偏快，可延长至6-9.5秒。"
    },
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "generation_density",
      "problem": "第3组0-2秒扶母复合动作链2秒内完成可能偏紧。",
      "evidence": "蹲下+扶臂+扶起三个子动作在2秒内。",
      "fix": "若验证不够，可延长至0-2.5秒。"
    }
  ]
}
