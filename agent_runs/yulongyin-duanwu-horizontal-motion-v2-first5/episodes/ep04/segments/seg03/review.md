{
  "pass": true,
  "summary": "已对照第4集4-3原剧本、横屏生成规则和当前分段分镜逐项审查，车内电话、包工头电话声、炸泉倒废液命令和天天听见后奔向后山均保留，无硬问题。",
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
      "type": "audio_mouth_sync",
      "evidence": "包工头台词明确写为手机外放里的电话声，手机在右前景亮屏，胡永贵只做画面内反应，没有误写成现场人物开口。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "胡永贵原台词“把石壁炸开，再倒五桶废液进去扩宽。”完整保留，并承接包工头说水太少的原因。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "天天在左前景屋檐阴影、皮卡在右中景、车窗半开，电话声和天天反应处于同一横向空间，避免跨空间跳切不清。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "天天台词写为对怀里的水壶说道，嘴唇和水壶同框可见，未虚构画外对话对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首为车内静态状态：车门、驾驶座、方向盘、手机和胡永贵的位置明确，未把爬进车内写入组首。",
      "fix_instruction": "若调整开头，胡永贵挪进驾驶座的过程仍应放在0-2.5秒镜头描述中。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "固定中近景承接听电话反应，轻微推近服务危险命令，摇向车窗缝提示外泄声源，运镜目标明确。",
      "fix_instruction": "不得把车内对白组改成连续无目的横移，以免破坏口型和声源稳定。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾写车窗缝向外漏声，第3组组首写天天在屋檐下与半开车窗同框，听见通话的因果连续。",
      "fix_instruction": "如需改场景，必须保留车窗漏声或手机外放等可听见的载体。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜未混入Seedance模板编号、占位符、广告式字幕或视频延长说明。",
      "fix_instruction": "后续不得加入模板说明或工程控制词。"
    }
  ],
  "issues": [],
  "warnings": []
}
