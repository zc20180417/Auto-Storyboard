{
  "pass": true,
  "summary": "seg01 审核通过。四组均保留原剧本台词和动作，时长在 10-15 秒默认范围内，空间和道具连续。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "原剧本中扫落水果、李少爷台词“废了我的手！我要她全家死！”和保镖台词“少爷，顾家倒了，咱们在省城没人了。”均保留，人物关系未改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组四段分别承载封杀命令、医生诊断和踹倒医生后的怒吼，最长台词“滚！我要让赵朵朵求生不得求死不能！”给 3.5 秒，未超过 6.5 字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "U盘从赵朵朵右手口袋中取出，随后递到赵大雷手中，组尾明确赵大雷握着U盘，道具归属连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组虽然有医生诊断和踹倒医生，但拆成四个时间段，总时长 14 秒，未把多个剧情目标压入同一短段。",
      "fix_instruction": "若不通过，应把医生诊断和踹倒医生后的怒吼拆成相邻独立组。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第3组组首只写办公室内人物位置、退货单归属和桌面状态，没有入场或镜头推进。",
      "fix_instruction": "若不通过，应删除组首中的过程动作，只保留第一帧人物和道具状态。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "赵朵朵三句关键台词“动用京城关系压我？他真当自己手眼通天。”“顾家的账本里，李家拿的分红可不少。”“大哥，把这个直接寄给京城纪委。”均完整保留。",
      "fix_instruction": "若不通过，应恢复被删改的原台词，并通过拆段或拆组承载。"
    }
  ],
  "issues": [],
  "warnings": []
}
