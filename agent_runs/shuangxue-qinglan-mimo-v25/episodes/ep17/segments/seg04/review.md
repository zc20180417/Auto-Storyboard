{
  "pass": true,
  "summary": "seg04含第5组，沈清举手机逼赵强还钱，周桂兰加入嘲讽，台词忠实、空间单一。",
  "checked_groups": ["第5组"],
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
      "evidence": "12秒4镜头，沈清'再往前一步，我马上按下去！'11字÷2.5秒=4.4字/秒，周桂兰'明天？你刚才不是说账上没钱吗？'13字÷2秒=6.5字/秒恰好在硬上限，均合格。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "手机从第4组掏出、第5组高举，归属沈清右手。房产证从第3组换至左手、第4-5组保持左手持有，状态连续。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "台词'再往前一步，我马上按下去！''千万别报！我明天就去凑钱还你！''明天？你刚才不是说账上没钱吗？''不用明天，就今晚。转账一分钟内不到位，警察局见。'均与原剧本17-4完全一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾赵强扑抢动作完成→第5组首赵强双手举起投降，状态由扑抢转为投降通过组间切换处理，可生成。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒4镜头，强节拍4个（威胁、投降哀求、嘲讽、最后通牒），属同一事件链连续推进，无过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词为画面人物现场开口对白，无心声或画外音。周桂兰的嘲讽为现场开口。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "最后一段5秒包含两句台词加短暂停顿，整体节奏偏慢但服务于最后通牒的压迫感",
      "evidence": "19字÷5秒有效=3.8字/秒，低于普通对白目标但有强调效果支撑。",
      "fix": "若需加快节奏可压缩至4秒。"
    },
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "character_availability",
      "problem": "周桂兰在第5组首次出现，之前未在组首空间锁定中出现",
      "evidence": "原剧本17-4明确列出周桂兰为在场人物，短视频中新角色直接出现属常见处理。",
      "fix": "无需修改。"
    }
  ]
}
