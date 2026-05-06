{
  "pass": true,
  "summary": "seg02 current final.txt 复审通过：第1组U盘与车门动作、第2组坠崖动作均已按现稿修正为合规时长，无硬错误。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组9-12秒承载“将U盘塞进自己内衣”和“一把推开副驾驶车门”两个连续动作，共3秒；12-14秒承载短台词“跳！”，总时长14秒且镜头数6个一致。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组坠落动作已拆为4-7秒和7-10秒两个无台词全景镜头，各3秒，没有保留旧 review 指出的6-10秒4秒无台词镜头。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留坠落瞬间头部撞击A柱、鲜血模糊视线、苏清寒OS“朱文浩，我没做废棋。”等原剧本信息，台词以画外音对朱文浩呈现，未删改关键情节。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首写明苏清寒在驾驶座安全带已解开、身体侧向副驾驶，小郑在副驾驶座抱双肩包；U盘从小郑包中取出再交到苏清寒手中，道具来源清楚。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第2组只发生在盘山公路悬崖边车外空间，渣土车、半悬越野车、断裂护栏和悬崖深渊均属于同一事故空间，无室内外混杂硬切。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以苏清寒喊“跳”、小郑向车门倾斜结束；第2组接渣土车后退、撞上越野车并使其坠崖，跳车提示到撞击坠落的动作链连续。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "第3组用车内天旋地转、头部撞击A柱、鲜血从额头涌出、染血手指攥紧衣料等可拍细节呈现坠落冲击和意识模糊，OS台词来源明确。",
      "fix_instruction": "通过，无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
