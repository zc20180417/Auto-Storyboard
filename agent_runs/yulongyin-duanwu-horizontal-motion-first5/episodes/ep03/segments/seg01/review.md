{
  "pass": true,
  "summary": "seg01 已对照剧本 3-1、横屏生成规则和当前分镜逐组审查，台词、道具连续、夜间光源、运镜设计和心声音画分离均可交付。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留反锁房门、掏出半个干硬白馒头、对云宝说“你饿不饿？我只有这个了，你尝尝。”、掰碎馒头丢进水壶和云宝吞渣的动作顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“慢点吃，别噎着。我明天再去给你找吃的。”安排在3秒内，约17字/3秒，字秒比约5.7；“你从云里来，又是个宝贝，以后就叫你云宝吧。”安排在4秒内，约20字/4秒，口型可承载。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "天天OS写为画外心声，镜头明确画面中的天天嘴唇闭合、不做口型，避免把心声误写成现场开口。"
    },
    {
      "group": "第1组",
      "type": "camera_motion",
      "evidence": "每个时间段都有运镜设计，固定机位用于稳定门、小桌、水壶和天天口型，轻微推近只用于馒头渣入壶的道具过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "房门在左后方，小桌和透明水壶在右前方，天天从左门口走向右侧小桌，横屏左右路线清楚。",
      "fix_instruction": "若不通过，应补充房门、小桌、水壶和天天走位的左中右关系。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "透明水壶从第1组小桌右前方延续到本组中央偏右，天天始终托近水壶，云宝在壶底翻滚，没有道具跳变。",
      "fix_instruction": "若不通过，应补充天天拿起、放下或托住水壶的可见过渡。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "0-3秒固定壶口锁住喷雾方向，3-6秒轻微后拉交代水雾落点，6-11秒固定机位稳定心声和闭口状态。",
      "fix_instruction": "若不通过，应为每个时间段补足具体运镜类型和服务目的。"
    }
  ],
  "issues": [],
  "warnings": []
}
