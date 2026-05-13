{
  "pass": true,
  "summary": "seg01已对照第12集原剧本和竖屏生成规则完成审核，5组均保留客流反转、街坊评价、韩彪威胁与炉火收尾，未发现阻断交付的硬问题。",
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
      "evidence": "原剧本中林小满喊排队、路人甲催单、许安回应少辣、唐婶帮喊、路人乙评价都在第1组按原台词保留，人物关系和客流变多的因果未改写。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部许安仍在炉前、林小满记单；第2组组首继续写许安在炉后、林小满在点单桌旁，并引入对面韩彪摊空桌，空间仍是同一街口两边摊位。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组2-5.5秒承载街坊甲14字和街坊乙8字，共22字/3.5秒，约6.3字/秒，低于6.5硬上限；低声议论配合点头和吃串动作，节奏可表演。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组组首列明许安、林小满、韩彪和街坊的位置及身体朝向，韩彪位于对面摊位通道口，随后镜头中穿过通道到许安炉前，人物可用性有明确入场动作。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "evidence": "第5组只写韩彪威胁、许安回应、韩彪转身离开和新串落炉火起，没有出现模板编号、参考图、自动分镜或模型说明词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林小满对排队路人、路人甲对许安、许安对路人甲、唐婶对后来的排队路人、路人乙对同桌街坊说话，所有画面内对白都有真实对象。",
      "fix_instruction": "若后续改稿导致对白对象丢失，应补回具体对话对象，不能写成对空气或对桌面说话。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组包含林小满报桌不够、许安安排搬凳、对面空桌落差、韩彪催阿顺和阿顺发虚五个短节拍，总时长12秒，动作都围绕同一客流反转，没有外加新事件。",
      "fix_instruction": "若增加新的冲突动作或道具操作，应拆到新组，避免在12秒内过载。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "街坊甲、街坊乙、林小满和许安四句台词均按原文保留，街坊认准许安味道的转折没有新增剧情或改成人物直接宣判。",
      "fix_instruction": "若改稿时压缩街坊议论，必须保留招牌的魂在许安这边和最近总差一口两层信息。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪在组首已位于右侧通道口，0-2.5秒完成来到炉前并开口；林小满组首在点单桌旁，7-10秒挡到两人之间后再反问，所有行动前均可见或有入场过程。",
      "fix_instruction": "若删去韩彪来到炉前或林小满挡上去的动作，会造成角色位置跳变，应补回可见过渡。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第5组组首写新一把生串位于炉边托盘，9-11秒许安把新串落上炉面，烤串从托盘到炉面的道具转移有可见动作；夹子持续在许安手中。",
      "fix_instruction": "若调整收尾火焰镜头，应保留新串在托盘和落上炉面的过渡，避免道具突然出现在炉上。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本段无心声、旁白、电话音或门外音，韩彪和许安均为现场开口对白，口型承载与画面主体一致。",
      "fix_instruction": "若后续增加旁白或心声，应明确声音来源，并写明画面人物嘴唇闭合、不做口型。"
    }
  ],
  "issues": [],
  "warnings": []
}
