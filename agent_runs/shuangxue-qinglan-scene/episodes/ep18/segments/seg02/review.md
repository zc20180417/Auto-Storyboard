{
  "pass": true,
  "summary": "seg02 保留周美娟护镯、沈清转向赵强、复述电话内容和赵强惊惧追问，未发现 hard issue。",
  "checked_groups": ["第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "“不行！这是我的命根子！”、“不摘是吧？赵强，你来说。”和“那天吃饭时，你接了个电话。”均按原顺序保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "沈清复述约 18 字用 4 秒约 4.5 字/秒，赵强追问约 9 字用 2 秒约 4.5 字/秒，均未超过 6.5 字/秒。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾沈清扣住周美娟手腕，第3组首继承这一状态；第3组尾赵强贴近茶几，第4组首继续在茶几旁。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "两组都发生在夜间明亮的周家正屋客厅，组首列出沈清、赵强、周美娟位置和朝向。",
      "fix_instruction": "若不通过，应补足人物位置、身体朝向和关键道具状态。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "电话内容由沈清现场复述，赵强现场追问，没有心声、画外音或电话音口型混用。",
      "fix_instruction": "若不通过，应明确声音来源或改为现场对白。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组只有复述电话内容、赵强震惊、赵强追问三个连续节拍，9 秒短组属于单句揭示与反应，不硬凑 10 秒。",
      "fix_instruction": "若不通过，应保留短组或与相邻同冲突轻节拍合并。"
    }
  ],
  "issues": [],
  "warnings": []
}
