{
  "pass": true,
  "summary": "seg02（第3-4组）通过审核，会议室质问场景台词节奏合理，老孙掉笔反应、王海涛凉茶动作均保留，无硬错误。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "5-10秒连续对话节拍：'城南地块三期两亿资金。为什么没过风控会？'28字/5秒=5.6字/秒，低于6.5字/秒硬限制。含老孙掉笔反应镜头和王海涛坐直反应，节奏合理。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "原剧本关键台词完整保留：'你这是查账，越界了！''违规特批，总裁兜底吗？''资金暴雷，你拿什么自证清白？''郑总监独断专行。资金流向，我完全插不上手。''您慢点说，我们详细记。'凉茶猛灌动作保留。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "全组保持单一物理空间（战投部会议室），0-3秒王海涛敷衍开场、3-5秒朱文浩打断、5-10秒逼问资金问题，均在同一会议室内完成。四名角色位置均在组首声明。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "四名角色均在组首空间锁定中声明位置：王海涛坐在会议桌一侧（画面右侧），朱文浩坐在另一侧（画面左侧），老孙坐在王海涛旁边手中握笔，吴德海坐在老孙旁边。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部王海涛坐直身体、脸色大变；第4组组首王海涛坐在会议桌一侧、上半身坐直、脸色惊变，状态连续。老孙和吴德海仍在原位。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "所有台词和动作均为可拍内容：发怒表情、撑桌动作、前倾逼视、凉茶猛灌、咬牙说话、拿笔翻开笔记本。无不可视信息。",
      "fix_instruction": "N/A"
    }
  ],
  "issues": [],
  "warnings": []
}