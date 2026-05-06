{
  "pass": true,
  "summary": "seg04分镜忠于原剧本，公寓场景空间锁定完整，慢语台词拆分合规，电话与心声处理正确",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "苏清寒前两条条件共17字，剧本标注一字一顿，按慢语4.2字/秒计算约4.0秒，实际分配5秒（5-10秒），节奏合规。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "苏清寒公寓内单一物理空间，朱文浩仅以电话音出现，画面主体始终是苏清寒，无跨场景硬切。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "苏清寒心声'不是信任他，是只有他能帮我复仇'完整保留，以画外音形式呈现，符合原剧本OS标注。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏清寒坐于书桌前，苏晓晓 initially 不在画面内，随后于7-10秒在门口出现，此前已在组首空间锁定中标注门位于画面右侧背景。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾苏晓晓出现在门外，第2组组首苏晓晓跪在苏清寒面前，人物位置连续，有明确的开门→跪地动作衔接。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "苏晓晓泪流满面、跪下、苏清寒按录音键等均为可见可拍细节，情绪通过表情和动作转译，无抽象心理描述。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "节奏",
      "problem": "第5组以3秒无台词背影收尾，虽在3秒上限内，但建议确保窗外夜景有足够视觉信息支撑。",
      "evidence": "7-10秒为远景背影无台词镜头，时长3秒。",
      "fix": "可在远景中增加窗外车流或霓虹闪烁等动态元素，避免画面静止感。"
    }
  ]
}
