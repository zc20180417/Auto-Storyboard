{
  "pass": true,
  "summary": "第20集分镜完整保留安全屋并肩上会、董事会逼宫、投影证据、剪辑视频、赵明海作证、录音笔反击和秦越短信收束，格式与审核门槛均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "type": "dialogue_pacing",
      "evidence": "董事甲约18字用3.5秒，约5.1字/秒；周振邦约20字用3.5秒，约5.7字/秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS写成内心声音，镜头明确嘴唇闭合不做口型，没有误写成现场开口对白。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "evidence": "赵明海和法务在组首被锁定在会议室门外走廊一侧，随后先开门进入再由赵明海作证，人物可用性和入场顺序清楚。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "evidence": "录音笔在组首位于许知夏手边，0-3秒被按下播放冷库证词；周振邦手机在组首位于手边，8-11秒亮起秦越短信，道具转移和状态变化明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "会议名单、周氏代表、秦越旁听席、顾北辰提醒靶子和许知夏坚持露面的台词均保留。",
      "fix_instruction": "若压缩安全屋开场，不要删除秦越旁听席位或许知夏露面的决心。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "微型录音器从顾北辰手中放到许知夏掌心，组尾明确许知夏握住录音器，为第9组录音笔反击建立道具延续。",
      "fix_instruction": "若改写手部动作，应保留录音器交付和许知夏持有结果。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "许知夏反问、周振邦沉脸、周振邦问证据、助理开投影分为四段，投影证据没有和长对白挤在同一瞬间。",
      "fix_instruction": "若增加董事反应，应保持投影打开独立阶段。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "全场哗然、董事乙询问、许知夏点破中间人、周振邦起身反击四个强节拍在15秒内顺序推进，未超过片段负载。",
      "fix_instruction": "若加入更多投影细节，应拆出证据展示组，避免本组过载。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "剪辑视频作为投影画面，顾北辰OS作为内心声音且闭口，董事甲对白有真实对象顾北辰。",
      "fix_instruction": "若把OS改为对白，必须写成顾北辰对谁说并调整剧情语义。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾许知夏看向门口，第7组组首延续她面向门口，并写法务和赵明海在门外，随后入场作证。",
      "fix_instruction": "若调整入场位置，应同步修改第6组组尾和第7组组首。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周振邦怒吼明确对赵明海说，赵明海反咬明确对周振邦说，没有假对象或对象缺失。",
      "fix_instruction": "若改成群体质问，应写清每句对白对象。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第9组禁止项锚定录音笔、秦越、周振邦手机和赵明海法务站位，均是本组关键道具和人物风险，没有泛泛项。",
      "fix_instruction": "若删除秦越短信，应同步删除秦越相关禁止项。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文未出现模型说明词、参考图占位、模板编号、广告词或非分镜正文，格式为自然分镜组。",
      "fix_instruction": "若追加风格或负面词，应交给收集阶段，不写入 final。"
    }
  ],
  "issues": [],
  "warnings": []
}
