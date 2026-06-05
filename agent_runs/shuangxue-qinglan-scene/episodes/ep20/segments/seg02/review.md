{
  "pass": true,
  "summary": "seg02完整承接油纸包到遗嘱揭示，产权信息、周建国反应和沈清驱逐台词均忠于原剧本。",
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
      "type": "prop_continuity",
      "evidence": "沈清从叠好的油纸包展开遗嘱，3-5.5秒把遗嘱拍在茶几上，组尾保持遗嘱摊在茶几中央。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组两句台词约10字/3秒和25字/4.5秒，均低于6.5字/秒且符合质问和冷读节奏。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留周建国凑近后脸色灰败、沈清十八岁产权台词、住是情分赶走是本分、周建国结巴反驳。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "展开油纸包、拍遗嘱、指字质问、冷读产权分别在独立时间段内完成，没有单镜多主动作过载。",
      "fix_instruction": "无。若遗嘱展开和长台词挤在同段，应拆开。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾遗嘱摊在茶几中央，第2组组首继续以遗嘱摊在茶几上、周建国弯身查看开始。",
      "fix_instruction": "无。若道具位置跳变，应补组尾或组首状态。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清两句均明确对周建国说道，周建国结巴也明确对沈清说。",
      "fix_instruction": "无。若缺对象，应补真实对话对象。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组禁止项围绕泛黄遗嘱、沈清、周建国、周桂兰居住权，3条均为本组证据揭示风险。",
      "fix_instruction": "无。若出现泛泛道具错误，应替换为具体遗嘱错误。"
    }
  ],
  "issues": [],
  "warnings": []
}

