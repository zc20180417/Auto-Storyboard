{
  "pass": true,
  "summary": "seg01 已按原剧本完成会议室审计落地、纪念墙释怀、集团门口并肩和羁押室彩蛋九组竖屏分镜，未发现阻断交付的 hard issue。",
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
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "法务VO通过会议桌中央免提电话传出，许知夏嘴唇闭合看投影屏，声音来源和口型分离清楚。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "许知夏安全顾问与并肩长句约35字分配7秒，约5字/秒，顾北辰短句2秒完成，未超过6.5字/秒。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "evidence": "片尾彩蛋单独放在昏暗羁押室，未与第8组许氏集团门口广场混入同一现实空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "董事甲道歉、许知夏关于底线与审人的原台词、众董事沉默点头和许知夏走到窗前均保留。",
      "fix_instruction": "若不通过，应恢复会议室关键台词和起身走到窗前动作。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "白花由顾北辰放到碑前并被旧军靴压住，组尾仍在碑前，未转移或消失。",
      "fix_instruction": "若不通过，应补足白花、旧军靴和碑面名字的位置关系。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS写明嘴唇闭合不做口型，许知夏现场对白对象为顾北辰，林元退后动作可见。",
      "fix_instruction": "若不通过，应改正OS口型并明确现场对白对象。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾顾北辰仍在驾驶位、许知夏仍在车外；第6组首承接同一车旁状态并由许知夏走近。",
      "fix_instruction": "若不通过，应在组尾或组首补充车内外位置和车门状态。"
    },
    {
      "group": "第7组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "许知夏伸手、顾北辰握手后松开、许知夏转身回答、顾北辰跟上分段清楚，没有把握手和并肩离开压成一个动作。",
      "fix_instruction": "若不通过，应拆分握手、松手、转身和跟上动作。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "广场收尾和顾北辰OS均为自然分镜描述，未出现模型说明词、模板编号、参考图或视频延长等工程词。",
      "fix_instruction": "若不通过，应删除工程词并改成可见画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
