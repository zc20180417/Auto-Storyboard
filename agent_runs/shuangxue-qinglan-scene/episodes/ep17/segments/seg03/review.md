{
  "pass": true,
  "summary": "seg03 已完成真实审核，周美娟赖账、沈清按110、刑责威胁、赵强求饶和扑抢手机均按原剧本顺序保留。",
  "checked_groups": ["第6组", "第7组", "第8组"],
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
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "红色房产证复印件由沈清左手压住，手机在7-13秒被取出并按下110，组尾同时说明两件道具归属。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "沈清约19字刑责台词给6秒，赵强约12字求饶给5.5秒，均符合字秒比硬上限且情绪不拖慢。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "evidence": "第8组只承载赵强绕茶几扑向手机和伸手未抢到两个连续动作，8秒短动作余波成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留周美娟“钱都花光了”、沈清“父债子偿”和按下110三个数字的关键动作。",
      "fix_instruction": "若遗漏，应补回对应台词或手机拨号动作。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟、沈清、赵强均为画面内现场开口，且标明各自对沈清或对周美娟和赵强说道。",
      "fix_instruction": "若对象不明，应补具体听话人。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "短组理由是赵强扑抢手机这一单一动作余波，没有靠停顿或表情凑时长。",
      "fix_instruction": "若加入额外台词或抢夺成功，应拆组并恢复手机未被抢走。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定赵强、沈清、手机、红色房产证复印件和周家正屋客厅，3条均为本组具体风险。",
      "fix_instruction": "若禁止项泛化，应改为本组手机抢夺和复印件归属风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
