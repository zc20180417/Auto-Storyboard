{
  "pass": true,
  "summary": "seg04两组正确处理电话音、免提载体、宋子昂反应和摔杯动作，未发现硬问题。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "陈刚台词写为手机扬声器传出的电话音，陆凡嘴唇闭合不做口型，声音来源和可见载体明确。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "宋子昂质疑越区采购、陆凡说明市委顾书记特批、宋子昂砸碎红酒杯均按剧本顺序保留。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "手机从第7组桌面免提到第8组挂断扣回桌面，红酒杯在宋子昂手边并被抓起砸碎，道具过渡可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "陈刚电话音约17字用5秒，陆凡对陈刚约14字用4秒，均未超过6.5字/秒。",
      "fix_instruction": "若失败，应延长电话音或拆分到反应镜头。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾部手机在桌面免提，宋子昂僵硬盯手机；第8组首部手机仍在陆凡面前，宋子昂脸色铁青。",
      "fix_instruction": "若失败，应补手机位置和宋子昂状态。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "挂断电话、质问、特批回应、抓杯、摔杯五段动作和对白各有时间承载，15秒内可表演。",
      "fix_instruction": "若失败，应将砸杯单独成短组或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
