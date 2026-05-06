{
  "pass": true,
  "summary": "seg02共4组已复审，破门、对峙、逐客剧情完整，旧 review 中的举杯、门状态和景别硬问题均已清除。",
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
      "evidence": "第1组按剧本写套房大门被推开、闪光灯涌入、朱文浩搂着苏清寒从容举杯，没有写成碰杯。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "王队长、朱文浩的每句开口台词均写明对朱文浩或对王队长说道/问道，未使用无对象的说道。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "evidence": "第4组总时长10秒，时间段为0-2、2-4、4-7、7-10秒，最后时间点等于组标题总时长，镜头数4个一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明酒店行政套房、朱文浩与苏清寒在落地窗前、套房大门正被猛然推开，王队长和安保人员在行动前由门外涌入获得可生成位置。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组到第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以王队长额头冒汗、不敢抬头收尾，第3组组首继续写王队长站在朱文浩面前、额头冒汗，状态连续。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "安保人员收起相机、慌乱退出、房门重新关上均为可见动作，未以抽象'威压'替代画面。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "多句压迫台词语速偏快但可接受",
      "evidence": "第3组4-6秒'拿着薪水，干构陷的脏活。'13字/2秒=6.5字/秒；6-8秒'这身制服你们还想不想穿？'13字/2秒=6.5字/秒。",
      "fix": "可选延长或拆分，但当前未超过7字/秒硬阈值。"
    }
  ]
}
