{
  "pass": true,
  "summary": "seg01 两组均通过审核，台词节奏、空间锁定、道具连续性均无硬伤。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "沈清厉声15字/3秒=5.0字/秒（情绪对白），周建国9字/2秒=4.5字/秒（情绪对白），沈清25字/5秒=5.0字/秒（情绪对白），均在4.5-6.5范围内。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清原文'周叔，你不是说对这笔钱不知情吗？'完整保留，周建国'没大没小！又在闹什么！'完整保留，沈清'两年前我妈重病昏迷，你拿着她的身份证去银行办代办变更！'完整保留。委托书拍茶几、周建国放壶瞥签名脸色微变等关键动作均保留。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组组尾：委托书摊开在茶几上、周建国壶搁在茶几边、沈清手仍按委托书、周桂兰站立。第2组组首：委托书仍在茶几上、紫砂壶仍在茶几边、沈清手仍按委托书、周桂兰站立。状态完全连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内真人开口，写明了谁对谁说。无心声/画外音/电话音混用。",
      "fix_instruction": "无需修改，口型和指向均正确。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组5个时间段，2-3个强节拍（沈清进入拍纸、沈清厉声质问、周建国放壶瞥签名），动作链完整无过载。第2组4个时间段，2个强节拍（沈清逼问、周桂兰崩溃），节奏合理。",
      "fix_instruction": "无需修改，强节拍密度合理。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作或一个连续对话节拍。沈清逼问在3秒内完成（逼近+指签名+台词），周桂兰两句台词作为连续对话节拍分在两个时间段，各自只承载一句台词和对应的身体反应。",
      "fix_instruction": "无需修改，动作拆分清晰。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "委托书从第1组到第2组始终摊在茶几上，紫砂壶从周建国手中到茶几边保持一致，无道具跳变。",
      "fix_instruction": "无需修改，道具归属连续。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "video_negative_constraints",
      "problem": "第1组视频禁止项'沈清进入方向与门位置矛盾'表述略泛，可更具体化。",
      "evidence": "当前写'沈清进入方向与门位置矛盾'，不如写'沈清从画面右侧进入（门在左侧）'更具体。",
      "fix": "建议改为'沈清从画面右侧进入（门在画面左侧）'以锚定具体方向错误。"
    }
  ]
}
