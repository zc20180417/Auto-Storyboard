{
  "pass": true,
  "summary": "seg02将广场大屏专访作为明确屏幕画面处理，保留主持人提问、沈清感谢母亲和周建国悔恨捶胸。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "主持人台词明确由广场LED大屏幕传出，并且主持人位于屏幕采访画面中，不会误作街头现场开口。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周建国悔恨台词约37字，用6-14秒8秒承载，约4.6字/秒，符合情绪喊话速度。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "沈清感谢周桂兰、周建国说出“报应啊”和“那是我的女儿和老婆啊”均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "现实空间是商业街头，采访内容明确标为广场大屏幕采访画面，属于屏幕画面例外。",
      "fix_instruction": "若不通过，应把屏幕内容独立标注为屏幕画面或另起组。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载沈清屏幕回答、周建国反应和周建国悔恨喊话，14秒内有足够台词和情绪转折支撑。",
      "fix_instruction": "若不通过，应拆分沈清回答和周建国悔恨。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、模型说明或官方占位符，仅使用自然短剧分镜语言。",
      "fix_instruction": "若不通过，应删除工程词和模板语气。"
    }
  ],
  "issues": [],
  "warnings": []
}
