{
  "pass": true,
  "summary": "第3-4组审核通过：廉价药盒揭穿和手机照片对质场景，台词忠实、道具连续、节奏合理。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组27字有效台词/11秒=2.45字/秒，其中周桂兰落泪台词按情绪对白5.2字/秒估算约1.5秒，分配3秒合理，留足反应时间。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "第4组保留原剧本全部关键动作：沈清拿出手机点开杂物间照片、举手机展示、质问八千块黑棉被、周美娟语塞回应'妈自己挑的'均完整。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组组尾塑料袋和空药盒散落桌面、周美娟身体僵住；第3组组首空药盒散落桌面和地面、沈清手指指向药盒，状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组强节拍：药盒证据展示、沈清愤怒台词、周桂兰落泪反应、周美娟狡辩，4个节拍分布在11秒内，每个时间段一个主动作，属同一事件链的连续推进。",
      "fix_instruction": "无需修改，强节拍分布合理。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第4组手机道具从沈清拿出→点开屏幕→举向周美娟→收回身前，状态变化清晰有可见过渡；空药盒从第3组延续到第4组组首。",
      "fix_instruction": "无需修改，道具连续性合格。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第4组4个时间段各承载一个主动作：嘲讽反问、拿出手机、举手机展示、厉声质问+语塞回应。无动作过载。",
      "fix_instruction": "无需修改，动作原子性合格。"
    }
  ],
  "issues": [],
  "warnings": []
}
