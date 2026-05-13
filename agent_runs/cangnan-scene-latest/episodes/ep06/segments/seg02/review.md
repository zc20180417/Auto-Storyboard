{
  "pass": true,
  "summary": "seg02已核对路障直播、黄毛冲击和陆凡挡棍动作，关键台词与动作顺序保留完整。",
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
      "evidence": "周思思拍路障、弹幕滚动、黄毛发现并冲过来的顺序与原剧本一致，扑克和路障均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "黄毛“把手机给我砸了！”约8字给3秒，周思思“啊！救命！”约4字给2秒，陆凡“继续直播！录下他们！”约10字给5秒并包含推开黄毛动作，口型容量充足。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "组首黄毛手中持有棒球棍，5-9秒棒球棍砸向周思思并被陆凡右臂格挡，道具状态清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "路障、黄毛一伙、周思思和陆凡均锁定在水头村土路，没有跨场景。",
      "fix_instruction": "若不通过，应拆出新物理空间或补足组首空间位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组集中表现挥棍、周思思尖叫、陆凡挡棍和推开黄毛四个连续动作，14秒内有完整动作链，不额外塞入新剧情。",
      "fix_instruction": "若动作过载，应拆分为攻击与反推两组。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部混混冲来，第2组组首延续为混混到道路中段、陆凡站在周思思左后侧准备拦截。",
      "fix_instruction": "若不连续，应补黄毛靠近和陆凡站位过渡。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "没有出现模型说明、模板编号、参考图或自动分镜等污染词。",
      "fix_instruction": "若出现污染词，应删除并改为现场可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
