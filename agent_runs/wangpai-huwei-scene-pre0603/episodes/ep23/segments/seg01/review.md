{
  "pass": true,
  "summary": "ep23 seg01 保留顾北辰顶层入侵、秦越设陷、沈曼声纹反制和暗格弹开的关键剧情，格式与竖屏 scene 规则通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "许知夏的长句作为耳机声音出现，顾北辰画面中嘴唇闭合不做口型；顾北辰现场只低声回应“收到”。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "秦越拍手现身、说“顾北辰，技术不错。”，顾北辰回应“多谢夸奖。”，秦越亮出录音笔并说“想要？来拿。”均按原剧本顺序保留。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "沈曼楼下接通声纹和顶层暗格弹开被明确标注为蒙太奇转场，未伪装成同一现实空间连续移动。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "许知夏约34字耳机声分配5.5秒，约6.2字/秒，处于可接受的急促任务信息范围；顾北辰“收到”2字分配2秒含抬眼反应，未拖慢主对白。",
      "fix_instruction": "若仍认为耳机信息偏快，可压缩前后动作并继续给许知夏VO增加0.5秒。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组只承载顾北辰半步试探、保险室门开启、红外线显露、许知夏耳机警告和秦越短句收束，四个时间段清楚分开。",
      "fix_instruction": "若不通过，应拆出保险室门开启和红外线显露为独立短组。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "折叠反光镜明确从工具车底层抽出，袖口按钮由顾北辰按下；秦越手里的录音笔在组首和组尾均保持。",
      "fix_instruction": "若不通过，应补充折叠反光镜取出前的位置或录音笔仍在秦越手中的状态。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部袖口信号已触发，第5组开头沈曼在会客室按下声纹设备，因果连续；顶层暗格弹开后秦越惊惶，承接前一组秦越仍握录音笔的状态。",
      "fix_instruction": "若不通过，应在第4组尾部或第5组组首补充信号触发与声纹设备的可见联系。"
    },
    {
      "group": "第5组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项限定沈曼错位、暗格未弹开、秦越表情错误和录音笔消失，均为本组特有风险且数量为4项。",
      "fix_instruction": "若不通过，应删除泛化禁止词并只保留沈曼、暗格、秦越、录音笔相关风险。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、官方模板编号、参考图占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除任何工程说明或模板字样。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "timing_math",
      "problem": "第5组为9秒短组。",
      "evidence": "该组用于蒙太奇承接沈曼按键、暗格弹开和秦越惊惶反应，属于短承接和反转余波。",
      "fix": "交付时可保留；若需统一10秒以上，可只将秦越反应延至4秒，但不建议硬凑。"
    }
  ]
}
