{
  "pass": true,
  "summary": "seg01 已对照原剧本和竖屏生成规则完成审核，关键台词、人物关系、街口单一空间、cut_id、时间轴与组尾衔接均可交付；第6组时间段较多但服务试吃反转，不构成 hard issue。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "evidence": "韩彪对许安说“还真支上了？”，许安对林小满说“小满，签子递我”，韩彪再对许安问“许安，你这是做给谁看？”，每句现场对白均有真实说话对象。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "韩彪对围观路人喊“大家看清了，对面现摆的，小摊小炉，不好吃别怪我没提醒。”有效字数约27字，用6.5秒承载，约4.2字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "韩彪隔街喊话时本人位于街对面店门口并抬高声音，声音来源可见；唐婶回头对韩彪说“你少吵”，现场口型和对象明确。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "唐婶咬一口后停住，林小满问“婶子，咋样？”，唐婶说“这味……”，许安追问“婶子？”，唐婶再说“这不是以前那家店真正的味吗！”，台词顺序和试吃反转保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "许安、林小满、韩彪、阿顺和路人均在组首空间锁定中有位置和朝向；韩彪、阿顺从对面店门口进入关注点后再参与嘲讽。",
      "fix_instruction": "无需修改；若后续改稿新增人物说话，需先在组首或前半段给出可见入场。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林小满反击、韩彪冷笑、阿顺嘲炉子旧、许安回应旧炉出味四个剧情节点全部保留，未新增改变因果的动作。",
      "fix_instruction": "无需修改；保持台词原文和说话对象不变。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部韩彪抬手准备引向路人，第3组组首复述韩彪在摊位外侧一只手停在胸前，并接入他对路人喊话，状态连续。",
      "fix_instruction": "无需修改；若调整第2组结尾，应同步更新第3组组首。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第4组仍在街口空地单一空间内，唐婶位于街口背景处，随后走近询价，人物可用性和物理移动清楚。",
      "fix_instruction": "无需修改；不要把唐婶写成突然出现在摊前而缺少靠近动作。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "烤串先位于许安手边，3-6秒许安夹起并递到唐婶面前，13-15秒唐婶接过并抬到嘴边，道具归属过渡明确。",
      "fix_instruction": "无需修改；保持递出和接过两个可见动作。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "warning",
      "evidence": "第6组为15秒6个时间段，节拍包括咬一口停住、林小满追问、唐婶迟疑、许安追问、唐婶确认老味道、路人回头；内容都围绕试吃反转，理解清楚但略碎。",
      "fix_instruction": "可选优化：若后续需要更顺滑，可合并5-9.5秒唐婶迟疑与许安追问；当前不影响交付。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第6组",
      "rule": "generation_density",
      "problem": "第6组有6个时间段，存在轻微过碎风险。",
      "evidence": "15秒内连续承载试吃、两次短问答、老味道确认和路人回头，但全部围绕同一试吃反转，未造成理解断裂。",
      "fix": "可选合并唐婶迟疑与许安追问的反应段；当前无需作为 hard issue 修复。"
    }
  ]
}
