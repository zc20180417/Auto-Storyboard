{
  "pass": true,
  "summary": "已按原剧本、生成规则和当前分镜逐组审查，segment 01 的四组均保留关键动作、台词、电话来源和场景边界，无硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
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
      "evidence": "3-8秒为屋内快速问答，三句台词约25个有效字，5秒内包含两次换人和正在挨打求饶的反应，字秒比约5.0；8-10秒承接原剧本手机突然震动，整组总时长10秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组场景始终为赵大强家内，王强只通过电话画外音出现，未把王强所在空间硬切进同一组。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留赵大强问“怎么搞？我这条烂命豁出去了！”，王强约他晚上进城，村民甲抢手机，以及赵大强推开村民甲、抓破菜刀乱挥并喊“滚开！老子马上就有大钱了！”的全部关键内容。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "evidence": "第4组标题总时长13秒，时间段为0-3、3-6、6-8、8-10、10-13秒，相加13秒，镜头数5个与实际时间段一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵大强、村民甲、村民乙都在组首锁定中有画面位置和身体朝向，扫帚和手机也在空间内可见或可用。",
      "fix_instruction": "无需修复；若后续增加人物，必须在组首或行动前给出位置或声音来源。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王强被明确标注为只通过电话声音出现，赵大强接听手机后才听到他的电话画外音，人物来源清楚。",
      "fix_instruction": "无需修复；电话角色继续保持画外音来源即可。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组结尾赵大强趴地握手机，第3组组首延续为赵大强位于画面右侧地面、右手攥着接通的手机，村民甲和村民乙仍在屋内逼近。",
      "fix_instruction": "无需修复；组间手机归属和人物位置已连续。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第4组是新的总裁办公室物理空间，组首锁定落地窗、真皮沙发、茶几、合同和两人坐位，未与赵大强家混在同一组。",
      "fix_instruction": "无需修复；不同物理空间已另起一组。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“钱不是问题。下午去银行提现。”通过林刚放下茶杯站起身、看向王百川说出安排来呈现，没有把抽象判断当画面信息。",
      "fix_instruction": "无需修复；保持以可见动作和原台词传达剧情。"
    }
  ],
  "issues": [],
  "warnings": []
}
