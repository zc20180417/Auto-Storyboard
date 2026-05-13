{
  "pass": true,
  "summary": "已对照第2集剧本、generator规则和HappyHorse包装要求完成审稿，7组均保留原剧情与台词，未发现阻断交付的硬问题。",
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "林建国怒骂、张桂兰劝阻、林建国回喊三句台词合计约40个有效字，集中在5.5-12秒的冲突动作段承载，约6.2字/秒，未超过6.5字/秒硬上限，且砸桌和抄锄头动作均有独立表演时间。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保留林跃掏出协议、双手递给赵百川、提出转让果园并请求通水、赵百川得意接协议、赵大强嘲讽怂包的原剧本顺序和人物关系。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "本组始终在村委会办公室办公桌前，赵百川、赵大强、林跃的位置、身体朝向、协议、印泥盒和笔的归属均在【主体】中锁定，暗写小字发生在同一桌面空间。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "林跃OS被写为内心旁白，画面中林跃位于门外走廊且嘴唇闭合不做口型；办公室内只保留赵大强狂笑和赵百川低笑，不把心声写成现场开口。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "evidence": "全组使用【场景】、【主体】、【运动】、【音频】、【画面风格】HappyHorse外壳，未出现Seedance默认包装、技术参数、参考图占位、独立负向行或模型说明词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组强节拍为砸桌怒骂、抄起锄头、张桂兰拉拦并回喊，3个主要节拍分布在12秒内，动作和对白没有互相挤压。",
      "fix_instruction": "若后续出现仓促，应优先拆出抄锄头与拉拦段，不能删原台词。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾林建国手握锄头被张桂兰拉在门口，第2组开头复述林建国在门口手握锄头、张桂兰仍拉着胳膊，林跃从右侧前景上前后再按肩拿下锄头，状态连续。",
      "fix_instruction": "若不通过，应在第2组【主体】补林建国、张桂兰和锄头的具体起始状态。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵百川和赵大强开组已在办公室可见，林跃在3-6秒推门进入并停到桌前，三人都在说话前具备可见位置和对话对象。",
      "fix_instruction": "若林跃未入场即说话，应先补推门入场动作。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留赵百川拿红色印泥盒并催促、林跃眼眶泛红手抖、身体遮挡后飞快加极小字、赵大强催促的关键剧情，没有新增改变协议内容的动作。",
      "fix_instruction": "若不通过，应只修暗写小字的遮挡和催促动作，不重写其他组。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林跃旁白来自OS，运动段明确嘴唇闭合不做口型；赵大强狂笑是办公室现场声音，来源和可见人物一致。",
      "fix_instruction": "若不通过，应把OS改为内心旁白并补闭口反应，不能让林跃现场说出心声。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "所有组均未使用【技术参数】、比例、分辨率、standalone --neg、参考图、首帧尾帧、BGM或Seedance默认字段，负向词压缩在【画面风格】内。",
      "fix_instruction": "若出现污染，应按HappyHorse profile把人物、场景、道具和负向词分别并入【主体】与【画面风格】。"
    }
  ],
  "issues": [],
  "warnings": []
}
