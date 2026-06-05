{
  "pass": true,
  "summary": "seg01已按原剧本保留转账成功、赵强强撑否认和短信从周美娟包内响起的证据链，无硬问题。",
  "checked_groups": ["第1组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留沈清“钱已经到账了”、赵强“没……没动静啊。看来你查错了”，并把短信声明确写为从周美娟名牌包内响起。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "沈清6字用2秒，赵强约13字用3秒，字秒比均低于6.5且不拖慢情绪对白。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组只发生在夜晚周家正屋客厅，组首列明沈清、周美娟、赵强、周桂兰、周建国、小雨位置和朝向。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "短信提示音写明来自周美娟怀里的名牌包，现场对白均由画面人物对真实对象说出。",
      "fix_instruction": "无须修复；若改动需继续保持短信声来源为周美娟包内。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "沈清手机显示转账成功，周美娟名牌包被双手压住，包内手机通过短信声被定位。",
      "fix_instruction": "无须修复；不得让短信声改由其他手机发出。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周美娟名牌包、短信声来源、赵强和周桂兰，没有泛泛占位词。",
      "fix_instruction": "无须修复；若新增禁止项须保持2-5条且绑定本组人物或道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
