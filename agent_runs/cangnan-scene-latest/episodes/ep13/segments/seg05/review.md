{
  "pass": true,
  "summary": "seg05 两组保留宋子昂砸屏泄愤、刀疤出主意、五百万堵门和威胁工地的剧情。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "保留新闻屏幕、宋子昂抓威士忌酒瓶砸液晶屏、咆哮废物、刀疤擦铁棍并提出黑道手段。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "evidence": "现金先位于宋子昂手边，0-3.5秒被砸到茶几，8-12秒由刀疤收起，归属变化可见。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂两句威胁分别约15字/3.5秒和22字/4.5秒，刀疤约20字/4秒，均未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为新闻刺激、砸屏、咆哮、刀疤出主意四个连续节拍，13秒内动作和对白可表演。",
      "fix_instruction": "若不通过，应把刀疤出主意拆到下一组。"
    },
    {
      "group": "第10组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂两句均对刀疤说，刀疤回应也对宋子昂说，没有缺失对白对象。",
      "fix_instruction": "若不通过，应补全每句现场对白的对象。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、字幕、模板编号、参考图或视频延长等污染内容。",
      "fix_instruction": "若不通过，应删除工程词并改写成自然短剧画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
