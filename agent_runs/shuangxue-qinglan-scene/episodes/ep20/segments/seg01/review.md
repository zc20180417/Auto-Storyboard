{
  "pass": true,
  "summary": "seg01保留周建国耍赖、沈清转向母亲询问遗嘱、周桂兰取出油纸包的完整因果，格式和台词节奏可交付。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "周建国两句耍赖台词、沈清反问男主人、沈清转向周桂兰询问遗嘱均按原剧本顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组四段台词分别为约17字/3.5秒、17字/3秒、18字/3.5秒、16字/4秒，均低于6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "油纸包从周桂兰贴身衣袋取出，7-10秒递到沈清手中，组尾明确沈清持有叠好的油纸包。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "所有现场对白均写明周建国对沈清、沈清对周建国或沈清对周桂兰说道。",
      "fix_instruction": "无。若失去对象，应补为A对B说道。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写三人在周家正屋客厅的静态位置、朝向和衣襟处手势，没有过程动作。",
      "fix_instruction": "无。若出现取出等动作，应移入时间段。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "周桂兰回答、背身取油纸包、递给沈清被拆成三个清楚时间段，每段一个主动作。",
      "fix_instruction": "无。若动作挤在同一镜，应拆段。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周建国、周桂兰、沈清和油纸包，数量3条且不使用占位示例。",
      "fix_instruction": "无。若变成通用词，应替换为本组人物和道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
