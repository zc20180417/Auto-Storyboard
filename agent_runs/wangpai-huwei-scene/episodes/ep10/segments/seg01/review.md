{
  "pass": true,
  "summary": "第10集seg01覆盖周振邦电话、安全屋决策、定位针袭击、威胁视频和两人设局，分镜格式、忠实度、台词节奏与空间连续性通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "type": "audio_mouth_sync",
      "evidence": "陌生男声明确来自手机听筒，周振邦现场开口只对电话那端说话，未把秦越写成办公室现场人物。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "扑倒、两人摔地、玻璃碎裂探针入墙、许知夏发问分为4个时间段，顾北辰保护站位明确挡在许知夏和窗户之间。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周振邦要求明早九点盛远会议室、一个人来、带硬盘的台词在11.5-15秒承载，有效字数21、时长3.5秒，字秒比约6.0，未超过6.5硬上限。"
    },
    {
      "group": "第8组至第9组",
      "type": "script_fidelity",
      "evidence": "保留许知夏指出周振邦目的就是拆开两人、硬盘不是换人质筹码、顾北辰OS三年前搭档为救他牺牲，以及许知夏提出一起设局的关键因果。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组至第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部红点移向许知夏肩头且顾北辰准备扑向她，第4组组首继承红点位置和两人站位，随后执行扑倒动作。",
      "fix_instruction": "若不通过，应在第3组尾或第4组组首补红点、许知夏位置和顾北辰准备动作。"
    },
    {
      "group": "第5组至第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "定位针被顾北辰拔下并收进口袋，手机视频播放后中断，硬盘在第7组从电脑侧边拔下并转入顾北辰手中，关键道具转移可见。",
      "fix_instruction": "若不通过，应补拔探针、收手机或拿硬盘的可见过渡。"
    },
    {
      "group": "第5组至第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "现实空间保持城西安全屋，周振邦、搭档母亲只出现在手机视频画面或视频声音中；楼道属于手机画面，不与安全屋混成同一现实空间。",
      "fix_instruction": "若不通过，应明确手机视频画面或另起屏幕画面标识。"
    },
    {
      "group": "第7组至第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "视频中断后的分析、顾北辰拿硬盘决定独去、许知夏阻拦、硬盘用途争执、OS与设局被拆成三组，未把外部威胁、拿硬盘、争吵和情绪转折压进单组。",
      "fix_instruction": "若不通过，应继续拆分顾北辰拿硬盘、许知夏阻拦和设局决定。"
    },
    {
      "group": "第3组至第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "复杂动作、探针、手机视频、硬盘转移和保护站位组均提供2-3条锚定人物或道具的本组特有禁止项，没有泛泛模板词。",
      "fix_instruction": "若不通过，应删除无锚点禁止项，改为红点、探针、硬盘、顾北辰、许知夏等本组锚点。"
    },
    {
      "group": "第1组至第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文未出现模板编号、参考图、模型说明、自动分镜、JSON、调试标记或批量模板化描述。",
      "fix_instruction": "若不通过，应删除工程说明词和模板化描述，只保留自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
