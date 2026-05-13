{
  "pass": true,
  "summary": "seg02 共3组，完成回到裂缝、滴水唤醒、黑水灼尾和水壶切换为安全入口；水壶阶段和黑水承接来源清楚。",
  "source_status": "script_provided",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "physical_continuity",
      "evidence": "第5组滴水阶段写明壶嘴略低于壶内水线、只滴几滴、随后控制住壶身，没有出现口沿高于水面但水流出的矛盾。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第5组组尾先建立裂缝右侧油亮黑水暗痕，为第6组承接黑水危险提供来源。"
    },
    {
      "group": "第6组",
      "type": "physical_continuity",
      "evidence": "第6组把水壶从滴水阶段切换到斜立防漏入口阶段，壶底抵土坎、双手托住、口沿高于水面且不漏水。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第4组明确壶盖从水壶上拧下并放到左膝旁，后续组可承接壶盖来源。",
      "fix_instruction": "若不通过，应补充开盖动作和壶盖落点，避免后续封盖无来源。"
    },
    {
      "group": "第5组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "滴水时壶嘴低于水线，防漏状态尚未提前套用，水流路径从壶嘴到裂缝清楚。",
      "fix_instruction": "若不通过，应把滴水阶段改成壶嘴略低于水线，并删除口沿高于水面的出水描述。"
    },
    {
      "group": "第6组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "黑水只表现油亮暗痕、极淡白雾和尾尖灰白，没有怪物化、爆炸毒液或恐怖血腥。",
      "fix_instruction": "若不通过，应删掉夸张腐蚀、爆炸和怪物化描述，改回真实克制的接触痕迹。"
    }
  ],
  "issues": [],
  "warnings": []
}
