{
  "pass": true,
  "summary": "第1组（五百万的对峙）12秒4镜头，周建国索要→律师警告→沈清反击，台词指向正确，空间单一。",
  "checked_groups": ["第1组"],
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
      "evidence": "周建国25字/4秒=6.25字/秒（情绪喊话），律师17字/3秒=5.7字/秒，沈清12字/2秒=6.0字/秒，沈清16字/3秒=5.3字/秒。均在6.5以内。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "五百万赡养费、敲诈勒索警告、不怒反笑、自投罗网等关键台词均保留。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间（宴会厅），周建国蹲地、律师右后方、沈清左侧，位置关系清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "warning",
      "evidence": "上一组（seg02）周美娟和赵强被隔离，本组仅出现周建国、律师、沈清，周美娟/赵强位置未交代。",
      "fix_instruction": "建议在组首空间锁定中补充周美娟和赵强被隔离在画面边缘的状态。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "4个时间段分别承载：周建国站起来喊话、律师上前警告、沈清笑讽、沈清平静宣判。属于同一对峙事件链的递进，密度合理。",
      "fix_instruction": "无需修改，对峙节奏合理。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "周建国25字台词完整保留，律师17字警告保留（压缩'您的言论'为省略但核心意思不变），沈清两句台词均保留。原剧本台词顺序、说话对象、剧情因果无改变。",
      "fix_instruction": "无需修改，台词忠实度合格。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "handoff_continuity",
      "problem": "周美娟和赵强在上一组被隔离后本组未出现，位置过渡略缺交代。",
      "evidence": "seg02组尾周美娟/赵强被隔离，本组组首未提及。",
      "fix": "建议组首空间锁定补充周美娟/赵强状态。"
    }
  ]
}