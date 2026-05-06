{
  "pass": true,
  "summary": "seg01 current final.txt 复审通过：第1组旧硬伤已修复，3组均无台词节奏、原剧本忠实度、空间锁定或格式硬错误。",
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
      "evidence": "第1组小郑台词“姐姐，后面有车追我们！”约10字，2秒承载；苏清寒“抓紧扶手！”短台词2秒承载。原4-8秒无台词反应已拆为4-6秒小郑盯后窗、6-8秒苏清寒看后视镜，均未超过无台词3秒上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留后方两辆无牌渣土车逼近、黑皮在头车内用对讲机下令、渣土车撞向越野车尾部等原剧本关键动作和台词，没有提前改写撞击结果。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组场景限定在被撞后的黑色越野车内部，苏清寒在驾驶座、小郑在副驾驶座，方向盘和双肩包位置明确，单组内无跨物理空间硬切。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "旧问题中“小郑身体被惯性甩向车门方向”的撞击后动作已不存在；当前4-6秒仅写小郑身体前倾、盯后窗、嘴唇颤抖，符合撞击前追车紧张状态。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定写明苏清寒位于驾驶座双手握方向盘，小郑位于副驾驶座双手紧抱双肩包，两人后续台词和动作均有可生成位置来源。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以苏清寒盯前方路面、双手握方向盘结束，第2组切到车外渣土车逼近并撞击越野车尾部，镜头空间切换服务原剧本追车撞击事件，因果连续。",
      "fix_instruction": "通过，无需修改。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "第3组使用头部后仰、猛打方向盘、车身左右摇摆、小郑撑住车门等可见动作呈现失控甩尾，没有把抽象心理判断当作主要画面信息。",
      "fix_instruction": "通过，无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
