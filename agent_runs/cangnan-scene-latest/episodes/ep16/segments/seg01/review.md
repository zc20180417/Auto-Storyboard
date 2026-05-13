{
  "pass": true,
  "summary": "两组均保留备用金消失、公章缺失和报警的因果链，时长、对白对象、空间锁定和道具连续性可用。",
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
      "evidence": "财务总监冲入办公室、十个亿备用金消失、银行称本人签字盖章并转去海外的台词和因果均保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "财务总监最长句约27字用5秒承载，约5.4字/秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组尾部江若晴看向保险柜，第2组组首保险柜仍关闭，随后转密码、柜门弹开、公章缺失的道具状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "财务总监和江若晴的现场对白均写明对谁喊道、问道或说道，没有假对象。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "全组保持嘉禾项目部办公室一个物理空间，组首列明江若晴、财务总监、办公桌和保险柜位置。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载否认签字、开保险柜、发现公章丢失、报警四个连续动作信息点，13秒内分成四段，未把16秒以上节拍压缩进单组。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位符或批量模板化句式。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
