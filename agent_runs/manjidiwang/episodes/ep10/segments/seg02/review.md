{
  "pass": true,
  "summary": "第10集第二段分镜基本忠于原剧本，时长与空间锁定合格，第2组存在同角色相邻镜头景别重复，建议修正。",
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
      "type": "dialogue_pacing",
      "evidence": "刘海平台词12字按情绪语速6.0字/秒取整2秒，叠加抓住手臂动作同步完成，总时长2秒合理；苏长明台词13字取整3秒叠加推开动作同步；14字台词取整3秒。三段对话节奏紧凑，未拖慢。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出走廊内刘海平与苏长明位置，单组仅涉及走廊一个物理空间；第1组与第2组均位于同一会审室走廊，空间连续。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中'你过河拆桥'、'是你侄女太蠢'、OS独白及电话指令均完整保留；OS以画外音形式呈现，电话以明确说话对象呈现，未删减或改写。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定已列出刘海平与苏长明的画面位置与身体朝向，两人均在组首拥有可生成位置。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为苏长明侧身站立斜睨刘海平；第2组组首两人仍在同一走廊，位置与状态自然衔接。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'失魂落魄'转译为走出姿态与眼神失焦；'冷漠'转译为推开动作与视线避开；'阴毒'转译为侧脸眼神与阴冷画外音。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "景别切换",
      "problem": "苏长明在2-5秒与5-10秒连续作为相邻镜头主要主体，且两镜均为中景，缺乏景别、构图或机位差异，易造成视觉跳帧。",
      "evidence": "2-5秒：中景，苏长明整理西装...；5-10秒：中景，苏长明转身大步离去...",
      "fix": "将2-5秒或5-10秒其中之一改为近景/全景，使同角色相邻镜头形成景别差异。"
    }
  ]
}
