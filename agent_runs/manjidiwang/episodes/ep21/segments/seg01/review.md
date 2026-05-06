{
  "pass": true,
  "summary": "seg01分镜保留招标会开场、孙耀致辞、田立民点头和某老总奉承等原剧本信息，未发现硬性问题。",
  "checked_groups": ["第1组"],
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
      "evidence": "原剧本中的香槟塔、孙耀高定西装举杯、两句致辞、台下掌声、田立民点头、某老总奉承和孙耀宣布竞标均已按顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-4秒台词约13字/2秒，4-6秒台词约12字/2秒，10-12秒台词约12字/2秒，均未超过7字/秒且没有拖慢短句凑时长。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "整组只发生在洲际酒店宴会厅，组首列出孙耀、田立民、某老总、各界权贵的位置和朝向，香槟塔与宴会台布局明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "孙耀在组首位于台前中央，田立民位于台下前排，某老总和权贵位于台下席位，后续说话和反应均有可生成位置。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "意气风发、得意等状态被转译为举杯、嘴角上扬、抬高下巴、台下掌声和点头等可见可听信息。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "孙耀均明确对台下众人说话，某老总明确对孙耀说话，孙耀回应某老总时对象明确。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
