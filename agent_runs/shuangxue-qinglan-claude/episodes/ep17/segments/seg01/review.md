{
  "pass": true,
  "summary": "第1组手机威胁：台词忠实、对白指向明确、时长合理、空间锁定完整，无硬问题。",
  "checked_groups": ["第1组"],
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
      "evidence": "5句台词共56有效字，分布在12秒内，平均4.7字/秒。各时间段字秒比：3.7、4.0、5.2、5.7，均未超过6.5硬上限。情绪对白（厉声、哀求、嘲讽、冷声）按5.2字/秒目标估算合理。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组只包含一个物理空间（周家正屋客厅），组首空间锁定列出全部3名在场人物及其画面位置、身体朝向和关键道具（手机），无跨空间问题。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本5句台词全部保留且未改写：沈清厉声威胁（再往前一步我马上按下去）、赵强哀求（千万别报我明天就去凑钱还你）、周桂兰嘲讽（明天你刚才不是说账上没钱吗）、沈清冷声（不用明天就今晚、转账一分钟内不到位警察局见）。说话对象和台词顺序与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部5句台词均为画面人物现场开口对白，无心声、画外音、电话音或广播音。每句均写明说话人和对白对象（对赵强说道/对沈清哀求道），无口型问题。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒组内强节拍：手机威胁动作1个、赵强冻结投降1个、周桂兰嘲讽对白1个、沈清冷酷对白1个，共4个强节拍。其中赵强投降和周桂兰嘲讽是同一冲突的连续推进，沈清的两句是同一说话人的情绪递进，无并列抢焦点问题。每个时间段只承载一个主动作或一个连续对话节拍。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "本集只有1组，组尾衔接写明沈清右手仍举手机、赵强双手仍举在肩侧、周桂兰双臂环抱站在原位，状态明确。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机是本组唯一关键道具，从组首空间锁定（沈清右手举起手机）到时间段1（手机向前推出）到视频禁止项（手机屏幕熄灭），归属和状态连续，无跳变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作/对话节拍：0-3秒手机推出+威胁对白，3-6秒赵强冻结+投降+哀求，6-8.5秒周桂兰嘲讽，8.5-12秒沈清冷酷对白。无多个顺序主动作塞入同一时间段，非主动作人物（周桂兰在赵强动作段只保持环抱站位）无抢戏。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项4条，均为本组特有剧情错误：沈清放下手机（原剧本手机威胁核心道具）、赵强双手放下（原剧本投降动作）、周桂兰走近赵强（原剧本周桂兰在背景嘲讽未移动）、手机屏幕熄灭（手机可见性）。每条锚定本组人物名和道具名，无泛泛词。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
