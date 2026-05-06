# 《刚毅物流 ep01》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP01_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | ep01 第1组-第7组 | 林刚从代收点冲突到决定离村的主角连续形象 | no | reuse existing character state |
| EP01_USE_CHAR_002 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep01 第1组-第6组 | 赵大强举碎碗讹赔、抢通知书、踹门威胁 | no | reuse existing character state |
| EP01_USE_SCENE_001 | SCENE_LINGANG_DEPOT_BASE | STATE_SCENE_DEPOT_DAY_DUST_V1 | scene | asset_bible | ep01 第1组-第6组 | 代收点院门前白天强日光、尘土、快递纸箱凌乱状态 | no | reuse existing scene state |
| EP01_USE_PROP_001 | PROP_EXPRESS_BOX_BASE | BASE | prop | asset_bible | ep01 第1组、第3组-第6组 | 快递包裹、纸箱和快递单承载代收点纠纷与摊牌证据 | no | reuse existing prop base |
| EP01_USE_PROP_002 | PROP_BROKEN_BOWL_BASE | BASE | prop | asset_bible | ep01 第1组-第6组 | 赵大强讹赔用的豁口碎碗 | no | reuse existing prop base |
| EP01_USE_PROP_003 | PROP_CRACKED_PHONE_BASE | STATE_PROP_PHONE_CRACKED_RECORDING_V1 | prop | asset_bible | ep01 第2组-第3组、第7组 | 林刚录像反制、手机摔裂后仍保留录像证据 | no | reuse existing prop state |
| EP01_USE_PROP_004 | PROP_LEDGER_BASE | BASE | prop | asset_bible | ep01 第6组 0-6秒 | 林刚撕毁记满油费的账本，象征代收点阶段结束 | no | reuse existing prop base |
| EP01_USE_COMP_001 | COMPOSITION_DEPOT_CONFRONTATION_V1 | BASE | composition | asset_bible | ep01 第1组-第5组 | 林刚和赵大强在代收点院门前左右对峙的复用构图 | no | reuse existing composition |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_PROP_NOTICE_STAMPED_V1 | PROP_VILLAGE_NOTICE_BASE | BASE | prop | prop_condition | 村委会盖章通知书，正反两面用于宣布代收点关闭和便民服务站运营 | 模糊红章、通知书纸张、正反面说明 | episode_range | ep01 | ep01 第4组-第5组 | yes | generate stamped notice prop state | candidate | 村委会盖章通知书道具，A4纸大小，纸面略有折痕，红色印章清楚但正文不可读，正反两面都可作为拍摄参考，真实乡镇办事文件质感，竖屏道具特写，柔和日光 | 可读正文、真实公章名称、二维码、品牌logo、水印、字幕、手指畸形、卡通、3D渲染 | Village committee stamped notice prop, A4 paper with slight creases, a visible red stamp but unreadable body text, both front and back usable as production reference, realistic township paperwork texture, vertical prop close-up, soft daylight | readable body text, real official seal name, QR code, brand logo, watermark, subtitles, deformed fingers, cartoon, 3D render |
| STATE_PROP_LEDGER_TORN_V1 | PROP_LEDGER_BASE | BASE | prop | prop_condition | 油费账本被林刚当众撕碎，碎纸落入垃圾桶 | 账页撕裂、碎纸、旧账本纸张 | one_episode | ep01 | ep01 第6组 0-6秒 | yes | generate if torn ledger close-up needed | no | 旧运输账本被撕开的状态，泛黄账页断裂成碎纸，边缘粗糙，表格痕迹模糊不可读，少量碎纸落入普通垃圾桶，真实手持比例，日光与院角阴影混合 | 可读金额、清晰个人信息、品牌logo、血迹、过度戏剧化火焰、字幕、水印、卡通、3D渲染 | Torn old transport ledger state, yellowed pages ripped into rough paper fragments, blurry unreadable table marks, some scraps falling into a plain trash bin, realistic handheld scale, daylight mixed with yard-corner shadow | readable amounts, clear personal information, brand logo, blood, exaggerated flames, subtitles, watermark, cartoon, 3D render |
| STATE_SCENE_LINGANG_ROOM_DAY_V1 | SCENE_LINGANG_ROOM_BASE | BASE | scene | lighting_time | 林刚简陋屋内白天窗光状态，床、旧柜、衣物和墙上证件可见 | 白天窗光、简陋陈设、墙上证件 | episode_range | ep01 | ep01 第7组 | yes | generate new interior scene state | candidate | 林刚简陋屋内空镜，单人床、旧柜、几件衣物和墙上贴着的物流资格证及零事故记录，床底露出旧帆布包一角，白天窗光从左侧进入，墙面漫反射柔和，无人无人脸，真实乡镇出租屋质感，竖屏电影构图 | 人物、人脸、可读证件编号、品牌logo、字幕、水印、豪华装修、卡通、3D渲染、过曝 | Empty interior of Lin Gang's modest room, single bed, old cabinet, a few clothes, logistics qualification certificate and zero-accident record posted on the wall, a worn canvas bag partly visible under the bed, daylight entering from the left window, soft wall bounce, no people, no faces, realistic township rental-room texture, vertical cinematic framing | people, faces, readable certificate numbers, brand logo, subtitles, watermark, luxury decor, cartoon, 3D render, overexposure |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| PROP_VILLAGE_NOTICE_BASE | prop | 村委会盖章通知书 | 乡镇村委会通知书类文件，A4纸，带红章，可用于代收点关闭、服务站说明等剧情证据，正文不可读 | episode_range | ep01 | candidate | 乡镇村委会通知书道具，A4纸张，白纸黑字形成模糊排版感，局部红色印章，纸面有轻微折痕，正式但朴素的基层通知文件质感，竖屏道具参考图 | 可读正文、真实单位名称、二维码、品牌logo、水印、字幕、过度崭新塑料感、卡通、3D渲染 | Township village committee notice prop, A4 paper, black text only as blurry layout texture, partial red stamp, slight paper creases, formal but plain grassroots notice document texture, vertical prop reference image | readable body text, real organization name, QR code, brand logo, watermark, subtitles, overly glossy plastic feel, cartoon, 3D render |
| PROP_CANVAS_BAG_BASE | prop | 旧帆布包 | 林刚离村时反复携带的旧帆布包，磨损布面和肩带，适合装衣物或现金 | episode_range | ep01 | candidate | 旧帆布包道具，深灰绿色或褪色军绿色粗帆布，边角磨损，拉链和肩带结实，包体可半开露出普通衣物边缘，真实手提比例，乡镇物流人物随身行李质感 | 品牌logo、可读文字、奢侈品外观、过度崭新、人物脸、字幕、水印、卡通、3D渲染 | Worn canvas bag prop, dark gray-green or faded army-green coarse canvas, scuffed corners, sturdy zipper and strap, bag can be half open with plain clothes barely visible, realistic handheld scale, luggage texture for a township logistics worker | brand logo, readable text, luxury look, overly new condition, human face, subtitles, watermark, cartoon, 3D render |
| SCENE_LINGANG_ROOM_BASE | scene | 林刚屋内 | 简陋乡镇住处，床、旧柜、衣物、墙上物流资格证和零事故记录，作为林刚离村决定场景 | episode_range | ep01 | candidate | 林刚简陋屋内空镜，狭小房间，单人床靠墙，旧柜和少量衣物，墙上贴着物流从业资格证和零事故记录但文字不可读，水泥或旧涂料墙面，白天自然窗光，无人无人脸，真实电影质感 | 人物、人脸、清晰证件文字、品牌logo、字幕、水印、豪华家具、卡通、3D渲染、广角畸变 | Empty interior of Lin Gang's modest room, narrow room, single bed against the wall, old cabinet and a few clothes, logistics qualification certificate and zero-accident record on the wall but unreadable, cement or old painted walls, natural daylight from window, no people, no faces, realistic cinematic texture | people, faces, readable certificate text, brand logo, subtitles, watermark, luxury furniture, cartoon, 3D render, wide-angle distortion |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_PROP_PHONE_CRACKED_RECORDING_V1 | PROP_CRACKED_PHONE_BASE | prop | 裂屏手机仍显示录像红点 | ep01 第3组 0-3秒、第7组 0-6秒 | no | reuse existing phone evidence state | 复用已有状态 |
| STATE_PROP_NOTICE_STAMPED_V1 | PROP_VILLAGE_NOTICE_BASE | prop | 村委会盖章通知书正反面 | ep01 第4组-第5组 | yes | generate stamped notice state | 建议同步到asset_bible |
| STATE_PROP_LEDGER_TORN_V1 | PROP_LEDGER_BASE | prop | 油费账页被撕碎并丢进垃圾桶 | ep01 第6组 0-6秒 | yes | generate if torn ledger close-up needed | 仅本集使用 |
| STATE_SCENE_DEPOT_DAY_DUST_V1 | SCENE_LINGANG_DEPOT_BASE | scene | 代收点院门前白天尘土与快递凌乱状态 | ep01 第1组-第6组 | no | reuse existing dusty depot state | 复用已有状态 |
| STATE_SCENE_LINGANG_ROOM_DAY_V1 | SCENE_LINGANG_ROOM_BASE | scene | 简陋屋内白天窗光、床柜衣物和墙上证件 | ep01 第7组 | yes | generate interior scene state | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 石桌、院门、屋门、垃圾桶 | ep01 第3组-第6组 | 普通场景陈设，已由代收点场景状态或屋内场景承载，无需单独稳定生成 |
| 村民甲、村民乙、十几个村民 | ep01 第1组-第6组 | 临时围观群众和台词功能角色，不固定脸，不作为跨集基础人物资产 |
| 皱眉、冷笑、咬牙、互相看一眼 | ep01 多组近景 | 短暂表演和情绪变化，不是可复用资产状态 |
| 床、旧柜、几件衣物 | ep01 第7组 | 普通室内陈设，归入林刚屋内场景资产，不单独入库 |
| 手机消息文字、证件墙面文字 | ep01 第7组 | 屏幕或墙面信息来自分镜展示，除必要剧情屏幕外不建立可读文字资产，避免生成错误文字 |
