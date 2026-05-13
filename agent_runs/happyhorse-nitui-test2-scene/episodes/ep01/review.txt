{
  "pass": true,
  "summary": "已对照原剧本、分镜生成规则和HappyHorse边界审查ep01全片，7个分镜组保留原台词、关键动作、空间拆分和音画关系，无需硬修。",
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
      "evidence": "原剧本开场的林跃被绑木桩、赵百川怒斥偷割集体电线、赵大强嚣张补刀、林建国嘶吼和张桂兰哭求均按顺序保留；断电线被固定为赵百川脚边竹筐里的关键道具，没有新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "林跃内心旁白“我重生了？回到了被陷害的这一天！”放在0-3秒，画面明确写林跃嘴唇闭合、不做口型；随后3-7.5秒承载挣断麻绳和站起的复合动作，10-14秒再现场开口质问赵百川。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "0-2.5秒承载赵百川“剪断的电线就是赃物！”与林跃“那人呢？”的短句交锋，约13个有效字配2.5秒，节奏可表演；9-14秒承载林跃问鞋码和李二狗心虚回答，约22个有效字配5秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "本组只承载抓脚踝展示红泥鞋底、林跃质问、李二狗发抖、村民怀疑四个连续节拍，均发生在晒谷场同一冲突中，14秒内没有叠加新空间或额外道具。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "水渠总闸被关单独拆成村头水渠边一组，组首只放王四和水渠总闸，未把晒谷场人物硬塞进同一现实空间；赵百川只以内心旁白作为画外音出现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林跃的重生认知是OS，分镜写为内心旁白并明确嘴唇闭合；现场对白“赵村长，你说人赃俱获，赃物在哪？”另在10-14秒由林跃对赵百川开口承载。",
      "fix_instruction": "无需修复；若后续改动，应继续把OS和现场开口对白分离。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部林跃仍站在李二狗面前，第5组首复述林跃在李二狗面前、李二狗红泥鞋落回地面、赵大强在右后方；第5组尾部林跃扶母，第6组首以林跃扶着张桂兰开场，人物位置连续。",
      "fix_instruction": "无需修复；同场景后续组继续复述上一组尾部的人物和道具状态即可。"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王四在第6组组首被写入背景人群靠右的位置，身体朝向和脸朝方向明确，随后先接住赵百川眼色再离场，满足行动前可用性。",
      "fix_instruction": "无需修复；不可把王四写成未在组首或未入场就直接去水渠操作。"
    },
    {
      "group": "第7组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“果园变荒地”的抽象威胁没有直接画成结论，而是通过支渠断流、湿泥露出、水草贴泥和王四确认阀门的可见细节承载。",
      "fix_instruction": "无需修复；若强化威胁，应继续用水渠断流和人物反应表现，不加字幕或解释卡。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全片未出现@图、Image、参考图、首帧、尾帧、独立音频时间轴、方括号声学控制或HappyHorse/Seedance模型说明词；声音都写入每个时间段的音频设计。",
      "fix_instruction": "无需修复；不得把生产侧参考图槽位写入final.txt。"
    }
  ],
  "issues": [],
  "warnings": []
}
