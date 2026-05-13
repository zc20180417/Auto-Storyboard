{
  "pass": true,
  "summary": "seg03 preserves the撤队 order, certificate tug, archive-crime warning, Jiang Ruoqing recording beat, certificate return, threat, and escape without hard issues.",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "第1组保留王局长撤队、宋子昂骂王局长、抢证书想撕毁、陆凡握住另一端的动作顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡0-7秒约38字，字秒比约5.4；江若晴12-15秒约17字，字秒比约5.7，均未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "证书从陆凡和宋子昂各握一端，到宋子昂松手，再由陆凡转交老馆长，归属变化有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "撤队对白、辱骂、抢证书和陆凡握证书分为4段12秒，强动作与对白没有挤在同一短时间段内。",
      "fix_instruction": "若不通过，应拆出抢证书动作或延长拉扯组。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "江若晴在组首已位于人群边缘并持有手机，说话前有举手机动作，可用性明确。",
      "fix_instruction": "若不通过，应在组首锁定江若晴位置或安排入场动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾两人仍各握证书且江若晴录像，第3组首复述这一状态，再写宋子昂松手，连续性成立。",
      "fix_instruction": "若不通过，应在第3组组首复述证书和手机状态。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "宋子昂看群众和执法记录仪、不甘松手、陆凡交还证书、宋子昂威胁并钻进车逃走均完整保留。",
      "fix_instruction": "若不通过，应补齐松手、交证、威胁和逃走动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
