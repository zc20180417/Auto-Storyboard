{
  "pass": true,
  "summary": "seg01保留授权书质问、周建国否认和周桂兰识破手机号变更，格式、时间和连续性通过。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "原剧本中沈清进入并把伪造授权委托书拍到茶几上，分镜0-4.5秒保留该动作，4.5-7.5秒保留“周叔，你不是说对这笔钱不知情吗？”"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清指证台词约28字承载5秒，约5.6字/秒；周建国否认约17字承载3秒，约5.7字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组始终在周家正屋客厅，组首列明沈清、周建国、周桂兰位置和委托书状态，没有跨空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周建国说道、周建国对沈清呵斥，现场对白对象明确。",
      "fix_instruction": "若失败，应补足每句真人对白的说话对象。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "授权委托书从第1组茶几中央延续到第2组纸面签名处，紫砂壶从周建国手边放到茶几边缘，转移可见。",
      "fix_instruction": "若失败，应补充委托书或紫砂壶的位置过渡。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留沈清“趁老伴昏迷伪造授权书”以及周桂兰两句追问，没有新增周建国承认情节。",
      "fix_instruction": "若失败，应恢复原台词和人物关系。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部委托书在茶几中央、周建国避开目光；第3组组首继续以同一状态开始。",
      "fix_instruction": "若失败，应在组尾或组首复述茶几文件和人物站位。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "5-7秒只承载周建国放下紫砂壶并扫到签名的同一反应动作，未把辩解台词挤入同一动作段。",
      "fix_instruction": "若失败，应拆开道具动作和对白。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定授权委托书、周建国、周桂兰，数量3条且不与正文矛盾。",
      "fix_instruction": "若失败，应替换为本组人物或道具相关的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
