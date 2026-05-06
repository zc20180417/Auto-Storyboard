{
  "pass": true,
  "summary": "第10集第一段分镜忠于原剧本，对话指向明确，时长计算准确，空间锁定完整，无硬性错误。",
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
      "evidence": "刘海平台词11字按情绪语速6.0字/秒计算为1.83秒，向上取整2秒，叠加推文件动作2秒，总时长4秒，合理；邱瑞台词12字取整2秒；朱天和台词14字取整3秒叠加端起茶杯1秒同步，总时长4秒。三组台词均未被压快或拖慢。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出会审室内刘海平、邱瑞、朱天和、田立民四人位置与朝向，单组仅涉及会审室一个物理空间，无跨场景硬切。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中刘海平'得饶人处且饶人'、朱天和'集团纪律，不容任何人践踏'、田立民'行了，证据确凿，交纪检办'及刘海平瘫坐反应均完整保留，未删减台词或新增剧情动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定已明确列出刘海平、邱瑞、朱天和、田立民四人的画面位置与身体朝向，所有说话人物均在组首拥有可生成位置。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱天和放下茶杯视线锁定刘海平；第2组组首仍位于同一会审室，四人位置与上一组兼容，文件仍在桌上，茶杯状态连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'气氛压抑'已转译为会审室肃杀环境、冷光、人物推文件等可见元素；'面如死灰'转译为刘海平瘫坐、视线失焦的具体表情动作。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "无台词镜头",
      "problem": "刘海平瘫坐反应镜头3秒，虽在3秒上限内，但建议控制在2秒以保持短剧快节奏。",
      "evidence": "7-10秒：近景，刘海平浑身一软，瘫坐在椅子上，面如死灰，视线失焦。",
      "fix": "可考虑压缩至2秒，将多余1秒分配给田立民敲桌动作。"
    }
  ]
}
