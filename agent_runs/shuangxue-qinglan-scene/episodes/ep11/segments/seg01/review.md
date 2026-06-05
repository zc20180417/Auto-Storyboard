{
  "pass": true,
  "summary": "seg01保留银行查证、空转账户、录像取证和沈清心声，格式、时间轴、对白指向与口型分离均通过。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "原剧本中沈清递身份证请求查询、柜员核对后说没有购买记录，分镜按同一顺序保留，未新增其他业务动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "周桂兰10字台词给2.5秒，柜员12字台词给2.5秒，沈清15字台词给5秒内含手机稳定动作，均未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "沈清OS明确写为心声，画面写明嘴唇闭合、不做口型；柜员现场复述有明确对象沈清。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定银行大厅业务窗口、三人位置和身份证/柜台电脑状态，第一时间段从该状态递证件开始。",
      "fix_instruction": "若不通过，应把组首改成静态站位和道具状态，动作放入0秒后的镜头。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "身份证从第1组尾到第2组首仍在柜员手边，手机从桌边被沈清拿起并对准柜台电脑。",
      "fix_instruction": "若不通过，应补充身份证和手机的可见归属。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "8秒短组只承载柜员复述、手机录制证据和沈清心声，属于道具插入与短动作余波，不硬凑10秒。",
      "fix_instruction": "若不通过，应保留短组或合并同空间轻节拍，不能增加无剧情停顿。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定沈清、手机录制界面和柜台电脑，数量为3条，没有模板占位。",
      "fix_instruction": "若不通过，应删除泛泛词并改成本组人物、手机或柜台电脑相关错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
