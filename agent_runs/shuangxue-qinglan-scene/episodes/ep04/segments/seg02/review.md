{
  "pass": true,
  "summary": "seg02三组保留小雨抱洋娃娃入场、Party尾款说漏嘴、刘美娟捂嘴和沈清八千元质问，短组理由成立。",
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
      "type": "character_availability",
      "evidence": "小雨未写入组首，但在0-3秒先从卧室门口跑进客厅，之后才举洋娃娃说话，人物可用性顺序正确。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清询问Party花钱、小雨说钱一到账结宴席尾款、刘美娟脸色煞白并捂住小雨嘴、斥责回屋均与原剧本一致。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清最终质问约21字给6秒，约3.5字/秒，因咬牙切齿的情绪压低语速且只有单句反击；整组8秒属于短促反击和情绪余波。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只锁定周家正屋客厅，卧室门作为背景入口存在，没有跨越第二个主要物理空间。",
      "fix_instruction": "若不通过，应把卧室只写作入口或另起组处理。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "进口洋娃娃从小雨入场开始一直由小雨抱着，第1组尾部明确小雨抱娃站在客厅右侧。",
      "fix_instruction": "若不通过，应补充洋娃娃归属和位置。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "沈清询问、小雨说漏嘴、刘美娟扑过去捂嘴、刘美娟斥责、沈清观察分段承载，没有把捂嘴和长对白塞进同一时间段。",
      "fix_instruction": "若不通过，应拆分捂嘴动作和斥责台词。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定刘美娟、小雨、进口洋娃娃、古法金镯和沈清，没有泛泛的画面混乱类词。",
      "fix_instruction": "若不通过，应替换为本组具体错误风险。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只有刘美娟和小雨僵住的2秒余波加沈清6秒单句反击，8秒短组符合单句反应和短动作余波例外。",
      "fix_instruction": "若不通过，应并入上一组或缩短普通反应，但当前上一组已15秒且不能再合并。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有官方模板编号、@占位符、广告语、参考图或模型说明词。",
      "fix_instruction": "若不通过，应删除污染文本并保留自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "沈清最终质问语速偏慢但仍可由咬牙切齿的强情绪支撑。",
      "evidence": "约21字给6秒，约3.5字/秒，且本组是八千元被算准后的短促压迫反击。",
      "fix": "若后续生产觉得拖沓，可把0-2秒余波压到1秒并保持总时长7秒。"
    }
  ]
}
