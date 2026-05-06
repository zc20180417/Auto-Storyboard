{
  "pass": true,
  "summary": "seg03分镜稿无硬性问题，公寓夜戏空间锁定完整，情绪对白时长合理，刀戏与心理击溃段落节奏准确，无可视化缺失。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
  ],
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "7-14秒特写镜头苏清寒逼问台词38字按情绪对白6.0字/秒计算约7秒，实际7秒，处于情绪爆发合理上限。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "朱文浩点破苏清寒母亲换肾、手术费未凑齐等关键台词完整保留，刀掉地上动作保留，无删减或改写。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组组首空间锁定明确写出苏清寒面向镜头眼眶泛红、朱文浩弯腰看向地上水果刀，道具位置与第4组刀掉地上兼容。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏清寒从包中掏刀上前一步抵喉的动作发生在台词之前，朱文浩始终坐在原位，两人在组首或行动前均获得可生成位置。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以苏清寒持刀逼问收尾，第3组以苏清寒持刀抵喉、朱文浩未动开场，道具与人物位置完全一致。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "苏清寒瘫坐、看刀、眼眶泛红、下唇颤抖均为可见动作与表情；心声通过画外音呈现，无抽象心理判断直接当画面。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "单镜头时长7秒，处于警告区间",
      "evidence": "7-14秒镜头苏清寒逼问台词38字/6.0≈7秒",
      "fix": "已处于情绪对白合理上限，建议保留"
    },
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "dialogue_pacing",
      "problem": "单镜头时长7秒，处于警告区间",
      "evidence": "0-7秒镜头朱文浩威胁台词38字/6.0≈7秒",
      "fix": "已处于情绪对白合理上限，建议保留"
    },
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "部分有台词镜头比目标多1秒",
      "evidence": "3-6秒和6-10秒镜头各比目标时长多1秒",
      "fix": "可接受，不影响整体节奏"
    }
  ]
}