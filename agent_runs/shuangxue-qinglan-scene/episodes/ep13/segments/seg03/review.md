{
  "pass": true,
  "summary": "seg03保留赵强上前打圆场、借用周转、欠条和还款记录逼问，以及周建国拍桌阻断。",
  "checked_groups": [
    "第5组",
    "第6组"
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
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "赵强上前说钱在店里、沈清追问用途和欠条、赵强说自家人不用欠条，关键台词和因果完整。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "8-13秒沈清与赵强两句合计约20字用5秒，约4字/秒，并含半步逼近和退缩反应，节奏可执行。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "evidence": "第6组将伸手索要记录、赵强结巴、周建国拍桌、周建国发火拆成4段，没有把拍桌和长台词塞进同一瞬间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵强在组首位于右后侧，0-3秒先前跨半步，再说台词，人物可用性清楚。",
      "fix_instruction": "若不通过，应在组首写出赵强位置或在说话前补入场动作。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "流水账单和空药盒从第5组尾到第6组首均在旧餐桌上，拍桌时被震动但没有消失。",
      "fix_instruction": "若不通过，应补充账单和空药盒在桌上的连续状态。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周建国、旧餐桌、流水账单、赵强和拍桌动作，数量3条且与剧情一致。",
      "fix_instruction": "若不通过，应替换泛泛禁止项为本组具体错误风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
