{
  "pass": true,
  "summary": "第28集分镜稿忠实还原原剧本，台词承载、时间精度、空间连续性和人物可用性均通过审核。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "周美娟台词'不——沈清！你好狠的心啊！'有效字数10字，时间段0-3.5秒（3.5秒），字秒比2.86，属于情绪对白（凄厉惨叫），目标语速5.2字/秒，估算10÷5.2=1.92秒，加拖拽动作（中等动作+2秒）共3.92秒，取整3.5秒可接受。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组和第3组均在法庭内，单一物理空间。组首空间锁定正确排除已退场的周美娟和法警，只保留沈清和周桂兰。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "沈清台词'走，我们回家。回真正属于我们自己的家。'16字完整保留，说话对象周桂兰正确。周桂兰'是啊，结束了。心里的石头总算落了地。'15字完整保留。所有关键动作（拖出、关门、转身、握手、扶起）均忠实还原。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟'凄厉惨叫'为画面内真人开口对白，明确写明'朝沈清方向惨叫'，说话对象清楚，口型正确。法庭大门关闭后声音被隔绝，音画分离合理。",
      "fix_instruction": "无需修改，口型和声音来源正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组9秒，3个强节拍：转身握手、沈清台词、周桂兰台词+反应。强节拍属于同一连续事件链（安慰-回应），每个时间段只承载一个主动作/对话节拍，表演时间充足。",
      "fix_instruction": "无需修改，强节拍密度合理。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾'法庭大门关闭，周美娟和法警已不在场内，沈清和周桂兰并肩站在法庭前景'，第2组组首'法庭内安静下来，周美娟和法警已不在场内'，人物位置和空间状态连续。",
      "fix_instruction": "无需修改，组间状态衔接正确。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "沈清握住周桂兰的手从第2组延续到第3组，组尾'沈清双手握着周桂兰的手'与第3组组首'双手握住周桂兰的手'一致。",
      "fix_instruction": "无需修改，道具归属连续。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第3组2个时间段：0-2秒扶起动作、2-6秒对话，每个时间段只承载一个主动作/对话节拍。非主动作人物无抢戏。",
      "fix_instruction": "无需修改，动作原子性正确。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组提供3个视频禁止项：'周美娟被拖走后仍出现在法庭内、法庭大门自行打开、法警留在法庭内不退场'，均锚定本组人物和场景，无泛泛词。",
      "fix_instruction": "无需修改，视频禁止项具体且锚定正确。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "generation_density",
      "problem": "第2组9秒属于短组（6-9秒区间），包含转身握手+两人对白+情绪反应，理由成立但需确认：转身握手+沈清台词+周桂兰台词+情绪释放属于同一安慰事件链，自然落在9秒。",
      "evidence": "转身握手（2秒）+ 沈清台词10字÷4.5=2.2秒取整2.5秒 + 周桂兰台词15字÷4.5=3.3秒+反应1秒=4.5秒，总计9秒。",
      "fix": "无需修改，短组理由充分。"
    }
  ]
}