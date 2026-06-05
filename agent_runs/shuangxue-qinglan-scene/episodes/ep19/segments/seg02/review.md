{
  "pass": true,
  "summary": "seg02完成税务局威胁和金镯子目标揭示，台词顺序、手机转账记录、金镯道具归属均清楚。",
  "checked_groups": ["第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "周美娟讹人台词、沈清转账记录和假账威胁、赵强求饶要价均按原剧本顺序保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清税务局台词约19字用3.5秒，约5.4字/秒；假账台词约19字用3.5秒，约5.4字/秒，低于6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "金镯子在组首明确戴在周美娟右手腕，3-5秒被沈清目光锁定，组尾仍在周美娟手腕上。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为现场人物开口，对象为沈清、周美娟和赵强，没有画外音或心声混用。",
      "fix_instruction": "若不通过，应补充说话对象或声音来源。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "8秒短组只承载沈清指出值钱物、目光落镯和命令摘镯，属于关键道具插入与短促压迫节拍。",
      "fix_instruction": "若不通过，应与上一组合并或拆出金镯特写。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定周美娟金镯、沈清抢镯风险和赵强位置，均为本组具体剧情错误。",
      "fix_instruction": "若不通过，应替换为带人物和道具锚点的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
