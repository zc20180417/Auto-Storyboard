{
  "pass": true,
  "summary": "ep16 seg01 已对照原剧本、竖屏生成规则和当前分镜逐组审核，9 个分镜组保留关键台词、人物关系、水势推进和开第二道分洪口的决策，未发现 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组"
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组 12 秒内承载沈砚川拦住周大柱、村民甲追问、沈砚川说“水还在涨，先保命”、赵有福反呛和沈砚川警告；有效台词约 37 字，分成 3.5 秒、3.5 秒、5 秒三个时间段，情绪对白字秒比未超过 6.5。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组只发生在凌晨雨中的果园后沟，组首写明沈砚川、林知夏、周大柱、村民乙和村民的位置、身体朝向、沟口黄水、木桩与碎石，没有把坡道或果园中排混入同一现实空间。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "第8组按原剧本保留“开哪儿？”“从东排果树穿过去。”“那是你家果树！”“那一排都得砍？”“不砍树，人都得埋这儿。”的台词顺序和说话对象，没有新增改变剧情的动作。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "evidence": "第9组组首先把铁锹放在画面左前方泥地边，随后周大柱弯腰抓起铁锹并握紧木柄，对应原剧本“周大柱(抄锹): 俺也去！”，道具可操作状态有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "村民甲、村民乙、赵有福、赵成武、周大柱的现场对白均写明对赵成武、村民或围上来的村民说话，对象真实可见，未出现假对白对象。",
      "fix_instruction": "若后续改稿新增对白，继续使用“A对B说道/问道/喊道”并确保 B 是画面中真实人物或明确声音来源。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林知夏的“后沟又响了！”是画面人物现场开口；远处闷声写成雨幕深处传来的环境声音，并配合众人转头和水流变急的可见反应，没有让人物替闷响做口型。",
      "fix_instruction": "若加强闷响表现，应继续写成环境声和人物反应，不要改成某个画面人物开口解释。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组 14 秒分为沈砚川解释老石坝、辨认散水/憋坝声、村民乙追问蓄水、林知夏补充风险四个节拍，均在同一后沟空间，台词量约 44 字，未叠加中等以上动作链或道具操作。",
      "fix_instruction": "若增加上游动作或新的外部事件，应拆到新组，避免与憋坝判断台词挤在同一 14 秒内。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部是众人确认可能憋坝并看向后沟上游，第6组组首延续同一后沟空间、同一水流和木桩状态，赵有福、赵成武作为本转场角色在背景泥地边缘可见，随后才参与对白反应。",
      "fix_instruction": "若删去赵有福或赵成武的组首位置，第6组台词前需补足他们在后沟边缘的可见状态。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第7组保留木桩被冲断、沟水斜扑仓房、沈小禾喊“哥，水拐过来了！”、林知夏提示后沟顶不住、村民问“那咋办！”以及沈砚川决定开第二道分洪口的因果顺序。",
      "fix_instruction": "若需要压缩，只能压缩反应动作，不能删掉水拐向仓房和开第二道分洪口的因果链。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第8组没有模板编号、参考图、自动分镜、首尾帧、视频延长、广告口号或横屏字段，也没有出现“空间先被交代出来”等模板化批量描述。",
      "fix_instruction": "后续修稿不得加入 Seedance 模型说明、官方模板字样、@图片/@视频/@音频占位符或非短剧模板语气。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "timing_math",
      "problem": "第3组为 9 秒短组。",
      "evidence": "该组只承载林知夏提示“后沟又响了”、众人回头、远处闷声和水势加急，是坡道转向后沟的外部事件短承接，合并进第2组会使坡道对峙节拍过载。",
      "fix": "可保留为短承接；收集说明中提示该组属于水势突变的短事件组。"
    },
    {
      "severity": "soft",
      "group": "第6组",
      "rule": "timing_math",
      "problem": "第6组为 9 秒短组。",
      "evidence": "该组只承载赵有福否认、沈砚川回应和远处闷裂导致众人变色，是后沟判断后的短动作余波与转场触发；强行扩到 10 秒以上会增加无剧本依据的拖时动作。",
      "fix": "可保留为短动作余波；不要用长凝视或额外解释台词凑时长。"
    }
  ]
}
