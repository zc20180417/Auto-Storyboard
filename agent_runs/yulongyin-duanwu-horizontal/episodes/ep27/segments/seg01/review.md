{
  "pass": true,
  "summary": "seg01两组已对照原剧本审查，保留爸爸跃下龙背、刀疤男威胁、爸爸反击、水漩涡封住遥控器和刀疤男崩溃等关键内容，横屏轴线清楚。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "第1组将爸爸固定在画面左中景、刀疤男固定在右中景，炸药背心和遥控器在右侧可见，水龙占左后方，符合16:9左右对峙。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组承接第1组尾部遥控器暴露状态，水漩涡从左向右进入遥控器，后续刀疤男仍攥着失效遥控器，关键道具归属连续。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "刀疤男威胁台词约23字放在4秒，爸爸台词约12字放在3秒，均低于硬上限且有动作与反应承载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本中爸爸跃下龙背、刀疤男要求交出怪物、爸爸回应背后的人救不了命均保留，未新增改变剧情的动作。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爸爸持续在画面左侧，刀疤男持续在右侧，拳风和水漩涡从左向右运动，视线与动作轴线稳定。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒内分为出拳、水漩涡封遥控器、疯狂按按钮、崩溃喊话四个节拍，动作链单一且可表演。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
