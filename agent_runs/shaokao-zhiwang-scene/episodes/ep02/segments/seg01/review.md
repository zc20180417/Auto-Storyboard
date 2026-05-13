{
  "pass": true,
  "summary": "seg01 已对照原剧本和竖屏生成规则审核，8 个分镜组保留医院缴费、母子对话、老店对峙和被逐出门的关键台词与动作，无 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "医生对许安说“这点钱只够先压着，后面检查和用药还得补”分配 4.5 秒，约 23 个有效字，字秒比约 5.1；许安追问和医生答复共约 13 字分配 3 秒，快速问答节奏可承载。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本中“一万”“他当着伙计的面甩给我的”“你跟他签过字吗”“没有”“那分红呢”“只有口头话”“我只管后厨。账他从不让我碰”均按顺序保留，人物关系和账目无凭的因果未改写。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组只发生在老店后厨，组首写明许安在后厨门门槛处、韩彪在收钱桌旁、阿顺在烤炉前、马会在备料台附近，人物在说话和行动前均可用。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "后厨钥匙从韩彪衣兜中掏出、在许安眼前展示、再收回衣兜，随后韩彪宣布许安不用进后厨，道具归属和动作过渡清楚。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "evidence": "韩彪最后一句被写成门内高声传出，画面主体许安明确嘴唇闭合不做口型，门板震动提供声音载体，未把门内音误写成许安现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "缴费、票据打印、余额单推回、医生说明费用不足和医生离开的剧情节点均保留，未新增改变剧情的医疗动作。",
      "fix_instruction": "若不通过，应恢复医生费用台词、余额单和医生离开三个关键节点。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩秀兰、许安的所有现场对白均写成对对方说道或问道，母亲拉袖口、许安蹲下承载原剧本动作，未出现假对白对象。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对话对象，并删除假对象表达。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组 15 秒内承载许安入门、韩彪问话、许安要算账和韩彪反击四个连贯节拍，动作集中在同一后厨空间，没有叠加额外道具操作。",
      "fix_instruction": "若不通过，应拆出入门或韩彪反击，避免同组过载。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾部韩彪收钥匙、许安看向阿顺；第7组组首继续写韩彪钥匙在衣兜、许安在门内、阿顺在烤炉前，状态连续。",
      "fix_instruction": "若不通过，应在第6组组尾或第7组组首补充钥匙归属和人物位置。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜未出现模板编号、官方模板说明、参考图、首尾帧、自动正反打、Seedance 自动等工程或模型说明词；负面词仅保留尾部约束。",
      "fix_instruction": "若不通过，应删除模型说明词和模板污染内容，改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
