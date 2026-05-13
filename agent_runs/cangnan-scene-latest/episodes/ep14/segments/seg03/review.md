{
  "pass": true,
  "summary": "seg03 两组保留高压水柱冲散混混、混混甲惨叫、刀疤喊顶住和撤退的动作结果，无硬问题。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "数十道水柱喷射、混混甲惨叫、前排被掀翻、刀疤被冲倒仍喊顶住均完整保留。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "混混甲约8字用2秒，刀疤约8字用3秒，情绪喊话节奏均未超过6.5字/秒。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "evidence": "第5组尾部刀疤倒地指挥，第6组组首刀疤仍在泥地上，混混部分倒地或丢下武器，状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "水柱喷射、冲击人群、混混惨叫、前排翻滚、刀疤喊顶住分成5个连续节拍，12秒内不压缩关键台词。",
      "fix_instruction": "若不通过，应拆分水柱冲击和刀疤喊话。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "陆凡站越野车顶冷看、混混丢盔弃甲逃窜、刀疤喊撤和带人逃跑均来自原剧本。",
      "fix_instruction": "若不通过，应恢复陆凡车顶位置和刀疤撤退台词。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图、首尾帧或自动分镜等工程词。",
      "fix_instruction": "若不通过，应删除工程说明并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
