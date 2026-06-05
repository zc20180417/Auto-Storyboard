{
  "pass": true,
  "summary": "seg02 互咬和法警控制均在同一被告席区域内完成，短控制组理由成立，无 hard issue。",
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
      "evidence": "周美娟三年崩溃、指责赵强让她拿养老钱填账、赵强反咬她贪虚荣买金买车三句均保留且顺序一致。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "evidence": "周美娟第一句对法庭方向，后两句分别明确对赵强喊话和赵强对周美娟反驳，没有假对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "evidence": "8秒短组只承载法警喝止和两名法警控制二人的动作余波，属于短动作余波，不硬凑10秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "三段短句分别给3秒、4秒、4秒，争吵语速处于可表演范围。",
      "fix_instruction": "若不通过，应延长单句时间或拆成两组。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "法警厉喝、扣住手臂肩背、压住争执分三段执行，非主动作人物没有抢动作。",
      "fix_instruction": "若不通过，应拆开控制动作或明确法警对应对象。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周美娟、赵强、法警和被告席控制动作，数量4条且不与正文矛盾。",
      "fix_instruction": "若不通过，应替换泛泛禁止项并保留本组人物锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
