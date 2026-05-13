{
  "pass": true,
  "summary": "已对照第2集原剧本、生成规则和当前 seg01 分镜逐组审核，台词、动作、空间锁定、口型承载和时间轴均可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组"
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中张桂兰哭喊、林建国喊“我今天非跟他拼了不可！”，林跃按住肩膀拿下锄头并说“爸，冲动解决不了问题。”，随后保留“那片果园是我们的命根子啊！”和“我去解决。”，分镜顺序与动作因果一致。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "3-7秒承载林跃“我愿意……把果园转让出来。”约12个有效字，4秒约3.0字/秒，但包含双手递协议和恳求表演；7-10秒承载“只求您，把水给我们家的田通上。”约15个有效字，3秒约5.0字/秒，符合哀求口型节奏。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "保留赵百川拿出红色印泥盒并催“按手印吧。”，林跃眼眶泛红、捏笔颤抖、俯身用身体挡住对方视线并在协议末尾加小字，赵大强催“磨磨蹭蹭的干什么？快点按！”，没有新增改变剧情的动作。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "林跃 OS 被写成“林跃的内心旁白响起”，9-13秒明确林跃嘴唇闭合不做口型；画面主体是门外林跃反应，门内赵大强举协议狂笑作为可见载体和剧情对照。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组负载为饭菜冷清交代、林建国砸桌怒骂、抄锄头要冲出三类主要节拍，12秒内4段承载，环境交代仅2秒，未用静默拖时。",
      "fix_instruction": "无需修复；若后续压缩，应保留砸桌、怒骂和抄锄头三个关键节点。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵百川对林跃说道“呦，这不是林跃吗？怎么，想通了？”，林跃对赵百川恳求认错，赵大强对林跃嘲讽，所有现场开口均有真实对象。",
      "fix_instruction": "无需修复；若调整镜头，仍需保持三句对白的说话对象和先后顺序。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部林跃放下笔、印泥盒在协议旁，第6组首部林跃手指靠近印泥盒并看向落款处，赵百川和赵大强仍在桌边盯着，手印动作衔接自然。",
      "fix_instruction": "无需修复；若移动人物位置，需同步调整第5组组尾和第6组组首。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第7组场景为办公室门口与门内可见区域，办公室门半开，林跃在门外前景，赵百川和赵大强在门内背景，属于同一连通门框空间内外关系，不是无标识跨场景跳切。",
      "fix_instruction": "无需修复；若改成室外道路或村委会外景，应单独另起一组或明确转场。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有出现模型说明词、模板编号、参考图、首尾帧、自动分镜或官方占位符；OS 以自然分镜语言承载。",
      "fix_instruction": "无需修复；继续避免写入任何模板或模型工程说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
