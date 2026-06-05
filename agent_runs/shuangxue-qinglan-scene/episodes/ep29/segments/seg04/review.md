{
  "pass": true,
  "summary": "seg04完整保留周桂兰半降车窗、拒绝原谅、递百元钞票、车辆离开和周建国雪地落泪，关键道具连续。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "周建国求原谅台词约25字用5秒承载，周桂兰拒绝台词约29字用5秒承载，均未超过6.5字/秒。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "百元钞票从周桂兰大衣口袋取出，递给司机，再由第9组司机塞给周建国，归属过渡清楚。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "司机塞钱、车窗升起、绿灯亮起、汽车扬长而去、周建国攥钱流泪均按原剧本收束。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "周桂兰“这位老先生，你认错人了，我丈夫早死了”保留原意和冷漠态度，没有改成原谅或争吵。",
      "fix_instruction": "若不通过，应恢复周桂兰拒绝原谅的原台词和态度。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "拿出钞票、递给司机、司机接钱分为三个时间段，没有把递钱和车辆驶离压在同一段。",
      "fix_instruction": "若不通过，应拆分递钱和车辆离开。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第9组为9秒片尾余波，承载塞钱、车窗升起车辆离开、周建国落泪三个短动作，短组理由成立。",
      "fix_instruction": "若不通过，应合并到第8组或延长有真实动作支撑的时间段。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定百元钞票、周建国手心、纯黑色豪华轿车和周桂兰车窗，数量为3条且不泛化。",
      "fix_instruction": "若不通过，应替换为本组具体车辆、钞票、人物风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
