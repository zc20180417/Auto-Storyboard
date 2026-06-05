{
  "pass": true,
  "summary": "seg03保留豪车停红灯、周建国认出周桂兰、扒车窗、司机下车拦阻和两句哀求台词，动作阶段清楚。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "豪车停稳、周建国认出周桂兰、周建国跑到车窗分为三个时间段，没有把车辆抵达和扒窗挤进同一镜。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周建国“桂兰！清清！是我啊！”约9字用2秒承载，第二句约24字用4秒承载，均低于6.5字/秒。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "evidence": "第5组尾部周建国双手扒窗、司机仍在前排；第6组组首继承该状态，随后司机下车阻拦。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周建国、司机、周桂兰在组首均有明确位置；周桂兰在后排车窗内可被周建国认出。",
      "fix_instruction": "若不通过，应在组首补充车内人物位置或在行动前安排入场。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "司机“老人家，请退后，注意安全。”和周建国“我是沈总的爸！我是周桂兰的老公！我知道错了！”均忠于原剧本。",
      "fix_instruction": "若不通过，应恢复原剧本台词和说话顺序。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定司机、周建国、周桂兰和后排车窗，避免拦阻动作被错误生成。",
      "fix_instruction": "若不通过，应改成本组具体人物、车辆和车窗风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
