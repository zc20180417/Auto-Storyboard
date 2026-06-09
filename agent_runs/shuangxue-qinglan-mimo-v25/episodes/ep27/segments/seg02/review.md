{
  "pass": true,
  "summary": "第3-4组审核通过，警察入场和赵强被捕场景格式正确、台词节奏合理。",
  "checked_groups": ["第3组", "第4组"],
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
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "警察台词26字/4秒=6.5字/秒，赵强台词6字/1秒=6字/秒，均未超过硬上限。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "12秒内3个强节拍各占独立时间段，无过载。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首列出全部6名在场人物位置和朝向，均为同一物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "警察对赵强说话对象明确，赵强喃喃自语写明对地面。",
      "fix_instruction": "若不通过，应检查说话对象是否明确。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作：出示证件、瘫软反应、手铐铐上、转身，无过载。",
      "fix_instruction": "若不通过，应拆分时间段。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾宴会厅内其他人物位置未变，第3组组首赵强、周美娟等均在原位。",
      "fix_instruction": "若不通过，应在组尾补具体状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
