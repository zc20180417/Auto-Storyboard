{
  "pass": true,
  "summary": "seg01已对照原剧本、竖屏生成规则和当前分镜逐项审核，炸弹解除段落无硬问题。",
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
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留江若晴让陆凡快跑、陆凡向排爆组报告承重柱位置和红蓝黄三线的关键信息，未新增拆弹结论。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "对讲机回复明确写为画外排爆手声音，陆凡嘴唇闭合，不会误成陆凡现场开口。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "排爆手台词约15字分配3秒，陆凡短句分配3.5秒，均未超过6.5字/秒上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确厂房、承重柱、炸弹、陆凡和江若晴的位置与朝向，单一物理空间成立。",
      "fix_instruction": "如不通过，应补足两人画面位置、身体朝向和炸弹固定位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内只承载对讲回复、排爆手入场和剪断引线三个强节拍，动作链完整。",
      "fix_instruction": "如不通过，应拆分排爆手入场和剪线动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾红灯熄灭，第3组首明确红灯已灭、排爆手仍在炸弹旁复查，状态连续。",
      "fix_instruction": "如不通过，应在第2组尾或第3组首补充红灯和排爆手位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
