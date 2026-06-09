{
  "pass": true,
  "summary": "ep11 seg01 已对照原剧本和竖屏生成规则审核，7组均保留关键台词、道具和空间递进，没有阻断生产的硬问题。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "许知夏长台词“我已经发给法务和媒体定时投递……全网公开。”安排在5-15秒共10秒，约64字，字秒比约6.4，未超过6.5硬上限；前置拿手机动作单独占2.5秒，没有挤压口型。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏以耳机VO出现，8-12秒明确顾北辰嘴唇闭合，只做听见后的扫视反应；12-15秒才由顾北辰现场低声回复许知夏。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "会议室内铁门、旧档案柜、两名黑衣人、搭档母亲被封口反绑、周振邦揭出顾北辰身份、顾北辰提出放人换硬盘、周振邦追问真货均按原剧本顺序保留。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "黑色硬盘包由顾北辰手中打开，硬盘先放到会议桌并推向周振邦一侧，再由黑衣人拿起插入电脑，进度条从1%到5%，道具转移有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只锁定清晨安全屋、桌面两只硬盘、顾北辰和许知夏的位置与朝向，第一段从顾北辰换芯开始，没有把过程动作写进组首。",
      "fix_instruction": "若不通过，应把组首改为静态结果状态，把拆盘、装芯片等动作移入时间段。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "陌生男声VO在12-15秒作为门外局势声出现，并写明画面中的许知夏和顾北辰嘴唇闭合，不承载该句口型。",
      "fix_instruction": "若不通过，应明确VO来源并写闭口，不能让现场人物开口说秦越旁白。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "车旁叮嘱司机、司机点头、顾北辰进大厅、许知夏耳机VO、顾北辰回复分成5个连续时间段，外部移动和耳机对话没有压在同一镜头。",
      "fix_instruction": "若不通过，应继续拆分进门动作和耳机对话，或减少非关键扫视。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "前台明确对顾北辰说道“顾先生，周总在会议室等您。”；顾北辰OS写明嘴唇闭合不做口型，没有伪装成现场对白。",
      "fix_instruction": "若不通过，应补足真实对话对象，OS必须闭口承载。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "铁门打开、看清人质、人质状态展示、周振邦台词、顾北辰回应、周振邦追问按阶段拆开；黑衣人只押人和站位，没有抢顾北辰或周振邦的主动作。",
      "fix_instruction": "若不通过，应拆开入场、人质揭示和对峙台词，避免一镜多主动作。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项为硬盘未插入电脑、进度条直接满格、搭档母亲离开椅子、顾北辰抢回硬盘，均锚定本组道具和人物，数量4个且不与正文矛盾。",
      "fix_instruction": "若不通过，应删除泛泛负面词，改成本组具体人物、硬盘、电脑或人质状态错误。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、模板编号、参考图、自动正反打、@图片、固定尾部风格或调试标记，均为自然中文分镜。",
      "fix_instruction": "若不通过，应删除模型说明词和工程占位符，只保留自然画面、声音和光影描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
