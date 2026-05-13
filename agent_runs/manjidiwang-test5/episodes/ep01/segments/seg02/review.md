{
  "pass": true,
  "summary": "seg02共3组，忠于原剧本1-2场景全部内容，格式规范，空间锁定完整，无硬性问题。",
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "朱文浩'拿着薪水干构陷的脏活这身制服你们还想不想穿'19字/3秒=6.3字/秒，情绪对白偏快但在5.8-6.5 warning范围。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "破门闪光灯、搂着举杯、王队长错愕、朱文浩威严质问等全部保留。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "evidence": "安保人员在组首有'正准备退出'的位置，后续动作合理。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首交代朱文浩搂着苏清寒站在落地窗前举杯，大门紧闭，与上文剧情衔接。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首交代朱文浩面对王队长、王队长后退冒汗，与上组结尾王队长后退举手状态兼容。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "手机屏幕搜索结果和贪腐证据链均写为可见画面。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "朱文浩台词偏快",
      "evidence": "有效字数19字/镜头3秒/字秒比6.3字/秒，情绪对白偏快但在5.8-6.5可接受范围。",
      "fix": "可选拆分时间段。"
    }
  ]
}