{
  "pass": true,
  "summary": "seg01 宣判赵强与周美娟两组忠于原剧本，时间轴、cut_id、对白指向和跪倒反应均可执行。",
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
      "evidence": "法官两段宣判分别给出4秒和3秒，判罪与刑期台词字秒比未超过6.5，并留出3秒给赵强瘫跪。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留周美娟盗窃罪、非法侵占他人财产罪、有期徒刑三年、责令退赔赃款四个关键宣判信息。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "两组均锁定同一明亮法庭空间，法官、被告席、旁听席位置明确，赵强跪倒状态从第1组尾接到第2组首。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "法槌、宣判、宣判结果、赵强跪倒按时间段拆开，每段只有一个主动作或对白节拍。",
      "fix_instruction": "若不通过，应把法槌和赵强跪倒拆成独立时间段。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾赵强跪在地面，第2组首继续低跪；周美娟仍在被告席内，空间状态连续。",
      "fix_instruction": "若不通过，应在第2组组首补赵强跪地和周美娟位置。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模型说明词、模板编号、参考图占位或批量模板化描述。",
      "fix_instruction": "若不通过，应删除工程词和模板语气。"
    }
  ],
  "issues": [],
  "warnings": []
}
