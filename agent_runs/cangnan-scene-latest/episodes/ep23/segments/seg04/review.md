{
  "pass": true,
  "summary": "seg04 保留周长海抵达半山腰、倒计时启动、工人求救和陆凡车辆逼近，半山腰状态连续。",
  "checked_groups": ["第9组", "第10组", "第11组"],
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
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "周长海下车、要求马上引爆、血狼按下计时器并确认三分钟后起爆，均与剧本一致。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "evidence": "工人“里面还有人在值班！会出人命的！”约16字分配4秒，约4字/秒并带绝望呼喊反应，不超过硬上限。"
    },
    {
      "group": "第11组",
      "type": "handoff_continuity",
      "evidence": "第10组尾周长海站在车灯前、工人被按住；第11组首复述周长海、血狼、工人、炸药和计时器位置后引入远光灯。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "工程炸药位于岩层前，血狼手中持有计时器，按下按钮后红色数字亮起，关键道具状态清楚。",
      "fix_instruction": "若不通过，应补充计时器和炸药位置。"
    },
    {
      "group": "第10组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "工人对周长海喊话，周长海对工人回应，现场对白对象明确。",
      "fix_instruction": "若不通过，应恢复具体说话对象。"
    },
    {
      "group": "第11组",
      "type": "filmability",
      "result": "pass",
      "evidence": "刺眼远光灯和越野车冲上盘山道均被转译为可见灯光、车辆运动和人群反应。",
      "fix_instruction": "若不通过，应删掉抽象压迫描述，改成灯光、车辆、人物动作。"
    },
    {
      "group": "第11组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载远光灯出现、越野车冲上山路和现场反应，10秒内动作节奏清楚。",
      "fix_instruction": "若过载，应拆出车辆急刹到下一组。"
    }
  ],
  "issues": [],
  "warnings": []
}
