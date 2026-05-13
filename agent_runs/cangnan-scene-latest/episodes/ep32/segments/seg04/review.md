{
  "pass": true,
  "summary": "seg04已审核，按键、硬币击腕、偏离按钮、耳麦断电和庄园黑暗失效自毁均完整保留。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "龙万山按红色自毁键、陆凡掷硬币、硬币击中手腕麻筋、龙万山痛呼并跌伏偏离按钮，均按原剧本顺序呈现。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "陆凡明确对耳麦里的技术组说道“技术组，切断庄园物理电源。”商会总管明确对陆凡说道“大人神机妙算，属下佩服。”"
    },
    {
      "group": "第8组",
      "type": "timing_math",
      "evidence": "第8组总时长12秒，时间段0-4、4-8、8-12连续且结束于总时长，镜头数3个与时间段一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "组首交代龙万山大拇指悬在红色自毁键上方，5-7秒硬币击腕使手指偏离按钮，7-12秒确认没有压下按钮。",
      "fix_instruction": "若不通过，应补足手指从按钮上方到偏离按钮的可见过渡。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "技术组只作为耳麦通信存在，陆凡现场开口对耳麦下令，未让技术组画面口型承担台词。",
      "fix_instruction": "若不通过，应区分耳麦音和现场对白。"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "庄园陷入黑暗通过灯光熄灭、控制台红光断掉、低照度环境光和警灯轮廓表达，可生成且不让人物完全黑脸。",
      "fix_instruction": "若不通过，应补充可见光源以保持面部细节。"
    }
  ],
  "issues": [],
  "warnings": []
}
