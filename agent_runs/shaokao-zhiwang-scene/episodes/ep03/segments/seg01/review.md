{
  "pass": true,
  "summary": "seg01六组已对照第3集原剧本完成审核，台词、空间、cut_id、组间衔接和门口转场均符合竖屏生产合同。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "evidence": "街坊甲2秒承载“来都来了，坐下把话说开”，韩彪3秒承载“许安，来，坐我边上”，许安2秒承载“有话就说”，韩彪5秒承载扩店和留脸台词，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保留韩彪指着许安说“他要真有本事，就自己支个炉子去卖。我看他两天就黄。”、许安追问“你说完了没有？”、韩彪继续羞辱以及许安“那你等着看”后离席，剧情因果未改变。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第4组尾部许安跨出包间门，第5组切到饭馆门口时明确许安从玻璃门内走出并握着打火机，林小满从门内追出站到侧前方，承接原剧本门口场景。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "林小满0-7秒连续说明“我早看过你忙……我烦他那样的人”，约41个有效字，约5.9字/秒；9-13秒承载“我信刚才那桌上，最像人的那个”，约4字/秒，均可表演。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组-第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "包间开局、韩彪请人谈扩店并给许安留脸、唐婶质疑、一万元羞辱、街坊乙意外、许安压火追问的顺序均与剧本一致。",
      "fix_instruction": "若不通过，应只回到对应组补回原剧本台词或纠正说话对象，不重写无关组。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪、许安、马会、唐婶和街坊在组首均有位置；林小满和服务员在9秒后通过包间门口入场并先出现后说话，人物可用性成立。",
      "fix_instruction": "若不通过，应在角色开口前补入入场动作或在组首写明其已处于可被揭示的位置。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含林小满放菜、韩彪指人挑衅、许安压火追问、韩彪二次羞辱、许安站起离席五个时间段，总时长15秒，强节拍围绕同一包间冲突，没有跨空间硬塞。",
      "fix_instruction": "若不通过，应拆出离席或压缩非关键放菜动作，而不是删改韩彪和许安的关键台词。"
    },
    {
      "group": "第5组-第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "两组均发生在饭馆门口，组首写明玻璃门、街边招牌、许安和林小满的位置与身体朝向，打火机归属持续在许安手中直到第6组尾部收进口袋。",
      "fix_instruction": "若不通过，应补具体门口位置、身体朝向和打火机归属，避免只写延续上组。"
    },
    {
      "group": "第1组-第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位、自动分镜、广告字幕、MV卡点或模板化批量描述；尾部只保留稳定画面风格和负面提示。",
      "fix_instruction": "若不通过，应删除工程说明词并改成具体人物动作、声音来源、场景和道具状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
