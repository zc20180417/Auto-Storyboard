{
  "pass": true,
  "summary": "第2-3组保留大厅对峙、龙天傲求救、龙万山怒斥、陆凡扔人、龙万山命令安保和甩棍逼近，未发现硬问题。",
  "checked_groups": ["第2组", "第3组"],
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "龙万山端坐、四名顶级保镖、龙天傲求救、龙万山怒斥和陆凡说“你的废物儿子，还给你”后扔人均与原剧本一致。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "龙万山“拿下他！别让他站着走出这里！”约15字分配3.5秒，字秒比约4.3，符合情绪台词承载。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾部龙天傲摔在龙万山脚下，第3组组首复述龙天傲低伏在龙万山脚边，人物状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙天傲对龙万山惨叫，龙万山对陆凡厉声说，陆凡对龙万山冷声说，对象明确且台词原文保留。",
      "fix_instruction": "若不通过，应逐句补足真实说话对象。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "甩棍在组首为保镖身侧可见道具，6.5-11秒明确抽出并甩开，归属和动作过渡清楚。",
      "fix_instruction": "若不通过，应补充甩棍从何处被取出。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组14秒承载大厅压迫、两句情绪对白和一次扔人动作，动作与台词分段清楚，没有把安保进攻塞入同组。",
      "fix_instruction": "若不通过，应把扔人或保镖逼近拆到下一组。"
    }
  ],
  "issues": [],
  "warnings": []
}
