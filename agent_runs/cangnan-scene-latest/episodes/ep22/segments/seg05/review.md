{
  "pass": true,
  "summary": "seg05保留吴总监召李队长反咬陆凡、陆凡出示至尊黑卡和平板证据链的关键剧情，审核通过。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "第1组保留陆凡逼近说砸试试、吴总监叫李队长、大批经侦警察进入和李队长实名举报台词。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "吴总监约24字急切甩锅用4秒承载，李队长短句用3秒，陆凡短句用3秒，均未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "陆凡从衣袋取出至尊黑卡，随后递平板；李队长接过平板查看证据链，关键道具交接清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "李队长在5-8秒随大批经侦警察入场，8-12秒才开口，人物可用性成立。",
      "fix_instruction": "若不通过，应先写李队长入场再安排发言。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾吴总监指向陆凡，第2组首继续保持吴总监指向陆凡、李队长居中、陆凡在桌前，状态连续。",
      "fix_instruction": "若不通过，应补足组首状态。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "加密证据链通过平板屏幕呈现，李队长脸色变化承载判断，抽象信息有可视载体。",
      "fix_instruction": "若不通过，应补平板屏幕内容或可见反应。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有官方模板、参考图、字幕、工程说明或模型自动生成表述。",
      "fix_instruction": "若不通过，应删除工程污染内容。"
    }
  ],
  "issues": [],
  "warnings": []
}
