{
  "pass": true,
  "summary": "seg01已对照原剧本、横屏生成规则和当前草稿完成审核，未发现阻断交付的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "爸爸固定在画面左侧压近，刀疤男、胡永贵和打手甲在画面右侧形成阵营，泥水涟漪和视线轴线都服务广场对峙。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留刀疤男“大言不惭！给我上！打断他的手脚！”以及打手甲甩棍砸向爸爸面门、爸爸右臂硬挡和甩棍弯折的因果。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "打手甲“这还是人的胳膊吗！太邪门了！”安排在3秒惊恐反应中，随后4秒承载爸爸反手一推，节奏可表演。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刀疤男对爸爸、爸爸对刀疤男、胡永贵对刀疤男的说话对象均在同框或过肩关系内明确可见。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "精钢甩棍从打手甲手中挥出，到砸中爸爸右臂，再在画面中央弯折，归属和动作连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以甩棍弯折和爸爸格挡收尾，第3组从打手甲看弯折甩棍和爸爸右臂开始，衔接自然。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
