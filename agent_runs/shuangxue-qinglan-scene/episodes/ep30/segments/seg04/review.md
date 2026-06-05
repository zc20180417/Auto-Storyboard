{
  "pass": true,
  "summary": "seg04保留助理退下后的母女和解收尾、玉镯手部细节和阳光下的家，情绪释放自然且没有新增剧情。",
  "checked_groups": ["第6组"],
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
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "沈清不再提苦日子、周桂兰只享女儿福、沈清说以后都是好日子三句台词均保留，结尾仍是阳光下的母女和家。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "三句对白分别约15字/3秒、18字/3秒、13字/3秒，均低于6.5字/秒硬上限，情绪对白不被拖慢过度。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "玉镯在组首位于周桂兰手腕，0-2.5秒被沈清握住，组尾继续锚定戴玉镯的手被沈清握住。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内有手部动作、三句情绪对白和片尾缓拉，属于温情收尾，未用普通沉默硬凑。",
      "fix_instruction": "如不通过，应压缩片尾或删去无剧情停顿。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对周桂兰说道、周桂兰对沈清说道，现场对白对象明确。",
      "fix_instruction": "如不通过，应补明每句对白对象。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "没有定格、模板编号、模型说明词、参考图占位或非分镜正文。",
      "fix_instruction": "如不通过，应删除污染词或改成可见自然动作。"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "抽象的幸福和安宁被转译为母女依偎、手部相握、茶杯草莓盘和阳光下的露台家景。",
      "fix_instruction": "如不通过，应把抽象评价改成可见动作和光影。"
    }
  ],
  "issues": [],
  "warnings": []
}
