{
  "pass": true,
  "summary": "seg03 保留朋友圈发现、龙腾酒店VIP厅、遗产猜疑和合法丈夫闹场筹码，手机道具连续。",
  "checked_groups": ["第5组", "第6组", "第7组"],
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
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "周美娟从衣兜掏出摔裂手机，举起展示朋友圈，组尾仍由周美娟持有。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "赵强约12字用3.5秒，周建国约20字用5秒，均低于6.5字/秒。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "保留周建国“走！明天咱们去闹一场！”和“我还是她合法丈夫，她敢不给我钱？”两句核心台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "朋友圈内容以手机屏幕上的VIP厅布置图和“周桂兰答谢宴”文字可视化呈现。",
      "fix_instruction": "若不通过，应补手机屏幕可见内容和角色反应。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾周美娟举手机，第6组首继续举着手机供赵强和周建国观看。",
      "fix_instruction": "若不通过，应补手机归属和屏幕朝向。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载周建国站起、提出闹场、强调合法丈夫三步，10秒内动作和对白清楚。",
      "fix_instruction": "若不通过，应把站起或合法丈夫台词拆到独立短组。"
    }
  ],
  "issues": [],
  "warnings": []
}
