{
  "pass": true,
  "summary": "seg01逐组对照原剧本、生成规则和当前分镜完成审稿，关键台词、动作、空间和时长均未发现硬性问题。",
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
      "evidence": "2-14秒为赵大强、林刚、村民甲、村民乙围绕车钥匙和收费的快速短句交锋，含原台词约63个有效字、6轮台词、12秒承载，字秒比约5.3，符合情绪对峙节奏。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留小混混威胁交钥匙、林刚说“想要车？行啊。”、回院子取通电角磨机、小混混误喊电锯、切断大铁锁、赵大强喊“你敢砸我的锁！”等全部关键动作和台词。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组只发生在夜晚阴天停车场，赵大强、白糖、面包车油箱口均在组首锁定，未把赵大强家门外电话场景混入同组。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "evidence": "赵大强对手机里的债主说“喂？李哥……”，债主画外音明确标注来源为手机并对赵大强凶狠说道，心声也写为赵大强对自己。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚、赵大强、村民甲、村民乙在组首均有画面位置、身体朝向和视线关系，后续台词人物都可生成。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾铁锁断开、林刚蹲在车轮旁，接第3组首粗铁链已断、林刚手持刚停下的角磨机，赵大强摩托车已横在车前，状态可连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“臭气熏天”未直接当作画面信息，而是转译为赵大强衣裤沾满黑泥、水珠从袖口滴落、从臭水沟爬出等可拍细节。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第6组单一空间为赵大强家门外，债主只以手机听筒画外音出现，不构成跨物理空间硬切。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
