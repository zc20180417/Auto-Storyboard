{
  "pass": true,
  "summary": "seg02已对照原剧本、横屏空间和新运镜规则审核，云宝喷水、泥水结冰、胡永贵摔倒及天天接水均闭环，无hard issue。",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
      "group": "第4组",
      "type": "character_availability",
      "evidence": "云宝明确在水壶内部特写中出现，胡永贵在右后景作为外部威胁，不存在人物来源混乱。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "泥水从皮卡右侧流向中央并结成薄冰，胡永贵踩冰摔倒后水管从右侧滑到中央偏左，过渡可见。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "天天最后一句“走！我们回家！”放在2.5秒中景内，短句兴奋语速合理。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定天天左前景、胡永贵右后景、泥水从右向左流，水壶内外空间清楚。",
      "fix_instruction": "若改稿，不要让云宝出现在水壶外部空间。"
    },
    {
      "group": "第5组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "每段运镜说明低位固定、轻推和后拉的目标，均服务泥水改向、薄冰位置和水管脱手。",
      "fix_instruction": "若调整运动镜头，需继续说明起点终点和揭示目标。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾水管滑到天天右前方，第6组首天天视线锁住水管并扑过去，组间衔接一致。",
      "fix_instruction": "若后续压缩，保留水管落点和天天扑管动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
