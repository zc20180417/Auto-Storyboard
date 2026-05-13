{
  "pass": true,
  "summary": "seg01已对照原剧本完成审核，台词、武器放下动作、陆凡追责和宋天明威胁均保留，未发现硬问题。",
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
      "evidence": "保留宋天明质疑最高裁决官、独眼老者确认龙纹印记、黑衣人放下武器三项原剧本关键信息。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组3.5-8秒承载宋天明18个有效字，4.5秒约4.0字/秒；10.5-15秒承载19个有效字，4.5秒约4.2字/秒，未超过上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首复述陆凡、宋天明、独眼老者和黑衣人们在同一包厢内的位置、朝向和武器低垂状态，与第1组尾部连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋天明对陆凡说，独眼老者对黑衣人们说，对白对象明确，没有假对象。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对话对象。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "武器从组首手中持有到9-14秒低垂在腿侧，动作过渡可见。",
      "fix_instruction": "若不通过，应补充武器放下或归属变化的可见动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组为连续追责和赔偿交锋，4个时间段分别承载逼问、赔偿、冷笑回应、威胁，强节拍清楚且未塞入额外事件。",
      "fix_instruction": "若不通过，应拆出威胁或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
