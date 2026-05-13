{
  "pass": true,
  "summary": "seg02单组分镜忠实于原剧本，画外音/心声口型隔离正确，对话指向明确，时长计算合理。",
  "checked_groups": ["第1组"],
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
      "evidence": "第1组第4镜朱文浩台词'资本游戏，该由我制定规则'共9字，按情绪对白5.2字/秒=1.7秒，与前句'皮相是最好的伪装'7字合并为一个连续台词段，两段合计16字，分配3.5秒（6-9.5秒），字秒比4.6字/秒，节奏合理。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "evidence": "李娟(OS)台词'这上位气场，比董事长还重'正确处理为心声，镜头描述写明画面人物嘴唇闭合、不做口型，音画分离正确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组保持单一物理空间（高定男装店），组首空间锁定写明朱文浩位于画面中央刚走出试衣间、李娟位于画面左侧坐在沙发上，空间关系清晰。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩在组首有明确位置（画面中央，面向试衣镜），李娟在组首有明确位置（画面左侧，坐在沙发上）。原剧本出场角色含'导购'，但导购在剧本中无台词无动作，分镜合理省略。",
      "fix_instruction": "无需修改，人物可用性已满足规则。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "本组为场景首组（从朱家别墅餐厅切换至高定男装店），不涉及与上一场景的组间连续性问题。组内4个时间段衔接自然，从走出试衣间到闭目深吸气收尾。",
      "fix_instruction": "无需修改，场景切换已通过组首空间锁定交代。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本'朱文浩左手大拇指习惯性摩挲虎口，气场极具压迫感'中，'气场极具压迫感'属不可视信息，分镜已转译为'指节微微收紧，眼神从镜中扫过自己，下颌微抬'等可见细节。",
      "fix_instruction": "无需修改，可视化转译已满足规则。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "script_fidelity",
      "problem": "原剧本出场角色包含'导购'，但分镜中导购未出现。原剧本中导购无台词无动作，省略合理，但建议确认是否需要在画面中保留导购作为背景人物。",
      "evidence": "原剧本：'出场角色：朱文浩，李娟，导购'。分镜组首空间锁定未列出导购。",
      "fix": "可选：在组首空间锁定或某个时间段中加入导购作为背景人物（如站在试衣间旁），但不影响剧情完整性。"
    }
  ]
}