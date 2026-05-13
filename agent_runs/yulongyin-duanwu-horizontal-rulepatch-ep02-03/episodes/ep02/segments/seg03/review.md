{
  "pass": true,
  "summary": "seg03 三组将入壶封盖、卧室安顿和水雾龙舟线索拆开处理，远距离转场、壶盖连续、命名前称谓和道具文字风险均可通过。",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组", "第3组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "prop_continuity": "checked",
    "physical_continuity": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "第1组先写小龙爬入斜立水壶，再写天天扶正水壶，最后从左膝旁拿起壶盖并拧紧，组尾封盖状态有镜头来源。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留做贼一样抱回卧室、放到书桌、贴近观察、安抚台词和自责台词，没有提前命名云宝。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "evidence": "第3组龙舟信息由水雾轮廓和天天台词共同表达，不依赖模型生成准确中文小字。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "水壶从斜立入壶到竖立封盖有连续动作，且壶口高于水面、清水留在壶底，没有平放漏水矛盾。",
      "fix_instruction": "若不通过，应补充水壶斜立、扶正、壶盖来源和水面稳定的连续动作。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "天天全程用他和角色名描述，没有性别代词错误；小龙命名前仍称小龙。",
      "fix_instruction": "若不通过，应把错误代词改回他或天天，并在命名前统一称小龙。"
    },
    {
      "group": "第3组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "第3组从小龙睁眼回应，到尾巴划水雾，再到龙舟轮廓和天天疑问，信息递进清楚。",
      "fix_instruction": "若不通过，应重建小龙回应、划动、图形出现、天天问话的因果顺序。"
    }
  ],
  "issues": [],
  "warnings": []
}
