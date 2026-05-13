{
  "pass": true,
  "summary": "seg01 已对照原剧本、HappyHorse 外壳和 storyboard-generator 规则完成审核，6 组均保留关键台词、动作、道具和声音来源，无硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "evidence": "原剧本中林跃被绑、赵百川和赵大强指控、林建国和张桂兰求情、林跃睁眼及 OS 均被保留；OS 写在【音频】第四段并注明林跃闭口不做口型。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "本组承载林跃锁定李二狗、走近、询问鞋码、抓脚踝展示红泥鞋底四个连续动作阶段，14秒分为4段，动作链完整且未新增剧情。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组单独锁定村头水渠边，王四、铁阀门和通往林家果园的水渠位置明确；赵百川只以内心旁白出现，未被写成水渠边现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "林跃、赵百川的现场对白均在【音频】第三段写明说话对象；【运动】只写嘴唇开合、指向剪断电线和对峙动作，没有重复完整台词。",
      "fix_instruction": "无需修复；若后续改写，应继续把完整台词留在【音频】并保持口型对象明确。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "林跃两句质问、赵大强反驳和林跃低语分散到3段音频，画面动作分别承载展示鞋底、人群反应、逼近赵大强，总时长13秒，节奏可表演。",
      "fix_instruction": "无需修复；如要压缩，不能删去红泥质问和赵大强色厉内荏反应。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组林跃压迫赵大强后，第5组让林跃回到父母身边扶住张桂兰，赵百川在同一晒谷场以眼色示意王四，王四退出后自然接第6组水渠边动作。",
      "fix_instruction": "无需修复；若补写，应避免让王四在未退场前直接出现在水渠。"
    }
  ],
  "issues": [],
  "warnings": []
}
