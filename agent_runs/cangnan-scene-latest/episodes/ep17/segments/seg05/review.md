{
  "pass": true,
  "summary": "seg05分镜保留执法车到场、王局长停工命令、江若晴质问、地契压场、查封和拖官司风险，节奏通过。",
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
      "type": "dialogue_pacing",
      "evidence": "王局长约17字大喝停工安排5秒，含抬手指向挖掘机动作，字秒比和动作容量合理。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "地契在组首由王局长持有，5-9秒被举起展示为证，后续江若晴和陆凡看向地契，归属清楚。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "王局长'擅自开发私人领地'、执法队驱赶工人拉警戒线、江若晴提示官司拖几年均按原剧本保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王局长和执法队员在组首位于执法车内或车旁，4-7秒站到道路中央后再下命令。",
      "fix_instruction": "若不通过，应补入场动作或在组首明确人物可见位置。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组包含王局长查封台词、执法队拉警戒线、江若晴对陆凡焦急说明三个强节拍，15秒内有足够动作和口型时间。",
      "fix_instruction": "若不通过，应拆出拉警戒线或江若晴说明为独立短组。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部王局长站在主干道中央命令停工，第2组组首仍在主干道并手持地契，陆凡和江若晴位置连续。",
      "fix_instruction": "若不通过，应补充人物站位和地契取得状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
