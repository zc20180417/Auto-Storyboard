{
  "pass": true,
  "summary": "seg03 将路边车祸和入水砸窗救人拆成两组，动作链清楚且未跨空间硬凑。",
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
      "evidence": "保留陆凡拖行李箱、轿车避让行人失控、冲入河中、村民喊救命和陆凡喊“不好”的事件顺序。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留陆凡入水、游向沉车、看见昏迷林夏、说“必须砸开车窗”、砸碎玻璃、解安全带并揽腰游向岸边。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "evidence": "入水、抓车、砸窗、解安全带、带人游走分成5个时间段，15秒内动作链可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组单一主要空间为清河乡泥泞公路，河水作为同一事故空间的路基下方环境出现。",
      "fix_instruction": "若不通过，应把路面事故和水中救援拆组。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林夏在组首已位于轿车车内驾驶位并昏迷，陆凡行动前也在水面可用。",
      "fix_instruction": "若不通过，应在组首明确林夏位于车内和陆凡朝向沉车。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "车窗从完整到碎裂通过8-11.5秒砸窗动作转变，安全带在11.5-15秒被陆凡解开。",
      "fix_instruction": "若不通过，应补砸窗或解安全带的可见过渡。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "未出现参考图、自动分镜、模板编号等工程污染词。",
      "fix_instruction": "若不通过，应删去工程词并保留可拍动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
