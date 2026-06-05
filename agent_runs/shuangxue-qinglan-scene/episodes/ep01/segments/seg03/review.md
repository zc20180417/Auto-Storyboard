{
  "pass": true,
  "summary": "seg03完成杂物间发现周桂兰、冷粥、冻疮、羽绒服和药钱追问，短组第5组理由成立。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
    {"group": "第1组", "type": "script_fidelity", "evidence": "保留破旧门、冷风、纸皮箱、生锈农具、周桂兰蜷在缺腿硬板床并藏破瓷碗。"},
    {"group": "第2组", "type": "dialogue_pacing", "evidence": "第2组末连续对白约32字占5秒，约6.4字/秒，未超过6.5硬上限。"},
    {"group": "第5组", "type": "generation_density", "evidence": "第5组8秒只承载周桂兰‘一分钱都没收到’和沈清后退撞门框，是单句反应和短动作余波，短组成立。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "character_availability", "result": "pass", "evidence": "沈清在组首位于木门外侧阴影处，推门后再进入对话；周桂兰在床上可见。", "fix_instruction": "若沈清未在组首或无入场动作，应补门外位置。"},
    {"group": "第2组", "type": "prop_continuity", "result": "pass", "evidence": "第1组尾破瓷碗被藏进棉被边缘，第2组掀开棉被后破瓷碗露出，冷粥与咸菜丝清楚。", "fix_instruction": "若碗直接出现在沈清手中，应补掀被过渡。"},
    {"group": "第3组", "type": "script_fidelity", "result": "pass", "evidence": "保留冻疮裂口、沈清追问羽绒服、周桂兰没看见新衣服、美娟说那是自己买的。", "fix_instruction": "若改成周桂兰穿着羽绒服，应恢复旧毛衣和未收到衣服。"},
    {"group": "第4组", "type": "filmability", "result": "pass", "evidence": "进口药和舍不得买通过台词承载，旧毛巾作为可见替代物锚定周桂兰只用热毛巾敷腿。", "fix_instruction": "若只写关节痛抽象感受，应补旧毛巾可见道具。"},
    {"group": "第5组", "type": "action_atomicity", "result": "pass", "evidence": "周桂兰落泪说没收到钱、沈清追问并后退撞门框分两段，动作清楚。", "fix_instruction": "若同时冲出杂物间，应另起下一场门外组。"},
    {"group": "第5组", "type": "video_negative_constraints", "result": "pass", "evidence": "禁止项锚定周桂兰、沈清、破瓷碗、旧毛巾，4条具体风险。", "fix_instruction": "若禁止项禁止后退撞门框则与正文矛盾，应删除。"}
  ],
  "issues": [],
  "warnings": [
    {"severity": "soft", "group": "第5组", "rule": "generation_density", "problem": "第5组为8秒短组。", "evidence": "该组是‘一分钱都没收到’的单句反应和沈清后退撞门框的短动作余波，符合短组例外。", "fix": "无需硬凑10秒；保持短促反应。"}
  ]
}
