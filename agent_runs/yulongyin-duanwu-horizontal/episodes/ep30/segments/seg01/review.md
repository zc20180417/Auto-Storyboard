{
  "pass": true,
  "summary": "seg01保留龙舟下水、爷爷喊话、村民欢呼和祭酒动作，横屏空间与时间格式可交付。",
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
      "evidence": "第1组把河道放在中线，左岸村民和彩旗、右岸高台爷爷、前景龙舟形成清楚的16:9左右与前后层次。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "爷爷台词“吉时已到！龙舟下水！”安排在2-5秒，约10字/3秒，配合抬手示意和人群反应，节奏可表演。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留爷爷穿新唐装、站高台、将清酒洒入河中祭奠水脉与神龙，没有新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爷爷始终在右侧高台面向左侧河道，龙舟从右前景入水后停在近岸，视线方向连续。",
      "fix_instruction": "若不通过，应补充爷爷或龙舟换位的可见过渡。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "清酒碗从爷爷双手捧持到酒线入河再到空碗收回，归属和位置连续。",
      "fix_instruction": "若不通过，应补充酒碗拿起、倾倒或收回的动作。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内承载建立场面、爷爷喊话、村民欢呼、龙舟下水四个短节拍，没有长台词和复杂跨空间动作。",
      "fix_instruction": "若不通过，应拆分欢呼或下水动作，避免同镜头堆叠。"
    }
  ],
  "issues": [],
  "warnings": []
}
