# Seedance 2.5 横屏仙侠真实探针协议

本 runbook 定义《丹道仙途》三个 `single` 探针在获得真实 CPA/ManJuWeb 授权后如何提交、留证、审核和晋级。它是 Unit 7 的操作合同，不是模型调用客户端；Auto-Storyboard 只生成经过哈希绑定的 package、接收脱敏回写并执行证据校验，ManJuWeb/VideoService 负责认证提交、轮询和结果持久化。

## 当前门槛

在以下证据全部齐备前，保持 `submit_allowed=false`，不得付费提交：

- ManJuWeb consumer contract、认证 transport、anti-replay/nonce 和 preflight fixture 已由双方确认；
- 目标 Ark 账号已开通 `doubao-seedance-2-5-260628`，区域为 `cn-beijing`，配额和本批次预算已预注册；
- 方平、元鼎、服装、炼丹室和关键状态图片具有明确使用权，且在 ManJuWeb 中为 `Active`；
- 三集 worker 已分别完成 generator → reviewer → 修复/复审 → episode validate → asset extractor → asset reviewer → 资产 validate；
- 每个目标 cut 的 v2 package 通过 `workflow-status`，至少一项真实 reference content 已按 package 顺序序列化；
- 受控存储、访问角色、`retention_until`、删除责任和人工 `probe_signer` 已登记。

离线 fixture、模拟 attempt 或 provider 文档不能替代上述外部证据，也不能被描述成视频效果验证。

## 三个独立探针

| 类别 | 完整 episode | 目标 cut | 必须观察 |
| --- | --- | --- | --- |
| `ordinary-alchemy` | EP005 | 场5-5 | 元鼎一人高；投药后再入山泉；灵火贴鼎；禁制稳定；药液由清转浊 |
| `failed-alchemy-rewind` | EP003 | 场3-3 | 焦渣先稳定；银光由鼎壁/鼎纹触发；焦渣、药液、药材按可追踪逆过程恢复；鼎外边界不被改写；银光收束 |
| `yuanding-ability-reveal` | EP028 | 场28-2 | 鼎纹逐段点亮；材质/结构/尺度不漂移；银光增强仍局限鼎内；能力范围不擅自扩大 |

每个探针都使用自己的完整 episode 和 attempt 目录，不把三段拼成一个 episode，不共享可变的 prompt、素材或结果文件。

## 提交与持久化

1. 由 run owner 创建本批次，预注册每类最大 attempts、总预算、超时和停止条件；看到结果后不得扩大原批次预算。
2. ManJuWeb 接收 v2 package，透传 `16:9`、`720p`、整数 `4–30` 秒、`generate_audio=true` 和 `omni_reference_task_type=reference`。创建 body 不发送 `fps` 或内部 `multimodal_generation`。
3. ManJuWeb 以认证 transport 提交并记录脱敏 request/response digest、nonce、task ID、账号 pseudonym、region、deployment/contract ID 和有效期。
4. provider 完成后，ManJuWeb 在临时 URL 过期前安全下载到受控存储。只回写 `controlled://` locator、媒体 SHA-256、字节数、MIME、下载时间和 task/environment 绑定；真实签名 URL、cookie、原始抓包和内部 host 不进入仓库。
5. 下载器只接受 HTTPS 和明确 provider/object-storage allowlist，限制重定向、超时、最大字节数，并拒绝环回/内网/链路本地地址；下载后先做 magic/container/size 检查，再在资源受限隔离进程解析媒体 metadata。

## attempt 生命周期

合法状态链为：

```text
prepared → submitted → provider_running → download_pending
  → semantic_qa_pending → signoff_pending → accepted
```

提交或外部证据有 blocker 时进入 `submit_blocked`，修复后回到 `prepared`。provider、机械 QA、语义 QA 或签收失败分别进入对应终止状态；重试必须创建新的 `attempt-02`、`attempt-03`，不能覆盖历史 attempt。`accepted` 之后若依赖、素材、请求、结果或真实性绑定漂移，只能标记 `stale`，不能回写旧结论。

每次状态变更都要记录 `from`、`to`、actor id/role 和带时区时间。校验器会拒绝非法跳转和越权 actor。

## QA 与签收

机械 QA 必须证明：可解码、`1280×720`、`16:9`、`4–30` 秒、`24 fps`、存在音轨。`fps=24` 只验收结果，不是创建字段。

结构化 semantic QA 的每个 required check 只能是 `pass`、`fail` 或 `not_reviewable`，并包含时间段/帧范围、直接观察、判定阈值、相关素材 ID/hash、rubric 版本、reviewer 身份/角色和时间。必检项覆盖：

- 方平脸型和元鼎结构/尺度稳定；
- PBR 写实材质、手绘纹理、低饱和东方色盘和克制轮廓在运动中不退化；
- 横屏动作、轴线、对话对象与口型；
- 炼丹或回溯的完整状态链；
- 炉火/鼎内/回溯声源与峰值同画面动作，无现代 UI 音或无来源法术声。

任一 required 项为 `fail` 或 `not_reviewable`，attempt 不得 `accepted`。`probe_reviewer` 完成逐项审核；具有 `probe_signer` 角色的人类签收人记录接受/拒绝、授权来源、时间和 rubric 版本。

三类单项都通过后，还要由同一 `probe_signer` 完成跨探针并排复核：方平脸型、元鼎模型、PBR+手绘材质、克制轮廓和低饱和东方色盘。

## promotion 与对外结论

每个 category manifest 同时记录单调递增的 `latest_attempt_id` 和 run owner 显式选择的 `promoted_attempt_id`。`latest` 只代表最高编号，不代表通过；失败的较新 attempt 不会自动替换已 promotion 的 accepted attempt。只有当前依赖、package、provider contract、ManJuWeb schema、真实性证据和 QA 全部一致的 accepted attempt 才能被 promotion。

三个 category 都有有效 promoted attempt，且跨探针签收通过时，才可写：

> 在预注册预算内各取得一个合格样本，验证范围为 `dandao-xiantu/alchemy`；不声明统计稳定率或跨项目复用。

否则统一写：

> 合同原型完成，视频工作流未验证。

历史 accepted attempt 的环境快照必须保留；preflight 默认 24 小时有效，过期或 deployment/account/region 改变只会让当前提交 readiness 失效，并要求重跑探测，不会抹掉历史事实。所有媒体和授权材料按分类留存，达到 `retention_until` 后由 deletion owner 安全删除并保留 deletion receipt。
