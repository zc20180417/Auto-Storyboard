{
  "pass": true,
  "summary": "seg04 正确处理陆凡与屏幕中龙天傲的视频对话，手机来源、屏幕人物和现场口型区分清楚。",
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
      "type": "audio_mouth_sync",
      "evidence": "龙天傲通过手机屏幕和扬声器出现，陆凡为现场开口，声音来源与画面载体明确。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留加密铃声、屏幕出现白色西装金丝眼镜青年、龙天傲不高兴和陆凡回应稀土不可染指。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-4秒承载龙天傲约20字，4-8秒承载约18字，8-11秒承载陆凡约15字，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首复述陆凡持有正在通话手机，屏幕中可见龙天傲，两个说话主体都有明确可见载体。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡在组首位于工地中央持手机，龙天傲在2-5秒由屏幕接通后出现，开口前已通过屏幕可用。",
      "fix_instruction": "若不通过，应在龙天傲说话前补屏幕接通和可见画面。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "龙天傲两句威胁、陆凡回应和龙天傲已到苍南的收尾拆为4段共14秒，隔屏对峙节奏清楚。",
      "fix_instruction": "若不通过，应拆出最后一句威胁或压缩非关键屏幕反应。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾陆凡举手机与屏幕中龙天傲对峙，第2组首延续正在通话的手机和屏幕人物。",
      "fix_instruction": "若不通过，应在第2组组首补手机通话持续状态。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现自动分镜、模板编号、参考图、字幕或模型说明词。",
      "fix_instruction": "若不通过，应删除工程词并改写为自然画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
