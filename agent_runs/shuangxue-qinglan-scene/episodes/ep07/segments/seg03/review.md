{
  "pass": true,
  "summary": "seg03 完整保留打印流水、刘美娟阻拦、抢排队号、沈清护住周桂兰和终句反击，关键道具与保护站位清楚。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清递身份证并要求打印两年流水，刘美娟以侵犯隐私阻拦，两句关键台词与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "evidence": "刘美娟扑向柜台抢排队号、沈清厉喝、推开刘美娟、站到周桂兰身前被分成4段，抢号与保护站位可执行。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟台词约18字在0-5秒，约3.6字/秒；沈清台词约13字在5-9秒，约3.25字/秒，均低于6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "身份证从沈清手中递进窗口，排队号和银行卡仍位于柜台台面靠沈清一侧，为下一组抢号动作保留可见目标。",
      "fix_instruction": "若不通过，应补身份证、排队号或银行卡所在位置。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有递身份证、要求打印流水、刘美娟阻拦三个同一流程强节拍，12秒内未过载。",
      "fix_instruction": "若不通过，应把刘美娟阻拦单独拆组或压缩非关键动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确沈清贴近窗口、刘美娟在右侧朝向柜台、排队号在台面上，第一段从刘美娟扑向排队号开始，无起点矛盾。",
      "fix_instruction": "若不通过，应修正组首第一帧和第一时间段动作起点。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定排队号、沈清保护站位、周桂兰位置和身份证窗口状态，数量4条且与剧情一致。",
      "fix_instruction": "若不通过，应删除矛盾禁止项或补足本组保护站位风险。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾沈清挡在周桂兰前、刘美娟退回右侧，第3组组首继承该站位和排队号、银行卡、身份证位置。",
      "fix_instruction": "若不通过，应在第2组尾或第3组首补充站位和道具状态。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟对沈清控诉，沈清对刘美娟反击，双方对白对象明确，未新增人物关系或台词。",
      "fix_instruction": "若不通过，应补明对白对象并恢复原台词。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文为自然分镜文本，没有模型词、模板编号、参考图或占位符污染。",
      "fix_instruction": "若不通过，应删除所有工程说明和模板化表达。"
    }
  ],
  "issues": [],
  "warnings": []
}
