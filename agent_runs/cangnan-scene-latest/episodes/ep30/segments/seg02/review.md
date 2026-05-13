{
  "pass": true,
  "summary": "seg02保留陆凡独自出门、三分钟警告、申请已批和两分钟倒计时，机械格式与审稿证据通过。",
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
      "evidence": "陆凡双手插兜、孤身走出大门，龙天傲说“你终于肯出来了”，陆凡三分钟警告均按原顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "陆凡长句约44字给7秒，约6.3字/秒，属于情绪克制但信息密集的警告，未超过6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "陆凡在3-6秒明确从衣兜掏出手机并展示已通过申请，后续看表另有8-11秒动作，手机和腕表归属清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组首承接上一段正门已打开，陆凡在门内阴影处可用，随后才走到门口台阶前发言。",
      "fix_instruction": "若陆凡直接在门外发言却无入场，会要求补出门动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙天傲、陆凡所有现场台词都明确写为对对方说道，未出现假对象。",
      "fix_instruction": "若缺少对象，应补为龙天傲对陆凡或陆凡对龙天傲说道。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为短句交锋，包含质疑、手机证明、龙天傲震住、看表倒计时四个轻节拍，11秒内可表演。",
      "fix_instruction": "若再加入车辆到场或新人物入场，应拆出新组。"
    }
  ],
  "issues": [],
  "warnings": []
}
