{
  "pass": true,
  "summary": "seg04完成警车到场、民警控制疯狗、陆凡说明证据并点名宋子昂，且明确疯狗无伤无吐血。",
  "checked_groups": ["第9组", "第10组", "第11组"],
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
      "group": "第9组",
      "type": "character_availability",
      "evidence": "民警甲、民警乙在组首位于警车内侧车门后方可见，先随警车到场下车，再执行控制动作。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "民警乙询问“你没事吧？”和陆凡说明绑架未遂、行车记录仪、手机录像均按原文保留。"
    },
    {
      "group": "第11组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“他的幕后主使是宋子昂，我会配合做笔录。”分配4.5秒，语速自然且口型清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "铁棒在疯狗身旁地面，手铐由民警乙控制疯狗时落锁，关键道具转移清楚。",
      "fix_instruction": "若不通过，应补铁棒落地位置和手铐扣住双手的可见动作。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第9组尾部疯狗被按倒铐住；第10组组首复述疯狗在地面且双手已被手铐扣住。",
      "fix_instruction": "若不通过，应在第10组组首明确疯狗仍在地面和民警控制状态。"
    },
    {
      "group": "第11组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本要求疯狗没有受伤、无吐血，本稿在第10组押起时明确可见，未新增受伤表现。",
      "fix_instruction": "若不通过，应删除任何受伤、吐血或过度打斗表现。"
    }
  ],
  "issues": [],
  "warnings": []
}
