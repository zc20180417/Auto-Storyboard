{
  "pass": true,
  "summary": "seg04 保留赵强求别报警、掏手机转账、周美娟阻拦、赵强推开并完成十九万二到账，审核通过。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "action_atomicity",
      "evidence": "赵强喊话、掏手机开 APP、周美娟阻拦、赵强推开分别是独立时间段，手机始终在赵强手里。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "第7组尾赵强握亮屏手机，第8组首继承；第8组新增沈清手机在身侧手中，8-10 秒收到到账提醒。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "保留“清清，十九万二，一分不少，别报警。”和沈清手机“叮”声亮屏，没有改成现金、支票或其他支付方式。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组为同一连续事件链：赵强保命、拿手机、周美娟阻拦、赵强推开，14 秒内每段只承载一个主动作。",
      "fix_instruction": "若不通过，应拆分阻拦和推开，或弱化周美娟非主动作。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "“叮”声来自沈清手中手机，赵强乞求为现场开口对白并写明对象沈清。",
      "fix_instruction": "若不通过，应明确手机声源或补现场对白对象。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定沈清手机、十九万二金额、赵强手机、周美娟金镯子，均为本组关键生成风险。",
      "fix_instruction": "若不通过，应删除无锚点泛泛项并补具体人物道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
