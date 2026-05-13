{
  "pass": true,
  "summary": "seg01 已对照原剧本和横屏规则审查，第1至第3组保留喂食、命名与水雾心声，横屏空间、运镜、道具状态链和台词承载可交付。",
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
      "evidence": "第1组把房门放在画面左侧背景、水壶放在右侧前景，天天从门边到小桌的移动路线清楚，横屏左右空间成立。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组白馒头从天天手中被掰碎、丢入壶口、沉向壶底并被小龙吞下，关键道具路径连续。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组心声写为画外心声，明确天天嘴唇闭合不做口型，没有把 OS 写成现场开口。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "evidence": "第3组10.5-14秒运镜从右侧壶口摇向左侧天天脸颊，服务水雾来源、路径和落点。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写房门、天天、小桌和水壶的第一帧静态位置，没有把反锁或移动过程放入组首。",
      "fix_instruction": "若后续改稿出现走到、拿起、放下等过程动词，应移入时间段镜头描述。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留掰碎馒头、丢进水壶、小龙探头吞馒头渣、打嗝吐水泡等原剧本动作顺序。",
      "fix_instruction": "若不通过，应恢复原剧本动作顺序，不新增改变剧情的喂食方式。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "4-8秒承载命名台词约20字，约5字/秒且有微笑与云宝抬头反应；10.5-14秒心声配合水雾动作，整体可表演。",
      "fix_instruction": "若字秒比进一步上升，应拆分台词或延长对应时间段。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现参考图、模板编号、Seedance执行提示补充、组间承接或本镜估算时长等生产备注字段。",
      "fix_instruction": "若出现工程备注，应删除并改成自然画面、台词或运镜描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
