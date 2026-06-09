{
  "pass": true,
  "summary": "seg01 分镜覆盖楼梯间撤离、回忆克制、天台证据公开和秦越被封锁，未发现阻断交付的硬问题。",
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
      "evidence": "许知夏台词约22字安排在3-7秒4秒内，约5.5字/秒；顾北辰6字安排在7-9秒2秒内，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "搭档台词明确为回忆闪回中的画外音，顾北辰OS写明嘴唇闭合、心声响起，没有让现场人物错误开口。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "秦越冲向许知夏、顾北辰横跨阻挡并撞上护栏、秦越嘶吼、许知夏回应分别拆成四个时间段，保护站位写明挡在许知夏前方。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留三年前雨夜火场、搭档VO、顾北辰收住致命一击和OS的因果，没有把顾北辰写成杀死手下。",
      "fix_instruction": "若不通过，应恢复闪回、搭档VO和顾北辰收手的连续因果。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确天台出口、秦越、顾北辰、许知夏、沈曼和直升机位置，单一物理空间清楚。",
      "fix_instruction": "若不通过，应补齐各人物画面位置和身体朝向。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "许知夏手机从合并完成到外放录音持续在她手中，沈曼另一部手机同步开启直播，两个道具归属没有跳变。",
      "fix_instruction": "若不通过，应补写手机归属和直播开启的可见过渡。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒内承载冲刺、阻挡撞栏、秦越短句和许知夏回应四个清楚节拍，动作与台词没有压在同一时间段内。",
      "fix_instruction": "若不通过，应把冲撞和台词继续拆分或缩短非关键反应。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部顾北辰和秦越贴在护栏前，第6组组首继承两人在护栏前并补入林元在后方阴影处，状态连续。",
      "fix_instruction": "若不通过，应在第5组尾或第6组首补齐护栏位置和林元可用位置。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定秦越、民警、原始交接记录和顾北辰，数量4个且均为本组具体剧情风险。",
      "fix_instruction": "若不通过，应删除泛泛词并替换为本组人物或道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
