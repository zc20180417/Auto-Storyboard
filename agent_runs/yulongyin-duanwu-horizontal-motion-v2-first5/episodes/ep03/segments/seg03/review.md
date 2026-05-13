{
  "pass": true,
  "summary": "seg03已对照原剧本和横屏规则审完，爷爷清明消散、天天退回房间、旧照片与云中君线索均可拍且连续。",
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
      "type": "dialogue_direction",
      "evidence": "第1组天天对爷爷追问，爷爷对天天糊涂回答和反问，说话对象均在画面左右关系中明确。"
    },
    {
      "group": "第2组",
      "type": "blocking_continuity",
      "evidence": "第2组天天从堂屋左侧门框退回自己的房间，爷爷留在右侧堂屋并移动到旧木柜前，左右空间变化有可见路线。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "老照片先在抽屉里露出一角，再被爷爷捧在手中，随后第3组继续由爷爷持有，照片归属无跳变。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留年轻爷爷在龙舟船头举鼓槌、爷爷低语“三十年了……云中君的影子”和照片背后字迹三项关键信息。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "第1组延续天天左、爷爷右的轴线，门槛作为中间隔断，追问和糊涂反问方向清楚。",
      "fix_instruction": "无需修复；若改写堂屋位置，需保留或明确交代换边过渡。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首空间锁定写的是天天在左侧门框旁、爷爷在右中景、旧木柜在右后景的静态结果，没有过程动词。",
      "fix_instruction": "无需修复；后续不要把退回、摸索、拉抽屉等过程动作写进组首。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "固定照片特写、轻推爷爷与照片、摇向照片背面字迹分别服务照片证据、低语口型和关键信息揭示。",
      "fix_instruction": "无需修复；若调整，仍需保持照片正反面的可见证据链。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、官方占位符、首帧尾帧、视频延长、自动分镜或工程说明词，照片背面文字属于剧情道具内容。",
      "fix_instruction": "无需修复；交付稿继续避免任何模型控制台占位词。"
    }
  ],
  "issues": [],
  "warnings": []
}
