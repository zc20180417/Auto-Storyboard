{
  "pass": true,
  "summary": "seg04将山巅独处、加密电话和海外财团潜入信息以电话音承载，音画分离和台词节奏通过。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "商会总管台词来自电话，画面中的陆凡嘴唇闭合不做口型，手机亮屏和贴耳动作提供声音载体。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "商会总管长句约45字用9.5秒，约4.7字/秒；目标句约18字用4秒，约4.5字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "evidence": "第8组全程位于黑风山顶，海外信息通过电话音传来，没有把海外地点写成现实转场。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "商会总管只以电话音出现，陆凡和加密手机在组首及镜头中均可见。",
      "fix_instruction": "若不通过，应补充电话来源或改为现场人物入场。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "龙家覆灭惊动罗斯柴尔德、商业间谍潜入和夺取稀土控制权三项关键信息完整保留。",
      "fix_instruction": "若不通过，应恢复原剧本的信息顺序和目标对象。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为电话信息揭示，动作负载仅陆凡听电话和握紧手机，15秒内不拥挤。",
      "fix_instruction": "若不通过，应拆分长电话信息或减少无关动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
