{
  "pass": true,
  "summary": "seg01 已按原剧本保留山路追车、刹车失灵、专业安保身份疑点、盛远签约和楼顶观察者，未发现阻断硬问题。",
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
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS“油管被剪...”明确写为嘴唇闭合的内心声音，许知夏“什么？！”和顾北辰“刹车被人动过手脚”均为现场对白。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "evidence": "右侧黑车贴近、顾北辰说抓稳、拉手刹甩尾、右车翻滚停住分为四段，复杂驾驶动作没有压进一镜。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "许知夏关于第七条的台词约20字给4秒，字秒比约5.0；“盛远要许氏的渠道...”约19字给5秒，低于6.5硬上限。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "evidence": "主要空间是盛远集团门口，对面楼顶作为同一观察关系背景呈现，黑衣人藏在墙后并由望远镜反光暴露。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "两辆黑车压来、左打方向贴崖甩弯、许知夏质问普通司机不该会这些均保留。",
      "fix_instruction": "若不通过，应恢复贴崖甩弯和许知夏质问台词。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "左侧黑车撞击和顾北辰卸力分段表达，许知夏惊呼单独承载，商务车没有同时完成多段主动作。",
      "fix_instruction": "若不通过，应拆出撞击、惊呼和黑车撞护栏。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏对顾北辰质疑训练、顾北辰对许知夏说命大，顾北辰OS闭口承载“难道又是他”。",
      "fix_instruction": "若不通过，应补全对白对象或改为闭口内心声。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "从路肩事件切到盛远会议室是剧本明确新空间，许知夏西装灰尘和手持合同承接前一场。",
      "fix_instruction": "若不通过，应在盛远组首补许知夏入场状态和合同。"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "合同签下、指尖松开、眼睫垂下均为可见动作，没有用不可视心理结论承载后怕。",
      "fix_instruction": "若不通过，应把抽象后怕转成手部和眼神动作。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定黑衣人、望远镜和顾北辰/商务车，数量3条且不禁止原剧本必须发生的望远镜收回。",
      "fix_instruction": "若不通过，应删除泛泛词或与剧情冲突的负面项。"
    }
  ],
  "issues": [],
  "warnings": []
}
