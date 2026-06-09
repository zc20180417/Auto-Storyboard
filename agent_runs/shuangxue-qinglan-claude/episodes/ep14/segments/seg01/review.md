{
  "pass": true,
  "summary": "第1组结构完整，台词全部保留，空间单一，时长合理。无硬问题。",
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
      "evidence": "总台词30字/14秒=2.14字秒比，各时间段均低于6.5上限。最长对话段'4-7秒'仅7字/3秒=2.33，有周建国身体前倾和质问情绪支撑，不属于慢语误用。最后段'12-14秒'8字/2秒=4.0，符合普通对白基准。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间'周家正屋客厅'，组首锁定沈清、周美娟、周建国、刘和众人的画面位置和身体朝向，手机和确认转账按钮为关键道具，无跨空间问题。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "全部7个剧本节拍保留：手指悬停、环视宣告、阴沉质问、盯刘回应、冷酷宣言、众人屏息、按按钮确认。台词顺序、说话对象和'两元'反转完整不变。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部对白为画面内现场开口，每句均写明说话人和对象：沈清对众人说道、周建国对沈清质问道、沈清对刘说道。无心声/画外音混用。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "1组内仅1个核心事件链（沈清宣布转账→周建国追问→沈清回应→按按钮确认），每时间段1个主动作或对话节拍，无强节拍过载。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "本集仅1组，无相邻组衔接问题。组尾锚定沈清手指位置、众人视线和周建国姿态，为可能的后续组提供连续性基础。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机始终在沈清手中：组首→手指悬停→环视时持有→按下按钮。确认转账按钮状态从'悬停未触碰'→'按下'，过渡清晰。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "6个时间段各承载1个主动作或对话节拍：手指悬停(动作)、宣告(对话)、质问(对话)、回应(对话)、众人反应(环境)、按按钮+确认(动作+对话同步)。非主动作人物(周美娟、刘、众人)仅写站位和视线反应。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为单空间简单动作+对话组，非复杂动作/保护站位/多人物调度组，视频禁止项可省略。核心道具'手机'和'确认转账按钮'在正文中状态清楚。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "video_negative_constraints",
      "problem": "最后一组涉及关键道具操作（按确认转账按钮），可选择性补充2-3条视频禁止项如'按钮文字消失''沈清手指未触碰屏幕''众人视线偏离手机'，增强生成稳定性。",
      "evidence": "12-14秒时间段沈清按按钮为核心动作，正文描述清楚但无显式禁止项约束。",
      "fix": "可在组尾衔接后补一行：视频禁止项：确认转账按钮文字消失、沈清手指未接触屏幕、众人视线离开手机"
    }
  ]
}
