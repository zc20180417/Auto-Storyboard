{
  "pass": true,
  "summary": "seg03 保留三大家主劳斯莱斯赶到工地、求饶、认错、陆凡命令自首和走向警车的完整动作链。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留三辆劳斯莱斯急刹、三大家主连滚带爬下车、赵家主痛哭求陆凡高抬贵手。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留李家主称金董逼迫并愿意赔偿、陆凡两句冷酷处置、钱家主答应去自首以及三人走向警车。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-3秒承载李家主约18字，字秒比约6.0；6-10秒承载陆凡约19字，字秒比约4.8，均低于6.5硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首锁定黑风山工地、泥泞路面、三辆劳斯莱斯、警车、陆凡和三大家主位置，人物行动前可用。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "急刹、下车、赵家主求饶和陆凡冷眼反应拆为4段共13秒，后续判罚另在第2组，密度可控。",
      "fix_instruction": "若不通过，应继续拆分车辆到达和求饶对白。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾三大家主在陆凡面前低头求饶，第2组首复述三人低头站在陆凡面前，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首补三大家主和陆凡的相对位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "李家主、陆凡和钱家主的每句现场对白都标明对陆凡或三大家主说，未出现无对象开口。",
      "fix_instruction": "若不通过，应补充真实对白对象。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板化批量描述、参考图或工程占位符。",
      "fix_instruction": "若不通过，应删除污染表达并改为现场可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
