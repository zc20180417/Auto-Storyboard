{
  "pass": true,
  "summary": "seg01 已对照第21集原剧本、竖屏生成规则和当前草稿完成真实审核，9个分镜组按洞口外、洞内主闸段、洞口外的空间顺序推进，保留关键台词、绳号、闸板、拖人和断绳坍响等剧情节点，无阻断交付的硬问题。",
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
      "evidence": "第1组保留洞口水雾、沈砚川重新系绳、沈小禾“哥，别去了！”，沈母“娘拦不住你。”、“但你得回来。”，沈砚川“我答应你。”，周大柱“我陪你进！”以及沈砚川“外头得有人镇着。”，台词顺序和说话对象与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组14秒承载沈砚川和林知夏围绕下口乱石滩、检修槽、闸右边通下口的7句短对白，约55个有效字，平均约3.9字/秒，并含林知夏反应和沈砚川指向洞口右侧石壁的轻动作，不存在超过6.5字/秒的硬性问题。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "第3组组首写明林知夏手中攥着绳索尾端、加长铁钎靠在洞口石壁旁；6-10秒林知夏把绳扣压紧并交代绳号，12-15秒沈砚川接过加长铁钎入洞，绳索和铁钎归属有可见过渡。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "evidence": "第5组13秒集中呈现压钎、闸板开缝、水压顶入、赵成武惊喊、沈砚川命令再推、洞顶碎石和退离命令，属于同一主闸段连续动作链，未额外塞入无关对白或跨空间事件。"
    },
    {
      "group": "第9组",
      "type": "format",
      "evidence": "第9组标题含cut_id EP21-G09，总时长10秒，4个时间段为0-3、3-5、5-7、7-10秒，镜头数与时间段数一致，人物、场景、道具、组首、组尾、画面风格和负面提示字段完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈砚川和林知夏的所有现场对白均明确为对对方说话，包括“记住下口乱石滩。”、“什么意思？”、“就去那儿等我。”、“你留了后路？”等，没有假对象或对象缺失。",
      "fix_instruction": "若不通过，应补足每句真人对白的真实对象，并避免把台词写成对空气或道具说话。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵成武、赵有福、林知夏、沈砚川、周大柱、沈小禾和沈母在组首均有明确位置和身体朝向；赵成武先走出半步再开口，沈砚川入洞动作发生在组尾，人物可用性清楚。",
      "fix_instruction": "若不通过，应在组首或开口前补足人物位置、朝向、可见状态或入场动作。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第4组全部为洞内现场对白，赵成武和沈砚川均在画面中承担自己的口型，没有心声、旁白、电话音或门外音误写成现场开口。",
      "fix_instruction": "若不通过，应将非现场声音改成画外音、电话音或心声，并写明画面人物嘴唇闭合不做口型。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部沈砚川和赵成武准备从主闸段后退；第6组切回洞口外，组首写明林知夏、周大柱和村民握住从洞口延出的主绳，空间切换与原剧本转场一致，绳索压力连续。",
      "fix_instruction": "若不通过，应补明内外转场、绳索从洞内延到洞外的状态或洞口众人的接续动作。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第7组保留洞口喷出更猛洪水、众人连退、绳子绷直、林知夏喊“拉！”以及众人先拖出呛水的赵成武，未提前写出沈砚川获救或改变剧情结果。",
      "fix_instruction": "若不通过，应恢复原剧本的拖人顺序和人物状态，不能新增沈砚川出洞。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第8组10秒只承载赵成武报告“砚川还在里头！”，沈小禾哭喊，周大柱冲洞口与林知夏阻拦，三个强节拍均在同一洞口空间内完成，未超过片段复杂度预算。",
      "fix_instruction": "若不通过，应拆分赵成武汇报和周大柱冲洞口，或压缩非关键反应。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第9组和全段正文没有Seedance说明词、官方模板、参考图、首尾帧、工程占位符、字幕广告语或批量模板化句式；断绳和坍响均以可见可听动作表达。",
      "fix_instruction": "若不通过，应删除污染词并改为自然可拍的画面、声音和人物反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
