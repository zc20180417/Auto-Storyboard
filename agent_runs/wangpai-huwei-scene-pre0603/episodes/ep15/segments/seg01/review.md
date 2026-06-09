{
  "pass": true,
  "summary": "第15集已完成真实审核，周氏办公室供出A17、安全屋收到短信、两人同行和秦越监听收尾均符合竖屏 scene 分镜合同，未发现阻断交付的 hard issue。",
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
      "evidence": "赵明海说明当年偷听和地下档案室的一句约31个有效字，分配8-15秒共7秒，约4.4字/秒；周振邦单字命令分配3秒并伴随压近半步，没有超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "秦越台词处理为侧门外传来的声音，正文写明秦越本人不在画面内，周振邦和赵明海看向门缝，未让画面人物替秦越做口型。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "安全屋中手机、耳机和红色监控灯归属清楚：许知夏拿起手机和耳机离开，组尾明确桌面不再有手机，桌下红灯仍闪烁。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "秦越办公室作为独立短承接组处理，没有把安全屋和启元办公室硬塞进同一现实空间；监听红点和A17标记作为屏幕道具承接前一组红灯。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "周振邦摔碎手机、抱怨秦越让自己挨刀、赵明海携护照机票进入和周振邦讥讽赵副总跑得快均按原剧本顺序保留。",
      "fix_instruction": "若不通过，应恢复手机碎裂、新闻推送、护照机票和周振邦原台词顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵明海对周振邦说明自己替他们办事和备份位置，周振邦对赵明海说说，所有真人对白都有真实对话对象。",
      "fix_instruction": "若不通过，应逐句补足周振邦或赵明海作为真实对话对象，不能写成对空气或道具说话。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载赵明海补充A17和秦越门外警告两个信息节拍，再用赵明海扶桌反应收尾，未把秦越入场、追逐或额外强动作塞入15秒内。",
      "fix_instruction": "若不通过，应拆出秦越声音或赵明海反应，避免同组加入额外入场动作。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "新场景安全屋重新锁定桌子、手机、文件袋和两人站位；短信内容A17柜今晚十二点与原剧本一致，组尾手机仍在桌面供第5组承接。",
      "fix_instruction": "若不通过，应在第4组组尾或第5组组首补足手机位置和短信状态。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "许知夏拿耳机回应、顾北辰成交、两人离开和红色监控灯显露分别占用独立时间段，未让关灯、离开、拿手机和监控红灯同时挤在一个镜头里。",
      "fix_instruction": "若不通过，应拆分离开动作和红灯揭示，保证手机与耳机归属清楚。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文未出现Seedance说明词、模板编号、参考图、官方占位符或自动分镜等工程词，秦越低笑被写成自然画面。",
      "fix_instruction": "若不通过，应删除所有工程说明并改写为秦越办公室里的可见动作和声音。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "复杂道具连续组的视频禁止项锚定许知夏手机、红色监控灯、顾北辰和房门，数量4个且没有泛泛的画面混乱或人物错误。",
      "fix_instruction": "若不通过，应删除泛泛负面词，改成本组人物、道具和房门状态的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
