{
  "pass": true,
  "summary": "第10集10-3段分镜通过审核，赵强打圆场被沈清反击、沈清带母离场、刘美娟赵强惊慌密谋等关键剧情完整保留。",
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
      "evidence": "第1组各段台词字秒比均在6.5以内：赵强18字/3秒=6.0、沈清16字/3秒=5.33、赵强13字/3秒=4.33、沈清14字/3秒=4.67。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组组尾：沈清扶周桂兰手臂、宣传单收在手中。第2组组首：沈清扶周桂兰、手持宣传单和流水单。状态连续。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "赵强打圆场'合同都在公司走账'、沈清反击'钱根本不在我妈名下'、赵强'自家人放谁名下不都一样'、沈清'带我妈去银行查'等关键台词完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每段只承载一个说话人的对白，赵强和沈清交替对峙节奏清楚，无动作过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面人物现场开口对白，每句写明说话人和对象。沈清'非法侵占'为对赵强和刘美娟的当面警告。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组3个时间段：沈清警告+扶母离场、刘美娟惊慌抓赵强、赵强密谋烧账单，每段一个主动作，8秒短组属短动作余波。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
