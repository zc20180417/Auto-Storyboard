{
  "pass": true,
  "summary": "seg03 已对照身份揭露、搜索假人设、证据链、十秒沉默和名片离开审阅，剧情闭环完整。",
  "checked_groups": ["第11组", "第12组", "第13组", "第14组"],
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
      "group": "第11组",
      "type": "script_fidelity",
      "evidence": "房门关上、苏清寒问身份、朱文浩回答集团常务副董之子、搜索朱文浩并显示花花公子等假人设均完整保留。"
    },
    {
      "group": "第12组",
      "type": "filmability",
      "evidence": "苏长明三年贪腐证据链、苏晓晓转账记录、李佳佳异常账户均放在手机屏幕界面呈现，属于可拍道具信息。"
    },
    {
      "group": "第13组",
      "type": "timing_math",
      "evidence": "第13组0-3秒为朱文浩选择台词，3-13秒分成四段无口型沉默反应，明确覆盖原剧本“沉默十秒”，13-15秒接过手机，总时长15秒。"
    },
    {
      "group": "第14组",
      "type": "dialogue_pacing",
      "evidence": "朱文浩“验证完，打这个电话。只等24小时。”用3.5秒承载递名片动作，苏清寒心声用4.5秒闭口反应承载，节奏未超硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第11组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第10组安保退出后，第11组组首写明房门已经关上且屋内只剩朱文浩和苏清寒，承接清楚。",
      "fix_instruction": "无需修改；不得让安保人员继续留在房内。"
    },
    {
      "group": "第12组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "“看看这个”、证据链、妹妹苏晓晓和母亲李佳佳账户、苏清寒“你……你早就知道？”以及朱文浩查半年均保留。",
      "fix_instruction": "无需修改；证据链不得改成其他人物或其他案由。"
    },
    {
      "group": "第13组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "本组沉默十秒来自原剧本明确动作，不是普通拖时；无台词反应被拆为多个可见手指、视线、屏幕细节。",
      "fix_instruction": "无需修改；保留十秒沉默证据，不要压缩成普通短反应。"
    },
    {
      "group": "第14组",
      "type": "filmability",
      "result": "pass",
      "evidence": "名片递交、接过名片、脚步虚浮离开和心声闭口均为可拍动作或清晰声画分离。",
      "fix_instruction": "无需修改；心声继续使用嘴唇闭合、不做口型。"
    }
  ],
  "issues": [],
  "warnings": []
}
