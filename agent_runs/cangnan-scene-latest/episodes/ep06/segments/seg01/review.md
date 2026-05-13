{
  "pass": true,
  "summary": "seg01已对照河滩相遇与转型邀约剧本完成审稿，台词、空间、时长和人物可用性均可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留陆凡河滩思索、周思思举自拍杆跳舞和原台词“感谢大哥送的穿云箭！思思给大家跳个舞！”，未新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "7.5-15秒连续承载陆凡、周思思三句关键问答约42字，7.5秒约5.6字/秒，并包含指向村口动作，容量充足。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首明确陆凡位于画面左前方、周思思位于画面右侧，均在水头村河滩，同组没有跨物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡和周思思在组首均已有明确位置、朝向和道具，周思思开口前已可见。",
      "fix_instruction": "若不通过，应在组首补足人物位置、身体朝向和手机/自拍杆状态。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周思思、陆凡的现场对白均写成对对方说道或问道，没有假对象对白。",
      "fix_instruction": "若不通过，应将每句现场对白改成A对B说道/问道。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡挡在镜头前，第2组组首延续为陆凡站在周思思手机镜头前，人物状态连续。",
      "fix_instruction": "若不通过，应在第1组尾或第2组组首补清陆凡与手机镜头的位置关系。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图或自动分镜等工程词。",
      "fix_instruction": "若出现模型或模板说明，应删除并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
