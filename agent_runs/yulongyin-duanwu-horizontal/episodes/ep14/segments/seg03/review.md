{
  "pass": true,
  "summary": "seg03审核通过，两名村民夜间靠近祠堂、犹豫与纵火动机、爸爸持斧出场均忠于原剧本并具备横屏压迫关系。",
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
      "type": "script_fidelity",
      "evidence": "第1组保留村民甲、村民乙手持火把悄悄靠近祠堂，以及村民乙犹豫、村民甲红眼回应的台词。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "村民乙约22字台词安排在5-9秒4秒内，村民甲约21字台词安排在9-12.5秒3.5秒内，均未越过硬上限。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "第2组把村民甲、村民乙固定在左侧台阶下，爸爸从右侧祠堂大门内出现并站上石阶，左右高低压迫关系明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "两名村民从画面左侧向右侧祠堂门靠近，视线和火把方向始终朝右，没有无过渡换边。",
      "fix_instruction": "无需修复；后续对峙继续保持村民在左、祠堂门和爸爸在右。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "火把在第1组未点燃，第2组打火机靠近未点燃火把后被大门声打断，未把火把写成已经烧到龙舟。",
      "fix_instruction": "无需修复；不要新增点燃成功或烧船动作。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "爸爸在第2组通过祠堂大门猛开入场，出现在右侧石阶上，持斧状态可见且与下一段对峙衔接。",
      "fix_instruction": "无需修复；若调整，必须保留爸爸从门内出现的可见入场。"
    }
  ],
  "issues": [],
  "warnings": []
}
