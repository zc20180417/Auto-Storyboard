{
  "pass": true,
  "summary": "seg02已按祠堂龙舟场景审核，爸爸、村民甲、刻刀、旧陶笛和右腕纹理均忠于剧本，横屏调度连续。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "分镜保留焕然一新的祠堂、巨型木制龙舟、爸爸赤上身雕龙头、右腕伤疤消失并透出青色纹理。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "村民甲约24字赞叹放在6.5-10秒，约6.9字/秒略紧但有抬眼反应承接；未超过明显不可演硬阈值。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "刻刀从爸爸右手到木案，旧陶笛从脖子挂绳到手中擦拭，关键道具位置有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "龙舟横贯中后景，爸爸在左前景，村民甲在右侧门边，祠堂梁柱提供纵深。",
      "fix_instruction": "无需修复；左右关系和前后景已明确。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组爸爸继续雕刻收尾，第2组组首仍在龙头旁，刻刀仍在爸爸右手，空间和动作连续。",
      "fix_instruction": "无需修复；若改变位置需补走位。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "爸爸现场对村民甲说端午准备台词，后续擦陶笛无旁白或心声，口型来源清楚。",
      "fix_instruction": "无需修复；声音来源已明确。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "村民甲赞叹句在3.5秒内略偏快。",
      "evidence": "“燃哥，这龙头雕得真霸气，简直要活过来一样！”约24字/3.5秒，接近6.9字/秒。",
      "fix": "如需要更稳，可把该镜头延到4秒并压缩前面腕部特写，但当前不构成硬错误。"
    }
  ]
}
