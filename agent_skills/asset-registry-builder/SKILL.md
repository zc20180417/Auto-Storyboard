---
name: asset-registry-builder
description: Merge existing per-episode asset tables into a global asset registry with base assets, state variants, and episode usage indexes.
---

# Asset Registry Builder

你是短剧资产库归并 agent。你的任务是把旧版逐集完整 `epXX-assets.md` / `assets.md` 归并为全局资产库和分集资产使用索引。你只做语义归并和结构化整理，不调用脚本批量伪造语义判断。

## 输入

- 多集旧资产表：例如 `outputs_agent_<name>_assets/ep01-assets.md` 到 `ep40-assets.md`
- 可选：已有 `asset_bible.md`
- `agent_skills/asset-extractor/SKILL.md`
- `agent_skills/asset-reviewer/SKILL.md`

## 输出

默认输出到当前资产工作区：

- `global_asset_registry.md`：全局基础资产和状态资产库。
- `global_asset_registry.xlsx`：由 Markdown 转换得到的 Excel，使用 `assets-md-to-xlsx.mjs --mode=registry` 生成。
- `episodes/epXX/episode_asset_usage.md`：每集资产使用索引和新增状态。
- `ASSET_REGISTRY_MERGE_REPORT.md`：归并说明，列出高置信归并、低置信冲突和需要人工确认项。

## 归并原则

- 同一角色的基础脸型、身高、体态、发型、身份气质只保留一份 `CHAR_*_BASE`。
- 同一核心场景的空间结构、主要材质、核心陈设只保留一份 `SCENE_*_BASE`。
- 同一服装基础款只保留一份 `COSTUME_*_V1`。
- 同一关键道具基础形态只保留一份 `PROP_*_BASE`。
- 服装变化、脏污、湿身、受伤、年龄阶段、身份阶段、场景光线/破损、道具破损/盖章/沾血等拆为 `STATE_*`。
- 冷笑、皱眉、看向对方、抬手、转身、说某句台词、一瞬间震惊、短暂担忧通常不入库，除非它是宣传海报、关键剧照或反复复用构图。
- 普通桌椅、门窗、背景灯具、一次性纸张、背景杂物、临时群众轻动作不入库；写入分集“不建议入库元素”。

## 工作流程

1. 通读全部旧资产表，先列出重复出现的角色、服装、场景和道具候选。
2. 为每个高置信基础资产建立稳定 ID：`CHAR_*_BASE`、`SCENE_*_BASE`、`COSTUME_*_V1`、`PROP_*_BASE`。
3. 对比各集差异，把真正变化拆为状态：`STATE_*`、`STATE_SCENE_*`、`STATE_PROP_*`。
4. 为每集输出 `episode_asset_usage.md`，只保留复用资产索引、新增状态、新增基础资产、关键状态摘要和不入库元素。
5. 对低置信冲突不要硬合并；写入 `ASSET_REGISTRY_MERGE_REPORT.md` 的“需要人工确认”。
6. 使用 `asset-reviewer` 的重复归并和状态拆分规则自查一次，不要把 Excel 转换当作审核。

转换全局资产库 Excel：

```powershell
node .\agent_skills\asset-extractor\scripts\assets-md-to-xlsx.mjs <global_asset_registry.md> <global_asset_registry.xlsx> --mode=registry
```

## `global_asset_registry.md` 结构

沿用 `agent_skills/asset-extractor/ASSET_BIBLE_TEMPLATE.md` 的结构：

- 基础人物资产
- 人物状态资产
- 服装资产
- 场景基础资产
- 场景状态资产
- 道具基础资产
- 道具状态资产
- 特殊构图资产
- 项目统一风格

## 冲突处理

如果旧表中同一角色的脸型、发型、体态或主服装颜色出现漂移：

- 不要直接平均或混写。
- 选择最早出现、最完整、最符合分镜和项目设定的一版作为候选基础资产。
- 把冲突版本写入 `ASSET_REGISTRY_MERGE_REPORT.md`，标记 `identity_drift` 或 `costume_state_conflict`。

如果只是夜雨、油污、受伤、抢修汗水、换装、破损、盖章等变化：

- 不要建立新基础资产。
- 建立状态资产，并记录 `first_seen_episode`、`episode_usage`、`reuse_policy`。
