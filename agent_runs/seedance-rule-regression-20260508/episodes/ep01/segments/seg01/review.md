{
  "pass": true,
  "summary": "已按 storyboard-reviewer 对 seg01 草稿逐组核对原剧本、时长、对话对象、空间锁定、音画分离和提示词洁净度，未发现 hard issues。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组"
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
      "type": "script_fidelity",
      "evidence": "原剧本中赵百川怒斥、赵大强嚣张、林建国嘶吼、张桂兰哭喊四句台词均保留原文和顺序，画面也保留林跃被绑木桩、父母被村民拦在外围的状态。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组 6.5-10秒承载“赵村长，你说人赃俱获，赃物在哪？”，3.5秒内约16个有效字；10-12.5秒承载“剪断的电线就是赃物！”，2.5秒内约10个有效字；12.5-15秒承载短句“那人呢？”，均未超过字秒比硬上限。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "evidence": "赵百川的 OS 被写成内心旁白，画面明确只有王四和水渠，且王四嘴唇闭合不做口型，未把心声误写成现场开口对白。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "第7组只发生在晒谷场人群边，王四在组首位于人群缝隙里，先接收赵百川眼色再退出人群，未在同组切到水渠物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林跃 OS 写为内心旁白，并注明嘴唇闭合不做口型，画面只表现眼神从迷茫到锐利。",
      "fix_instruction": "无需修复；若后续改动，应继续保持 OS 与现场开口分离。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "李二狗在组首空间锁定中已站在赵大强身边稍后位置，之后林跃锁定、逼近和问鞋码都有明确可见对象。",
      "fix_instruction": "无需修复；不要把李二狗写成未入场却直接参与对话。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组只承载抓脚踝展示鞋底、两句红泥质问和村民反应，13秒内强节拍清晰，没有额外加入外部事件或跨空间动作。",
      "fix_instruction": "无需修复；若增加动作，应优先拆组而不是压缩现有证据展示。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组结尾林跃压住赵大强气势后，第7组开头林跃转身走到父母身边并扶住张桂兰，人物移动有可见过渡；王四在第7组尾离开，为第8组水渠边动作铺垫。",
      "fix_instruction": "无需修复；保持王四从晒谷场到水渠的组间过渡。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、官方模板说明、@图片/@视频/@音频、首尾帧参考、视频延长或自动分镜等工程词，只保留自然画面描述。",
      "fix_instruction": "无需修复；后续不要加入任何模型模板或参考图占位语。"
    }
  ],
  "issues": [],
  "warnings": []
}
