{
  "pass": true,
  "summary": "已逐组对照第26集剧本、竖屏生成规则和Seedance污染约束，9组均保留关键台词、动作、道具和声源，未发现硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中顾长海砸碎茶具、怒骂“蠢货！被两个乡下乞丐耍了！”，顾雪解释遗弃关系、顾长海说全省笑话、顾秘书汇报商超进展，分镜在0-14秒内按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "文件夹从顾秘书手中到顾雪抽出，再递给顾长海，随后顾长海接过并合上文件夹，关键道具有可见转移，没有凭空换手。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "副局长对排队群众喊停，顾雪对副局长指控朵朵牌，群众对身边人惊呼工业明胶，三处现场对白均有真实对象。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "正局长两段报告台词分别约19字/4.5秒和19字/4.5秒，字秒比约4.2，低于6.5硬上限，且配合举报告和人群反应。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "录音笔播放顾雪声音时明确写出声音来自录音笔，画面中的顾雪嘴唇闭合不做口型，声音来源和口型分离清楚。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "evidence": "第8组组尾正局长转向执法人员，第9组组首警察位于通道入口，随后执行带走命令，人物位置和动作承接自然。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组-第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "顾家客厅段保留砸茶具、顾雪献计、递文件、顾长海命令和警告的完整因果链，没有新增改变剧情的动作。",
      "fix_instruction": "无需修复；若后续改稿，必须继续保留茶具碎裂、文件夹递接和顾长海最后警告。"
    },
    {
      "group": "第3组-第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "展会查封段拆为到场指控、查封拦阻、顾雪挑衅三组，每组强节拍不超过可表演范围，未把查封、质问、反击全部压进单组。",
      "fix_instruction": "无需修复；若压缩组数，应优先避免把副局长查封、赵朵朵质问和顾雪挑衅合并过载。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确副局长、顾雪、执法人员、赵朵朵和果冻样品在朵朵牌展位的相对位置，后续封存袋、拦阻动作均在同一物理空间发生。",
      "fix_instruction": "无需修复；若调整镜头，应保持赵朵朵在展台内侧绕出并挡住封存袋的可见过渡。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "首富怒喝约12字/3秒、副局长解释约9字/3秒、两段报告台词各4.5秒，均未超过6.5字/秒，入口行动和举报告动作有承载时间。",
      "fix_instruction": "无需修复；若缩短第6组，需重新核算首富和正局长台词的字秒比。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "录音笔台词作为扬声器声音处理，赵朵朵只按下播放键，顾雪本人闭嘴不做口型，避免把录音误写成现场开口。",
      "fix_instruction": "无需修复；若重写录音段，必须保留录音笔指示灯或扬声器等可见声音载体。"
    },
    {
      "group": "第8组-第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组结束时顾雪后退、副局长瘫坐、正局长转向执法人员；第9组从正局长下令和警察进入接上，手铐归属和人物状态连续。",
      "fix_instruction": "无需修复；若调整结尾，应保持副局长瘫坐和顾雪被戴手铐的状态衔接。"
    },
    {
      "group": "第1组-第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、占位符、参考图说明、广告或MV语气，负向提示只作为每组尾部约束出现。",
      "fix_instruction": "无需修复；后续不得加入模板编号、占位符、参考图或由模型自动处理等工程说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
