{
  "pass": true,
  "summary": "seg02 保留封店、冻结、两百万罚款、贵族学校焦虑、扇耳光和找沈清要钱的冲突链。",
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
      "type": "dialogue_pacing",
      "evidence": "赵强两句和周美娟一句约42字，分布在2-13秒内，含砸账单与扑近动作，未超过6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "赵强起身吼骂、扇耳光、周美娟倒地、周建国护短分别拆成4个时间段。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "evidence": "视频禁止项锚定赵强、周美娟、周建国和散落账单，数量4条且均为本组风险。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定地下出租屋、破木床、散落账单及三人位置，第一时间段从该状态继续。",
      "fix_instruction": "若不通过，应删除组首过程动作并补足人物朝向。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留“上个屁”“丧门星”“你打她干什么”“找沈清要去”等关键台词和打翻在地动作。",
      "fix_instruction": "若不通过，应恢复原台词和扇耳光后倒地状态。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾周美娟站在赵强身前，第4组首复述该状态后赵强才站起动手。",
      "fix_instruction": "若不通过，应补第3组尾或第4组首的站位过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
