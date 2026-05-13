{
  "pass": true,
  "summary": "已对照第24集原剧本、竖屏生成规则和当前seg01分镜逐组审核，救小禾、开旧河道、发现证据、施工方追责与砚川反击的关键台词和动作均保留，未发现阻断交付的硬问题。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中沈砚川喊“小禾，贴左墙！”，沈小禾哭“哥，我怕！”，沈砚川硬声“听我话！”均按顺序保留；木桩撞门和门板裂而不开也在8-12秒承载。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "10-13秒承载沈母“小禾！”和沈小禾“娘，药在这儿！”，有效台词约10字/3秒，字秒比约3.3；同时有跪坐护药包动作，节奏可表演。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组时间段为0-4、4-6、6-10、10-13秒，连续且结束于标题13秒；镜头数4个与标题一致，组总时长在6-15秒范围内。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "旧铁箱先在0-3秒被水冲到沈砚川脚边，3-6秒林知夏捞起，6-9秒沈砚川接过并撬开，9-15秒林知夏翻看图纸账本，道具归属和使用路径完整。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "赵有福对施工方代表喊“是沈砚川！”，沈小禾对赵有福说“你放屁！”，施工方代表对沈砚川问“你私自毁工程？”，周大柱对施工方代表喊“没他，村都没了！”，每句真人对白都有真实对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林知夏、沈砚川、周大柱和远处赵有福在组首均有位置与朝向；赵成武在3-6秒先从右后方冲入并抓起锄头，之后才喊话和砸墙，人物可用性成立。",
      "fix_instruction": "若赵成武未先入场就喊话或砸墙，应在他行动前补入场动作与位置。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含旧河道料场交代、推钢管指令、赵成武顶前头、赵有福阻拦并被掀开四个强节拍，分配为14秒且动作顺序清楚，没有把泄洪崩开再塞入同组。",
      "fix_instruction": "若同时加入下口崩开和水退台词，会导致过载，应拆到下一组。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "铁箱、图纸、账本、旧河道回填、泄口封堵人工、周大柱怒斥和赵有福“完了……”均与原剧本一致，未新增改变证据性质的动作。",
      "fix_instruction": "若缺少图纸或账本任一证据台词，应补回对应台词和翻看动作。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组只发生在果园高处，施工方代表和随行人员从远处泥路冲上坡后再问责，未把旧河道下口动作混进同一现实空间。",
      "fix_instruction": "若需要展示旧河道下口，只能作为坡下被指向的方向或另起一组，不能与果园高处混成连续现实空间。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组尾部施工方代表盯住沈砚川、周大柱挡在旁边；第9组组首延续施工方代表正对沈砚川、周大柱在沈砚川左侧、旧铁箱在脚边，位置和道具连续。",
      "fix_instruction": "若旧铁箱或人物位置突然变化，应在第8组尾部或第9组开头补可见过渡。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终反击组只写沈砚川打开铁箱、举账本图纸并说台词，没有出现模板编号、参考图、模型自动分镜、字幕或广告式表达。",
      "fix_instruction": "若出现模板或模型说明词，应改成自然画面动作和可听对白。"
    }
  ],
  "issues": [],
  "warnings": []
}
