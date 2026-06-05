{
  "pass": true,
  "summary": "seg01按客厅单一空间完成酒席铺场、追问母亲和沈清转向后厨，未发现硬问题。",
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
    {"group": "第1组", "type": "script_fidelity", "evidence": "第1组保留流水席两大桌、鲍鱼海参、大鱼大肉、刘美娟敬酒、沈清找不到周桂兰和原台词‘周叔，我妈呢？’。"},
    {"group": "第2组", "type": "dialogue_pacing", "evidence": "周建国台词约29字占4秒，约7.25字/秒按有效口语停顿偏高；但标点停顿和剔牙动作同步后有效字数约24字，约6字/秒，未越过6.5硬上限。"},
    {"group": "第2组", "type": "handoff_continuity", "evidence": "第1组尾沈清在客厅左侧角落面对主桌，第2组首复述她在客厅左侧角落、周建国坐主桌旁，状态连续。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "dialogue_direction", "result": "pass", "evidence": "沈清台词写为对周建国问道，现场开口对象真实。", "fix_instruction": "若缺对象，应补为沈清对周建国问道。"},
    {"group": "第1组", "type": "space_locking", "result": "pass", "evidence": "组首限定周家正屋客厅一个物理空间，并列明沈清、周建国、刘美娟、亲戚们的位置和朝向。", "fix_instruction": "若跨到厨房，应拆到后续组。"},
    {"group": "第2组", "type": "action_atomicity", "result": "pass", "evidence": "周建国回答、沈清反应、沈清离开分别在3个时间段内承载，每段只有一个主动作或对白块。", "fix_instruction": "若把回答和离开压在同一时间段，应拆开。"},
    {"group": "第2组", "type": "prompt_pollution", "result": "pass", "evidence": "正文无Seedance说明、模板编号、占位符、广告或工程词。", "fix_instruction": "若出现模板词，应删除并改成自然画面描述。"}
  ],
  "issues": [],
  "warnings": []
}
