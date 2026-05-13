{
  "pass": true,
  "summary": "seg01五组均已对照第18集原剧本、竖屏生成规则和当前分镜逐项审核，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组"
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
      "type": "script_fidelity",
      "evidence": "原剧本中主办方感谢许安、许安平静回应、投资人甲质问韩彪、韩彪硬撑解释的顺序完整保留；分镜分别写成主办方甲对许安、许安对主办方甲、投资人甲对韩彪、韩彪对投资人甲说话，未改变人物关系。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "马会“失手一次，能把前排全砸了？”约13字用2.5秒，字秒比约5.2；林小满“现在大家都看明白了”约9字用2秒，字秒比约4.5；投资人甲“账和货，我回头都要看”约10字用2.5秒，字秒比约4.0，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "本组承载韩彪关门扫单子、咬牙发泄、阿顺解释、韩彪拍桌反问四个节拍，总长12秒；0-4.5秒给完整复合动作链，后续三句短对白分别独立承载，未把门外事件、道具操作和长台词挤在同一时间段。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "手机没有提前出现在桌面；第4组9-12秒改为韩彪从上衣口袋慢慢掏出手机，第5组组首承接为韩彪手中持有手机，符合原剧本“慢慢把手机拿出来”。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "evidence": "最终分镜正文只包含自然画面、对白、光影、画面风格和负面词，未出现模板编号、参考图、自动分镜、模型会处理、首帧尾帧或其他工程说明词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "四句现场对白均明确写出真实说话对象：主办方甲对许安、许安对主办方甲、投资人甲对韩彪、韩彪对投资人甲，没有假对象或旁白误写成开口。",
      "fix_instruction": "若出现缺对象对白，应补成“A对B说道/问道”的现场说话关系。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾韩彪仍在广场被投资人甲盯住，第2组组首复述同一广场人物站位，随后韩彪离开、许安收炉，状态变化有可见过渡。",
      "fix_instruction": "若组间状态跳变，应在上一组组尾或下一组前半段补人物移动和道具归属。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组只发生在韩彪店后门内侧小屋，组首写明后门、木桌、单子、韩彪、阿顺、马会的画面位置和朝向，韩彪关门扫单子放在时间段内推进。",
      "fix_instruction": "若组首写入进入、走向、拿起等过程动作，应移入后续镜头描述。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "马会“你早该收手”、韩彪“你也站他那边了？”、马会“我站能把东西做好的人”全部保留，韩彪拿手机的动作也按原剧本后置呈现。",
      "fix_instruction": "若台词或动作错置，应按原剧本顺序局部改回对应时间段。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本组没有心声、电话音或门外音，韩彪和阿顺的台词均是画面内现场开口，并写明说话对象，手机只作为计划道具和动作载体。",
      "fix_instruction": "若后续改成电话或旁白，应写清声音来源和画面人物是否闭口不做口型。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组用11秒承载韩彪威胁、阿顺追问、韩彪说明泼脏水三段同空间短对白，手机动作与台词同步完成，没有新增会改变剧情的强动作。",
      "fix_instruction": "若加入拨号、外部人物入场或额外操作，应拆组或删除新增强节拍。"
    }
  ],
  "issues": [],
  "warnings": []
}
