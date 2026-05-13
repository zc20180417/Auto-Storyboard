{
  "pass": true,
  "summary": "seg04保留陆凡电话下令、周长海来电变脸和秘书电话告知破产的完整爽点，电话音口型分离正确。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "陆凡嘲弄、取出加密手机、拨通商会金融中心专线并下达A级商业狙击命令，关键道具和台词均保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组组首写明周长海自己的手机在外衣口袋内，3-6秒震动亮屏，6-10秒摸出接听，道具可操作状态连续。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "秘书只以周长海手机里的电话声音出现，两段秘书台词均写明电话音，周长海嘴唇闭合不做口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "陆凡命令台词约24字安排在7-14秒，含持手机下令动作，约3.4字/秒略稳但有拨号后正式命令状态支撑。",
      "fix_instruction": "若不通过，应压缩持手机动作或拆成反应镜头承载。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡完成电话命令，周长海跪地看他；第2组首保持同一位置并补充周长海手机在口袋内。",
      "fix_instruction": "若不通过，应在第2组首复述陆凡和周长海位置。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "秘书第一句约34字安排6秒约5.7字/秒，第二句约15字安排4秒约3.8字/秒，电话崩溃语速和反应时长可表演。",
      "fix_instruction": "若不通过，应拆电话音或调整周长海反应时长。"
    }
  ],
  "issues": [],
  "warnings": []
}
