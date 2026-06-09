{
  "pass": true,
  "summary": "seg03共4组，凭条收卡、轿车溅水、金镯发现、质问对峙场景完整，台词忠实，口型节奏合规。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "第2组完整保留沈清脱大衣裹周桂兰、白色轿车溅水、沈清拉母亲躲避、刘美娟抱小雨下车、小雨'新车坐着真舒服'和刘美娟'报马术班'台词，忠于原剧本。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组 2-5秒和5-9秒：沈清心声均写明'嘴唇闭合不做口型'，心声格式正确，不与画面内对白混淆。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "evidence": "第4组视频禁止项4条：金镯消失、小雨消失、周桂兰提前开口、白色轿车驶离，均锚定本组人物和道具，无泛泛词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第1组凭条从机器口抽出→收入口袋→银行卡拔出握在手心，道具状态连续。",
      "fix_instruction": "无需修复，道具连续。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第2组13秒4个时间段：裹衣走路、轿车溅水躲避、刘美娟母女下车、母女对话，每个时间段一个主动作或连续对话节拍。",
      "fix_instruction": "无需修复，动作原子性合格。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组首与第2组组尾连续：刘美娟抱着小雨站在车旁、沈清搀扶周桂兰站在马路内侧、周桂兰身上裹着沈清大衣。",
      "fix_instruction": "无需修复，状态连续。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组10秒3个时间段：刘美娟回应、沈清逼近质问、对峙僵持，强节拍数合理，无过载。",
      "fix_instruction": "无需修复，密度合理。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "第3组9-12秒沈清台词'刘美娟，新车和金镯子，用着烫手吗？'15字÷3秒=5.0字/秒，略低于情绪对白目标5.2字/秒，但在4.5字/秒以上，属冷声质问的合理节奏。",
      "evidence": "有效字数15，镜头3秒，字秒比5.0。",
      "fix": "可选优化：若需更自然的冷声质问节奏，可延长至4秒（3.75字/秒），但当前3秒不阻断交付。"
    }
  ]
}
