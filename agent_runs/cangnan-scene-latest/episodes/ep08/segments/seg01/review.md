{
  "pass": true,
  "summary": "seg01两组保留徐虎封杀沙石和陆凡上门的关键台词动作，格式、时长、空间锁定和对白指向均可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中徐虎扯掉纱布、手下汇报找料和封杀、徐虎狂笑威胁卖沙均按原顺序保留。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "陆凡未在组首出现，但在4-7秒有明确推门入场动作，且在7秒后才开口。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“徐老板，胃口不小啊”约9字用3.5秒，徐虎“你还真敢送上门来？”约10字用3.5秒，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写清办公室、办公桌、门、徐虎和手下的位置与身体朝向，未把空间锁定写成镜头动作。",
      "fix_instruction": "若失败，应补足人物位置、身体朝向和关键道具静态状态。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部徐虎在桌后、手下站前，第2组首部继续保持同一办公室和门关闭状态，陆凡随后推门进入。",
      "fix_instruction": "若失败，应在第1组尾或第2组首补门和人物位置状态。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、参考图、模板编号、自动分镜或广告/MV模板语气。",
      "fix_instruction": "若出现污染词，应删除工程说明并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
