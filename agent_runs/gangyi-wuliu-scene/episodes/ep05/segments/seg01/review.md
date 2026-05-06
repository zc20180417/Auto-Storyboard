{
  "pass": true,
  "summary": "已对照第5集完整剧本、生成规则和当前分镜逐组审稿，5组均保留原台词与关键动作，未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组"
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中刘管家捏鼻子指帝王蟹、怒斥“都发臭了！十万块的货，你赔得起吗！”，林刚反问“迟到五分钟能臭成这样？你逗我？”，保安推搡并骂“让你赔钱听见没！穷光蛋！”均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组5-7秒“车厢温度二十五度！”约9字/2秒=4.5字/秒，短台词配合举枪动作可接受；9-12秒“冷机根本没开过，出站前就是坏的！想黑我？”约17字/3秒=5.7字/秒，符合情绪质问节奏。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组全程发生在雨夜别墅门口，王主管只通过刘管家手机免提画外音出现，没有把电话另一端作为新的物理空间硬切。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组结尾为刘管家握手机僵住、林刚仍举测温枪；第4组开头林刚先把测温枪放低到身侧，再说差价背锅，手机仍在刘管家手里，过渡连续。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "evidence": "赵大强两句台词均写明对村民们喊道/说道，村民甲的提问写明对赵大强问道，对话对象清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚、刘管家、保安三人都在组首空间锁定中有画面位置和身体朝向，后续捏鼻子、发火、反问、推搡都由已在场人物完成。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾保安推住林刚；第2组首延续为林刚胸口被保安顶住，随后林刚推开保安、保安倒地，人物状态衔接自然。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本的恶臭没有被当作不可视画面单独输出，而是通过刘管家捏鼻子、泡沫箱污水、台词“都发臭了”承载；电话挂断用手机免提断线和忙音呈现。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林刚指出主管赚差价、刘管家道歉、掏金色名片并自称刘福和王百川管家、林刚接名片要求结清运费，均未删改关键台词和道具。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第5组单独进入晴天村头空地，组首锁定拖拉机、赵大强和村民位置，未与雨夜别墅门口合并在同一组内。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "dialogue_pacing",
      "problem": "王主管画外音节奏略快但未超过硬错误阈值。",
      "evidence": "第3组5-7秒“刘管家，是那个司机没开冷机！”约14字/2秒=7字/秒，属于6-7字/秒偏快区间。",
      "fix": "如后续制作觉得听感紧，可将该句与前后反应微调到3秒，但当前不阻断通过。"
    }
  ]
}
