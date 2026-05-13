{
  "pass": true,
  "summary": "已对照26-1原剧本、竖屏生成规则和当前分镜逐组审核，动作、台词、空间锁定和时长均可交付。",
  "checked_groups": [
    "第1组",
    "第2组"
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
      "evidence": "原剧本金董台词“给我教训他！”、保镖拔甩棍、陆凡低扫踢翻保镖甲和保镖甲“哎哟！”均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组6-9秒承载金董“你别过来！我是龙少的代表！”，有效约12字/3秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首复述办公室、陆凡、保镖甲、其余保镖和金董位置，承接第1组尾部倒地和迟疑状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内只包含金董下令、保镖逼近、陆凡低扫和保镖甲倒地四个清晰节拍，没有把三秒解决战斗硬塞进同组。",
      "fix_instruction": "如不通过，应拆出低扫或压缩保镖逼近动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部保镖甲倒地，第2组组首保镖甲仍在陆凡脚边，甩棍夺取动作有可见来源。",
      "fix_instruction": "如不通过，应补充甩棍从保镖甲手中到陆凡手中的过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "金董的现场对白均写明对陆凡喊道，没有把恐惧台词写成旁白或假对象。",
      "fix_instruction": "如不通过，应把对白改为明确的A对B说话格式。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、参考图、模板编号或自动分镜等污染词。",
      "fix_instruction": "如不通过，应删除工程说明并改写成自然画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
