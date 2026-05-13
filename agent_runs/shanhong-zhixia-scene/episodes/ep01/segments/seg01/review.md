{
  "pass": true,
  "summary": "seg01 已对照原剧本、竖屏生成规则和当前草稿完成审稿，6 个分镜组保留台词顺序、说话对象、场景转场和关键动作，无阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "type": "dialogue_pacing",
      "evidence": "第1组 0-14 秒承载村民甲、村民乙、周大柱、赵有福、沈砚川的 6 句现场对白，约 41 个有效字，含雨中拥挤和沈砚川压住仓门动作，整体约 2.9 字/秒，不存在超过 6.5 字/秒的硬性风险，也没有用短句拖慢凑时长。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留原剧本“开门！”、“你最后进。”、“行，我认。”三处关键台词，并呈现仓门打开、人群往里进、沈砚川按住赵有福的动作，未新增改变剧情的动作或道具。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组进入三天前白天村委会公示栏前，组首明确沈砚川、赵有福、周大柱和村民的位置、朝向及补助名单位置，单组只有一个主要物理空间。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "evidence": "第5组所有现场对白均写明对象：沈砚川对赵有福质问“你卡我补助？”、“拿补助换我地？”，赵有福对沈砚川说“话别说硬。”、“地的事松口，补助能商量。”、“我是帮你。”"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林知夏、沈小禾、周大柱、赵有福、沈砚川和村民甲均在组首空间锁定中有明确位置和身体朝向，开口或行动前都已可见。",
      "fix_instruction": "若不通过，应在组首补足开口人物位置、朝向和可见状态，或在说话前增加入场动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部沈砚川仍守仓门、赵有福低头忍情绪；第3组组首延续仓门关闭、沈砚川靠近横木、赵有福在人群前，门开和拦人动作随后发生，状态连续。",
      "fix_instruction": "若不通过，应在第2组组尾或第3组组首补出仓门、横木、赵有福位置的具体状态。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第4组全部为画面内现场对白，沈砚川、赵有福、周大柱均明确对真实人物说话，无心声、电话音或画外音误承载。",
      "fix_instruction": "若不通过，应将非现场声音改为画外音、电话音或心声，并写明嘴唇闭合不做口型。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组 14 秒只承载补助换地的连续对峙对白和赵有福压近半步、沈砚川情绪反击两个轻中等节拍，没有叠加外部事件或关键道具操作。",
      "fix_instruction": "若不通过，应拆出交易条件或拒绝反击，避免把长动作、道具操作和情绪反转塞入同组。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第6组正文只包含自然画面、台词、光影、风格和负面提示，没有模型说明词、参考图、模板编号、字幕或工程占位符进入正文。",
      "fix_instruction": "若不通过，应删除模型说明词、参考图/模板/首尾帧等工程表达，改为可见画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
