{
  "pass": true,
  "summary": "已审核26-3商会会议段，三大家主断供和金董要求陆凡认输的关键台词均保留。",
  "checked_groups": [
    "第1组",
    "第2组"
  ],
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
      "evidence": "金董关于黑风山干股、赵家主切断物流、李家主砖头都买不到三句台词均按原顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "钱家主约18字/4秒，金董约12字/3秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首列明会议室、会议桌、金董首位以及三大家主两侧位置，后续发言人物均可用。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵家主、李家主、钱家主在第1组组首均位于会议桌周边，后续对话前可见。",
      "fix_instruction": "如不通过，应在组首补足发言家主的位置和身体朝向。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "高脚杯在组首已位于四人面前，7-11秒碰杯有可操作来源。",
      "fix_instruction": "如不通过，应补充杯子从桌面到手中的过渡。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只有钱家主台词、金董台词和碰杯三个节拍，11秒容量充足。",
      "fix_instruction": "如不通过，应压缩碰杯动作或拆分台词。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有参考模板、自动分镜、参考图等污染表达。",
      "fix_instruction": "如不通过，应删除污染词并改写成会议室内可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
