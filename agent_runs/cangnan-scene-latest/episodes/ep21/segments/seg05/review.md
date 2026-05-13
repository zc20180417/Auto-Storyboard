{
  "pass": true,
  "summary": "seg05已审核，周长海通过新闻得知宋家覆灭、点出金矿利益并命令审计组设局，剧情钩子完整。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "平板新闻标题保留‘苍南宋家覆灭，黑风山项目顺利通车’，周长海评价宋天明废物，管家点出黑风山地下金矿。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-5秒周长海命令24字约4.8字/秒；5-8秒管家回应14字约4.7字/秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "format",
      "evidence": "第2组总时长8秒、2个时间段连续，作为反派设局短钩子，标题、人物、场景、道具、组首、组尾和负面词均完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "黑风山金矿通过管家台词承载，新闻通过平板页面可见呈现，不依赖不可视内心判断。",
      "fix_instruction": "若不通过，应把不可视利益信息改为屏幕、台词或可见道具承载。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周长海对管家下令，管家对周长海回应，现场对白对象明确。",
      "fix_instruction": "若不通过，应补齐真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只包含下令和领命两个强节拍，8秒短组用于片尾反派钩子，未硬凑动作。",
      "fix_instruction": "若不通过，应与第1组合并或延长为10秒但不能添加无关动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
