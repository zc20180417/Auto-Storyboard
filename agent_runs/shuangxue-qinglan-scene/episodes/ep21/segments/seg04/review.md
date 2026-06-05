{
  "pass": true,
  "summary": "seg04保留法警监督下拆旧门窗、旧落地窗拆下、周美娟尖叫和沈清合法重装反击，室内状态连续。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "action_atomicity",
      "evidence": "拆旧门窗、松开落地窗固定点、落地窗拆下、周美娟尖叫分为四段，单段只承载一个主动作或一段对白。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "沈清第一句约32字用6秒约5.3字/秒，第二句约23字用5秒约4.6字/秒，均在硬上限内。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "evidence": "第6组尾旧落地窗靠墙、窗洞灌风、沈清站在风口旁，第7组首逐项继承这些状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟现场对工人们喊话，砰声是旧落地窗拆下的环境声，没有误作人物对白。",
      "fix_instruction": "若不通过，应写清砰声来源或周美娟对白对象。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组围绕拆窗一条动作链推进，12秒承载施工、松动、拆下和尖叫反应，未把沈清长台词也塞入同组。",
      "fix_instruction": "若不通过，应把周美娟尖叫或拆窗动作另起短组。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第7组为周家客厅单一空间，组首写明旧落地窗靠墙、窗洞敞开、人物位置和朝向。",
      "fix_instruction": "若不通过，应删除跨院落信息或补具体室内位置。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "旧落地窗从墙面原位到被拆下扶到墙边，再到第7组首靠墙，状态变化有可见过渡。",
      "fix_instruction": "若不通过，应补充旧落地窗拆下后放置位置。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "沈清站在风中和两句反击台词均按原文保留，未新增体罚、驱赶或其他改变剧情的动作。",
      "fix_instruction": "若不通过，应恢复原台词并删除新增强动作。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定旧落地窗、周美娟、沈清、工人们、纸箱和法警，共4条，均为本组具体风险。",
      "fix_instruction": "若不通过，应用本组人物和道具替换泛泛风险词。"
    }
  ],
  "issues": [],
  "warnings": []
}
