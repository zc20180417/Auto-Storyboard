{
  "pass": true,
  "summary": "5组分镜格式完整，台词忠实度合格，空间锁定和组尾衔接清楚。第2组和第4组语速偏慢但不构成硬错误。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "赵朵朵'敲钟'2字/2秒=1.0字/秒，属于动作伴随短句，合理。全场'涨停了！上市即涨停！'7字/1.5秒=4.7字/秒，在欢呼情绪下合理。赵大雷'妈！咱们家发大财啦！'8字/2秒=4.0字/秒，情绪对白但有抱起动作伴随，合理。赵朵朵'这只是一个新起点'9字/4秒=2.25字/秒，偏低但有看屏幕确认和情绪沉淀，不判hard。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确写清'远县村口，宽阔的水泥大桥横跨河面，桥头右侧立着朵朵希望桥石碑'，并写清村长和村民在桥头左侧、赵朵朵和赵大雷从桥面走来站到右侧。单一物理空间，无跨场景违规。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "原剧本大嫂'朵朵快坐，红烧肉刚出锅'、桂姨'多吃点，你在外头太累了'、赵大雷'来！咱一家人碰一个！'、赵朵朵'祝咱们家的日子越来越红火'全部保留，说话对象和台词顺序不变。碰杯、咬红烧肉、看繁星等关键动作全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "warning",
      "evidence": "赵朵朵'助理，启动希望小学捐建项目'9字/3秒=3.0字/秒，低于普通对白4.5字/秒基准。助理'明白，第一站定在哪里'8字/2秒=4.0字/秒，略低。赵朵朵'我的老家，远县北沟村'8字/2秒=4.0字/秒。整体29字/7秒=4.14字/秒，偏低但属于重要宣布场景，有转身和入场动作支撑。",
      "fix_instruction": "可考虑将0-3秒段缩短到2.5秒，或将助理台词段缩短到1.5秒，使整体语速接近4.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有2个轻节拍：赵大雷评论路和赵朵朵问饭。无外部事件、无关键道具操作、无情绪反转。赵大雷擦汗是轻动作，与台词同步。整体节奏清楚，不存在过载。",
      "fix_instruction": "若不通过，应拆组或压缩非关键动作。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾写清'赵朵朵面向大屏幕站立，赵大雷放下桂姨，人群仍在背景中鼓掌欢呼'。第2组组首写清'赵朵朵站在大屏幕前方，助理从人群后方走来'。空间连续（交易所大厅），赵大雷放下桂姨的状态衔接合理，助理入场有来源（人群后方）。",
      "fix_instruction": "若不通过，应在组尾补充人物位置和道具状态的具体锚点。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "桥头石碑在组首空间锁定中写清位置（桥头右侧），重卡在8-12秒时间段中从桥面驶来，石碑和桥面在组尾仍可见。道具状态无跳变。",
      "fix_instruction": "若不通过，应补充道具从谁手中转移到谁可操作的可见过渡。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "整体语速4.14字/秒，略低于普通对白4.5字/秒基准",
      "evidence": "29字/7秒，赵朵朵宣布语速3.0字/秒，助理回应4.0字/秒",
      "fix": "可微调时间段使语速接近基准，但当前节奏在重要宣布场景下可接受"
    },
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "dialogue_pacing",
      "problem": "赵朵朵'大哥，家里的饭做好了吗'3.5字/秒，偏低",
      "evidence": "7字/2秒=3.5字/秒，有低头动作伴随，但无明确慢语标记",
      "fix": "可将该段缩短到1.5秒或加入轻动作填充，但当前兄妹私语节奏自然"
    }
  ]
}
