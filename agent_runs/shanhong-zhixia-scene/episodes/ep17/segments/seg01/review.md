{
  "pass": true,
  "summary": "已对照第17集seg01原剧本、竖屏生成规则和seg01草稿逐组审核，砍树分洪到老石坝二次险情的台词、空间、时长和组间衔接均无硬问题。",
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
      "evidence": "沈小禾说“哥，这是爹留下的。”、沈母要求砍树并说明“树没了能再种。人没了就没了。”、林知夏催沈砚川下决定、沈砚川说“我先来。”均按原剧本顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "周大柱对村民喊深挖、林知夏对村民喊立木桩、赵成武对林知夏喊“我来扛”、赵有福对赵成武喊“你回来”、赵成武对赵有福吼“都怪你”，现场对白对象清楚。"
    },
    {
      "group": "第3组",
      "type": "timing_math",
      "evidence": "第3组标题总时长13秒，时间段0-4、4-7、7-11、11-13连续，镜头数4个与时间段一致，最后时间段结束于13秒。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组另起果园高处空间，组首明确坡下分洪口、山体黑影和沈砚川、林知夏、周大柱、村民甲乙的位置，没有把分洪口工地动作硬塞在同组。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第4组结尾众人脸色全变并看向村里低处，第5组组首继续在果园高处，沈砚川、林知夏、周大柱和村民都面向转移方向，危险压力连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第1组15秒承载约60字短句交锋并包含接斧动作，分为5段，最长沈母两句约13字给在7.5-11.5秒内，未超过6.5字/秒。",
      "fix_instruction": "若短句过挤，应拆出赵有福挑衅或沈母决定；当前无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组负载为挖沟推土、木桩立住、赵成武冲上和沈砚川压住争吵，15秒内4个时间段可表演，未把分洪口冲开同时挤入本组。",
      "fix_instruction": "若加入分洪口冲开，应拆到下一组；当前已经拆分。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "赵成武磨破手、林知夏看到水头、沈砚川指挥后撤、急水冲开分洪口都转译为可见动作和可听声响，画面可生成。",
      "fix_instruction": "若只写分洪成功结论，应补木桩、急水和众人后撤；当前无需修改。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "山上传来的裂响和闷响作为环境声处理，村民甲、林知夏、周大柱、沈砚川、村民乙均为画面内现场开口对白，没有心声或画外音口型混用。",
      "fix_instruction": "若把裂响写成角色台词，应改回环境声并写人物反应；当前无需修改。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈砚川、林知夏、周大柱和村民在组首已有位置，沈小禾在7-10秒先从泥路边跑入后再说“我去带人！”，人物可用性满足规则。",
      "fix_instruction": "若沈小禾未入场便说话，应在组首锁定或台词前补入场动作；当前已经补足。"
    },
    {
      "group": "第1组至第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "seg01草稿未出现模板编号、参考图占位、模型说明词、自动分镜、官方模板语气或模板化批量描述，尾部仅保留稳定画面风格和负面词。",
      "fix_instruction": "若污染项进入正文，应删除或改为自然画面描述；当前无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
