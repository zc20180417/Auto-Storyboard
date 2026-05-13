{
  "pass": true,
  "summary": "seg02 preserves the archive delivery, certificate reveal, both Lu Fan evidence lines, and Song Ziang's shocked retreat with valid scene-mode timing.",
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
      "type": "script_fidelity",
      "evidence": "第1组保留桑塔纳急刹、老馆长抱木盒快步来、老馆长报告绝密资料、陆凡接盒并让众人看。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组从陆凡手中木盒打开，到取出土地捐赠证书，再点向签名和手印，关键道具有可见过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组2-7.5秒约26字、7.5-13秒约25字，字秒比约4.6-4.8，符合证据揭示台词节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "老馆长在组首已位于桑塔纳车旁并持有木盒，随后下车和说话前可见可用。",
      "fix_instruction": "若不通过，应在组首或入场动作中明确老馆长位置。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "土地捐赠证书、五十年前捐给国家、无偿捐赠协议、太爷爷签名手印和宋子昂后退均保留。",
      "fix_instruction": "若不通过，应补回证书信息和宋子昂反应。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "证书取出、两段证据台词、宋子昂后退分为4段15秒，证据展示和情绪转折未被硬压缩。",
      "fix_instruction": "若不通过，应将证据揭示拆成两个组。"
    }
  ],
  "issues": [],
  "warnings": []
}
