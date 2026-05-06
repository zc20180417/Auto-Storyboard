{
  "pass": true,
  "summary": "seg03 五组均忠于原剧本，客厅场景空间锁定完整，父子对话与高明动作全部保留，时长合规，无硬性错误。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-4秒朱天和8字醉意台词/2秒=4.0字/秒，符合短台词豁免（≤10字且≤2秒）；10-13秒高明11字恭敬台词/3秒≈3.7字/秒，系5.2字/秒向上取整自然结果。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确朱天和坐沙发中央、位于画面左侧、脸朝画右，朱文浩站沙发旁、位于画面右侧、脸朝画左，单组物理空间为客厅，无跨场景。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "关键台词'还有这个，城投三亿亏空''你查出了他的烂账底牌？''这是掀翻他总裁位置的杀招'均完整保留，城投亏空与杀招的因果链条未断裂。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和、高明、朱文浩三人均在组首空间锁定中获得明确位置与身体朝向；高明搀扶朱天和入门动作先于其台词，朱文浩在楼梯中段有明确画面位置。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱天和挥手让高明退下；第2组组首为高明退下关门，朱天和坐沙发、朱文浩站沙发旁，人物位置与房门状态连续。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'震惊''微缩''冷笑'等情绪标签均已转译为瞳孔放大、肩膀后缩、嘴角上扬等可见面部与肢体细节，'烂账底牌'通过纸张道具与台词共同承载。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "10-13秒高明11字台词/3秒≈3.7字/秒，系向上取整导致，节奏略偏慢。",
      "evidence": "11字按5.2字/秒计算为2.12秒，向上取整为3秒，字秒比3.7。",
      "fix": "当前不阻断产出，后续迭代可考虑合并上楼检查与返回台词为更长对话块以提升节奏密度。"
    }
  ]
}
