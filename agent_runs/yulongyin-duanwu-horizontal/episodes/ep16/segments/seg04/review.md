{
  "pass": true,
  "summary": "第5组保留烈日土路、爸爸扛牛皮狂奔、正午前绷鼓皮的画外心声、抬头看太阳和汗落黄土，音画口型处理正确。",
  "checked_groups": [
    "第5组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "5-9秒明确写爸爸嘴唇闭合不做口型，台词作为画外心声响起，符合原剧本OS而非现场开口。"
    },
    {
      "group": "第5组",
      "type": "horizontal_composition",
      "evidence": "土路从左前景延伸到右后方，爸爸从左中景向右后方奔跑，太阳在上方偏右，宽画幅呈现路径和时间压力。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "烈日热浪、扛牛皮狂奔、正午前绷鼓皮心声、抬头看太阳加快脚步、汗水滴入黄土均来自原剧本，没有新增剧情。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "画外心声约25个有效字安排在4秒内，作为紧迫内心独白约6.3字/秒，未超过硬性上限且画面有奔跑动作支撑。",
      "fix_instruction": "若不通过，应延长心声承载时间或拆分到相邻奔跑镜头。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确土路左前景、右后方村口、爸爸进入方向、牛皮在右肩和太阳位置，单一物理空间清楚。",
      "fix_instruction": "若不通过，应补充土路方向、村口方位和爸爸奔跑路线。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内只有环境建立、奔跑、画外心声、看太阳加速、汗落黄土五个节拍，动作和心声承载不拥挤。",
      "fix_instruction": "若不通过，应删除非关键空镜或拆开心声和看太阳动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
