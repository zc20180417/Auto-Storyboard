{
  "pass": true,
  "summary": "seg01已对照剧本、生成规则和当前分镜逐组审核，医院报复与工厂反击信息完整，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "李少爷“废了我的手！我要她全家死！”放在2.5-7.5秒，约12个有效字/5秒；保镖“少爷，顾家倒了，咱们在省城没人了。”放在7.5-12秒，约16个有效字/4.5秒，均低于6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "本组始终在罐头厂办公室内，赵朵朵坐桌内侧、赵大雷在桌旁、物流经理在桌前，退货单从经理手中到桌面，空间和人物可用性清楚。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "保留赵大雷外省订单违约的焦急、赵朵朵识破京城关系施压、从顾家账本证据转到U盘并交给大哥寄京城纪委的因果链。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "李少爷对保镖下令，医生在床尾可见后对李少爷说明伤情，所有现场台词都有明确可见对象和口型承载。",
      "fix_instruction": "若不通过，应把无来源声音改成现场可见人物开口，或补充门外音、电话音等载体。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有踹倒医生和怒吼复仇两个强节拍，4秒完成跌倒动作，6秒承载长句台词和医生后缩反应，未压缩到不可表演。",
      "fix_instruction": "若不通过，应拆出踹倒动作或延长动作段，并删去无关反应。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "U盘从赵朵朵抽屉中取出，先放到退货单旁，再递到赵大雷手里，道具归属和转移动作连续。",
      "fix_instruction": "若不通过，应补充U盘从桌面到赵大雷手中的可见递交动作。"
    },
    {
      "group": "第1组至第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未写入模板编号、控制台占位符、广告语或视频工程说明，画面描述均围绕剧本人物、道具和空间。",
      "fix_instruction": "若不通过，应删除污染词并改为自然短剧分镜描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
