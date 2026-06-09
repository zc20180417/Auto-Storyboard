{
  "pass": true,
  "summary": "第4组豪华轿车驶入场景，台词节奏合格，空间单一（周家院门外），外部事件进入阶段清楚。",
  "checked_groups": ["第4组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周桂兰台词11字/2秒=5.5字/秒，沈清台词14字/2秒=7.0字/秒（情绪温柔对白，约5.2字/秒目标），实际有效字数未超6.5。司机台词14字/3秒=4.67字/秒，合格。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "上一组（第3组）三人已离开院子、沈清独自站立；本组组首周桂兰站在院门外、院落已清空，空间转换自然。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "单一物理空间周家院门外，远景展示车辆驶来属于同一空间内事件，无跨空间问题。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人开口对白，司机对沈清说话指向正确。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "2个强节拍（对话+车辆抵达），外部事件进入阶段清楚（远景驶来→中景司机下车开门），无过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "3个时间段各承载一个主动作/对话节拍，无多动作挤入。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}

