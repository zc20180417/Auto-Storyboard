{
  "pass": true,
  "summary": "seg04拆为列罪、宋天明登场录音反制、播放录音警笛逼近三组，保留原剧本的关键台词和证据动作。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留陆凡没有踩踏动作、列举雇凶伤人绑架非法拘禁、宋子昂喊父亲救命和黑衣人涌入。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组7-12秒承载陆凡约22字台词，字秒比约4.4；12-15秒约15字，字秒比约5.0，均未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组0-3秒手机扬声器播放宋子昂惨叫，陆凡嘴唇闭合不做口型，声音来源和画面口型分离清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "宋天明入场、威胁、陆凡后退掏手机和长台词拆成4段15秒，播放录音另放第3组，未把证据揭示压进同一组。",
      "fix_instruction": "若不通过，应拆开宋天明登场和陆凡录音台词。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾陆凡举手机，第3组首陆凡仍持手机并按播放键，宋天明和宋子昂位置连续。",
      "fix_instruction": "若不通过，应补足手机从举起到播放的过渡。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "三组均发生在天宫会所顶层包厢，组首均复述关键人物、门口和道具状态，未跨越主要物理空间。",
      "fix_instruction": "若不通过，应拆出门外空间或补清包厢入口位置。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "没有出现自动分镜、参考模板、字幕、首尾帧或模型说明词。",
      "fix_instruction": "若不通过，应删除工程说明并改写为可见可听画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
