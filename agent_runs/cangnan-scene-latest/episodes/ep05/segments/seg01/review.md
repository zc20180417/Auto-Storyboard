{
  "pass": true,
  "summary": "seg01已对照村口雨景剧本逐组审查，台词、动作、空间锁定和时长合同均可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留陆凡雨中进村、牛大春树下抽旱烟、陆凡自我介绍、牛大春质疑和陆凡卖鱼干承诺，未新增改变剧情的动作。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "6-9.5秒承载陆凡16字左右自我介绍和抹雨动作，9.5-14秒承载两句短对白约17字，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组仍在水头村村口，组首明确陆凡在画面左侧、牛大春在画面右侧大树下，人物可用性完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对牛大春说道、牛大春对陆凡说道均有明确现场对话对象。",
      "fix_instruction": "若后续改稿丢失对象，应恢复为A对B说道格式。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部牛大春仍蹲在树下审视陆凡，第2组组首复述同一位置，随后才站起指向村落。",
      "fix_instruction": "若改为开场已站立，应补充上一组站起过渡或调整组首状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只有一句质疑延续、站起指路和一句路况说明三个主要节拍，12秒可表演。",
      "fix_instruction": "若加入额外走位或村民反应，应拆组或删去非剧本动作。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位或模板化批量描述。",
      "fix_instruction": "若出现工程词，应改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
