{
  "pass": true,
  "summary": "seg01三组完整保留客厅对账冲突，电话、手机、赡养费和家用说法的因果清楚，无阻断问题。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中沈清捕捉赵强电话关键词、质问账上钱、赵强挂断并塞手机、以建材店进货账搪塞，均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清约28字台词给6秒，约4.7字/秒；赵强约20字台词给5秒，约4字/秒，均在口型可承载范围内。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组始终位于周家正屋客厅，刘美娟、周建国、沈清、赵强都在组首有位置和朝向，周建国站起动作放在5-9.5秒内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机从赵强手中贴耳通话，5.5-8秒挂断后塞进口袋，组尾明确手机已在赵强口袋内。",
      "fix_instruction": "若不通过，应补赵强挂断和手机归属变化。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有沈清逼问和赵强否认两个连续对话节拍，11秒承载自然，没有额外动作挤压。",
      "fix_instruction": "若不通过，应拆出刘美娟插话或压缩普通反应。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟、周建国、沈清的现场对白均写明对沈清或周建国说道，没有假对象或心声混用。",
      "fix_instruction": "若不通过，应逐句补真实对话对象。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第3组涉及多人物对峙和手机连续性，视频禁止项锚定周建国、赵强手机、沈清、刘美娟，数量为4条。",
      "fix_instruction": "若不通过，应删除泛泛条目并锚定本组人物道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
