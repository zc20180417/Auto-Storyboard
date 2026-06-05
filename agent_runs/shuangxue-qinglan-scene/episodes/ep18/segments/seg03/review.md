{
  "pass": true,
  "summary": "seg03 保留查税诈问、赵强瘫坐、周建国追问、沈清揭穿假账洗钱和报警威胁，审核通过。",
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
      "evidence": "沈清两句揭示、赵强瘫坐、赵强绝望台词分成独立时间段，瘫坐动作给 3.5 秒完整表演。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周建国约 17 字用 3.5 秒约 4.9 字/秒；沈清洗钱揭穿约 24 字用 5.5 秒约 4.4 字/秒，含指向赵强动作；报警威胁约 22 字用 6 秒约 3.7 字/秒，含赵强发抖反应，未超速。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "保留“做假账用我妈的卡洗钱”和“报了警，税务局一查，你那店就别想开了！”两句核心揭示，没有新增报警已发生等剧情。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列出沈清、赵强、周美娟、周建国在客厅的位置，周建国作为背景可被后续追问使用。",
      "fix_instruction": "若不通过，应在组首补足周建国的位置和朝向。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾赵强瘫坐在茶几旁，第6组首继承为赵强位于画面右侧地板上、瘫坐在茶几旁。",
      "fix_instruction": "若不通过，应修正上一组组尾或本组组首姿态。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定赵强、沈清、周建国、周美娟金镯子，限制瘫坐状态、洗钱对象和人物留场，没有泛泛模板词。",
      "fix_instruction": "若不通过，应删除泛化禁止项并补本组具体人物道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
