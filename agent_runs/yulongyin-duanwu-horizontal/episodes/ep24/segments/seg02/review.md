{
  "pass": true,
  "summary": "seg02三组完整覆盖龙鳞牵引云宝、爸爸护住云宝、前扑导致毒液瓶脱手，横屏动线与道具连续。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留云宝颤抖、哀鸣并向龙鳞方向飘去，天天和胡永贵两句台词顺序未改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "爸爸怒吼“别做梦了！”时胡永贵在画面右侧可见，台词对象明确。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "毒液瓶从胡永贵右手下方脱落并坠向泉眼，承接下一段瓶子急速下坠。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "爸爸和天天在左侧，胡永贵在右侧，云宝的移动方向明确为左向右被龙鳞吸引。",
      "fix_instruction": "如不通过，应明确左右阵营和云宝飘移动线。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载攥紧云宝、怒吼、压低重心三项节拍，10秒内可演。",
      "fix_instruction": "如不通过，应拆出爸爸护住云宝或前扑准备。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爸爸从左向右扑，胡永贵始终在右侧，毒瓶从右侧上方下坠，轴线清楚。",
      "fix_instruction": "如不通过，应补充中性全景或删除无依据换边。"
    }
  ],
  "issues": [],
  "warnings": []
}
