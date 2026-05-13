{
  "pass": true,
  "reviewer_source": "storyboard-horizontal-reviewer",
  "summary": "已对照第4集4-1原剧本和横屏生成规则审核，四组保留送水车排队、胡永贵插队洗车、村民质问、天天抢水管并被推倒的因果链，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "送水车在左后方，队伍横向排到右后方，天天在队尾，胡永贵和皮卡压在右前方，第一帧空间锁定清楚呈现左右权力差。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "村民甲质问放在6.5-10.5秒，胡永贵反讽放在10.5-14秒，两句均有固定机位承载口型，字秒比未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "水管在组首由胡永贵控制，5.5-11秒天天从队尾冲到中央抓住喷头，组尾两人的手同时卡在喷头附近，道具转移有可见过渡。"
    },
    {
      "group": "第4组",
      "type": "camera_motion",
      "evidence": "0-3秒固定双人中景承载推搡，3-6.5秒手持轻晃跟随跌落，6.5-10秒推近水壶，运镜围绕推倒和水壶险些摔碎的结果递进。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "胡永贵从右前方压向左侧队伍，天天始终在右后方队尾，后续冲向水管的路线与该站位连续。",
      "fix_instruction": "无需修改；若后续换边，需要在组尾或下一组镜头描述中给出可见过渡。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留胡永贵拿水洗车、村民甲质问、胡永贵以出钱包车回应的台词和先后顺序，没有新增改变剧情的动作。",
      "fix_instruction": "无需修改；若压缩台词，必须保留原句和说话对象。"
    },
    {
      "group": "第3组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "本组从天天看见水被浪费的情绪动作，推进到她喊话，再到冲向水管的行动，信息链清楚。",
      "fix_instruction": "无需修改；若调整节奏，应继续保留焦急、喊话、抢水管三个节点。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写天天和胡永贵已在中央前景争夺水管、水壶贴在左臂弯、村民和皮卡位置，没有把推倒过程写入第一帧锁定。",
      "fix_instruction": "无需修改；后续动作仍应放在时间段镜头描述中。"
    }
  ],
  "issues": [],
  "warnings": []
}
