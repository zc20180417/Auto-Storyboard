{
  "pass": true,
  "summary": "seg03完成美娟赵强入场、周建国赖账、沈清拿出二十四个月流水并宣告对账，动作拆分清楚。",
  "checked_groups": ["第7组", "第8组", "第9组", "第10组"],
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
      "group": "第7组",
      "type": "character_availability",
      "evidence": "周美娟和赵强在组首位于里屋门帘后方空间内，3-6秒先入场，6-10秒周美娟才开口。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "周建国“钱进了这个家，就是这个家的钱！你报警抓我啊！”约22字承载5秒，约4.4字/秒，未超速。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "evidence": "沈清背包在组首挂在身侧，2-5秒取出银行流水，5-10秒铺满大理石茶几，授权委托书被推到一侧但仍可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第7组只有周家正屋客厅一个物理空间，里屋门帘后方作为同一客厅入口区域被明确列出。",
      "fix_instruction": "若失败，应把里屋入场拆成单独组或明确门帘位置。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留周建国指着沈清鼻子耍赖和“你报警抓我啊”台词，没有新增肢体冲突。",
      "fix_instruction": "若失败，应删除打人或抢文件等新增动作。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "冷笑、拉开背包取流水、铺开账单分成三个时间段，每段只承载一个主动作链。",
      "fix_instruction": "若失败，应拆开取出和铺开动作。"
    },
    {
      "group": "第10组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清两句摊牌均明确对周建国、周美娟和赵强说道，符合三人对账语境。",
      "fix_instruction": "若失败，应明确沈清对三人说。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第10组只承载两句摊牌对白和手按账单的轻动作，11秒容量充足，不靠停顿撑时长。",
      "fix_instruction": "若失败，应压缩普通反应或保留短组。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第9组禁止项4条锚定银行流水、授权委托书、周美娟、赵强和背包，未使用泛泛错误词。",
      "fix_instruction": "若失败，应替换无锚点或与剧情冲突的禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
