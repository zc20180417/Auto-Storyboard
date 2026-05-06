{
  "pass": true,
  "summary": "seg01两组完整保留转账、复核、授权、进度冻结和苏长明怒吼，空间与时长符合生成规则。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组依次保留财务总监“总裁，五亿资金已集结。”、“汇往海外户头，需要董事长复核。”以及苏长明“我有董事长授权，直接打。”，未新增关键剧情。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组主体仍在集团财务中心，只有大屏幕作为屏幕画面展示转账进程和“权限冻结”，未把人物硬切到新物理空间。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组苏长明心声约10个有效字用2秒承载，怒吼“怎么回事！谁干的！”约8个有效字用2秒承载，短台词节奏符合规则。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定列出苏长明位于画面中央、财务总监位于画面右侧，并写明二人朝向、操作台和大屏幕位置，后续说话人物均可用。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾财务总监手指停在确认键上方，第2组组首继续写财务总监手仍停在操作台旁，苏长明和财务总监仍盯向大屏幕，状态连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“转账进程90%……95%……”和“权限冻结”都转译为大屏幕可读画面，苏长明心声按心声格式处理，可听信息来源明确。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
