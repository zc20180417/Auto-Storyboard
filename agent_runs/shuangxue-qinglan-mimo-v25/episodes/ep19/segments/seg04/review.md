{
  "pass": true,
  "summary": "第5-6组通过审核，周建国入场自然，驱逐令台词完整，状态连续。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "沈清13字÷3.5秒=3.7字/秒；周建国13字÷3秒=4.3字/秒；沈清18字÷3.5秒=5.1字/秒。均合理。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清14字÷2.5秒=5.6字/秒；沈清11字÷2.5秒=4.4字/秒；周美娟9字÷3秒=3.0字/秒；周建国17字÷3秒=5.7字/秒。均合理。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "evidence": "周建国在组首空间锁定中明确位于画面左侧入口处，面向镜头，有明确入场动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金镯子从第4组纸巾中→第5组收进衣袋，纸巾包裹状态连续。衣袋收起动作在0-3.5秒时间段内完成。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部：沈清画面中央、周建国画面左侧攥拳、赵强原地看周建国、周美娟背景捂手腕。第6组首：沈清画面中央对准周建国、周建国画面左侧攥拳铁青、赵强画面右侧原地、周美娟背景捂手腕。连续无跳变。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作或连续对话节拍：沈清命令、沈清厉喝+反应、周美娟大喊、周建国暴跳。非主动作人物赵强只写站位和轻反应。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
