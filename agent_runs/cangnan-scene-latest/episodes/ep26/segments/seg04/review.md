{
  "pass": true,
  "summary": "已审核26-4工地断供段，工头汇报、江若晴焦虑、陆凡拨电话走天上的转折均完整。",
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
      "evidence": "停工、工头“水泥、钢筋全断了”、江若晴两句绝望台词均保留，没有新增解决方案。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "江若晴“怎么送？省道都被三大豪门的工程车故意堵死了！”约24字/5秒，字秒比约4.8。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "手机在组首标为陆凡口袋处，8.5-13秒取出拨号有明确可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首固定工地、停转机器、江若晴、陆凡和工头位置，后续发言和反应均在同一物理空间内。",
      "fix_instruction": "如不通过，应补足所有在场人物位置和朝向。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡和江若晴的对白均明确互为对象，拨电话动作未把台词误写成电话音。",
      "fix_instruction": "如不通过，应区分现场对白和电话行为。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒只承载陆凡安抚、江若晴质问和陆凡拨号回应三个节拍，容量合理。",
      "fix_instruction": "如不通过，应拆出拨电话动作或延长质问时长。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "未出现模型说明词、参考图或模板化批量描述。",
      "fix_instruction": "如不通过，应改写成具体工地动作和人物反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
