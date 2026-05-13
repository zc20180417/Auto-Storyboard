{
  "pass": true,
  "summary": "seg05保留陆凡回应罗斯柴尔德、拒绝调防、挂断电话并望向乌云冷笑的收尾，审核通过。",
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
      "type": "dialogue_pacing",
      "evidence": "陆凡17字用3.5秒，约4.9字/秒；商会总管24字用5秒，约4.8字/秒；均未超过6.5字/秒。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "商会总管只通过电话音出现，陆凡听电话时嘴唇闭合不做口型。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "陆凡“不必”和“这里是我们的地盘……”两句台词完整保留，随后挂断电话、捏住手机、转身看乌云冷笑。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为电话问答和手部反应，动作轻，13秒内没有外部事件或道具复杂操作叠加。",
      "fix_instruction": "若不通过，应将陆凡回应和商会总管询问拆成两组。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机从贴耳通话到放下、捏在掌心的变化有5-8秒可见过渡。",
      "fix_instruction": "若不通过，应补充挂断和收手机动作。"
    },
    {
      "group": "第10组",
      "type": "filmability",
      "result": "pass",
      "evidence": "海外方向和滚滚乌云通过远处天边乌云的可视画面表达，没有把抽象威胁写成不可见结论。",
      "fix_instruction": "若不通过，应改成可见天气、视线和表情动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
