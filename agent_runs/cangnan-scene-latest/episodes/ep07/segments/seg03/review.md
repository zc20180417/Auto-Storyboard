{
  "pass": true,
  "summary": "seg03已对照原剧本完成审核，赵大江听汇报、徐虎装病、伪造验伤和打压水头村的阴谋均保留，无硬问题。",
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
      "evidence": "第1组保留赵大江靠椅背听手机汇报、说“干得好，直接关进看守所”，以及徐虎说进看守所后找人教训陆凡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-3秒、3-6秒、6-9秒分别承载三句短台词，均约10-18字/3秒，未超过6.5字/秒。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "第1组固定在乡长办公室，赵大江在办公椅上持手机，徐虎在沙发上缠纱布装病，人物和道具可用性清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵大江对徐虎得意说话，徐虎对赵大江回应，现场对白对象明确，没有心声或电话音误作口型。",
      "fix_instruction": "若出现电话汇报内容，应写明来自手机听筒并让画面人物只做反应。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "徐虎组首头缠纱布，0-3秒拍胸脯说验伤报告，赵大江3-13秒夹烟、吐烟、按烟，纱布和烟的状态连续。",
      "fix_instruction": "若烟或纱布突然变化，应补持有、按灭或触碰等可见动作。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文为自然办公室对话和动作，没有模板编号、模型说明词、参考图、字幕或广告式语气。",
      "fix_instruction": "若出现模型说明词或模板污染，应改成可见动作、表情、道具和声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
