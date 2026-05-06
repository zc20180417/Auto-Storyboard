{
  "pass": true,
  "summary": "seg01复审通过。朱天和出门台词已补回第1组，两个餐厅组均保留原剧本台词与动作，时长、空间锁定和对话指向合规。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "0-3秒已保留朱天和原台词\"我去集团，让你母亲陪你去。\"，并保留原动作\"大步出门/离开\"；3-5秒李娟下楼入场，5-7秒保留\"太阳打西边出来了？起这么早。\"，7-11秒保留朱文浩\"母亲，今天麻烦您陪我去苏家。\"。"
    },
    {
      "group": "第1组",
      "type": "timing_math",
      "evidence": "0-3秒、3-5秒、5-7秒、7-11秒相加为11秒，与组标题总时长11秒一致；镜头数4个与实际时间段数一致。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-5秒连续短句问答包含\"去那干嘛？/提亲/跟苏家大女儿苏清寒？/是的\"，按连续对话节拍整体承载；5-9秒两句共20字分配4秒，约5.0字/秒；9-13秒两句与转身动作共约20字分配4秒，节奏合规。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组完整覆盖\"集团高岭之花，被你拿下了？\"、\"恋爱三年，时机成熟。\"、\"有意思，老苏老脸往哪搁。\"、\"买套正装，我给你撑场子。\"，无删改台词或新增剧情动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和、朱文浩在组首空间锁定中已位于朱家餐厅；李娟在4-6秒通过\"穿着真丝睡袍从楼梯走下\"明确入场后才开口说话。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组全程发生在朱家别墅餐厅，朱天和离开和李娟下楼均是同一室内空间内的连续动作，没有负面状态描述或跨物理空间硬切。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾朱文浩站起并面向李娟；第2组组首朱文浩仍在餐桌旁面向李娟，李娟端着茶杯面向朱文浩，人物位置与道具状态自然承接。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "审视、大笑、淡定等表演状态均转译为视线上下打量、嘴角咧开、面色淡定和视线迎向对方眼睛等可拍动作与表情。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
