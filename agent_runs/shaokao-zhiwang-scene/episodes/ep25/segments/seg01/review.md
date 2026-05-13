{
  "pass": true,
  "summary": "已对照第25集原剧本、竖屏生成规则和seg01草稿逐组审核，台词、人物关系、道具归属、空间衔接和时间轴均可交付；第11组为片尾意象短组，保留软提醒。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组",
    "第10组",
    "第11组"
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本中林小满以“经营时间短，不代表口碑短。聚餐救场、街坊回头，这些算不算？”顶回韩彪，草稿第3组0-6秒保留原句、说话对象和韩彪质疑后的因果位置。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "第9组12.5-15秒承载许安“飞不飞我不知道，我只知道味道落地。”，有效字数15字、2.5秒，字秒比6.0，低于6.5硬上限；同组其他台词段也均在可表演范围内。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组组首明确韩彪、许安、林小满、唐婶和管理员甲都在公告栏前，韩彪拉管理员低语发生在同一物理空间内，没有跨空间硬切。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "evidence": "第9组组尾许安仍在炉后翻串、主办方甲准备接话；第10组组首继续锁定许安在炉后、韩彪在摊前、主办方甲位于韩彪旁边，人物位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林小满对围观街坊念报名要求，唐婶对林小满和街坊支持许安，韩彪对许安冷笑质疑，三处现场对白均写明真实说话对象。",
      "fix_instruction": "无需修复；若后续改动，继续保持每句现场对白的说话对象。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组14秒内承载唐婶公开喊话、街坊围上来、路人甲和路人乙作证四个节拍；唐婶长句给6秒，后两句短证词分别给3秒和2.5秒，节奏可表演。",
      "fix_instruction": "无需修复；若增加更多街坊证词，应拆到相邻组而不是塞入本组。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "管理员甲从公告栏旁持有记录夹和签字笔开始，第6组0-4秒翻到空白页记录推荐意见，道具归属和操作过程清楚。",
      "fix_instruction": "无需修复；若改写记录动作，应保留记录夹和签字笔的可见归属。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "主办方甲和林小满均为画面内人物现场开口对白，没有心声、画外音或电话音混用，口型承载清楚。",
      "fix_instruction": "无需修复；若增加远处韩彪反应，不要把他的心理活动写成现场开口。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "主办方甲、老客甲、唐婶、韩彪和许安均在组首空间锁定中有位置和朝向，韩彪在12-14秒走近摊前后才参与下一组正面对峙。",
      "fix_instruction": "无需修复；若让韩彪提前说话，需先在组首或前半段给出可见位置。"
    },
    {
      "group": "第11组",
      "type": "timing_math",
      "result": "warning",
      "evidence": "第11组总时长8秒，属于片尾意象短组；镜头时段0-2、2-5、5-8秒连续且总和正确，但交付时需知道它不是默认10-15秒组。",
      "fix_instruction": "可保留为片尾意象；若需要完全保守，可与第10组尾部合并或扩写到10秒，但不应硬塞无关动作。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "草稿未出现Seedance说明词、模板编号、参考图占位、自动分镜、人物图、场景图等工程或模板污染词，画面风格和负向词保持短剧提示词表达。",
      "fix_instruction": "无需修复；后续整集组装时不要添加模板说明或官方占位符。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第11组",
      "rule": "timing_math",
      "problem": "第11组为8秒片尾意象短组，低于默认10-15秒范围但符合片尾意象例外。",
      "evidence": "第11组承载夜里收摊、公告栏灯仍亮、韩彪独自等待公示三段视觉收束，没有新增对白或硬凑动作。",
      "fix": "可保留；若后续统一要求默认时长，可扩到10秒或并入第10组尾部。"
    }
  ]
}
