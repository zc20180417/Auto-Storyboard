{
  "pass": true,
  "summary": "seg05已审核，备用探照灯、龙天傲押解求饶、陆凡带走命令和回苍南收尾均与剧本一致。",
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
      "evidence": "备用探照灯亮起、龙天傲被拖进押解车并求饶、陆凡回答“晚了。带走。”均按原剧本呈现。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "evidence": "商会总管请示约23字分配5秒，陆凡“回苍南。项目到了该收尾的时候了。”约16字分配4秒，口型节奏自然。"
    },
    {
      "group": "第10组",
      "type": "space_locking",
      "evidence": "第10组切到庄园大院外街道，组首明确新空间为街道并列出陆凡、商会总管、车队和纠察员位置，属于场景收尾转换。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙天傲对陆凡求饶，陆凡对联合纠察员下令带走，对象明确。",
      "fix_instruction": "若不通过，应补足求饶和命令的真实对象。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第9组含探照灯亮、拖向押解车、求饶、陆凡命令四个节拍，13秒内分段清楚，拖行动作给5秒。",
      "fix_instruction": "若不通过，应压缩探照灯或拆分押解动作。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第10组没有模板编号、参考图、自动分镜、字幕或广告式说明，结尾以可见雨风、外套、车队警灯承载收尾意象。",
      "fix_instruction": "若不通过，应删除工程说明词并改成自然画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
