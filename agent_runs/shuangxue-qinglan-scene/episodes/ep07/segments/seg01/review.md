{
  "pass": true,
  "summary": "seg01 保留手机号变更、旧手机和短信提醒确认三处关键证据，台词对象、内心旁白闭口和柜台空间连续性均通过。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "沈清询问绑定号码和柜员回答尾号8864、两年前7月15号变更均按原剧本保留，柜台屏幕和银行卡位置没有改变。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "沈清内心旁白“那正好是我第二个月开始打八千块钱的日子！”写明嘴唇闭合不做口型，未被误写成现场开口。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "柜员台词约18字承载在0-4秒，约4.5字/秒，属于自然柜台答复；第3组总时长8秒是单句证据确认后的短反应，短组理由成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确沈清、周桂兰和柜员分别位于柜台两侧，身体朝向和柜台屏幕、银行卡位置清楚。",
      "fix_instruction": "若不通过，应补足人物位置、身体朝向和柜台关键道具状态。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "老年机从周桂兰口袋取出后递给沈清，组尾写明沈清持有老年机；银行卡仍留在柜台凹槽旁。",
      "fix_instruction": "若不通过，应补充老年机递接或银行卡位置锚点。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含递出老年机、沈清低声确认日期、内心旁白和追问柜员四个同一证据链节拍，每段只承载一个主动作或声音块。",
      "fix_instruction": "若不通过，应拆分内心旁白或追问，不应压缩口型时间。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部柜员准备回答，第3组组首仍在同一柜台前，沈清持有老年机，银行卡仍在柜台凹槽旁。",
      "fix_instruction": "若不通过，应在第2组尾或第3组首补充柜员、老年机和银行卡状态。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组只有柜员确认短信去向和母女反应两个轻节拍，没有把后续刘美娟入场提前塞入本组。",
      "fix_instruction": "若不通过，应将外部入场另起组。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定老年机、内心旁白和银行卡三项本组关键风险，数量为3条且不与剧情矛盾。",
      "fix_instruction": "若不通过，应删除无锚点泛泛词或补成本组道具与声音风险。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图、占位符或批量模板化描述。",
      "fix_instruction": "若不通过，应删除工程词和模板说明，只保留自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
