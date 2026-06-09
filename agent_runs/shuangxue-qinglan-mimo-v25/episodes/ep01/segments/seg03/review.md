{
  "pass": true,
  "summary": "seg03四组分镜通过审核，杂物间空间锁定、道具连续性、台词节奏均合格。",
  "checked_groups": ["第4组", "第5组", "第6组", "第7组"],
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
    {"group": "第4组", "type": "space_locking", "evidence": "杂物间单一物理空间，组首锁定周桂兰在硬板床上。"},
    {"group": "第5组", "type": "prop_continuity", "evidence": "破瓷碗从G4暴露到G5白粥特写，状态连续。"},
    {"group": "第6组", "type": "script_fidelity", "evidence": "羽绒服、进口药、八千块三条质问线完整保留。"}
  ],
  "semantic_checks": [
    {"group": "第4组", "type": "handoff_continuity", "result": "pass", "evidence": "G3组尾沈清走向后院，G4组首沈清在门外，空间转换合理。", "fix_instruction": "无需修改"},
    {"group": "第5组", "type": "prop_continuity", "result": "pass", "evidence": "破瓷碗从藏在被子里到暴露在床面上，状态连续。", "fix_instruction": "无需修改"},
    {"group": "第6组", "type": "action_atomicity", "result": "pass", "evidence": "每组每个时间段只承载一个主动作。", "fix_instruction": "无需修改"},
    {"group": "第7组", "type": "dialogue_pacing", "result": "pass", "evidence": "八千块质问台词节奏合理。", "fix_instruction": "无需修改"}
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第6组",
      "rule": "script_fidelity",
      "problem": "12.5-15秒时间段将原剧本'我每个月按时给你打八千块'微缩为'我每月给你八千块'，核心指控保留。",
      "fix": "如需严格还原，可将该时间段延长至3秒。"
    }
  ]
}
