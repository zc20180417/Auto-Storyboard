{
  "pass": true,
  "summary": "seg02完成陆凡林夏入场、审计质问、吴总监甩假流水并下令控制的审核，无硬问题。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留推门入场、林夏质问、吴总监傲慢回应、陆凡问查出什么问题和吴总监指责胆大包天。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "打印流水单从吴总监手边到0-3秒被甩到陆凡面前，后续指控和林夏反驳均围绕该单据。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组3-14秒承载四句现场对白，单句时长均在自然口型范围内，未出现过快或拖慢。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡和林夏在0-3秒入场后才开口，吴总监在组首已站在会议桌旁可用。",
      "fix_instruction": "若不通过，应补入场动作或组首位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "吴总监对陆凡大喝，林夏对吴总监大惊反驳，命令手下方向明确，没有无对象台词。",
      "fix_instruction": "若不通过，应补充说话对象或声音来源。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "甩流水单、指控、林夏反驳、下令控制分为14秒内4个清楚节拍，没有把安保逼近塞入同组。",
      "fix_instruction": "若不通过，应拆分指控和控制动作。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文只包含自然短剧分镜描述，没有Seedance说明、模板编号或占位符。",
      "fix_instruction": "若不通过，应删除工程说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
