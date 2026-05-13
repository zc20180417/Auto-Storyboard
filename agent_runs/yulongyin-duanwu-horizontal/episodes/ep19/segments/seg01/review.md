{
  "pass": true,
  "summary": "第1组保留胡永贵目睹鳞片、贪婪自语并爬向落点的原剧本动作，横屏左右关系和道具落点清楚，无硬问题。",
  "checked_groups": [
    "第1组"
  ],
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
      "type": "script_fidelity",
      "evidence": "原剧本的紫雷劈裂缝、青金光被震飞、鳞片脱离水龙坠入泥沙、胡永贵说“那是神仙的宝贝……有了它，我能换回十个厂子！”以及顶雨爬向落点均被保留。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "组首锁定胡永贵在画面左前景泥坑，裂缝和水龙残影在右后方，鳞片坠向右前方泥沙，左到右的追逐视线明确。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "唯一台词放在5.5-9.5秒的4秒镜头内，有效字数约20字，字秒比约5.0，低于6.5硬上限，且标明胡永贵自语。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "鳞片从右后方水龙残影脱离，坠入右前方泥沙，9.5-13秒胡永贵按同一落点爬行，道具位置连续。",
      "fix_instruction": "若不通过，应补足鳞片从脱离到落点再到胡永贵爬向它的可见路径。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "胡永贵是独自趴在泥坑中，台词明确为盯着鳞片方向自语，没有虚构对话对象。",
      "fix_instruction": "若不通过，应把台词改为自语或补充真实在场听话对象。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、官方模板说明、自动分镜或其他模型工程词。",
      "fix_instruction": "若不通过，应删除工程词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
