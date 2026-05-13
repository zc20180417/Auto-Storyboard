{
  "pass": true,
  "summary": "seg01 已对照第14集原剧本完成审核，6组均保留关键台词、动作、空间转换和父子异样收尾，无阻断交付的 hard issue。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本棚口找孩子的连续台词均保留：妇人说“我儿子刚还在这儿！”，沈小禾说“我分水时还看见他了。”，周大柱喊“都别乱跑！”，赵有福质疑，妇人反驳，林知夏发现小脚印往后坡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组总时长14秒，包含约54字情绪对白和下令动作，按情绪对白约5.2字/秒估算约10.4秒，加转身下令和赵有福上前质疑动作，14秒可表演，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组只发生在夜雨中的后坡旧鸡棚边，组首锁定沈砚川、林知夏和门内阴影里的失踪男孩，孩子在开口前已经位于鸡棚门内可用位置。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组组尾为沈砚川抱着孩子站在鸡棚门口，林知夏守在旁边；第4组组首延续为沈砚川抱着失踪男孩、林知夏在旁，破门敞开，人物和道具状态连续。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "evidence": "第6组正文无 Seedance、参考模板、@图片、自动分镜、字幕贴片等工程或模板污染词，收尾以赵有福和赵成武的异样眼神承载剧情悬念。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "妇人、沈小禾、周大柱、赵有福和林知夏的现场对白均写明对棚内众人、村民妇人、赵有福或沈砚川和众人的说话对象，没有对空气或道具说话。",
      "fix_instruction": "若不通过，应把每句现场对白改为明确的“A对B说道/喊道/问道”。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "男孩哭喊“娘！”来自鸡棚门内，破门晃动和门内裤脚小手提供声音来源；林知夏的“别怕，我们来了！”为现场开口并朝门内孩子喊出。",
      "fix_instruction": "若不通过，应补充声音来源或改成画外音承载，并说明画面人物不做口型。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组14秒承载孩子鞋掉、林知夏提醒水涨、坡边滑倒、沈砚川拽稳四个连续救援节拍，均在同一泥坡空间内，动作链按0-4、4-7、7-11、11-14秒分配，可表演且未硬塞额外剧情。",
      "fix_instruction": "若不通过，应拆出滑倒救援或压缩非关键反应，避免同组动作过载。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "妇人抱住孩子、村民甲说找回来了、赵有福想把事算了、周大柱反驳、沈砚川表态均与原剧本顺序一致，没有新增改变因果的动作。",
      "fix_instruction": "若不通过，应恢复原台词顺序和关键动作，不添加额外冲突。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "油桶在第5组组首和第6组组首均位于仓房背景角落，只作为赵有福试图了结事件的背景证据，没有出现无过渡的道具转移或操作。",
      "fix_instruction": "若不通过，应补充油桶位置、归属或可见转移过程。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部沈砚川挡在众人和赵有福之间，第6组组首仍为沈砚川面对赵有福和村民，赵成武位于背景右侧人群后方，支持片尾父子异样对视。",
      "fix_instruction": "若不通过，应在第5组尾或第6组组首补清人物站位和赵成武可用位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
