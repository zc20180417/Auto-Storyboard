{
  "pass": true,
  "summary": "两组分镜格式正确，台词忠实，空间连续，节奏合理，无硬问题。",
  "checked_groups": ["第1组", "第2组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组仅第4时间段有台词（周美娟11字/4秒=2.75字/秒），属正常语速，其余为无台词动作镜头，节奏合理。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "全组单一物理空间（周家客厅），组首锁定所有在场人物位置和朝向，无跨空间问题。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清两句台词完整保留：'法院的期限已过，我合法重装我自己的家！你们不是喜欢赖在这吗？'（27字/5秒=5.4字/秒）和'既然不想体面地走，那就配合法院强制执行吧。'（18字/4秒=4.5字/秒），说话对象均为周美娟，台词顺序与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟的喊叫为画面内现场开口对白，写明了对工人们喊道，有明确说话对象和口型。无心声/画外音/电话音混用。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "4个强节拍（工人拆卸、窗框松动、窗落地+风灌入、周美娟尖叫），属同一连续事件链的因果推进，每段一个主动作，12秒承载合理。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾锚定旧落地窗已落地、窗框空洞、寒风灌入、周美娟抱头站立、沈清面向周美娟。第2组组首复述空窗框处寒风持续灌入、沈清面向镜头衣角被风吹动、周美娟双手仍抱在头顶附近。状态连续无跳变。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每组每个时间段只承载一个主动作：第1组为工人拆卸→窗框松动→窗落地→周美娟尖叫；第2组为沈清说话→周美娟反应→沈清冷笑说话。无动作过载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组为拆除动作组，拆卸工具已通过组首空间锁定和镜头描述锚定；第2组为普通对话组，无需视频禁止项。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文无Seedance可、自动正反打、模板编号、@图片/@视频/@音频占位符、广告slogan等模型说明词或工程词。无模板化批量描述。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}