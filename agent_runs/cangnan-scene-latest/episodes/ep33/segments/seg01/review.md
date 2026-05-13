{
  "pass": true,
  "summary": "seg01已保留通车仪式等待、江若晴担心陆凡以及黑色越野车队驶入的剧情，格式和台词承载通过。",
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
      "evidence": "工头、林夏、江若晴三句台词均按原顺序保留，未新增剪彩动作或陆凡出场。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "江若晴17字用3.5秒，约4.9字/秒；林夏15字用3.5秒，约4.3字/秒并带安慰动作，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均在黑风山通车仪式现场，车队从远处公路入口进入，未跨越新的主要物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "工头对江若晴、林夏对江若晴、江若晴对林夏的说话对象均明确。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实说话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载江若晴担忧、林夏安慰和车队驶入三个节拍，12秒内动作清楚且无关键道具操作叠加。",
      "fix_instruction": "若不通过，应拆分车队驶入为独立组或压缩非关键反应。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部江若晴望向远处公路，第2组组首继续保持她看向公路入口，状态连续。",
      "fix_instruction": "若不通过，应在第1组组尾或第2组组首补充人物视线与站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
