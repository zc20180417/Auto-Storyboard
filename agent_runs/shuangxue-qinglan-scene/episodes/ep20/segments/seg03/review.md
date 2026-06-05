{
  "pass": true,
  "summary": "seg03保留三十万保姆费勒索、周美娟附和、沈清转向青花瓷空位质问的冲突升级，未发现硬问题。",
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
      "type": "script_fidelity",
      "evidence": "周建国功劳、三十万保姆费、周美娟必须给钱、沈清反笑四个原剧本节点按顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组四个对白时间段约23字/4秒、18字/3.5秒、17字/3秒、15字/3.5秒，最高约5.75字/秒，均低于6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组始终在周家正屋客厅，组首明确茶几、遗嘱、博古架空位和四人位置。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组是同一勒索节拍下的连续短句交锋，四个时间段分别承载周建国两句、周美娟附和、沈清反击，没有并列外部事件或动作过载。",
      "fix_instruction": "无。若加入额外动作，应拆组或删除。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "泛黄遗嘱留在茶几上，同时新增博古架空位作为被质问道具状态，组尾同时锚定两者。",
      "fix_instruction": "无。若遗嘱或空位跳变，应补具体位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清质问明确对周建国说道，没有把质问对象错置到周美娟。",
      "fix_instruction": "无。若对象含糊，应补周建国。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考模板、自动分镜、占位符或泛化模板句。",
      "fix_instruction": "无。若出现工程词，应删除并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}

