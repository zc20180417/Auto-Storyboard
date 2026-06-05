{
  "pass": true,
  "summary": "seg02 已对照原剧本审核，周美娟震惊、周建国呵斥、沈清追房租和十九万、赵强缓和说辞均完整保留。",
  "checked_groups": ["第4组", "第5组"],
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "周美娟“爸！这房子不是你的？”、周建国“闭嘴！大人的事少插嘴！”和沈清嘲讽台词均按原顺序保留。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "沈清约22字质问给5.5秒、赵强约18字回应给5秒、沈清约16字大喝给4.5秒，均未超过6.5字/秒。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组全程发生在周家正屋客厅，沈清、赵强、周美娟、周建国都在组首拥有位置和朝向。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周美娟、赵强、周建国、沈清均在组首可见，周美娟开口前已位于沙发旁。",
      "fix_instruction": "若人物缺失，应在组首补其画面位置、身体朝向和视线。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为沈清问房租、赵强缓和、沈清索回十九万的连续对话节拍，没有额外抢焦点动作。",
      "fix_instruction": "若密度过高，应把赵强回应或沈清大喝拆成短承接组。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词都是画面内真人现场开口，并逐句标明对话对象，无画外音或心声。",
      "fix_instruction": "若出现旁白或心声，应写明声音来源并标注闭口。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组组尾保留沈清手中复印件和沙发旁人物位置，第5组组首直接继承这些状态。",
      "fix_instruction": "若断裂，应在两组之间补复印件和沙发旁站位锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
