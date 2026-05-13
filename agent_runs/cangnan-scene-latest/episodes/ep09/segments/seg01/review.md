{
  "pass": true,
  "summary": "seg01审讯室三组保留逼签、账本对质和电话打断，时长与空间锁定满足竖屏分镜规则。",
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
      "type": "dialogue_pacing",
      "evidence": "王建国24字台词用4.5秒，约5.3字/秒；陆凡32字台词用5.5秒，约5.8字/秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留财政所账本被封、陆凡质问底层数据、王建国承认太晚并逼问签字的台词顺序和人物关系。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "民警在组首已位于审讯室门内侧阴影处，后续上前拦住王建国前具备可用位置；场景始终为审讯室。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "王建国对陆凡说道、陆凡对王建国说道均明确真实对话对象，没有假对象或心声混用。",
      "fix_instruction": "若不通过，应为每句现场对白补足真实说话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为同一审讯桌对峙，包含一段威胁、一句质问和一句得意回应，三段台词承载清楚，无外部事件或复杂道具操作叠加。",
      "fix_instruction": "若不通过，应拆分威胁和承认数据修改两个节拍。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾王建国俯身压桌，第3组开头王建国仍在桌边并起身绕向陆凡，认罪书仍在桌中央，状态连续。",
      "fix_instruction": "若不通过，应在第2组尾或第3组组首补足王建国和认罪书位置。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "民警现场低声对王建国汇报林书记来电话，声音来源和口型承载都是画面内民警。",
      "fix_instruction": "若不通过，应改为电话音画外音或明确民警现场转述。"
    }
  ],
  "issues": [],
  "warnings": []
}
