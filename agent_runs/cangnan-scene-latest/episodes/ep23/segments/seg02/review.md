{
  "pass": true,
  "summary": "seg02 保留周长海摔壶、金矿动机和联系血狼安保团的命令，书房空间与道具连续。",
  "checked_groups": ["第4组", "第5组"],
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "周长海摔碎紫砂壶、追问吴大有折了、管家提到商会警告和周长海强调千亿金矿均按剧本保留。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "“伪装成地质勘探队，今晚直接把矿洞给我炸开！”约23字分配6秒并包含拿起电话动作，节奏不过快。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "第4组尾周长海盯向电话，第5组首右手靠近电话，随后拿起听筒下令，电话归属和操作过渡清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组始终在豪华别墅书房内，周长海和管家的位置、朝向、紫砂壶和电话位置清楚。",
      "fix_instruction": "若不通过，应补充书桌、电话、人物站位和朝向。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "摔壶、两段问答、金矿动机共四个节拍，15秒内容量可承载。",
      "fix_instruction": "若过载，应把摔壶与金矿台词拆成两组。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "管家对周长海提问，周长海对管家下令，均为现场真实开口对白。",
      "fix_instruction": "若不通过，应补齐说话对象。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、自动分镜、视频延长等工程词或模板污染。",
      "fix_instruction": "若出现污染，应删除工程说明并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
