{
  "pass": true,
  "summary": "seg04已核对鱼干直播秒空、村民装车和保存打斗录屏，销售转折与证据动作完整。",
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
      "evidence": "周思思推销鱼干、一万单秒空、牛大春确认、陆凡安排装车四个剧情点全部保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "7-15秒将一万单秒空、牛大春确认和陆凡安排装车拆成3个时间段，单段字秒比均低于6.5。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "周思思手中手机从直播销售延续到保存打斗录屏，纸箱从堆放到村民搬运有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡、周思思、牛大春和村民们均在组首有位置，纸箱和鱼干也已锁定。",
      "fix_instruction": "若人物缺失，应在组首补位置、朝向和道具状态。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡安排装车，第2组组首村民们围在纸箱周围并开始搬运，行动承接自然。",
      "fix_instruction": "若不连续，应在第1组尾或第2组开头补装车开始动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对周思思说道保存录屏，周思思对陆凡回应铁证，对象明确。",
      "fix_instruction": "若缺对象，应补为A对B说道。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "鱼干销售按短剧现场直播处理，没有广告模板编号、参考图或工程说明。",
      "fix_instruction": "若出现模板污染，应改为人物动作和现场道具描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
