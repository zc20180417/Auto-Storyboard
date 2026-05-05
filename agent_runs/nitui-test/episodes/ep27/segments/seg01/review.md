{
  "pass": true,
  "summary": "已按原剧本、分镜生成规则和当前seg01分镜逐组审核，未发现阻断产出的硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
  ],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked"
  },
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "台词节奏",
      "problem": "林跃揭示幕后买家一句节奏略快但未超过硬错误阈值。",
      "evidence": "台词“这些毒药材的幕后买家，是省城的龙腾集团。”有效字数约23字 / 4秒 / 约5.75字秒比，属于情绪信息揭示台词的可接受偏快范围。",
      "fix": "若后续要求更稳，可把第4组6-10秒与12-15秒重新分配为6-9秒和9-13秒，但当前不构成硬性问题。"
    }
  ]
}
