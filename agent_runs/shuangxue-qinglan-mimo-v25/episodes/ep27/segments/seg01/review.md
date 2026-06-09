{
  "pass": true,
  "summary": "第1-2组审核通过，离婚协议签字和沈清宣判场景台词节奏合理、空间锁定完整。",
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
      "evidence": "债主台词13字/2.5秒=5.2字/秒，周建国台词13字/2秒=6.5字/秒，均未超过硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清两段台词'从今天起你跟我妈没有任何关系'和'你们一家三口就留在这慢慢还那五百万的合法债务吧'完整保留。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首列出周建国、债主张总、沈清、律师四人位置和朝向，均为龙腾酒店宴会厅同一空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白为现场开口，债主张总冷喝、周建国哀求、沈清冷笑均写明说话对象。",
      "fix_instruction": "若不通过，应检查是否有心声被写成现场开口。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "11秒内4个时间段各承载一个主动作：律师拍诉状、周建国哀求、签字按手印、绝望嘶吼，无过载。",
      "fix_instruction": "若不通过，应拆分时间段。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾周建国坐桌前、沈清站左侧后方、离婚协议在桌面，第2组组首状态一致。",
      "fix_instruction": "若不通过，应在组尾或组首补具体状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
