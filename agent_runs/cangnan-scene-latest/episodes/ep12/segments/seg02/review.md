{
  "pass": true,
  "summary": "seg02已完成真实审核，厂门封控、资金被转走和明日竞标承诺均忠于原剧本。",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "防暴车冲入、林夏询问伤势、陆凡说明赵大江从后门跑了，顺序与原剧本一致。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "evidence": "林夏命令对象为警员，江若晴和陆凡互相对话，未出现对空气或道具说话。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "林夏问句分配5秒，陆凡答句分配5秒，均低于6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定厂门、陆凡、江若晴和防暴车来向，林夏在镜头内入场后再说话。",
      "fix_instruction": "如不通过，应补充林夏从车旁上前后再开口。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内承载封锁命令、资金消息和陆凡判断三个短节拍，没有硬塞长动作。",
      "fix_instruction": "如不通过，应拆出资金消息或压缩警员动作。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾资金压力延续到第6组首封控现场，人物仍在厂门外同一空间。",
      "fix_instruction": "如不通过，应在第6组首复述陆凡、江若晴、林夏站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
