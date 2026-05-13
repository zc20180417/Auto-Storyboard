{
  "pass": true,
  "summary": "seg01 已按竖屏 storyboard-reviewer 对照原剧本和分镜草稿完成审核，6 组均保留原台词、现场动作和转折，无阻断交付的 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组"],
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中路人甲问“这是今天刚到的？”，许安答“凌晨到的，先看纹路”，邻居乙评价肉色，林小满写“老周肉市，今早进货，三十六斤”，分镜在第2组按相同顺序保留，并通过小黑板和肉盆承载证据。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组0-4秒承载路人乙和路人甲点单约24个有效字，字秒比约6.0；4-9秒承载唐婶和林小满约27个有效字，字秒比约5.4，均低于6.5硬上限并有点单、记单动作支撑。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组只发生在傍晚摊前，组首明确许安在烤炉后、林小满在摊前、马会在背景人群后方且手持折过单据，人物在开口和动作前均可用。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "evidence": "第5组正文没有出现模板编号、参考图、自动分镜、模型说明词或工程占位符，台词和画面均为摊前现场自然描述。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "唐婶明确对街口围观的人说话，邻居甲明确对林小满问话，林小满明确回应邻居甲，没有假对象或无对象对白。",
      "fix_instruction": "若发现无对象对白，应改为某角色对具体人物或围观人群说道。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组包含许安备货动作、唐婶喊人、围观者评价、林小满与许安短句交流，分为4个时间段共15秒，复合备货动作独立给3.5秒，没有与长台词硬挤。",
      "fix_instruction": "若动作和对白过载，应拆出备货动作或压缩非关键围观反应。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组作为傍晚新场景，重新锁定烤炉、桌椅、许安、林小满、唐婶和食客位置；第4组尾部的烤炉开烤和食客围满可自然衔接第5组摊前品尝。第5组组首复述烤炉、桌椅、人群和人物位置。",
      "fix_instruction": "若同场景衔接断裂，应在上一组组尾或下一组组首补人物位置、道具归属和炉火状态。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "马会在组首已手持折过的单据，0-3秒挤到前排时继续捏着单据，6.5-12秒把单据抬起半寸，许安只握紧自己炉边炭夹，道具归属没有跳变。",
      "fix_instruction": "若单据或炭夹归属突变，应补充递出、放下、拿起或握紧等可见过渡动作。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第2组全部为现场真人开口对白，均写明说话人和对象；没有心声、画外音或电话音误写成现场口型。",
      "fix_instruction": "若出现画外音或心声，应写明声音来源，并让画面人物嘴唇闭合不做口型。"
    }
  ],
  "issues": [],
  "warnings": []
}
