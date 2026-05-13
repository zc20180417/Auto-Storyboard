{
  "pass": true,
  "summary": "seg04审核通过，陆凡在土路被刘波追回、说明通知发错并上车返回的动作链完整。",
  "checked_groups": ["第7组", "第8组"],
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
      "type": "space_locking",
      "evidence": "组首写明陆凡在乡间土路中央偏左、黑色轿车在远处道路、刘波在车内暂不可见，随后车停和刘波下车可生成。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "刘波追上陆凡、陆凡疑惑、刘波解释通知发错、陆凡服从周书记指示并上车返回均保留。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "各对白段为3-4秒短句承载，7-11秒约18字/4秒为4.5字/秒，没有超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组为短承接动作组，10秒内只承载土路行走、轿车拦停、刘波下车三个动作节拍。",
      "fix_instruction": "若动作过载，应把下车和开口拆到下一组。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘波和陆凡每句现场对白都写明对对方说道或问道。",
      "fix_instruction": "若缺少对象，应补成刘波对陆凡、陆凡对刘波的明确格式。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾部刘波在车旁看向陆凡，第8组组首延续车门打开、二人面对面的位置。",
      "fix_instruction": "若状态断裂，应在组首复述车门、行李箱和人物位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
