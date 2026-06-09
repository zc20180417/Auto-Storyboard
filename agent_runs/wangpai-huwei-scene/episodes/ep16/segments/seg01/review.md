{
  "pass": true,
  "summary": "seg01 已完成冷库调查、A17空柜、雨夜闪回、秦越设局、坐标发现和断电收尾，审核未发现 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组", "第13组"],
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
      "group": "第4组",
      "type": "space_locking",
      "evidence": "该组场景字段明确写为“回忆闪回：雨夜仓库外”，许振南和戴帽口罩的人只在闪回空间内出现，未被写成冷库现实空间。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "许知夏对秦越的质问约20字用0-5秒，约4.0字/秒；秦越威胁约25字用8-12秒，约6.25字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "evidence": "秦越先从冷库内退到门外侧再落锁，第9组尾部明确秦越在门外，第10组组首继承为秦越位于玻璃窗外侧。"
    },
    {
      "group": "第11组",
      "type": "prop_continuity",
      "evidence": "A17空盒底部的N38°坐标从特写暴露，到许知夏喊出旧仓储转运站，再到第12组手机拍下坐标，关键道具状态连续。"
    },
    {
      "group": "第13组",
      "type": "audio_mouth_sync",
      "evidence": "秦越台词写为冷库门外传来的声音，画面内许知夏和顾北辰只看向门口方向，没有替秦越做口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏OS写明嘴唇闭合不做口型，声音内容忠于“爸，如果你真留下第二支录音笔...”",
      "fix_instruction": "若不通过，应把OS改为内心声音并写明闭口，不能写成现场对白。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "A17为空、只剩三年前封条、许知夏“被拿走了”和顾北辰“三年前就动过”均保留，未新增录音笔出现。",
      "fix_instruction": "若不通过，应恢复空柜、封条日期和顾北辰判断。"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越从货架后走出，手下分散，周振邦押着双手反绑的赵明海随后出现，所有后续说话或行动人物都有入场来源。",
      "fix_instruction": "若不通过，应在人物说话前补入货架后走出或被押入的动作。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "秦越对顾北辰、赵明海对许知夏、周振邦对赵明海的对白对象均明确，没有假对象。",
      "fix_instruction": "若不通过，应逐句补清真实对话对象。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "周振邦在门内拍玻璃，秦越在门外隔玻璃回应，之后顾北辰让许知夏找应急阀，门内外位置没有跳变。",
      "fix_instruction": "若不通过，应修正秦越门外、周振邦门内和顾北辰在A17附近的位置。"
    },
    {
      "group": "第11组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "摸索墙面、看见刻痕、OS识别坐标、向顾北辰喊出旧仓储转运站分成四段，14秒内承载清楚。",
      "fix_instruction": "若不通过，应拆分摸索、发现和喊话，不能把坐标发现压进单个短镜。"
    },
    {
      "group": "第12组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "秦越下令、顾北辰挡开手下、拳击一人、肘击另一人与许知夏拍照按阶段拆开，保护站位明确挡在许知夏和A17前方。",
      "fix_instruction": "若不通过，应拆开打斗动作并补足顾北辰挡在许知夏前方的站位。"
    },
    {
      "group": "第12组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定许知夏、顾北辰、秦越手下、手机和坐标刻痕，均是本组具体生成风险。",
      "fix_instruction": "若不通过，应删除无锚点泛泛词，改为本组人物和道具错误。"
    },
    {
      "group": "第13组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "断电黑暗收尾没有模型说明词、模板编号、参考图或工程占位符，保持自然分镜正文。",
      "fix_instruction": "若不通过，应删除所有模型说明和工程词。"
    }
  ],
  "issues": [],
  "warnings": []
}
