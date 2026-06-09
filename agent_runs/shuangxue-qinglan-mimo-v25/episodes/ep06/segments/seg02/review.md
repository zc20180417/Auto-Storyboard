{
  "pass": true,
  "summary": "两组均在周家杂物间夜景，母女对话全部保留，台词节奏合格，情绪递进清楚。",
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
      "evidence": "周桂兰哀求21字/4.5秒=4.67字/秒(情绪对白)；沈清心痛19字/4秒=4.75字/秒(情绪对白)；周桂兰流泪17字/3.5秒=4.86字/秒(情绪对白)。全部≥4.5且<6.5。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清'妈你别怕有我在'和'这钱是怎么转没的我明天一定查个水落石出'两句台词原文保留；周桂兰含泪点头动作保留。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组组尾周桂兰落泪、沈清站立；第2组组首周桂兰坐在床边有泪痕、沈清位于面前，握手动作自然承接。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内真人现场开口对白，每句写明'A对B说道'，无心声混用。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "握手+对白(4秒)、坚毅宣言(3.5秒)、周桂兰点头(2.5秒)各时间段只承载一个主动作或一个对话节拍。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "三句情绪对白构成母女哀劝-心痛-流泪的自然递进，每句独立时间段，无过载。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
