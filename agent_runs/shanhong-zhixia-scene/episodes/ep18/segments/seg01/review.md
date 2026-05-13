{
  "pass": true,
  "summary": "seg01共8组，已对照原剧本完成竖屏scene分镜审核，关键台词、救人动作、协议揭露和组间状态连续，未发现阻断交付的hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
      "evidence": "保留晒场撤离的核心台词：村民甲“水追上来了！”，沈小禾“老人先走这边！”，周大柱“别堵路！”，赵有福“让开！让我先过去！”，村民乙“你还有脸抢前头！”，沈砚川“都靠右，留出路！”，说话对象均明确为周围村民、赵有福或人群。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "第4组14秒承载沈砚川取绳喊“拉绳”、周大柱质疑、沈砚川回应“我救人，不救账！”以及众人稳住绳子和倒木，强节拍约4个，分成4个时间段，救援动作有5秒表演空间，未压进不可表演节奏。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "第7组15秒包含“这里有名单”“还有协议”“这是让地协议”“哥，这张有娘的手印！”“我没按过！”等短句，分别落在3.5秒、2.5秒、3秒和6秒内，配合翻袋、接协议和沈母反应，字秒比未超过6.5字/秒。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "evidence": "第8组结尾只写仓房内众人围住赵有福、协议在沈砚川手中、雨声持续等自然画面，没有Seedance说明、模板编号、参考图、字幕、广告或工程词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部沈砚川让出窄路、赵有福卡在人群前沿；第2组组首复述窄路和赵有福位置，并让沈母、沈小禾、林知夏进入同一晒场状态，随后急水撞倒木架，组尾自然接到第3组边沟事故。",
      "fix_instruction": "若不通过，应在第1组尾或第2组组首补足赵有福与边沟、木架的相对位置。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵有福、沈砚川、林知夏、周大柱、村民甲均在组首空间锁定中有明确画面位置、身体朝向和视线方向，赵有福被压、周大柱和村民甲发声、林知夏看沈砚川均有可用性基础。",
      "fix_instruction": "若不通过，应把发声或行动人物先写入组首空间锁定，或在说话前安排入场动作。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第5组保留“几人合力抬木，赵有福被拖出来，脸都白了”、赵有福“砚川，我错了……”和沈砚川“现在知道错，晚了。”，没有新增改变剧情的惩罚或和解动作。",
      "fix_instruction": "若不通过，应删除新增剧情动作，只保留救出、认错和沈砚川冷回应。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "防水袋先在赵有福怀里，赵成武摸出后赵有福扑抢，周大柱按住赵有福，赵成武再把防水袋递到木桌边给林知夏，关键道具归属变化有可见过渡。",
      "fix_instruction": "若不通过，应补充防水袋从赵有福怀中到赵成武手中、再到林知夏手中的递接动作。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第7组全部为仓房内现场开口对白，均写明说话对象或对屋内众人发声；没有心声、画外音、电话音或广播音被误写成现场口型。",
      "fix_instruction": "若不通过，应把非现场声音改成画外音并注明画面人物嘴唇闭合、不做口型。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第8组单一物理空间为果园仓房内，组首明确木桌、协议、防水袋、沈砚川、赵有福、周大柱、沈母、林知夏、村民乙的位置和朝向，未跨到外部雨场。",
      "fix_instruction": "若不通过，应将外部雨景只作为门外声音和光线，不把人物切到另一个现实空间。"
    }
  ],
  "issues": [],
  "warnings": []
}
