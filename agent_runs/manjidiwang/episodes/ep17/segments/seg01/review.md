{
  "pass": true,
  "summary": "seg01分镜保留废厂逼近、纵火威胁、朱文浩下通风管和王队长冲锋的全部剧情，未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组"
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
      "evidence": "第1组保留朱文浩带内卫小队逼近、黑皮同伙倾倒汽油、王队长提醒纵火销毁证据、朱文浩决定从通风口下地下室。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组5-11秒为连续对话节拍，两句台词约24字加拔枪动作共6秒，未超过7字/秒，也未拖慢短句。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组始终在废弃红星工厂外，组首列出朱文浩、王队长、内卫小队、黑皮及同伙的位置和身体朝向，未跨入地下空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩、王队长、内卫小队在厂房阴影边，黑皮和同伙在远处汽油桶旁，所有行动人物在组首已有可生成位置。",
      "fix_instruction": "若不通过，应在组首补足缺失人物的位置、身体朝向和可见状态。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾朱文浩握枪看向通风管道，第2组首延续他握枪、王队长挡在身前的位置关系，随后才扯领带翻上管道。",
      "fix_instruction": "若不通过，应在第1组尾或第2组首补足朱文浩到通风管道前的过渡动作。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "苏长明的死穴通过原台词表达，纵火威胁通过汽油桶、厂房门口和黑皮同伙动作呈现，没有把抽象判断当作画面主体。",
      "fix_instruction": "若不通过，应将抽象信息替换为可见道具、动作或原台词。"
    }
  ],
  "issues": [],
  "warnings": []
}
