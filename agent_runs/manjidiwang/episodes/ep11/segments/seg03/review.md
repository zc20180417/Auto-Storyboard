{
  "pass": true,
  "summary": "seg03 current final.txt 复审通过：第2组U盘拾取镜头已为2秒，4组均无硬性节奏、忠实度、空间或格式问题。",
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
      "evidence": "第1组依次保留暴雨手电、越野车完全变形冒黑烟、王队长急喊车头变形、朱文浩冲向残骸扯开车门、苏清寒满脸是血昏迷等原剧本信息。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组12-14秒为朱文浩弯腰捡起带血U盘并攥紧的无台词特写，共2秒；旧 review 指出的12-13秒1秒独立时间段已不存在。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "evidence": "第4组朱文浩对昏迷的苏清寒低声说“她赌的是我的局，我不能让她输。”，画外音标注对苏清寒/内心继续说道，最后明确对王队长喊“通知内卫部，全城搜捕黑皮！”。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首写明朱文浩位于画面左侧、王队长位于画面右侧、救援队在背景、苏清寒在变形车内，所有后续动作与台词人物都有可生成位置来源。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第2组限定在山崖底部泥泞地面，朱文浩抱出苏清寒、触碰紧攥的手、掰开手指、U盘滑落、捡起U盘均发生在同一物理空间。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以朱文浩攥紧U盘结束，第3组从他转身要走时苏清寒抓住袖口开始，人物位置和动作自然承接，没有突然改变道具或人物状态。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "第4组用低头、下颌绷紧、直起身望向夜空、苏清寒昏迷特写、朱文浩猛然转头锁定王队长等可见动作承载情绪与命令，没有不可视抽象信息单独驱动画面。",
      "fix_instruction": "通过，无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
