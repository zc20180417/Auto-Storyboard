{
  "pass": true,
  "summary": "两组保留小李交代、马行长收回扣和民警带走的证据链，录音与口供道具连续清楚。",
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
      "evidence": "小李和手下甲被控制、陆凡质问偷公章转十个亿、小李承认宋少逼迫及五百万绿卡均与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "录音笔在第1组位于桌面并由陆凡按住，第2组陆凡推近录音笔继续问话，口供记录随后递给民警。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "小李关于三千万回扣和加急汇款的台词约22字用5.5秒承载，约4字/秒，未超速且符合交代口供语气。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡、小李、手下甲、民警均在组首有位置和朝向，小李在说话前可见且被控制。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对小李问话、小李对陆凡交代、陆凡对民警说明、民警对陆凡回应，对象明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为连续审讯收束，问话、交代、递交口供、民警带走分段清楚，总时长15秒内可表演。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、模型说明、参考图占位符或字幕工程词。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
