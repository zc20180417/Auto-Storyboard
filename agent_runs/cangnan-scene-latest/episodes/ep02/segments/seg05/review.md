{
  "pass": true,
  "summary": "seg05已审核，陆凡向苏有光提交台账、苏有光压案以及陆凡云盘后手均保留，OS承载正确。",
  "checked_groups": ["第11组", "第12组"],
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
      "group": "第11组",
      "type": "script_fidelity",
      "evidence": "陆凡摆出台账、要求上报，苏有光擦汗并称复杂、民政办脱不了干系的台词均按原剧本保留。"
    },
    {
      "group": "第12组",
      "type": "audio_mouth_sync",
      "evidence": "陆凡OS被写为内心声音，画面中陆凡嘴唇闭合不做口型，没有误写成现场自语。"
    },
    {
      "group": "第12组",
      "type": "prop_continuity",
      "evidence": "第11组台账摆在桌上，第12组苏有光手掌压住台账并要求留下，道具归属变化清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第11组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第11组由入门摆台账和四轮短对话构成，台词分段清楚，15秒内没有过载。",
      "fix_instruction": "若不通过，应把摆台账和上报争论拆成两组。"
    },
    {
      "group": "第12组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第11组尾部台账在苏有光面前，第12组首继续保持台账位于桌面中央靠近苏有光一侧。",
      "fix_instruction": "若不通过，应补足台账从陆凡手中到桌面的状态。"
    },
    {
      "group": "第12组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "现场对白均明确陆凡对苏有光、苏有光对陆凡；OS未写成对话对象。",
      "fix_instruction": "若不通过，应把OS改为内心声音并写明闭口。"
    }
  ],
  "issues": [],
  "warnings": []
}
