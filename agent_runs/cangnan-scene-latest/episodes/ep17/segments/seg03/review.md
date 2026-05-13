{
  "pass": true,
  "summary": "seg03分镜保留运钞车到场、发放双倍工资、工人道歉、陆凡承诺和宋子昂远处窥视，短反应组理由成立。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "两辆武装运钞车进工地、车门打开露出成捆现金、江若晴确认追回钱、陆凡下令发钱均保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "陆凡约24字大声承诺安排5秒，情绪对白字秒比约4.8字/秒，符合自然口型。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "evidence": "第4组为6秒、2个镜头，只承载远处山坡车内宋子昂咬牙切齿的短反应和片尾式威胁余波，没有硬凑到10秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "工人甲明确向陆凡和江若晴道歉，陆凡、江若晴均在组首可见且位置明确。",
      "fix_instruction": "若不通过，应补足对白对象并保证对象在画面内可用。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第4组另起黑风山远处山坡车内空间，组首明确轿车、车窗和宋子昂在驾驶位，避免与工地空地硬并组。",
      "fix_instruction": "若不通过，应拆分不同物理空间或标明片尾意象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只包含陆凡公开承诺、人群欢呼和陆凡收住神情三个节拍，11秒内可表演。",
      "fix_instruction": "若不通过，应拆出人群欢呼或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "timing_math",
      "problem": "6秒短组为片尾威胁反应，符合短动作余波例外，但交付时应意识到它不是默认10秒组。",
      "evidence": "该组只有宋子昂在山坡车内盯着工地、咬牙扣方向盘两个无台词反应镜头。",
      "fix": "如需减少短组，可在不跨空间混乱的前提下把远处窥视改为第3组结尾片尾意象。"
    }
  ]
}
