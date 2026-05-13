{
  "pass": true,
  "summary": "祠堂内护龙舟段已完成审核，天天保护云宝、胡永贵破门夺舟和天天挡在龙舟前的转折完整。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "粗瓷碗始终由天天抱在怀里，碗中黑色木屑水和痛苦翻滚的云宝清楚承接原剧本道具状态。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "胡永贵从右后方大门进入，天天从左下方船底钻出并站到中央龙舟前，横屏走位路线清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "胡永贵“把这破龙舟给我拖出去劈了！”明确朝门外手下喊出，门外手下影子作为声音对象和行动来源可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "天天对云宝说话时画面中低头抱碗，口型由天天现场承载，云宝不被误写为开口对象。",
      "fix_instruction": "若不通过，应明确天天开口、云宝只在碗中翻滚。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留大门被暴力踹开、胡永贵扫视四周、命令拖龙舟、天天从船底钻出挡在龙舟前，未新增反击动作。",
      "fix_instruction": "若不通过，应删除剧本没有的打斗、逃跑或夺碗动作，只保留挡住龙舟。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内分为破门、进入扫视、下令、天天钻出、挡住五个连续节拍，动作链清楚且没有额外停顿凑时长。",
      "fix_instruction": "若不通过，应拆分破门进入和天天阻挡，或压缩非关键扫视。"
    }
  ],
  "issues": [],
  "warnings": []
}
