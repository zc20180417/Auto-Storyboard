{
  "pass": true,
  "summary": "seg04 保留三人打算当众勒索、逼补欠税、躺酒店大厅污蔑继父虐待和贪婪笑容。",
  "checked_groups": ["第8组", "第9组"],
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
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "周美娟约20字用5秒，赵强约21字用5秒，情绪对白字秒比约4.0-4.2且有动作支撑。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "保留周建国躺酒店大厅污蔑虐待继父和周美娟让沈清身败名裂的原剧情。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位符或批量模板化描述。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾三人站位和手机归属，在第8组首完整复述并继续同一出租屋冲突。",
      "fix_instruction": "若不通过，应补周美娟手机和周建国站位。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载周建国两句阴谋、周美娟一句附和和三人笑容收束，15秒内节拍清楚。",
      "fix_instruction": "若不通过，应压缩收束或拆出短尾组。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周建国、周美娟手机、赵强和三人笑容，4条均为本组风险。",
      "fix_instruction": "若不通过，应替换无锚点或与剧情冲突的禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
