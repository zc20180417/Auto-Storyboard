{
  "pass": true,
  "summary": "ep21 单段分镜保留会议室取证、赵明海爆料、周振邦供出保险室与走廊行动部署，未发现阻断交付的 hard issue。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "5-12秒承载周振邦辩解和许知夏短句反击，约40个有效字分配7秒，字秒比约5.7，低于6.5硬上限，且属于同一桌面对峙节拍。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "evidence": "周振邦冲向赵明海、保安拦住、赵明海喊出录音笔、全场静住被拆为0-3秒、3-5秒、5-11秒、11-13秒四段，外部动作和爆料台词没有塞入同一镜。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "周振邦OS在9-12秒明确写为心声，且标明嘴唇闭合不做口型，没有被误写成现场开口。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "周振邦供出的启元顶层保险室、录音笔明晚九点转入秦越私人柜、声纹、秘书沈曼均与原剧本一致，没有新增录音笔现身或改变密码信息。"
    },
    {
      "group": "第7组",
      "type": "prompt_pollution",
      "evidence": "最终正文未出现模型说明词、模板编号、参考图、自动分镜或固定尾部负面词；秦越电梯心声以自然画面和声音来源承载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "流水打印件由顾北辰手中推到会议桌中央，并在组尾停在周振邦和许知夏之间，后续第3至第5组持续锚定在会议桌中央。",
      "fix_instruction": "若不通过，应补充打印件从顾北辰手中到会议桌中央的可见过渡。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列明会议室内周振邦、赵明海、保安、许知夏、顾北辰与董事的位置，周振邦从座位边冲向赵明海与第一帧状态兼容。",
      "fix_instruction": "若不通过，应把周振邦或保安的入场和站位改成明确第一帧状态。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载许知夏追问、周振邦咬牙、顾北辰压低声威胁、周振邦心声动摇四个短节拍，没有额外动作或跨场景过载。",
      "fix_instruction": "若不通过，应拆出周振邦心声或缩短非关键反应。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组会议室信息结束后切到许氏集团走廊，属于新物理空间；第6组组首明确会议室门关闭、许知夏持手机、顾北辰从门附近走来，交代了会议结束后的空间状态。",
      "fix_instruction": "若不通过，应在组首补会议室门、手机和顾北辰位置。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越在第7组组首已位于远处电梯内背景阴影里，后续电梯门合上和心声均有可见载体，不是突然参与画面。",
      "fix_instruction": "若不通过，应在组首提前锁定秦越位于电梯内或改成纯画外信息。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定秦越、电梯、许知夏、顾北辰和心声口型，数量4个，均为本组具体剧情错误风险。",
      "fix_instruction": "若不通过，应删除泛泛词并改为本组人物、场景或道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
