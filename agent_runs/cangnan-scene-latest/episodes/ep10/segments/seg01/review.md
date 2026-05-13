{
  "pass": true,
  "summary": "seg01三组均保留爆炸物发现、报警、排爆、留证和发现嫌疑人的剧情链，未发现阻断问题。",
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
      "type": "dialogue_pacing",
      "evidence": "陆凡报警台词约30字安排在5-10.5秒的5.5秒段内，紧急电话语速约5.45字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留村民后撤、陆凡用安全锥和警戒带围出危险区、排爆手把炸药转移进防爆罐三个关键动作。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "排爆队长对陆凡、陆凡对排爆队长、陆凡对身旁民警的说话对象均明确，黑影只作可见逃窜动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定施工现场桥洞、陆凡和村民位置，炸药包在桥洞阴影处可见，人物可用性充分。",
      "fix_instruction": "若不通过，应补清陆凡、村民、炸药包的画面位置与身体朝向。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载撤离、围警戒线、排爆车到场、转移炸药四个动作节拍，13秒内可表演。",
      "fix_instruction": "若不通过，应拆开排爆到场和转移炸药。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组防爆罐完成转移，第3组组首继续锁定防爆罐、警戒带和陆凡等待结果的状态。",
      "fix_instruction": "若不通过，应在第2组组尾或第3组组首补防爆罐和陆凡位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
