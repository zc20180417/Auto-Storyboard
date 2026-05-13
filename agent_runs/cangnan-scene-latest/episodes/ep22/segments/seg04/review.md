{
  "pass": true,
  "summary": "seg04完成砸主机未遂、经侦封存设备、镇纸被夺和林夏冷讽的审核，无硬问题。",
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
      "type": "script_fidelity",
      "evidence": "第1组保留吴总监命令砸电脑、两名手下扑向主机、陆凡挡在主机前并喊经侦同志的动作和台词。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾陆凡挡主机、手下被拦，第2组首复述相同状态，并让经侦警察从门外冲入拦人。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "镇纸在组首位于吴总监手边，0-3秒由吴总监抓起，3-6秒被经侦警察夺下，转移明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "下令、手下扑向主机、陆凡挡住和喊话分成4段12秒，动作链清楚，没有强行塞入警察入场。",
      "fix_instruction": "若不通过，应拆分手下扑向主机和警察入场。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "经侦警察对两名手下大喝，吴总监对陆凡咬牙，现场对白对象明确。",
      "fix_instruction": "若不通过，应补对话对象。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡、吴总监、经侦警察、林夏均在组首写明位置和朝向，发声和动作前均可用。",
      "fix_instruction": "若不通过，应补林夏或警察组首位置。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全段没有模板化批量描述、Seedance说明或占位符。",
      "fix_instruction": "若不通过，应清除污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
