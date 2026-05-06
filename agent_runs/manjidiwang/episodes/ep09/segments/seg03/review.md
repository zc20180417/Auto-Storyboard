{
  "pass": true,
  "summary": "公寓突袭三组均忠于原剧本，对话指向清晰，时长计算正确，空间锁定完整，无明显硬错误。",
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
      "type": "dialogue_pacing",
      "evidence": "王队长画外音7字/2秒=3.5字/秒、刘晓蕾尖叫9字/2秒=4.5字/秒，均因≤10字且≤2秒获得短台词豁免；王队长厉声台词12字/2秒=6.0字/秒处于情绪对白警告区间。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定列出刘晓蕾坐于桌前、王队长持手电筒位于左侧、两名安保人员分列左右，公寓客厅单一物理空间，夺袋与倒出动作在空间内完成，无跨场景硬切。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "'完了……'保留，执法记录仪红灯闪烁与绝密试卷特写均得到呈现，未删减关键情节。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "刘晓蕾在组首空间锁定中已就位；王队长与安保人员通过5-7秒明确冲入动作获得可生成位置，发生在其台词与行动之前。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组首空间锁定中刘晓蕾仍坐在桌前、王队长手持手电筒位于左侧，与第1组组尾王队长厉声说完台词、手电筒光柱锁定刘晓蕾的状态兼容。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "执法记录仪红灯、绝密印章、试卷散落、跌坐等均为可见可拍细节，'铁证彻底定格'转译为记录仪闪烁与试卷特写，无抽象概念直接输出。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "王队长厉声台词'有人举报小偷窜入此栋楼'12字/2秒=6.0字/秒，处于情绪对白偏快区间。",
      "evidence": "第1组9-11秒，王队长对刘晓蕾厉声说道，12字分配2秒。",
      "fix": "如模特语速允许可保持，或延长至3秒并相应压缩其他镜头。"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "王队长冷笑台词'刘小姐，这小偷的胃口真大啊'14字/2秒=7.0字/秒，处于情绪对白偏快区间。",
      "evidence": "第2组10-12秒，王队长对刘晓蕾说道，14字分配2秒。",
      "fix": "如模特语速允许可保持；因延长至3秒会导致情绪对白低于5.2字/秒形成硬错误，当前2秒为最优解。"
    }
  ]
}
