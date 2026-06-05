{
  "pass": true,
  "summary": "seg02保留露台休养、保姆送草莓、沈清入座和母女对阳光的对白，单一空间与道具状态清楚。",
  "checked_groups": ["第3组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保姆送新鲜草莓、周桂兰让张妈歇会儿、沈清问阳光、周桂兰感叹过去不敢想的日子均被保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "保姆约15字用3秒，周桂兰约13字用2秒接近6.5字/秒但未超过，末段两句合计约31字用5秒，口型承载仍在上限内。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "evidence": "周桂兰和保姆在组首可见，沈清在7-10秒先从露台入口入场并坐下，之后才开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组全程为公寓露台，组首明确藤椅、小圆桌、露台入口和在场人物位置。",
      "fix_instruction": "如不通过，应拆出室内空间或补足入口位置。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "草莓盘由保姆手中端来并放到小圆桌，茶杯始终在周桂兰手中，文件在沈清手中。",
      "fix_instruction": "如不通过，应补充草莓盘放置和文件归属。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每段分别承载环境轻起、保姆端盘、周桂兰回应、沈清入座、母女对白，没有一个时间段塞多段主动作。",
      "fix_instruction": "如不通过，应拆分端盘、入座或对白段。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图占位或批量化描述。",
      "fix_instruction": "如不通过，应删除工程词和模板化句子。"
    }
  ],
  "issues": [],
  "warnings": []
}
