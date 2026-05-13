{
  "pass": true,
  "summary": "seg04已审核，陆凡回到民政办、张强惊怒、台账对质和抢夺失败均保留，时长与道具连续性通过。",
  "checked_groups": ["第8组", "第9组", "第10组"],
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
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "陆凡进门、张强问谁让回来、陆凡答苏主任、张强拍桌骂苏有光均按原剧本顺序保留。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "第9组每段对白均短于20字且分配2.5-3.5秒，最高约6字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "evidence": "第9组台账在陆凡手中，第10组张强伸手抢、陆凡后退并收进公文包，道具转移和保护动作可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "民政办大厅单一空间，陆凡门内、张强桌后、茶杯位置均在组首明确。",
      "fix_instruction": "若不通过，应补足大厅内人物位置和桌面道具状态。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第9组以短句对质为主，拿出台账、追问、指控和否认拆成5段，15秒内节奏清楚。",
      "fix_instruction": "若不通过，应拆出台账揭示或张强否认为独立组。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第9组尾部陆凡举台账、张强撑桌，第10组首保持该状态并写出伸手抢台账的动作。",
      "fix_instruction": "若不通过，应在第9组尾或第10组首补台账归属。"
    }
  ],
  "issues": [],
  "warnings": []
}
