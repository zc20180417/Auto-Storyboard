{
    "pass":  true,
    "summary":  "已对照25-2塔吊攀爬脚本审核，两组保留黑曼巴惊恐、金属攀爬声、陆凡攀爬、射击、踢飞手枪和扳手压制，无硬问题。",
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
                            "evidence":  "黑曼巴台词“这不可能！他速度怎么这么快！”、“别想上来！”及陆凡徒手攀爬均保留。"
                        },
                        {
                            "group":  "第1组",
                            "type":  "space_locking",
                            "evidence":  "组首将黑曼巴放在塔吊操作台边、陆凡放在下方钢架底部，单一物理空间清楚。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "prop_continuity",
                            "evidence":  "麻醉手枪先在黑曼巴手中，陆凡踢飞后滑向角落，随后陆凡用铁扳手压制黑曼巴，道具归属连续。"
                        }
                    ],
    "semantic_checks":  [
                            {
                                "group":  "第1组",
                                "type":  "dialogue_pacing",
                                "result":  "pass",
                                "evidence":  "0-3秒承载黑曼巴13字惊恐台词并同步调整瞄准镜，字秒比约4.3，未超过硬上限。",
                                "fix_instruction":  "若不通过，应延长或拆分惊恐台词。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "generation_density",
                                "result":  "pass",
                                "evidence":  "第2组三段动作分别为射击闪避、跃起踢枪、落台压制，12秒内没有叠加长对白。",
                                "fix_instruction":  "若不通过，应拆开踢枪和落台压制。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "handoff_continuity",
                                "result":  "pass",
                                "evidence":  "第1组尾部黑曼巴持枪向下，陆凡仍在钢架上；第2组组首复述枪口向下和陆凡在钢架边缘。",
                                "fix_instruction":  "若不通过，应补枪口方向和陆凡位置。"
                            }
                        ],
    "issues":  [

               ],
    "warnings":  [

                 ]
}
