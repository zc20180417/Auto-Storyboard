{
  "pass": true,
  "summary": "seg03已审核车内电话、屋檐偷听和奔向后山的空间连续性；电话声来源、口型归属和后山行动目标清楚，无hard issue。",
  "checked_groups": ["第7组", "第8组", "第9组"],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "包工头台词明确由手机扬声器传出，胡永贵嘴唇闭合听着，电话声与现场口型区分清楚。"
    },
    {
      "group": "第8组",
      "type": "horizontal_composition",
      "evidence": "胡永贵在右侧车内，天天在左侧屋檐阴影，半开车窗作为声音通道，左右关系稳定。"
    },
    {
      "group": "第9组",
      "type": "screen_direction",
      "evidence": "天天从左侧屋檐冲向右远方后山，皮卡留在左后方，行动方向与目标一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "胡永贵对电话里的包工头说话，包工头作为电话声出现，并有手机载体。",
      "fix_instruction": "若改稿，不能把包工头写成车内现场人物。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留胡永贵“把石壁炸开，再倒五桶废液进去扩宽”的原台词，以及天天听见后脸色惨白。",
      "fix_instruction": "若压缩，废液计划和天天偷听反应必须保留。"
    },
    {
      "group": "第9组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "固定中近景承载台词，横向跟拍和远景后拉服务天天从左到右奔向后山的路线。",
      "fix_instruction": "若调整奔跑镜头，需保持后山在右远方并保留皮卡在左后方。"
    }
  ],
  "issues": [],
  "warnings": []
}
