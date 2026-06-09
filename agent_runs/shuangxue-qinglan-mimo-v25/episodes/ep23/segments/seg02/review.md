{
  "pass": true,
  "summary": "seg02（第3-5组）通过审核。城中村出租屋夜景，赵强崩溃怒吼、打翻周美娟、周建国护短挡人，暴力动作拆段清楚，保护站位明确。",
  "checked_groups": ["第3组", "第4组", "第5组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "赵强'税务局把店封了！账户全冻结了！'14字÷3秒=4.7字/秒；'还要罚款两百万！我全完了！'12字÷3秒=4.0字/秒，节奏合格。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "赵强'上个屁！都是你这个丧门星惹的祸！'17字÷3秒=5.7字/秒，情绪对白节奏合格。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "周建国从门框旁冲到周美娟身前的挡人动作在组首用状态描述（周美娟倒地、赵强站在身旁、周建国靠在门框旁），无过程动词，符合组首空间锁定规则。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人对白，无心声/画外音需要音画分离。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每时间段只有一个主动作：0-4秒周美娟哭喊，4-7秒赵强打人，7-8秒周美娟倒地。非主动作人物周建国未抢戏。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第5组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项3条均锚定本组人物和具体动作，无泛泛词。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}