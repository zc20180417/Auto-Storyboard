{
  "pass": true,
  "summary": "已对照第10集原剧本、竖屏生成规则和当前seg01分镜逐组审核，8组均保留关键台词、动作、空间与声音来源，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
      "evidence": "原剧本肉市开场中老周询问许安、许安要新鲜货、老周说明有人放话、许安现金拿货、马会替许安说话的台词顺序均在2-13秒内保留，人物关系没有改变。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "10-15秒承载许安、林小满、许安三句短对白，约14个有效字分配5秒，并包含许安拦住林小满和拉近肉筐的动作，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "医生两句催费都写为手机听筒传出的电话音，画面中许安只对手机低声回应，林小满只做听见后的可见反应，没有让医生电话音落到画面人物口型上。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "evidence": "第7组组尾为许安放下手机、林小满抱账本看向他；第8组组首复述许安手中持有刚放下的手机、林小满抱账本面对许安，手机和账本状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组-第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "肉市三组均固定在凌晨肉市摊口，组首逐组列出许安、老周、马会的位置、身体朝向、肉案和保鲜布状态，后续动作从这些状态自然发生。",
      "fix_instruction": "无需修复；若后续改稿，应继续避免在组首写走来、进入、掀开等过程动作。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "肉块从第2组被老周推到肉案前侧，第3组组首复述肉块在肉案前侧；现金由许安掏出并放入老周掌心，肉块与现金归属变化都有可见过渡。",
      "fix_instruction": "无需修复；若调整成交段，应保留肉块前移和现金交付两个可见动作。"
    },
    {
      "group": "第4组-第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "街口空地戏拆为帮工被抢、许安独自忙摊、韩彪放狠话三组；每组仅承载2到3个强节拍，没有把抢人、开工、整夜忙碌和三天后威胁硬塞进同一15秒片段。",
      "fix_instruction": "无需修复；若压缩组数会造成动作和对白过载，应保持当前拆分。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "客人甲对许安催单、许安对客人甲回应、林小满对许安提醒、许安对林小满低声回应均写清说话对象，没有假对象或无对象台词。",
      "fix_instruction": "无需修复；新增对白时仍需写明A对B说道。"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本这一晚硬扛全场被转译为许安送盘、翻火、收钱找零和客人散去的可见时间压缩蒙太奇，韩彪隔街盯视与放狠话可直接生成。",
      "fix_instruction": "无需修复；若加强整夜辛苦，应继续用可见动作而不是抽象评价。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "医生催费明确来自手机听筒，手机亮屏和许安贴近耳边提供声音载体，林小满听见后只看向许安侧脸。",
      "fix_instruction": "无需修复；不得把医生电话音改成现场人物开口。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "医院催费后的关心段完整保留林小满、许安关于治疗费用和共同承担的台词顺序，没有增加新的承诺、借钱动作或改变人物关系。",
      "fix_instruction": "无需修复；如需局部调整，只能调整承载镜头，不能改写台词含义。"
    },
    {
      "group": "第1组-第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文未出现模型说明词、模板编号、参考图占位、官方模板语气或批量化空泛描述；每组均保持自然分镜正文和稳定cut_id。",
      "fix_instruction": "无需修复；后续不要加入工程说明、模板编号或自动分镜字样。"
    }
  ],
  "issues": [],
  "warnings": []
}
