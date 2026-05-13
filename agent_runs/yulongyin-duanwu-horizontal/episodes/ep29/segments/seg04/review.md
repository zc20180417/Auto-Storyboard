{
  "pass": true,
  "summary": "seg04已审核金色小鲤鱼、水皇冠和天天回应云宝的收尾，奇观动作按原剧本呈现，未新增剧情。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留河面涟漪、金色小鲤鱼跃出、水花凝成透明水皇冠并落到天天头顶化雾的原剧本动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "天天台词约17字放在0-4秒，约4.25字/秒，适合大笑后的情绪表达。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "天天固定在左侧青石板，右侧河道深处留出回应空间，挥手方向从左指向右，横屏轴线清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "水皇冠以水花凝聚和逆光水雾呈现，奇观动作可视化明确，没有抽象说明替代画面。",
      "fix_instruction": "无需修复；视觉因果已经清楚。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "天天现场对河道深处喊话，画面右侧无实体但对象是云宝，嘴唇开合和声音来源明确。",
      "fix_instruction": "无需修复；若改画外音需注明来源。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图占位、首尾帧说明或视频延长等工程词。",
      "fix_instruction": "无需修复；继续保持自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
