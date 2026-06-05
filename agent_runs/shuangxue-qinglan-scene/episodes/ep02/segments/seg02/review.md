{
  "pass": true,
  "summary": "seg02 已对照原剧本完成审核，刘美娟入场、递蛋糕羞辱、冷粥质问和夺卡借口均保留，未发现硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟递蛋糕台词约 23 个有效字 / 4 秒，约 5.8 字/秒；沈清质问约 18 字 / 3.5 秒，约 5.1 字/秒，均未超过硬上限。"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "evidence": "刘美娟在第1组 2-5 秒明确推门入场，随后才在 8-12 秒对沈清开口，人物可用性成立。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "第3组组尾写刘美娟的手停在银行卡前方，第4组组首继承该状态，银行卡仍由沈清持有。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写杂物间内的沈清、周桂兰、银行卡和关闭的门，刘美娟通过后续推门动作入场。",
      "fix_instruction": "若不通过，应把未入场人物从组首删除，并在说话前安排入场。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本中草莓蛋糕、好菜吃光、帝王蟹与冷粥对比、胃口不好借口均保留。",
      "fix_instruction": "若不通过，应恢复原剧本关键台词和蛋糕羞辱动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含沈清反问鞋底、刘美娟看到银行卡、向周桂兰急问、伸手探向卡，动作按阶段拆开，没有把夺卡结果提前完成。",
      "fix_instruction": "若不通过，应把逼近质问和伸手夺卡拆成更清楚的两个组。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟先对周桂兰说卡会弄丢，再对沈清说放她这里最安全，对话对象符合现场关系。",
      "fix_instruction": "若不通过，应分别标明对周桂兰或沈清说。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定刘美娟、银行卡、沈清和草莓蛋糕，数量 3 条，和本组夺卡风险一致。",
      "fix_instruction": "若不通过，应删除泛泛词并补入本组具体道具。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文是自然短剧分镜，没有模板编号、参考官方模板、@图片或模型说明词。",
      "fix_instruction": "若不通过，应删除模板污染内容。"
    }
  ],
  "issues": [],
  "warnings": []
}
