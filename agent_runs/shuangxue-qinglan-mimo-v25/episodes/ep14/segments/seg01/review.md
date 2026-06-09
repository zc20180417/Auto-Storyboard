{
  "pass": true,
  "summary": "seg01分镜忠实原剧本，台词指向清楚，时间节奏合理，空间锁定完整。",
  "checked_groups": ["第1组"],
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
      "evidence": "周美娟2句对白19字÷4秒=4.75字/秒，赵强2句20字÷4秒=5字/秒，沈清1句7字÷2秒=3.5字/秒含转身走位，周桂兰2句14字÷2秒含递卡动作，均在合理范围内。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首列出全部5名在场人物的位置和朝向。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "5句对白全部保留原词，说话对象明确，周桂兰递卡动作忠实原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内现场开口，每句写明说话人和对象。",
      "fix_instruction": "若不通过，应补充说话人和对象指向。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "强节拍3个，属同一冲突链的连续推进，每段只承载一个主动作，12秒容量充足。",
      "fix_instruction": "若不通过，应拆分强节拍或延长组时长。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾写明沈清持有银行卡、周美娟原位、赵强抱臂，为下一组提供连续锚点。",
      "fix_instruction": "若不通过，应在组尾补充具体人物位置和道具状态。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "旧银行卡从周桂兰手中递到沈清手中，有明确交接动作，道具归属清楚。",
      "fix_instruction": "若不通过，应补充道具过渡动作。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "6个时间段各承载一个主动作或连续对话节拍，无过载。",
      "fix_instruction": "若不通过，应拆分过载时间段。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为普通对话组，无复杂动作/保护站位/关键道具操作，省略视频禁止项合理。",
      "fix_instruction": "若不通过，应补充2-5个本组特有视频禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
