{
  "pass": true,
  "summary": "ep02 七组均保留原剧本关键台词、道具动作和反转信息，并已按 HappyHorse 专属外壳输出，未发现硬问题。",
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
      "type": "script_fidelity",
      "evidence": "原剧本中林家小屋、冷饭、干涸田垄、林建国砸桌怒吼和抓起锄头均保留；台词“赵百川这老王八蛋！这是要逼死我们啊！”在【音频】第二段完整保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "张桂兰对林建国哭喊、林建国对张桂兰和林跃激动喊话、林跃对林建国平静劝阻和承诺，均写明说话对象，没有假对象或心声混用。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "本组承载掏出协议、两句恳求、赵百川接协议、赵大强嘲讽四个清晰节拍，15秒内按0-3、3-7、7-11、11-15秒分配，动作和对白能自然完成。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "evidence": "林跃在协议末尾加极小字的动作通过身体遮挡、笔尖短促反光、纸面纹理不可读来表现，避免新增可读文字内容，同时保留剧情暗手。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "林跃OS被写成内心旁白，画面中的林跃嘴唇闭合、不做口型；门内赵大强笑声作为远处闷响存在，声音来源清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "【场景】和【主体】锁定林家小屋、饭桌、窗外田垄、三人站位与锄头位置；本组只发生在同一室内空间。",
      "fix_instruction": "无。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾林建国握锄头朝门口冲去，第2组开头复述林建国位于门口方向并握锄头，张桂兰和林跃的位置也能自然接上。",
      "fix_instruction": "无。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵百川和赵大强开场已在办公室内，林跃在3-6秒先推门入场，之后才接受赵百川嘲讽和开口认错。",
      "fix_instruction": "无。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "红色印泥盒、赵百川催促按手印、林跃眼眶泛红、偷偷在协议末尾加极小字、赵大强催促均与原剧本一致。",
      "fix_instruction": "无。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全组使用【场景】、【主体】、【运动】、【音频】、【画面风格】结构；【画面风格】未包含16:9、9:16、秒数、s单位、4K、1080p、720p等生产界面参数，未出现@图、Image、参考图、首帧或独立--neg。",
      "fix_instruction": "无。"
    }
  ],
  "issues": [],
  "warnings": []
}
