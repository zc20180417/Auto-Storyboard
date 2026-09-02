# Seedance 2.5 素材交接合同 v2

## 范围

v2 只服务 `seedance-2.5-horizontal-xianxia-3d-cg`。它把经 hash 保护的横屏分镜/资产身份、逻辑素材、实际文件和 ManJuWeb Ark 回写编译为 provider reference 请求草稿。

v2 是本地合同，不是提交凭证。当前 Unit 6A 没有 ManJuWeb 认可的 consumer fixture、认证 transport、目标账号 preflight 或防重放证据，因此即使每个 cut 已有 Active reference，仍固定 `submit_allowed=false`。

真人竖屏继续使用 [v1](seedance-material-handoff-v1.md)，其 `referenceImageSlots`、9:16 和现有 package schema 不迁移。

## 输入链

```text
final.txt
  -> storyboard_index.json schema v2 + workflow_identity
  -> asset_bindings.json + asset_evidence
  -> seedance_material_requirements.json schema v2
  +  seedance_local_materials.json schema v2
  -> ManJuWeb Ark sync
  -> ark_sync_results.json schema v2
  -> seedance_generation_package.json schema v2
  +  seedance_submission_prompts.md（人读镜像）
```

`storyboard_index.json`、bindings/status 的身份与失效规则见 [Resolved Workflow Identity Contract](resolved-workflow-identity-contract.md)。

## 逻辑需求

`seedance_material_requirements.json` 由程序编译，禁止手写：

```json
{
  "schema_version": 2,
  "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
  "project": "丹道仙途",
  "episode_id": "EP01",
  "source_hashes": {
    "storyboard_index_sha256": "...",
    "asset_bindings_sha256": "..."
  },
  "workflow_identity": {
    "resolved_workflow_hash": "..."
  },
  "requirements": []
}
```

首期资产表自动产生图片 reference。schema 和 provider 能力允许 image/video/audio，但 video/audio 只有在真实 transport、Active 回写与实际 `content` 序列化均成立时才计入；空数组、逻辑声明或不存在的 Ark ID 不算素材。

`seedance_local_materials.json` 使用 schema v2，包含 profile/project/episode/materials。它只登记本地/公网素材、MIME、SHA-256 和授权状态，不得包含 Ark ID 或 Ark 状态。

## Provider request

每个 cut 的 `provider_request` 使用唯一 serializer 生成：

```json
{
  "model": "doubao-seedance-2-5-260628",
  "content": [
    {"type": "text", "text": "资产分类前置、整体画风、空间衔接与连续时间轴 prompt"},
    {
      "type": "image_url",
      "role": "reference_image",
      "image_url": {"url": "asset://asset-example"}
    }
  ],
  "omni_reference_task_type": "reference",
  "ratio": "16:9",
  "resolution": "720p",
  "duration": 4,
  "generate_audio": true
}
```

硬约束：

- `duration` 必须是 4–30 的整数；provider 的 `-1` 自动时长不开放。
- `content` 至少有一个真正 Active、文件 hash 一致且被序列化的 `reference_image` / `reference_video` / `reference_audio`。
- 创建请求不得含 `fps`。24 fps 只用于结果媒体 QA。
- 创建请求不得含内部 `video_task_type=multimodal_generation`。内部任务通过 `omni_reference_task_type=reference` 与 reference content 映射。
- `ratio=16:9`、`resolution=720p`、`generate_audio=true` 固定。
- 官方 reference 路径不反向开放纯文本、首尾帧、关键帧、编辑、延长/续写或轨道补全。

### 提交提示词合同

`final.txt` 是资产无关审核母版；它按 `人物`、`场景`、`道具/关键视觉资产` 分出静态资产范围，但不能虚构 `@图片/@视频/@音频`。只有 Active 素材通过绑定与 hash 门禁后，v2 编译器才为每个 cut 生成 `submission_prompt`，并让 `provider_request.content[0].text` 与它完全一致。

编译顺序固定为：

1. `【人物资产】`：真实 token、逻辑键、参考职责和排除职责。
2. `【场景资产】`：真实 token、空间/材质/光线或构图职责。
3. `【道具与关键视觉资产】`：真实 token、器物/状态/关键视觉职责。
4. `【整体画风说明】`：横屏 16:9 高质量国漫 3D CG，“写实材质＋克制卡通轮廓”，亚洲骨相、适度动漫五官、可信 PBR＋少量手绘纹理、稳定轮廓、东方低饱和色盘、电影级布光、原生音频、无字幕、无配乐。
5. `【组间空间衔接】`：继承上一组世界末态，写清空间锚点、人物位置/朝向/视线/动作停点、画外在场者、道具归属与状态、VFX 持续/收束、轴线/机位、光线和声场；尾帧只可提供可见的局部信息。
6. `【横屏空间与调度】`、`【连续时间轴】`、`【组尾世界状态】`。
7. `【负面约束（--neg）】`：只保留本组 2–5 个具体失败风险。

不再编译 `一句话概述`、`视觉峰值/特效重点`、`运镜强化词` 或 `Seedance执行提示补充`，也不使用“资产1/资产2”的扁平清单。核心动态特效不得因静态资产参考而缩水，必须在实际连续时间轴保留来源→形态→路径→作用对象→反馈→收束→声音的完整语义链；局部余光、火星和环境底色按其可见因果写最小必要信息。特效、光影、声音和确有必要的执行约束直接写入时间轴，镜头运动和景别由 Seedance 2.5 自主选择，除非剧情/连续性需要锁定。`seedance_submission_prompts.md` 是同一 `submission_prompt` 的人读镜像，方便生产人员在提交前逐组核对实际引用了哪些资产；它不是第二状态真源，也不能绕过 `submit_allowed`。

## 本地有效性与提交门禁

`handoff_schema_valid=true` 表示：profile、workflow identity、final/index/bindings hash、schema、project/episode、duration 和 provider 固定字段在本地一致。它不需要已有 Ark 回写。

`generation_ready=true` 还要求每个 cut 至少有一项本地文件 hash 一致且 ManJuWeb 回写为 Active 的 reference，并且该项实际出现在 provider `content` 中。

`submit_allowed=true` 还要求：

- 每项使用素材授权确认；
- ManJuWeb consumer contract 与 serializer schema 已由双方 fixture 对齐；
- 当前目标 environment/account/model/region preflight 有效；
- 回写来自认证 transport，nonce、摘要、环境、账号假名、时间窗和防重放验证通过；
- 所有 policy blocker 清零。

Unit 6A 不具备后三类外部证据，因此只能产生 `submit_allowed=false` 的包。手工创建一个名为 preflight/consumer 的 JSON 文件不能解除门禁。

## 命令

```powershell
python .\storyboard_agent_workspace.py export-seedance-material-requirements --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py validate-seedance-materials --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py export-seedance-package --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py workflow-status --episode-dir <episode-dir>
```

三类真实探针属于 run 级状态；三集 episode readiness 均已生成后，再运行：

```powershell
python .\storyboard_agent_workspace.py workflow-status --run-dir <run-dir>
```

run 级命令会重算并核对三集当前 readiness、package identity 和 probe evidence。未接入可信 ManJuWeb authenticity verifier 时，它必须以非零退出并保持 `workflow_validated=false`。

`export-seedance-package` 可以写出被阻塞的审计包；横屏 v2 在 `submit_allowed=false` 时以非零状态结束并列出 submission blockers。

## 外部 consumer 合同待办（Unit 6B）

只有真实 ManJuWeb 团队/环境提供并认可的脱敏 fixtures 才能完成 Unit 6B。fixtures 至少覆盖 outbound package、Ark sync response、task create/final response 和可选 preflight acknowledgment，并绑定 package/request digest、nonce、environment/account pseudonym、task/model/region、时间窗和结果 digest。

仓库和普通 run 不保存 Authorization、cookie、签名参数、临时结果 URL、内部 host、真实账号 ID、真实素材 ID 或原始抓包。缺失、未认证、过期、重放、摘要不符、环境/账号不符的证据必须 fail closed。
