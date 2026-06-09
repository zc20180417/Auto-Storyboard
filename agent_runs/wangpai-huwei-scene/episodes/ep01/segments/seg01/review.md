{
  "pass": true,
  "summary": "seg01 已按原剧本保留许振南临终托付、会议室危机、门口出发、赵明海通话和山路逼车，未发现阻断硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组"],
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
      "type": "script_fidelity",
      "evidence": "保留许振南交代保险柜、塞钥匙、提到当年事和心电长音；保险柜钥匙从许振南掌心转移到顾北辰掌心，因果清楚。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "许知夏命令台词约26个有效字放在3-9秒共6秒，字秒比约4.3；顾北辰回应约4字放在3秒内，均低于6.5硬上限。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "evidence": "赵明海现场对手机低声说话，陌生男声明确来自手机听筒，没有让陌生男声出现在窗边开口。"
    },
    {
      "group": "第11组",
      "type": "action_atomicity",
      "evidence": "黑车压近、商务车晃动、许知夏惊问、顾北辰提醒合同拿稳分成四个时间段，没有把逼车和台词压进同一主动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "董事甲、许知夏、赵明海三句会议室关键台词均保留，投影股价暴跌和财务章位置也被写入。",
      "fix_instruction": "若不通过，应恢复缺失台词或财务章/投影等关键道具状态。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "顾北辰在组首位于门外，0-3秒推门探头后再发言；许知夏、董事甲、赵明海均在组首有明确位置。",
      "fix_instruction": "若不通过，应先写入场动作或在组首提供人物位置。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾部许知夏持合同和补充资料、顾北辰在驾驶位；第7组组首继承相同位置和豆浆空杯状态。",
      "fix_instruction": "若不通过，应在第6组尾或第7组首补充车门、资料和驾驶位状态。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "主要物理空间锁定在盘山路商务车内，后方黑车通过后视镜和车外道路呈现，没有跨到新空间。",
      "fix_instruction": "若不通过，应拆出车外追踪组或明确后视镜视角。"
    },
    {
      "group": "第12组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒内只承载急弯逼近、许知夏问句和顾北辰坐稳回应，作为片尾危险悬念，未塞入实际甩尾动作。",
      "fix_instruction": "若不通过，应把急弯动作留到下一集，或进一步压缩为短承接组。"
    },
    {
      "group": "第11组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定合同文件、黑车、顾北辰、许知夏扶手等本组要素，数量4条且不与剧情冲突。",
      "fix_instruction": "若不通过，应删除泛泛词，换成本组人物、车辆和合同状态锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
