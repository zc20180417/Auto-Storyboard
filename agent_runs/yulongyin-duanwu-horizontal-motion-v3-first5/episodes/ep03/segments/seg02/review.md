{
  "pass": true,
  "summary": "seg02 已完成真实横屏审核，第4至第7组保留爷爷听见水声、闯入质问、识别云宝与黑水警告，空间轴线和水壶归属连续。",
  "checked_groups": [
    "第4组",
    "第5组",
    "第6组",
    "第7组"
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
      "group": "第4组",
      "type": "camera_motion",
      "evidence": "第4组0-3秒用低位横向跟拍从拐杖脚点到卧室门下缘，明确声音来源和压迫路径。"
    },
    {
      "group": "第5组",
      "type": "screen_direction",
      "evidence": "第5组爷爷保持画面左侧，天天保持画面右侧，质问和解释都沿同一左右轴线完成。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "第6组保留爷爷眼神清明、说出“清水养它，脏水害它”、天天紧张出汗并试探追问的原剧本顺序。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "第7组3-8秒承载约20字警告台词，5秒内约4字/秒，符合严肃警告的可表演节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "爷爷在门外可见，天天作为门内被问话对象由门板和后续开门承接，没有发明假对话对象。",
      "fix_instruction": "若不通过，应补充声音来源或门内人物反应，确保问话对象成立。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从小桌前被天天抱进怀里，后续质问、解释和爷爷视线都围绕怀中水壶展开。",
      "fix_instruction": "若道具归属跳变，应补写抱起、护住或放回的可见动作。"
    },
    {
      "group": "第6组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "信息链从爷爷眼神清明，到说出清水脏水规则，再落到天天意识到爷爷认识它。",
      "fix_instruction": "若递进断裂，应恢复眼神、规则台词、天天追问三步。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写爷爷、天天、水壶、门口阴影的静态位置和视线关系，没有过程动作。",
      "fix_instruction": "若出现推开、走到、拿起等过程动词，应移入时间段镜头描述。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图字段、组间承接、Seedance执行提示补充或本镜估算时长。",
      "fix_instruction": "若出现生产备注，应删除并改写为自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
