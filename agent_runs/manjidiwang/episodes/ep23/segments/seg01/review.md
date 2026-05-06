{
  "pass": true,
  "summary": "seg01共5组已对照办公室剧本、生成规则和分镜正文审核；台词、旧协议动作、窗边OS及空间锁定均保留，无硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组"
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留砸碎古董花瓶、田立民咬牙台词、李长庚担心孙总乱咬、田立民以家人威胁并启动毒丸计划的全部剧情点。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组0-3秒承载'朱天和当年进集团，签过一份对赌'，3-10秒承载长句协议触发条款并配合翻文件动作，未超过8秒单台词硬门槛。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组始终位于集团董事长办公室，窗外朱家车辆作为窗边可见对象出现，不切入第二个实体场景。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "田立民和李长庚均在组首空间锁定中有明确画面位置、身体朝向和视线关系。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组到第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以田立民取出旧协议收尾，第3组开头继续由田立民手捧旧协议说明对赌，关键道具归属连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "田立民OS通过俯拍朱家车、旧协议贴在胸前和窗边剪影承载，卖身契信息以台词和可见文件共同呈现。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "短促惊呼语速略快但可接受",
      "evidence": "第2组0-2秒'那可是杀敌一千自损八百啊'约13字/2秒=6.5字/秒，属于情绪惊呼的可接受偏快节奏。",
      "fix": "如需更稳，可与后续冷笑镜头重分配为3秒。"
    }
  ]
}
