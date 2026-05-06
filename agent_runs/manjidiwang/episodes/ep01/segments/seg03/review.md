{
  "pass": true,
  "summary": "seg03共4组已复审，身份揭露、证据展示、验证名片和离开动作均保留，旧景别与说话动词硬问题已清除。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留房门关闭、苏清寒问'你到底是谁？'、朱文浩答身份、苏清寒搜索'朱文浩'和手机人设结果。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组始终在酒店行政套房内，证据链以手机屏幕画面呈现，未切换到其他现实空间。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组0-3秒'我查苏长明半年了。你，只是他最新的牺牲品。'21字/3秒=7.0字/秒，偏快但仍在可接受上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组到第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组以苏清寒盯着手机证据、手指颤抖收尾，第3组组首承接苏清寒手持手机、眼眶泛红面对朱文浩。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "第3组朱文浩两句关键台词均为对苏清寒冷声说道，未使用'冷酷道'等非标准说话动词。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "苏清寒接过名片、转身离开、脚步虚浮和朱文浩放下酒杯均为可拍动作，OS作为自言自语画外音承载内心判断。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "身份台词语速偏快但可接受",
      "evidence": "第1组4-6秒'集团常务副董之子，朱文浩。'13字/2秒=6.5字/秒。",
      "fix": "可选延至3秒。"
    },
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "压迫台词语速接近上限",
      "evidence": "第3组0-3秒'我查苏长明半年了。你，只是他最新的牺牲品。'21字/3秒=7.0字/秒。",
      "fix": "可选拆成正反打，但当前未超过硬错误阈值。"
    }
  ]
}
