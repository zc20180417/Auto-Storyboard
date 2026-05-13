{
  "pass": true,
  "summary": "seg03已审核，宋天明追问身份、陆凡压制回应、宋子昂被架起、宋家崩塌和押走命令均保留。",
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
      "evidence": "保留宋天明问‘商会总部的证据？你到底是谁！’和陆凡答‘你还没资格知道。’，随后警察架起宋子昂。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组6-10秒陆凡台词18字，4秒约4.5字/秒；10-12.5秒高局长台词14字，2.5秒约5.6字/秒，均低于硬上限。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部宋子昂被架起、宋天明看向儿子，第2组组首复述宋子昂被警察架住和宋天明被控制的状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "宋子昂在组首位于背景地面附近，两名警察位于两侧，因此6-12秒被架起前人物可用。",
      "fix_instruction": "若不通过，应在组首或动作前补足宋子昂所在位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂对宋天明喊，宋天明对宋子昂喃喃说，陆凡对宋天明说，高局长对警察命令，对象明确。",
      "fix_instruction": "若不通过，应补齐真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组按求救、崩溃、冻结资产、押走命令、押离动作推进，虽为5段但每段承载单一信息或动作。",
      "fix_instruction": "若不通过，应拆出押离动作或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
