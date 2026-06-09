{
  "pass": true,
  "summary": "两组分镜格式正确，台词指向清楚，字秒比全部合格，空间单一且组间状态连续，无硬问题。",
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
      "type": "dialogue_pacing",
      "evidence": "第1组 0-3秒：周建国台词12字÷3秒=4.0字/秒；3-6.5秒：沈清台词18字÷3.5秒=5.1字/秒；6.5-10秒：沈清台词17字÷3.5秒=4.9字/秒。全部低于6.5字/秒硬上限，情绪对白符合5.2字/秒目标区间。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均在周家正屋客厅单一物理空间内，无跨场景。组2组首空间锁定与组1组尾衔接一致：周建国瘫坐太师椅、沈清面向周建国、周桂兰在背景。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本四句台词全部保留，说话对象正确（周建国对沈清、沈清对周建国），关键动作'双腿发软跌坐在太师椅上''扶着周桂兰转身离开'均完整呈现，未新增改变剧情的动作或台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "四句台词字秒比分别为4.0、5.1、4.9字/秒，12秒组承载4个时间段+1个复合动作（跌坐），节奏合理无过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首空间锁定列出沈清、周建国、周桂兰三人位置和朝向，周桂兰虽无台词但在背景可见，为组2沈清扶她离开做铺垫。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组1组尾：周建国瘫坐太师椅、沈清举手机、周桂兰在背景。组2组首：周建国仍瘫坐、手机已收好、周桂兰在右侧偏后。手机从举起到收好为自然过渡，其余状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机在组1为沈清举证道具，组2组首已收好，属自然道具状态推进，无跳变。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每时间段仅一个主动作：举手机质问、否认结巴、举手机威胁、跌坐反应。无多个顺序主动作挤入同一时间段。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组视频禁止项'手机消失、周建国提前站起来、周桂兰提前离开客厅'均为本组特有剧情错误，锚定具体人物和道具。第2组为普通对话/离场组，省略视频禁止项符合规则。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
