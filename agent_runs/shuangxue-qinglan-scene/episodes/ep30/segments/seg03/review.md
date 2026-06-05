{
  "pass": true,
  "summary": "seg03保留女助理汇报、沈清签字命名和安养院接收规则，拆为两组后对白速度和动作状态稳定。",
  "checked_groups": ["第4组", "第5组"],
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "女助理汇报收购强盛建材对面街道、改建公益养老院，沈清命名桂兰安养院，均按原剧本保留。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "沈清关于优先接收和诚信档案的长句约28字用6秒，字秒比约4.7；女助理短句约5字用2.5秒，不存在超速。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "计划书和钢笔由女助理递向沈清，沈清接过后签字，第4组尾部明确仍在沈清手中，第5组组首继续继承。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "入场递计划书、两句汇报、沈清签字命名分别分段，单段主动作清楚。",
      "fix_instruction": "如不通过，应将递计划书或签字动作独立出来。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组只承载沈清制度要求、女助理接回计划书和离开，11秒内节拍集中且没有并列过载。",
      "fix_instruction": "如不通过，应拆出女助理离场或减少非关键反应。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部沈清持有钢笔和计划书，第5组组首明确已经签过字的计划书和钢笔仍在沈清手中。",
      "fix_instruction": "如不通过，应补写计划书和钢笔在组尾与组首的状态。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "没有Seedance说明、模板编号、参考图占位或广告式字卡。",
      "fix_instruction": "如不通过，应删除污染词并改为自然分镜。"
    }
  ],
  "issues": [],
  "warnings": []
}
