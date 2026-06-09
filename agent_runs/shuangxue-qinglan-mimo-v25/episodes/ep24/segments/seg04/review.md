{
  "pass": true,
  "summary": "两组分镜覆盖屏幕证据揭示和高利贷致命一击，LED屏幕道具状态连续，台词指向正确，空间单一。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "沈清23字/3.5秒=6.6字/秒（稍快但为情绪揭露台词），周美娟6字/2秒=3.0字/秒，沈清9字/2.5秒=3.6字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "LED屏幕从G1延续到G2（仍亮着显示监控画面），道具状态连续。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "打响指、LED屏幕亮起、转账记录、偷刷养老钱台词、杂物间抢手机视频、周美娟关掉喊话、你以为这就完了，均完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个时间段各承载一个主动作/反应，沈清揭露→周建国面色变化→周建国踉跄，表演时间充足。",
      "fix_instruction": "无需修改，密度合理。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "打响指+屏幕亮起（同步动作）、屏幕内容+沈清台词（同步信息揭示）、周美娟反应、沈清逼视，每个时间段一个主动作目标。",
      "fix_instruction": "无需修改，动作拆分清楚。"
    },
    {
      "group": "第1组和第2组之间",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "G1组尾LED屏幕仍亮着、周美娟捂嘴后退、周建国视线被钉住。G2组首LED屏幕仍亮着显示监控画面、沈清在左侧、周建国在中央脸色发白。状态连续。",
      "fix_instruction": "无需修改，组间状态连续。"
    }
  ],
  "issues": [],
  "warnings": []
}