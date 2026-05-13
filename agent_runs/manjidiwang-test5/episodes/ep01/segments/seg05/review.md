{
  "pass": true,
  "summary": "seg05共1组，忠于原剧本1-5新增片段全部内容，格式规范，空间锁定完整，无硬性问题。",
  "checked_groups": ["第1组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "generation_density": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "酒店地下车库为主空间，主观想象闪回为例外空间，已在时间段中明确标注，符合Seedance片段空间规则。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "evidence": "闪回画面（龙袍、毒酒、满门抄斩喊声、玉玺）均为可生成的视觉画面。OS心声写明'嘴唇闭合、不做口型'。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "全部闪回画面和OS台词保留：前世死于毒酒、满门三百余口、资本战场布局、递毒酒的手、既得重生唯我执棋。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩在组首有明确位置（驾驶座、双手握方向盘、等红灯），闪回中的人物为主观想象不要求在场。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "OS心声正确标注'心声响起（对自己）'和'嘴唇闭合、不做口型'，闪回用叠化转场明确标识。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首交代车辆在路口等红灯，与上组朱文浩启动车辆驶入车流的状态衔接。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "generation_density",
      "problem": "闪回蒙太奇与OS叠加",
      "evidence": "闪回4画面快速切换加3句OS和绿灯反应，4个强节拍在10秒组内密度适中但闪回节奏紧凑。",
      "fix": "可选延长闪回时间段或拆分。"
    }
  ]
}