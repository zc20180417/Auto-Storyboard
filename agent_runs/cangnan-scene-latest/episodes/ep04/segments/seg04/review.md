{
  "pass": true,
  "summary": "seg04完整呈现赵大江以鱼干任务施压、陆凡接下任务并离开、赵大江阴狠收尾，审核通过。",
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
      "evidence": "赵大江点烟、说“既然你这么能干，有个重担交给你。”，陆凡答“请领导指示。”，水头村鱼干卖不出去的信息均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵大江“这是政治任务！完不成，自动引咎辞职。”约18字分配5秒并配合前倾压桌动作，语速不超限。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾陆凡站在桌前未退让，第3组首仍在办公桌前，随后2.5-5.5秒转身走出办公室。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "乡长办公室、赵大江老板椅、陆凡办公桌前站立、香烟位置均在组首明确。",
      "fix_instruction": "若不通过，应补办公室布局、两人位置和香烟归属。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载驻村任务、陆凡迟疑、赵大江政治施压和陆凡反应，14秒内强节拍不过载。",
      "fix_instruction": "若不通过，应将政治施压或陆凡反应单独拆出。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对赵大江说“好，我接了。”；赵大江低声对已离开的陆凡说威胁台词，声音来源和对象清楚。",
      "fix_instruction": "若不通过，应明确赵大江是低声对门口方向说，避免无对象台词。"
    }
  ],
  "issues": [],
  "warnings": []
}
