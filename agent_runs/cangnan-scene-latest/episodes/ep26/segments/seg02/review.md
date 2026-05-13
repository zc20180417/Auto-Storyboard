{
  "pass": true,
  "summary": "已对照26-2原剧本审核，金董威胁、陆凡回应和逃离办公室的因果链完整，未发现硬问题。",
  "checked_groups": [
    "第1组",
    "第2组"
  ],
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
      "evidence": "陆凡“龙天傲在哪？”、金董“龙少即将亲临省城，你完了！”和被摔到沙发后的“咳咳……你敢动手？”均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-4.5秒承载金董封杀嘉禾约19字，字秒比约4.2；4.5-8.5秒断供台词约19字，字秒比约4.8。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部金董在沙发上咳嗽，第2组组首仍位于沙发上，后续逃离办公室有可见动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "甩棍在组首标为陆凡脚边地面，后续不再作为关键可操作道具，未产生归属跳变。",
      "fix_instruction": "如不通过，应补充甩棍被放下或离手的位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "金董威胁和陆凡回击均明确写为对陆凡或对金董说，没有假对象和旁白误口型。",
      "fix_instruction": "如不通过，应明确每句现场对白的说话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内承载两句威胁、一句陆凡回应和逃离动作，时间分配充足，没有超出15秒硬压缩。",
      "fix_instruction": "如不通过，应把逃离动作独立为短承接组。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、模型自动处理等污染词。",
      "fix_instruction": "如不通过，应删除工程词并改为可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
