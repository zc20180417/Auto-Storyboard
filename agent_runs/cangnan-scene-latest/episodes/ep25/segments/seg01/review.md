{
    "pass":  true,
    "summary":  "已对照25-1追击脚本、竖屏生成规则和段落稿完成审核，麻醉弹、掩体、耳机汇报、扳手冲锋和Z字逼近均保留，无硬问题。",
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
                            "evidence":  "原剧本中麻醉弹擦肩、陆凡躲入报废越野车、黑曼巴耳机汇报“目标移动速度太快，无法锁定”、陆凡说“找到你了”均按顺序保留。"
                        },
                        {
                            "group":  "第1组",
                            "type":  "dialogue_direction",
                            "evidence":  "黑曼巴通过耳机对同伴低声说道，陆凡对塔吊方向低声说道，声音来源和对象清楚。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "generation_density",
                            "evidence":  "第2组只承载抓扳手冲出、黑曼巴连续开火、陆凡Z字逼近三段动作，12秒内动作链可表演。"
                        }
                    ],
    "semantic_checks":  [
                            {
                                "group":  "第1组",
                                "type":  "space_locking",
                                "result":  "pass",
                                "evidence":  "组首明确越野车、碎石坡、塔吊远近关系，陆凡与黑曼巴位置和朝向可生成。",
                                "fix_instruction":  "若不通过，应补足两人位置、朝向和塔吊方位。"
                            },
                            {
                                "group":  "第1组",
                                "type":  "audio_mouth_sync",
                                "result":  "pass",
                                "evidence":  "耳机台词标明黑曼巴通过耳机说话，画面角色口型与声音来源不混淆。",
                                "fix_instruction":  "若不通过，应明确耳机声或画面开口承载。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "handoff_continuity",
                                "result":  "pass",
                                "evidence":  "第1组尾部陆凡仍在越野车掩体后，第2组组首复述该状态并让他抓扳手冲出。",
                                "fix_instruction":  "若不通过，应在组尾或组首补掩体和扳手位置。"
                            }
                        ],
    "issues":  [

               ],
    "warnings":  [

                 ]
}
