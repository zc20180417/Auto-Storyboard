{
  "pass": true,
  "summary": "seg01两组均保留朱文浩接掌集团、李副总表态和城南项目任命苏清寒的原剧情，格式、空间锁定和台词节奏通过。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "6-10秒承载朱文浩两句台词，有效字数18字，4秒约4.5字/秒，且包含落座后环视众高管的原动作，未超过7字/秒。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留高管面面相觑、李副总擦汗表态、朱文浩翻开文件宣布城南项目、看向苏清寒任命负责的全部剧情节点。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "本组始终在集团最高会议室内，组首列出朱文浩、苏清寒、李副总、众高管的位置和朝向，没有跨物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首明确朱文浩位于画面左侧入口旁，苏清寒和众高管分坐会议桌两侧，朱文浩行动和发言前均有可生成位置。",
      "fix_instruction": "无须修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾朱文浩坐在董事长主位看向众高管，第2组首延续他坐在主位、众高管仍在会议桌两侧的状态。",
      "fix_instruction": "无须修复。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "李副总11字台词用2秒约5.5字/秒；朱文浩宣布城南项目并任命苏清寒共18字用4秒约4.5字/秒，同步翻文件和转向苏清寒，节奏达标。",
      "fix_instruction": "无须修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
