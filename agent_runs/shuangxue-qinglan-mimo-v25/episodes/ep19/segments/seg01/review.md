{
  "pass": true,
  "summary": "第1-2组通过审核，台词指向清楚，时长合理，空间单一，状态连续。",
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
      "evidence": "沈清'很好，十九万二，一分不少'11字÷2.5秒=4.4字/秒；赵强'钱还了，你把那视频删了，别报警'15字÷4秒=3.75字/秒；沈清'删视频？我有说还了本金就算完吗？'14字÷3.5秒=4.0字/秒。均在合理范围内。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首锁定三人位置和道具手机，无跨空间。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留原剧本全部台词：利息怎么算、精神损失费怎么算，指向杂物间动作完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部为画面内现场对白，每句写明'A对B说道'，无心声/画外音混用。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "三句台词字秒比分别为4.4、3.75、4.0字/秒，均在合理范围。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部：沈清站画面中央、手机已收起、赵强瘫坐地面、周美娟背景微颤。第2组首：沈清画面左侧手机已收起、周美娟画面右侧后仰、赵强地面仰头。位置和状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒组承载1个沉默反应+2句台词+1个指向动作+1个等待反应。每个时间段单一主动作，无过载。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
