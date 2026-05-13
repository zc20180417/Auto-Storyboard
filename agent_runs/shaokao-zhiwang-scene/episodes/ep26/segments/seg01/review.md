{
  "pass": true,
  "summary": "已对照第26集seg01剧本和竖屏生成规则审核8组分镜，公告栏入选、街坊备战、韩彪暗中盯流程等关键台词和动作均保留，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
      "evidence": "林小满按原剧本念出“入选名单……韩彪烧烤……许安炭炉……”，唐婶、路人甲、路人乙的喜悦台词顺序保留，韩彪盯住“许安炭炉”僵住的反应也被单独呈现。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "0-5.5秒承载韩彪、许安、韩彪三句对峙台词，约25个有效字，字秒比约4.5；5.5-8秒承载许安10字回应，字秒比约4.0，均低于6.5硬上限且有视线动作支撑。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "组首明确许安、林小满、唐婶、老周、街坊甲、街坊乙的位置、身体朝向和木板、砂纸、旧招牌归属，街坊帮忙的动作均发生在白天街口空地许安摊位前。"
    },
    {
      "group": "第8组",
      "type": "timing_math",
      "evidence": "第8组总时长8秒，时间段为0-2.5秒和2.5-8秒，最后一段结束于标题总时长；该组是韩彪偷看流程的短尾声，属于悬念动作余波。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩彪对管理员甲问“这也能进？”，管理员甲对韩彪说明入选依据，林小满和唐婶均明确对韩彪回怼，没有无对象对白或假对象对白。",
      "fix_instruction": "若不通过，应补齐每句真人对白的真实说话对象，并避免把现场开口写成旁白。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只包含旧炉清灰、林小满询问新花样、许安说明不玩花三个核心节拍，15秒内动作和对白容量充足，没有搭台对街事件挤入同组。",
      "fix_instruction": "若不通过，应拆出对街搭台或压缩非关键修炉动作。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "老周在组首已位于街边且肩上扛着肉筐，4-9秒把肉筐卸到案板旁，随后老周和许安围绕这筐好货产生反应，道具归属和位置连续。",
      "fix_instruction": "若不通过，应补充肉筐从肩上到案板旁的可见过渡。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾部许安和街坊仍在摊位前忙碌，第7组组首复述许安摊位和对街搭架区的相对位置，韩彪转身阴沉的尾部状态自然接到第8组组首。",
      "fix_instruction": "若不通过，应在上一组尾部或下一组组首补清人物位置和对街搭架区状态。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第8组没有出现模板编号、参考图、模型说明词、自动分镜或横屏专属字段，只保留自然分镜正文、画面风格和负面提示词。",
      "fix_instruction": "若不通过，应删除工程说明和模板化词语，改成韩彪、伙计、旧炉、木架等可见画面信息。"
    }
  ],
  "issues": [],
  "warnings": []
}
