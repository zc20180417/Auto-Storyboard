{
  "pass": true,
  "summary": "seg01保留了冷库探查、三年前转移线索、秦越设局、坐标暴露、护住照片和黑暗威胁的原剧本信息，连续事件链合并后未出现台词错漏、空间跳变或低密度长组。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本的“被拿走了”“不是今晚拿的。三年前就动过。”以及许父VO“这份东西，不能进许氏，也不能落到启元手里。”均保留，闪回明确标注为雨夜仓库外，没有把回忆误写成现实冷库。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "赵明海约33字台词给6秒，约5.5字/秒；周振邦“闭嘴！”给2秒并带推搡动作；许知夏约20字质问给5秒，约4字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "evidence": "门外秦越解释、周振邦扑门、周振邦质问、秦越弃子台词、顾北辰命令找阀属于同一冷库落锁后的连续陷阱事件链，分成5个清楚时间段，总时长15秒，没有把每个反应机械拆成独立长组。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏OS“不是柜号，是坐标”明确写嘴唇闭合不做口型；现场喊话“顾北辰！A17底下有坐标...”写成许知夏对顾北辰急促喊，声音来源正确。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "手下扑向A17、顾北辰撞开手下、一拳击中咽喉、肘击同时许知夏拍照、备用电源切断按顺序分段；顾北辰是主保护动作执行者，非主动作人物未抢戏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定冷库外通道、门锁、温控灯、顾北辰蹲位和许知夏阴影站位，第一段从门锁检查开始，没有把门内动作提前写入组首。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏心声明确写嘴唇闭合不做口型，A17打开和旧封条揭示与原剧本顺序一致。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“三年前就动过”的不可见判断由顾北辰摸到封条边缘凹凸承载，许父转移备份用雨夜仓库外闪回和银色封存盒可视化。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越、周振邦、赵明海和手下在组首被放置于背景货架阴影后方，本组后半段再通过鼓掌声和走出完成揭示。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部是许知夏与秦越对峙、顾北辰握封条；第6组组首继承同一冷库站位，并把冷库门与温控屏加入可操作位置，落锁动作有明确过渡。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒组具备足够台词容量、落锁后周振邦反应动作链、秦越弃子关系变化和顾北辰救场转向，符合12-15秒长组准入。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "A17空盒从第2组打开后持续存在，第8组明确坐标刻痕位于盒底，许知夏从墙面摸索转向盒底再喊给顾北辰，没有道具跳变。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第10组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第10组为断电后的短动作余波和片尾威胁，9秒内承载握手、顾北辰安抚、许知夏确认目标、秦越VO压迫，属于允许的6-9秒短承接。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组-第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文未出现自然收尾、不强制静止、Seedance自动、参考模板、@占位符或模板化批量描述；组尾均为具体连续性状态。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组-第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "复杂动作、关键道具和保护站位组均有2-4条锚定本组人物、A17、封条、坐标、冷库门或温控屏的禁止项，没有泛泛复制同一串负面词。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
