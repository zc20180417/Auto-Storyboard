{
  "pass": true,
  "summary": "ep01 分镜忠实覆盖晒谷场陷害、林跃苏醒反击、红泥鞋底举证和水渠关闸，HappyHorse 【画面风格】外壳已去除生产界面参数，未发现 hard issues。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
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
      "evidence": "原剧本中赵百川怒斥、赵大强嚣张附和、林建国嘶吼和张桂兰哭喊四句关键台词均保留，人物位置也对应晒谷场当众围观。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "林跃 OS 被写成内心旁白，且镜头描述明确画面中的林跃嘴唇闭合、不做口型，没有误写成现场开口。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "第5组 15 秒承载红泥证据、两句质问、村民反应、赵大强反驳和林跃低语；4 个时间段分别为 4、4、3、4 秒，短句交锋语速合理。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "第7组明确切到村头水渠边，以王四和水渠总闸为主体，单一物理空间内完成走到总闸、转阀门、水流停止。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "evidence": "各组均使用【画面风格】承载真人实拍、电影质感、浅景深、高清细节、无字幕、无配乐和负向词；未再出现16:9、组时长或4K/1080p/720p等生产界面参数。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林跃、赵百川、赵大强、林建国、张桂兰和众村民在【主体】中均有位置或围观关系，所有开口人物可用。",
      "fix_instruction": "无"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林跃追问赃物、赵百川用剪断电线强撑、林跃反问“那人呢”并锁定李二狗，剧情因果与原剧本一致。",
      "fix_instruction": "无"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组只包含林跃逼近、鞋码问答、抓脚踝展示鞋底三个强节拍，13 秒内动作链清楚，没有过载。",
      "fix_instruction": "无"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组结尾林跃压住赵大强气势后，第6组转到林跃扶住父母、赵百川暗中递眼色，晒谷场人物状态连续。",
      "fix_instruction": "无"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第7组使用【场景】、【主体】、【运动】、【音频】、组尾衔接、【画面风格】结构；【画面风格】只保留视觉风格、无字幕、无配乐和负向词，没有16:9、12秒、4K等生产界面参数。",
      "fix_instruction": "无"
    }
  ],
  "issues": [],
  "warnings": []
}
