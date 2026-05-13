{
  "pass": true,
  "summary": "seg01（第1-2组）通过审核，HR报到和任务交派场景台词节奏合理，心声正确标注闭口，无硬错误。",
  "checked_groups": ["第1组", "第2组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "generation_density": "checked",
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
      "evidence": "4-11秒连续对话节拍：35字/7秒=5字/秒，低于6.5字/秒硬限制。含2次换人和倒水递水动作，节奏合理。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本心声'想看我出丑？好戏刚开始'完整保留，正确标注为心声格式、嘴唇闭合不做口型。'服从安排''下周战投部中期风控研判''这个艰巨任务交给你了'等关键台词全部保留。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组保持单一物理空间（集团HR部二处办公室），0-4秒敲门迎接到4-11秒倒水对话，均在同一办公室内完成，无跨场景硬切。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩和赵德胜均在组首空间锁定中声明位置：赵德胜坐在办公桌后方（画面深处），朱文浩站在门口（手持报到证）。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部朱文浩接过水杯、赵德胜面带笑意站在一旁；第2组组首赵德胜站在朱文浩面前、朱文浩手中端着水杯，人物位置和道具状态连续。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "心声'想看我出丑？好戏刚开始'已转译为可见表演：嘴角冷笑、锐利眼神、视线看向走廊尽头、嘴唇闭合不做口型。",
      "fix_instruction": "N/A"
    }
  ],
  "issues": [],
  "warnings": []
}