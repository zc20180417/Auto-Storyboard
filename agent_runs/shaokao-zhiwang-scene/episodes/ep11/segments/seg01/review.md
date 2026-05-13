{
  "pass": true,
  "summary": "seg01 分镜完整覆盖第11集街口抢客、唐婶回呛、韩彪口味翻车和客人回流许安的剧情链，5组均符合竖屏分镜格式、台词承载、空间锁定和时长规则。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "原剧本中韩彪摆满大桌、许安照常起炉、林小满说“他这是把整条街都包了”、许安回“热闹归他，味归我”、韩彪和阿顺吆喝、路人甲心动，均按原顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-4.5秒唐婶约11字台词并含走到通道动作；4.5-8.5秒韩彪与唐婶约22字情绪交锋，约5.5字/秒；8.5-13秒林小满和许安约14字对白并含上串与看火动作，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首明确韩彪店门口烧烤桌区、后厨门帘、桌面烤串，以及韩彪、阿顺、唐婶、路人乙、路人丙的位置和身体朝向；本组所有发言人物均已可见或拥有明确声音对象。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第4组尾部写明路人乙扶住餐盘准备起身，第5组组首继续让路人乙在韩彪桌边手扶餐盘，随后0-4秒端盘起身，动作衔接清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林小满对许安说、许安对林小满说、韩彪对众人喊、阿顺朝路人甲方向喊、路人甲对同伴说，现场对白均有真实对象。",
      "fix_instruction": "若不通过，应补齐每句现场对白的说话对象，避免对空气或道具说话。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载唐婶介入、韩彪回怼、许安稳住林小满三个连续同场冲突节拍，总时长13秒，没有叠加关键道具操作或跨空间强事件。",
      "fix_instruction": "若不通过，应拆开唐婶回呛和许安稳住林小满两个节拍。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "路人乙说咸、路人丙说苦、韩彪问谁烤的、阿顺解释桌太多火顾不过来、唐婶指出味还是对面正，原剧本关键台词和因果均保留。",
      "fix_instruction": "若不通过，应恢复原剧本台词顺序，不新增韩彪主动认错或许安插手等剧情。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "0-3.5秒韩彪约5字台词，3.5-8秒唐婶约20字情绪台词，约4.4字/秒，略低但有当众抬声和对峙动作支撑；8-10秒为无台词群体反应，时长合理。",
      "fix_instruction": "若不通过，应压缩无台词反应或将唐婶台词保持在4-5秒内。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "餐盘从第4组路人乙手边，到第5组组首路人乙手扶餐盘边缘，再到0-4秒端起餐盘、11-15秒端到许安小桌边，关键道具归属变化有可见过渡。",
      "fix_instruction": "若不通过，应补充端起、放下或递交餐盘的可见动作。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、官方模板标题、@图片/@视频/@音频、参考模板、自动正反打、Seedance 可等污染词，也未使用禁用模板化句式。",
      "fix_instruction": "若不通过，应删除工程或模板说明，改为自然画面动作和声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
