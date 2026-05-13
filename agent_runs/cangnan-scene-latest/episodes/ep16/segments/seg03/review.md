{
  "pass": true,
  "summary": "三组保持工地讨薪、煽动、安抚失败和砖块袭击的递进，动作链和现场对白可生成。",
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
      "evidence": "数百名工人举横幅堵门、工人甲讨薪、宋家手下带头起哄和手下甲喊砸工地均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "江若晴约22字台词用5秒承载，约4.4字/秒；工人甲约21字台词用5.5秒承载并含举砖动作，节奏可表演。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾部手下甲看向砖块堆，第3组组首手下甲靠近砖块堆，随后弯身抓砖和砸向江若晴，动作衔接清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "三组均保持黑风山工地大门口一个物理空间，人物、人群、围挡、砖块堆位置明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "江若晴对工人群喊话，工人甲对江若晴怒喊，现场对白对象明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只承载抓砖、砸砖、江若晴尖叫和防护反应，总时长10秒，属于清晰动作冲突，不存在多线过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "袭击信息通过半头砖、飞行轨迹、江若晴抬臂自护和人群惊乱表现，未用抽象心理结论替代画面。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
