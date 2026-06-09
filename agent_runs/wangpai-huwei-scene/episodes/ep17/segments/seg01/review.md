{
  "pass": true,
  "summary": "seg01已对照第17集剧本完成竖屏分镜审核，关键台词、冷库逃生动作、A17信息和城北仓储站钩子均保留，无阻断问题。",
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
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏OS写明嘴唇闭合，周振邦和秦越均以暗处或门外声音承载，没有误写成现场口型。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周振邦供述拆成两个4秒台词段，分别承载城北旧仓储站坐标和许振南备份、姓林女人接货信息，未超过硬上限。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "推出许知夏、拖赵明海、许知夏伸手呼喊、顾北辰冲出受伤分为4个时间段，未把侧门下落逃生动作压进同一镜。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "赵明海作证、许知夏开启录音、秦越留下城北仓储站威胁、顾北辰和许知夏决定同去城北均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确冷库内许知夏、顾北辰位置和周振邦、赵明海声音来源，第一镜从该静态状态开始。",
      "fix_instruction": "如不通过，应补齐所有在场人物位置和门外声音来源。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "货架金属杆、制冷管外罩和应急阀门从脚边、外罩缝隙到顾北辰握阀门有可见过渡。",
      "fix_instruction": "如不通过，应补充金属杆卡入外罩或阀门被握住的过渡。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "周振邦供述被拆成6-10秒和10-14秒两段，分别承载不同信息，短句前后没有叠加动作。",
      "fix_instruction": "如出现语速超限，应继续缩短单段台词或把秦越威胁保留在下一组。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "秦越砸控制盒、侧门下落、秦越放狠话分三段，每段一个强动作或台词，没有同时塞入拖人逃生。",
      "fix_instruction": "如不通过，应把侧门下落与逃生动作拆到下一组。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组尾部侧门正在下落，秦越在通道；第9组首承接侧门正在下落，赵明海仍在冷库内，位置连续。",
      "fix_instruction": "如不通过，应在第8组尾或第9组首补侧门、赵明海和顾北辰的位置。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定侧墙门缝、顾北辰、封存盒和甩棍，均为本组复杂动作和关键道具风险。",
      "fix_instruction": "如不通过，应删除泛泛词并改成本组人物道具锚点。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图占位符或非短剧模板语气。",
      "fix_instruction": "如出现污染词，应改成自然画面、声音和人物动作描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
