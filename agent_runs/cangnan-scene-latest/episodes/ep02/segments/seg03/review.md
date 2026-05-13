{
  "pass": true,
  "summary": "seg03已审核，林夏查到陆凡身份、得知被发配、电话要求调回的剧情和电话音承载均符合规则。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "小熊查到救人者、林夏询问是谁、小熊递交陆凡资料的台词和动作均保留。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "苏有光只以手机听筒电话音出现，林夏听电话时写明嘴唇闭合不做口型，电话来源清楚。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "第7组8.5-11.5秒承载林夏18字电话质问约6字/秒，未超过6.5字/秒；11.5-15秒电话音和林夏命令合计约6字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "病房单一物理空间，林夏病床位置、小熊门内位置和资料页归属明确。",
      "fix_instruction": "若不通过，应补足人物位置和资料页归属。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组按赞许、得知发配、发怒、拨号、电话命令分为5段，台词短且动作轻，15秒内可表演。",
      "fix_instruction": "若不通过，应将拨号和电话下令拆成独立短组。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、模型说明词或广告式文本，尾部约束为标准短剧风格。",
      "fix_instruction": "若不通过，应删除工程词和模板化描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
