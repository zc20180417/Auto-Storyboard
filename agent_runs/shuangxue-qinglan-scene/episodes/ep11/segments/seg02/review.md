{
  "pass": true,
  "summary": "seg02保留王婶递药袋、止痛片空壳揭示和沈清质问十九万理财的情绪转折，审核未发现 hard issue。",
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
      "evidence": "原剧本的周家院门外、王婶手拿塑料袋并说明昨晚掉在门口的药袋子均保留，未改变人物关系。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "塑料袋从第1组尾停在三人中间，到第2组由沈清接过打开，空止痛片和空药盒有清楚揭示。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "王婶20字台词给4秒，沈清约21字质问给4.5秒，均低于6.5字/秒且有明确对话对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首为周家院门外单一物理空间，沈清、周桂兰、王婶位置和身体朝向完整。",
      "fix_instruction": "若不通过，应补齐每个人的画面位置和身体朝向。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "沈清询问、接过打开袋子、空药露出、王婶解释被分成四个时间段，没有把递物和长台词挤在同一镜。",
      "fix_instruction": "若不通过，应拆开递接物、打开袋口和解释台词。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载王婶补充说明、沈清捏紧空药盒和情绪质问，12秒有道具状态变化和冲突升级支撑。",
      "fix_instruction": "若不通过，应压缩或拆分低密度动作，但不得删掉空药盒情绪锚点。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定空药盒、沈清和王婶，避免药盒状态、人物位置和台词归属错误。",
      "fix_instruction": "若不通过，应用本组人物名或药盒/塑料袋替换无锚点表述。"
    }
  ],
  "issues": [],
  "warnings": []
}
