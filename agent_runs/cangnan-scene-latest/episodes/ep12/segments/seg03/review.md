{
  "pass": true,
  "summary": "seg03已审核通过，竞标会资金反转的台词、入场和银行凭证动作完整保留。",
  "checked_groups": ["第7组", "第8组", "第9组"],
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
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "宋子昂嘲讽、江若晴反击和宋氏夺项目的挑衅顺序未改。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "evidence": "陆凡在0-3秒先从会议室大门入场，随后才在3-6秒开口，人物可用性成立。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“林家注资十亿，三分钟前到账”分配5秒，字速约5.2字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "会议室、宋子昂、江若晴、资料和关闭的大门均在组首固定，单一空间明确。",
      "fix_instruction": "如不通过，应补足会议室门和陆凡不在首帧的信息。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "银行凭证从陆凡手中进入画面并被拍在桌面，归属转移有可见动作。",
      "fix_instruction": "如不通过，应补充凭证从手中到桌面的过渡。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒只呈现陆凡宣布到账和全场哗然两个强节拍，不拥挤。",
      "fix_instruction": "如不通过，应延长到账台词或拆出会场反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
