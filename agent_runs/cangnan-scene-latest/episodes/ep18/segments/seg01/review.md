{
  "pass": true,
  "summary": "seg01 keeps the roadside confrontation, all six dialogue lines, clear dialogue targets, valid timing, and usable first-frame space locks.",
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
      "evidence": "第1组保留宋子昂下车抽雪茄、嘲讽陆凡、陆凡反问地契、王局长举地契呵斥的顺序。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2.5-6秒承载宋子昂约23字台词，6-9秒承载陆凡约18字台词，9-12秒承载王局长约17字台词，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首复述陆凡、宋子昂、王局长在黑风山主干道上的位置、身体朝向和地契文件归属。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂、陆凡、王局长每句现场对白都写明对陆凡或宋子昂说道，没有假对象。",
      "fix_instruction": "若不通过，应逐句补足真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾王局长举着地契，宋子昂车旁对峙；第2组首仍保留三人同一位置和地契归属，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首补充地契和人物位置。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
