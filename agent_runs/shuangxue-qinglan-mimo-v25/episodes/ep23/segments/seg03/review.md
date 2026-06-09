{
  "pass": true,
  "summary": "seg03（第6-8组）通过审核。手机屏幕揭示答谢宴、三人嫉妒发狂、周建国决定明天去闹，台词忠实、道具连续、空间单一。",
  "checked_groups": ["第6组", "第7组", "第8组"],
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
      "type": "prop_continuity",
      "evidence": "屏幕摔裂的手机在第6组组首'手中持有'，2-4秒举起展示，6-7秒赵强和周建国凑向手机，道具归属和位置连续。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "周建国'肯定是那死老太婆私吞了老头子的遗产！'24字÷5秒=4.8字/秒，节奏合格。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "周建国'走！明天咱们去闹一场！''我还是她合法丈夫，她敢不给我钱？'和周美娟'对！当着全城名流的面，看她敢不敢赶我们！'均忠实原剧本23-3。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人对白，无心声/画外音需要音画分离。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒组3个强节拍（周美娟嫉妒喊、赵强震惊问、周建国咬牙说），属于同一冲突推进，不过载。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组组尾周建国咬牙站在原地、周美娟坐在床边、赵强站在原地；第8组组首周美娟坐在床边（连续）、赵强和周建国站在原位（连续），状态衔接无跳变。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}