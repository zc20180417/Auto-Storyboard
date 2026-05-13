{
  "pass": true,
  "summary": "seg01已对照原剧本和横屏规则审完，喂食、命名、水雾心声三个节拍完整，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "第1组把天天放在画面左侧前景，水壶放在桌面中央，房门和门闩在画面右后方，半个馒头从口袋到壶口的路径清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组6.5-10秒承载“慢点吃...”约16个有效字，3.5秒内约4.6字/秒；10-14秒承载命名台词约18个有效字，4秒内约4.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "第3组6-11秒明确天天嘴唇闭合不做口型，画外心声响起，心声没有被误写成现场开口。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "水雾由云宝在水壶底部张嘴产生，穿过壶口落到天天手背和脸颊，来源、路径、结果均可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留反锁房门、掏出半个干硬白馒头、对水壶轻声喂食的剧情顺序，没有新增改变剧情的动作。",
      "fix_instruction": "无需修复；若后续改写，请继续保留房门右后方和水壶中央的空间锚点。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天两句对白都写为对水壶里的云宝说道，现场口型和被说对象明确。",
      "fix_instruction": "无需修复；若删减台词，不能改动原句和说话对象。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "每个时间段都有运镜设计，固定道具近景、轻微摇向、固定中近景分别服务云宝翻滚、水雾路径和心声音画分离。",
      "fix_instruction": "无需修复；若调整运镜，仍需写清起点、终点或稳定理由。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "三个组首空间锁定均为静态第一帧状态，没有把走位、拿放、进入等过程动作写入锁定行。",
      "fix_instruction": "无需修复；后续组首仍需只写静态位置和视线关系。"
    }
  ],
  "issues": [],
  "warnings": []
}
