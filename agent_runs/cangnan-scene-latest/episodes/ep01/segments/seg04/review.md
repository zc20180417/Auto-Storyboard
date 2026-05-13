{
  "pass": true,
  "summary": "seg04 保留河滩抢救、林夏苏醒、追问姓名和陆凡离开，OS闭口处理正确。",
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
      "evidence": "保留陆凡把林夏平放河滩、喊醒、判断心肺复苏、按压胸口和人工呼吸的救援动作。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留林夏吐水醒来、“是你……救了我”、警笛救护车声、陆凡“你没事就好”、林夏问姓名和陆凡入林。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "林夏OS写明嘴唇闭合不做口型，声音来源为内心旁白。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "抢救动作被拆为平放、喊醒、判断、按压、人工呼吸五段，15秒内未叠加额外长对白。",
      "fix_instruction": "若不通过，应拆出CPR动作或减少非关键反应。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾林夏手指轻动但未醒，第2组首林夏仍仰躺在地，随后咳水醒来，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首复述林夏仰躺和陆凡跪在旁边。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "12-15秒承载林夏问句、陆凡离开和短OS，台词量低于6.5字/秒，且有离开动作支撑。",
      "fix_instruction": "若不通过，应拆分追问和OS。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文为自然分镜描述，没有模型词、模板化批量句或占位符。",
      "fix_instruction": "若不通过，应删除污染内容。"
    }
  ],
  "issues": [],
  "warnings": []
}
