{
  "pass": true,
  "summary": "seg05工地两组保留夜间抢修、黑影埋炸药、引线燃起和陆凡示警卧倒的悬念动作链。",
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
      "type": "space_locking",
      "evidence": "水头村修路工地、路基、探照灯、推土机、涵管、树林边缘都在组首锁定，两个黑影在远处暗处具备后续靠近条件。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留黑影塞炸药、打火机点燃引线、陆凡发现火星并喊出‘谁在那边’和‘有炸药！全员卧倒！’。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡5字质问用2.5秒，11字示警用3秒并伴随村民卧倒动作，没有字秒比过快或拖慢。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为工地环境、陆凡指挥、村民施工、黑影靠近四个清晰节拍，14秒内动作链完整。",
      "fix_instruction": "若不通过，应拆分施工指挥和黑影靠近。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "炸药和引线在组首位于桥洞旁，黑影塞入桥洞后用打火机点燃，引线火星继续缩短，道具归属和状态连续。",
      "fix_instruction": "若不通过，应补充炸药从黑影手边进入桥洞的可见动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对暗处大喊‘谁在那边’，随后面向施工区村民喊‘有炸药！全员卧倒！’，对象和声音来源明确。",
      "fix_instruction": "若不通过，应明确陆凡喊话对象为暗处或村民。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾黑影靠近路基阴影，第2组首黑影已在桥洞旁暗处，陆凡和村民仍在施工区，连续合理。",
      "fix_instruction": "若不通过，应在第1组尾或第2组首补黑影到桥洞旁的位置过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
