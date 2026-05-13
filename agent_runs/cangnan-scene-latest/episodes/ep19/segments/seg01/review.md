{
  "pass": true,
  "summary": "seg01已按雨夜追撞到砸窗威胁的剧本顺序完成，台词、关键道具和车辆状态均保留。",
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
      "evidence": "原剧本中保时捷雨中疾驰、悍马撞车尾、江若晴惊呼、保时捷撞护栏熄火均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "疯狗台词“江总，下车聊聊吧！”分配3秒，江若晴尖叫“救命！你要干什么！”分配3秒，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "铁棒在组首即由疯狗持有，随后用于砸碎车窗，破碎车窗状态进入组尾衔接。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定盘山公路、保时捷、悍马和江若晴驾驶位，人物与车辆起点可生成。",
      "fix_instruction": "若不通过，应补齐车辆位置、江若晴朝向和悍马相对车尾位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "疯狗对江若晴说道，江若晴对疯狗尖叫，现场开口对象明确。",
      "fix_instruction": "若不通过，应把每句对白改为A对B说道或喊道。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部保时捷斜停护栏边、悍马在后方；第2组组首复述同一位置并让疯狗从悍马旁出现。",
      "fix_instruction": "若不通过，应在第2组组首复述斜停车辆、驾驶位江若晴和悍马停靠状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
