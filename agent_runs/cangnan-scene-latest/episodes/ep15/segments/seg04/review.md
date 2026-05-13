{
  "pass": true,
  "summary": "seg04保留推土机施工提速、宋子昂败退和陆凡现场压制，主干道空间与动作节奏通过。",
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
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "陆凡驾驶特种推土机、推土铲推平土方、五台推土机一字排开且进度更快的三个动作节点均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-3.5秒宋子昂约17字怒喊，8-10.5秒陆凡约10字回应，10.5-12.5秒宋子昂约6字短句，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部宋子昂在路边看施工加速，第2组组首仍在道路右侧安全线外并看向推土机，位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组只有驾驶启动、推土铲推进、五车排开三个动作节拍，10秒内可表演，没有对白叠加。",
      "fix_instruction": "若不通过，应缩短环境展示或拆施工动作。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡组首在驾驶室内，4-8秒下车后才对宋子昂说话；宋子昂和律师团组首已在道路右侧可用。",
      "fix_instruction": "若不通过，应补充下车动作或人物位置。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "宋子昂“混账！这到底是从哪冒出来的机器！”、“咱们走着瞧！”和陆凡“前方施工，闲杂人等让开。”均按原剧情保留。",
      "fix_instruction": "若不通过，应恢复原台词和离场动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
