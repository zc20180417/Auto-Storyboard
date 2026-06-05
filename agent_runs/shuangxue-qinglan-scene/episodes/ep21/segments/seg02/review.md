{
  "pass": true,
  "summary": "seg02保留赵强端豆浆耍赖、沈清回应并命令王队长进场，分成两个可执行组。",
  "checked_groups": ["第2组", "第3组"],
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "赵强从屋里出来、手端热豆浆、两句耍赖台词均按原文保留，未把豆浆改为其他道具。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清第一句约13字用3秒约4.3字/秒，第二句约27字用5秒约5.4字/秒，均未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾赵强端碗站在周美娟身侧，第3组首延续为赵强在画面右侧手持热豆浆碗，沈清和律师位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵强现场对律师和沈清开口，两句均写明对话对象，没有画外音误承载。",
      "fix_instruction": "若不通过，应补充赵强具体对谁说道。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为赵强出屋到台阶前加两句连续挑衅，12秒承载一个3秒入场动作和两个连续对白节拍，密度正常。",
      "fix_instruction": "若不通过，应把出屋动作与两句对白拆成两个短组。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "工程队长在组首位于院门外侧背景，被院门遮住半身，沈清转头对他说话前已经可用。",
      "fix_instruction": "若不通过，应在工程队长说话或被呼叫前安排清楚入场或画外位置。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "热豆浆碗从赵强组首持有，到出屋、说话、组尾均在他手中，未跳变到地面或他人手中。",
      "fix_instruction": "若不通过，应补充赵强端碗、收碗或放碗的可见动作。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "沈清回应、转头下令、院门外车辆刹停声与王队长点头分为三个时间段，每段主动作单一。",
      "fix_instruction": "若不通过，应拆出车辆刹停和王队长回应。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定工程队长、赵强热豆浆碗、周美娟和沈清清场指令，共3条，未使用占位项。",
      "fix_instruction": "若不通过，应删除泛泛禁止项并改成具体剧情错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
