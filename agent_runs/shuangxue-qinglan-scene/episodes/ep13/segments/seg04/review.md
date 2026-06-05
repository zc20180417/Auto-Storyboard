{
  "pass": true,
  "summary": "seg04保留盗窃定性、周建国威胁、周美娟转为索要证据和短信号码质疑，审核通过。",
  "checked_groups": [
    "第7组",
    "第8组"
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
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "沈清说盗窃养老钱、周建国威胁、沈清回击、周美娟突然笑并说别太得意，顺序和对象均与原文一致。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "5.5-8.5秒约13字用3秒，约4.3字/秒；10.5-13秒约16字用2.5秒，约6.4字/秒，低于6.5硬上限。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "沈清只触碰自己的手机边缘，周美娟手机没有被提前拿出，符合原文中她要求证明短信在自己手机上的信息状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组组首继承第6组周建国在旧餐桌右侧、沈清在桌左侧对峙的状态，周美娟从后方露出身位有可见过渡。",
      "fix_instruction": "若不通过，应在第7组首明确周建国和沈清仍在桌两侧。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第8组仍为周家正屋客厅单一物理空间，五名人物位置和朝向均在组首可用。",
      "fix_instruction": "若不通过，应补齐周建国、赵强、周桂兰的背景位置。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项3条锚定周美娟手机、流水账单、周建国和短信台词，避免关键证据状态被提前改写。",
      "fix_instruction": "若不通过，应删除无锚点条目或改成本组手机与短信相关风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
