{
  "pass": true,
  "summary": "走廊密谋组分镜忠于原剧本，对话指向清晰，时长计算正确，空间锁定完整，无明显硬错误。",
  "checked_groups": ["第1组"],
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
      "evidence": "廖副总警告台词14字/2秒=7.0字/秒，属于情绪对白警告区间；其余台词均符合普通对白5.2字/秒或情绪对白6.0字/秒基准。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出廖副总位于画面左侧侧对镜头脸朝画右、刘晓蕾位于画面右侧侧对镜头脸朝画左，两人位置与走廊空间一致，无跨场景问题。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本四句台词全部保留，动作'塞给''塞进包里''快步走向电梯'均得到体现，未删减关键情节。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "廖副总和刘晓蕾均在组首空间锁定中拥有明确画面位置、身体朝向和可见状态。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "本组为场景首组，无上一组衔接问题。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "走廊昏暗、监控红灯、塞纸袋、高跟鞋声等均转译为可见可听细节，无抽象概念直接输出。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "廖副总警告台词14字/2秒=7.0字/秒，处于情绪对白偏快区间（6-7字/秒）。",
      "evidence": "第1组6-8秒，廖副总警告道：'别漏风声，出事谁也保不住你。'共14字，镜头时长2秒。",
      "fix": "如模特语速允许可保持，或延长至3秒（但需调整组内其他镜头避免总时长超过15秒）。"
    }
  ]
}
