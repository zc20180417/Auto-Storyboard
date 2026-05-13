{
  "pass": true,
  "summary": "seg06 保留陆凡高效录入、张强震惊、改派敬老院和陆凡跟上的剧情，时长节奏合格。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留陆凡敲键盘、数据页面滚动、张强晃来嘲讽、“早就做完了”和屏幕展示完成数据。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留“就这点事，很难吗”“算你有点真本事”“即刻去敬老院”“凭什么去那”“凭我是副主任！我说了算！”等关键台词。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾电脑屏幕转向张强并显示完成列表，第2组首继续锁定屏幕停在完成数据页面。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第1组各对白时间段均在2.5-3秒，字秒比未超过6.5硬上限。",
      "fix_instruction": "若不通过，应拆分张强震惊台词或延长对应段。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "改派敬老院的对话和张强转身、陆凡跟上被分为4段，13秒内清楚可表演。",
      "fix_instruction": "若不通过，应拆出离开动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明陆凡坐在桌前、张强站在桌边、电脑显示完成页面，人物和道具可用。",
      "fix_instruction": "若不通过，应补充桌前位置和电脑屏幕状态。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、参考模板、占位符或字幕指令。",
      "fix_instruction": "若不通过，应删除工程污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
