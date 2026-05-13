{
  "pass": true,
  "summary": "seg01 草稿按原剧本顺序保留雨夜果园门口秩序建立、仓房登记避难和旧仓房救援信息，格式、空间锁定、台词指向和时间轴均可交付。",
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
      "evidence": "原剧本 8-1 中村民甲“先让我进！”、村民乙“我孩子发抖了！”、周大柱“别挤！听砚川的！”、沈砚川“老人孩子先进 / 凭这是我家地”、林知夏“受伤的到左边”、沈小禾“带粮的报数！”均按顺序保留，未改变说话对象和门口混乱分流的因果。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组总时长15秒，4个时间段连续；沈砚川“粮食统一堆，火种统一放，谁私抢谁出去”约18字给5秒，并带翻本子和面向整队村民的动作，约3.6字/秒但有规则宣布的停顿和动作支撑；赵有福、沈砚川后续短句分别给3-4秒并含对峙反应，不存在超过6.5字/秒的过快问题。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组固定在夜雨中的仓房侧边，坡下旧仓房方向只作为视线和救援目标，没有把人物带入另一个现实空间；沈砚川、周大柱、村民甲和村民位置均在组首明确。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "第6组尾部写两人注意到墙边麻绳，第7组组首写麻绳位于墙边木架下；第7组0-3秒周大柱抓起麻绳，3-6秒沈砚川按住麻绳另一端，道具归属变化有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵有福“砚川，先把仓房打开”“先救人，别翻旧账”和沈砚川“你也来求我？”“规矩我定”都明确写为赵有福对沈砚川、沈砚川对赵有福的现场对白，没有假对象或心声混用。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实说话对象，或改成有来源的画外音/电话音。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只承载仓房前登记、村民质疑、赵有福帮腔和沈砚川反压四个轻中等节拍，14秒内分成4个时间段，动作和对白没有叠加门外事件或复杂道具操作。",
      "fix_instruction": "若不通过，应拆出登记动作或赵有福帮腔，避免一组塞入过多强节拍。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第5组保留林知夏发现两个孩子发热、沈小禾给婆婆水、村民丙感叹果园成避难地三个原剧本节点，并用草垫、水桶、粮袋转译避难地状态，未新增改变剧情的动作。",
      "fix_instruction": "若不通过，应恢复原台词和发热孩子、递水、避难地三项信息。"
    },
    {
      "group": "第6组-第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾部沈砚川和周大柱确认旧仓房有人并注意到墙边麻绳；第7组组首延续仓房侧边、坡下泥路、墙边麻绳和相关人物站位，救援动作从该状态自然开始。",
      "fix_instruction": "若不通过，应在第6组组尾或第7组组首补清麻绳位置、人物朝向和坡下目标。"
    },
    {
      "group": "第1组-第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "各组正文没有出现 Seedance 自动、参考模板、模板编号、@图片/@视频/@音频、字幕贴片或“空间先被交代出来”等模板化污染词；画面风格和--neg为稳定尾部约束。",
      "fix_instruction": "若不通过，应删除模型说明词、模板来源说明、官方占位符和非分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
