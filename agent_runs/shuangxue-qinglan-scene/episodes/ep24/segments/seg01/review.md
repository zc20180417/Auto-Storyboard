{
  "pass": true,
  "summary": "seg01 保留宴会庆贺、母女对白和门外冲突进入，格式与时长合同通过。",
  "checked_groups": ["第1组"],
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
      "evidence": "原剧本中周桂兰和沈清的两句对白、门外保安阻拦和周建国自称老公的骂声均被保留，未新增改变剧情的动作。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-6秒承载母女两句约23字对白，约5.75字/秒；8-11秒保安约15字，约5字/秒；11-15秒周建国约15字并伴随门板晃动，未超过6.5字/秒。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组固定在龙腾酒店宴会厅，门外声音通过宴会厅大门和门板晃动提供来源，没有跨到外部物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周建国为门外声音，画面通过半开大门和门板晃动承载声源；画面内周桂兰、沈清、保安均有真实对象。",
      "fix_instruction": "若不通过，应把门外音改成可见声源或让人物入场后再现场开口。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含宴会建立、母女对白、门口吵闹进入三个连续节拍，15秒内分成5个时间段，每段主动作清楚。",
      "fix_instruction": "若过载，应把门外冲突另拆一组。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周桂兰、保安、周建国、宴会厅大门等本组元素，未使用泛泛占位词。",
      "fix_instruction": "若禁止项泛化，应改成与本组人物和道具绑定的具体错误。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位符或批量模板化表达。",
      "fix_instruction": "若污染，应删除工程词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
