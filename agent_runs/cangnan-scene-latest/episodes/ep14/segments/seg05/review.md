{
  "pass": true,
  "summary": "seg05 按源文件重复的14-3段落再次呈现水柱压制和刀疤撤退，未新增或改写剧情，无硬问题。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "源segment重复14-3，分镜再次保留水柱喷射、混混甲惨叫、前排翻滚和刀疤喊顶住。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "混混甲约8字用2秒，刀疤约8字用3秒，台词节奏未超过6.5字/秒。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "evidence": "第9组尾部刀疤倒地喊顶住，第10组组首刀疤仍在泥地，水柱持续，撤退动作承接清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "虽与seg03内容重复，但这是episode源脚本中重复出现的段落，分镜没有自行删去或改成新剧情。",
      "fix_instruction": "若不通过，应以源脚本为准保留重复段落或由上游修正源脚本。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "陆凡车顶观察、混混逃窜、刀疤喊撤、带人逃跑分为4个节拍，12秒内动作可表演。",
      "fix_instruction": "若不通过，应拆分撤退喊话与逃跑全景。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文保持自然分镜描述，没有模型说明词、模板编号、参考图或自动分镜表述。",
      "fix_instruction": "若不通过，应删除污染词并改成可见画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
