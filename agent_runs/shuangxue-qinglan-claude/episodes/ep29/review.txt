{
  "pass": true,
  "summary": "EP29分镜稿忠于原剧本，台词承载指向清晰，时空锁定完整，组间状态连续，无硬问题。",
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
      "evidence": "周建国台词22字÷4秒=5.5字/秒（情绪对白范围），周桂兰台词27字÷5秒=5.4字/秒（情绪对白范围），均未超过6.5硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间商业街十字路口，车内外同场景；组首锁定写明沈清驾驶座、周桂兰后座车窗关闭、周建国车外前景中央，均为静态结果态。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本'周桂兰拿出一张百元大钞，递给外面的司机''司机将钱塞给周建国，车窗缓缓升起。绿灯亮起，汽车扬长而去''周建国站在雪地里，攥着那一百块钱，望着远去的车影，流下了悔恨的眼泪'均完整保留，台词顺序、说话对象和道具归属未改变。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周建国和周桂兰的台词均为画面内真人开口对白，写明了'A对B说道'指向，无心声/画外音混入。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组0-3秒同时包含周桂兰掏钱动作和台词，但两者属于同一事件链（掏钱→递钱→说话），动作与台词同步完成，未抢画面焦点；后续3个时间段各承载单一主动作。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾写明'周桂兰仍在后座、车窗仍半开、周建国仍站在车外原地'；第2组组首写明'车窗仍处于半开状态，周桂兰位于后座，周建国位于车外画面前景中央'，人物位置、车窗状态完全一致。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "百元大钞从周桂兰手中→沈清接过→塞进周建国手中→周建国攥紧，全程有递出、接住、攥紧的可见过渡；汽车从停在路口→驶离路口→车影拉长→驶离画面，状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每组每个时间段只承载一个主动作或一个连续对话节拍：0-3秒掏钱+递钱+台词（同一事件链），3-4秒车窗升起，4-7秒汽车驶离，7-10秒周建国流泪低头。沈清只完成接钱递钱的辅助动作，未抢主角戏份。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组视频禁止项'周桂兰提前出车窗、周建国位置跳变到车内、沈清提前离开驾驶座'为3条本组特有错误，锚定人物名和场景；第2组视频禁止项'百元大钞从周建国手中消失、汽车未驶离路口、周桂兰出现在车外'为3条本组特有错误，锚定道具和人物。无模板占位或泛泛词。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
