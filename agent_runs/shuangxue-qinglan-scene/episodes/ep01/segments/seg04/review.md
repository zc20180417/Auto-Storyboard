{
  "pass": true,
  "summary": "seg04完成门外听见到账声和沈清锁定餐厅方向，画外音来源明确。",
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
    {"group": "第1组", "type": "audio_mouth_sync", "evidence": "刘美娟不在画面内，只以餐厅方向画外音出现；沈清嘴唇闭合不做口型，声音来源和口型分离正确。"},
    {"group": "第1组", "type": "dialogue_pacing", "evidence": "刘美娟画外音约22字占4秒约5.5字/秒，沈清台词约12字占3秒约4字/秒，均未超过硬上限。"},
    {"group": "第1组", "type": "script_fidelity", "evidence": "保留玻璃杯碰撞声、刘美娟‘这月到账真准’和‘小雨的钢琴课尾款’信息、沈清‘好一个到账真准’反应。"}
  ],
  "semantic_checks": [
    {"group": "第1组", "type": "space_locking", "result": "pass", "evidence": "组首限定杂物间门外，餐厅只通过亮灯窗户和画外音存在，没有跨入餐厅实体空间。", "fix_instruction": "若进入餐厅，应另起组或标明转场。"},
    {"group": "第1组", "type": "handoff_continuity", "result": "pass", "evidence": "承接上一段沈清背靠杂物间门框，组首复述破旧木门打开和她背靠门框。", "fix_instruction": "若位置跳到餐厅门口，应补移动动作。"},
    {"group": "第1组", "type": "action_atomicity", "result": "pass", "evidence": "站稳、玻璃杯声引转头、画外音、沈清咬牙回应分段清楚。", "fix_instruction": "若把听音和冲进餐厅并列，应拆分。"},
    {"group": "第1组", "type": "prompt_pollution", "result": "pass", "evidence": "正文无模板编号、Seedance说明、占位符或广告/工程词。", "fix_instruction": "若出现模板词，应删除。"}
  ],
  "issues": [],
  "warnings": []
}
