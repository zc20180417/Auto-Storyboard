{
  "pass": true,
  "summary": "seg01两组保留天天跌落、水壶摔裂、云宝暴露和天天护友被踹飞的剧情，横屏站位与时间轴可生产。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本的天天踩空滚落、痛呼“哎哟”、水壶砸青苔岩石、云宝随水落出、打手乙台词均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "组首把云宝和水壶锁在右前景，天天在云宝前方，打手乙和打手丙从左侧逼近，踹飞方向为左到右，符合横屏调度。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "天天17字台词用3.5秒承载，约4.9字/秒；打手丙10字台词用3秒承载，约3.3字/秒但伴随踏前威胁动作，不构成硬错误。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从天天身侧脱手，砸到右前景岩石，盖子飞开后云宝随半壶水落在泥草中，道具轨迹完整。",
      "fix_instruction": "若不通过，应补充水壶从手中到岩石再到摔开的位置过渡。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "同一坡底空间中打手保持画面左侧压近，天天和云宝在右侧，未发生无过渡换边。",
      "fix_instruction": "若不通过，应在组尾或组首补充明确换边动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载天天护住云宝、打手丙骂人、踹飞天天三个强节拍，14秒内可表演。",
      "fix_instruction": "若不通过，应拆出踹飞动作或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
