{
  "pass": true,
  "summary": "seg04一组分镜通过审核，刘美娟VO音画分离正确，沈清咬牙自语指向清晰。",
  "checked_groups": ["第8组"],
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
    {"group": "第8组", "type": "audio_mouth_sync", "evidence": "刘美娟VO正确标注画外音，沈清嘴唇闭合不做口型，咬牙自语为真实开口。"},
    {"group": "第8组", "type": "handoff_continuity", "evidence": "G7组尾沈清站在床边、周桂兰蜷坐床上，G8组首沈清靠在门框上、周桂兰仍在床上，位置转换有退后两步撞门框动作衔接。"},
    {"group": "第8组", "type": "dialogue_pacing", "evidence": "刘美娟VO'老公这月到账真准'10字/2秒=5字/秒，'小雨钢琴课尾款'14字/2.5秒=5.6字/秒，节奏合理。"}
  ],
  "semantic_checks": [
    {"group": "第8组", "type": "audio_mouth_sync", "result": "pass", "evidence": "VO与口型分离正确，沈清闭口听VO，然后咬牙自语。", "fix_instruction": "无需修改"},
    {"group": "第8组", "type": "handoff_continuity", "result": "pass", "evidence": "G7到G8空间从杂物间内到杂物间门口，沈清退后两步撞门框动作清晰衔接。", "fix_instruction": "无需修改"},
    {"group": "第8组", "type": "dialogue_pacing", "result": "pass", "evidence": "VO台词和自语台词字秒比合理。", "fix_instruction": "无需修改"}
  ],
  "issues": [],
  "warnings": []
}
