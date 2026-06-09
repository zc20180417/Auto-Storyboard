{
  "pass": true,
  "summary": "seg01 两组均符合规则：台词忠实、口型指向正确、时长节奏合理、空间单一且连续、道具油纸包归属清晰。",
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
      "evidence": "周建国两句台词13字÷4秒=3.25字/秒，沈清反问14字÷5秒=2.8字/秒，连续对话节拍有效字数27字÷5秒=5.4字/秒，均未超6.5字/秒硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首锁定周建国坐太师椅、沈清在画面右侧、周桂兰在画面左侧坐着，三人均有位置和朝向描述。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "油纸包从周桂兰贴身衣物中取出（0-4秒），递到沈清手中（4-9秒），组尾衔接写明'油纸包在沈清手中'，与下一组连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内现场对白，无心声/旁白/画外音，每句写明说话人和对象。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个强节拍（两句耍赖台词+沈清反问转向），每段只承载一个主动作，13秒容量充足。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "上一组组尾'周桂兰起身准备取物'，本组组首'周桂兰刚起身站立'，人物位置连续；周建国和沈清位置不变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第一段只承载周桂兰取物动作，第二段只承载递出油纸包+沈清接过，每段一个主动作。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "character_availability",
      "problem": "周桂兰未在seg01 script.txt人物列表中出现，但在分镜中加入以保持组间连续性（seg02需她递出油纸包）。",
      "evidence": "script.txt人物为'沈清、周建国、周桂兰'，周桂兰实际在场且有台词，属于合理补充。",
      "fix": "无需修改，周桂兰在原剧本中确实出现在seg01场景。"
    }
  ]
}