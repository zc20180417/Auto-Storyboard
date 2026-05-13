{
  "pass": true,
  "summary": "seg04审核通过，环保审批阻击、假专家身份和江若晴反驳均按原剧本呈现。",
  "checked_groups": ["第10组", "第11组", "第12组"],
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
      "group": "第10组",
      "type": "character_availability",
      "evidence": "假专家在组首已位于宋子昂身后人群边缘，5-9秒被拉到桌旁，9-13秒再开口。"
    },
    {
      "group": "第11组",
      "type": "script_fidelity",
      "evidence": "保留蓝羽雀、栖息地和必须叫停三个关键信息，县领导震惊反应也保留。"
    },
    {
      "group": "第12组",
      "type": "dialogue_direction",
      "evidence": "江若晴对假专家反驳，宋子昂对江若晴施压，对话对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒承载宋子昂发难、拉出假专家和专家自称三个节拍，台词与动作时间充足。",
      "fix_instruction": "如不通过，应把专家自称拆到下一组。"
    },
    {
      "group": "第11组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "会议室、专家、县领导、江若晴和宋子昂的站位在组首清楚，单一空间成立。",
      "fix_instruction": "如不通过，应补足县领导席和专家朝向。"
    },
    {
      "group": "第12组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第11组尾县领导被影响，第12组首会议室骚动未平，假专家和宋子昂位置延续。",
      "fix_instruction": "如不通过，应在第12组首补充假专家仍站在桌旁。"
    }
  ],
  "issues": [],
  "warnings": []
}
