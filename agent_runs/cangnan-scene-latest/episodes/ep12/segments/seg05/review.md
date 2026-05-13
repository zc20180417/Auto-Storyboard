{
  "pass": true,
  "summary": "seg05审核通过，陆凡揭穿假专家、会场反应、假专家逃离和宋子昂对峙均符合原剧本。",
  "checked_groups": ["第13组", "第14组", "第15组", "第16组"],
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
      "group": "第13组",
      "type": "script_fidelity",
      "evidence": "陆凡质疑假证、假专家暴跳、陆凡宣布展示真面目的三句台词均保留。"
    },
    {
      "group": "第14组",
      "type": "prop_continuity",
      "evidence": "遥控器由陆凡手边按下，大屏幕再亮起蓝羽雀资料，道具操作和结果连续。"
    },
    {
      "group": "第16组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂和陆凡两句对峙台词各分配5秒，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第14组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒内只有屏幕亮起、陆凡说明热带雨林、陆凡反问高寒针叶林三个强节拍。",
      "fix_instruction": "如不通过，应把屏幕展示和陆凡逼问拆开。"
    },
    {
      "group": "第15组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第14组尾假专家被问住，第15组首屏幕资料仍在，假专家仍站在桌旁后才露怯逃离。",
      "fix_instruction": "如不通过，应补足屏幕仍亮和假专家位置。"
    },
    {
      "group": "第16组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、自动分镜、视频延长等工程词，保持自然分镜文本。",
      "fix_instruction": "如不通过，应删除污染词并改成可见画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
