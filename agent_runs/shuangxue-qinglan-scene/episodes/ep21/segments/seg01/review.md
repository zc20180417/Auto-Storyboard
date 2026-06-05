{
  "pass": true,
  "summary": "seg01保留沈清带律师进院、周美娟拒搬和律师宣告限期公告生效，格式与时长可执行。",
  "checked_groups": ["第1组"],
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
      "evidence": "原剧本中沈清带律师准时推开院门、院子凌乱未收拾、周美娟两句拒搬和律师限期公告台词均保留，未新增改变剧情的动作。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "周美娟两句约26字用4秒，约6.5字/秒；律师约34字用6秒，约5.7字/秒，未超过硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首锁定周家院落院门口一个物理空间，沈清、周桂兰、律师、周美娟均有画面位置、身体朝向和关键道具状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟和律师均为现场开口对白，分别写明对沈清、对周美娟说道，没有心声或画外音混用。",
      "fix_instruction": "若不通过，应补明确对话对象或改写为可见声音来源。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含进院、环境确认、周美娟短句挑衅、律师宣告四个顺序节拍，14秒内每段只承载一个主动作或连续对白。",
      "fix_instruction": "若不通过，应拆分进院和律师宣告，或压缩非关键环境镜头。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾保留沈清、周桂兰、律师在院门内侧，周美娟在散乱行李旁，律师仍持公告副本，可接下一段院内对峙。",
      "fix_instruction": "若不通过，应在组尾补人物位置和公告副本归属。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "法院限期腾房公告副本从组首到律师宣告再到组尾都在律师手中，散乱行李始终位于周美娟身旁。",
      "fix_instruction": "若不通过，应补公告副本被律师举起或收回的可见过渡。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "推门入院、院内凌乱展示、周美娟挑衅、律师宣告分别落在连续时间段，单段没有塞入多个顺序主动作。",
      "fix_instruction": "若不通过，应拆开推门与人物跨入动作。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项共3条，锚定周美娟、散乱行李、法院限期腾房公告副本和周桂兰，没有使用占位词或泛泛词。",
      "fix_instruction": "若不通过，应替换为本组人物、道具、场景相关的具体错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
