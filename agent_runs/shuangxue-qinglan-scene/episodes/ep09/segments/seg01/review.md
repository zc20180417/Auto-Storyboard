{
  "pass": true,
  "summary": "seg01 保留了沈清摔出银行流水、质问养老钱去向、赵强装傻和刘美娟附和的原剧本顺序，三组格式、口型、道具连续性和短句节奏均可交付。",
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
      "type": "script_fidelity",
      "evidence": "原剧本中赵强喝茶、沈清冲进来、流水单啪地摔在茶几上、沈清怒斥和赵强装傻均按顺序保留，没有新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "银行流水单从第1组组尾的茶几中央延续到第2组组首，沈清按住并指向转账记录，赵强茶杯抖洒茶水后仍在手中。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟约18字台词给2.5秒，沈清约18字反击给3秒，均不超过6.5字/秒；9秒短组承载短句交锋和反应，属于可接受短组。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清明确对赵强说道，赵强明确对沈清装傻回应，现场真人对白都有真实对象。",
      "fix_instruction": "若缺少对象，应改为沈清对赵强说道、赵强对沈清说道。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第2组按点记录、质问、茶杯抖洒、赵强强装镇定回应分段，每个时间段只承担一个主动作或对白节拍。",
      "fix_instruction": "若动作混在同一时间段，应拆出茶杯抖洒和赵强回应。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾的赵强握杯、流水单在茶几、沈清站在茶几左侧，都被第3组组首复述，人物和道具状态连续。",
      "fix_instruction": "若缺少状态，应在第3组组首补流水单、赵强茶杯和刘美娟位置。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组视频禁止项锚定银行流水单、赵强、周桂兰、茶杯，均是本组关键道具和人物风险，数量为4条。",
      "fix_instruction": "若出现泛泛禁止项，应替换为本组人物和道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
