{
  "pass": true,
  "summary": "seg02完整呈现数据自毁、硬盘破坏、陆凡云盘备份反转和证据链闭合，未发现硬问题。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "张强“没证据能定我的罪？我明天就去市里告你们！”约19字分配5.5秒，约3.45字/秒但带向前探身和嚣张表演，未构成硬拖慢。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "陆凡手机先在组首衣袋内，8-10.5秒掏出并点开递给纪委干部，10.5-15秒承载云盘备份台词。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "张强问“你……你什么时候拍的？”，陆凡答“昨天去敬老院，第一件事就是拍照留痕。”，纪委干部下令“证据链闭合。带走！”均保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含键盘检查、密码错误揭示和张强两句挑衅，四个时间段总计13秒，动作与对白分配清楚。",
      "fix_instruction": "若不通过，应拆出张强长挑衅或压缩非关键表情。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "纪委干部、陆凡对白均明确对张强或纪委干部说，手机备份作为道具展示而非假对白对象。",
      "fix_instruction": "若不通过，应补明说话对象或改掉假对象对白。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾陆凡递出手机、张强笑容僵住；第3组首延续为手机在纪委干部手边、张强笑容僵硬双腿发软。",
      "fix_instruction": "若不通过，应在第3组首复述手机归属和张强状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
