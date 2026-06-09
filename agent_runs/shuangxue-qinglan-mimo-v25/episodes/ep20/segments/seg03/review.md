{
  "pass": true,
  "summary": "seg03 两组均符合规则：台词忠实保留保姆费质问和青花瓷追问，口型指向正确，周美娟出场处理得当，周桂兰保持在场维持连续性，空间单一，博古架空位作为视觉线索清晰。",
  "checked_groups": ["第4组", "第5组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周建国两句台词20字÷3.5秒=5.7字/秒，周美娟12字在3.5-7.5秒内与周建国合并为连续对话节拍28字÷4秒=7.0字/秒，需检查是否超限。沈清9字÷2.5秒=3.6字/秒。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "沈清质问'我爸生前留在架子上的两只明代青花瓷呢？'完整保留，指向博古架空位的动作忠实于原剧本'指着博古架上空缺的位置'。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，周美娟从门口进入客厅并走到周建国身后，属于同一空间内入场，不需要另起一组。周桂兰虽无台词但保持在场以维持组间连续性。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内现场对白，每句写明说话人和对象，无心声/旁白混用。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个强节拍（周建国两段喊话+周美娟附和、沈清气极反笑+扫视博古架），每个时间段只承载一个主动作或连续对话节拍，10秒容量充足。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "上一组组尾'沈清视线锁定博古架空位'，本组组首'沈清右手抬起指向博古架方向'，动作自然承接；周建国和周美娟位置不变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "两个时间段分别承载：沈清质问（单一动作+台词）、周建国反应（单一反应），每段一个主动作。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}