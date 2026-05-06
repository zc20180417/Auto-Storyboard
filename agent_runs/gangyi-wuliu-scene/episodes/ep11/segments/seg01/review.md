{
  "pass": true,
  "summary": "seg01已对照原剧本、生成规则和当前分镜逐组审核，台词、关键动作、空间锁定、时长数学和格式均通过，未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "type": "dialogue_pacing",
      "evidence": "3-6秒王强台词“满载高档冻肉。两小时送到南区冷库。”约16个有效字/3秒，约5.3字/秒；8-10秒“不敢开就拿着你的二十万滚蛋！”约14字/2秒，约7.0字/秒，未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留林刚掏螺丝刀撬开控制面板、要求王强过来看、展示两根粗大电源线被整齐剪断、指出新剪口和王强后退否认等原剧本关键动作和台词。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "全组限定在货运场大门附近，冷藏车驶出、王强躲到堆货角落拨号均属于同一货运场空间内连续动作，没有跨主要物理空间硬切。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首明确王强、林刚、王百川三人在冷藏车停放区的位置和身体朝向，后续三人台词和动作均从该空间关系发生。",
      "fix_instruction": "无需修复；若后续新增人物，应在组首或出场动作前给出可生成位置。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "制冷机恢复通过指示灯亮起、轰鸣声、强冷风吹动衣角和雾气散开呈现，未把不可视判断作为主要画面。",
      "fix_instruction": "无需修复；继续用可见道具状态和声音表现机械恢复。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾为制冷机恢复运转且三人看向指示灯，第5组首延续到冷藏车车门旁并说明制冷机已恢复、车头轻微震动，人物和道具状态连续。",
      "fix_instruction": "无需修复；同场景相邻组继续保持车门、人物位置和制冷机状态一致。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留冷藏车喷尾气开出大门、王强躲到角落掏手机拨号，以及对豹哥说“带几个人去南崖路堵个大车。往死里打！”的威胁。",
      "fix_instruction": "无需修复；不得删减电话内容或改变打电话对象。"
    }
  ],
  "issues": [],
  "warnings": []
}
