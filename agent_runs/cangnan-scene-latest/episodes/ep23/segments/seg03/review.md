{
  "pass": true,
  "summary": "seg03 保留无牌车闯入、牛大春阻拦被推倒、佣兵卸炸药和血狼封锁入口命令，动作链清楚。",
  "checked_groups": ["第6组", "第7组", "第8组"],
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
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "十辆无牌越野车撞开工地大门、黑衣壮汉下车、牛大春举铁锹阻拦三项关键动作和台词均保留。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "血狼“滚开。”2秒内完成并配合冷笑；牛大春求报警台词约15字分配3秒，约5字/秒，符合痛呼急喊。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "工程炸药先在越野车后厢，随后被黑衣人搬下并运向半山腰，关键道具转移过程可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "牛大春、血狼和佣兵们在组首分别位于工地门内、第一辆越野车内和后方车辆内，之后行动顺序成立。",
      "fix_instruction": "若不通过，应在组首补充车内血狼和佣兵位置。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有血狼短句、推倒牛大春、牛大春呼救和佣兵越过四个节拍，10秒内不拥挤。",
      "fix_instruction": "若过载，应把呼救和佣兵进入拆开。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组仍在黑风山工地大门内侧，卸炸药和封锁入口都发生在同一主要空间，没有跨场景混用。",
      "fix_instruction": "若不通过，应把半山腰装药动作拆到后续半山腰组。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾牛大春倒在门内，第8组首复述他倒在左前方、铁锹落在身旁，状态连续。",
      "fix_instruction": "若不连续，应在第8组首补足倒地位置和铁锹状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
