{
  "pass": true,
  "summary": "第10集10-2段分镜通过审核，沈清逼问合同、刘美娟翻包找传单、沈清质问传单等关键剧情完整保留。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组各段台词字秒比均在6.5以内：沈清14字/3秒=4.67、刘美娟14字/3秒=4.67、沈清17字/3秒=5.67。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "皱巴巴的广告宣传单从刘美娟包底掏出→递到沈清面前→沈清接过→举到刘美娟眼前，道具归属和状态变化连续清楚。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清伸手要合同、刘美娟结巴推脱、沈清逼看手机银行、刘美娟翻包等关键动作和台词完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每段只承载一个主动作或一句对白：伸手要合同、结巴推脱、逼看手机、翻找包，动作拆分清楚。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面人物现场开口对白，每句写明说话人和对象。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组包含传单特写、递传单、接传单冷笑、质问等节拍，每段一个主动作，无过载。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
