{
  "pass": true,
  "summary": "seg04分镜忠实原剧本，转账悬念节奏紧凑，8秒短组作为悬念收尾合理。",
  "checked_groups": ["第4组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "沈清6字÷2秒=3字/秒，周建国5字÷2秒=2.5字/秒，沈清7字÷2秒=3.5字/秒，沈清6字÷2秒=3字/秒含按下确认动作，均在合理范围内。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首列出全部5名在场人物位置，沈清手机屏幕亮着显示转账界面，道具状态从上一组连续。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "4句对白全部保留原词，确认转账两元的关键动作忠实原剧本，所有人屏息盯手机的反应完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内现场开口，无心声/画外音混用。",
      "fix_instruction": "若不通过，应补充说话人和对象指向。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "强节拍2个（周建国追问+沈清宣布转账、沈清按下确认），8秒容量充足，悬念收尾节奏紧凑。",
      "fix_instruction": "若不通过，应延长组时长或拆分强节拍。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首从上一组组尾继承：沈清手机屏幕亮着显示转账界面，周美娟在原位，赵强在身后。",
      "fix_instruction": "若不通过，应在组首补充具体人物位置和道具状态。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机在沈清手中保持连续，从输入转账信息到按下确认，屏幕状态从亮着变为转账成功提示。",
      "fix_instruction": "若不通过，应补充道具状态过渡动作。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作，无过载。",
      "fix_instruction": "若不通过，应拆分过载时间段。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为悬念收尾组，动作简单明确，省略视频禁止项合理。",
      "fix_instruction": "若不通过，应补充2-5个本组特有视频禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
