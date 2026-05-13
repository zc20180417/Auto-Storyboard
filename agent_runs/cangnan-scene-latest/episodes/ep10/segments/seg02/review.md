{
  "pass": true,
  "summary": "seg02三组完整覆盖追捕、制服、录音取证和移交刑侦，没有发现硬问题。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首把黄毛、打手、陆凡、民警甲、民警乙都锁定在树林深处同一物理空间，追捕路线清楚。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留陆凡抓衣领绊倒打手、民警乙铐住打手、陆凡逼问黄毛、黄毛供出赵大江。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "黄毛供述约22字在3-8.5秒的5.5秒内完成，哭腔语速约4字/秒，配合发抖状态可接受。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "追跑、包抄、喊话、黄毛摔倒四个动作节拍分布在13秒内，没有把抓捕和审讯硬塞在同组。",
      "fix_instruction": "若不通过，应把黄毛摔倒后的按住动作拆到下一组。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "民警乙对打手、陆凡对黄毛、黄毛对陆凡的对白对象明确，没有假对象。",
      "fix_instruction": "若不通过，应把每句现场对白改成A对B说道格式。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "录音笔由民警乙持有并打开，随后举到黄毛面前取证，道具归属和用途连续。",
      "fix_instruction": "若不通过，应补录音笔从民警乙手中打开并靠近黄毛的过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
