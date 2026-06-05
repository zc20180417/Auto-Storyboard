{
  "pass": true,
  "summary": "seg03保留授权委托书、周建国代办签名、昏迷住院日期和沈清确认一家合谋的反转，审核通过。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈清强忍眼泪取出银行补充材料、翻到手机号变更代办授权委托书复印件，原剧本关键道具完整保留。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "分镜明确写出日期对应周桂兰两年前重症肺炎昏迷住院期间，代办人签名为周建国，没有改成刘美娟。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "沈清关于一家子合伙吸血的OS写明嘴唇闭合、不做口型；最终台词对着院门方向现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "银行补充材料被沈清取出并翻页，授权委托书复印件始终位于材料最上方，组尾保持手指压住标题。",
      "fix_instruction": "若不通过，应补清文件从材料堆到最上方的可见过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "沈清约24字质问给5秒，字秒比约4.8，情绪台词不过快；前7秒用于签名和日期揭示。",
      "fix_instruction": "若不通过，应延长台词时间或拆分签名揭示和质问。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒包含心声、攥紧回执单、现场怒斥和组尾站位，均围绕同一证据反转，没有新增动作线。",
      "fix_instruction": "若不通过，应删去非剧本动作或拆开心声与现场台词。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模板编号、参考图、模型说明词、字幕或工程占位符，所有信息转译为文件特写、心声和现场台词。",
      "fix_instruction": "若不通过，应删除工程词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
