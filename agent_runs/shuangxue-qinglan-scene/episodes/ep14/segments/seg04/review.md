{
  "pass": true,
  "summary": "seg04 保留确认转账前的全员注视、金额质问和沈清按下两元转账，手机与旧银行卡状态清楚。",
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
      "evidence": "沈清手指悬在确认按钮、大家听好、周建国问金额、沈清说明不用太多并按下两元转账均按原剧本顺序保留。"
    },
    {
      "group": "第1组",
      "type": "timing_math",
      "evidence": "时间段为0-2、2-4.5、4.5-7、7-10、10-13秒，总计13秒，标题镜头数5个与实际一致。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "evidence": "禁止项锚定沈清、周美娟、沈清手机、旧银行卡和两元金额，避免按键顺序和金额被误生成。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "本组有效对白分布在2-13秒，约45字/11秒，且中间包含周建国质问和沈清回应，未超过硬上限。",
      "fix_instruction": "若压缩时长，不要让7-10秒的两句沈清对白挤到2秒内。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "悬停确认键、环视、周建国质问、沈清说明、按下确认键分阶段呈现，每个时间段只有一个主动作或连续对白节拍。",
      "fix_instruction": "若重写，应继续把按下确认键放在最后，不要提前完成转账。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、官方模板、参考图、自动分镜、@图片/@视频/@音频等工程词或模板化句式。",
      "fix_instruction": "若加入Seedance参考，也不能把模板说明写进final。"
    }
  ],
  "issues": [],
  "warnings": []
}
