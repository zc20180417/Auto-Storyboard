{
  "pass": true,
  "summary": "seg03三组完整保留银行查卡、短信提醒号码异常、赵强新车和沈清心声揭示，银行卡归属与心声闭口处理清楚。",
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
      "type": "prop_continuity",
      "evidence": "破旧银行卡从窗口台面被沈清推给柜员，再由柜员接入窗口内读卡，组尾明确银行卡已在柜员窗口内。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "柜员约17字疑问给4.5秒，约3.8字/秒；周桂兰约10字给3秒并带点头动作；柜员约27字严肃说明给7.5秒，节奏可承载。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "沈清现场问句写为对银行柜员问道；末尾心声写明沈清嘴唇闭合不做口型，避免心声被误生成现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "0-3秒扶坐和放卡，3-7.5秒推卡并说查流水，7.5-12秒柜员接卡刷卡敲键盘，动作链按阶段拆开。",
      "fix_instruction": "若不通过，应拆分接卡和敲键盘动作。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留柜员询问本人使用、周桂兰贴身藏卡、短信提醒号码不是本人这三个关键信息。",
      "fix_instruction": "若不通过，应恢复原剧本关键台词和顺序。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部异常信息说出，第3组组首沈清和周桂兰仍在窗口前，银行卡仍在读卡器旁，连续无跳变。",
      "fix_instruction": "若不通过，应在第2组尾或第3组首补银行卡和人物位置。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第3组涉及心声、车、银行卡等关键生成风险，视频禁止项锚定沈清心声、赵强、银行卡、周桂兰座椅，数量4条。",
      "fix_instruction": "若不通过，应补充具体锚点或删除泛泛禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
