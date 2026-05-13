{
  "pass": true,
  "summary": "seg01 已对照第7集原剧本、竖屏生成规则和当前分镜逐组审核，台词、说话对象、街口空间、组首锁定、时长与提示词洁净度均可交付。",
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
      "type": "dialogue_pacing",
      "evidence": "9-12秒韩彪台词“对面的，学着点，做生意不是守死规矩。”约18个有效字，3秒承载，字秒比约6.0，低于6.5硬上限；前两段林小满与许安短句也分别用4.5秒和2.5秒承载，口型可完成。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留许安“你先把肉备够”、阿顺“彪哥今天人得爆”、路人甲乙对便宜和香味的分歧、林小满“客都过去了”和许安“留下来的，才是客”，且顺序与原剧本一致。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首固定在许安烧烤摊前的空桌区，唐婶、街坊、老客、许安、林小满均有画面位置和身体朝向；唐婶拍桌点串、林小满应单、老客评价味不稳都发生在同一物理空间。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "0-4秒许安将刚烤好的烤串递到唐婶桌前并等她接稳，4-8秒老客接过烤串咬一口评价，关键道具从炉边到客桌的过渡清楚。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "evidence": "本组没有出现模板编号、参考图、自动分镜、Seedance说明词、字幕贴片或首尾帧等工程词；对供货贩子的交代只写可见动作，没有杜撰具体台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林小满对许安说价格压力，许安对林小满回应不动价，韩彪隔街冲许安挑衅，所有现场对白都有真实人物对象，没有假对象。",
      "fix_instruction": "若后续改稿新增对白，仍需写清谁对谁说，门外或画外声音需标明来源。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组由许安回击、阿顺得意、路人转向对面、林小满焦急与许安稳定回应构成，强节拍分布在4个时间段内，没有将中等动作、关键道具和长台词硬塞到同一镜头。",
      "fix_instruction": "若需要增加更多顾客拉客细节，应拆到相邻组，不要塞入现有14秒组。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "唐婶点“三十串”、林小满应声、老客说对面味不稳、唐婶说便宜但嘴受罪，四个剧本信息点完整保留，没有新增剧情因果。",
      "fix_instruction": "若修稿，不能改唐婶点单数量或老客对对面味道不稳的判断。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部唐婶和街坊坐稳、林小满准备记串、许安继续翻肉；第4组首继续在同一客桌与炉边，唐婶、老客、许安、林小满的位置和烤串状态连续。",
      "fix_instruction": "若改变人物站位，应在第3组尾或第4组首补出可见移动过渡。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪和阿顺在组首已位于对面店门口；供货贩子在6-10秒从门帘旁靠近后才参与动作，满足入场后行动的可用性要求。",
      "fix_instruction": "若让供货贩子提前说话或操作道具，需先在组首写明其位置或在说话前给出入场动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
