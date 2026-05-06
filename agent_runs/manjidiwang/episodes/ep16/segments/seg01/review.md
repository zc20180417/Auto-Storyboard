{
  "pass": true,
  "summary": "seg01两组已对照审讯室剧本完成审核，台词、录音、红星厂秘密和空间连续性均保留，无硬性问题。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留朱文浩扔照片、雷军涉黑袭警、雷震替人办事、拉椅坐下、安保部分管等原剧本信息，未新增会改变剧情的强动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组7-15秒为连续对话节拍，承载朱文浩交易条件与雷震两句供述，约45个有效字，8秒内完成，字秒比约5.6，低于硬错误阈值。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组全程锁定特勤局审讯室，录音来自桌上播放器，苏长明只以录音画外音出现，没有跨现实空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩位于画面左侧、雷震位于画面右侧，组首写明身体朝向和桌面照片，二人开口前均可生成。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾朱文浩坐在桌前冷看雷震，第2组首延续朱文浩坐桌前、雷震坐审讯椅、照片摊在桌上的状态。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "卸磨杀驴和崩溃情绪通过眼眶充血、肩膀塌下、攥桌沿等可见动作表现，红星厂秘密由台词直接交代。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "连续供述节拍略快但可接受。",
      "evidence": "第2组7-15秒有效字数约45，镜头8秒，字秒比约5.6，接近短剧快节奏上限但仍清晰。",
      "fix": "如后续强审要求更稳，可拆成朱文浩条件与雷震两句供述两个时间段，但当前不构成硬错误。"
    }
  ]
}
