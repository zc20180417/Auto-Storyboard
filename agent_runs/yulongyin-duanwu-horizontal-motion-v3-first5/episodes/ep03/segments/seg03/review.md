{
  "pass": true,
  "summary": "seg03 已按横屏 reviewer 逐项审查，第8至第9组保留追问、爷爷糊涂、天天退回房间、旧照片和云中君线索，格式与空间调度可交付。",
  "checked_groups": [
    "第8组",
    "第9组"
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
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "第8组天天对爷爷追问，爷爷对天天糊涂回答和反问，画面中双方同框且对象明确。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "第8组将三句爷爷台词拆成6.5-9.5秒、9.5-12.5秒和12.5-15秒，避免长句堆进同一镜头。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "evidence": "第9组照片从旧木柜抽屉中翻出，到爷爷手中，再到正反面特写，证据路径连续。"
    },
    {
      "group": "第9组",
      "type": "horizontal_composition",
      "evidence": "第9组天天从右侧门离开，爷爷留在左侧，再横向跟到右后景旧木柜，横屏空场表达人物分离。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留天天追问、爷爷清明消散、龙舟鼓、燃燃放学与不回家反问，未改写台词顺序。",
      "fix_instruction": "若不通过，应恢复原剧本台词原文和糊涂递进顺序。"
    },
    {
      "group": "第8组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "信息链从追问开始，落到爷爷认知断裂和天天失望，组尾自然承接人物分离。",
      "fix_instruction": "若递进断裂，应补足清明消散和天天无奈反应。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写爷爷、旧木柜、卧室门和天天不在画面内的静态状态，没有动作过程。",
      "fix_instruction": "若出现走到、拉开、翻出等过程动词，应放入后续时间段。"
    },
    {
      "group": "第9组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "第9组有固定人物分离、横向跟拍旧木柜、推近照片和摇向背面文字，运镜均服务记忆线索。",
      "fix_instruction": "若运镜空泛，应写清跟随对象、起点、终点或证据揭示目标。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现参考图、模板编号、视频延长、组间承接或本镜估算时长等污染项。",
      "fix_instruction": "若出现工程字段，应删除并改成自然镜头描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
