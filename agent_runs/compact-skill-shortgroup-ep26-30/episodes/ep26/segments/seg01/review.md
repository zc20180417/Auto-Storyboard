{
  "pass": true,
  "summary": "已对照第26集原剧本、竖屏生成规则和当前分段分镜逐组审核；七组均保留原台词、道具与反转关系，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "顾长海摔茶具、怒骂“蠢货！被两个乡下乞丐耍了！”，顾雪解释遗弃她的人，顾秘书汇报商超铺货，均按原顺序保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "evidence": "赵朵朵直接对副局长问“凭什么查封？有化验证明吗？”，顾雪对赵朵朵威胁坐牢，赵朵朵再直视顾雪回击，没有假对话对象。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "录音笔台词明确写为从赵朵朵手中录音笔传出，顾雪本人没有现场开口承载这句录音内容，声音来源与口型分离清楚。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "evidence": "第6组尾部顾雪退到通道边、副局长瘫坐在地、录音笔在赵朵朵手中；第7组组首延续这些位置，再执行带走命令和上铐动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "最长对话段为5-11秒，顾雪解释与顾长海回击合计约31个有效字，6秒承载，低于6.5字/秒硬上限，并有正反打反应承托。",
      "fix_instruction": "若不通过，应拆分顾雪解释与顾长海回击，或延长承接反应段，不能删改原台词。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载执法人员冲到展位、副局长喝止、顾雪指控、群众惊恐和查封命令，分为4个连续时间段，每段只推进一个主要节拍。",
      "fix_instruction": "若密度过载，应把群众惊恐或查封命令拆成独立组，而不是压缩台词。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首把赵朵朵、顾雪、副局长、正局长、首富和报告位置都锁在会展中心展位前通道内，正局长与首富已在入口内，后续快步走向展位可生成。",
      "fix_instruction": "若不通过，应补正局长和首富在入口内的位置，避免未入场人物直接发声。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "录音笔从赵朵朵右手贴近展台下沿开始，3-7秒由赵朵朵拿起并按下播放键，之后录音笔继续握在她手中，关键证据归属连续。",
      "fix_instruction": "若不通过，应补充录音笔从展台下沿到赵朵朵手中的可见过渡动作。"
    },
    {
      "group": "第7组",
      "type": "format",
      "result": "pass",
      "evidence": "第7组总时长10秒，时间段为0-4.5、4.5-8.5、8.5-10秒，镜头数3个且标题数值一致，属于竖屏默认时长范围内的收束组。",
      "fix_instruction": "若不通过，应调整时间段末尾与标题总时长一致，并保持0.5秒粒度。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、官方占位符、参考图/视频/音频占位、模型自动处理说明或广告式模板语气；风格与负向约束保持为短剧分镜正文。",
      "fix_instruction": "若出现污染词，应删除工程说明词，改成具体人物、空间、动作、光影或声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
