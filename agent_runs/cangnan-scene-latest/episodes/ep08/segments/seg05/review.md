{
  "pass": true,
  "summary": "seg05两组保留王建国闯入、亮文件、非法集资指控、江若晴反驳和陆凡被带走，审核通过。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "character_availability",
      "evidence": "王建国和警察未在组首出现，但0-3秒明确踹门冲入，之后王建国才开口并亮文件。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "江若晴“那是我的投资款”、王建国“账目对不上，有人实名举报。带走！”和陆凡最后警告均完整保留。"
    },
    {
      "group": "第10组",
      "type": "dialogue_pacing",
      "evidence": "王建国约16字用4秒，陆凡约17字用3秒，均在6.5字/秒以内；江若晴约15字用3秒，情绪节奏可承载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列出包厢、餐桌、手机、碎杯、大门关闭和三名已在场人物位置，新进人物通过入场动作解决可用性。",
      "fix_instruction": "若失败，应补门状态、已在场人物或入场动作。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "文件从第9组王建国手中举起延续到第10组手中持有，手机仍在陆凡桌面，门保持打开。",
      "fix_instruction": "若失败，应补文件归属和门/手机状态。"
    },
    {
      "group": "第10组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“按规定带走”转译为两名警察扶住陆凡手臂并示意离开，没有新增手铐或殴打等改变剧情动作。",
      "fix_instruction": "若失败，应删除新增强动作并改回可见但克制的带离动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
