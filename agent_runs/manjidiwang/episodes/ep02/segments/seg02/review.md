{
  "pass": true,
  "summary": "seg02 三组均忠于原剧本，门口对峙空间单一，对话指向清晰，时长计算合规，无硬性错误。",
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
      "evidence": "2-6秒王涛台词21字/4秒=5.25字/秒，符合普通对白5.2字/秒基准向上取整；8-10秒12字情绪台词/2秒=6.0字/秒，符合情绪基准。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出朱文浩挡门框中央、面向镜头、脸朝画外，王涛站台阶下面朝画左，单组物理空间为别墅门口，无跨场景。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "王涛逃跑动作'死死抱住塑料袋，跌跌撞撞地逃跑'完整保留于0-3秒；朱文浩OS'现代商战走狗，骨头太软'完整保留于5-7秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩与王涛均在组首空间锁定中获得明确画面位置与身体朝向，两人对峙关系清晰，无'尚未进入'等不可生成描述。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱文浩冷扫质问、王涛发毛状态；第2组组首为朱文浩仍挡门框、王涛仍站台阶下紧抱塑料袋，人物位置与道具状态连续。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'堆笑''发毛''结巴''冷酷''嘲弄''质问'等情绪标签均已转译为具体的面部肌肉变化、视线移动与身体姿态，无抽象概念直出。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
