{
  "pass": true,
  "summary": "seg03完成砸碗、当众质问、周建国举杯和赵强电话泄露，动作与道具拆段可执行。",
  "checked_groups": ["第6组", "第7组", "第8组", "第9组"],
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
    {"group": "第6组", "type": "action_atomicity", "evidence": "沈清走到桌前、砸下缺口碗、汤汁飞溅和全场停住分成3个时间段，未把砸碗和质问挤在同一段。"},
    {"group": "第7组", "type": "dialogue_pacing", "evidence": "沈清质问约30字占6秒约5字/秒，刘美娟反击约25字占5秒约5字/秒，均低于6.5硬上限。"},
    {"group": "第9组", "type": "script_fidelity", "evidence": "第9组保留周建国举酒杯要砸、赵强从门外进来、握手机捂嘴低声打电话和原台词‘账上的钱千万别动……’。"}
  ],
  "semantic_checks": [
    {"group": "第6组", "type": "prop_continuity", "result": "pass", "evidence": "第6组首沈清端缺口碗入客厅，3-5秒碗砸到主桌中央，组尾碗和汤汁留在桌面。", "fix_instruction": "若碗未留在主桌，应补桌面位置。"},
    {"group": "第7组", "type": "dialogue_direction", "result": "pass", "evidence": "沈清对刘美娟质问，刘美娟对沈清反击，现场对白对象明确。", "fix_instruction": "若只写台词不写对象，应补A对B说道。"},
    {"group": "第8组", "type": "generation_density", "result": "pass", "evidence": "第8组承载三句冲突对白和酒杯预备动作，酒杯真正抬起留到第9组，未过载。", "fix_instruction": "若酒杯砸出也放入第8组，应拆到后续组。"},
    {"group": "第9组", "type": "character_availability", "result": "pass", "evidence": "赵强在第6-9组组首均位于客厅门外侧阴影处或门口内侧，电话台词前有入场动作和手机载体。", "fix_instruction": "若赵强未在组首或入场前可用，应补门外阴影位置。"},
    {"group": "第9组", "type": "audio_mouth_sync", "result": "pass", "evidence": "赵强电话内容写为压低声音对电话另一端说道，属于现场真实低声通话，手机亮屏为载体。", "fix_instruction": "若写成旁白或无来源音，应改为电话通话。"},
    {"group": "第9组", "type": "video_negative_constraints", "result": "pass", "evidence": "第9组禁止项锚定周建国酒杯、赵强手机、赵强挂断电话和缺口碗，4条具体风险。", "fix_instruction": "若禁止原剧本必须发生的举杯，应改为禁止砸中沈清。"}
  ],
  "issues": [],
  "warnings": [
    {"severity": "soft", "group": "第6组", "rule": "generation_density", "problem": "第6组为9秒短组。", "evidence": "内容是端碗进入、砸碗、汤汁溅出和全场反应，属于道具插入与短动作余波，短组理由成立。", "fix": "交付时说明该短组用于砸碗打断，不需要硬凑到10秒。"}
  ]
}
