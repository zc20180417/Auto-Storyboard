{
  "pass": true,
  "summary": "seg01已对照第15集原剧本、竖屏生成规则和审核规则逐组检查，台词、人物关系、雨夜后沟到果树坡道的空间变化、音画承载和cut_id格式均可交付。",
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中沈砚川分派“大柱带两个人扩沟”“小禾去搬沙袋”、林知夏喊“木桩再来三根”、赵有福抱怨和沈砚川回怼均按原顺序保留，未新增改变排险逻辑的动作。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "木板、草捆堵住后沟转弯口，沈砚川从木板缝里扯出湿麻绳，承接原剧本“新绑的”证据点，道具来源和位置清楚。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "赵成武“不是我塞的！”与沈砚川“那你跑什么？”共9个有效字安排在3秒内；赵成武“我怕你们打我！”与周大柱“只怕打，不怕害人？”共17个有效字安排在3秒内，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "evidence": "组首写明赵有福已位于画面右后方坡道口，之后他说“他吓糊涂了！”具备可见入场结果状态；沈砚川、赵成武、周大柱和村民乙的位置也清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "村民甲讥讽偷油、赵成武说“我都说了不是我一个人！”以及赵有福脸色难看的反应完整保留，赵家父子的关系压力未被改写。",
      "fix_instruction": "无需修复；若后续改稿，应继续保留赵成武说漏嘴对赵有福造成压力这一因果。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "脚步声作为画外可听事件处理，并配合三人转头、手电光扫向坡道和树后人影，不让画面人物误承载脚步声口型。",
      "fix_instruction": "无需修复；若增加脚步声细节，应继续写清可见反应或声音来源。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵成武在组首已位于果树后方手电光边缘，随后转身逃跑、周大柱指认和沈砚川下令追都有明确可见对象。",
      "fix_instruction": "无需修复；不要把赵成武写成突然凭空出现。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组集中在泥坡逼问，四个时间段依次为问木板、承认搬木板、村民反应、追问谁指使，强节拍数量可控且每段动作单一。",
      "fix_instruction": "无需修复；若添加赵有福入场，应拆到下一组或保持本组尾部承接。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组尾部赵有福挡在赵成武旁边、沈砚川正对面、村民手电照住父子；第9组组首复述这一站位，父子和村民压力连续。",
      "fix_instruction": "无需修复；下一稿仍需保持赵有福挡在赵成武前方的关系。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图占位符或横屏字段；画面风格和负面词为自然短剧交付约束。",
      "fix_instruction": "无需修复；不得加入模板编号、官方模板说明或@图片等占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
