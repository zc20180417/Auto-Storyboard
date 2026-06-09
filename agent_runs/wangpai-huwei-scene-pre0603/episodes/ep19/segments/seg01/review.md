{
  "pass": true,
  "summary": "seg01 已按原剧本完成仓储站逃脱、秦越电话、安全屋解密和赵明海语音七组分镜，未发现阻断交付的 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
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
      "evidence": "林元指暗门、顾北辰拉许知夏、林元踹门、秦越喊追被拆成四个连续时间段，没有把发现暗门、冲刺、踹门和追击压在同一镜。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "许父只以电脑音频出现，分镜明确许知夏嘴唇闭合不做口型，声音来源是电脑扬声器。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "赵明海语音约49字分配8秒，约6.1字/秒，属于慌乱求救语音但未超过6.5字/秒硬上限；顾北辰短句2秒完成。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾暗门打开、三人在门边，第2组组首改到仓储站外巷道，第一镜写顾北辰和许知夏钻出暗门，空间切换有动作过渡。",
      "fix_instruction": "若不通过，应补足从仓库内到巷道外的钻出动作，或拆分旧车启动。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留秦越站在暗门口、拨通电话并对周振邦说“你最后一点价值到了”的关键剧情，没有新增抓住三人的动作。",
      "fix_instruction": "若不通过，应恢复秦越电话对象和原台词，并删除新增追上逃跑者的剧情。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "硬盘、存储卡和录音笔都在桌面保持可见，顾北辰解释证据链，林元说明录音笔原始声纹，许知夏再判断护身符。",
      "fix_instruction": "若不通过，应补清硬盘、存储卡、录音笔分别位于何处以及谁在看它们。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵明海通过手机语音出现，许知夏嘴唇闭合不做口型，手机扬声器是可见载体。赵明海未被写成现场人物。",
      "fix_instruction": "若不通过，应改成手机语音来源，删除赵明海现场开口。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏对顾北辰、林元对许知夏、许知夏对林元的对白对象清楚，台词顺序与原剧本一致。",
      "fix_instruction": "若不通过，应逐句补足真实对白对象并恢复原剧本台词顺序。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜未出现模型说明词、模板编号、参考图、官方占位符或批量模板化描述，均为自然画面语言。",
      "fix_instruction": "若不通过，应删除工程说明词，改写成可见动作、道具和声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
