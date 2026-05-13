{
  "pass": true,
  "summary": "seg01逐组对照剧本、横屏生成规则和当前分镜完成审核：喂食、命名、水雾与心声均保留，命名前后称呼正确，格式和物理连续性可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
  ],
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
    "special_effects": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留天天反锁房门、拿出半个干硬白馒头、轻声问小龙饿不饿、掰碎馒头丢进竖立水壶、小龙吞下馒头渣等原剧本动作和台词。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组命名前称呼为小龙，命名台词“你从云里来，又是个宝贝，以后就叫你云宝吧”之后才写刚被命名的云宝在壶底打滚。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组将“凉凉的，就像真正的雨一样。如果是大暴雨就好了”写为内心旁白，并明确天天闭嘴不做口型。"
    },
    {
      "group": "第3组",
      "type": "physical_continuity",
      "evidence": "三组都保持透明水壶竖立或由天天扶稳，第3组水雾从壶口上方溢出后落到手背和脸颊，没有让装水容器平放或倒置。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "第1组写清左前方桌面和水壶、右后方房门与门闩，天天从右侧回到桌边，横屏左右关系明确。",
      "fix_instruction": "无需修复；如后续调整，应继续保留房门右后方和水壶左前方的空间关系。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第2组保留打嗝、水泡、天天承诺明天找吃的、正式命名云宝和云宝打滚，未提前污染命名后的称呼。",
      "fix_instruction": "无需修复；命名台词前仍必须使用小龙或壶中小龙。"
    },
    {
      "group": "第3组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "第3组水雾路径来自云宝张嘴，经壶口落到天天手背和脸颊，青蓝微光只在边缘轻微出现，没有科幻化或卡通化。",
      "fix_instruction": "无需修复；特殊元素继续保持真实克制。"
    },
    {
      "group": "第1组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第1组4个镜头时长为3+4+3+2=12秒，标题总时长12秒且镜头数一致。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
