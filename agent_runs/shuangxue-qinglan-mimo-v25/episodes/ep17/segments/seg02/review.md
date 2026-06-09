{
  "pass": true,
  "summary": "seg02含第3组，周美娟和赵强震惊对峙，沈清追问房租并爆发要求还钱，台词忠实、空间单一。",
  "checked_groups": ["第3组"],
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
      "evidence": "12秒5镜头，沈清'谁跟你是一家人！把十九万吐出来！'13字÷3.5秒=3.7字/秒，赵强'那个..咱们是一家人，分这么清干嘛'13字÷2秒=6.5字/秒恰好在硬上限，均合格。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "单组物理空间'周家正屋客厅'，组首列出沈清、周美娟、赵强、周建国四人位置和朝向，周建国从第2组瘫坐状态延续到背景沙发。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "台词'爸！这房子不是你的？''闭嘴！大人的事少插嘴！''原来你们连自己亲爹的话都信？'与原剧本17-2完全一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾沈清手持房产证、周建国瘫坐→第3组首沈清右手持房产证、周建国坐在背景沙发表情僵硬，位置和道具连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒5镜头，强节拍4个（震惊质问、怒斥、嘲讽、逼问房租+爆发），属同一对峙事件链，每段一个主动作。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段一个主动作或连续对话节拍，赵强讪笑和沈清爆发在同一时间段内属快速交锋。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
