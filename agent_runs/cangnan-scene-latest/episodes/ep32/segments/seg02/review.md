{
  "pass": true,
  "summary": "seg02已审核，电话音来源、财团切割、龙天傲崩溃和收网命令均忠于原剧本。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "摩根总裁只以电话音出现，声音来源明确为龙万山手中的加密电话，龙万山嘴唇闭合不做口型。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "摩根总裁两句电话台词均完整保留，且保留亚洲账户冻结、财团切割龙家的因果。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“龙家恶意做空市场，证据确凿，立刻收网。”约20字分配4秒，约5字/秒；商会总管命令约13字分配4秒并含挥手动作，节奏可表演。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "摩根总裁未作为画面人物出现，组首明确其为电话音，龙万山、陆凡、商会总管均有可见位置。",
      "fix_instruction": "若不通过，应把摩根总裁改为电话音并补声音来源。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组结尾龙万山握电话脸色惨白，第4组组首延续他手持加密电话的状态，并让电话挂断声在0-2秒发生。",
      "fix_instruction": "若不通过，应补足电话从通话到挂断的可见过渡。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组包含挂断声、龙天傲崩溃、陆凡下令、总管挥手四个节拍，13秒内分段清楚，没有叠加复杂动作链。",
      "fix_instruction": "若不通过，应拆出龙天傲崩溃或总管下令。"
    }
  ],
  "issues": [],
  "warnings": []
}
