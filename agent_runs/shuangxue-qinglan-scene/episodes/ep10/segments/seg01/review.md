{
  "pass": true,
  "summary": "seg01保留刘美娟理财搪塞、赵强附和、沈清追问收益和周桂兰劝和的完整因果，时间与空间连续可执行。",
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
      "evidence": "保留刘美娟挡在赵强身前并说“谁说这钱被我们花了！我是拿去理财了！”以及沈清用建材店账户反问的关键台词。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟19字用4秒、赵强17字用3.5秒、沈清20字用4秒，均低于6.5字/秒且没有低密度长组。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "组首继承沈清手中手机流水记录和刘美娟挡住赵强的位置，组尾保留周桂兰在沈清身边，为后续逼要凭证衔接。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "挡人动作、刘美娟辩解、沈清反问、刘美娟继续强辩分在四个时间段，单段主动作清楚。",
      "fix_instruction": "若不通过，应拆开挡人动作和台词承载。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组是同一冲突下三句连续交锋加1.5秒反应，没有同时塞入新道具操作或跨空间动作。",
      "fix_instruction": "若不通过，应把赵强附和或沈清追问拆到相邻组。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟、周桂兰、沈清每句现场对白都写明对沈清或对周桂兰说，未出现假对白对象。",
      "fix_instruction": "若不通过，应补足真实对话对象。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组涉及保护赵强的站位和手机流水关键道具，视频禁止项共3条并锚定刘美娟、沈清手机流水记录、赵强。",
      "fix_instruction": "若不通过，应删除泛泛禁止项或补充本组人物道具锚点。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、模板编号、参考图、@图片或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明词和模板污染内容。"
    }
  ],
  "issues": [],
  "warnings": []
}
