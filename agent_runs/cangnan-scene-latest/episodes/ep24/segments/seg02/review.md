{
  "pass": true,
  "summary": "seg02保留周长海按遥控器、民警夺下并押送上车的关键动作，台词对象和道具归属清楚。",
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
      "type": "prop_continuity",
      "evidence": "遥控按钮先在周长海右手，随后被民警抓住手腕并夺下，最后落入民警手中，关键道具转移有可见过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "周长海挣扎台词约20字安排在3-7秒，约5字/秒；民警短句安排在7-10秒，没有超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "陆凡的周首富台词、周长海声称认识省里大人物、民警要求去经侦大队、押上警车均按原剧本顺序呈现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周长海、陆凡和两名民警都在组首拥有位置、朝向和可操作状态，民警在夺遥控器前已经可用。",
      "fix_instruction": "若不通过，应在组首补足民警位置或安排明确入场动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部周长海被按倒、遥控器被控制；第2组首周长海跪伏在泥地、双手受控，连续性成立。",
      "fix_instruction": "若不通过，应在第2组组首补充周长海已被按倒和遥控器归属。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对周长海说道、周长海对陆凡喊道、民警对周长海说道，三处现场对白对象明确。",
      "fix_instruction": "若不通过，应逐句补足说话对象。"
    }
  ],
  "issues": [],
  "warnings": []
}
