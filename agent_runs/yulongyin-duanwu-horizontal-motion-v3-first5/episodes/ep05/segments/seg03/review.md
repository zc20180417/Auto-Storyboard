{
  "pass": true,
  "summary": "seg03 两组完成胡永贵黑液污染威胁、天天阻止、云宝护泉和灰化结果，灾害状态链明确且无硬问题。",
  "checked_groups": [
    "第5组",
    "第6组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "第5组保留胡永贵大怒台词“邪门了！我今天非把这破洞平了不可！”，并按原剧本让他拎起黑色废液泼向泉眼，天天喊“不要！”。"
    },
    {
      "group": "第5组",
      "type": "horizontal_composition",
      "evidence": "天天和水壶在左前景，胡永贵与黑色废液桶在右中景和右后侧，泉眼在中央后景，黑液从右侧弧线压向中央泉眼。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "黑液弧线在组首悬于画面中上部，云宝从左前景水壶口跃到中央泉眼前承接，3-6秒黑液浇在云宝身上，9-13秒落到灰化结果。"
    },
    {
      "group": "第6组",
      "type": "camera_motion",
      "evidence": "第6组先横向跟拍云宝从水壶到泉眼，再固定黑液落点，后拉呈现天天和胡永贵反应，最后固定灰化特写，运镜服务保护路径和结果落点。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "胡永贵 3.5 秒承载约 18 个有效字，天天 3.5 秒承载“不要！”，均低于 6.5 字/秒硬上限且对象明确。",
      "fix_instruction": "若胡永贵台词偏快，应延长 0-3.5秒或拆出反应镜头，不应改写台词。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首以天天、水壶、云宝、胡永贵、黑液弧线、泉眼和水洼的静态位置开场，没有把跃出、浇落、摔倒或灰化动作写进组首空间锁定。",
      "fix_instruction": "若组首包含过程动作，应改成第一帧静态状态并把动作移入时间段。"
    },
    {
      "group": "第6组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "信息链从黑液压向泉眼，推进到云宝从水壶跃出护泉，再到黑液浇身惨叫、摔落、青蓝身体变死灰色，结果清楚留在组尾。",
      "fix_instruction": "若结果不清，应补足黑液浇中云宝和云宝灰化后的可见状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
