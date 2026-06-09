{
  "pass": true,
  "summary": "seg01（第1-3组）通过审核。高档公寓日景，沈清与周桂兰对话、订答谢宴、下令挖证据，台词忠实、口型节奏合格、空间连续。",
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
      "type": "dialogue_pacing",
      "evidence": "周桂兰'这……这得花不少钱吧？'14字÷3秒=4.0字/秒；沈清'妈，你这大半辈子受苦了。'17字÷4秒=4.25字/秒，节奏合格。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清'李助理，明天的答谢宴订在龙腾酒店，把请柬发出去。'21字÷4秒=5.25字/秒；助理'好的沈总'5字在同一时间段内完成，整体节奏合格。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "沈清'联系私家侦探，把周建国和赵强这几年的老底连同证据，统统给我挖出来！'忠实原剧本23-1最后一句，未删改。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人对白，无心声/画外音需要音画分离。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾沈清握着周桂兰的手；第2组组首沈清仍握手，状态连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组为8秒单镜头组，仅承载沈清一句命令，密度合理。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}