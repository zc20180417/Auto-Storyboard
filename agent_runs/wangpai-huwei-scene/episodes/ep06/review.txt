{
  "pass": true,
  "summary": "第6集分镜保留假视频分析、保险柜线索、周振邦派人夜闯、顾北辰反制并收集物证、许知夏走廊试探和窗外黑影退出的完整链路；对白节奏、空间分组、道具连续和心声口型均已检查通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "许知夏追问伪证链和反击筹码的长句安排在3-10秒，约42个有效字用7秒承载，字秒比约6.0，低于6.5硬上限；顾北辰保险柜提示单独占10-15秒。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "赵明海说明打草惊蛇、许振南藏东西、许知夏发出去就完蛋，以及'多半藏在公司保险柜里'均按原剧本保留，没有改变保险柜线索来源。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "顾北辰对黑衣人甲的肘击、补拳，以及对黑衣人乙的侧身卸力、拧腕、压跪反扣分为四个时间段，单段只承载一个主动作链。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "evidence": "第10组从黑衣人口袋翻出微型撬具和周氏门禁卡并收入口袋，组尾写明两件物证在顾北辰口袋里，保险柜仍关闭，物证和保险柜状态清楚。"
    },
    {
      "group": "第12组",
      "type": "space_locking",
      "evidence": "第12组主空间为许氏集团走廊，窗外黑影作为背景窗外可见事件处理，许知夏和顾北辰仍在走廊对峙，没有把黑影写入室内空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏关于假视频毁掉许父和许氏的内容写为心声，并明确嘴唇闭合不做口型，没有被写成现场对白。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "顾北辰和许知夏的现场对白均写明顾北辰对许知夏、许知夏对顾北辰说道，没有假对象或遗漏对话方向。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许知夏追问'你怎么知道有保险柜'、顾北辰避开话题并提醒今晚不能走、许知夏警惕心声均按原剧本顺序保留。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "周振邦命令黑衣人的台词安排在0-6秒，约31个有效字用6秒承载，字秒比约5.2，符合情绪命令台词节奏。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "顾北辰在组首被放在办公室内阴影深处，黑衣人进入保险柜前即可被揭示；两名黑衣人和保险柜位置也在组首明确。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第9组复杂打斗的视频禁止项锚定黑衣人乙、顾北辰、黑衣人甲、保险柜门，数量4条，未使用无锚点泛泛词且不禁止原剧本动作。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第11组",
      "type": "filmability",
      "result": "pass",
      "evidence": "许知夏怀疑顾北辰被转译为看衣袖划痕和保险柜旁脚印；'野猫'笑点由现场对白和可见道具承载，不依赖抽象心理判断。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第12组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、自动正反打、参考模板、@图片/@视频/@音频、广告/MV语气或模板化批量描述。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
