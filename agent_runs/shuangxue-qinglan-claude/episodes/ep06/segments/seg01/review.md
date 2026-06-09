{
  "pass": true,
  "summary": "银行大厅场景三组分镜结构清晰，台词节奏合理，空间连续，道具流转清楚，OS正确标注闭口，无硬问题。",
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
      "evidence": "第1组15秒5个时间段，台词54字÷15秒=3.6字/秒，节奏适中。沈清问话15字÷3秒=5.0字/秒，柜员接卡后动作占2秒无台词，柜员问话16字÷3秒=5.3字/秒，周桂兰答话10字÷3秒=3.3字/秒，柜员严肃揭示24字÷4秒=6.0字/秒，均未超过6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组14秒，场景始终为银行大厅窗口前。柜员在柜台后方，周桂兰在窗口前椅子上，沈清站在周桂兰身侧，三人位置与第1组组尾衔接一致。组首写明柜员手指指向屏幕、手中持有银行卡，与第1组组尾状态连续。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本沈清猛转头看向窗外赵强新车、OS'狐狸尾巴，终于藏不住了'均完整保留。OS正确标注嘴唇闭合、不做口型、内心旁白响起。原剧本未写周桂兰反应，分镜补充'困惑地看向沈清'，属轻反应不改变剧情因果，合规。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第1组全部为画面内现场对白，每句写明说话人和对象：沈清对柜员、柜员对周桂兰、周桂兰对柜员、柜员对沈清和周桂兰。无心声或画外音混入。",
      "fix_instruction": "无需修复，全部为画面内现场对白，指向正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组14秒3个时间段，每段一个主动作：柜员指着屏幕问话、柜员手指划过屏幕说两年更改、柜员继续指着屏幕说收不到短信。三个信息揭示属同一事件链的连续推进，非并列抢焦点。沈清瞳孔收缩和眼神转向窗外为伴随反应，不构成独立强节拍过载。",
      "fix_instruction": "无需修复，三个信息揭示属同一事件链连续推进，每段一个主动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾：柜员手指指向屏幕、沈清目光盯住柜员、周桂兰右手仍按胸口、银行卡在柜员手中。第2组组首：柜员手指指向屏幕、手中持有银行卡、周桂兰右手仍按胸口、沈清目光盯住柜员。人物位置、道具归属、关键状态完全连续。",
      "fix_instruction": "无需修复，组尾与组首状态完全连续。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第2组组尾银行卡在柜员手中，第3组组首未提及银行卡归属但组尾写明'银行卡仍在柜员手中'，连续无跳变。沈清右手握紧动作发生在第3组，与银行卡在柜员手中不矛盾。",
      "fix_instruction": "无需修复，道具归属连续。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组11秒3个时间段：沈清猛转头看窗外（动作1）、沈清看窗外+OS闭口心声（动作2+声音）、沈清收回目光看向周桂兰（动作3）。每段只有一个主动作或一个连续对话节拍，无过载。非主动作人物周桂兰只写坐姿和困惑表情，未抢主动作。",
      "fix_instruction": "无需修复，每段一个主动作，非主角未抢戏。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组视频禁止项：柜员离开柜台、沈清代周桂兰回答、银行卡从柜员手中消失。3条均锚定本组人物和道具，无泛泛词。第2组视频禁止项：屏幕内容消失、沈清跨出银行空间、银行卡从柜员手中消失。3条均锚定本组剧情。",
      "fix_instruction": "无需修复，视频禁止项锚定具体人物和道具。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "generation_density",
      "problem": "第3组11秒3个时间段，第三段6-11秒沈清收回目光看向周桂兰，主要是轻反应收尾，可考虑缩短为4秒以压缩整组时长。",
      "evidence": "6-11秒段只有沈清收回目光、周桂兰困惑表情，无新剧情信息或道具状态变化。",
      "fix": "可选：将第三段缩短为6-9秒或6-10秒，整组缩为9-10秒。"
    }
  ]
}
