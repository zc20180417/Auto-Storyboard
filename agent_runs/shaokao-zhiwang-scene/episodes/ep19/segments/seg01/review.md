{
  "pass": true,
  "summary": "seg01 已对照第19集原剧本、竖屏生成规则和当前分镜逐组审核，台词、人物关系、空间锁定、时长合同和提示词洁净度均可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中假顾客甲先嚷“谁是老板？”，林小满问“你点单吗？”，再由假顾客甲拍桌控诉吃坏肚子；分镜按同一顺序保留三句台词，并加入路人甲、路人乙的原文反应。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "9-15秒承载许安“昨晚我满桌，路边只坐过熟客。”和假顾客甲“你什么意思，吃坏肚子还不认？”两句，约30个有效字/6秒，约5.0字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组尾部是假顾客甲被问住、路人关注他；第4组组首仍在同一摊前，假顾客甲、林小满、许安、唐婶、路人和韩彪位置延续，随后新客放下菜单、韩彪插话、假顾客甲离开，状态连续。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组明确单一物理空间为街口拐角巷口，组首列出林小满与假顾客甲的画面位置、身体朝向和巷口杂物；8秒短组只承载追丢假顾客的短动作余波。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "案板、肉盘、调料盒和炭火在组首已位于许安身前；7.5-11秒许安口头允许检查，11-15秒许安把案板上的肉盘慢慢摊开，关键食材道具归属和操作过程清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "假顾客甲对摊前众人嚷道，林小满对假顾客甲问道，路人甲对路人乙说道，所有现场开口对白都有真实对象。",
      "fix_instruction": "若不通过，应补足说话对象，避免只写台词或发明非人物对象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组包含唐婶作证、假顾客甲反咬、林小满追问、许安补刀四个连续对峙节拍，均在同一摊前空间内完成，单段台词字秒比均低于6.5，动作没有额外强道具操作。",
      "fix_instruction": "若不通过，应拆分林小满逼问和许安补刀，或压缩非关键反应。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本中的新客退缩、林小满挽留、韩彪假惺惺插话、林小满回怼、许安试探韩彪、韩彪否认、假顾客甲离开均被保留，未新增改变剧情的动作。",
      "fix_instruction": "若不通过，应恢复原台词顺序和假顾客甲离开的动作。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第5组标题总时长8秒，时间段0-4.5秒、4.5-8秒连续且为0.5秒粒度，短组用于街口追丢假顾客这一短动作余波。",
      "fix_instruction": "若不通过，应把短追逃与相邻同空间内容合并，或保留短组并明确只承载动作余波。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "夜市管理甲、夜市管理乙在组首已位于画面右后方人群入口处，证件夹在夜市管理甲手中，二人在说话前通过0-3秒穿过人群停到摊位前，人物可用性完整。",
      "fix_instruction": "若不通过，应在组首或前半段补充管理人员入场位置，不能让其突然开口。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第8组最终正文只有自然分镜字段、画面风格和负面提示词，没有模型说明词、模板编号、参考图占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明词、参考模板措辞和工程占位符，改为可见动作与自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
