{
  "pass": true,
  "summary": "seg02完成客厅生日布置、喊母亲、听见后院咳嗽并离开，未发现硬问题。",
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
    {"group": "第1组", "type": "script_fidelity", "evidence": "保留水晶吊灯彩带气球、祝小雨十岁生日快乐烫金字、名牌童装包装袋和沈清把营养品放上茶几。"},
    {"group": "第2组", "type": "audio_mouth_sync", "evidence": "后院咳嗽声作为环境声源出现，沈清现场开口‘这声音……是妈？’并未替咳嗽声做口型。"},
    {"group": "第2组", "type": "handoff_continuity", "evidence": "第1组尾沈清站在茶几旁且营养品已放下，第2组首复述电视机、茶几、营养品和沈清位置。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "space_locking", "result": "pass", "evidence": "组首限定周家正屋客厅，人物只有沈清，没有提前出现周桂兰。", "fix_instruction": "若出现周桂兰，应移到杂物间段。"},
    {"group": "第1组", "type": "dialogue_direction", "result": "pass", "evidence": "沈清对空荡客厅大声喊母亲，符合呼喊母亲的现场对白语境。", "fix_instruction": "若需要更明确对象，可写对屋内喊道。"},
    {"group": "第2组", "type": "action_atomicity", "result": "pass", "evidence": "空客厅环顾、后院咳嗽、转身离开分成三个时间段，每段一个主动作或声音反应。", "fix_instruction": "若把咳嗽和离开压成一镜，应拆开。"},
    {"group": "第2组", "type": "video_negative_constraints", "result": "pass", "evidence": "禁止项锚定行李箱、营养品、咳嗽声、周桂兰，4条具体风险且不矛盾。", "fix_instruction": "若禁止项无锚点，应重写。"}
  ],
  "issues": [],
  "warnings": []
}
