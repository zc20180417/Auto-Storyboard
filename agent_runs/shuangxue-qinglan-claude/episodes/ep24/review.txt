{
  "pass": true,
  "summary": "第24集分镜共3组，台词忠实、口型指向正确、空间单一、状态连续，无硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "沈清台词'大家看清楚，这是他女婿偷刷我妈养老钱的记录！'有效21字，承载时间段4-10秒共6秒，字秒比3.5字/秒，低于6.5硬上限。情绪对白按5.2字/秒目标约需4秒，实际分配6秒含指向屏幕动作，节奏合理。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首空间锁定写明'龙腾酒店宴会厅内，LED大屏幕仍然亮着显示转账记录'，单一物理空间，与第1组组尾衔接一致。人物位置从第1组继承：沈清画面右侧、周建国画面中央、周美娟画面左侧。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "沈清台词'我还查到，你两年前偷偷在外面借了高利贷！'完整保留；周建国'面如死灰'反应通过特写镜头呈现；周美娟在背景中捂嘴惊恐的反应与剧本'大惊失色'呼应。台词顺序、说话对象、剧情因果均未改动。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈清'大声'台词为画面内现场开口对白，写明'对在场众人高声说道'，口型与声音一致，无心声/画外音混用。",
      "fix_instruction": "无需修改，口型与声音来源一致。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组6秒承载3个时间段：屏幕画面切换、周美娟反应喊叫、沈清逼视周建国。每段只有一个主动作，强节拍数3个（视频揭示、惊慌反应、压迫对峙），属于同一事件链的连续推进，6秒短组属短承接/单句反应合理例外。",
      "fix_instruction": "无需修改，6秒短组属合理例外。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾：LED屏幕亮着显示转账记录、沈清指向屏幕、周建国和周美娟惊愕。第2组组首：LED屏幕仍亮着显示转账记录、人物位置不变。状态连续无跳变。",
      "fix_instruction": "无需修改，状态衔接连续。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "LED大屏幕从第1组亮起，经第2组显示监控视频，到第3组仍然亮着，状态连续。无关键道具归属跳变。",
      "fix_instruction": "无需修改，道具状态连续。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组3个时间段各承载一个主动作：沈清说出台词（0-4秒）、周建国面部反应（4-6秒）、周建国身体反应+周美娟背景反应（6-8秒）。无时间段同时塞入多个主动作。周美娟在背景中仅做轻反应，未抢沈清主动作。",
      "fix_instruction": "无需修改，每段一个主动作。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项4条均锚定本组具体人物和道具：周美娟挡屏幕、沈清关屏幕、周建国逃离、监控视频消失。无泛泛词，无模板化条目。",
      "fix_instruction": "无需修改，禁止项已锚定本组具体人物和道具。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "generation_density",
      "problem": "第3组8秒主要由沈清4秒台词+周建国4秒反应构成，剧情密度偏低但属转折揭露节拍，不构成硬问题。",
      "evidence": "有效台词18字÷4秒=4.5字/秒，周建国'面如死灰'反应4秒含面部特写和身体反应两段，整体承载揭露+反应的完整戏剧节拍。",
      "fix": "如需优化，可将6-8秒的中景周建国反应缩短为2秒，使整组压缩为6秒短组；但当前8秒对转折揭露节拍尚可接受。"
    }
  ]
}