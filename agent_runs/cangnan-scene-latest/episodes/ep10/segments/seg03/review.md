{
  "pass": true,
  "summary": "seg03三组保留赵大江装钱、陆凡破门、对峙和录音压证，审核通过。",
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
      "evidence": "保险柜大开、赵大江往旅行箱塞现金、红木大门被推开、陆凡满身泥水站在门口均被保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡、赵大江、陆凡三句短对峙各用2.5秒，台词量均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "黄毛供认以手机扬声器录音声出现，并明确画面中赵大江嘴唇闭合不做口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "办公室、保险柜、旅行箱、现金、赵大江和关闭大门在组首均有明确位置；陆凡在门外不可见，随后有入场动作。",
      "fix_instruction": "若不通过，应补陆凡入场前的门外来源或赵大江位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾陆凡在门口、赵大江在保险柜旁，第2组组首复述门开、二人对峙和现金位置。",
      "fix_instruction": "若不通过，应在第2组组首复述门和旅行箱现金状态。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "陆凡手中手机先被扔到办公桌，再播放录音压制赵大江狡辩，道具转移可见。",
      "fix_instruction": "若不通过，应补手机从陆凡手中到桌面的动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
