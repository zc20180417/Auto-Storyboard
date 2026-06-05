{
  "pass": true,
  "summary": "seg04 保留宾客掌声祝福、沈清与周桂兰碰杯和母女温情收尾，未发现 hard issue。",
  "checked_groups": ["第1组", "第2组"],
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
      "type": "script_fidelity",
      "evidence": "原剧本中沉默三秒后掌声、宾客甲赞叹和宾客乙举杯祝福均保留，台词未改写。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "离婚协议书从沈清手中放到宴会桌，红酒杯从桌上到母女碰杯，再到周桂兰手中，转移过程清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清约24字用4秒约6字/秒；周桂兰约18字用4秒约4.5字/秒并有含泪慢语动作，未超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "沉默转掌声、宾客甲赞叹、宾客乙举杯祝福构成温情收束的连续事件链，11秒不低密度撑时长。",
      "fix_instruction": "若不通过，应压缩掌声或合并宾客祝福。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "放下协议端酒、碰杯、沈清说话、周桂兰回应分成四段，每段只有一个主动作或对白节拍。",
      "fix_instruction": "若不通过，应拆开递杯、碰杯和对白。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周桂兰说，周桂兰对沈清说，宾客甲和宾客乙都明确朝母女方向发言，不存在假对象。",
      "fix_instruction": "若不通过，应补明真实说话对象。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾保留宾客鼓掌、沈清周桂兰站在中央偏左；第2组组首继承母女位置并让掌声渐弱。",
      "fix_instruction": "若不通过，应补充掌声状态和母女站位。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考官方模板、@图片占位、广告字卡或模型说明词。",
      "fix_instruction": "若不通过，应删除污染词并回到自然短剧分镜表述。"
    }
  ],
  "issues": [],
  "warnings": []
}
