{
  "pass": true,
  "summary": "seg03把披衣回程、轿车溅水保护、刘美娟抱小雨下车、金镯识别和当街逼问拆开，外部事件与OS口型处理清楚。",
  "checked_groups": ["第9组", "第10组", "第11组", "第12组", "第13组"],
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
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "白色轿车逼近、溅水、沈清拉母亲到内侧、车辆急刹分成四段，保护动作写清沈清挡在周桂兰靠车一侧。"
    },
    {
      "group": "第12组",
      "type": "audio_mouth_sync",
      "evidence": "两句沈清OS均写为沈清嘴唇闭合不动的内心声音，未误写成现场开口。"
    },
    {
      "group": "第13组",
      "type": "dialogue_pacing",
      "evidence": "沈清两句质问分别给3.5秒，刘美娟反驳给3秒，争吵对白字秒比低于6.5且对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第11组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "刘美娟抱小雨下车，小雨夸新车舒服，刘美娟炫耀马术班，原剧本台词和关系未改写。",
      "fix_instruction": "若失败，应恢复小雨和刘美娟的原台词顺序与母女关系。"
    },
    {
      "group": "第12组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "古法金镯始终在刘美娟右手手腕，从露出、反光到被袖口遮住有连续过渡。",
      "fix_instruction": "若失败，应补金镯位置、遮袖动作或避免转移到其他人物身上。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定白色轿车、沈清、周桂兰、大衣和水坑，避免保护站位错误且不阻止原剧本溅水急刹。",
      "fix_instruction": "若失败，应把禁止项改为本组车辆和保护关系的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
