{
  "pass": true,
  "summary": "ep07 seg01 已对照原剧本、竖屏 generator 规则和当前分镜审查，关键台词、钥匙、旧档案、加密硬盘、录音与黑车悬念均保留，未发现阻断生产的硬问题。",
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
      "type": "dialogue_pacing",
      "evidence": "许知夏台词“野猫还会撬保险柜呢”约10字给3秒，顾北辰台词约27字给6秒，均低于6.5字/秒，且有指向顾北辰/许知夏。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留许知夏用钥匙打开保险柜、柜内无现金、旧档案和加密硬盘、证据链封面以及两句关于周振邦的关键对白。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "许父录音明确从电脑里传出，许知夏和顾北辰闭口听着，未把许父VO写成现场人物开口。"
    },
    {
      "group": "第7组",
      "type": "format",
      "evidence": "标题使用EP07-G07 cut_id，12秒内5个连续时间段，最后一段结束于12秒，镜头数与时间段数一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "保险柜钥匙从顾北辰外套内袋取出，放到办公桌中央，组尾明确停在桌面，下一组许知夏从桌上拿起钥匙打开保险柜。",
      "fix_instruction": "若不通过，应补充钥匙从顾北辰手中到桌面再到许知夏手中的可见过渡。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "旧照片内容、许知夏判断顾北辰与父亲关系好、顾北辰低声承认许振南帮过他，均与原剧本一致。",
      "fix_instruction": "若不通过，应恢复旧照片与顾北辰旧关系的揭示顺序。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏质问、顾北辰回答“都有”、许知夏要求全部告知、顾北辰提醒危险，均写明对顾北辰或许知夏说道。",
      "fix_instruction": "若不通过，应逐句补足真实对话对象，不得写对空气或对道具说话。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载一次许知夏质问、一次硬盘插入、录音播放、红色入侵提示，15秒内分成5段，强节拍按阶段拆开，没有把拔网线也塞入同组。",
      "fix_instruction": "若不通过，应把硬盘插入、录音播放、入侵提示进一步拆组或移动到下一组。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首继承第6组的硬盘插在电脑、红色入侵提示、许知夏握旧档案；组内顾北辰拔网线后再说定位到硬盘，状态连续。",
      "fix_instruction": "若不通过，应在第6组尾或第7组首补清硬盘、网线和屏幕提示状态。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定顾北辰、旧档案、黑车、陌生男声VO，且针对拔网线、道具、跨空间和口型风险，数量4条未超限。",
      "fix_instruction": "若不通过，应删除泛泛禁止词并替换为本组人物、道具或场景锚点。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明词、参考模板、@图片/@视频/@音频、自动正反打或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明词和非分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
