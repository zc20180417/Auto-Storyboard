{
  "pass": true,
  "summary": "seg01 已对照第9集原剧本、竖屏 generator 规则和 reviewer 门禁逐组审核，挑人救援、泥坡绕路、旧仓房破门三段剧情完整保留，未发现 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
      "evidence": "原剧本中沈砚川甩下麻绳、说“我带头，周大柱跟我”，周大柱回应“行”，赵有福拦阻“不行，天亮再说”，沈砚川反问“等天亮你去收尸？”的顺序完整保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组 14 秒承载三人系绳挪坡、周大柱与沈砚川两句短答、村民甲一句“我听见孩子哭了”、沈砚川停下听水声并解释水急不能下；台词总量约 49 字，分散在 3-6 秒、6-9.5 秒、9.5-14 秒并有泥路行进和停步听水动作，口型节奏可表演。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "孩子“救命！”和刘婆“外头有人吗！”均写明从门缝和木板后传出，刘婆和孩子在组首标明位于仓房内不可见；周大柱“有！别怕！”是画面人物现场开口，声音来源清楚。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "第6组尾部周大柱举锄头、沈砚川照住侧板，第7组组首延续该状态；周大柱砸侧板两下后裂缝扩大，后坡泥石落下，再由沈砚川命令继续砸，锄头和侧板状态连续。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "evidence": "收尾只写旧仓房外破板救人的自然画面和现场喊话，没有出现 Seedance、模板编号、参考图、自动分镜、字幕说明或其他工程词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列明夜雨果园仓房前的仓房门、油灯、麻绳，以及沈砚川、赵有福、周大柱、林知夏、村民的位置和身体朝向；全组只发生在仓房前一个物理空间。",
      "fix_instruction": "若不通过，应补齐每个在场人物的位置、朝向和关键道具位置，或拆出新的物理空间。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵有福“夜里看不清，出了事谁担？”明确对沈砚川说；沈砚川“我担”“你是怕担责”明确对赵有福说；村民乙求救明确对沈砚川说；周大柱和赵有福互相对话对象明确。",
      "fix_instruction": "若不通过，应给每句现场对白补真实人物对象，不得写成对空气或道具说话。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部周大柱抓紧麻绳、赵有福无话可接，第3组组首延续麻绳在泥地、周大柱抓绳、赵有福在门边的状态；林知夏接管果园后，沈砚川和周大柱系绳离开，为下一场老茶坡小路建立过渡。",
      "fix_instruction": "若不通过，应在第2组尾或第3组开头补麻绳归属、赵有福位置或沈砚川离开的可见动作。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "三人系绳往坡下挪、脚下全是泥、周大柱说路没人走、沈砚川解释正路塌了只能绕、村民甲听见孩子哭、沈砚川要求听水声并说明水急不能下，均按原剧本保留。",
      "fix_instruction": "若不通过，应恢复绕路、孩子哭声、水声判断三项救援信息。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组只承载碎石滚落、村民甲惊叫、沈砚川命令贴坡、周大柱追问是否继续、沈砚川决定继续救援；动作和对白都在同一泥坡空间内，12 秒可表演，没有额外新增强动作。",
      "fix_instruction": "若不通过，应拆出碎石滚落或继续救援决定，避免把更多事件塞入本组。"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈砚川和周大柱在旧仓房外组首可见；刘婆和孩子不在画面内，但组首明确他们位于仓房门内不可见，声音从门缝和木板后传出，符合声音人物可用性。",
      "fix_instruction": "若不通过，应在组首写明门内声音来源，或在角色开口前安排可见入场。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "锄头从第6组尾部周大柱手中延续到第7组组首，木侧板先被砸出裂缝，再由沈砚川照进缝内查看，后坡泥石滚落后手电转向再回到侧板，关键道具和操作顺序清楚。",
      "fix_instruction": "若不通过，应补锄头归属、侧板裂缝形成过程或手电照向变化。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "孩子“爹！”从木板裂缝里传出，沈砚川“听着，我们来了！”明确为画面人物隔着木板向仓房内喊话，并写明嘴唇清楚开合；门内刘婆只以喘息回应，不承担画面口型。",
      "fix_instruction": "若不通过，应区分门内声音和画面外现场开口，补声音来源或人物口型状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
