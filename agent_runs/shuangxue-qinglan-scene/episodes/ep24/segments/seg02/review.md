{
  "pass": true,
  "summary": "seg02 保留闯入、撒泼未遂、律师带安保隔离和录像取证，动作分段清楚。",
  "checked_groups": ["第1组"],
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
      "evidence": "原剧本中周建国带周美娟和赵强撞开保安、衣服皱乱、准备坐地撒泼、律师和两名安保隔离并录像取证均被保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "10-15秒律师约31字对白，用5秒承载，约6.2字/秒，低于6.5硬上限，并有周建国僵住作为同步反应。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "evidence": "闯入、反差展示、坐地未遂、安保隔离、律师警告分成5个时间段，单段只有一个主动作或一个对白节拍。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "周建国、周美娟、赵强、律师、安保人员、沈清和周桂兰都在组首有位置或可入场路径，行动前可用。",
      "fix_instruction": "若不通过，应在组首或前半段补足人物位置和入场。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机录像由律师侧安保举起并在组尾继续对准周建国，未无故消失。",
      "fix_instruction": "若不通过，应补手机由谁持有及镜头对准对象。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项针对周建国坐地、周美娟赵强越线、律师手机、沈清站位，均为本组具体风险。",
      "fix_instruction": "若不通过，应删除泛泛项并锚定本组人物和道具。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模板编号、工程占位、模型说明或不可视抽象主承载。",
      "fix_instruction": "若污染，应改为可见的短剧画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
