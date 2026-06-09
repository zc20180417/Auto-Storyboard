{
  "pass": true,
  "summary": "第02集已完成真实审核，山路脱险、盛远签约和门口发现楼顶观察者均按原剧本分组，未发现阻断交付的 hard issue。",
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "许知夏质问约19字分配5秒，约3.8字/秒并伴随惊惧抓扶手表演；顾北辰回应约11字分配4秒，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS被写成内心声，分镜明确嘴唇闭合不做口型；秦越未在本集该段出现，未混入口型。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "右侧黑车逼崖、顾北辰口令、拉手刹急打方向分为三个时间段，未把连续弯、口令和甩尾全部塞进同一镜。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "许知夏点住第七条，要求付款改成分段结算；盛远代表迟疑后与助理交换眼色并点头，合同谈判因果与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "急弯动作拆成黑车压近、方向盘左打甩弯、许知夏质问、顾北辰回应四段，15秒内强节拍清楚。",
      "fix_instruction": "若不通过，应继续拆分甩弯动作或减少同段对白负载。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "挡杆从D挡连推至2挡、手刹仍在中央位置且许知夏未触碰，为后续顾北辰拉手刹建立连续道具状态。",
      "fix_instruction": "若不通过，应补充挡杆和手刹归属，避免许知夏抢动作。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部左侧黑车撞护栏冒烟，第5组组首只保留右侧黑车继续逼近，追击车辆状态不矛盾。",
      "fix_instruction": "若不通过，应在组尾或组首说明左侧黑车退出追击。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏对顾北辰质疑其专业安保训练，顾北辰对许知夏回应命大，现场对白对象明确。",
      "fix_instruction": "若不通过，应把所有真人对白补成A对B说道。"
    },
    {
      "group": "第12组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第12组锁定为盛远集团门口及对面楼顶视线范围，黑衣人只在远处楼顶墙后和望远镜反光中可见，未直接参与门口动作。",
      "fix_instruction": "若不通过，应拆出楼顶观察镜头或明确为远处观察视线。"
    },
    {
      "group": "第12组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文未出现模型说明词、模板编号、官方占位符、参考图或视频延长等工程词，内心声与低声自语均为自然画面描述。",
      "fix_instruction": "若不通过，应删除工程词并改成可见可听的短剧画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
