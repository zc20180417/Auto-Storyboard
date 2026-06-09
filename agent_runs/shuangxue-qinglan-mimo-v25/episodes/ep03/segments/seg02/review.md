{
  "pass": true,
  "summary": "seg02共3组，ATM查账场景完整，周桂兰崩溃情绪到位，台词节奏合规。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组 7-12秒：'妈，按密码'4字，周桂兰按密码动作+机器按键声，节奏合理。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组完整保留'可用余额 37.62 元'屏幕显示、周桂兰'怎么只有三十七块六毛二？'台词、周桂兰瘫倒痛哭'钱呢！我女儿给我的救命钱呢！'，忠于原剧本。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "第3组9秒3个时间段：抱住母亲、咬牙发誓、打印凭条，每个时间段一个主动作，密度合理。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内对白，写明说话对象。ATM机器声音通过'机器发出滴滴的按键声'交代。",
      "fix_instruction": "无需修复，音画分离正确。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第2组 4-8秒：'怎么只有三十七块六毛二？'10字÷4秒=2.5字/秒，颤声慢语，原剧本明确'瞪大眼'情绪，可接受。8-12秒：'钱呢！我女儿给我的救命钱呢！'14字÷4秒=3.5字/秒，痛哭场景，合理。",
      "fix_instruction": "无需修复，节奏合理。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组首与第2组组尾连续：周桂兰瘫倒在机台面上、ATM屏幕仍显示37.62元、沈清扶住周桂兰肩膀。",
      "fix_instruction": "无需修复，状态连续。"
    }
  ],
  "issues": [],
  "warnings": []
}
