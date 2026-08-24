# Seedance 2.5 素材交接合同 v1

本合同连接 Auto-Storyboard 与 ManJuWeb，但不让两个仓库共同维护 Ark 状态。

## 职责边界

Auto-Storyboard 负责：

- 从 `final.txt` 生成并保留稳定的 `storyboard_index.json`，每组使用 `EPxx-GNN` 形式的 `cut_id`。
- 从已审核的 `asset_bindings.json` 编译逻辑素材需求。
- 登记实际素材的本地路径或公网 URL、MIME、SHA-256 和授权确认。
- 校验 ManJuWeb 回写结果是否属于同一轮输入。
- 按真实 Active 素材顺序编译每个 `cut_id` 的 Seedance 请求草稿。

Auto-Storyboard 不负责：

- Ark 密钥、上传、轮询、重试或状态持久化。
- 生成或猜测 Ark `assetId`。
- 把静态图片绑定猜成动作视频、运镜视频或音频素材。

ManJuWeb 后端负责：

- 接收需求 JSON、本地素材清单和实际文件。
- 复核上传字节与清单 SHA-256、MIME 和授权状态。
- 按文件哈希复用已有 Active Ark 图片，或通过既有 Ark 中转和 OpenAPI 入库。
- 以 `ArkAsset` 作为 Ark 状态的唯一权威来源，并保存逻辑素材到 Ark ID 的映射。
- 原样返回 `ark_sync_results.json`；不得改写 Auto-Storyboard 的逻辑需求。

ManJuWeb 前端在 v1 不承担 Ark 业务逻辑。后续 UI 只负责选择两份 JSON 和实际文件、调用后端接口、下载回写结果及展示缺失项；浏览器不能直连 Ark、不能保存 Ark 密钥、不能自行宣布 Active。先稳定后端合同，再接入现有视频页面，避免把半成品状态写进生产任务。

## 文件流

```text
final.txt
  -> storyboard_index.json
  -> asset_bindings.json
  -> seedance_material_requirements.json
  +  seedance_local_materials.json
  -> ManJuWeb /api/seedance-materials/sync
  -> ark_sync_results.json
  -> seedance_generation_package.json
```

## Auto-Storyboard 输出

### `seedance_material_requirements.json`

该文件由程序编译，禁止手写。核心字段：

```json
{
  "schema_version": 1,
  "profile": "seedance-2.5-live-vertical",
  "project": "项目名",
  "episode_id": "EP01",
  "source_hashes": {
    "storyboard_index_sha256": "64位小写十六进制",
    "asset_bindings_sha256": "64位小写十六进制"
  },
  "requirements": [
    {
      "requirement_id": "EP01_BIND_001",
      "cut_id": "EP01-G01",
      "material_key": "CHAR_MOTHER_BASE",
      "media_type": "image",
      "role": "character_identity",
      "required": true,
      "requirement_mode": "yes",
      "priority": 100,
      "provides": ["face", "hair", "age", "body_identity"],
      "excludes": ["wardrobe", "action", "camera_motion"]
    }
  ]
}
```

当前自动编译只接受 `asset_bindings.json` 中 `use_for_video=yes|conditional` 的静态图片绑定；`use_for_video=no` 不进入素材清单。

### `seedance_local_materials.json`

该文件可由素材准备环节填写，但不得出现 Ark ID 或 Ark 状态字段。

```json
{
  "schema_version": 1,
  "project": "项目名",
  "episode_id": "EP01",
  "materials": [
    {
      "material_key": "CHAR_MOTHER_BASE",
      "media_type": "image",
      "source": {
        "kind": "local_file",
        "path": "materials/mother.png"
      },
      "mime_type": "image/png",
      "sha256": "64位小写十六进制",
      "authorization": {
        "status": "confirmed",
        "note": "项目自有素材"
      }
    }
  ]
}
```

`source.kind` 支持 `missing`、`local_file`、`public_url`。v1 ManJuWeb MVP 只自动入库随请求上传且 SHA-256 匹配的图片文件；公网 URL、视频和音频会返回明确的未就绪结果，不会静默替代。

## ManJuWeb 接口与回写

`POST /api/seedance-materials/sync`，需要现有登录令牌，使用 `multipart/form-data`：

- `requirementsFile`：一份 `seedance_material_requirements.json`。
- `localMaterialsFile`：一份 `seedance_local_materials.json`。
- `materialFiles`：最多 30 个图片文件；服务端按 SHA-256 匹配，不依赖文件顺序或文件名。

若相同 SHA-256 已存在于 ManJuWeb 的 Active Ark 资产库，`materialFiles` 可以省略该文件并直接复用；缓存未命中时才必须上传实际字节。

返回体可直接保存为 `ark_sync_results.json`：

```json
{
  "schema_version": 1,
  "authority": "manjuweb",
  "project": "项目名",
  "episode_id": "EP01",
  "generation_ready": true,
  "source_hashes": {
    "material_requirements_sha256": "上传需求文件原始字节哈希",
    "local_materials_sha256": "上传本地清单原始字节哈希"
  },
  "materials": [
    {
      "material_key": "CHAR_MOTHER_BASE",
      "media_type": "image",
      "sha256": "素材文件哈希",
      "ark_asset_id": "asset://asset-example",
      "ark_status": "active",
      "reused": false
    }
  ]
}
```

状态只使用 `missing`、`processing`、`active`、`failed`。只有 ManJuWeb 可写 `ark_status` 和 `ark_asset_id`。

## 生成包门禁

```powershell
python .\storyboard_agent_workspace.py export-seedance-material-requirements --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py validate-seedance-materials --episode-dir <episode-dir>
python .\storyboard_agent_workspace.py export-seedance-package --episode-dir <episode-dir>
```

`seedance_generation_package.json` 同时绑定以下 SHA-256：

- `final.txt`
- `storyboard_index.json`
- `seedance_material_requirements.json`
- `seedance_local_materials.json`
- `ark_sync_results.json`
- 每项实际素材文件

任一内容变化都会使旧包失效。每个 `cut_id` 至少需要一项哈希一致且 Ark 状态为 Active 的素材；缺文件、授权未确认、回写不匹配、数量越界、Ark ID 无效或输入过期时，输出保持 `generation_ready=false`、`submit_allowed=false`。

`storyboard_index.json.source_hashes.final_txt_sha256` 还会直接绑定生成索引时的最终稿；即使尚未导出过生成包，只要 `final.txt` 后续发生变化，旧索引和由它派生的素材需求也会被门禁判为过期。

每个 cut 的 `request_draft` 使用 ManJuWeb `VideoService` 可直接识别的字段，包括 `referenceImageSlots[].assetId`、`generateAudio`、`ratio`、`resolution` 与 `duration`；`@图片N` 的编号顺序与 `referenceImageSlots` 顺序一致。当前 MVP 尚未启用视频/音频 Ark 入库，因此 `referenceVideos` / `referenceAudios` 保持空数组。
