{
  "pass": true,
  "summary": "seg04三组覆盖求饶、持刀行凶、民警制伏和林夏严查，未发现硬问题。",
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
      "evidence": "赵大江跪地求饶、陆凡拒绝、赵大江发狠摸向裁纸刀均对应原剧本。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "evidence": "持刀刺向腹部、陆凡闪开、民警冲入按手、夺刀按倒拆成5个时间段，12秒内动作链清楚。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "林夏先对赵大江怒斥，再对纪委干部下令，两个说话对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "裁纸刀在组首位于办公柜边缘，赵大江先看向刀再摸刀，归属变化有过渡。",
      "fix_instruction": "若不通过，应补裁纸刀初始位置或赵大江摸刀动作。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "民警在组首锁定为门外走廊暗处可从打开门口进入，冲入制止前已有空间来源。",
      "fix_instruction": "若不通过，应把民警提前锁定在门外或增加入场动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组结尾赵大江被按倒、刀脱手；第3组组首继续锁定赵大江在地、民警控制、刀远离手边。",
      "fix_instruction": "若不通过，应复述赵大江被控制和刀的位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
