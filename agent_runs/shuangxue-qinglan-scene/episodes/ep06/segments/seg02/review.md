{
  "pass": true,
  "summary": "seg02三组完整保留杂物间母女对话、周桂兰恐惧、沈清承诺追查与母亲点头，空间和手部道具连续。",
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
      "evidence": "原剧本中亲戚散去、周桂兰绞衣角求沈清算了、沈清指出杂物间和剩菜，均保留且没有新增剧情动作。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "衣角先在周桂兰手中，4-6秒由沈清用双手稳住，组尾转为沈清握住周桂兰双手，状态过渡清楚。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清约20字承诺给5秒，约4字/秒；随后3秒只承载周桂兰含泪点头，是短承接和情绪确认。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组始终在周家杂物间，组首列出旧床、周桂兰坐床边、沈清在床边，第一时间段没有重演入场。",
      "fix_instruction": "若不通过，应把任何进出门动作移出组首并放入时间段。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "0-4秒只承载周桂兰恐惧台词，4-6秒只承载握手动作，6-13秒承载沈清安抚台词，没有并列抢动作。",
      "fix_instruction": "若不通过，应拆分握手动作或减少同步反应。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组8秒为短承接，承载一句追查承诺和周桂兰点头，合并到第2组会让承诺与手部动作、恐惧台词同组过密。",
      "fix_instruction": "若不通过，应并入前组或改为6-9秒短节拍。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程词和模板词。"
    }
  ],
  "issues": [],
  "warnings": []
}
