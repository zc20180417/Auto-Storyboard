{
  "pass": true,
  "summary": "seg01已逐项对照原剧本审核，山道事故和别墅门口拒收剧情完整保留，未发现硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "原剧本中的刹车失灵、连续踩刹车无效、车速表到一百二、悬崖急转弯、主管手机来电、林刚心声均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "林刚台词“给老子停！”有效4字/2秒，为短台词豁免；“算你命大。”有效5字/2秒，同步踹门和看悬空前轮，节奏可接受。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "本组只在豪华别墅门口雨夜展开，林刚、保安、管家均在组首获得明确位置和身体朝向，管家位于大门内侧背景角落并在8-10秒走出。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "林刚对管家的情绪对白有效22字/4秒，字秒比5.5；管家末句有效18字/3秒，字秒比6.0，符合短剧争执节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚在组首位于驾驶位，主管通过副驾驶手机声音出现，声音来源明确。",
      "fix_instruction": "无。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾林刚盯住急弯，第2组组首延续货车冲到悬崖急转弯前，人物和车辆状态连续。",
      "fix_instruction": "无。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“豪华别墅门口”“额头流血”“扯开后车厢门”“黑伞”“看手表”均为可见动作或道具，没有用抽象判断替代画面。",
      "fix_instruction": "无。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "管家拒收、林刚说明刹车管被剪并拿命送货、管家以首富货物压人，台词和人物关系未改写。",
      "fix_instruction": "无。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "dialogue_pacing",
      "problem": "管家首句略快但不阻断。",
      "evidence": "“你晚了五分钟。这货我不收。”有效13字/2秒，字秒比6.5，属于6-7字/秒偏快区间。",
      "fix": "如需更稳可给3秒，但当前短剧争执节奏可接受。"
    }
  ]
}
