{
  "pass": true,
  "summary": "seg01两组分镜通过审核，台词指向、音画分离、空间连续性均无问题。",
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
    {"group": "第1组", "type": "audio_mouth_sync", "evidence": "沈清OS'连续加了两个月夜班赶核心项目'正确标注画外音，嘴唇闭合不做口型。"},
    {"group": "第1组", "type": "dialogue_pacing", "evidence": "张姐电话7字/2秒=3.5字/秒，OS18字/4秒=4.5字/秒，均在合理范围。"},
    {"group": "第2组", "type": "handoff_continuity", "evidence": "G1组尾手机贴近耳边、铁门虚掩，G2组首手机握在手中、铁门虚掩，状态连续。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "audio_mouth_sync", "result": "pass", "evidence": "OS画外音与口型分离正确，嘴唇闭合不做口型写清楚。", "fix_instruction": "无需修改"},
    {"group": "第2组", "type": "handoff_continuity", "result": "pass", "evidence": "G1到G2状态连续，铁门虚掩、行李箱和营养品在手。", "fix_instruction": "无需修改"},
    {"group": "第2组", "type": "dialogue_pacing", "result": "pass", "evidence": "欣慰台词24字/5秒=4.8字/秒，困惑台词9字/2.5秒=3.6字/秒，节奏合理。", "fix_instruction": "无需修改"}
  ],
  "issues": [],
  "warnings": []
}
