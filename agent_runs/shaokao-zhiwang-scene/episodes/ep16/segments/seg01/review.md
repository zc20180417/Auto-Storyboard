{
  "pass": true,
  "summary": "已逐组对照第16集原剧本与竖屏生成规则审核，台词、空间、时长、口型承载和组间衔接均可交付。",
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
      "evidence": "原剧本中许安备炭、肉、签子，林小满低声问准备是否过足，许安回答不是赌而是防韩彪翻车，并保留“那我就当练手”；分镜第1组按原顺序呈现这些台词和动作，没有新增剧情。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "韩彪、许安、林小满的挑衅交锋分布在2.5秒、2.5秒、4秒、4.5秒等时间段；最长的9-13.5秒连续对话约18个有效字，约4字/秒，低于6.5字/秒硬上限且含换人反应。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组全程在社区广场备餐区，组首锁定许安、林小满、马会和后厨门位置；阿顺在2.5-6秒从后厨门口入场后才参与动作，人物可用性成立。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "客人甲、客人乙、韩彪、阿顺、主办方甲均为画面内现场开口，分镜逐句写明对话对象，没有把旁白、心声或门外音误写成现场口型。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "炭炉在组首位于许安双手扶着的推架上，8-12秒许安双手握住推架向主桌区前方推动；道具归属和移动过渡清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安与林小满关于备料、防翻车、练手的台词完整保留，韩彪经过并停下的事件只作为尾部承接，没有改变人物关系或因果。",
      "fix_instruction": "若不通过，应恢复原剧本台词顺序和韩彪经过后停下的承接动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "每句现场对白均写明“韩彪对许安”“许安对韩彪”“林小满对韩彪”“韩彪对林小满”的真实对象，没有假对象对白。",
      "fix_instruction": "若不通过，应补齐每句画面内对白的真实说话对象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组为9秒短承接，承载韩彪离开、阿顺抱料盆发抖、马会压声提醒和许安回应；前一组已满15秒且后一组切到主桌区，保留短组合理。",
      "fix_instruction": "若不通过，应只在同一备餐区内微调时长，不应跨主桌区硬合并。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第4组台词分布为客人短句2.5秒、韩彪和阿顺连续回应3.5秒、主办方质问3秒；有效字秒比均未超过6.5，且动作和反应可表演。",
      "fix_instruction": "若不通过，应拆分韩彪和阿顺回应，或压缩非关键反应。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部主办方甲站起质问韩彪、阿顺抱紧料盆；第5组组首延续主办方甲、韩彪、阿顺、客人和主桌道具状态，并补入许安和林小满在主桌区边缘的可用位置。",
      "fix_instruction": "若不通过，应在第4组尾部或第5组组首补明人物和道具位置。"
    },
    {
      "group": "第1组至第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位、自动正反打、字幕广告语或低质模板化描述；尾部负面词保持竖屏短剧通用约束。",
      "fix_instruction": "若不通过，应删除模板、模型和工程说明词，改成自然可拍画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
