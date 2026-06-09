{
  "pass": true,
  "summary": "seg04（第9-10组）通过审核。赵强要逼补税、周建国威胁躺酒店大厅、三人贪婪笑容定格，台词忠实、节奏合格。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "赵强'光要钱不够，必须逼她把欠税的窟窿补上！'21字÷4秒=5.25字/秒；周建国'明天要是她敢说个不字。'12字÷3秒=4.0字/秒；'我就躺在酒店大厅，说她虐待继父！'19字÷3秒=6.3字/秒，全部低于6.5硬上限。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "周美娟'让她身败名裂，以后在这个城市混不下去！'忠实原剧本23-4；全景定格三人贪婪笑容忠实原剧本结尾△。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "evidence": "第8组组尾周建国面向赵强和周美娟、身体前倾；第9组组首周建国站在画面左侧、面向镜头、身体前倾，状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人对白，无心声/画外音需要音画分离。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒组3个时间段（赵强台词、周建国两句台词），强节拍3个，属于同一冲突推进，不过载。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每时间段只有一个主动作：0-5秒周美娟台词，5-8秒赵强点头反应，8-10秒全景定格。非主动作人物不抢戏。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}