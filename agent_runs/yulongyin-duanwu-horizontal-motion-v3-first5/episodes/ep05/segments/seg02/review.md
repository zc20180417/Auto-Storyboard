{
  "pass": true,
  "summary": "seg02 两组完成云宝提示、陶笛触发、水洼炸开、水弹击中包工头和逃离，奇幻来源路径结果清楚。",
  "checked_groups": [
    "第3组",
    "第4组"
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "水壶在天天左前景怀中，云宝在壶口内可见并指向中央水洼；天天随后拧开壶盖并掏出陶笛，道具转移发生在 5-7.5秒可见镜头中。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "evidence": "天天对怀中水壶里的云宝说“云宝，靠你了！”，云宝作为可见对话对象位于壶口内侧，没有虚构对空气说话。"
    },
    {
      "group": "第4组",
      "type": "camera_motion",
      "evidence": "水弹段从左前景陶笛固定承载，到中央水洼轻推触发，再横向跟拍水弹射向右侧包工头，最后跟拍包工头逃向洞口，运镜跟随来源、路径、结果。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保留尖锐笛声回荡、水洼猛地炸开、几十颗水弹射出、包工头惨叫“哎哟！什么东西打我的脸！”以及捂脸逃出岩洞。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天维持左前景，包工头和胡永贵维持右侧，水洼居中，连续承接前段左右压迫，没有无过渡换边。",
      "fix_instruction": "若站位跳变，应在镜头描述中补出可见走位或使用中性镜头重建轴线。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "奇幻链条完整：陶笛和水壶青蓝光触发中央水洼，水花炸成水弹，水弹沿中央到右侧路径击中包工头，组尾留下铁锤落地和包工头逃离结果。",
      "fix_instruction": "若链条缺失，应补足水弹来源、飞行路径或击中结果。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "包工头 7.5-10.5秒用 3 秒承载“哎哟！什么东西打我的脸！”，有效字数约 12，字秒比约 4.0，台词节奏可表演。",
      "fix_instruction": "若台词节奏超过硬上限，应延长受击反应段或拆分镜头。"
    }
  ],
  "issues": [],
  "warnings": []
}
