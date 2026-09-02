# Seedance 2.5 横屏仙侠操作状态

更新时间：2026-09-01

## 当前最高已证实层级

合同原型完成，视频工作流未验证。

本地已完成：

- 横屏仙侠 3D CG profile、命名画风 preset 和《丹道仙途》显式项目包；
- 4–30 秒整数时长、16:9、720p、原生音频与 provider reference 映射；
- 分镜/资产 resolved workflow identity 与 stale hash 链；
- v2 provider request serializer；
- 五层 readiness 与统一机器/人读状态输出。

尚未完成：

- 真实 CPA/ManJuWeb 测试账号和目标模型启用证明；
- ManJuWeb 认可的脱敏 consumer fixtures；
- 认证 transport、nonce/digest/environment/time-window 防重放证据；
- 有明确权利的实际人物/元鼎/场景参考素材；
- EP005、EP003、EP028 三条真实视频及机械/语义 QA 和签收。

因此当前所有横屏 v2 生成包即使 `generation_ready=true`，仍必须为 `submit_allowed=false`。

## 操作顺序

1. 使用 `prepare-agent-dandao-xiantu.ps1` 创建 `single` 横屏工作区。
2. 按 dispatcher/worker 约束完成单集 generator → reviewer → 局部修复 → 复审 → episode validate。
3. 建立引用项目事实源的 `asset_bible.md`，逐集完成 asset extractor → asset reviewer → 修复/复审。
4. 转换资产并运行 `validate-assets.mjs`，确认生成当前 `asset_validation.json`。
5. 导出 v2 requirements/local materials，准备实际授权素材并由 ManJuWeb 回写 Ark 结果。
6. 导出 package；每集运行 `python .\storyboard_agent_workspace.py workflow-status --episode-dir <episode-dir>`，写出当前本地 readiness。
7. 三集证据齐备后运行 `python .\storyboard_agent_workspace.py workflow-status --run-dir <run-dir>`，聚合 EP003/EP005/EP028 的当前 readiness 与探针证据。缺可信 ManJuWeb authenticity verifier 时该命令按设计返回非零并保持 `workflow_validated=false`。
8. Unit 7 离线探针协议已完成；只有 Unit 1B/6B 外部门禁、本批次预注册预算/角色/素材权利和每个 cut 的 `submit_allowed=true` 都满足后，才能进入 Unit 8 真实提交。

## 当前首要 blocker

Owner：用户/ManJuWeb/CPA 环境负责人。

Next action：提供测试环境、非敏感账号启用证明、最小授权图片和 ManJuWeb 认可的脱敏 consumer/preflight fixtures。不要把密钥、cookie、签名 URL、真实账号 ID 或原始抓包放进仓库或普通 run。
