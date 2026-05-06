{
  "pass": true,
  "summary": "seg03分镜完整覆盖正门火场、黑皮狂笑、叉车冲出、交付防火袋和收网指令，审核未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "type": "character_availability",
      "evidence": "第1组组首将朱文浩锁定在厂房火墙后方的报废叉车驾驶位，被烟火遮挡，支持后续叉车撞出火墙。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留朱文浩满脸烟灰、单手抓方向盘冲出火海、刹车说让他失望了、跳车并把防火袋拍给王队长。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组2-4秒和4-7秒分别承载朱文浩两句短促收网台词，均与转头、看向王队长动作同步，节奏未拖慢。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "三组都发生在红星工厂正门外，叉车从同一火墙缺口冲出，没有把地下室空间和正门空间塞入同一组。",
      "fix_instruction": "若不通过，应将地下室和室外正门拆成不同组或标明合法转场类型。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾叉车撞出火墙，第2组首延续叉车车头在正门缺口、朱文浩在驾驶位、王队长仍踩住黑皮。",
      "fix_instruction": "若不通过，应补足叉车从撞墙到停在正门外的状态衔接。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "铁证通过防火袋内账本、合同和公章的可见轮廓呈现，收网和拦五亿资金通过朱文浩原台词表达。",
      "fix_instruction": "若不通过，应以可见证据道具和原台词承载抽象的铁证信息。"
    }
  ],
  "issues": [],
  "warnings": []
}
