{
  "pass": true,
  "summary": "seg01共11组，忠于原剧本1-1场景全部内容，格式规范，空间锁定完整，无硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "generation_density": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "朱文浩OS'昨晚的聚会是个连环杀局'9字2秒=4.5字/秒，画外音4.5字/秒符合目标值。苏清寒'你毁了我'5字2秒=2.5字/秒，情绪对白偏慢但属短台词豁免。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "朱文浩4句连续台词39字在4秒时间段内按连续对话节拍处理，加递酒动作约9.7秒。6个强节拍在14秒组内密度偏高但每个节拍有独立时间段。"
    },
    {
      "group": "第11组",
      "type": "space_locking",
      "evidence": "第11组包含酒店地下车库和主观想象闪回两个空间，已在时间段中明确标注'主观想象闪回'，符合Seedance片段空间规则的例外条件。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩和苏清寒均在组首空间锁定中有明确位置，走廊安保以画外音和门缝人影方式出现。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "苏长明书房密谋完整保留，交叉剪辑标识明确，龙图腾字画和手机通话均为可见可拍内容。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第10组",
      "type": "filmability",
      "result": "pass",
      "evidence": "朱天和以电话音画外音方式出现，写明来源和可见载体（手机），朱文浩在驾驶座做反应，音画分离正确。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "generation_density",
      "problem": "强节拍密度边界",
      "evidence": "6个强节拍在14秒组内密度偏高。",
      "fix": "可选合并部分节拍。"
    },
    {
      "severity": "soft",
      "group": "第11组",
      "rule": "generation_density",
      "problem": "闪回与OS叠加",
      "evidence": "闪回4画面快速切换加3句OS，4个强节拍在10秒组内。",
      "fix": "可选延长闪回时间段。"
    }
  ]
}