{
  "pass": true,
  "summary": "第19集分镜保留仓储站逃离、许父音频、证据链和赵明海语音推进，时间轴、对白指向、音频闭口和道具连续性均可交付。",
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
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "顾北辰证据链台词约49字用8秒，约6.1字/秒；林元原始声纹台词约30字用5秒，约6字/秒；许知夏护身符判断已移到第6组用4秒承载，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "许父以电脑扬声器音频出现，镜头明确写许知夏嘴唇闭合不做口型，许父未被画面人物现场开口替代。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部暗门已打开且三人在门内侧，第2组组首从暗门外巷道入口开始，随后写钻出、反手锁门、上车，暗门状态和人物位置有可见过渡。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "赵明海语音完整保留周振邦甩锅、明天董事会、逼许知夏退出盛远项目、愿作证并求救四个信息点，顾北辰在第7组随后保留“不可信”的判断。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "林元指出暗门、顾北辰拉许知夏移动、三人到门前、林元踹门分成四段，未把指路、奔跑和踹门压进同一时间段。",
      "fix_instruction": "若后续修订压缩动作，应保持指路、移动、踹门至少分段。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "钻出暗门、反锁、秦越门内喊追、上旧车四个阶段在14秒内顺序展开，秦越和手下没有提前越过暗门。",
      "fix_instruction": "若增加追打动作，应拆出新组，避免巷道上车段过载。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定旧车、三人在车内、秦越在背景暗门口，后续旧车驶离和秦越拨电话均在仓储站外巷口同一空间内完成。",
      "fix_instruction": "若改成车内逃亡与仓储站门口交叉剪辑，应明确蒙太奇或拆组。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "存储卡插在读卡器、录音笔在电脑旁，播放音频和音频中断后组尾继续保留这些证物位置。",
      "fix_instruction": "若让许知夏拿起录音笔，应补充拿起和放回的可见动作。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵明海只以手机扬声器语音出现，第6组5.5-15秒明确许知夏、顾北辰和林元闭口听着，没有让安全屋人物替赵明海开口。",
      "fix_instruction": "若改成电话画面，应写清手机屏幕或电话声音来源。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许知夏关于不可信突破口、林元追问互咬、许知夏“把灯打开”的台词顺序和关系判断均保留。",
      "fix_instruction": "若缩短结尾，不要删除林元追问或许知夏最后一句。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第4组禁止项锚定存储卡、录音笔、许知夏和林元伤口，均对应本组音频和证物连续风险，没有使用泛泛词。",
      "fix_instruction": "若删除证物相关镜头，可同步删除对应禁止项。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文没有模型说明词、模板编号、参考图占位或批量模板化描述，所有组均为自然分镜正文。",
      "fix_instruction": "若加入风格尾巴，须交由收集阶段处理，不写入 final。"
    }
  ],
  "issues": [],
  "warnings": []
}
