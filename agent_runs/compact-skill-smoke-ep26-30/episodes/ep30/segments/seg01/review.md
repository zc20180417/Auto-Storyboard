{
  "pass": true,
  "summary": "seg01对照第30集原剧本、竖屏生成规则和Seedance参考层完成审核，三组均保留原动作、台词顺序与空间切换，没有硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "evidence": "证券交易所段保留赵朵朵举鼓槌、说“敲钟”、钟声、大屏股价飙升、全场欢呼、赵大雷抱桂姨，以及赵朵朵交代希望小学第一站在远县北沟村的完整顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组4.5-8.5秒承载“乡亲们以后运果子再也不愁了！”和“大家一起致富。”约21个有效字，4秒约5.3字/秒；10.5-15秒约24个有效字，4.5秒约5.3字/秒，均低于6.5硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组始终在夜间县城四合院葡萄架下，组首锁定桌面、红烧肉、玻璃杯、汽水和四名家人位置，后续端菜、夹肉、碰杯和抬头看星空都在同一空间内完成。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵朵朵分别对在场众人和助理说话，助理对赵朵朵提问，赵大雷对桂姨喊话，全场欢呼也明确为全场众人发声，没有假对象。",
      "fix_instruction": "若出现无对象开口，应改为具体对助理、对桂姨、对众人或由人群发声。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组共4个时间段，强节拍为村长感谢、村民鼓掌、赵大雷说明道路用途、赵朵朵回应致富、重卡驶过与回家吃饭问答，桥路展示和对白分段承载，没有把跨空间动作塞入同组。",
      "fix_instruction": "若显得过载，应拆出重卡路面展示或回家吃饭问答为独立组。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组从葡萄架餐桌开场到组尾围桌收束，红烧肉、汽水杯和家人座位连续，杯子碰响后接赵朵朵吃肉看星空，状态自然收尾。",
      "fix_instruction": "若组尾缺少状态，应补明赵朵朵端杯、红烧肉冒热气和家人围桌位置。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜只写短剧现场动作、声音来源、光影与负向提示，没有模板编号、官方占位符、参考图、自动分镜、视频延长或广告式语气。",
      "fix_instruction": "若出现模型说明词或模板占位符，应删除并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
