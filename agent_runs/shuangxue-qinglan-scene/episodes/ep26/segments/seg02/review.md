{
  "pass": true,
  "summary": "seg02保留周建国求赵强、赵强拒绝、张总依法查封和刘美娟护夫报警的连续冲突，动作与道具状态清楚。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "周建国抱赵强裤腿并要求拿新车抵债，赵强随后踹开，原剧本关键动作和台词均保留。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "赵强左腕手表在组首、张总查封台词和组尾都被锚定，没有在登记查封前消失。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "赵强17字/3秒约5.7字/秒，刘美娟16字/3秒约5.3字/秒，张总长句约31字/5秒约6.2字/秒，均未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "抱腿、求救、踹开分为三个时间段，保镖控制作为持续状态，不抢赵强动作。",
      "fix_instruction": "若不通过，应拆开抱腿和踹开，或弱化保镖动作。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵强对周建国说车已被砸，张总对保镖说登记查封，现场对白对象明确。",
      "fix_instruction": "若不通过，应补齐赵强和张总的对白对象。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "全段固定在龙腾酒店宴会厅，赵强、刘美娟、张总、周建国和保镖都在组首有位置和朝向。",
      "fix_instruction": "若不通过，应补充缺失人物位置或拆出新空间。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "查封动作和法律文书组写有4个本组特有禁止项，锚定法律文书、赵强手表、刘美娟和周建国。",
      "fix_instruction": "若不通过，应将泛化禁止项替换为本组道具和人物锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
