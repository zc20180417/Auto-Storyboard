---
name: dandao-xiantu
description: Apply the explicit Dan Dao Xian Tu project overlay for its characters, alchemy, spirit fire, pills, Yuanding visual states, and bounded rewind rules.
---

# 《丹道仙途》项目包

本包默认关闭。只有 run 元数据明确写入 `project_pack_id=dandao-xiantu` 时才能读取和使用；剧名、人物名或剧情相似都不能自动启用。

## 启用合同

- 兼容 profile：`seedance-2.5-horizontal-xianxia-3d-cg`
- 首期：`single + horizontal + 3d-cg + 720p`
- 固定画风：`realistic-material-restrained-anime-outline`
- 版本：1

启动时完整读取：

1. `pack.json`
2. `references/alchemy-system.md`
3. `references/yuanding-visual-bible.md`

生成器、审核器和资产 worker 必须使用同一版本与 hash，不得各自重写元鼎外观或回溯能力。

## 首期范围

- 方平的炼丹流程、灵火控制、丹药成形与品质反馈。
- 元鼎的实体视觉、尺度/材质/结构、常态/回溯/复苏状态。
- 元鼎对炼丹结果的有界回溯，以及鼎外结果固定边界。
- 首期不为法器战斗、符箓、阵法和遁光追加本剧专属扩展；这些仍按通用仙侠 VFX 语法和当集剧本执行。

## 禁止推断

- 不把项目词或元鼎规则迁移到未启用本包的 run。
- 不因为“宝鼎”“炼丹”“回溯”等通用词就推断元鼎、方平、落阳宗或每日九次。
- 不扩展剧本未建立的元鼎能力、作用对象、回溯范围、每日次数、品阶或复苏结果。
- 项目包只补充事实，不能覆盖原剧本当前集的先后顺序、人物认知和揭示时点。
