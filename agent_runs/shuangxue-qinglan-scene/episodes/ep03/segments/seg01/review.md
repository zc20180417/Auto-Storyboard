{
  "pass": true,
  "summary": "seg01保留杂物间堵门、周建国压场、沈清反击和拉母亲出门的原剧本节拍，时间、对白指向和道具连续性可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "type": "dialogue_pacing",
      "evidence": "刘美娟告状对白给3秒、沈清8字反击给3秒，字秒比低于6.5且符合争吵口型。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "周建国叼牙签披大衣入场、威严呵斥、刘美娟告状和要求沈清放卡均按原剧本顺序保留。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "推开刘美娟、扶周桂兰出门、周建国喊话与沈清回怼分成4个时间段，没有把保护走位和对骂压在同一段。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确刘美娟堵门、沈清扶周桂兰并握卡，第一帧就是当前可生成状态。",
      "fix_instruction": "若失败，应补齐门口三人站位、朝向和银行卡归属。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "破旧银行卡从第1组到第4组始终在沈清手中，周建国只命令放下，没有被写成抢走。",
      "fix_instruction": "若失败，应在组尾或下一组组首补银行卡仍在沈清手中。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周桂兰、刘美娟、周建国和破旧银行卡，数量4条且不禁止原剧本必须发生的出门动作。",
      "fix_instruction": "若失败，应删除泛泛禁止词，改成本组人物和银行卡相关的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
