{
  "pass": true,
  "summary": "第05集分镜完整保留晚宴黑屏、顾北辰夺证、监控反转、赵明海暴露和许知夏定性犯罪的剧情，格式、时长、对白指向和音画分离均通过。",
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "原剧本中许知夏从容宣布设备故障并展示真正有价值内容，分镜保留原台词，并用9-15秒呈现屏幕重新亮起和工作人员插U盘、周氏助理递卡的监控画面。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "顾北辰对周振邦的关键台词约43字，3-11秒共8秒承载，约5.4字/秒，属于情绪压迫对白可接受范围，且没有额外硬塞动作。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "该组场景栏明确为慈善晚宴大厅、回忆闪回走廊，8.5-11.5秒标明回忆闪回，回到大厅后手机外放作为声音来源，未把走廊误写为同一现实空间。"
    },
    {
      "group": "第10组",
      "type": "audio_mouth_sync",
      "evidence": "周振邦OS和顾北辰OS均写明嘴唇闭合不做口型，现场画面只表现他们的视线和站位，没有把内心声写成现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏OS在8-12秒写明嘴唇闭合不做口型；周振邦现场对白有明确对象许知夏。",
      "fix_instruction": "若不通过，应把OS改为内心声闭口，现场对白写明说话对象。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "黑衣人推搡、顾北辰扣腕、抬膝压墙、处理第二名黑衣人分成4个时间段，每段主动作清楚，非主动作人物未抢动作。",
      "fix_instruction": "若不通过，应继续拆分冲撞、压墙、摔倒等动作。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "U盘在组首插于主控台，2-5秒由顾北辰拔下并握在掌心，组尾继续由顾北辰持有，状态连续。",
      "fix_instruction": "若不通过，应补充U盘从接口离开并归属顾北辰的可见过渡。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载顾北辰示意、许知夏一段公开回应、屏幕重亮和监控画面四个节拍，总时长15秒，屏幕画面单独占3秒，未压缩外部事件。",
      "fix_instruction": "若不通过，应将屏幕证据展示拆成独立组。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组组尾赵明海仍在人群边缘，第7组组首复述他位于人群右后方并朝出口，随后才后退，连续性成立。",
      "fix_instruction": "若不通过，应在第6组尾或第7组首补赵明海所在位置。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第10组视频禁止项锚定顾北辰手机和U盘、周振邦内心声、许知夏舞台、赵明海出口前，4项均为本组具体风险，没有泛泛占位。",
      "fix_instruction": "若不通过，应删除泛化负面词并改成本组人物道具锚点。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第9组只包含自然短剧分镜正文，没有Seedance说明、模板编号、参考图、首尾帧或广告式表达。",
      "fix_instruction": "若不通过，应删除模型说明词和模板化说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
