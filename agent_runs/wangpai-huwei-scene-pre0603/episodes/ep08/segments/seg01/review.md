{
  "pass": true,
  "summary": "seg01按办公室、黑车、地下车库分开承载，完整保留复制硬盘、秦越监听、车库伏击、顾北辰保护和定位器尾钩，未见阻断交付的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组", "第13组"],
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
      "type": "dialogue_pacing",
      "evidence": "许知夏长句“他们越想抢，说明这东西越有用。我不能把全部筹码押在你一个人身上。”在9-15秒承载，约34字/6秒，约5.7字/秒，未超过6.5硬上限，且有推近防静电袋的必要动作。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏OS“太安静了”被写为画外心声，镜头明确许知夏嘴唇闭合不做口型，且有空车库、灯光滋滋声和后视镜晃动作为可见警觉来源。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "第一名黑衣人的冲来、顾北辰挡开、扣腕、击膝、黑衣人单膝跪地被拆成5个连续时间段，顾北辰始终遮在许知夏前方。"
    },
    {
      "group": "第12组",
      "type": "prop_continuity",
      "evidence": "车底微型定位器先在组首声明仍固定在后方车辆底盘边缘，5.5-8秒给特写，后续第13组再由秦越取下，归属转移清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "顾北辰合电脑、拔硬盘、把硬盘和旧档案装进防静电袋，并保留“今晚不能留在公司。监控、门禁、网络都可能被盯上。”",
      "fix_instruction": "若不通过，应恢复合电脑、拔硬盘、防静电袋和原台词。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏问“去哪？”、“你知道。”，顾北辰解释安全屋和布置来源，均明确对对方说，没有假对象。",
      "fix_instruction": "若不通过，应补足真实对话对象。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "楼下黑车监听单独成组，组首锁定后排陌生男人、前排手下、耳机和车载屏幕，没有与办公室复制画面混在一个现实空间。",
      "fix_instruction": "若不通过，应拆分黑车空间或明确屏幕画面例外。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "三名黑衣人在组首已位于车后阴影里，3-6秒走到灯下后才参与对峙，人物出现路径清楚。",
      "fix_instruction": "若不通过，应在组首补车后阴影位置或增加入场镜头。"
    },
    {
      "group": "第9组-第11组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "打斗被拆为第一名黑衣人、第二名黑衣人、发现车胎、第三名黑衣人、消防通道五段，未把三人打斗和逃跑压入一个15秒片段。",
      "fix_instruction": "若不通过，应继续拆分单个攻击或逃跑节点。"
    },
    {
      "group": "第12组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS“这不像是周振邦的手法”标注为画外心声，画面中顾北辰嘴唇闭合不做口型；随后现场对白“那是谁？”和“看来周振邦后面还有人。”对象明确。",
      "fix_instruction": "若不通过，应将OS改为闭口心声或补现场开口对象。"
    },
    {
      "group": "第13组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第12组尾部顾北辰和许知夏进入消防通道、定位器仍在车底闪红光；第13组组首复述安全门合上、定位器仍在车底，秦越随后取下，连续性成立。",
      "fix_instruction": "若不通过，应在第13组组首补安全门合上和定位器仍在车底。"
    },
    {
      "group": "第1组-第13组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模型说明词、参考模板、工程占位符、调试标记或模板化批量句式。",
      "fix_instruction": "若不通过，应删除污染词并恢复自然分镜正文。"
    },
    {
      "group": "第7组-第13组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "复杂站位和打斗组均有2-4个锚定本组人物、甩棍、车胎、消防通道或定位器的禁止项，未使用泛泛词，且不禁止原剧本必须动作。",
      "fix_instruction": "若不通过，应替换为本组特有风险，删除泛泛或矛盾禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
