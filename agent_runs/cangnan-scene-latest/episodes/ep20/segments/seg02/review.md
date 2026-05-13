{
  "pass": true,
  "summary": "seg02保留警察控制保镖、陆凡入场、疯狗被押、陆凡回应和宋子昂退后的对峙关系，未发现硬问题。",
  "checked_groups": ["第1组"],
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
      "evidence": "分镜按原剧本顺序呈现警察控制保镖、陆凡进包厢、宋子昂问疯狗、疯狗被押、陆凡说人在警车上、宋子昂以宋家地盘威胁。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "10-15秒连续对峙承载陆凡12字与宋子昂15字台词，共约27字5秒，字秒比约5.4，未超过6.5硬上限。"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "evidence": "宋子昂、陆凡、警察、疯狗和保镖在组首或动作前均有明确位置，疯狗在说到前由警察押出，人物可用性成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "包厢门口连通走廊作为同一连续入口空间处理，陆凡从门口进入包厢，未硬切到不相关空间。",
      "fix_instruction": "若不通过，应拆分走廊控制和包厢对峙。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂问陆凡、陆凡对宋子昂回应、宋子昂再对陆凡威胁，所有现场对白对象明确。",
      "fix_instruction": "若不通过，应补足说话对象。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾明确陆凡站在门内、疯狗被押在背景、宋子昂退到沙发前，可自然衔接后续包厢拔枪。",
      "fix_instruction": "若不通过，应在组尾补清人物和道具状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
