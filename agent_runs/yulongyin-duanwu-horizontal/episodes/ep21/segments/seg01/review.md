{
  "pass": true,
  "summary": "第1组胡永贵带人压到村头广场已按原剧本、横屏调度、台词节奏和可生成性完成审核，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留胡永贵两句原台词、村民乙维护李燃的原台词、村民举锄头反抗和被黑市打手打倒的动作顺序。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "右侧刀疤男和打手阵线压住左侧村民，胡永贵从右后方走到偏右前景，广场阵营关系适合16:9横向呈现。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-5秒承载“没想到吧！我又回来了！”约10字/3秒，5-9秒承载“李燃那个残废在哪……”约25字/4秒，均未超过硬上限；全组15秒5镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "胡永贵对左侧村民喊话，村民乙反向对右侧胡永贵回应，现场对话对象清楚。",
      "fix_instruction": "已通过；若后续修改台词，保持说话对象和声音来源明确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定右前景越野车、右侧打手阵线、左侧村民和锄头，关键人物均可见。",
      "fix_instruction": "已通过；若后续改镜头，保留组首左右、前后景和关键道具位置。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图占位、视频延长、自动分镜等工程说明词；负向词仅用于排除竖屏构图。",
      "fix_instruction": "已通过；不要加入模型模板说明或控制台占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
