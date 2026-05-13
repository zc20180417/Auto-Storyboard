{
  "pass": true,
  "summary": "seg04保留护卫队空降、缴械、队长报到、裁决官身份揭示和龙天傲被控制，审核通过。",
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
      "type": "generation_density",
      "evidence": "空降、缴械、队长敬礼、龙天傲反应分成4个时间段共14秒，动作链没有与长台词挤在同一镜头。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "龙天傲身份震惊约22字给4秒，陆凡宣判约25字给4秒，龙天傲崩溃约22字给4秒，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留龙天傲问最高裁决官、陆凡让其去商业调查局忏悔、龙天傲称京城龙家嫡系和有大人物、防务精锐按倒控制。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首把防务精锐定位在绳索末端和车辆周边可见位置，空降动作在0-4秒展开，人物可用性清楚。",
      "fix_instruction": "若防务精锐未在组首或入场动作前直接缴械，应补空间位置或入场动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾龙天傲双膝发软，第2组首延续其车辆前双膝发软，随后才下坠发问。",
      "fix_instruction": "若姿态从站立到倒地无过渡，应补下坠动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "防务队长、龙天傲、陆凡台词均有明确对象，不存在电话音或心声误作现场口型。",
      "fix_instruction": "若出现无对象喊话，应明确对陆凡或对龙天傲说道。"
    }
  ],
  "issues": [],
  "warnings": []
}
