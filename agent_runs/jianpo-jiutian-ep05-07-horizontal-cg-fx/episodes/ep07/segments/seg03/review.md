{
  "pass": true,
  "summary": "已对照第7集7-3脚本、横屏生成规则和3D CG视觉规则复审，2组保留敌国使臣阻止沐家、赵天宇两百万两、沐清寒两百五十万两和五百万两逼局，未发现阻断交付问题。",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组"],
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留敌国使臣对赵天宇说不能让沐家拿到解药、赵天宇喊两百万两、沐清寒咬牙喊两百五十万两和现银压力。"
    },
    {
      "group": "第2组",
      "type": "special_effects",
      "evidence": "第2组用拍卖槌震动杯盏、盒缝青金灵光一闪、烛火轻颤和前景衣袖被无形气压掀动表现五百万两压场，特效绑定竞价逼局。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "赵天宇五百万两台词写明对上方包厢沐清寒方向喊，敌国使臣在后方阴影里不出声，声音来源清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "第1组保持下方右侧赵天宇与敌国使臣、上方包厢沐清寒、中央展台锦盒的斜向对峙关系，没有无过渡换边。",
      "fix_instruction": "若不通过，应补充上下左右方位或中性镜头，避免大厅与包厢轴线混乱。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "敌国使臣台词4秒、赵天宇两百万两4秒、沐清寒两百五十万两5秒，均可承载口型和反应。",
      "fix_instruction": "若不通过，应拆分竞价台词或延长镜头，不能删价格信息。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组8秒只承载拍卖槌确认节拍和赵天宇五百万两压价两个强节点，未把敌国使臣、沐清寒反击或新动作硬塞进同一组。",
      "fix_instruction": "若不通过，应拆分拍卖槌、报价和反应，不要在短组内追加新剧情动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
