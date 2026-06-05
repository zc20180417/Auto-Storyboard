{
  "pass": true,
  "summary": "seg02 保留警税人员入场、实名举报证据、赵强被调查和周美娟一并带走的剧情，未发现 hard issue。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "evidence": "外部事件进入分成酒店经理让路、警税人员入场、带队警察问法人、赵强反应三个阶段，未压进单一时间段。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "警察对赵强的调查台词约25字用4秒，约6.25字/秒；对周美娟的罪名台词约23字用4秒，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留赵强瘫软在地并说完了全完了，保留周美娟涉嫌盗窃和非法侵占他人巨额财产一并带走。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "带队警察、税务局人员在组首位于门口外侧走廊方向，入场后才发问；赵强和周美娟已在厅内可用。",
      "fix_instruction": "若不通过，应把入场人物放在门口可见位置，或将其入场动作提前到说话前。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾写赵强位于右侧椅边、周美娟在其身旁，第2组组首继承同一位置并让赵强扶着椅背。",
      "fix_instruction": "若不通过，应在上一组组尾或本组组首补足赵强与周美娟位置。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为现场人物开口，分别写明带队警察对赵强、赵强发虚自语、带队警察对周美娟。",
      "fix_instruction": "若不通过，应补清现场对白对象或改成画外音来源。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载外部入场和一次法人询问，赵强反应为轻反应，10秒容量足够。",
      "fix_instruction": "若不通过，应拆出入场或压缩非关键反应。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "未出现参考图、模板编号、自动分镜或广告/MV式说明，均为自然分镜正文。",
      "fix_instruction": "若不通过，应删除工程词和模板词。"
    }
  ],
  "issues": [],
  "warnings": []
}
