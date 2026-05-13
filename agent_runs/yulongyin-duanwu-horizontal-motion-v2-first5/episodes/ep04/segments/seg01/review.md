{
  "pass": true,
  "summary": "已对照第4集4-1原剧本、横屏生成规则和当前分段分镜逐项审查，三组保留抢水、洗车、质问、推倒和水壶险些摔碎的因果链，无硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "evidence": "第1组用送水车右后景、队列横贯中景、天天左后景队尾、胡永贵左前景皮卡旁建立缺水队列和压迫来源，符合16:9横向关系要求。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "村民甲16个左右有效字安排在6-10秒，胡永贵约21个有效字安排在10-14秒，均未超过6.5字/秒硬上限，且说话对象明确为胡永贵和村民甲。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "水壶从组首的天天怀里，到9-12秒滑出半寸又被护住，组尾仍归天天；水管由胡永贵握持并引发抢夺，关键道具归属清楚。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "evidence": "第3组有固定机位承载天天台词和推倒结果，横向跟拍只服务天天从队尾到水管的路线，轻微推近落在水壶险些摔碎的关键点。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写送水车、队列、天天、胡永贵、村民甲的静态位置和视线，没有把走来、进入、抢夺等过程动作写进空间锁定。",
      "fix_instruction": "若后续修改，应继续把胡永贵压进队伍等过程动作放在时间段镜头描述中。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留胡永贵插队用水管洗皮卡、村民甲质问、胡永贵以付款为由回怼的原台词和顺序。",
      "fix_instruction": "若需压缩，只能压缩水花和村民退让的过程，不得删改两句关键对白。"
    },
    {
      "group": "第3组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "天天从左后景冲向中右水管，胡永贵在右侧推开她，组尾天天落在左前景护壶，方向和因果连续。",
      "fix_instruction": "若调整动作，需保留天天左向右抢水、被推回左前景的屏幕方向。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、官方占位符、参考图说明、视频延长或自动分镜等工程说明词。",
      "fix_instruction": "后续不得加入模板编号、@图片占位符或非短剧模板语气。"
    }
  ],
  "issues": [],
  "warnings": []
}
