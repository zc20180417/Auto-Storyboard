{
  "pass": true,
  "summary": "ep04 分镜保留办公室预警、晚宴试探、后台U盘外接信号和大屏将亮未亮的悬念，台词、心声、空间连续和道具状态均通过审核。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "type": "dialogue_pacing",
      "evidence": "助理提醒约35字给6秒，约5.8字/秒，属于信息密集提醒但未超过6.5硬上限；许知夏OS约25字给3秒偏快但仍在硬上限内。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "工作人员在第6组8-10秒明确把U盘插入主控台，第7组组首和组尾继续锚定U盘仍插在设备上。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "evidence": "顾北辰到后台入口、黑衣人抬手阻拦、顾北辰松袖口、顾北辰放话分成四个连续时间段，没有把入场、阻挡和威胁压成一个动作。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "许知夏台上察觉异常、大屏跳闪、全场看向大屏、周振邦含笑和许知夏OS均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏警惕OS写明嘴唇闭合不做口型，助理现场提醒写明对许知夏提醒。",
      "fix_instruction": "若OS改成开口对白，应恢复为内心声并保留闭口说明。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏必须上台和顾北辰手势提醒均明确写为对对方说道，没有遗漏对话对象。",
      "fix_instruction": "若删去对话对象，应补回许知夏/顾北辰。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组包含周振邦压低声、离开、顾北辰借取酒观察、工作人员插U盘、顾北辰OS五个节拍；前四个动作短，主信息在U盘和OS，15秒内可执行。",
      "fix_instruction": "若增加肢体冲突或新台词，应拆出后台入口前置组。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾U盘插在主控台，第7组组首继续写工作人员在主控台旁且U盘插在设备上，大屏缓冲因果连续。",
      "fix_instruction": "若删除U盘锚定，应在第7组组首补回设备状态。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "后台入口单独成组，组首列出顾北辰、两名黑衣人、后台门和方向，人物在行动前均可用。",
      "fix_instruction": "若顾北辰直接进入后台，应补过黑衣人让开或被突破的可见动作。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定许知夏OS、大屏完整播放、顾北辰位置和周振邦在场四个本组风险，没有通用负面词。",
      "fix_instruction": "若大屏需要播放完整画面，应另起下一组承载，不要与本组禁止项矛盾。"
    },
    {
      "group": "第5组",
      "type": "format",
      "result": "pass",
      "evidence": "第5组标题含EP04-G05 cut_id，0-14秒时间连续，镜头数4个与实际时间段一致，结构字段完整。",
      "fix_instruction": "若调整台词时长，应同步修标题总时长和镜头数。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全篇未出现Seedance、参考模板、@图片、自动分镜或首尾帧等工程词，均为自然分镜正文。",
      "fix_instruction": "若出现模型或模板说明词，应改写成可见画面描述。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "助理提醒和许知夏OS信息密度略高。",
      "evidence": "助理提醒约35字/6秒约5.8字每秒；许知夏OS约25字/3秒约6.25字每秒，未超过硬上限但偏快。",
      "fix": "如后续扩展办公室段，可把许知夏OS单独给到4秒。"
    }
  ]
}
