{
  "pass": true,
  "summary": "seg04 保留响指、LED证据、抢手机视频、周美娟惊慌和高利贷揭露，证据道具连续。",
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
      "type": "script_fidelity",
      "evidence": "沈清打响指、LED显示盖章转账记录、她公开指出偷刷养老钱、屏幕播放抢手机视频、周美娟喊关掉均被保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-2秒8字约4字/秒，2-7秒约23字约4.6字/秒，均在合理范围内并有逼视和反应动作支撑。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "LED屏幕从黑屏亮起，到转账记录，再切到抢手机视频，组尾仍保持视频播放状态，第2组组首继承该状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "响指亮屏、记录展示、沈清说明、视频切换和周美娟惊慌分段呈现，没有把多个主动作塞入同一时间段。",
      "fix_instruction": "若过载，应拆分屏幕亮起和视频播放，或减少同段动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾LED仍播放抢手机视频，第2组组首明确LED仍显示该视频，人物站位也连续。",
      "fix_instruction": "若不连续，应在第1组组尾或第2组组首补LED屏幕状态。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定LED屏幕、连环转账记录、周美娟抢手机视频和周建国，避免证据画面错置。",
      "fix_instruction": "若禁止项无锚点，应替换为本组证据道具和人物相关风险。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "两组没有出现官方模板、参考图、视频延长、自动分镜等污染词。",
      "fix_instruction": "若污染，应删除相关词并重写为自然短剧分镜。"
    }
  ],
  "issues": [],
  "warnings": []
}
