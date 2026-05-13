{
  "pass": true,
  "summary": "seg02已审核，账本涂改、老人围拢、老李供出张强和陆凡带账离开均按剧本保留，无硬问题。",
  "checked_groups": ["第3组", "第4组", "第5组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "陆凡发现涂改七次、老李解释算错改过来的台词均保留，账本金额栏被明确展示。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组11-15秒承载老李16字台词，约4字/秒，未超过硬上限；老人甲台词10字占4秒段内也充足。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "第4组陆凡握紧账本，第5组0-4秒合上账本，7.5-11秒装进公文包，道具归属和动作连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "老人甲和老人们在组首已位于背景廊檐和院门旁，之后围拢和喊话有入场基础。",
      "fix_instruction": "若不通过，应在喊话前补入老人们位置或入场动作。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "金额揭示、老人围拢、老人甲讨钱、老李供出张强分为四段，15秒内节拍清楚。",
      "fix_instruction": "若不通过，应拆分老人围拢和老李供认。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部老李发抖供认、陆凡握账本，第5组首继续保持石桌旁对峙和账本在陆凡手中。",
      "fix_instruction": "若不通过，应在组尾或组首补足人物和账本道具状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
