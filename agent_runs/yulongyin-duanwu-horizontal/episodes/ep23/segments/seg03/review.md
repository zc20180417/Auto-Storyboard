{
  "pass": true,
  "summary": "seg03完整保留石头救场、爸爸跃下、击倒打手丙和发现云宝濒危，横屏动作方向与父子视线衔接明确。",
  "checked_groups": ["第5组", "第6组"],
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "尖锐石头砸中打手丙手腕、打手丙惨叫、开山刀掉落、爸爸满身鲜血从坡顶跃下及暴喝台词均保留。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "evidence": "天天对爸爸说“爸爸……你流了好多血。”，爸爸对天天说“爸爸没事。快看看云宝怎么样了？”，对象明确。"
    },
    {
      "group": "第6组",
      "type": "horizontal_composition",
      "evidence": "爸爸由左中冲向中央打手丙，天天在右后方，云宝在右前景，击倒后视线从打手丙转向云宝，横向关系清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "开山刀从打手丙手中被石头击落，落到右下泥地，为第6组地面刀具状态提供连续性。",
      "fix_instruction": "若不通过，应补充刀从手中脱落到泥地的位置。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内依次承载重拳、打手昏倒、父子两句短对白、查看云宝，动作和对白分段清楚。",
      "fix_instruction": "若不通过，应将查看云宝拆到下一组。"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "云宝濒危被转译为泥水中身体几近透明、微光贴近水面的可见状态。",
      "fix_instruction": "若不通过，应用具体可见光色和身体状态替代抽象濒危。"
    }
  ],
  "issues": [],
  "warnings": []
}
