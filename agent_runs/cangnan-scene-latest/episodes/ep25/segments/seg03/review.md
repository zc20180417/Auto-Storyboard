{
    "pass":  true,
    "summary":  "已对照25-3审讯揭示脚本审核，问话、威胁、压迫、龙天傲、金矿和战略级稀土信息均按顺序保留，无硬问题。",
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
                            "evidence":  "陆凡“谁派你来的？”、黑曼巴公司身份和威胁、陆凡“废话太多。”均未删改。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "script_fidelity",
                            "evidence":  "黑曼巴崩溃供出“京城龙少！龙天傲！”及“战略级稀土”信息，陆凡关于龙家的反应和“走。”保留。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "dialogue_pacing",
                            "evidence":  "第2组最长台词“黑风山下不仅有金矿，还有战略级稀土！”在6-10秒承载，约4.8字/秒，符合节奏硬上限。"
                        }
                    ],
    "semantic_checks":  [
                            {
                                "group":  "第1组",
                                "type":  "prop_continuity",
                                "result":  "pass",
                                "evidence":  "铁扳手从组首抵住肩膀，到11-15秒加力压下，归属和动作连续。",
                                "fix_instruction":  "若不通过，应补扳手位置和加力动作。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "generation_density",
                                "result":  "pass",
                                "evidence":  "第2组为连续逼供问答加末尾制服拖离，信息量较高但每句台词均分段承载，末尾动作独立3秒。",
                                "fix_instruction":  "若不通过，应将拖离交警方另起短组。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "handoff_continuity",
                                "result":  "pass",
                                "evidence":  "第1组尾部黑曼巴被压在栏杆前，第2组组首复述陆凡压制和黑曼巴崩溃状态。",
                                "fix_instruction":  "若不通过，应补栏杆前压制状态。"
                            }
                        ],
    "issues":  [

               ],
    "warnings":  [

                 ]
}
