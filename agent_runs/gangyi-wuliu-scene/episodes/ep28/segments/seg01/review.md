{
  "pass": true,
  "summary": "分段稿经节奏修复后保留原剧本所有关键台词、动作和人物关系，五组均为国际码头同一装卸空间内的连续冲突，无硬性问题。",
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
      "evidence": "原剧本的五十台重卡进码头、远洋货轮泊位、王百川擦汗台词、林刚跳下车命令降挡板和司机操作均被保留，未新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "4-7秒主管台词约10字/3秒属于短台词豁免，7-11秒王百川质问约15字/4秒，11-14秒主管回应约16字/3秒，节奏未拖慢。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "王强、赵大强、刀疤在组首被放置于集装箱堆垛阴影后方，9-11秒才走出，不存在人物突然无来源出现。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "evidence": "第5组5-9秒刀疤对林刚喊出秦爷交代的台词、王百川对林刚说违约金和积蓄，9-11秒林刚对王百川回应破产台词，对话对象均明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王强、赵大强、刀疤在组首空间锁定中位于集装箱堆垛阴影后方，随后走出并说话，具备可生成位置来源。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组结尾林刚转身面对三人，第4组组首延续为林刚位于左侧面对王强、赵大强和刀疤，位置关系连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "违约金、破产威胁和围堵通过台词、铁钩砍刀、包围圈、脱外套等可见可听信息表达，没有依赖不可视心理结论。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "整组均在国际码头吊装区，龙门吊停摆、主管走近、王百川质问和主管摊手均未切换到第二物理空间。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
