{
  "pass": true,
  "summary": "第3组通过审核，15秒长组有足够台词容量和冲突升级支撑，5个时间段合理。",
  "checked_groups": ["第3组"],
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
      "evidence": "周美娟12字÷2秒=6.0字/秒；沈清16字÷3秒=5.3字/秒；沈清17字÷4秒=4.25字/秒；赵强+沈清22字÷4秒=5.5字/秒；沈清命令10字÷2秒=5.0字/秒。均不超过6.5硬上限。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "15秒组承载5个台词节拍+1个护腕反应。每个时间段只承载一个主动作或连续对话节拍，无过载。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留原剧本全部台词和动作：讹人、税务局、假账、给多少、身上值钱的、金镯子当利息。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部为画面内现场对白，每句写明说话人和对象，无心声/画外音混用。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部：沈清画面左侧、周美娟右侧后退、赵强地面仰头。第3组首：周美娟画面中央叉腰、沈清画面左侧、赵强地面仰头。周美娟从后退变叉腰是同一空间内的自然反应变化。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "5句台词字秒比分别为6.0、5.3、4.25、5.5、5.0字/秒，均在合理范围内。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
