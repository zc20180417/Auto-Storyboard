{
  "pass": true,
  "summary": "已对照第7集7-1脚本、横屏生成规则和3D CG视觉规则复审，6组保留门口请柬压力、赵天宇带伤挑衅、长刀拦路、玄铁卡压场跪拜、请入包厢和茶盏发狠，未发现阻断交付问题。",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
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
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "prop_continuity": "checked",
    "physical_continuity": "checked",
    "visual_peak": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中沐清寒没有请柬、陆渊说直接进去、豪华马车停在身旁均保留；台词按原句写入第1组1-2和1-3。"
    },
    {
      "group": "第4组",
      "type": "special_effects",
      "evidence": "玄铁卡首次改变局势时，第4组4-1写暗金纹路沿金龙图腾微亮，4-3写烛火轻颤和衣袖被无形气压掀动，特效绑定玄铁卡和跪拜压场。"
    },
    {
      "group": "第5组",
      "type": "horizontal_composition",
      "evidence": "第5组明确中央低位是管事，左侧高位是陆渊与沐清寒，右侧是赵天宇，守卫长刀低垂退成边缘，横屏阵营关系清楚。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "第6组承接第5组赵天宇手中茶盏，6-1写捏碎茶盏和玻璃渣刺破手心，组尾保留碎茶盏、玻璃渣和掌心出血状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵天宇两句嘲讽均写明对沐清寒和陆渊说，沐清寒冷回应也写明对赵天宇说，没有无对象对白。",
      "fix_instruction": "若不通过，应补充每句现场对白的说话对象，并区分画外音与现场开口。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "第3组用低角度推近承接赵天宇命令，贴地推进跟随守卫抽刀落位，再以稳定中景承载守卫威胁台词，动静分配可生成。",
      "fix_instruction": "若不通过，应增加明确路径或落点的运镜，同时保留稳定中景承载台词。"
    },
    {
      "group": "第4组",
      "type": "asset_scope",
      "result": "pass",
      "evidence": "第4组人物5项、场景1项、关键道具3项，合计9项；玄铁卡、金龙图腾和守卫长刀均为剧情关键资产，没有把铜灯等普通环境细节列入资产。",
      "fix_instruction": "若不通过，应删除普通环境细节资产或拆组，不能删掉玄铁卡、守卫长刀等关键剧情资产。"
    },
    {
      "group": "第6组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "茶盏碎裂由赵天宇手部持有和用力捏碎触发，玻璃渣刺破手心并在组尾持续，物理来源和状态延续清楚。",
      "fix_instruction": "若不通过，应补足道具受力来源、碎片落点和伤口持续状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
