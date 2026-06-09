{
  "pass": true,
  "summary": "ep22 单段分镜完整保留许知夏以沈曼弟弟病情破防、转院申请单换取权限协助、沈曼决定配合并向秦越职业化汇报的剧情，未发现阻断交付的 hard issue。",
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "5-13秒承载沈曼短问和许知夏医院缴费单信息，约37个有效字分配8秒，字秒比约4.6，低于6.5硬上限。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "evidence": "沈曼左右看、拉许知夏到角落、沈曼低声追问、许知夏摊开秦越相关指控分为三段，拉人动作和长台词没有压在同一时间段。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "7-11秒许知夏对沈曼说“周振邦也这么信他的。现在周振邦在警察局录口供。”，有效字数21，时长4秒，字秒比约5.3，已避开过快硬问题。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "转院申请单由许知夏从包里拿出并展开，红章可见，第8组再由许知夏收回包边，道具归属和状态连续。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "沈曼对内线电话现场开口，电话里的秦越不在画面中也没有被赋予口型；对话来源为内线电话，画面载体清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确玻璃门、访客登记台、沈曼、许知夏、林元的位置和朝向，许知夏与林元进入前台区的第一段动作与大厅入口状态兼容。",
      "fix_instruction": "若不通过，应补充三人的画面位置、身体朝向或前台登记台位置。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许知夏明确说查的是秦越，并连续点出晚宴U盘和冷库温控，保留原剧本对沈曼被迫执行秦越命令的指控逻辑。",
      "fix_instruction": "若不通过，应恢复秦越、U盘、冷库温控三项原剧本信息。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载沈曼辩解、许知夏反问、沈曼眼眶泛红三个节拍，人物仍在大厅角落，没有加入额外道具或跨场景动作。",
      "fix_instruction": "若不通过，应拆出沈曼情绪反应或压缩非关键停顿。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "转院申请单在0-2秒从许知夏包里拿出，2-12秒展开给沈曼看，组尾仍在许知夏手中，后续第8组收回包边，过渡完整。",
      "fix_instruction": "若不通过，应写清申请单从包里拿出、展开、收回的可见动作。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈曼“我帮你”和“帮我转告顾北辰……”均明确对许知夏低声说道，许知夏也明确对沈曼回应，没有假对象对白。",
      "fix_instruction": "若不通过，应为每句现场对白补真实对话对象。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定沈曼、许知夏、林元、秦越和转院申请单，数量4个，都是本组具体剧情风险，没有泛泛模板词。",
      "fix_instruction": "若不通过，应删掉泛泛词，改成本组具体人物、电话、申请单或前台动作。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组许知夏把申请单收回包边，第9组组首明确申请单已收在包内；许知夏和林元离开角落，沈曼回前台拿电话，动作连续。",
      "fix_instruction": "若不通过，应在第8组尾或第9组首补申请单归属、沈曼回前台和内线电话位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
