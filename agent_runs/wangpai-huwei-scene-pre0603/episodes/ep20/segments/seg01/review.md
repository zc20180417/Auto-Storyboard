{
  "pass": true,
  "summary": "第20集已完成真实审核，安全屋录音器交付、许氏会议室逼宫、投影证据、赵明海出庭、冷库证词和秦越短信均符合竖屏 scene 分镜合同，未发现阻断交付的 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组"],
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
      "evidence": "保留顾北辰调出许氏会议名单、周氏代表和秦越旁听席位，以及顾北辰“你一露面，就是靶子”和许知夏“那我更要露面”的原台词。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS被处理为心声，分镜明确顾北辰嘴唇闭合不做口型，只看着投影屏里的剪辑视频，没有让他现场开口。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "赵明海供词约35字分配6秒，约5.8字/秒，属于颤声供述的可接受速度，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第10组",
      "type": "prop_continuity",
      "evidence": "微型录音器从第2组交到许知夏掌心，第7组藏在掌心，第10组由许知夏按下播放，归属和使用路径连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾会议名单亮着，许知夏整理袖口；第2组组首承接为电脑仍停在会议名单页面，顾北辰手中持有微型录音器并交给许知夏。",
      "fix_instruction": "若不通过，应补足微型录音器从顾北辰到许知夏掌心的可见交接。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "许知夏落座、反问周振邦、周振邦问证据、助理打开投影被拆成四个时间段，没有把落座、长台词和投影操作压进同一镜。",
      "fix_instruction": "若不通过，应拆分许知夏反问和助理打开投影的动作。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "周振邦起身、怒斥、手机播放、剪辑视频呈现分阶段完成，14秒内承载一个反击链，未同时塞入赵明海入场或录音笔证词。",
      "fix_instruction": "若不通过，应把剪辑视频呈现或身份质问拆到下一组。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS明确为心声，画面写明嘴唇闭合；许知夏对门外赵明海现场开口，声音类型边界清楚。",
      "fix_instruction": "若不通过，应将顾北辰OS改为闭口心声，或删除现场开口口型。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵明海在组首位于门外走廊阴影处，随后由法务带进会议室后才说供词，人物入场和发言顺序清楚。",
      "fix_instruction": "若不通过，应先写赵明海被法务带进门，再让他开口供述。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定微型录音器、赵明海、许知夏、周振邦四类本组关键风险，共4项，没有泛泛词或与剧情矛盾的限制。",
      "fix_instruction": "若不通过，应删除泛泛项并补入本组具体人物、道具或动作风险。"
    },
    {
      "group": "第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "整集 final.txt 未出现模型说明词、模板编号、参考图、官方占位符、广告语或模板化批量描述，短信内容作为剧情道具文字呈现。",
      "fix_instruction": "若不通过，应删除工程词和模板污染，保留自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
