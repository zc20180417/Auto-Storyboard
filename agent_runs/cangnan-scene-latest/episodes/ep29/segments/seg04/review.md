{
  "pass": true,
  "summary": "seg04保留矿洞外撤离确认、陆凡判断龙天傲仍在附近和远处警笛，短组均在10秒合同内。",
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
      "type": "script_fidelity",
      "evidence": "陆凡走出矿洞，林夏迎上并说“下面的人都撤出来了，一个不少。”，未漏改关键台词。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "陆凡看向远方并说“龙天傲应该还在附近。”，远处警笛声呼啸而过被保留。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "evidence": "警笛声写成远处山路警车灯光和由远及近的声音，现场人物不承担警笛口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定矿洞外入口、警戒线、陆凡、林夏和撤离人员位置，动作发生在同一矿洞外空间。",
      "fix_instruction": "若不通过，应补足洞口、警戒线和两人画面位置。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾陆凡视线转向远处道路，第8组首复述陆凡位于道路边并面向远处道路，状态连贯。",
      "fix_instruction": "若不通过，应在第8组组首复述陆凡和林夏的位置与视线方向。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "林夏台词约17字分配4秒，普通对话约4.25字/秒，承载自然。",
      "fix_instruction": "若不通过，应缩短反应动作或延长台词镜头到4秒以上。"
    }
  ],
  "issues": [],
  "warnings": []
}
