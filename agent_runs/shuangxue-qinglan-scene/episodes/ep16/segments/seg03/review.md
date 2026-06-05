{
  "pass": true,
  "summary": "seg03 保留周桂兰捡钻石壳手机、读尾号6789短信、确认自己银行卡、痛哭并砸向周美娟额头的关键动作。",
  "checked_groups": ["第4组"],
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
      "evidence": "第4组保留钻石壳手机、短信“尾号6789向您转入2.00元，余额…”，以及周桂兰两句原台词和砸周美娟额头的动作。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "屏幕短信校验有效字数16字给2.5秒约6.4字/秒；周桂兰确认银行卡台词约13字给2秒约6.5字/秒，痛哭台词约8字给1.5秒约5.3字/秒，周美娟喊话约8字给2秒约4字/秒。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "周美娟手机从组首周桂兰脚边，到周桂兰捡起，再作为砸向周美娟额头的道具，归属和位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "捡手机、读屏、两句情绪台词、扬手砸手机、周美娟捂脸反应分段明确。",
      "fix_instruction": "若不通过，应拆分读屏和砸手机动作。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "银行卡尾号和2元转账通过手机屏幕特写可见，周桂兰痛哭通过眼泪和攥手机动作表现，没有只写抽象判断。",
      "fix_instruction": "若不通过，应把不可视信息转成屏幕内容或可见动作。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首继承第3组周美娟手机亮屏停在周桂兰脚边，组尾明确周美娟捂额头、周桂兰手边仍有手机。",
      "fix_instruction": "若不通过，应补齐手机落点和砸后状态。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定钻石壳手机、尾号6789短信、周美娟额头和红印，均为本组关键视频风险。",
      "fix_instruction": "若不通过，应改成更具体的手机和额头红印禁项。"
    }
  ],
  "issues": [],
  "warnings": []
}
