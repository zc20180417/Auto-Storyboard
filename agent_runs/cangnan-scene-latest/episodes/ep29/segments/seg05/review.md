{
  "pass": true,
  "summary": "seg05保留龙天傲等待爆破、起爆失败、陆凡屏幕嘲讽和调集私人安保武装的完整升级。",
  "checked_groups": ["第9组", "第10组", "第11组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "龙天傲说“时间到了，矿区应该塌了。”，副官惊恐报告“起爆信号丢失，炸药没有引爆！”，因果保留。"
    },
    {
      "group": "第10组",
      "type": "audio_mouth_sync",
      "evidence": "陆凡作为屏幕画面出现，声音从车内扬声器传出，龙天傲前景嘴唇闭合不做陆凡口型。"
    },
    {
      "group": "第11组",
      "type": "dialogue_pacing",
      "evidence": "龙天傲下令“调集所有私人安保武装！包围项目部！给我施压！”约25字分配6秒，情绪喊话不超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定指挥车、雷达屏幕、控制台、龙天傲和副官位置，整组不跨空间。",
      "fix_instruction": "若不通过，应补充车内控制台和两人画面位置。"
    },
    {
      "group": "第10组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡通过大屏幕画面可见并通过扬声器出声，龙天傲和副官均在组首可见。",
      "fix_instruction": "若不通过，应明确陆凡是屏幕画面和车内扬声器声音来源。"
    },
    {
      "group": "第11组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第10组尾龙天傲手伸向对讲机，第11组首手边就是对讲机，并完成摔对讲机和按键喊话。",
      "fix_instruction": "若不通过，应在第10组尾或第11组首明确对讲机位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
