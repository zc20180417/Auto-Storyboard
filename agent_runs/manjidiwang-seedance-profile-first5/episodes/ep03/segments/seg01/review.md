{
  "pass": true,
  "summary": "seg01 已按原剧本完成朱家餐厅提亲前置对话，未发现硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "朱天和台词“我去集团，让你母亲陪你去”安排在2-4.5秒并同步大步出门；李娟台词“太阳打西边出来了？起这么早”安排在6.5-9.5秒，均未超过6.5字/秒硬上限，也没有用长静默凑时长。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组全程保持朱家别墅餐厅单一物理空间，组首列明朱文浩站在餐桌旁、李娟坐在餐桌边，水杯和餐巾位置明确。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留“恋爱三年，时机成熟”“有意思，老苏老脸往哪搁”“买套正装，我给你撑场子”三句原台词，并保留李娟大笑、转身的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩和朱天和在组首餐厅内有明确位置；李娟在4.5-6.5秒从楼梯走下后才开口，行动前来源清楚。",
      "fix_instruction": "无须修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾朱文浩站在餐桌旁、李娟停在入口，第2组组首承接为朱文浩站桌旁、李娟坐到餐桌边并端杯，对话空间连续。",
      "fix_instruction": "无须修复。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“被你拿下了”“撑场子”等信息均由原台词承载；画面只写李娟前倾审视、大笑、转身等可见动作，没有把抽象判断当作画面主体。",
      "fix_instruction": "无须修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
