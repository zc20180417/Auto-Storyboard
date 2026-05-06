{
  "pass": true,
  "summary": "seg04共3组已复审，手机通话来源、车内连续性、景别与时长均已清理为无硬问题。",
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
      "evidence": "第1组保留朱天和两句电话提醒、朱文浩'父亲，苏总裁的女儿在我床上。'、电话粗重呼吸和朱天和震怒台词。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组压缩为10秒，五个2秒电话节拍承载'危机暂缓''隐婚妻子''底牌''利刃''当面汇报反击'，没有用停顿凑时长。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组只在酒店地下车库和车库出口车流方向中表现朱文浩驾车离开，车辆移动为连续动作，不是硬切跨空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组到第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组朱文浩一手握方向盘、一手持手机贴耳，第2组组首延续同一姿态；朱天和声音来源统一为手机听筒。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩在驾驶座有明确位置，朱天和只以电话音出现且声音来源为手机听筒。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "挂断电话、手机放支架、启动车辆、驶出车库和汇入车流均为可见动作，危机缓解未以抽象画面表达。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "震怒台词语速偏快但可接受",
      "evidence": "第1组10-12秒'苏长明想用丑闻钉死我们！'13字/2秒=6.5字/秒。",
      "fix": "可选延至3秒。"
    }
  ]
}
