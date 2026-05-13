{
  "pass": true,
  "summary": "seg01 已对照第10集三场戏、竖屏生成规则和当前分镜逐组审核，救人、撤离、仓房前夺钥匙冲突均保留原剧本台词顺序和关键动作，未发现 hard issue。",
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
      "evidence": "原剧本中周大柱砸侧板、沈砚川喊“刘婆，把孩子先推过来！”，刘婆说“我腿软了！”，孩子说“我怕！”，周大柱提醒后坡掉、沈砚川命令砸大点，均按顺序保留在0-14秒内。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "11-15秒连续承载“低头！一步一步走！”“我要回家！”“先活着回去。”约21个有效字，4秒内字秒比约5.25，属于紧急情绪对白可承载范围，且与抱紧孩子、贴边前进动作同步。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组只发生在夜雨中的果园仓房前，组首锁定沈小禾手中钥匙、赵有福位置、林知夏站位和村民围在仓门前，未跨入旧仓房或茶坡空间。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "evidence": "第7组组首写明沈砚川、周大柱、刘婆和孩子位于画面外雨路方向，0-5.5秒先通过脚步声和入场动作进入仓房前，再承担救回与对质内容，人物可用性成立。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "evidence": "第8组最终警告只包含自然画面、现场对白、光影和负面提示词，没有出现Seedance说明、参考模板、自动正反打、@图片或广告/MV等模板污染词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第2组保留周大柱又砸两下、沈砚川把孩子拽出来、孩子喊“奶奶！”，沈砚川让孩子抱紧脖子、刘婆说自己动不了、沈砚川命令大柱进去背人的完整因果。",
      "fix_instruction": "若不通过，应补回遗漏台词或将救孩子与命令背刘婆拆回正确顺序。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组用12秒承载周大柱迟疑、沈砚川催促、周大柱钻入并背出刘婆、喊走四个节拍，复合动作链给到4.5秒，没有叠加长对白或额外道具操作。",
      "fix_instruction": "若不通过，应延长背出刘婆动作或拆成单独短组。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部众人转向回路，第4组组首已在老茶坡回路并写明沈砚川抱孩子、周大柱背刘婆、村民甲持绳和手电，空间转场是原剧本场景切换，人物状态连续。",
      "fix_instruction": "若不通过，应在第3组尾部或第4组组首补明撤离到回路的结果状态。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "麻绳从第4组组首和动作中持续连接众人，第5组组首继续写明麻绳连在众人之间，滚石只作为本组外部事件出现并擦过脚边，没有道具归属跳变。",
      "fix_instruction": "若不通过，应补充麻绳由谁抓住、滚石从坡上滚落到何处。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵有福对沈小禾说“把钥匙给我，我来分粮”“你懂什么，里头乱了”，沈小禾对赵有福说“不给！”，林知夏对赵有福说“砚川没回来前，谁也别碰仓房”，每句现场对白都有真实对象。",
      "fix_instruction": "若不通过，应为每句现场对白补明确人物对象。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第8组全部为画面人物现场开口对白，沈砚川、林知夏均在组首可见且面向赵有福或人群，没有心声、旁白、电话音或门外音误写口型的问题。",
      "fix_instruction": "若不通过，应把非现场声音改成画外音并写明嘴唇闭合不做口型。"
    }
  ],
  "issues": [],
  "warnings": []
}
