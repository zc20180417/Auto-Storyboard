{
  "pass": true,
  "summary": "seg02完整覆盖进入自助银行、插卡输密码、查询余额、崩溃痛哭和打印凭条，银行卡与小票状态连续且无硬问题。",
  "checked_groups": ["第5组", "第6组", "第7组", "第8组"],
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
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清两句短对白分别给2.5秒和2秒，按密码动作另给3.5秒，口型和手部操作没有互相挤压。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "屏幕金额严格写为可用余额37.62元，周桂兰台词保留“三十七块六毛二”。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "破旧银行卡从插卡口到拔出、白色余额小票从出纸口到沈清口袋都有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定自助银行玻璃门内，沈清扶周桂兰且持卡，第一帧与进入ATM流程一致。",
      "fix_instruction": "若失败，应明确玻璃门、ATM、沈清、周桂兰和银行卡位置。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒承载周桂兰扑靠、痛哭、沈清抱住安抚、打印凭条和拔卡，具备情绪转折、关键道具操作和完整动作链。",
      "fix_instruction": "若失败，应拆出打印凭条或压缩无台词反应，但当前容量充足。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "周桂兰软倒、沈清托住、沈清说话、打印拔卡分段呈现，每段一个主动作。",
      "fix_instruction": "若失败，应把扶人和打印凭条拆成独立时间段。"
    }
  ],
  "issues": [],
  "warnings": []
}
