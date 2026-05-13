{
  "pass": true,
  "summary": "seg02 三组保留带水回来、清水唤醒和黑水灼伤，水壶姿态、壶盖来源、黑水克制度和横屏左右危险关系均可通过。",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组", "第3组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "prop_continuity": "checked",
    "physical_continuity": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "第1组 1-2 明确天天拧开壶盖并放在左膝旁，组尾继续保留壶盖位置，后续壶盖不会凭空出现。"
    },
    {
      "group": "第2组",
      "type": "special_effects",
      "evidence": "第2组青蓝微光从裂缝内弱亮，小龙为半透明清水质感，没有科幻激光、怪物化或卡通萌宠化。"
    },
    {
      "group": "第3组",
      "type": "physical_continuity",
      "evidence": "第3组 3-4 写清水壶底部抵住土坎、双手托住、斜立、口沿高于水面，避免有水容器平放仍不漏的物理问题。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天朝裂缝喊话，是对裂缝深处的小龙呼救方向，非对空气或道具假对象。",
      "fix_instruction": "若不通过，应写明喊话对象为裂缝深处的小龙或声音方向，不得写对空气说道。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第2组保留滴入清水、青蓝光亮起、小龙探头和天天惊喜台词，剧情因果完整。",
      "fix_instruction": "若不通过，应恢复清水滴入到小龙探头的因果链和原台词。"
    },
    {
      "group": "第3组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "黑水表现为油亮、灰白尾尖和极淡薄雾，没有写成爆炸毒液、夸张腐蚀或恐怖血腥。",
      "fix_instruction": "若不通过，应把黑水改为真实克制的渗染、油亮反光和灰白痕迹。"
    }
  ],
  "issues": [],
  "warnings": []
}
