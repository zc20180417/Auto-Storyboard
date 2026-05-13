{
  "pass": true,
  "summary": "seg01已对照原剧本、竖屏生成规则和当前分镜逐组审核，台词、空间、时长、组尾衔接和污染项均未发现阻断问题。",
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
    "第10组"
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
      "evidence": "阿顺被投资人逼问、韩彪威胁、阿顺说出“这半年，店里常拿便宜冻货顶鲜货。赶客多的时候，还会压腌料、抢火候。”均按原剧本顺序保留，没有改变说话对象。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "投资人乙长句安排在4.5-10秒，共5.5秒，台词有效字数约23字，约4.2字/秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "本组始终在街口烧烤摊同一物理空间内，组首列明许安、林小满、唐婶、路人甲、路人乙和食客的位置与朝向，炉火和餐桌道具可用。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "韩彪、许安、林小满的现场对话都明确写成对许安或对韩彪说道，没有把台词写成无对象自语。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "evidence": "第9组韩彪夜晚离开摊前，第10组明确切到第二天早晨公告栏与对街店门口，时间和空间变化有场景标题与组首锁定，不会误接为同一夜晚连续动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "老伙计甲骂“难怪越来越难吃”、韩彪拍桌骂“你放屁”、阿顺揭穿宴席压货三处关键台词和动作均保留。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组13秒承载三句短台词、摘围裙摘帽、放签子和韩彪伸手拦人，动作链按0-2.5、2.5-4.5、4.5-7、7-11、11-13秒分开，未把长动作和长台词硬塞同一镜头。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部韩彪拦不住人，第5组组首延续老伙计位于门口方向、韩彪面向门口、阿顺在后方的状态，人物位置连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪在6.5-11秒从对街走到摊前后才参与后续冲突，第7组组首未把尚未到摊前的韩彪写成第一帧已在场，后续入场动作明确。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "韩彪和许安都是画面内人物现场开口，对话对象明确；韩彪沉默转身段无旁白或心声，不存在口型错配。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "公告通知和评选信息作为剧情道具呈现，正文未出现模板编号、官方占位符、模型说明词或参考图指令。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
