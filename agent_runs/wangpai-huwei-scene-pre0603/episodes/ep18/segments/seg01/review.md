{
  "pass": true,
  "summary": "ep18 segment已对照原剧本和竖屏规则逐组审查，废仓进入、保险柜证物、林晚身份、秦越包围、混战和大门关闭均按原剧本保留，未发现硬问题。",
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
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏关于三年前现场的内容写为心声且嘴唇闭合不做口型；林元保险柜说明是现场开口并明确对许知夏和顾北辰说。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "钥匙从许知夏内袋取出并打开保险柜，存储卡由保险柜转到许知夏手中，旧照片继续留在柜内，关键道具转移清楚。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "秦越索要证物、许知夏拒绝、两名手下进攻、顾北辰反击、林元踹膝弯分段呈现，没有把多人动作压进同一镜。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "秦越直扑许知夏、顾北辰格挡且旧伤牵动、许知夏捡铁管并击中秦越、顾北辰重拳击中秦越面门均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定废仓外铁门、汽车、手电筒和监控探头，三人位置和朝向完整，后续下车与监控判断都在同一物理空间内完成。",
      "fix_instruction": "若不通过，应补齐林元手电、监控探头或改正人物位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第2组林元最长一句28个有效字分配5秒，约5.6字/秒，低于6.5硬上限；其他台词也已给足时间。",
      "fix_instruction": "若不通过，应延长该句或拆成两段。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾许知夏站到保险柜前，第3组首从保险柜关闭且许知夏在柜前开始；第3组尾存储卡在许知夏手中，第4组首继续复述。",
      "fix_instruction": "若不通过，应补保险柜开关状态和存储卡归属。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越在组首已位于二层栏杆边，手下在仓库四角阴影里可被揭示，后续拍手、台词和六人现身都有可用来源。",
      "fix_instruction": "若不通过，应在组首增加秦越或手下的可见/遮挡位置。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "秦越扑向许知夏、顾北辰格挡、秦越近身压制、许知夏拾铁管、铁管击背和顾北辰重拳分为5段，15秒内动作链清楚。",
      "fix_instruction": "若不通过，应把秦越近身交手或铁管反击拆成独立组。"
    },
    {
      "group": "第7组",
      "type": "timing_math",
      "result": "warning",
      "evidence": "第7组为8秒短组，属于遥控器按下和仓库大门开始关闭的短动作悬念收尾，时间轴连续且镜头数正确。",
      "fix_instruction": "可选优化是与后续逃脱动作合并；当前作为片尾短承接不构成 hard issue。"
    },
    {
      "group": "第5组至第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "关键动作组的视频禁止项均锚定存储卡、林元、顾北辰、秦越、遥控器或仓库大门，数量在2-5个之间，没有泛泛占位项。",
      "fix_instruction": "若不通过，应替换为本组人物、道具或场景锚点。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、参考图占位、模板编号、自动分镜或横屏字段，保持自然竖屏分镜格式。",
      "fix_instruction": "若发现污染词，应删除并改成自然画面语言。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第7组",
      "rule": "timing_math",
      "problem": "第7组为8秒短组。",
      "evidence": "第7组只承载秦越按遥控器和仓库大门开始关闭的短动作悬念收尾，符合短承接例外。",
      "fix": "当前可保留；若后续有下一集连续逃脱动作，也可在跨集规划中接续强化门体关闭状态。"
    }
  ]
}
