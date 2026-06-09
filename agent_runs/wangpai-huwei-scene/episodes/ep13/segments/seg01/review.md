{
  "pass": true,
  "summary": "已对照第13集原剧本、竖屏生成规则和当前分镜逐组审核，关键台词、动作、空间连续性、倒计时手机和安全通道卡门均保留，无阻断交付硬问题。",
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
      "evidence": "周振邦命令台词约19个有效汉字安排在2-6秒的4秒内，字秒比约4.8，符合吼叫对白承载；同组其余时间为保安逼近和顾北辰应战姿态。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰在门后只以门后声音出现，分镜明确许知夏嘴唇闭合并侧身让开，随后顾北辰开门入场再可见行动。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "许知夏关于硬盘的判断、向秦越追问、秦越威胁以及顾北辰提到三年前清场害死项目队的台词均按原剧本顺序保留。"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "顾北辰击中一人、横扫一人、翻过档案柜、拉许知夏退入门口拆成4个连续时间段，非主动作人物只承担抢纸和追击反应。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏VO通过顾北辰耳机传来，顾北辰在听VO时嘴唇闭合，顾北辰自己的现场台词另写为对耳机说。",
      "fix_instruction": "若后续修改，应继续区分耳机VO和顾北辰现场开口，不要把许知夏VO写成顾北辰口型。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定地下档案库、安全通道门、许知夏、秦越和手下位置，秦越手下堵路动作发生在后续时间段内。",
      "fix_instruction": "若调整，应保持组首为静态结果，不要写手下正在走来或许知夏正在后退。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组组尾顾北辰挡在许知夏身前、手机和档案仍在许知夏手中，第7组组首继承相同站位并继续倒计时。",
      "fix_instruction": "若重排组别，应在相邻组尾和组首同步保留手机倒计时、顾北辰保护站位和安全通道门状态。"
    },
    {
      "group": "第9组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "档案文件从许知夏左手被扬起，形成散落纸页；第10组组首承接为许知夏左手已空、纸页位于地面和半空。",
      "fix_instruction": "若修改动作，应保留文件扬起到散落纸页的可见过渡。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组是动作脱身高密度组，但每个时间段只安排一个主动作链，14秒覆盖两次击倒、翻柜、拉人入门，未同时压入长对白。",
      "fix_instruction": "若新增台词或更多手下动作，应拆为两组，不要塞回本组。"
    },
    {
      "group": "第11组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定旧桌子、安全通道门、秦越手下、许知夏手机和顾北辰位置，数量4条，没有使用模板占位或泛泛词。",
      "fix_instruction": "若改视频禁止项，应继续使用本组人物、道具或场景名作为锚点。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图、自动分镜或工程占位符，组标题和时间段均为自然分镜格式。",
      "fix_instruction": "若追加内容，不要加入模型说明词或模板来源说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
