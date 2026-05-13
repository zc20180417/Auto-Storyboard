{
  "pass": true,
  "summary": "seg01 已对照村口缺水、胡永贵卖化肥、爷爷与天天拉扯、黑水入渠逐组审核，台词、道具归属、横屏调度和运镜字段均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "type": "script_fidelity",
      "evidence": "保留村民甲“三个月没下雨，井都干透了！这日子没法过了！”和村民乙“再没水...”两句原台词，井底黄泥、空桶、庄稼缺水均对应原剧本。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "0-2秒固定中全景锁住胡永贵右侧高位和村民左侧低位，9-12秒轻微推近到化肥袋缝隙黑水，运镜服务道具揭示。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "爷爷从左侧进入中央，胡永贵保持右侧车厢高位，天天在左后方，左右与高低关系支撑对峙。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "黑水从化肥袋落到干渠，再沿前景干渠由右向左流向河床方向，与前组道具来源连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "村民甲台词约26字用4秒，村民乙台词约27字用4秒，均有动作和群像承载，节奏可表演。",
      "fix_instruction": "如后续改短镜头，需拆分台词或增加反应承载，避免超过口型速度。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爷爷始终在画面左下或中央偏左仰看胡永贵，胡永贵保持右侧车厢高位俯视，轴线未跳变。",
      "fix_instruction": "如改换边，需增加正面中性镜头或明确走位过渡。"
    },
    {
      "group": "第4组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "天天从左后方挤入，抓住爷爷衣角向左侧拉，承接第3组天天在左后方看爷爷的位置。",
      "fix_instruction": "如增加人群遮挡，仍需保持天天入场路径可见。"
    },
    {
      "group": "第5组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "9-12秒低位沿干渠平移，从右下黑水起点带向左上河床方向，明确污染流向，不是静止空镜。",
      "fix_instruction": "若压缩该镜头，仍需保留黑水方向和河床目标。"
    }
  ],
  "issues": [],
  "warnings": []
}
