{
  "pass": true,
  "summary": "seg02 单组15秒，台词忠实完整保留遗嘱内容，口型指向正确，时长节奏合理，空间单一，道具遗嘱和油纸包状态连续。",
  "checked_groups": ["第3组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清连续台词29字÷4.5秒=6.4字/秒，未超6.5字/秒硬上限；宣读遗嘱19字÷3.5秒=5.4字/秒，在合理范围内。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "遗嘱原文'房屋产权归女儿沈清所有，周桂兰仅有居住权'完整保留，沈清逼视台词'这房子，从我十八岁起，产权就是我的！我让你们住是情分，赶你们走是本分！'无删改。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首锁定沈清在画面中央手持油纸包、周建国在太师椅上，无跨空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内现场对白，沈清对周建国直接宣读和逼视，无心声/旁白/画外音。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "5个时间段承载拍遗嘱、指字宣读、宣读遗嘱、周建国震惊、沈清逼视，每个时间段只承载一个主动作或连续对话节拍，15秒容量合理。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "上一组组尾'油纸包在沈清手中'，本组组首'沈清手中持有油纸包'，道具连续；周建国太师椅位置不变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "油纸包从沈清手中展开（0-2.5秒），遗嘱拍在茶几上后保持摊开状态至组尾，组尾衔接写明'遗嘱仍在茶几上摊开'。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}