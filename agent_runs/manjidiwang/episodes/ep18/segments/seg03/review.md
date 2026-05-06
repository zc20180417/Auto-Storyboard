{
  "pass": true,
  "summary": "seg03四组完整保留政策公告反转、坐牢宣判、警车前龙爷线索和朱文浩心声，硬性审核通过。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留苏长明疯魔等待、朱文浩“谁告诉你，那五亿买的是烂尾项目？”、“看看最新的政策公告。”、大屏幕国家级特区公告和苏长明“不可能！这绝不可能！”。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组发生在集团财务中心，警笛只作为窗外声音进入，特勤从财务中心门口进入视线边缘，没有把室外警车空间塞进同组。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组苏长明警车前三句分别用3秒、3秒、4秒承载，最长一句约23个有效字 / 4秒 / 5.8字秒比，符合情绪对白节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“烂账变资产”的信息通过政策公告屏幕、地图标注和朱文浩台词呈现，关键反转可见可听。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定列出苏长明、朱文浩、特勤人员在警车旁的位置、朝向和手铐，后续押送和对话人物均已可用。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾苏长明被推向警车，第4组首警车车门已合上且苏长明在车窗内可见，警车启动离开，过渡连续。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "苏长明“他养我二十年，就是为了让我试探你！”情绪句节奏偏快但可接受。",
      "evidence": "约18个有效字 / 3秒 / 6.0字秒比。",
      "fix": "可保留短剧反派揭底节奏；不影响通过。"
    }
  ]
}
