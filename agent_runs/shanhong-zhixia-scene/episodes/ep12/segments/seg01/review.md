{
  "pass": true,
  "summary": "已对照第12集原剧本、竖屏生成规则和seg01分镜逐组审核，仓房对质与后沟追查的台词、空间、时长和组间衔接均可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中赵有福先声质疑、沈砚川反问、赵有福要求给说法、村民甲乙担心发电和烘果、沈砚川说“说法我给”均按原顺序保留，人物关系未改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈砚川“七袋米，十二袋面，两桶柴油，刚才都记过。”约18字安排在3-8秒并配合指登记本后的抬眼，约3.6字/秒，未超过6.5字/秒；林知夏与赵有福短句分别给2秒和3秒。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "周大柱对赵有福骂“你少放屁”和指认抢钥匙，村民丙对沈砚川作证，赵有福对周大柱辩解，沈砚川对赵有福压声指出“帮忙还是下手”，每句现场对白均有真实对象。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "该组只发生在夜雨中的仓房后沟边，组首锁定沈砚川蹲在泥地边持手电、林知夏和周大柱站位、拖痕脚印位置，所有参与说话和动作的人物在组首可用。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第4组结尾周大柱说出赵成武胶鞋、沈砚川仍蹲在泥地边盯脚印；第5组组首继续写沈砚川蹲在脚印旁、林知夏和周大柱站在沟边，人物姿态和道具状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组负载为赵有福发难、沈砚川反问、村民恐慌和沈砚川走到桌前承诺给说法，12秒内4个时间段承载清楚，没有叠加关键道具操作或外部事件过载。",
      "fix_instruction": "若出现仓促，应拆出村民恐慌或沈砚川走桌前的动作；当前无需修改。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "登记本在组首已摊放于木桌，0-3秒明确沈砚川摊开并一行一行往下指，后续对账台词与道具位置一致。",
      "fix_instruction": "若登记本归属含糊，应补充沈砚川把本子摊开放在桌面；当前已经具备。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "抢钥匙指控、村民丙作证、赵有福辩称帮忙、沈砚川反压赵有福的台词均完整保留，没有新增打斗、递物或改变剧情因果的动作。",
      "fix_instruction": "若新增强动作，应删除并回到原剧本对质；当前无需修改。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“有人往外拖过东西”和“胶鞋”通过泥地拖痕、脚印花纹、手电光和人物低头观察转译为可见信息，未依赖不可视判断。",
      "fix_instruction": "若只写结论，应补脚印和拖痕特写；当前已经具备。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第5组全部为现场三人对话，没有心声、门外音或电话音；每句台词均由画面内角色对真实对象开口承载。",
      "fix_instruction": "若改成心声或画外音，应写明嘴唇闭合和声音来源；当前无需修改。"
    },
    {
      "group": "第1组至第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图占位、模型说明词、自动分镜、官方模板语气或模板化批量描述；尾部仅保留稳定画面风格和负面词。",
      "fix_instruction": "若出现模型或模板说明，应改成自然画面描述；当前无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
