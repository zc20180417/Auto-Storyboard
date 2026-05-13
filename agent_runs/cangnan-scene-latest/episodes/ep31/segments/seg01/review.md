{
  "pass": true,
  "summary": "第1组保留雨夜庄园门口、保镖喝止、强光手电、陆凡台词和踹门警报等关键内容，格式与时长通过。",
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
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本两辆防弹迈巴赫、十名黑衣保镖、陆凡拖着龙天傲、保镖喊“站住！放开少爷！”、陆凡说“让龙万山滚出来”和踹开铁栅栏门均已保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "保镖甲7字台词分配3秒，陆凡8字台词分配2秒，字秒比均低于6.5且不拖慢。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首明确庄园大门外单一物理空间，陆凡、龙天傲、保镖甲和黑衣保镖的位置、朝向、手电道具均可用。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "保镖甲对陆凡大喝，陆凡对保镖甲冷声说道，真人对白对象明确。",
      "fix_instruction": "若不通过，应补足说话对象并避免假对象。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为门口压迫与踹门动作，5个时间段总计13秒，强光、短对白和踹门警报有足够表演时间。",
      "fix_instruction": "若不通过，应拆分踹门或压缩非关键环境铺垫。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模型说明词、参考图占位符、模板编号或批量化禁用表达。",
      "fix_instruction": "若不通过，应删除工程词并改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
