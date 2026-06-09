{
  "pass": true,
  "summary": "第16集已完成真实审核，冷库A17调查、三年前闪回、秦越设局、降温封锁、坐标发现、打斗保护和黑暗收尾均符合竖屏 scene 分镜合同，未发现阻断交付的 hard issue。",
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
      "type": "dialogue_pacing",
      "evidence": "顾北辰关于门锁的台词约16字分配3.5秒，约4.6字/秒；许知夏短问句约7字分配3.5秒；顾北辰回应约13字分配4秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组明确写出场景为盛远地下冷库和雨夜仓库外回忆闪回，闪回时间段只承载许振南交出银色封存盒和原台词，不让现实人物跨空间移动。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "evidence": "第6组组尾秦越仍在冷库内对峙，第7组组首锁定冷库门打开、秦越靠近门口，再写他退到门外玻璃后和冷库门落锁，完成可见过渡。"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "秦越下令、手下扑向A17、顾北辰横跨挡人、一拳击喉、回身肘击和许知夏拍坐标按阶段拆成4个时间段，没有把打斗和拍照压在同一动作里。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏寻找第二支录音笔的内容处理为心声，镜头写明她嘴唇闭合不做口型；现场对白只用于她之后对顾北辰说被拿走了。",
      "fix_instruction": "若不通过，应把OS改成闭口心声，不能让许知夏现场开口说给无人对象。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "泛黄封条、三年前被动过、雨夜仓库外交出银色封存盒和许父台词均与原剧本一致，没有提前揭示戴帽口罩人身份。",
      "fix_instruction": "若不通过，应恢复封条线索、闪回遮脸人物和许父原台词。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越、周振邦、赵明海和两名手下在组首均已位于货架阴影或背景位置，秦越现身、周振邦押赵明海和手下站位都有可用来源。",
      "fix_instruction": "若不通过，应在组首把秦越或手下放入可被揭示的位置，或在说话前补入场动作。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "冷库封锁被拆成秦越退到门外、门锁落下、温控屏下降、许知夏质问和秦越解释四段，未把落锁、降温、周振邦惊恐和顾北辰找阀全部塞进同组。",
      "fix_instruction": "若不通过，应继续拆分封锁和周振邦反应，不要压缩到一个15秒组。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "A17空盒在第2组打开后持续保留，第9组明确盒底坐标刻痕露出，许知夏用眼发现后喊给顾北辰，没有让坐标凭空转移到其他道具上。",
      "fix_instruction": "若不通过，应补充A17空盒位置、坐标刻痕可见状态和许知夏发现动作。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "打斗保护组的视频禁止项锚定许知夏、顾北辰、秦越手下、手机和坐标刻痕，共4项，且不禁止原剧本必须发生的拍照和打斗。",
      "fix_instruction": "若不通过，应替换与剧情冲突的禁止项，并保留手机拍下坐标和顾北辰挡人的关键约束。"
    },
    {
      "group": "第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "黑暗收尾只写备用电源切断、温控屏微光、两人握手和秦越声音，未出现模型说明词、模板编号、参考图或视频延长等工程词。",
      "fix_instruction": "若不通过，应删除工程说明，改成可见低光画面和可听声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
