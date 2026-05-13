{
  "pass": true,
  "summary": "seg03两组按原剧本呈现井中轰鸣、泉水喷出、水渠河道灌满、村民欢呼和枯树抽绿。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "“轰！”明确来自画面中央偏左的井口，属于环境巨响，未写成人物开口。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "村民甲台词约12字/3秒，村民乙台词约15字/4秒，均在激动反应镜头内，字秒比约4.0和3.75，节奏可表演。"
    },
    {
      "group": "第6组",
      "type": "horizontal_composition",
      "evidence": "水渠斜贯前景，村民甲在左侧渠边、村民乙在右侧老树旁、爸爸在中后景古井方向，三方层次清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金光后的井口先爆响，再喷出泉水，最后水流汇入水渠，道具和自然现象推进顺序清楚。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留村民甲“水渠满了！河道也满了！”和村民乙“枯树发芽了！老天爷，显神迹了啊！”两句原文。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内承载水渠蔓延、两句村民反应和枯树抽绿，动作与对白分镜分开，没有同镜头过载。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}

