{
  "pass": true,
  "summary": "seg04保留沈清扔出离婚协议、周建国拒签、沈清转向祖宅强执和张总确认强制拍卖的完整压迫链。",
  "checked_groups": ["第10组", "第11组", "第12组"],
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
      "type": "prop_continuity",
      "evidence": "文件和签字笔由沈清挎包取出，扔到周建国脸前并在组尾停在地毯上，后续组可继续使用。"
    },
    {
      "group": "第11组",
      "type": "script_fidelity",
      "evidence": "周建国识别离婚协议书、质问净身出户、拒绝签字和强调合法丈夫的台词均按原顺序保留。"
    },
    {
      "group": "第12组",
      "type": "dialogue_pacing",
      "evidence": "沈清约31字/6秒约5.2字/秒，张总约29字/6秒约4.8字/秒，均低于6.5字/秒且符合压迫对白节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第10组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "取出文件笔、扔到脸前、周建国看文件分成三个时间段，文件和笔落点清楚。",
      "fix_instruction": "若不通过，应拆开扔文件和周建国阅读动作。"
    },
    {
      "group": "第11组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第10组尾文件笔在周建国脸前，第11组首复述离婚协议书和签字笔位于地毯上。",
      "fix_instruction": "若不通过，应在第11组首补文件和笔位置。"
    },
    {
      "group": "第12组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组内固定在宴会厅，没有切到祖宅室外画面，祖宅只通过沈清和张总台词推进。",
      "fix_instruction": "若不通过，应删除现实空间切换或标注为屏幕画面。"
    },
    {
      "group": "第12组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "祖宅强执组的禁止项锚定周建国、祖宅、法律文书、律师和张总台词，避免关键道具与空间误生成。",
      "fix_instruction": "若不通过，应补充本组具体人物和道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
