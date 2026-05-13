{
  "pass": true,
  "summary": "seg03 两组保留人质、炸弹、徐虎掌掴和陆凡入场，审核未发现硬问题。",
  "checked_groups": ["第1组", "第2组"],
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "江若晴被绑在承重铁柱、腰间土制炸弹红灯闪烁，以及赵大江、徐虎、江若晴、徐虎四句台词均保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组各短句分别分配2.5到3秒，最高约5字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "陆凡在组首被锁定在大门外侧阴影中，随后通过推开生锈大门入场后再说台词，人物可用性成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定厂房车间内、承重铁柱、江若晴、徐虎和赵大江位置，单一车间空间清楚。",
      "fix_instruction": "若不通过，应补齐三人位置、朝向和炸弹状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组13秒承载掌掴、江若晴警告、门被推开和陆凡寒声入场，动作按顺序给足时间。",
      "fix_instruction": "若不通过，应将掌掴或陆凡入场拆成独立组。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾徐虎逼近江若晴，第2组首保持徐虎在江若晴近处，炸弹红灯持续闪烁。",
      "fix_instruction": "若不通过，应补第2组组首的徐虎、江若晴和炸弹状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
