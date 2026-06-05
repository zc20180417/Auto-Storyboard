{
  "pass": true,
  "summary": "seg01完成院门外转账与院内生日残迹发现，未发现硬问题。",
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
    {"group": "第1组", "type": "audio_mouth_sync", "evidence": "沈清对手机里的张姐现场说话，内心旁白段明确嘴唇闭合不做口型，转账屏幕为可见载体。"},
    {"group": "第1组", "type": "dialogue_pacing", "evidence": "内心旁白约24字占4秒，约6字/秒；末句约25字占4秒，约6.25字/秒，均未超过6.5硬上限。"},
    {"group": "第2组", "type": "script_fidelity", "evidence": "保留推开虚掩雕花铁门、院子帝王蟹包装盒、三层翻糖蛋糕空盒、沈清疑问‘帝王蟹？家里办大寿？’。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "space_locking", "result": "pass", "evidence": "组首锁定周家院门外单一空间，列出沈清、手机、掉轮行李箱和营养品位置。", "fix_instruction": "若院子垃圾进入第1组，应拆到第2组。"},
    {"group": "第1组", "type": "prop_continuity", "result": "pass", "evidence": "手机从通话界面到转账界面再收起，行李箱和营养品在组尾仍锚定。", "fix_instruction": "若手机或行李箱消失，应在组尾补状态。"},
    {"group": "第2组", "type": "generation_density", "result": "pass", "evidence": "第2组承载推门入院、看包装盒、短句疑问三个清晰节拍，总时长10秒不过载。", "fix_instruction": "若加入进入正屋动作，应另起客厅组。"},
    {"group": "第2组", "type": "video_negative_constraints", "result": "pass", "evidence": "禁止项锚定帝王蟹包装盒、三层翻糖蛋糕空盒、沈清、营养品，4条具体风险。", "fix_instruction": "若禁止项泛泛，应替换为本组具体道具。"}
  ],
  "issues": [],
  "warnings": []
}
