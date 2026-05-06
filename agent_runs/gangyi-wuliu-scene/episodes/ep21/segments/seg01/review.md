{
  "pass": true,
  "summary": "seg01分镜完整覆盖装货区嘲讽、烂泥路颠簸、林刚放气减震等剧情，未发现硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留两家车队装箱、高级空气悬挂、林刚要求海绵垫和绑带固定药箱，陈天霸原台词与林刚原台词均完整出现。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "司机甲和林刚的连续对话合并在3-8秒，约29个有效字用5秒，约5.8字/秒，并伴随颠簸警报、看仪表盘和判断前方炮弹坑动作，节奏合理。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "组首锁定为林刚重卡驾驶室内，陈天霸车队仅作为挡风玻璃外同一烂泥路前方远景出现，没有把两个独立物理空间混成同组。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "evidence": "“物理减震”通过林刚按胎压控制阀、胎压数值下降、轮胎瘪下接地面积扩大和车身颠簸降低来可视化。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚、陈天霸和装货工人均在组首空间锁定中有画面位置、身体朝向和可见状态，后续说话与动作都有来源。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾药箱已被固定且陈天霸仍在旁边，第2组组首延续装货区两家车队并排停放，随后陈天霸车队启动、林刚上车，动作顺序连续。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "颠簸警报通过仪表盘灯闪烁、驾驶室摇晃、挡风玻璃外深坑碎石和对讲器画外音呈现，不依赖抽象心理描述。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "林刚看向前方、陈天霸车队靠气囊减震快速穿行、林刚拿对讲机下达“轮胎放气百分之三十”的关键动作和台词都保留。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "司机甲质疑和林刚回应合并在0-5秒，约28个有效字用5秒，约5.6字/秒，冷笑和移向胎压控制阀动作与台词同步，未出现过快或明显拖慢。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
