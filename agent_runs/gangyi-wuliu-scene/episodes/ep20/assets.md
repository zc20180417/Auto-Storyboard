# 《刚毅物流 ep20》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP20_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组0-6秒，第2组0-11秒，第3组0-6秒，第4组3-15秒 | 林刚准时到仓并接下赌局 | no | existing convoy-stage state |
| EP20_USE_CHAR_002 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | 第1组2-6秒，第2组3-5秒，第3组10-12秒，第4组9-13秒 | 王百川在医药仓库外交接和阻拦 | no | existing boss state |
| EP20_USE_CHAR_003 | CHAR_CHENTIANBA_BASE | STATE_CHENTIANBA_MINK_COAT_V1 | character | episode_variant | 第1组8-11秒，第2组0-11秒，第3组2-10秒，第4组0-15秒 | 陈天霸穿貂皮大衣到场挑衅 | conditional | if state not generated |
| EP20_USE_CHAR_004 | CHAR_SUNBIAO_BASE | STATE_SUNBIAO_FACE_GAUZE_V1 | character | episode_variant | 第1组8-11秒，第2组5-7秒 | 孙彪带伤跟随陈天霸指认林刚 | conditional | if ep19 state not merged |
| EP20_USE_SCENE_001 | SCENE_MEDICAL_WAREHOUSE_BASE | STATE_SCENE_MEDICAL_WAREHOUSE_SUNNY_DELIVERY_V1 | scene | episode_variant | 第1组至第4组 | 医药仓库外晴天装卸区和仓库门口 | conditional | if sunny exterior state not generated |
| EP20_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第1组0-8秒，第2组组首，第3组2-6秒，第4组0-15秒 | 五台重卡和赌局对象 | no | existing heavy truck base |
| EP20_USE_PROP_002 | PROP_MEDICAL_COLD_BOX_BASE | STATE_PROP_MEDICAL_BOX_URGENT_V1 | prop | asset_bible | 第1组0-2秒，第3组6-12秒，第4组组首 | 进口药箱和疫苗药箱 | no | existing urgent medical cold box state |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_CHENTIANBA_MINK_COAT_V1 | CHAR_CHENTIANBA_BASE | BASE | character | costume_change | 陈天霸穿貂皮大衣，站在黑色豪华轿车旁挑衅 | costume, outerwear_texture, arrival_status | episode_range | ep20 | 第1组8-11秒，第2组0-11秒，第3组2-10秒，第4组0-15秒 | yes | if state not generated | candidate | 基于 CHAR_CHENTIANBA_BASE 和 COSTUME_CHENTIANBA_MINK_COAT_V1，陈天霸穿深色貂皮大衣站在黑色豪华轿车旁，脸部保持大脸厚嘴唇和阴沉眼神，日间仓库外硬光，真实中国地方物流老板反派气质，竖屏电影质感 | 西方面孔，卡通，3D渲染，品牌logo，车牌号，可读文字，水印，字幕，过度奢华珠宝 | Based on CHAR_CHENTIANBA_BASE and COSTUME_CHENTIANBA_MINK_COAT_V1, Chen Tianba wearing a dark mink coat beside black luxury sedans, retaining broad face, thick lips, gloomy eyes, daylight outside a warehouse, realistic Chinese local logistics boss antagonist, vertical cinematic live action | Western face, cartoon, 3D render, brand logo, license plate, readable text, watermark, subtitles, excessive luxury jewelry |
| STATE_SUNBIAO_FACE_GAUZE_V1 | CHAR_SUNBIAO_BASE | BASE | character | injury | 孙彪捂着一只眼睛，脸侧纱布延续，跟在陈天霸身后 | facial_gauze, covered_eye, minor_injury | episode_range | ep19 | 第1组8-11秒，第2组5-7秒 | yes | if ep19 state not merged | candidate | 基于 CHAR_SUNBIAO_BASE 和 COSTUME_WORKER_LOGISTICS_V1，孙彪脸侧贴白色纱布，一只手捂住眼部后又放下指认林刚，深色物流工装，真实中国打手形象，医药仓库外日间硬光 | 西方面孔，血腥伤口，卡通，3D渲染，品牌logo，可读文字，水印，字幕 | Based on CHAR_SUNBIAO_BASE and COSTUME_WORKER_LOGISTICS_V1, Sun Biao with white gauze on the side of his face, one hand covering an eye before pointing at Lin Gang, dark logistics workwear, realistic Chinese enforcer, daylight outside a medical warehouse | Western face, bloody wound, cartoon, 3D render, brand logo, readable text, watermark, subtitles |
| STATE_SCENE_MEDICAL_WAREHOUSE_SUNNY_DELIVERY_V1 | SCENE_MEDICAL_WAREHOUSE_BASE | BASE | scene | lighting_time | 医药仓库外晴天装卸区，药箱码放，重卡和黑色轿车队对峙 | daylight, loading_area, vehicle_blockade | episode_range | ep20 | 第1组0-11秒，第2组组首，第3组组首，第4组组首 | yes | if sunny exterior state not generated | candidate | 中国医药冷链仓库外装卸区空镜，晴天自然日光，金属卷帘门、混凝土地面、码放整齐的白色医药冷链箱和装卸月台，远处车辆通道清晰，无人无人脸，真实仓储电影质感，竖屏构图 | 人物，人脸，品牌logo，车牌号，可读文字，卡通，3D渲染，水印，字幕 | Empty exterior loading area of a Chinese medical cold-chain warehouse, sunny natural daylight, metal roll-up door, concrete ground, neatly stacked white medical cold-chain boxes and loading dock, clear vehicle lane in the distance, no people, no faces, realistic warehouse cinematic texture, vertical framing | People, faces, brand logo, license plate, readable text, cartoon, 3D render, watermark, subtitles |
| STATE_VEHICLE_BLACK_SEDAN_BLOCKADE_V1 | VEHICLE_BLACK_LUXURY_SEDAN_CONVOY_BASE | BASE | prop | prop_condition | 黑色豪华轿车队斜插到重卡前方，形成挡路状态 | blockade_position, glossy_black_paint, convoy_arrival | episode_range | ep20 | 第1组6-11秒，第2组组首，第4组组首 | yes | generate with new base vehicle prop | candidate | 黑色豪华轿车队挡路状态，几辆无品牌黑色商务轿车斜向停在重卡前方，车漆硬朗反光，车牌不可读，仓库外混凝土地面和晴天日光，真实物流冲突现场 | 品牌logo，清晰车牌，可读文字，人物脸，卡通，3D渲染，水印，字幕 | Black luxury sedan convoy blocking the road, several unbranded black business sedans parked diagonally in front of heavy trucks, glossy paint reflections, unreadable plates, concrete warehouse yard and sunny daylight, realistic logistics conflict scene | Brand logo, clear license plate, readable text, human faces, cartoon, 3D render, watermark, subtitles |
| STATE_COMPOSITION_WAREHOUSE_BLOCKADE_V1 | COMPOSITION_WAREHOUSE_BLOCKADE_CONFRONTATION_V1 | BASE | composition | composition_reference | 医药仓库门前，重卡、黑色轿车队、药箱和三方对峙形成空间关系 | warehouse_axis, vehicle_blockade, character_triangle | episode_range | ep20 | 第1组6-11秒，第2组0-11秒，第4组0-15秒 | yes | key confrontation composition | candidate | 竖屏对峙构图，医药仓库门口和药箱在一侧，五台重卡在另一侧，黑色豪华轿车队横在中间，林刚、王百川、陈天霸形成三角站位，晴天硬光，真实短剧物流冲突场面 | 品牌logo，车牌号，可读文字，卡通，3D渲染，字幕，水印，西方面孔 | Vertical confrontation composition, medical warehouse door and medicine boxes on one side, five heavy trucks on the other, black luxury sedans blocking the middle, Lin Gang, Wang Baichuan and Chen Tianba forming a triangular standoff, sunny hard light, realistic short-drama logistics conflict | Brand logo, license plate, readable text, cartoon, 3D render, subtitles, watermark, Western faces |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| COSTUME_CHENTIANBA_MINK_COAT_V1 | costume | 陈天霸深色貂皮大衣 | 深色厚重貂皮大衣，毛绒纹理明显，搭配反派老板压迫感，不包含人物脸部设定 | episode_range | ep20 | candidate | 深色貂皮大衣服装资产，厚重毛绒纹理，宽松廓形，适合中年地方物流老板反派穿着，日间自然光下材质真实，服装展示不含人物脸 | 人脸，西方面孔，品牌logo，可读文字，卡通，3D渲染，塑料感，水印 | Dark mink coat costume asset, heavy fur texture, loose silhouette, suited for a middle-aged local logistics boss antagonist, realistic material in daylight, clothing display without a face | Face, Western face, brand logo, readable text, cartoon, 3D render, plastic look, watermark |
| VEHICLE_BLACK_LUXURY_SEDAN_CONVOY_BASE | prop | 黑色豪华轿车队 | 无品牌黑色商务轿车队，可用于反派到场、堵路和压迫式车队画面，车牌不可读 | episode_range | ep20 | candidate | 无品牌黑色豪华商务轿车队基础车辆资产，深黑车漆，低矮车身，车窗微暗，车牌不可读，无logo，真实中国城市物流场景质感，日间自然光 | 品牌logo，清晰车牌，可读文字，卡通，3D渲染，玩具车比例，水印 | Base vehicle asset of an unbranded black luxury business sedan convoy, deep black paint, low body, slightly dark windows, unreadable plates, no logo, realistic Chinese urban logistics setting, daylight | Brand logo, clear license plate, readable text, cartoon, 3D render, toy-car proportions, watermark |
| COMPOSITION_WAREHOUSE_BLOCKADE_CONFRONTATION_V1 | composition | 仓库门前堵车对峙构图 | 医药仓库门前药箱、五台重卡、黑色轿车队和三方人物的对峙空间构图 | episode_range | ep20 | candidate | 竖屏电影对峙构图，医药仓库卷帘门和白色药箱作为背景，五台重卡停在右侧，黑色豪华轿车队横向挡路，三名主要人物分站不同方向形成冲突中心，晴天硬光 | 品牌logo，车牌号，可读文字，卡通，3D渲染，水印，字幕，西方面孔 | Vertical cinematic standoff composition, medical warehouse roll-up door and white medicine boxes in the background, five heavy trucks on the right, black luxury sedan convoy blocking across the road, three main characters positioned around the conflict center, sunny hard light | Brand logo, license plate, readable text, cartoon, 3D render, watermark, subtitles, Western faces |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_MEDICAL_WAREHOUSE_SUNNY_DELIVERY_V1 | SCENE_MEDICAL_WAREHOUSE_BASE | scene | 晴天医药仓库外装卸交接状态 | 第1组0-11秒，第2组组首，第3组组首，第4组组首 | yes | 新增仓库晴天外景状态 | 建议同步到asset_bible |
| STATE_VEHICLE_BLACK_SEDAN_BLOCKADE_V1 | VEHICLE_BLACK_LUXURY_SEDAN_CONVOY_BASE | prop | 黑色豪华轿车队挡住重卡去路 | 第1组6-11秒，第2组组首，第4组组首 | yes | 新增反派车队挡路状态 | 建议同步到asset_bible |
| STATE_CHENTIANBA_MINK_COAT_V1 | CHAR_CHENTIANBA_BASE | character | 陈天霸貂皮大衣到场挑衅状态 | 第1组8-11秒，第2组0-11秒，第3组2-10秒，第4组0-15秒 | yes | 新增角色服装状态 | 建议同步到asset_bible |
| STATE_PROP_MEDICAL_BOX_URGENT_V1 | PROP_MEDICAL_COLD_BOX_BASE | prop | 进口药箱和疫苗药箱作为恒温避震货物 | 第1组0-2秒，第3组6-12秒，第4组组首 | no | 复用既有医药冷链箱急送状态 | 复用已有状态 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 香烟和吐烟动作 | 第2组0-3秒，第2组7-11秒，第3组2-10秒 | 一次性表演道具和动作，不影响跨镜头资产稳定 |
| 拍手动作 | 第4组0-3秒 | 临时动作调度，不是可复用资产 |
| 王百川阻拦的手势 | 第4组9-13秒 | 人物表演动作，不拆成状态 |
| 重卡司机车窗后的紧张表情 | 第1组6-8秒 | 群像短暂反应，不固定为角色资产 |
| 仓库门口普通阴影和地面反光 | 第1组至第4组 | 已由医药仓库晴天状态承载，无需单独入库 |
