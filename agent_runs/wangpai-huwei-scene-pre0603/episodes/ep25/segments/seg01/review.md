{
  "pass": true,
  "summary": "seg01 已按原剧本完成楼梯间撤离反击、火场闪回、天台录音取证和秦越放弃挣扎八组竖屏分镜，未发现阻断交付的 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
      "evidence": "许知夏低声说明合并进度约22字分配3.5秒，约6.3字/秒，属于紧急低声技术汇报的可执行范围；顾北辰短句2秒完成。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "搭档VO被写成回忆闪回中的画外声，顾北辰OS写明嘴唇闭合不做口型，火场和楼梯间以闪回结束分开。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "evidence": "秦越冲向许知夏、顾北辰横跨挡人、两人撞上护栏、秦越嘶吼和许知夏反击分别拆为连续时间段，保护站位明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "顾北辰左拳、右肘、侧踢和旧伤牵动均保留，结尾收住致命一击，未改成杀伤或逃跑剧情。",
      "fix_instruction": "若不通过，应恢复原剧本的动作顺序和收住杀意结果。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第4组固定在启元资本天台，秦越位于出口前，顾北辰挡在许知夏和沈曼前方，直升机为同一空间背景道具。",
      "fix_instruction": "若不通过，应拆出非天台空间或重写组首人物站位。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "年轻秦越录音通过手机扬声器播放，秦越本人嘴唇闭合不做口型，沈曼直播取证设备有可见载体。",
      "fix_instruction": "若不通过，应明确录音来源并删除秦越现场开口承载录音的写法。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定秦越、许知夏、顾北辰、直播设备和护栏，共4项，均为本组关键动作风险。",
      "fix_instruction": "若不通过，应把泛泛禁止词替换为本组人物、道具和动作风险。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "原始交接记录从林元背景阴影中的手里到举起展示再到组尾持续可见，未突然转移给其他人。",
      "fix_instruction": "若不通过，应补充林元持有、举起和保留文件的连续状态。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾林元举文件、秦越被挡住去路、警笛逼近；第8组首承接为林元仍举文件、民警封锁出口、秦越仍在顾北辰身前。",
      "fix_instruction": "若不通过，应在第7组尾或第8组首补足文件、秦越位置和民警封锁状态。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "许知夏的技术进度汇报接近偏快区间。",
      "evidence": "台词约22字分配3.5秒，约6.3字/秒，语境是低声急促汇报但仍需演员清晰吐字。",
      "fix": "如后续强审要求更稳，可继续压缩逼近动作并给该句增加0.5秒。"
    }
  ]
}
