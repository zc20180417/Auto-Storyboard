{
  "pass": true,
  "summary": "seg03按阶段处理工程车抵达、工人入场和沈清举文书宣告，外部事件与长台词承载清楚。",
  "checked_groups": ["第4组", "第5组"],
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
      "type": "action_atomicity",
      "evidence": "两辆工程车停下、工人走向院门、工程队长开口、递交文件夹分别为4个时间段，其中停车段为3秒，没有把车辆抵达和队伍入场压进同一镜。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "沈清宣告约47字用8秒，约5.9字/秒，属于偏紧但未超过6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "沈清举法院强制执行裁定书并宣告强制腾房文书、重装房子、私人物品依法清空的核心台词完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "工程队长现场对沈清喊话，声音来源是画面内人物；车辆刹停声作为环境声，不承载台词口型。",
      "fix_instruction": "若不通过，应明确喊话对象或车辆声来源。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为同一外部事件链：车辆停靠、队伍入场、队长喊话、文件夹递交，14秒内阶段清楚且每段主动作单一。",
      "fix_instruction": "若不通过，应拆出车辆停靠或递交文件夹。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾沈清手边接到强制执行文件夹，第5组首沈清持有从文件夹取出的裁定书，工程队长仍拿文件夹，过渡可理解。",
      "fix_instruction": "若不通过，应在第4组尾补沈清取出裁定书的动作。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "法院强制执行裁定书在第5组从组首到宣读再到组尾始终由沈清持有；强制执行文件夹在工程队长手中。",
      "fix_instruction": "若不通过，应补充裁定书和文件夹的归属。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第4组集中在周家院落院门口及门外道路同一入场空间，车辆、法警、工人、院内人物均有初始位置。",
      "fix_instruction": "若不通过，应拆分为门外车辆组和院内入场组。"
    },
    {
      "group": "第5组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定法院强制执行裁定书、沈清、工人们、法警、周美娟和赵强热豆浆碗，共4条，未使用泛泛占位词。",
      "fix_instruction": "若不通过，应删除无锚点的通用禁止项。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "沈清长句接近偏快区间。",
      "evidence": "约47字/8秒，约5.9字/秒，低于6.5硬上限但接近P1提醒范围。",
      "fix": "若后续演员口型显快，可把2-10秒扩到2-10.5秒并压缩末尾反应，但当前不阻断。"
    }
  ]
}
