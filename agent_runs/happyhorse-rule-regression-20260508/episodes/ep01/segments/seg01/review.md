{
  "pass": true,
  "summary": "seg01分镜保留第1集晒谷场陷害、红泥反证和水渠断流的关键剧情，HappyHorse包装、时长、口型和空间关系均可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
  ],
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
      "type": "script_fidelity",
      "evidence": "原剧本中赵百川指控林跃偷割集体电线、赵大强补刀、林建国和张桂兰替儿子求情的四句台词均保留在【音频】第二段和第三段，林跃睁眼但心声尚未提前。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "林跃心声写为画面中的林跃嘴唇闭合不做口型，后续林跃对赵百川问赃物、赵百川回答剪断电线、林跃追问那人呢均是现场开口并写清对象。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组14秒分为红泥展示、质问、村民反应和逼近赵大强四段，台词分布在音频段落中，没有在【运动】重复完整台词，单组节拍未超过4个强动作。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组单独切到村头水渠边，主体只锁定王四、水渠总闸和林家果园水渠，赵百川心声作为画外音处理，未把晒谷场人物混入同一现实空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "format",
      "result": "pass",
      "evidence": "第1组包含cut_id EP01-G01，标题总时长14秒、镜头数4个；组内只有【场景】【主体】【运动】【音频】【画面风格】与组尾衔接，没有Seedance默认字段。",
      "fix_instruction": "无需修复。若后续改稿，应继续避免**人物**、组首空间锁定、独立--neg等旧包装。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林跃重生心声标明嘴唇闭合不做口型；现场对话均写明林跃对赵百川、赵百川对林跃，声音来源清楚。",
      "fix_instruction": "无需修复。若改动心声，必须继续标明闭口、不做口型。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "第3组【主体】中明确林跃、李二狗、赵大强和众村民位置，李二狗在赵大强身旁且可被林跃逼近，后续抓脚踝动作具备人物可用性。",
      "fix_instruction": "无需修复。若调整站位，需保持李二狗在行动前已可见。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组结尾为李二狗鞋底被举给众人，第4组开头直接复述李二狗被迫抬脚、红泥鞋底朝向村民，关键道具和人物位置连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组12秒只承载扶住母亲、林跃与赵百川对视、赵百川递眼色、王四离场四个连贯轻中节拍，没有同时塞入新地点的水闸操作。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第6组使用HappyHorse专属包装，未出现参考图、首帧、技术参数、16:9、4K、BGM或独立--neg；负向词在【画面风格】内且为8项。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
