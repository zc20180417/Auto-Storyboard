{
  "pass": true,
  "summary": "seg04保留龙舟破浪、青金龙影托流、天天与爸爸对话、冲线动作，水上和水下空间有明确分层。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "horizontal_composition",
      "evidence": "第5组上半部船头和人物、下半部水下龙影，左向右高速运动和水流方向一致，横屏空间明确。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "天天长句约30字安排5秒，字秒比约6，处于可承载范围；爸爸8字约3秒，天天欢呼2字约2秒。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "保留“爸爸，是云宝！它虽然沉在井底，但这条河到处都是它的力量！”、“它一直在守护我们。”、“冲啊！”以及最终重鼓冲线。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "水上船身人物与水下青金龙影分为上下画面层，明确是龙舟正下方深水，不混成同一物理平面。",
      "fix_instruction": "若不通过，应明确水上和水下镜头的空间切换。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天身体朝向爸爸说长句，爸爸回头对天天回应，随后天天对前方终点线欢呼，对象清楚。",
      "fix_instruction": "若不通过，应补充说话对象或反应镜头。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内承载长句、爸爸回应、天天欢呼和冲线，动作均围绕同一冲刺空间，没有额外支线。",
      "fix_instruction": "若不通过，应拆分长句和冲线动作或压缩非关键水花描写。"
    }
  ],
  "issues": [],
  "warnings": []
}
