{
  "pass": true,
  "summary": "seg01共7组已按剧本与分镜规则复审，重复台词、景别和节奏硬问题均已清除。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留苏清寒尖叫、朱文浩OS、安保砸门画外音和朱文浩披浴袍倒两杯红酒；未再重复第2组的药物与做局台词。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组场景为苏家别墅书房，苏长明、龙图腾字画、抹布、手机均在同一书房空间内完成，没有未标注跨空间硬切。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "第5组每个有台词时间段为2秒，'他连亲生女儿声誉都牺牲？'14字/2秒=7.0字/秒，偏快但不超过硬错误阈值。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组到第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以朱文浩手持红酒杯看向苏清寒收尾，第2组组首承接为朱文浩手持红酒杯站在床前，苏清寒仍在床上。道具与位置连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "第6组苏清寒台词已写为对朱文浩低声说道'我绝不当争权夺利的牺牲品。'，对话对象不再错写成苏清寒本人。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第7组",
      "type": "filmability",
      "result": "pass",
      "evidence": "朱文浩提出'恶性丑闻，变成家族联姻'和'颠倒乾坤'均以人物低语、视线、表情和苏清寒反应呈现，没有把抽象策略当作不可拍画面。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "情绪台词语速偏快但可接受",
      "evidence": "第5组6-8秒'他连亲生女儿声誉都牺牲？'14字/2秒=7.0字/秒。",
      "fix": "如需更稳可延至3秒，但当前未超过硬错误阈值。"
    },
    {
      "severity": "soft",
      "group": "第6组",
      "rule": "dialogue_pacing",
      "problem": "情绪台词语速偏快但可接受",
      "evidence": "第6组4-6秒'我绝不当争权夺利的牺牲品。'14字/2秒=7.0字/秒。",
      "fix": "如需更稳可延至3秒，但当前未超过硬错误阈值。"
    }
  ]
}
