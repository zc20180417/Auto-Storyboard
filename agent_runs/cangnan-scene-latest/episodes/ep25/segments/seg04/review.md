{
    "pass":  true,
    "summary":  "已对照25-4项目部威逼脚本审核，文件砸桌、一元收购、龙家背书、保镖围住、父母医院威胁和江若晴反骂均保留，无硬问题。",
    "checked_groups":  [
                           "第1组",
                           "第2组"
                       ],
    "audit_coverage":  {
                           "script_fidelity":  "checked",
                           "dialogue_direction":  "checked",
                           "timing_math":  "checked",
                           "dialogue_pacing":  "checked",
                           "space_locking":  "checked",
                           "format":  "checked",
                           "character_availability":  "checked",
                           "handoff_continuity":  "checked",
                           "filmability":  "checked",
                           "audio_mouth_sync":  "checked",
                           "generation_density":  "checked",
                           "prompt_pollution":  "checked"
                       },
    "spot_checks":  [
                        {
                            "group":  "第1组",
                            "type":  "script_fidelity",
                            "evidence":  "金董“签字吧江总...”与江若晴“一元收购...”及龙家台词按原顺序出现。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "character_availability",
                            "evidence":  "保镖在组首已位于背景门口和江若晴身后两侧，随后围住江若晴可用。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "dialogue_direction",
                            "evidence":  "金董两句医院威胁均写成对江若晴说道，江若晴反骂写成对金董说道，无假对象。"
                        }
                    ],
    "semantic_checks":  [
                            {
                                "group":  "第1组",
                                "type":  "prop_continuity",
                                "result":  "pass",
                                "evidence":  "收购文件从金董手边砸到办公桌并摊开，后续成为第2组签字笔旁的核心道具。",
                                "fix_instruction":  "若不通过，应补文件落点和桌面状态。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "generation_density",
                                "result":  "pass",
                                "evidence":  "第2组围住、两句威胁、江若晴反骂分成4段，15秒内强节拍清楚。",
                                "fix_instruction":  "若不通过，应拆出医院威胁或保镖围困。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "audio_mouth_sync",
                                "result":  "pass",
                                "evidence":  "全部为现场会议室内真人对白，均有明确说话人与对象。",
                                "fix_instruction":  "若不通过，应改正对白对象。"
                            }
                        ],
    "issues":  [

               ],
    "warnings":  [

                 ]
}
