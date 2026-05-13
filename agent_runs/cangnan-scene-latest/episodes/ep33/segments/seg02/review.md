{
  "pass": true,
  "summary": "seg02已保留陆凡下车、江若晴惊喜、工人欢呼、牛大春喊放鞭炮以及陆凡接过金剪刀的动作，审核通过。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "evidence": "陆凡在组首被锁定为位于最前方车辆内，先下车再接受江若晴呼喊和工人围拢。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "江若晴短句用1.5秒快速惊喜喊出，牛大春10字用2秒，均未超过6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "陆凡原台词完整保留，随后走向剪彩台并接过江若晴递来的金剪刀，未新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "鞭炮声作为画外环境声处理，有工人转身跑向会场侧边和人群反应作为可见载体。",
      "fix_instruction": "若不通过，应补充声音来源或人物听见后的反应。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金剪刀在组首位于江若晴手中，7.5-10秒明确递出并由陆凡接过。",
      "fix_instruction": "若不通过，应补充递出、接过或道具归属变化。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部陆凡站在车旁，第4组通过组首锁定他在车队与剪彩台之间，并在组内走向剪彩台。",
      "fix_instruction": "若不通过，应补足陆凡从车旁到剪彩台的移动。"
    }
  ],
  "issues": [],
  "warnings": []
}
