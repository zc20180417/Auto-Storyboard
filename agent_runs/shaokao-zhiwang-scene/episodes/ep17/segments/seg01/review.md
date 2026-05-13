{
  "pass": true,
  "summary": "对照ep17分段剧本、竖屏生成规则和seg01草稿，4组完整保留主办方求援、韩彪阻拦、许安接手起火、分桌出串、客人认可和韩彪失势等关键剧情，未发现硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
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
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "韩彪2.5-5秒台词约11个有效字，2.5秒承载约4.4字/秒；主办方甲5-7秒约9字，2秒承载约4.5字/秒；林小满和许安7-12秒合计约22字，5秒承载约4.4字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "本组单一空间为社区广场主桌区，许安、林小满、韩彪、客人甲、唐婶和客人数人均在组首拥有位置、朝向或背景可见状态；许安的炉子和生肉串托盘在组首已明确位于画面中央偏前方。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "林小满报“三桌少辣，五桌先上”，许安回应“先走主桌”，客人乙和客人甲分别认可口味，唐婶扬声招呼等这一炉，台词顺序和出餐协作关系与原剧本一致。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组尾部许安继续分批翻串、唐婶举托盘招呼、韩彪在后方；第4组组首复述许安在炉前、唐婶托盘、韩彪背景右后方、客人围在桌边，状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "主办方甲求许安顶上、韩彪强调这是自己的单、主办方喝住韩彪、林小满问许安上不上、许安说明不是替韩彪收拾而是不能砸场，关键台词和因果完整。",
      "fix_instruction": "若不通过，应补回缺失台词，恢复主办方临场求援和许安接手理由的原始顺序。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "许安的炉子、生肉串托盘和炭火在组首已明确位置，5-10.5秒写出许安推炉到主桌前、摆肉和拨炭起火，道具状态变化有可见动作。",
      "fix_instruction": "若不通过，应补充炉子从原位到主桌前、肉串上炉和炭火点亮的可见过渡。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林小满对许安、许安对林小满、客人乙对唐婶、客人甲对身旁客人、唐婶对排队客人的现场对白都写明真实对象，没有假对象或口型混用。",
      "fix_instruction": "若不通过，应把所有现场对白改成明确的“A对B说道/问道/喊道”结构。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载客人点头、主办方放松、韩彪一句压火、许安一句反击和最后一桌稳住，4个时间段总时长10秒，动作与短句没有挤压到不可表演。",
      "fix_instruction": "若不通过，应拆开韩彪挑衅与最后一桌稳住，或压缩非关键人群反应。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文没有出现模型说明词、官方模板编号、占位符、参考图、广告式字幕或横屏字段，保持自然短剧画面描述。",
      "fix_instruction": "若不通过，应删除污染词并改写成可见动作、声音来源、人物视线和道具状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
