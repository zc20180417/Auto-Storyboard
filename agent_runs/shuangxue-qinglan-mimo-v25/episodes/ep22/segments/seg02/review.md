{
  "pass": true,
  "summary": "第2组赵强护车场景，台词节奏合格（字秒比均未超6.5），空间锁定包含沈清，视频禁止项锚定本组。",
  "checked_groups": ["第2组"],
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵强台词15字/2.5秒=6.0字/秒，工程队长台词15字/3秒=5.0字/秒，沈清台词18字/4秒=4.5字/秒，赵强气急败坏台词10字/2秒=5.0字/秒，均未超6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "沈清已在组首空间锁定中位于画面左侧，全景第一镜也包含沈清冷眼旁观，10秒后走来对话合理。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "evidence": "视频禁止项4条，均锚定本组人物（赵强、沈清、工程队长）和道具（车、杂物），无泛泛词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人开口对白，对话指向正确（赵强对工人、工程队长对工人、沈清对赵强、赵强对沈清）。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个强节拍（护车叫嚣、杂物围车、逼退对峙），每段一个主动作，15秒容量合理。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "5个时间段各承载一个主动作/对话节拍，非主动作人物（工程队长）只喊话不抢主角动作。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}

