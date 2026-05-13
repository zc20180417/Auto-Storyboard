{
  "pass": true,
  "summary": "seg03真实检查了毒液瓶救险、爸爸击飞胡永贵、龙鳞脱手和呼唤云宝，动作因果与空间连续均成立。",
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
      "evidence": "毒液瓶急速坠向泉眼、天天喊“泉水危险！”、飞扑抱住瓶子和手臂被岩石划破均保留。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "天天在中央偏左低处，爸爸由左向右出拳，胡永贵在右侧被击中并飞出，横屏动作线明确。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "爸爸台词“云宝，快接住它！”放在3-6秒，约7字/3秒，并由举手和抬头动作承载，节奏可表演。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "毒液瓶从下坠到被天天抱住，位置从中央上方到泉眼边低处，归属变化有可见动作。",
      "fix_instruction": "如不通过，应补充瓶子从胡永贵手中落下到天天接住的连续动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组仅承载爸爸出拳、胡永贵惨叫、胡永贵被砸飞、龙鳞脱手，11秒内动作链完整。",
      "fix_instruction": "如不通过，应拆分惨叫或龙鳞脱手镜头。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部爸爸即将张开手，龙鳞在半空，为下一段爸爸张开手、云宝跃起提供明确衔接。",
      "fix_instruction": "如不通过，应在组尾补充云宝位置和龙鳞悬停状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
