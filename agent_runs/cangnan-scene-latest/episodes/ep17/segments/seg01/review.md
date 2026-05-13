{
  "pass": true,
  "summary": "seg01分镜保留陆凡拦截马行长、保安围拢和播放回扣录音的关键动作与台词，格式和节奏通过。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "原剧本中马行长下班、陆凡挡住并要求撤回十亿汇款单，分镜按3-7秒和7-13秒保留两句对白与拦路动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "马行长约18字情绪对白安排4秒，陆凡约10字短句安排3秒并带手机动作，字秒比低于6.5且未拖慢。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "陆凡在组首持有手机，7-10秒抬起手机，10-15秒按下播放键，录音来源和手机归属连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "马行长对陆凡说道、陆凡对马行长说道，画面内对白对象明确。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实说话对象。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "小李供述作为手机扬声器录音出现，画面人物只做反应，没有把录音写成现场口型。",
      "fix_instruction": "若不通过，应写明录音从手机传出，并让画面人物闭口反应。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列出陆凡、马行长、保安的位置、朝向和手机、警棍、公文包，保安在说话前已在背景可用。",
      "fix_instruction": "若不通过，应在组首补充人物位置、身体朝向和关键道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
