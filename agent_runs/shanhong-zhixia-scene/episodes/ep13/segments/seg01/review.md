{
  "pass": true,
  "summary": "第13集单一 segment 已对照原剧本、storyboard-generator 与 storyboard-reviewer 逐组审核，仓房内引蛇出洞、后沟边抓到赵成武、带油桶回仓房审问及孩子不见的外部喊声均按原剧本保留，未发现 hard issue。",
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
      "evidence": "第1组保留沈砚川递登记本、低声说“先别声张”、林知夏问“你想钓他出来？”、沈砚川说明油没走远、周大柱要搜以及沈砚川拦住他的完整因果。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组15秒分5个时间段承载赵有福质问、沈砚川反问、沈小禾报灯快灭、村民担心、沈砚川公开警告和赵成武低头；最长台词“我现在把话放这儿，谁把油送回来，我不追”约20字给3.5秒，约5.7字/秒，属于情绪扬声可承载范围。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "第4组组首明确柴油桶在赵成武肩上，6-10秒沈砚川一把拽住桶把，之后桶被两人同时控制，道具归属变化有可见过渡。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组从后沟边转回果园仓房内，组首重新锁定打开的仓门、煤油灯、沈砚川、赵成武、周大柱、赵有福和村民位置，没有把后沟边动作硬塞进同一组。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "第7组9-12秒把孩子不见的喊声写为仓房外雨幕中的人声，并用木门晃动和门边村民转头作为可见载体，未让画面内人物错误承担口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈砚川对林知夏、林知夏对沈砚川、周大柱对沈砚川、沈砚川对周大柱的现场对白对象均明确。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对象，避免无对象开口。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵有福、沈小禾、村民甲、村民乙、赵成武均在说话或被镜头带到前具备组首位置或明确入场动作，赵成武在背景角落低头与原剧本钩子一致。",
      "fix_instruction": "若不通过，应在组首补人物位置朝向，或在说话前写出入场动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只承载木棚后等待、林知夏轻问、沈砚川解释、脚步声与赵成武扛桶出现、林知夏确认来了，节拍清楚且未和抓捕动作混塞。",
      "fix_instruction": "若不通过，应把抓捕与等待拆开，避免同组过载。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第5组保留赵成武说“桶不是我要挪的！”、沈砚川追问“那是谁的主意？”、赵成武答“我不知道！”的顺序与逃避状态，没有新增主使或改写因果。",
      "fix_instruction": "若不通过，应恢复原台词和未供出主使的剧情状态。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部柴油桶被沈砚川控制，第6组开头写沈砚川拖桶进仓房、赵成武被推到人前，空间转换通过可见动作完成。",
      "fix_instruction": "若不通过，应补从后沟边回仓房的拖桶和押人动作。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "整组只有自然分镜、现场对白、外部喊声、光影设计、画面风格和负面提示词，未出现模型说明词、模板编号、参考图、自动正反打或广告/MV语气。",
      "fix_instruction": "若不通过，应删除工程说明和模板污染，只保留可生成画面与声音。"
    }
  ],
  "issues": [],
  "warnings": []
}
