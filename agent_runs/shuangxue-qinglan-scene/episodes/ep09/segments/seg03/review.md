{
  "pass": true,
  "summary": "seg03 保留了赵强哑口无言、刘美娟尖叫护夫、周桂兰痛哭、沈清护住母亲以及赵强低声暴露假账风险的原剧本节点，审核通过。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "刘美娟两句尖声台词分别约20字和20字，各给4秒，字秒比约5.0；情绪喊话不超6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "evidence": "周桂兰哭诉、瘫坐捶胸、沈清挡到母亲前方、四人站位稳定分成四段，保护动作写清沈清挡在周桂兰和赵强一家之间。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "赵强趁沈清安慰母亲拉刘美娟衣角并低声说假账藏不住，刘美娟瞪大眼睛，原剧本关键反转完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "刘美娟、赵强、沈清、周桂兰都在组首拥有位置和朝向，刘美娟发话前可见，赵强反应可用。",
      "fix_instruction": "若刘美娟未在组首可见，应补其位于赵强身后或旁边。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾刘美娟停在赵强旁、沈清在茶几左侧、周桂兰靠木椅，第2组组首复述这些位置后再推进周桂兰瘫坐。",
      "fix_instruction": "若周桂兰突然坐下无过渡，应保留4-7秒瘫坐动作。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵强低声耳语是画面内真实开口且对象为刘美娟，镜头写清贴近耳边和嘴部不被遮住，不是心声或画外音误用。",
      "fix_instruction": "若改成心声，应写明嘴唇闭合；若是现场耳语，应保留可见开口和对象。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第3组禁止项锚定赵强、刘美娟、银行流水单、沈清和耳语风险，数量4条，未使用泛泛模板词。",
      "fix_instruction": "若禁止项无锚点，应改成本组具体人物和银行流水单相关错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
