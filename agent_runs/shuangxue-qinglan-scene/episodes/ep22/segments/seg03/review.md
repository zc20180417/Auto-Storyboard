{
  "pass": true,
  "summary": "seg03 保留周建国惊惧、沈清五分钟倒计时、周美娟哭求和三人拖袋离开，短组理由成立。",
  "checked_groups": ["第6组", "第7组", "第8组"],
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
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "周建国裹军大衣跑出、发抖并保留“疯了……你真是个疯子！连法警都叫来了！”"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "沈清两句分别为7字/3秒和25字/5秒，周美娟约12字/3秒，均未超过6.5字/秒。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "evidence": "第8组为三人拖化肥袋离开的短动作余波，8秒短组符合规则，没有靠停顿凑时长。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周建国在0-3秒入场后才参与发抖反应和台词，人物可用性成立。",
      "fix_instruction": "若不通过，应在说话前补清楚入场或组首位置。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清分别对周建国和三人说道，周美娟对周建国说道，对象明确。",
      "fix_instruction": "若不通过，应逐句补真实对话对象。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "拖起化肥袋与离开院门分成两个时间段，沈清只站位不抢三人的离开动作。",
      "fix_instruction": "若不通过，应拆开拿袋、拖行和出门动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
