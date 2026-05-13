{
  "pass": true,
  "summary": "seg02已对照原剧本完成审核，做笔录、林夏到场、县委通报、正当防卫判断、传真威慑和收队均保留，无硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "第1组保留老张看完视频后要求陆凡回去做笔录、陆凡同意配合、警察准备带人上车以及林夏乘黑色奥迪急刹赶到喊“慢着”。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组把林夏关于县委表扬通报的长台词拆成3-9秒、9-12秒、12-15秒三段，单段均有足够朗读时间。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组仍在水头村村口，林夏、老张、陆凡、警察和文件在组首均有明确位置，后续威慑和收队不跨空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "老张对林夏解释徐虎报案，林夏对老张说明不能凭一面之词和陆凡正当防卫，所有现场对白对象明确。",
      "fix_instruction": "若出现无对象对白，应补为对林夏、对老张或对陆凡说道。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "林夏组首手中持有盖章文件，3-9秒递到老张面前，9-12秒指向公章，12-15秒推到老张眼前，文件状态连续。",
      "fix_instruction": "若文件突然出现在老张手里，应补递出、接过或推近动作。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部老张下令收队，第5组组首警车和警察仍在村口并开始离开，随后林夏对陆凡交代继续盯路，状态连续。",
      "fix_instruction": "若警车状态跳变，应在第4组尾部或第5组开头补上上车离开的动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
