{
  "pass": true,
  "summary": "seg02保留廉价止痛片、周桂兰落泪、杂物间照片和黑棉被质问，未发现硬问题。",
  "checked_groups": [
    "第3组",
    "第4组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "廉价止痛片空盒、沈清两句愤怒台词、周桂兰落泪台词、周美娟没来得及买好药的狡辩均按原顺序保留。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "沈清先放下药盒，再从西装口袋取出手机点开杂物间照片，手机屏幕持续到组尾，关键道具转移清楚。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "7.5-11秒质问约13字用3.5秒，约3.7字/秒，符合冷厉质问；11-13秒周美娟约9字用2秒，约4.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组首继承第2组药盒袋摊开后的状态，空盒散在桌面和地面，不存在道具跳变。",
      "fix_instruction": "若不通过，应在上一组尾或本组首补充空药盒散落位置。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第4组按放下药盒、取手机、展示照片、质问、周美娟语塞分段，每段一个主动作或一句对白。",
      "fix_instruction": "若不通过，应拆开取手机和举手机质问动作。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、模型说明词或官方占位符，手机照片被写成剧情内屏幕画面。",
      "fix_instruction": "若不通过，应删除工程词并改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
