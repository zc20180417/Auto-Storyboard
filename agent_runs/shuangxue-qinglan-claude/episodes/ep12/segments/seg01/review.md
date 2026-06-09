{
  "pass": true,
  "summary": "三组分镜忠实覆盖原剧本全部台词和动作，台词节奏合理，空间连续性正确，关键道具银行流水账单状态变化清晰。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "周美娟尖叫台词11字÷2.5秒=4.4字/秒（情绪对白），周建国耍赖台词21字÷4秒=5.25字/秒（情绪对白），均在合理范围内，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "三组均在同一物理空间周家正屋客厅，无跨场景。第2组组首写明茶几空无一物、沈清手中提着背包，与第1组组尾衔接正确。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "沈清一字一句台词'今晚，全家对账！少一分，咱们就法庭见！'完整保留，未删改。周建国、周美娟、赵强三人的僵住反应忠实于原剧本'彻底不要脸的一家人'对峙后的情绪。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人开口对白，周美娟对沈清喊道、周建国对沈清大骂，均有明确说话对象，无心声或画外音混用。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组11秒内安排冷笑（微反应）+拉开背包拿账单（中等动作）+铺账单（中等动作）+台词+周建国微反应，属于同一连续事件链的阶段，每个时间段只承载一个主动作，表演时间充足。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组到第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾：沈清手中仍提着背包；第2组组首：沈清手中提着背包。第1组组尾：周建国手指指向沈清；第2组组首：周建国手已放下。过渡自然，状态连续。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "背包从第1组沈清手中持有→第2组拉开拉链拿出账单→账单铺满茶几→第3组茶几上仍铺满账单。道具状态变化链完整，每一步都有可见过渡动作。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第2组5个时间段各承载一个主动作：冷笑→拿账单→铺账单→说台词+直起身→周建国反应，无多个主动作挤在同一时间段。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第2组视频禁止项列出4条本组特有风险（账单消失、茶几消失、沈清提前离场、周建国等人散开），均锚定本组具体人物和道具，无泛泛词。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "video_negative_constraints",
      "problem": "第1组涉及多个人物调度（周美娟和赵强从里屋冲出、周建国上前指骂），但未输出视频禁止项。",
      "evidence": "第1组正文无视频禁止项行。",
      "fix": "建议补充2-3条本组特有风险，如'周美娟和赵强从客厅中央出现而非里屋''周建国手指未指向沈清''沈清提前打开背包'。"
    }
  ]
}
