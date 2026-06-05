{
  "pass": true,
  "summary": "seg03完成最后一页收款方揭示、强盛建材经营部曝光和回家对账收束，短组理由成立。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清翻到最后一页、盯住收款方、质问“那这个收款账户是谁的？”和把流水单举到刘美娟眼前均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“赵强的建材店，不是你家开的吗？”约16个有效字给4.5秒，约3.6字/秒，因冷笑后压迫逼问略慢但有逼近动作支撑。"
    },
    {
      "group": "第3组",
      "type": "timing_math",
      "evidence": "第7组总时长8秒，属于短动作余波和单句收束；0-2.5、2.5-5、5-8连续且镜头数3个匹配。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "流水单从沈清手中翻到最后一页并举到刘美娟眼前，收款方一栏的指认有清楚可见过渡。",
      "fix_instruction": "若不通过，应补充沈清翻页和指向收款方的动作。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "收款人“强盛建材经营部”、刘美娟否认、沈清点出赵强建材店三处关键台词均未改写。",
      "fix_instruction": "若不通过，应恢复原剧本收款人和赵强建材店台词。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈清、刘美娟、银行柜员都在组首锁定中可见，赵强只被台词提及，没有被写成现场出场。",
      "fix_instruction": "若不通过，应删除赵强现场出现或补成画外/台词提及。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组只承载刘美娟腿软、沈清收单和一句离场指令，8秒短组为动作余波和单句收束，不硬凑10秒。",
      "fix_instruction": "若不通过，应保持短组或与前组合并，不能增加无意义停顿。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定刘美娟、流水单、填单台、赵强和银行大厅，数量3条且与正文不冲突。",
      "fix_instruction": "若不通过，应删除无锚点或与剧情相反的禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
