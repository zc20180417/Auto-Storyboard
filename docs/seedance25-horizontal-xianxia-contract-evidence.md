# Seedance 2.5 横屏仙侠合同证据

证据快照日期：2026-09-01

## 结论

本地实现可以据此冻结 `seedance-2.5-horizontal-xianxia-3d-cg` 的 Unit 1A 合同：

- 模型为 `doubao-seedance-2-5-260628`
- 创建端点为 `POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks`
- 横屏使用 `16:9`
- 首期产品只启用 `720p`，对应 `1280×720`
- 每条视频显式使用 `4`–`30` 整数秒，不启用 provider 的 `-1` 自动时长
- 使用 `generate_audio=true` 生成原生音频
- 每个 cut 至少序列化一项图片、视频或音频 reference
- 内部 `multimodal_generation` 必须映射为 reference content 与 `omni_reference_task_type=reference`
- 24 fps 是输出响应/下载媒体的验收条件，不是创建请求字段

官方文档还列出了 480p 与 1080p，但这不表示本 profile 首期开放这些分辨率。首期只启用 720p，后续开放需要单独的产品决定、请求测试和回归验证。

## Unit 1A 与 Unit 1B

### Unit 1A：本地可复现合同

以下工件互相校验：

- `tests/fixtures/seedance25/provider-contract-reference.json`
- `tests/test_seedance25_provider_contract.py`
- `agent_skills/seedance-2-5-horizontal-xianxia-3d-cg/references/model-contract.md`

它们可以证明本地 profile、serializer 和 tests 应该实现什么，但不能证明目标账号或 CPA/ManJuWeb transport 已经可用。

### Unit 1B：真实账号/中转门禁

在声称双方已集成或设置 `submit_allowed=true` 前，还必须使用目标测试账号与一项有权使用的最小图片 reference 做经过授权的真实 preflight，并记录：

- 环境、region、模型与消费者合同版本
- 一次性 nonce、请求 digest、task ID、时间窗
- 关键字段是否被 CPA/ManJuWeb 正确透传
- 经过字段清洗的结构证据和验证结果

完整原始抓包不得进入仓库或普通 run。仓库 fixture 必须去除 Authorization、cookie、签名参数、临时下载 URL、内部主机名、真实账号/素材 ID，并通过 secret scan。未完成 Unit 1B 时，可以继续实现本地 profile、skills、资产和 v2 schema，但不能声称 ManJuWeb 已集成，且 `submit_allowed=false`。

## 官方来源

- Seedance 2.5 教程：https://docs.volcengine.com/docs/82379/2607688
- 创建任务 API：https://docs.volcengine.com/docs/82379/1520757
- 视频生成指南：https://docs.volcengine.com/docs/82379/2298881
- 模型开通与生命周期：https://docs.volcengine.com/docs/82379/2637911

截至快照日期，相关页面仍列出 Seedance 2.5，未发现 sunset/deprecation 公告。该观察不替代提交前的时效性 preflight。
