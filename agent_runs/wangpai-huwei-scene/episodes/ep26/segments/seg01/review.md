{
  "pass": true,
  "summary": "seg01 分镜覆盖会议室善后、旧案纪念墙、集团门口关系落点与羁押室彩蛋，未发现阻断交付的硬问题。",
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
      "evidence": "法务台词明确由免提电话传出，许知夏闭口听着，电话VO没有被写成会议室人物现场开口。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "许知夏台词约25字安排在2.5-7.5秒5秒内，约5字/秒；顾北辰OS约27字安排在9.5-15秒5.5秒内，约4.9字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "evidence": "片尾彩蛋单独放在昏暗羁押室8秒短组，没有与集团门口同组跨空间；组首列明秦越、审讯椅和铁栏阴影。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "董事甲认错、许知夏“先审人，再审利”和起身到窗前均保留原剧本顺序和关系。",
      "fix_instruction": "若不通过，应恢复董事甲认错和许知夏重立项目底线的台词顺序。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "白花由顾北辰放到纪念碑前并被旧军靴压住，组尾继续保留白花和旧军靴位置。",
      "fix_instruction": "若不通过，应补写白花放下和旧军靴压住花束的可见动作。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS写明嘴唇闭合、心声响起；许知夏现场对白明确对顾北辰说。",
      "fix_instruction": "若不通过，应把OS改为闭口心声或补清现场对白对象。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒内只承载许知夏走近、完整提出安全顾问和并肩关系、顾北辰反应三段，低密度但由关键关系转折支撑。",
      "fix_instruction": "若不通过，应拆出顾北辰下车动作到下一组，保留本组为 offer 和反应。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾顾北辰坐在驾驶位且手离开方向盘，第7组首继承该状态，再写推门下车，状态没有跳变。",
      "fix_instruction": "若不通过，应在第6组尾或第7组首补齐车门关闭和顾北辰仍在驾驶位。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定顾北辰、许知夏、黑色商务车和玻璃幕墙，均为本组具体连续性风险。",
      "fix_instruction": "若不通过，应删除泛泛禁止项并替换为本组人物、道具或场景锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
