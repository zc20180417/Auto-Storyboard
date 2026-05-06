{
  "pass": true,
  "summary": "seg02分镜完整覆盖破门、火把威胁、上方起火、开枪制止、取得合同与公章等剧情，审核未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组7-9秒和9-11秒分别承载短句台词，均为2秒，符合短台词与动作同步完成的节奏。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留通风口黑烟倒灌、朱文浩扣动扳机击中两人膝盖、跨过倒地杀手并扯开01号铁柜的动作顺序。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组仍在红星厂地下二层，围绕01号铁柜、账本、合同、公章和防火袋展开，没有切入室外正门空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩在防盗门外，手下甲和手下乙在铁皮柜前且手持火把，三人都在行动前有明确位置和朝向。",
      "fix_instruction": "若不通过，应补足朱文浩破门前位置或两名手下与账本、火把的相对位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾两名手下仍在账本旁，第2组首延续防盗门已开、朱文浩举枪、手下持火把，随后黑烟倒灌和开枪动作连续。",
      "fix_instruction": "若不通过，应在相邻组尾或组首补门、火把和人物站位状态。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "盛大建工合同和苏长明私刻公章均通过可见文件、公章特写及原台词呈现，黑烟也以通风口烟雾和火光表现。",
      "fix_instruction": "若不通过，应把证据信息落实到可见文件、公章或朱文浩原台词。"
    }
  ],
  "issues": [],
  "warnings": []
}
