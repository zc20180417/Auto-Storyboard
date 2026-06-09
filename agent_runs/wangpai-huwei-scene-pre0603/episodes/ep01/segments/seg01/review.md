{
  "pass": true,
  "summary": "seg01 已按原剧本完成病房托付、会议室危机、门口出发、山路逼车十组分镜，未发现阻断交付的 hard issue。",
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
      "type": "dialogue_pacing",
      "evidence": "许知夏命令顾北辰的长句约31字分配6秒，约5.2字/秒，属于冷声命令的合理情绪对白速度；顾北辰回应短句3秒内完成，没有超过6.5字/秒。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "秦越只通过手机电话音出现，分镜明确赵明海嘴唇闭合、手机听筒传出秦越声音，未让赵明海承担秦越口型。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "黑车压近被拆为许知夏询问、顾北辰回应、黑车加速压近、许知夏抓扶手发问四个连续时间段，没有把逼车和对白压进同一主动作镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留许振南托付许氏危险、知夏需要可靠的人、保险柜钥匙、当年事没那么简单和心电图长音等关键剧情。",
      "fix_instruction": "若不通过，应恢复被删改的托付台词和钥匙交接动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "董事甲对许知夏、许知夏对董事甲、赵明海对许知夏的对白对象均明确，未出现假对象。",
      "fix_instruction": "若不通过，应把每句真人对白改成明确的A对B说道。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "盛远合同文件从会议室带到集团门口，并与助理递上的资料一同被许知夏持有，未在上车前消失。",
      "fix_instruction": "若不通过，应补充许知夏拿着合同和资料上车的可见状态。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组固定在盘山路商务车车内，黑车通过后视镜和车外道路出现，未跨到其他主要物理空间。",
      "fix_instruction": "若不通过，应拆出车外追车镜头或明确屏幕/后视镜画面来源。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "急弯前节拍为顾北辰提醒、许知夏追问、急弯逼近、坐稳收尾，4个强节拍共12秒，合同和扶手状态连续。",
      "fix_instruction": "若不通过，应拆分急弯逼近和坐稳台词，避免同段塞入多主动作。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定顾北辰、许知夏、盛远合同、黑车和急弯，共4项，未使用泛泛模板词。",
      "fix_instruction": "若不通过，应删除泛泛项并改成本组具体人物、道具或场景风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
