{
  "pass": true,
  "summary": "第7-8组审核通过，母女碰杯和宾客祝酒场景温馨收尾，节奏合理。",
  "checked_groups": ["第7组", "第8组"],
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
      "type": "dialogue_pacing",
      "evidence": "沈清台词21字/4秒=5.25字/秒，周桂兰台词16字/3.1秒=5.2字/秒，均未超过硬上限。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "宾客甲乙台词完整保留，沈清和周桂兰碰杯情节完整。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "组首列出沈清和周桂兰位置和朝向，为同一物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒内3个节拍各占独立时间段，母女对话7.5秒承载两段台词合理。",
      "fix_instruction": "若不通过，应拆分时间段。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈清对周桂兰温声说道、周桂兰对沈清欣慰说道，说话对象均明确。",
      "fix_instruction": "若不通过，应检查说话对象。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组组尾沈清和周桂兰并肩坐在桌旁，第8组组首状态一致。",
      "fix_instruction": "若不通过，应在组尾补具体状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
