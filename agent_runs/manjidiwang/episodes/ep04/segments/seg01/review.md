{
  "pass": true,
  "summary": " seg01分镜忠于原剧本，时长、对话指向、空间锁定均符合规则",
  "checked_groups": ["第1组", "第2组", "第3组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "周正明发问与朱文浩三连答共37字，按普通对白5.2字/秒计算朗读约7.1秒，加换人间隙0.5秒、邱瑞点头0.5秒，总目标约9秒，实际分配9秒（2-11秒），节奏合理。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "本组保持集团特招考场单一物理空间，朱文浩、考官甲、另外三名考官均在组首空间锁定中有明确位置和朝向，无跨场景硬切。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "周正明'你们这是明目张胆压分'、朱文浩'利益面前，规则只是废纸''但废纸，也能包住火'及推开椅子离场等关键台词与动作均完整保留，无删减。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩坐于中央椅子、周正明立于前方、邱瑞位于左侧角落，三人均在组首空间锁定中有明确画面位置与身体朝向。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱文浩答题完毕视线锁定周正明，第2组组首朱文浩仍端坐中央，考官甲在其右前方，人物位置与道具状态连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "朱文浩起身、冷眼、推开椅子离场等动作均为可见可拍细节，无抽象心理描述或气味等不可视信息。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "光影",
      "problem": "三组均使用'前侧光从左侧45度照来'，光影模板化倾向明显，建议后续根据场景灵活调整。",
      "evidence": "第1组、第2组、第3组光影描述中多次出现'前侧光从左侧45度照来'或类似表述。",
      "fix": "建议在考场场景中尝试顶光配合环境反光、侧逆光等不同组合，避免重复。"
    }
  ]
}
