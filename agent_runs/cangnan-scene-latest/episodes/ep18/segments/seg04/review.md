{
  "pass": true,
  "summary": "seg04 keeps the underground fight-club setup, cash offer, Mad Dog's rule question, Song Ziang's malicious order, and Mad Dog's acceptance with clear space and timing.",
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
      "evidence": "第1组保留八角笼内疯狗踢倒对手、宋子昂扔现金、要求教训一个人、疯狗询问程度。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "第1组组首锁定八角笼、笼外贵宾区、疯狗、拳手对手和宋子昂的位置及朝向，单一室内空间清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-7秒承载宋子昂约30字恶毒台词，字秒比约4.3；10-12秒疯狗短句约9字，均符合节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "现金从宋子昂手中扔到笼边桌面，第2组组首继续位于他身前桌面，道具归属连续。",
      "fix_instruction": "若不通过，应在第1组补充现金落点或第2组组首复述。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "宋子昂要求折磨心爱女人后废掉陆凡、疯狗说有趣并接单的关键台词均保留，没有弱化剧情因果。",
      "fix_instruction": "若不通过，应补回原台词和接单反应。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有字幕、模板、参考图、模型自动等污染词，暴力威胁仅来自原剧本台词。",
      "fix_instruction": "若不通过，应删除工程词并保留原剧本可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
