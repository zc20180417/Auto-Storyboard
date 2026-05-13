{
  "pass": true,
  "summary": "seg01保留车队抵达、毒刺下令、麻醉门岗和破拆突入，格式与时长可交付。",
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
      "type": "dialogue_pacing",
      "evidence": "毒刺台词“任务目标：带走江若晴，其余阻碍全部清除。”约20字，7-12秒承载5秒，约4字/秒，冷酷命令语速合理。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留队员举起装有消音器的麻醉枪、两名保安被麻醉弹击中倒下、毒刺手势破拆门禁并突入大楼。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均锁定在嘉禾项目部大门外，人物位置、车辆、岗亭、门禁控制箱均在组首明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "毒刺明确对外籍安保精英说道任务命令，没有假对象或心声混用。",
      "fix_instruction": "若缺失对象，应改为“毒刺对外籍安保精英说道”。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "麻醉枪举起、两名保安倒下、战术手势、破拆突入分为4个连续动作段，12秒内动作链清楚。",
      "fix_instruction": "若节拍过载，应拆分麻醉压制与破拆突入。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾小队围在毒刺身后看向大门，第2组组首延续车队、毒刺、小队和门口保安的位置状态。",
      "fix_instruction": "若不连续，应在第2组组首复述车队、小队和保安的具体站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
