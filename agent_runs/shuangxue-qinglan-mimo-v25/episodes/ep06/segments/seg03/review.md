{
  "pass": true,
  "summary": "三组均在银行大厅，柜员揭示短信号码被篡改为本集关键反转，台词全部保留，OS心声正确标注闭口。",
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
      "evidence": "沈清平静请求16字/3秒=5.33字/秒(普通对白≥3.8)；柜员疑惑17字/3.5秒=4.86字/秒(情绪对白≥4.5)。合格。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "柜员'短信提醒号码不是本人的'和'两年前号码被更改过收不到短信'两句关键台词完整保留；周桂兰'天天贴身藏着'保留。揭示顺序与原剧本一致。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "沈清OS'狐狸尾巴终于藏不住了'正确标注为内心旁白，嘴唇闭合不做口型，两个时间段均写明。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "银行卡从沈清手中递出(第1组)→柜员手中持有(第2组组首)→柜员手指指向屏幕(第2组)。道具归属连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组15秒承载周桂兰回答(2.5秒)+柜员揭示(4.5秒)+沈清震惊反应(2秒)+柜员解释(6秒)。四个时间段各一个主动作/对话节拍，属于同一信息揭示事件链。15秒长组具备台词容量(62字约13.8秒朗读)+关键道具操作(指屏幕)+剧情反转(号码被篡改)，满足长组准入。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组两个时间段：转头看窗外(3.5秒)+OS旁白(2.5秒)，各承载一个动作/一个声音节拍。6秒短组为识破真相的戏剧节拍，有明确承接价值。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
