{
  "pass": true,
  "summary": "seg01保留龙家车队施压、江若晴反驳和正门打开的关键剧情，格式、时长、对白指向均通过。",
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
      "evidence": "原剧本的十几辆黑色越野车、二十余名黑西装男子、未持械、举产权异议书横幅和没有冲击大楼均在0-8秒保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "龙天傲喊话、江若晴反驳、龙天傲冷笑回应分别给4秒、4秒、5秒，均为快速对峙语速，预留了说话人反应和门打开动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首列出龙天傲、安保、律师、江若晴的位置、朝向和道具，整组保持项目部广场外同一物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "龙天傲、龙家私人安保、江若晴均在组首空间锁定中拥有明确位置和朝向，后续动作未使用未入场人物。",
      "fix_instruction": "若后续新增人物，需先在组首可见或安排入场动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙天傲对陆凡喊话、江若晴对龙天傲喊话、龙天傲对江若晴回应，均有真实对象。",
      "fix_instruction": "若出现无对象对白，应补成A对B说道或改成电话音/画外音。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部龙天傲在横幅前、江若晴隔门注视，第2组首延续龙天傲在门外、江若晴在门内、安保持横幅的状态。",
      "fix_instruction": "若状态跳变，应在上一组尾或下一组首补具体过渡。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "部分情绪台词接近快速争执语速。",
      "evidence": "江若晴喊话和龙天傲最后回应都属于对峙中的快速信息输出，但时间段仍给了4-5秒承载口型。",
      "fix": "如后续复审要求更稳，可将第2组拆成江若晴反驳和龙天傲回应两个时间段更长的组。"
    }
  ]
}
