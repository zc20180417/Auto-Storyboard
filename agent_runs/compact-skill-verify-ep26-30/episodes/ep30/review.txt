{
  "pass": true,
  "summary": "全部5组通过审核，无hard issue。5组分别覆盖敲钟上市、启动捐建、桥头感恩、新路畅行、星光团圆，时间轴连续，台词节奏合格，空间锁定完整，夜景光源正确，片尾星空意象收束自然。存在少量soft warning：第3组赵朵朵收尾台词偏慢、第3组对话密度偏高。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组有效台词：'敲钟'2字、'涨停了！上市即涨停！'8字、'妈！咱们家发大财啦！'9字、'这只是一个新起点'8字，合计27字，10秒，2.7字/秒。各时间段均未超过6.5字/秒上限。众人的'涨停了'和赵大雷的台词在4-7秒时间段内为连续反应，节奏合理。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组组首锁定写明赵朵朵和赵大雷并排站在桥头、村长在对面、村民围站两侧，全部人物在组首已有明确位置。单一物理空间（远县村口桥头），无跨空间问题。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "原剧本全部台词保留：大嫂'朵朵快坐，红烧肉刚出锅'、桂姨'多吃点，你在外头太累了'、赵大雷'来！咱一家人碰一个'、赵朵朵'祝咱们家的日子越来越红火'。关键动作保留：碰杯、咬红烧肉、抬头看星空。道具保留：红烧肉、玻璃杯、汽水。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "warning",
      "evidence": "赵朵朵'大家一起致富'6字/2秒=3.0字/秒，低于普通对白3.8字/秒下限。但该句为庆祝场景的收束语，原剧本标注'淡笑'，配合微笑表情和肢体语言有支撑，不构成hard issue。",
      "fix_instruction": "如需优化，可将该时间段延长至2.5秒（3.0→2.4字/秒仍在慢语范围），或在该句前加一个村民反应镜头间隔。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "warning",
      "evidence": "第3组12秒内5个时间段、4段对话（村长、村民、赵大雷、赵朵朵），平均每段对话间隔约2.5秒。对话密度偏高，但均为庆祝场景的简短感恩语句，无复合动作链、外部事件或情绪反转叠加，仍在可表演范围内。",
      "fix_instruction": "如需降低密度，可将村民鼓掌与赵大雷发言合并为同一时间段，腾出空间给环境镜头或反应。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组组尾：赵朵朵和赵大雷并排站在大路边，赵大雷搭着赵朵朵肩膀，面朝村内方向。第5组为独立夜景场景（县城四合院），属场景切换，不需要空间连续过渡。组首空间锁定完整描述了四合院葡萄架下的餐桌布局和四人位置。",
      "fix_instruction": "若发现同空间相邻组间状态跳变，应在上一组尾或下一组首补充人物位置和道具状态的过渡描述。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全部5组正文未出现模板化描述（'空间先被交代出来'等）、模型说明词（Seedance/HappyHorse相关）、参考图/首尾帧/视频延长等工程词。夜景光源使用暖色灯泡和星光，未出现日光、天光等昼夜错误。",
      "fix_instruction": "若发现污染词，应直接删除或替换为具体画面描述，不得保留模型说明词或模板化表达。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "赵朵朵'大家一起致富'字秒比3.0，低于普通对白3.8字/秒下限",
      "evidence": "有效字数6字，镜头2秒，字秒比3.0。原剧本标注'淡笑'，有微笑表情支撑但未明确慢语。",
      "fix": "可延长至2.5秒或在该句前加村民反应镜头间隔"
    },
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "generation_density",
      "problem": "12秒内5个时间段、4段对话，对话密度偏高",
      "evidence": "村长台词3-5.5秒、村民5.5-8秒、赵大雷8-10秒、赵朵朵10-12秒，平均每段间隔约2.5秒。",
      "fix": "可将村民鼓掌与赵大雷发言合并为同一时间段"
    }
  ]
}