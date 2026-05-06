{
  "pass": true,
  "summary": "seg01两组已对照集团大堂剧本逐项审核，台词、押送动作、空间锁定和格式均无硬性问题。",
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
      "evidence": "龙建秋“叛徒！一群叛徒！”为2秒短情绪台词，朱文浩“星辰公司已全面接盘鼎丰的债务。”16字/3秒约5.3字秒比，“现在，龙爷可以安心上路了。”11字/2秒约5.5字秒比，均未拖慢或过快。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留特勤将歇斯底里的龙建秋拖上警车、苏清寒收起文件说“城南项目，彻底干净了。”、朱文浩点头说“去医院。”，未新增会改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "场景限定为集团一楼大堂出口区域，组首说明玻璃门外可见警车和打开车门，押送动作在同一出口区域连续完成，没有把不相关空间硬塞同组。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "龙建秋、朱文浩、苏清寒均在组首空间锁定中有明确画面位置、身体朝向、道具或视线关系，后续台词和反应都有可生成来源。",
      "fix_instruction": "无需修复；若后续加入特勤则需在其行动前补足可见位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾朱文浩面向出口、龙建秋伏地；第2组组首龙建秋被特勤架起，朱文浩站在出口方向，押送状态承接自然。",
      "fix_instruction": "无需修复；若改为车内镜头，应补充从门内到车门的连续押送动作。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "败局和愤怒通过血迹、跪伏、俯视、转身、文件握紧等可见动作表现，没有把抽象心理判断当作画面主体。",
      "fix_instruction": "无需修复；保持用可见动作和台词承载情绪。"
    }
  ],
  "issues": [],
  "warnings": []
}
