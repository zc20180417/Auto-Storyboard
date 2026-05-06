# 《刚毅物流 ep07》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP07_USE_CHAR_001 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒，第6组0-10秒，第7组0-10秒 | 赵大强雪路抛锚、煽动村民、堵门冲突的反派人物基准 | no | reuse existing villain state |
| EP07_USE_CHAR_002 | CHAR_LINGANG_BASE | STATE_LINGANG_SNOW_WORK_V1 | character | episode_variant | 第5组0-14秒，第6组0-10秒，第7组0-10秒 | 林刚雪天驾驶皮卡、守在家门内、端水枪威慑人群 | conditional | if state not generated |
| EP07_USE_SCENE_001 | SCENE_MOUNTAIN_ROAD_BASE | STATE_SCENE_MOUNTAIN_SNOW_V1 | scene | asset_bible | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒 | 大雪盘山公路、故障车横停、村民围车与奔向村里 | no | reuse existing snowy mountain road state |
| EP07_USE_SCENE_002 | SCENE_LINGANG_HOME_GATE_BASE | STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | scene | episode_new | 第6组0-10秒，第7组0-10秒 | 林刚家大铁门外雪天围堵和门内威慑空间 | yes | new recurring home gate scene |
| EP07_USE_PROP_001 | VEHICLE_OLD_VAN_BASE | STATE_VEHICLE_OLD_VAN_SMOKING_FROZEN_V1 | prop | episode_variant | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒 | 赵大强的破旧面包车抛锚、车头冒黑烟、底盘冻住 | conditional | if damaged frozen vehicle state not generated |
| EP07_USE_PROP_002 | VEHICLE_PICKUP_BASE | STATE_PICKUP_SNOW_DRIVING_V1 | prop | episode_variant | 第5组0-14秒 | 林刚在雪路中稳定驾驶皮卡并挂低速四驱 | conditional | if snow driving pickup state not generated |
| EP07_USE_PROP_003 | PROP_HIGH_PRESSURE_WASHER_BASE | BASE | prop | episode_new | 第7组5-10秒 | 林刚端起高压洗车水枪指向门外人群 | yes | new key defensive prop |
| EP07_USE_PROP_004 | PROP_SEAFOOD_CARGO_BASE | STATE_PROP_SEAFOOD_FROZEN_V1 | prop | episode_new | 第1组6-11秒，第2组0-10秒，第3组6-11秒，第4组0-7秒 | 海鲜货箱与冻硬帝王蟹证明货损和赔钱冲突 | yes | new one episode cargo prop |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_LINGANG_SNOW_WORK_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | dirt_damage | 林刚雪天工作状态，深色工装外套沾少量雪粒，仍保持沉稳硬朗 | outerwear_snow，cold_light，work_jacket_continuity | episode_range | ep07 | 第5组0-14秒，第6组8-10秒，第7组5-10秒 | yes | generate if later snow home scenes reuse Lin Gang | candidate | 林刚基于 CHAR_LINGANG_BASE，沿用 COSTUME_LINGANG_WORK_JACKET_V1，深色工装外套肩头和袖口有少量雪粒，雪天冷白光，人物全身或半身定妆，写实电影质感，现代中国乡镇物流短剧，竖屏构图 | 西方人面孔，卡通，3D渲染，过度磨皮，夸张伤痕，新增服装颜色，品牌logo，可读文字，水印，字幕 | Lin Gang based on CHAR_LINGANG_BASE, using COSTUME_LINGANG_WORK_JACKET_V1, dark work jacket with light snow on shoulders and cuffs, cold white snowy light, full body or half body character reference, realistic cinematic Chinese township logistics drama, vertical composition | Western facial features, cartoon, 3D render, over-smoothed skin, exaggerated wounds, changed costume color, brand logo, readable text, watermark, subtitles |
| STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | SCENE_LINGANG_HOME_GATE_BASE | BASE | scene | scene_condition | 林刚家院门外雪天状态，大铁门、门檐积雪、门前雪泥和冷白散射光 | snow_cover，muddy_ground，cold_daylight，gate_pressure | episode_range | ep07 | 第6组0-10秒，第7组0-10秒 | yes | required for repeated home gate conflict | candidate | 林刚家院门外雪天空镜，大铁门占画面中心，门檐和门框压着积雪，门前泥地混着雪水和脚印，冷白阴雪天散射光，门内较暗但有层次，无人无人脸，真实乡镇院落，竖屏电影构图 | 人物，人脸，围观人群，卡通，3D渲染，古装，品牌logo，可读文字，水印，字幕，过曝 | Empty snowy exterior of Lin Gang home gate, large iron gate centered, snow on eaves and frame, muddy snow and footprints before the gate, cold overcast diffused daylight, darker layered interior beyond gate, no people or faces, realistic township courtyard, vertical cinematic framing | People, faces, crowd, cartoon, 3D render, historical costume, brand logo, readable text, watermark, subtitles, overexposure |
| STATE_VEHICLE_OLD_VAN_SMOKING_FROZEN_V1 | VEHICLE_OLD_VAN_BASE | BASE | prop | prop_condition | 破旧面包车雪路抛锚状态，车头冒黑烟，水箱漏光，底盘冻住 | black_smoke，frozen_chassis，snow_mud，damaged_front | one_episode | ep07 | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒 | yes | one episode damaged vehicle state | no | 破旧小型面包车基于 VEHICLE_OLD_VAN_BASE，斜停在积雪盘山公路上，车头引擎盖缝隙冒浓黑烟，保险杠边缘焦黑，轮胎周围是雪泥，底盘有冻住的冰雪痕迹，无品牌logo无车牌文字，写实车辆道具 | 可读车牌，品牌logo，人物，人脸，爆炸火焰，卡通，3D渲染，塑料感，字幕，水印 | Old small van based on VEHICLE_OLD_VAN_BASE, parked diagonally on a snowy mountain road, thick black smoke from hood seam, scorched bumper edge, snow mud around tires, frozen undercarriage traces, no brand logo or license text, realistic vehicle prop | Readable license plate, brand logo, people, faces, explosion flames, cartoon, 3D render, plastic look, subtitles, watermark |
| STATE_PICKUP_SNOW_DRIVING_V1 | VEHICLE_PICKUP_BASE | BASE | prop | prop_condition | 林刚皮卡雪路行驶状态，车身带雪泥，低速四驱行驶，车内冷光 | snow_mud，winter_driving，dashboard_cold_light | episode_range | ep07 | 第5组0-14秒 | yes | useful for following snowy driving episodes | candidate | 深色实用皮卡基于 VEHICLE_PICKUP_BASE，雪天盘山路行驶状态，轮胎沾雪泥，车身边缘有湿冷反光，驾驶室内仪表盘冷光，车辆无品牌logo无车牌文字，真实物流运输质感 | 可读车牌，品牌logo，夸张赛车改装，人物脸部特写，卡通，3D渲染，水印，字幕 | Dark utility pickup based on VEHICLE_PICKUP_BASE in snowy mountain road driving state, snow mud on tires, cold wet reflections on body, cool dashboard light inside cabin, no brand logo or license text, realistic logistics transport texture | Readable license plate, brand logo, exaggerated racing modification, facial close-up, cartoon, 3D render, watermark, subtitles |
| STATE_PROP_SEAFOOD_FROZEN_V1 | PROP_SEAFOOD_CARGO_BASE | BASE | prop | prop_condition | 海鲜货箱冻硬状态，货箱内帝王蟹和海鲜结冰成硬块 | frozen_food，ice_crust，open_cargo_box | one_episode | ep07 | 第1组6-11秒，第2组0-10秒，第3组6-11秒，第4组0-7秒 | yes | generated only for cargo loss shots | no | 海鲜货箱道具，普通泡沫箱和冷藏货箱打开，箱内帝王蟹和海鲜被冻成硬块，表面有冰霜和冷凝水，货箱无可读品牌文字，真实生鲜运输货损细节 | 可读商标，真实品牌，血腥，腐烂夸张，人物，人脸，卡通，3D渲染，水印，字幕 | Seafood cargo boxes, common foam and refrigerated boxes opened, king crab and seafood frozen into hard blocks, frost and condensation on surface, no readable brand text, realistic fresh food transport loss detail | Readable trademarks, real brands, gore, exaggerated decay, people, faces, cartoon, 3D render, watermark, subtitles |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_VILLAGER_CROWD_BASE | character | 村民群像 | 十几个乡村村民群像，不固定单人脸，作为围堵、起哄、冲门的群众资产使用 | episode_range | ep07 | candidate | 中国乡村村民群像，成年男女混合，冬天深色棉衣和旧外套，体态普通，表情可根据剧情变化但不固定单人脸，真实短剧群众定妆，竖屏构图，电影质感 | 固定明星脸，西方人面孔，统一制服，古装，卡通，3D渲染，品牌logo，可读文字，水印，字幕 | Chinese village crowd, mixed adult men and women, dark winter padded coats and worn jackets, ordinary body types, expressions can vary by scene without fixed individual faces, realistic short drama crowd reference, vertical cinematic style | Celebrity face, Western faces, uniform costumes, historical costume, cartoon, 3D render, brand logo, readable text, watermark, subtitles |
| SCENE_LINGANG_HOME_GATE_BASE | scene | 林刚家院门外 | 乡镇民宅院门外空间，核心是大铁门、门檐、院墙和门前泥地，基础资产为空镜 | episode_range | ep07 | candidate | 中国乡镇民宅院门外空镜，大铁门、旧院墙、门檐、门环、门前泥地和院内阴影层次，现代乡村住宅质感，冷天自然光，无人无人脸，竖屏电影构图 | 人物，人脸，围观群众，豪宅别墅，古装建筑，品牌logo，可读文字，卡通，3D渲染，水印，字幕 | Empty exterior of a Chinese township home gate, large iron gate, old courtyard wall, eaves, door ring, muddy ground before the gate and layered shadows inside, modern rural residence texture, cold natural light, no people or faces, vertical cinematic framing | People, faces, crowd, luxury villa, historical architecture, brand logo, readable text, cartoon, 3D render, watermark, subtitles |
| PROP_HIGH_PRESSURE_WASHER_BASE | prop | 高压洗车水枪 | 粗大的高压洗车水枪，金属接口和黑色软管清楚，是林刚守门威慑的关键道具 | episode_range | ep07 | candidate | 高压洗车水枪道具，粗黑枪身，金属喷嘴和接口，连接黑色高压软管，表面有水珠和冷光反射，手持比例真实，无品牌logo无可读文字 | 品牌logo，可读标签，玩具感，科幻武器，人物，人脸，卡通，3D渲染，水印，字幕 | High pressure car wash gun prop, thick black body, metal nozzle and connector, attached black high pressure hose, water droplets and cold reflections, realistic handheld scale, no brand logo or readable text | Brand logo, readable label, toy-like look, sci-fi weapon, people, faces, cartoon, 3D render, watermark, subtitles |
| PROP_SEAFOOD_CARGO_BASE | prop | 海鲜货箱与帝王蟹 | 运输海鲜用泡沫箱和货箱，包含帝王蟹轮廓，作为本集货损冲突证据 | one_episode | ep07 | no | 生鲜海鲜运输货箱道具，白色泡沫箱和冷藏货箱，箱内可见帝王蟹和海鲜轮廓，冷链运输质感，无真实品牌和可读标签，真实比例 | 可读品牌，二维码，个人信息，人物，人脸，血腥腐烂，卡通，3D渲染，水印，字幕 | Fresh seafood transport cargo prop, white foam boxes and refrigerated cargo boxes, visible king crab and seafood shapes inside, cold chain logistics texture, no real brands or readable labels, realistic scale | Readable brand, QR code, personal information, people, faces, gore or decay, cartoon, 3D render, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_MOUNTAIN_SNOW_V1 | SCENE_MOUNTAIN_ROAD_BASE | scene | 复用雪天盘山公路状态，承载故障车和村民冲突 | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒 | no | existing bible state | 复用已有状态 |
| STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | SCENE_LINGANG_HOME_GATE_BASE | scene | 林刚家大铁门雪天围堵状态 | 第6组0-10秒，第7组0-10秒 | yes | new recurring home gate state | 建议同步到asset_bible |
| STATE_VEHICLE_OLD_VAN_SMOKING_FROZEN_V1 | VEHICLE_OLD_VAN_BASE | prop | 破旧面包车冒黑烟、底盘冻结、水箱故障状态 | 第1组0-11秒，第2组0-10秒，第3组0-11秒，第4组0-10秒 | yes | one episode damaged vehicle state | 仅本集使用 |
| STATE_PICKUP_SNOW_DRIVING_V1 | VEHICLE_PICKUP_BASE | prop | 林刚皮卡雪路四驱行驶状态 | 第5组0-14秒 | yes | likely reused by ep08 and ep09 snowy driving | 建议同步到asset_bible |
| BASE | PROP_HIGH_PRESSURE_WASHER_BASE | prop | 高压洗车水枪基础道具 | 第7组5-10秒 | yes | key prop continues into ep08 | 建议同步到asset_bible |
| STATE_PROP_SEAFOOD_FROZEN_V1 | PROP_SEAFOOD_CARGO_BASE | prop | 冻硬海鲜货箱与帝王蟹货损状态 | 第1组6-11秒，第2组0-10秒，第3组6-11秒，第4组0-7秒 | yes | cargo loss evidence for this episode | 仅本集使用 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 车钥匙和仪表盘闪灯 | 第1组2-6秒 | 属于一次性操作细节和车内反馈，由车辆状态承载即可 |
| 村民甲、村民乙的单独脸部表情 | 第1组6-11秒，第2组2-10秒，第3组0-11秒 | 属于临时群众表演，不固定为跨集角色资产 |
| 大铁门门环震响和积雪震落 | 第6组0-10秒 | 已由林刚家院门场景状态承载，不需要拆成独立道具 |
| 石头 | 第6组6-10秒，第7组0-5秒 | 一次性威胁小道具，生产价值低，不建议入库 |
| 方向盘、对讲机、四驱挡杆 | 第5组0-14秒 | 普通车内部件，由皮卡车辆状态或即时分镜生成即可 |
