{
  "pass": true,
  "summary": "seg05保留逼问宋子昂位置、民警记录口供、陆凡给江若晴披外套并配合做笔录的收尾。",
  "checked_groups": ["第12组", "第13组"],
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
      "group": "第12组",
      "type": "dialogue_direction",
      "evidence": "陆凡对疯狗问“宋子昂在哪？”，疯狗对陆凡回答会所位置，民警甲对陆凡和民警乙确认“口供已录”。"
    },
    {
      "group": "第12组",
      "type": "script_fidelity",
      "evidence": "天宫会所顶楼包厢的地点信息完整保留，未改成其他地点。"
    },
    {
      "group": "第13组",
      "type": "handoff_continuity",
      "evidence": "疯狗从第12组被押在警车旁，进入第13组仍在警车旁被民警控制，随后上警车。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第12组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "三句短对白分别分配2秒、3.5秒、3.5秒并配合记录动作，未出现过快口型。",
      "fix_instruction": "若不通过，应缩短记录动作或拆出单独问答组。"
    },
    {
      "group": "第13组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "外套在组首属于陆凡，0-4秒清楚表现脱下并披到江若晴肩上。",
      "fix_instruction": "若不通过，应补陆凡脱下外套再披上的可见过渡。"
    },
    {
      "group": "第13组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "披外套、陆凡向民警表态、押疯狗上车、扶江若晴走向越野车四个节拍分布在12秒内，动作链连续且不含长台词。",
      "fix_instruction": "若不通过，应将押车或扶江若晴离开拆成下一组。"
    }
  ],
  "issues": [],
  "warnings": []
}
