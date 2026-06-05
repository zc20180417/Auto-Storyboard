{
  "pass": true,
  "summary": "seg02保留短信暴露、周美娟试图关机、沈清旧手机录像和逼她亮屏的连续证据推进，无硬问题。",
  "checked_groups": ["第2组", "第3组"],
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留周美娟“不是我！是垃圾短信！”、拉包关机动作和沈清“这么巧？刚好是垃圾短信？”的反击。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "沈清对周美娟说“周美娟，拿出手机”和“躲什么？把屏幕亮给大家看！”，周美娟对沈清喊“你拍什么拍！关掉！”，对象明确。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "周美娟名牌包中露出亮屏手机，随后第3组组首延续为周美娟一手握手机一手抓包，沈清旧手机也延续为录像道具。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "短信提示音来自周美娟包内手机，现场台词均由画面人物开口，不存在心声或电话音误口型。",
      "fix_instruction": "无须修复；若改动需保持短信声与包内手机绑定。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只承载沈清举镜要求拿手机、周美娟拒拍、沈清逼她亮屏三个连续冲突节拍，11秒内动作和台词可执行。",
      "fix_instruction": "无须修复；不要再加入抢夺或肢体冲突。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾沈清举旧手机录像、周美娟握亮屏手机，第3组组首直接复述该状态。",
      "fix_instruction": "无须修复；保持旧手机和周美娟手机的归属不跳变。"
    }
  ],
  "issues": [],
  "warnings": []
}
