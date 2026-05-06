{
  "pass": true,
  "summary": "监控密谋组分镜忠于原剧本，对话指向清晰，时长计算正确，空间锁定完整，无明显硬错误。",
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
      "evidence": "朱文浩冷厉台词12字/2秒=6.0字/秒、命令台词13字/2秒=6.5字/秒，均处于情绪对白6-7字/秒警告区间；其余台词节奏合格。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定列出朱文浩坐于主控台前面向镜头、王队长位于左侧侧对镜头脸朝画右，监控室单一物理空间，无跨场景硬切。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "六句台词全部保留，'双手交叉''迟疑''冷厉''命令''挺胸'等剧本标注的动作与情绪状态均在分镜中得到体现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩和王队长均在组首空间锁定中拥有明确画面位置、身体朝向和可见状态。",
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
      "evidence": "监控屏幕冷光、双手交叉、身体前倾、挺胸等均为可见可拍细节，无抽象气味或心理判断直接输出。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "朱文浩冷厉台词12字/2秒=6.0字/秒、命令台词13字/2秒=6.5字/秒，处于情绪对白偏快区间。",
      "evidence": "第1组7-9秒与9-11秒，朱文浩连续两句情绪对白分别12字/2秒和13字/2秒。",
      "fix": "如模特语速允许可保持；或合并为连续对话节拍并适当延长至4-5秒。"
    }
  ]
}
