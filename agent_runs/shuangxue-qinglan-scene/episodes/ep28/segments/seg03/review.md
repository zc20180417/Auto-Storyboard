{
  "pass": true,
  "summary": "seg03 保留周美娟求谅解、沈清周桂兰拒绝和沈清无声口型补句，音画承载清楚。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "evidence": "周美娟被押走、抓栏、两句求饶、沈清周桂兰反应按四段拆开，法警只负责控制动作。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "沈清最后一句写成没有发声、只动嘴唇，符合原剧本口型补句，不误写成现场对白。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清质问杂物间、周桂兰拒绝称妈、沈清承诺照顾小雨、口型补剩饭强均完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首已列周美娟、法警、沈清、周桂兰和栏杆位置，抓栏动作发生在同一法庭通道内。",
      "fix_instruction": "若不通过，应补齐栏杆两侧人物位置和法警控制关系。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "现场对白均写明沈清或周桂兰对周美娟说道，最后一句明确为无声唇形。",
      "fix_instruction": "若不通过，应把口型补句从对白改为无声唇形。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定沈清、周桂兰、周美娟、小雨和法庭，防止原谅、松手、错误出场等剧情错误。",
      "fix_instruction": "若不通过，应删除与正文冲突的禁止项并补具体角色锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
