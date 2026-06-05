{
  "pass": true,
  "summary": "seg01 保留公寓安顿、答谢宴安排和查底命令，格式、时长、对白指向均可交付。",
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
      "evidence": "周桂兰、沈清三句对白约39字，分布在2-14秒内，并含握手动作，字秒比低于6.5。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留“龙腾酒店”“请柬发出去”“联系私家侦探”“周建国和赵强老底连同证据”等关键信息。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "全段保持高档公寓客餐厅单一物理空间，周桂兰、沈清、保姆、李助理均在组首可用。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为现场人物开口，周桂兰对沈清、沈清对周桂兰的对象明确。",
      "fix_instruction": "若不通过，应补足真实对话对象或改为画外音闭口。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载转头下令、助理记录、继续下令和周桂兰反应，均在同一命令链内。",
      "fix_instruction": "若不通过，应拆分答谢宴安排和侦探调查命令。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部李助理持平板在门边，第2组首复述该位置并让其接收命令。",
      "fix_instruction": "若不通过，应在第1组尾或第2组首补平板和站位状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
