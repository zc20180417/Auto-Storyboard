{
  "pass": true,
  "summary": "seg01保留了张强拔U盘、陆凡提醒、纪委封存证物和带回数据恢复的完整因果，格式与节奏可交付。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中张强悄悄挪到办公桌旁拔U盘、陆凡喊“纪委同志，他要拔U盘！”均保留，U盘在7.5-12秒被纪委干部看见。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "纪委干部长台词约34字分配在6-14秒，约4.25字/秒，并配合出示工作证动作，未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "U盘从张强右手在0-3秒递出，3-8秒由纪委干部接过放入证物袋，道具归属变化有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确民政办大厅、三人画面位置和身体朝向，张强办公桌与U盘位置清楚。",
      "fix_instruction": "若不通过，应补齐三人位置、朝向和U盘所在桌面。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "张强和纪委干部所有现场对白均写明对谁说道，没有假对象或无对象台词。",
      "fix_instruction": "若不通过，应把对白改成A对B说道，并保留原台词。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾张强仍攥着U盘犹豫，第3组首延续为张强仍攥着U盘，随后递交。",
      "fix_instruction": "若不通过，应在组尾或组首补充U盘仍在张强手中。"
    }
  ],
  "issues": [],
  "warnings": []
}
