{
  "pass": true,
  "summary": "seg01保留流水账单逼问、医药费借口和空药盒塑料袋打断，格式、台词指向和道具连续性通过。",
  "checked_groups": [
    "第1组",
    "第2组"
  ],
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
      "evidence": "沈清要求解释流水去向、周美娟用住宿和吃喝反驳、沈清追问剩饭和杂物间房租，台词顺序与seg01原文一致。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "5-9秒周美娟两句共约22字用4秒，约5.5字/秒；9-13秒沈清两句约17字用4秒，约4.25字/秒，未超过6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "塑料袋先在沈清手边被拿起，再甩到旧餐桌中央，组尾明确袋口散开和空药盒滑出，可接seg02的空盒散落。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定周家正屋客厅、旧餐桌、三人位置和朝向，第一镜从账单桌面开始，无过程动词矛盾。",
      "fix_instruction": "若不通过，应补齐三人画面位置、身体朝向和账单在桌面的位置。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "0-6秒承载周美娟两段医药费狡辩，6-11秒单一主动作是沈清甩出药盒袋，未把药盒散落和新质问塞入同一复杂段。",
      "fix_instruction": "若不通过，应把甩袋动作与后续药盒揭示拆开。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项3条均锚定空药盒、塑料袋、流水账单和旧餐桌，没有泛泛词，也不禁止原剧本动作。",
      "fix_instruction": "若不通过，应删除无锚点负面词并改为本组道具状态错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
