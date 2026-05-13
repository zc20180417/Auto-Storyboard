{
  "pass": true,
  "summary": "seg01 已逐组对照原剧本、竖屏生成规则和当前分镜，台词顺序、说话对象、cut_id、时间轴、空间锁定和组间衔接均可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "韩彪当众对许安说“许安，我哪点对不起你？给你饭吃，给你活干，你倒好，转头抢我客。”，路人甲低声说“这下有热闹了。”，保留了原剧本开场冲突和围观反应。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "林小满对韩彪说“你还挺会演。”，韩彪不看林小满但明确对林小满说“我跟许安说话，轮不到你插嘴。”，许安与韩彪的对话对象也逐句明确。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "唐婶台词约24个有效字放在4.5-10秒的5.5秒时间段内，约4.4字/秒；林小满13字放在3秒内，约4.3字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "组首锁定为街口两边摊位之间，许安在右侧摊位、韩彪在左侧摊位、新客甲乙在街心持有两边烤串，后续比较烤串和评价都发生在同一物理空间内。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "evidence": "第5组尾部韩彪转开身，第6组组首写韩彪身体偏向自己摊位方向，并在0-2秒继续走出两步后回头放话，人物位置变化有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪、许安、林小满、唐婶、路人甲和吃串路人均在组首拥有明确画面位置、身体朝向和视线关系，路人甲开口前已在人群边缘可见。",
      "fix_instruction": "若不通过，应在组首补齐开口人物的位置、朝向和可见状态，或在开口前安排入场。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载许安一句反击、围观安静反应、唐婶提议和林小满接话，共4个轻中等节拍，13秒内分配清楚，没有长动作或关键道具操作挤压台词。",
      "fix_instruction": "若不通过，应把唐婶提议或林小满接话拆入相邻组，避免同组节拍过载。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "新客甲、新客乙分别评价两边烤串，原台词“话谁都会说，东西骗不了嘴。”和“对面那边油大味乱，这边稳。”完整保留，并保留韩彪脸色发紧的反应。",
      "fix_instruction": "若不通过，应恢复原台词和街心比较动作，不得改成旁白或删掉新客评价。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "许安“你不是最信客人吗，现在又不信了？”约15个有效字放在4秒内，约3.8字/秒，配合平稳质问和林小满旁观，不存在过快硬问题。",
      "fix_instruction": "若不通过，应延长该时间段或拆成许安开口与韩彪反应两个时间段。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "烤串和纸盘只作为街心比较后的环境道具出现，韩彪放话、林小满追问、唐婶解释大单均不依赖道具转移，不存在关键道具归属跳变。",
      "fix_instruction": "若不通过，应补充道具放下、递出或收回等可见过渡。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终组只写韩彪冷笑威胁、围观反应和许安回应，没有出现模型说明词、官方模板编号、占位符、字幕贴片或非短剧模板语气。",
      "fix_instruction": "若不通过，应删除相关工程词或模板词，改成可见动作、表情、声音和对话。"
    }
  ],
  "issues": [],
  "warnings": []
}
