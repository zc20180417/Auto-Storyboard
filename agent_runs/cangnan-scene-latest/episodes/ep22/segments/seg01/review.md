{
  "pass": true,
  "summary": "seg01保留吴总监封存账目、逼审计员植入三千万烂账的关键台词和道具动作，格式与时长通过。",
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
      "evidence": "第1组保留砸账本、封存账目、审计员说明黑风山账目干净、吴总监要求塞东西的原剧本顺序。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "黑色U盘由吴总监持有并递给审计员，12-15秒审计员接过后插入电脑，道具转移有可见动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组多句短对白分布在2.5-12秒，最长台词约22字用3.5秒承载，未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确会议室、会议桌、账本、电脑及吴总监和审计员的位置与朝向，单一物理空间清楚。",
      "fix_instruction": "若不通过，应补充人物位置、朝向或电脑位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "吴总监和审计员所有现场对白均写明对对方说道、冷喝或发抖说道，没有假对象。",
      "fix_instruction": "若不通过，应为每句现场对白补真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "递U盘、威逼、审计员反应和插入电脑分为5段15秒，动作链与对白未挤压。",
      "fix_instruction": "若不通过，应拆分U盘递接与电脑操作。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、参考模板、占位符、字幕或工程词。",
      "fix_instruction": "若不通过，应删除污染词并改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
