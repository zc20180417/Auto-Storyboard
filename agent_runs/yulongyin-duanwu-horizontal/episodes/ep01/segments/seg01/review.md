{
  "pass": true,
  "summary": "seg01五组已对照村口原剧本、横屏生成规则和时间合同完成审核，台词、黑水道具、左右站位和组间衔接均可交付。",
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
      "type": "horizontal_composition",
      "evidence": "村口、水井和干裂河床分别落在画面右侧井台、左侧远处河床和前景空桶，村民甲与村民乙左右分置，横屏关系不是单人居中近景。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "胡永贵两句原台词完整保留，化肥袋、皮卡高位和黑水从袋缝渗出后落向干渠的关键因果都与原剧本一致。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "爷爷“端午不能断水！龙舟必须下水！”约15字用3秒承载，胡永贵嘲笑约20字用4秒承载，爷爷第二句约22字用5秒承载，均低于6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "evidence": "村民甲明确对天天和周围村民说，天天明确对爷爷说，爷爷明确对天天说，没有把现场对白写成自语或假对象。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "黑水从第2组化肥袋缝隙渗出，第5组沿皮卡下方干渠由右向左流向河床，来源、位置和流向连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定交代村口外、井口、干裂河床、村民甲乙和空桶的左中右及前后景位置。",
      "fix_instruction": "若不通过，应补充井口、河床、空桶和两名村民的画面方位。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爷爷始终在画面左/中央偏左仰看右侧高位胡永贵，胡永贵保持右侧车厢高位俯视，视线轴线稳定。",
      "fix_instruction": "若不通过，应在组尾或下一组组首补充换边过渡或保持左右位置。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内只承载村民催促、天天拉爷爷、爷爷挣扎三段强节拍，没有叠加外部事件或关键道具揭示。",
      "fix_instruction": "若不通过，应拆出爷爷挣扎或压缩无关人群反应。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾天天拉爷爷向左退，第5组首延续两人从中央偏左退出，胡永贵仍在右侧皮卡车厢，人物位置衔接一致。",
      "fix_instruction": "若不通过，应补充天天拉爷爷离开人群的中间走位。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、视频延长、自动分镜等工程词，负向词仅把竖屏构图作为排除项。",
      "fix_instruction": "若出现工程词，应删除并改成可见动作、道具或声音描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
