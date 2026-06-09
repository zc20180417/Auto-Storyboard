{
  "pass": true,
  "summary": "第3组通过审核。",
  "checked_groups": [
    "第3组"
  ],
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
      "evidence": "助理入场台词在限制内，签字台词在限制内。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "组首继承第2组组尾状态。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本台词全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "沈清和周桂兰并肩坐着，文件在膝盖上。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒四个时间段合理。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "钢笔和计划书状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文无模板术语、无模型标签、无占位符。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}