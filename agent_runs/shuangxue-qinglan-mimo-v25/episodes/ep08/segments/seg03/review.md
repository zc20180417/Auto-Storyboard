{
  "pass": true,
  "summary": "seg03审核通过，2组台词节奏和空间锁定无硬伤。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清'跟你没关系？那这个收款账户是谁的？'15字÷5.2=2.9秒分配4秒，字秒比3.8；'收款人：强盛建材经营部！'10字÷5.2=1.9秒分配4秒，字秒比2.5。合格。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "组首空间锁定列出沈清举账单在画面左侧、刘美娟瞳孔收缩在画面右侧、柜员在柜台后方，空间关系清晰。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "原剧本'你……你胡说！''赵强的建材店，不是你家开的吗？''走，回家！找那个大老板对账去！'全部保留，刘美娟腿软撑台和沈清收单迈步的关键动作忠实还原。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为现场开口对白，有明确说话对象。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "4个时间段、10秒，包含刘美娟反驳（2秒）、沈清冷笑质问（3秒）、刘美娟腿软撑台（3秒）、沈清收单迈步（2秒），每段一个主动作，未过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第7组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作，无多个主动作挤在同一时间段，无非主动作人物抢戏。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
