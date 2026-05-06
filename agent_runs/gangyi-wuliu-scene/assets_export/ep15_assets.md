# 《刚毅物流 ep15》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP15_USE_CHAR_001 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep15 第1组0-14秒，第2组0-14秒，第3组2-11秒，第4组0-13秒 | 赵大强夜闯停泊场倒工业沙并误以为计成 | no | reuse existing villain state |
| EP15_USE_CHAR_002 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | ep15 第1组0-14秒，第2组0-14秒，第3组2-11秒，第4组0-13秒 | 王强和赵大强一起破坏重卡并躲到底盘下 | conditional | base character exists, no dedicated state in bible |
| EP15_USE_CHAR_003 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | ep15 第3组0-11秒，第4组3-5秒，第5组0-14秒，第6组0-11秒，第7组0-11秒 | 林刚提前得知消息，借旧重卡反制赵大强和王强 | no | reuse existing Lin Gang township stage |
| EP15_USE_SCENE_001 | SCENE_LOGISTICS_YARD_BASE | STATE_SCENE_LOGISTICS_YARD_NIGHT_V1 | scene | asset_bible | ep15 第1组0-14秒，第2组0-14秒，第3组0-11秒，第4组0-13秒，第5组0-14秒，第6组0-11秒，第7组0-11秒 | 夜晚阴天物流停泊场和另一处重卡旁 | no | reuse existing night yard state |
| EP15_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_TRUCK_SABOTAGED_V1 | prop | asset_bible | ep15 第1组12-14秒，第2组0-5秒，第3组5-11秒，第4组0-5秒 | 油箱被倒入工业微粒沙的重卡和车辆启动结果 | no | reuse existing sabotaged truck state |
| EP15_USE_PROP_002 | PROP_BLACK_BUCKET_SAND_BASE | BASE | prop | asset_bible | ep15 第1组0-14秒，第2组0-3秒 | 黑塑料桶与工业微粒沙，被赵大强和王强提入场倒进油箱 | no | reuse existing bucket and sand prop |
| EP15_USE_VEHICLE_001 | VEHICLE_PICKUP_BASE | STATE_VEHICLE_PICKUP_HEADLIGHTS_NIGHT_EP15 | prop | episode_variant | ep15 第2组5-14秒，第3组0-2秒 | 皮卡车灯突然逼近，制造强逆光并迫使二人躲到底盘下 | conditional | if night headlights state not generated |
| EP15_USE_PROP_003 | PROP_CRACKED_PHONE_BASE | BASE | prop | asset_bible | ep15 第7组0-6秒 | 林刚用手机给老张打电话借旧重卡 | no | reuse generic black phone base without cracked recording state |
| EP15_USE_COMP_001 | COMPOSITION_TRUCK_UNDERCARRIAGE_V1 | BASE | composition | asset_bible | ep15 第2组7-14秒，第3组2-11秒 | 赵大强和王强趴在重卡底盘阴影之间躲避 | no | reuse existing undercarriage composition |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_VEHICLE_PICKUP_HEADLIGHTS_NIGHT_EP15 | VEHICLE_PICKUP_BASE | BASE | prop | prop_condition | 夜晚停泊场内皮卡开启强车灯，从大门方向射入场地，地面水痕反光 | headlights, light_condition | one_episode | ep15 | ep15 第2组5-14秒，第3组0-2秒 | yes | generate if night headlight lighting plate is needed | no | 基于 VEHICLE_PICKUP_BASE，夜晚阴天物流停泊场内的深色实用皮卡，车灯打开形成两道强光束，水泥地水痕反光，车牌不可读，无品牌标志，真人实拍电影质感，竖屏构图 | 可读车牌，品牌logo，卡通，3D渲染，塑料感，过曝到全白，字幕，水印，西方场景 | Based on VEHICLE_PICKUP_BASE, a dark practical pickup truck in an overcast night logistics yard, headlights on and casting two strong beams, wet cement ground reflecting light, unreadable license plate, no brand logo, live action cinematic realism, vertical composition | readable license plate, brand logo, cartoon, 3D render, plastic texture, blown out white exposure, subtitles, watermark, western setting |
| STATE_VEHICLE_OLD_TRUCK_DECOY_EP15 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 老张车场里快报废的旧重卡，被林刚借来作为反制诱饵，车门和车身有明显磨损灰尘 | vehicle_condition | one_episode | ep15 | ep15 第7组2-11秒 | yes | generate old decoy truck if production needs separate look | candidate | 基于 VEHICLE_HEAVY_TRUCK_BASE，快报废的旧物流重卡，车门金属划痕和灰尘明显，车身老旧但仍可启动，夜晚低照度冷光，车牌不可读，无品牌标志，真人实拍电影质感 | 可读车牌，品牌logo，新增公司文字，卡通，3D渲染，塑料感，科幻改装，字幕，水印 | Based on VEHICLE_HEAVY_TRUCK_BASE, near scrap old logistics heavy truck, visible metal scratches and dust on the door and body, aged but still drivable, low cool night light, unreadable license plate, no brand logo, live action cinematic realism | readable license plate, brand logo, new company text, cartoon, 3D render, plastic texture, sci fi modification, subtitles, watermark |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_SECURITY_INFORMANT_BASE | character | 保安甲线人 | 瘦小男性保安，曾被主管开除后依靠林刚，穿保安服，神态紧张机灵，用于向林刚报信 | episode_range | ep15 | candidate | 中国县城物流场地瘦小男保安线人，30到40岁男性，体型偏瘦，短发，中国面孔，神情紧张机灵，穿深色保安服，肩膀微缩，真人实拍电影质感，竖屏角色定妆 | 西方人脸，警察制服，特警装备，夸张反派脸谱，品牌logo，可读文字，卡通，3D渲染，塑料感，字幕，水印 | Chinese logistics yard slim male security informant, 30 to 40 years old, thin build, short hair, Chinese face, tense and quick minded expression, wearing a dark security uniform, slightly hunched shoulders, live action cinematic realism, vertical character look image | western face, police uniform, SWAT gear, exaggerated villain stereotype, brand logo, readable text, cartoon, 3D render, plastic texture, subtitles, watermark |
| COSTUME_SECURITY_UNIFORM_V1 | costume | 普通保安服 | 深色保安服或保安夹克，裤脚普通，肩章和褶皱可见但不出现可读公司名，不是警服 | episode_range | ep15 | candidate | 当代中国普通保安服，深色夹克式制服和深色长裤，肩章轮廓和布料褶皱可见，实用旧感，非警服，无可读公司名，产品式服装参考，真人实拍质感 | 警徽，警服，特警装备，可读公司名，品牌logo，卡通，3D渲染，塑料感，字幕，水印 | Contemporary Chinese ordinary security uniform, dark jacket style uniform and dark trousers, visible shoulder patch shape and fabric creases, practical slightly worn look, not a police uniform, no readable company name, product style costume reference, live action texture | police badge, police uniform, SWAT gear, readable company name, brand logo, cartoon, 3D render, plastic texture, subtitles, watermark |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_LOGISTICS_YARD_NIGHT_V1 | SCENE_LOGISTICS_YARD_BASE | scene | 夜晚阴天物流停泊场，低照度冷光、地面水痕和重卡轮廓 | ep15 第1组0-14秒，第2组0-14秒，第3组0-11秒，第4组0-13秒，第5组0-14秒，第6组0-11秒，第7组0-11秒 | no | reuse existing night yard state | 复用已有状态 |
| STATE_VEHICLE_TRUCK_SABOTAGED_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 重卡油箱被倒入工业微粒沙，外观仍完整 | ep15 第1组12-14秒，第2组0-5秒，第3组5-11秒 | no | reuse existing sabotaged truck state | 复用已有状态 |
| BASE | PROP_BLACK_BUCKET_SAND_BASE | prop | 黑塑料桶和工业微粒沙，用于破坏重卡油箱 | ep15 第1组0-14秒，第2组0-3秒 | no | reuse existing bucket sand prop | 复用已有基础资产 |
| STATE_VEHICLE_PICKUP_HEADLIGHTS_NIGHT_EP15 | VEHICLE_PICKUP_BASE | prop | 皮卡夜间车灯强逆光扫进停泊场 | ep15 第2组5-14秒，第3组0-2秒 | yes | new one episode vehicle lighting state | 仅本集使用 |
| STATE_VEHICLE_OLD_TRUCK_DECOY_EP15 | VEHICLE_HEAVY_TRUCK_BASE | prop | 快报废旧重卡作为林刚反制诱饵 | ep15 第7组2-11秒 | yes | new decoy truck condition | 建议同步到asset_bible候选 |
| BASE | CHAR_SECURITY_INFORMANT_BASE | character | 保安甲向林刚报信并获得奖金承诺 | ep15 第5组2-14秒，第6组0-11秒，第7组0-2秒 | yes | new informant character | 建议同步到asset_bible候选 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 油箱盖拧动动作 | ep15 第1组12-14秒，第2组0-5秒 | 已由重卡被破坏状态承载，手部动作不单独入库 |
| 车门、方向盘、重卡轮胎局部 | ep15 第3组0-11秒，第5组0-2秒，第7组6-11秒 | 属于车辆基础资产的局部部件，可由重卡资产即时生成 |
| 黑烟和发动机轰鸣 | ep15 第3组8-11秒，第4组0-5秒 | 属于一次性动态效果和声音，不是静态资产 |
| 保安甲喘气、搓手、点头哈腰 | ep15 第5组5-14秒，第6组5-11秒 | 临时表演动作，不是人物外观状态 |
| 老张电话画外音 | ep15 第7组2-6秒 | 无画面人物，不建立角色资产 |
