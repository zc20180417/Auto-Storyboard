{
  "pass": true,
  "summary": "seg01四组已对照原剧本和横屏规则完成审核，救援承诺、父亲闪回、水壶归属和堂屋到屋外的动作链完整，无阻断问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "原剧本的天天触到陶笛后缩手、小爪子松开跌回黑暗、天天喊“对不起！我不是故意的！”均保留，裂缝青蓝光变弱作为组尾状态。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“你千万别死！等我回来救你！”有效约11字，安排在2.5秒镜头内，约4.4字/秒，配合绝望喊话和动作反应，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "堂屋内左侧门口、中央木桌、右侧水壶明确；闪回院子中幼年天天在左、爸爸在右，父子视线轴线和陶笛交接位置清楚。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "陶笛从闪回中落到幼年天天手里，现实中水壶由天天抱在胸前并带出屋外；全家福只作为情绪锚点，没有改变道具归属。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写天天低伏、陶笛横在裂边、小爪子半露和青蓝光微弱等第一帧静态状态，没有把缩手或小爪子跌落写入组首。",
      "fix_instruction": "若出现过程动作，应移入对应时间段镜头描述，并保留静态位置锚点。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "第2组包含固定裂缝、固定过肩、后拉建立路线、横向跟拍奔跑和固定远景落点，运镜围绕救援承诺和离开裂缝递进。",
      "fix_instruction": "若运镜变空泛，应写明跟随天天奔向村道或固定裂缝与陶笛的服务目的。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组从现实水壶触发闪回，第4组继续闪回父亲台词后回到现实全家福和水壶，空间转换均以闪回/结束闪回标识，不混成同一物理空间。",
      "fix_instruction": "若闪回标识缺失，应在场景和镜头描述中明确闪回蒙太奇及回到现实。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "爸爸对幼年天天说道“想爸爸的时候就吹，爸爸听得到”，现场说话对象明确；天天看全家福没有新增台词。",
      "fix_instruction": "若出现自语或旁白，应注明声音来源和口型状态。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、官方占位符、参考图说明或视频模型工程词，尾部只保留短剧风格和负向约束。",
      "fix_instruction": "若出现模板或工程说明，应删除并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
