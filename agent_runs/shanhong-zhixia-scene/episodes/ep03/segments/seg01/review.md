{
  "pass": true,
  "summary": "seg01 已按竖屏 scene 规则完成审核，关键台词、人物关系、雨中抢险因果、时间轴和组间衔接均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "沈砚川挖主沟、沈小禾拖木桩、铁锹麻绳在场，原台词“手套戴上”“我能搬”“这条是主沟”“那边开横槽”“这坑干啥”“沉砂，防堵”均按顺序保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "林知夏与沈砚川关于导流槽、沟线、乡里清沟的连续短句分布在 3-5.5 秒和 5.5-9 秒，台词总量约 29 字配 6 秒并含视线和指沟动作，口型容量合理。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组明确切到夜晚果园下坡，组首列出排水沟、粮袋、隔壁坡地、沈砚川、林知夏、周大柱、村民甲和村民乙的位置与朝向，没有把坡地与其他物理空间混写。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "粮袋在第4组组首和第5组组首均位于画面右侧棚边，第5组由沈砚川指向粮袋并要求村民先搬粮，道具归属和可操作状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "所有现场对白均写明说话对象：沈砚川对沈小禾、沈小禾对沈砚川，未出现假对象或无对象开口。",
      "fix_instruction": "若不通过，应把每句现场对白改成 A 对 B 说道或问道，并保留原台词。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周大柱、村民甲、赵成武、沈砚川和沈小禾都在组首拥有明确画面位置、身体朝向和视线，发声前已可见。",
      "fix_instruction": "若不通过，应在组首补齐发声人物的位置和朝向，或在其台词前写入清楚入场动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组核心负载为林知夏靠近看沟、导流槽短问答、上游风险判断和周大柱否认，13 秒内 4 个时间段承载清楚，没有叠加关键道具操作或外部灾变。",
      "fix_instruction": "若不通过，应拆出上游风险判断或压缩非关键走位。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "村民乙、周大柱、林知夏、沈砚川、村民甲的台词均为画面内现场开口，声音来源与口型一致；雨声和远处墙影只作为环境事件和可见反应存在。",
      "fix_instruction": "若不通过，应为门外音或远处喊声补可见载体，并避免让非声音主体做口型。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部是周大柱想往坡墙方向去、沈砚川和林知夏拦住人群；第5组组首复述周大柱前倾、沈砚川靠近其肩侧、黄水继续沿沟流，状态衔接连续。",
      "fix_instruction": "若不通过，应在第4组组尾或第5组组首补人物位置、黄水状态和粮袋位置。"
    },
    {
      "group": "第1组-第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位符、广告语、字幕要求或“空间先被交代出来”等模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程词和模板语气，改成自然画面、声音和动作描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
