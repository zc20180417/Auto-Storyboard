{
  "pass": true,
  "summary": "第1-2组审核通过。书房审账场景OS与开口对白分离正确，台词节奏合理，敲门声有可见载体（门板震动），空间锁定完整。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "0-4秒OS 22字/4.5=4.9s，实际4秒合理（OS无口型约束）；4-7秒开口对白10字/4.5=2.2s+冷笑=3s合理；7-10秒对白14字/4.5=3.1s+敏锐=3s合理；10-13秒对白10字/4.5=2.2s+提笔=3s合理。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "evidence": "敲门声写明'楼下隐约传来克制的敲门声，书房门板轻微震动'，有可见载体。OS写明嘴唇闭合、不做口型。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "OS两行（现代商战账目/城投债务膨胀）、开口三行（盛大建工/去年改造资金/致命死穴）全部保留，台词原文未删减。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩是唯一角色，组首空间锁定明确其坐在红木办公桌后，位置和朝向完整。",
      "fix_instruction": "无需修复，人物可用性完整。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "G01组尾朱文浩伏案持笔，G02组首朱文浩仍坐在办公桌后持毛笔，9-11秒搁笔起身，状态连续。",
      "fix_instruction": "无需修复，组间连续性完整。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "OS全部写明嘴唇闭合、不做口型；开口对白明确指向'对面前的报表文件'；不可视信息（前世简单、资金链脆弱）通过OS处理，不占画面时间。",
      "fix_instruction": "无需修复，不可视信息已通过OS转译。"
    }
  ],
  "issues": [],
  "warnings": []
}
