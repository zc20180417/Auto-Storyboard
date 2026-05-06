{
  "pass": true,
  "summary": "seg02三组完整保留朱文浩入场、朱天和锁账户、证据账本和苏长明债务雷反击，硬性规则通过。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留大门被踹开、朱文浩走入、朱天和紧随其后并说“我干的”，苏长明质问离岸账户，朱文浩举防火袋说明洗钱冻结。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组“盛大建工，红星工厂，两亿黑洞。”约12个有效字用2秒，“私刻公章，伪造债权，哪一条不够你死？”约15个有效字用3秒，均未低于节奏底线。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组仍在集团财务中心，账本、操作台和红色冻结大屏幕都在同一物理空间内，未发生跨场景硬切。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定写明苏长明在大屏幕前、朱文浩在门口、朱天和在朱文浩身后，三人都有画面位置和身体朝向。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾朱文浩举防火袋，第2组首朱文浩继续持防火袋和账本，苏长明仍在操作台前，证据道具归属连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第3组完整保留苏长明“你们以为赢了？那五亿债务雷已经爆了！”和“集团资金链断裂，大家一起死！”两句反击，没有替换或省略。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "苏长明质问句节奏偏快但未超过硬性上限。",
      "evidence": "“朱天和，你敢锁我的离岸账户！”约12个有效字 / 2秒 / 6.0字秒比。",
      "fix": "可保留；若后续统一慢化，可拆成反应镜头承载。"
    },
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "苏长明两句狂笑反击节奏较快但仍在可接受范围。",
      "evidence": "“你们以为赢了？那五亿债务雷已经爆了！”约18个有效字 / 3秒 / 6.0字秒比；“集团资金链断裂，大家一起死！”约14个有效字 / 2秒 / 7.0字秒比。",
      "fix": "可保留短剧快节奏；不作为硬性问题。"
    }
  ]
}
