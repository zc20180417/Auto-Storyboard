{
  "pass": true,
  "summary": "seg01三组保留凭条、金镯、周建国维护刘美娟和饭药质问，时间轴、对白指向、道具连续性均可执行。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "script_fidelity",
      "evidence": "原剧本中沈清扶周桂兰进客厅、37.62元凭条拍上茶几、沈清质问和刘美娟推脱均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "刘美娟右手腕先藏在身后，沈清在3-6秒抓腕上扯，古法金镯由隐藏变为灯下暴露，转移和揭示过程清楚。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "周建国台词约24字给4秒，约6.0字/秒；沈清台词约20字给3秒，约6.3字/秒；刘美娟短句约9字给3秒，均不超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定周家正屋客厅一个物理空间，沈清、周桂兰、刘美娟均有画面位置和身体朝向，打印凭条归属清楚。",
      "fix_instruction": "若不通过，应补齐人物位置、身体朝向和凭条位置。"
    },
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈清和刘美娟均为现场开口对白，分别写明对刘美娟、对沈清说道，没有心声或画外音混用。",
      "fix_instruction": "若不通过，应改为明确现场对白对象或标明声音来源。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "逼近质问、抓腕露镯、刘美娟尖叫、沈清追问分成四个时间段，每段只有一个主动作或一个连续对白节拍。",
      "fix_instruction": "若不通过，应拆开抓腕、露镯和台词承载。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项围绕古法金镯、刘美娟手腕、打印凭条、周桂兰四个本组锚点，没有使用泛泛占位词。",
      "fix_instruction": "若不通过，应删除无锚点泛泛词并改为本组具体人物道具。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部沈清抓刘美娟腕、凭条在茶几中央；第3组组首复述相同状态，并在4-7秒写明沈清松开手。",
      "fix_instruction": "若不通过，应在第3组组首或动作段补清手腕和凭条状态。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有Seedance说明词、模板编号、官方占位符、参考图或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程说明和模板化描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
