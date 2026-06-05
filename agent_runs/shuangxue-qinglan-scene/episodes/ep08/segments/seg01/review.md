{
  "pass": true,
  "summary": "seg01保留打印流水、第一笔进账、分批转出、二十四个月和周桂兰痛哭等关键节点，格式和时间轴可交付。",
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
      "type": "script_fidelity",
      "evidence": "原剧本中的打印机吐出厚账单、沈清接过并翻到两年前第一笔记录，以及台词“妈，你看，25号下午两点进账八千。”均被保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“下午两点零一分起……”约31个有效字给5秒，约6.2字/秒；“二十四个月……”约35个有效字给5.5秒，约6.4字/秒，接近上限但未超过6.5硬线。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组组尾写沈清持有流水账单，第2组组首继续写沈清手中持有流水账单，翻页和指认均有可见归属。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定银行大厅柜台前单一物理空间，四名人物位置和朝向完整。",
      "fix_instruction": "若不通过，应补齐银行柜员、沈清、周桂兰、刘美娟的画面位置和身体朝向。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "打印、递账单、翻页、指认第一笔记录分为四个连续时间段，每段只有一个主动作或一句对白。",
      "fix_instruction": "若不通过，应拆开递账单和翻页动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周桂兰、沈清对刘美娟、周桂兰对沈清的现场对白对象均明确。",
      "fix_instruction": "若不通过，应把每句真人对白改为A对B说道。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载一次金额揭示、一次翻页证据展示、一次二十四个月质问和一次痛哭反应，属于同一证据链推进，15秒内可执行。",
      "fix_instruction": "若不通过，应把周桂兰痛哭反应拆成短承接组。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定流水账单、刘美娟、银行大厅、周桂兰，数量3条且没有使用占位模板。",
      "fix_instruction": "若不通过，应删除泛泛禁止项并替换为本组具体人物和账单风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
