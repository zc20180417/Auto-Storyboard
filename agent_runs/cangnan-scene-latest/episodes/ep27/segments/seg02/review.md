{
  "pass": true,
  "summary": "seg02 保留省城商会大厅内股票、现金流、钢厂、贷款和破产连锁崩盘信息，分组节奏清楚。",
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
      "evidence": "保留赵家主喝茶、大门被推开、秘书报告股票毁灭性打击、赵家主摔杯和商会主权基金封死现金流。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-5.5秒承载秘书约20字急报，字秒比约5.7；8-14秒承载约23字现金流台词，字秒比约3.8，符合硬上限。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "李家主接电话时明确电话对象为电话那端；钱家主和赵家主为现场对白，声音来源没有混淆。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留李家主钢厂被查封、钱家主贷款被强制还款、赵家主总结十分钟三家破产的关键台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "功夫茶杯在组首位于赵家主手边，5.5-8秒明确被摔下并形成碎片，第2组组首延续碎裂茶杯。",
      "fix_instruction": "若不通过，应补茶杯从手边到桌边碎裂的动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明赵家主、李家主、钱家主和秘书在大厅的画面位置与朝向，全部说话人物可用。",
      "fix_instruction": "若不通过，应补充三大家主和秘书的静态位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "电话噩耗、贷款噩耗、赵家主反应和破产总结拆成4段共13秒，未超过片段复杂度。",
      "fix_instruction": "若不通过，应把李家主电话或钱家主贷款信息拆成独立组。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、模板编号、参考图、字幕或自动正反打等污染内容。",
      "fix_instruction": "若不通过，应删除污染词并改成具体画面动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
