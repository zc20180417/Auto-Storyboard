# 《刚毅物流 ep25》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP25_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | 林刚在天霸物流园持合同对峙并指挥刚毅车队 | no | reuse existing convoy stage |
| EP25_USE_CHAR_002 | CHAR_CHENTIANBA_BASE | BASE | character | asset_bible | 第1组2-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | 陈天霸在秦爷身后挑衅和慌张反应 | no | reuse existing base character |
| EP25_USE_CHAR_003 | CHAR_QINYE_BASE | BASE | character | asset_bible | 第1组2-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | 秦爷拄拐压场并威胁林刚 | no | reuse existing base character |
| EP25_USE_CHAR_004 | CHAR_POLICE_BASE | STATE_GANGYI_DRIVERS_V1 | character | asset_bible | 第4组5-10秒，第5组0-13秒 | 刚毅车队退伍汽车兵和退伍兵甲群像 | no | reuse existing driver crowd proxy |
| EP25_USE_CHAR_005 | CHAR_LAOCUNZHANG_BASE | BASE | character | asset_bible | 第9组2-11秒，第10组0-11秒，第11组0-11秒，第12组0-11秒，第13组0-11秒，第14组0-7秒 | 老村长认出林刚并转交村民心意 | no | reuse existing base character |
| EP25_USE_CHAR_006 | CHAR_LISHEN_BASE | BASE | character | asset_bible | 第15组8-10秒，第16组组首空间锁定 | 李婶在新路旁认出林刚心意 | no | reuse existing base character |
| EP25_USE_SCENE_001 | SCENE_TIANBA_PARK_BASE | STATE_SCENE_TIANBA_PARK_DAY_TRUCKS_V1 | scene | episode_variant | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | 天霸物流园白天广场与成排重卡背景 | conditional | if state not generated |
| EP25_USE_SCENE_002 | SCENE_VILLAGE_ROAD_BASE | STATE_SCENE_VILLAGE_ROAD_NIGHT_REPAIR_V1 | scene | episode_variant | 第6组0-12秒，第7组0-12秒，第8组0-10秒，第9组0-11秒，第10组0-11秒，第11组0-11秒，第12组0-11秒，第13组0-11秒，第14组0-10秒 | 夜间村口土路修路现场 | conditional | if state not generated |
| EP25_USE_SCENE_003 | SCENE_VILLAGE_ROAD_BASE | STATE_SCENE_VILLAGE_ROAD_REPAIRED_DAY_V1 | scene | episode_variant | 第15组0-10秒，第16组0-8秒 | 三天后修好的村口柏油路 | conditional | if state not generated |
| EP25_USE_PROP_001 | PROP_CONTRACT_BASE | STATE_PROP_CONTRACT_SIGNED_V1 | prop | asset_bible | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | 林刚手中用于合法接管园区的合同 | no | reuse signed contract state |
| EP25_USE_PROP_002 | PROP_CRACKED_PHONE_BASE | BASE | prop | asset_bible | 第4组0-5秒，第5组组首空间锁定 | 林刚发送语音召集车队的手机 | no | reuse phone base without cracked state |
| EP25_USE_PROP_003 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第1组0-10秒，第3组0-10秒，第4组5-10秒，第5组0-13秒 | 天霸园区和刚毅车队的重卡阵列 | no | reuse heavy truck base |
| EP25_USE_PROP_004 | VEHICLE_PICKUP_BASE | BASE | prop | asset_bible | 第6组0-12秒，第7组0-12秒，第8组0-10秒，第9组0-11秒，第14组0-5秒，第16组8-13秒 | 林刚匿名夜修路和远处山梁离开的无牌皮卡 | no | reuse pickup base with no readable plate |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_TIANBA_PARK_DAY_TRUCKS_V1 | SCENE_TIANBA_PARK_BASE | BASE | scene | scene_condition | 天霸物流园白天广场停满重卡，水泥地硬光清楚 | 日景晴天，广场重卡密集，车辆阴影，园区压迫感 | episode_range | ep25 | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | yes | generate new scene state | candidate | 天霸物流园广场空镜，白天晴朗硬光，水泥地开阔，成排大型重卡整齐停放，车头朝向广场中央，地面有胎印和浅尘，工业园区大门与仓库轮廓清楚，无人无人脸，竖屏电影质感，真实物流园比例 | 人物，人脸，人群，品牌logo，可读车牌，字幕，水印，卡通，3D渲染，过曝，低清，畸变 | Empty shot of Tianba logistics park plaza in clear daytime hard light, wide concrete yard, rows of heavy trucks parked toward the center, tire marks and light dust on the ground, gate and warehouse silhouettes visible, no people, no faces, vertical cinematic live action realism | people, faces, crowds, brand logos, readable plates, subtitles, watermark, cartoon, 3D render, overexposure, low resolution, distortion |
| STATE_LINGANG_MASKED_NIGHT_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | costume_change | 林刚夜间匿名修路时戴帽子和口罩，仍穿旧深色外套 | 帽子，口罩，夜间匿名伪装，皮卡车灯照明 | one_episode | ep25 | 第6组0-12秒，第7组0-12秒，第8组0-10秒，第9组0-11秒，第10组0-11秒，第11组0-11秒，第12组0-11秒，第13组0-11秒，第14组0-3秒 | yes | generate one episode disguise state | no | 基于CHAR_LINGANG_BASE和COSTUME_LINGANG_WORK_JACKET_V1，林刚夜间匿名状态，深色旧工装外套，戴低檐帽和口罩遮住下半张脸，眼神沉稳克制，皮卡车灯形成侧逆光，真实中国乡村夜路环境，竖屏电影剧照质感 | 西方人脸，改变脸型，改变发型，夸张英雄服装，品牌logo，可读文字，字幕，卡通，3D渲染，塑料感，低清 | Based on CHAR_LINGANG_BASE and COSTUME_LINGANG_WORK_JACKET_V1, Lin Gang in anonymous night state, old dark work jacket, low brim cap and face mask covering the lower face, restrained steady eyes, pickup headlights as side backlight, realistic Chinese rural night road, vertical cinematic still | western face, changed facial structure, changed hairstyle, superhero costume, brand logo, readable text, subtitles, cartoon, 3D render, plastic look, low resolution |
| STATE_SCENE_VILLAGE_ROAD_NIGHT_REPAIR_V1 | SCENE_VILLAGE_ROAD_BASE | BASE | scene | scene_condition | 村口坑洼土路夜间修路前后，皮卡和工程车灯照出泥坑砂石 | 夜景晴天，坑洼泥路，车灯光束，砂石沥青施工物料 | episode_range | ep25 | 第6组0-12秒，第7组0-12秒，第8组0-10秒，第9组0-11秒，第10组0-11秒，第11组0-11秒，第12组0-11秒，第13组0-11秒，第14组0-10秒 | yes | generate night road repair state | candidate | 村口土路夜间空镜，坑洼泥路和破碎路沿延伸到远处，低处车灯照亮泥坑碎石，几辆工程车灯光在远处形成交错光束，砂石和沥青物料停在路边，无人无人脸，真实乡村施工夜景，竖屏电影质感 | 人物，人脸，人群，施工队正脸，可读标语，品牌logo，车牌号，字幕，水印，卡通，3D渲染，过曝 | Empty night shot of a rural village road, muddy potholes and broken road edges stretching into depth, low vehicle headlights revealing stones and ruts, construction truck beams crossing in the distance, gravel and asphalt materials by the roadside, no people, no faces, realistic rural roadwork night, vertical cinematic realism | people, faces, crowd, readable signs, brand logos, license plates, subtitles, watermark, cartoon, 3D render, overexposure |
| STATE_SCENE_VILLAGE_ROAD_REPAIRED_DAY_V1 | SCENE_VILLAGE_ROAD_BASE | STATE_SCENE_VILLAGE_ROAD_NIGHT_REPAIR_V1 | scene | scene_condition | 三天后村口土路变成崭新柏油路，路面向山外延伸 | 崭新柏油路，日景晴天，施工新痕，路碑旁边 | episode_range | ep25 | 第15组0-10秒，第16组0-8秒 | yes | generate repaired road state | candidate | 村口修好后的柏油路空镜，白天晴朗日光，崭新黑色路面从村口延伸到山外，路边泥土保留施工新痕，细小沥青颗粒有真实反光，低矮民房和远山虚化，无人无人脸，竖屏电影质感 | 人物，人脸，围观村民，可读多余文字，品牌logo，车牌号，字幕，水印，卡通，3D渲染，过曝 | Empty shot of a newly paved asphalt road at a village entrance, clear daytime sunlight, fresh black road stretching toward the mountains, new construction marks on roadside soil, tiny asphalt grains catching realistic highlights, low houses and distant hills softly blurred, no people, no faces, vertical cinematic realism | people, faces, villagers, extra readable text, brand logos, license plates, subtitles, watermark, cartoon, 3D render, overexposure |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_FOREMAN_BASE | character | 修路工头 | 夜间修路施工队负责人，成年男性，普通施工管理者体态，穿耐脏工装或反光背心，神情谨慎听命 | one_episode | ep25 | no | 中国乡村修路工头，成年男性，中等身材，穿耐脏深色工装和反光背心，安全帽可选，皮肤有户外劳动痕迹，神情谨慎务实，夜间车灯照明，真人实拍电影质感 | 西方人脸，夸张反派脸，品牌logo，可读文字，字幕，卡通，3D渲染，塑料感，低清 | Chinese rural roadwork foreman, adult male with average build, dark practical workwear and reflective vest, optional hard hat, weathered outdoor complexion, cautious pragmatic expression, lit by vehicle headlights at night, live action cinematic realism | western face, exaggerated villain face, brand logo, readable text, subtitles, cartoon, 3D render, plastic look, low resolution |
| CHAR_CONSTRUCTION_CREW_BASE | character | 修路施工队群像 | 夜间村口修路的施工队群像，不固定具体脸，穿工装反光背心，围绕工程车和路面作业 | one_episode | ep25 | no | 中国乡村道路施工队群像，成年工人，深色工装与反光背心，劳保鞋，围绕工程车和道路物料待命，夜间车灯和手电交错照明，不固定具体脸，真人实拍电影质感 | 清晰固定个人脸，西方人脸，品牌logo，可读文字，字幕，卡通，3D渲染，塑料感，低清 | Chinese rural road construction crew, adult workers in dark workwear and reflective vests, safety shoes, waiting around construction vehicles and road materials, crossed headlights and flashlight beams at night, no fixed individual faces, live action cinematic realism | clear fixed individual faces, western faces, brand logo, readable text, subtitles, cartoon, 3D render, plastic look, low resolution |
| VEHICLE_CONSTRUCTION_TRUCK_BASE | prop | 工程车 | 夜间修路用工程车，可装砂石和沥青，车灯强，车身无品牌无车牌文字 | one_episode | ep25 | no | 乡村道路施工工程车，车厢装满砂石和沥青物料，粗重轮胎，车身有尘土和施工磨损，夜间前灯明亮，真实比例，无品牌logo，无可读车牌 | 品牌logo，可读车牌，可读标语，人物正脸，字幕，水印，卡通，3D渲染，玩具感，低清 | Rural road construction truck loaded with gravel and asphalt materials, heavy tires, dusty worn body, bright headlights at night, realistic scale, no brand logo, no readable license plate | brand logo, readable license plate, readable slogan, front facing people, subtitles, watermark, cartoon, 3D render, toy look, low resolution |
| PROP_ROAD_MARKER_PASSERBY_BASE | prop | 过客留路碑 | 新修村口柏油路旁的路碑，碑面明确来自分镜的文字“过客留”，用于承载林刚匿名修路线索 | episode_range | ep25 | candidate | 村口新路旁的小型石质路碑，粗糙灰色石材，碑面刻着“过客留”三个中文，字迹简洁清楚但不添加其他文字，晴天侧光，柏油路边施工新痕，真实乡村纪念碑比例 | 多余文字，错字，品牌logo，二维码，人脸，字幕，水印，卡通，3D渲染，过度花纹 | Small stone road marker beside a newly paved village road, rough gray stone, the Chinese characters 过客留 carved on the face, simple clear lettering with no extra text, daytime side light, fresh construction marks near asphalt, realistic rural marker scale | extra text, wrong characters, brand logo, QR code, faces, subtitles, watermark, cartoon, 3D render, excessive ornament |
| PROP_RED_CLOTH_MONEY_BASE | prop | 红布包与零钱 | 老村长转交的皱巴巴红布包，里面是一沓卷边零钱，属于本集情感道具 | one_episode | ep25 | no | 皱巴巴的红布包被双手托开，里面露出一沓卷边旧零钱，红布纤维粗糙，纸币只呈现模糊面值感不过分清晰，夜间车灯侧光，真实手持比例 | 可读完整钞票编号，新增文字，品牌logo，字幕，水印，卡通，3D渲染，塑料感，低清 | Wrinkled red cloth bundle opened in hands, a stack of worn curled small banknotes inside, coarse red fabric fibers, banknotes only loosely readable without precise serial details, side headlight at night, realistic hand held scale | readable full banknote serial numbers, added text, brand logo, subtitles, watermark, cartoon, 3D render, plastic look, low resolution |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_TIANBA_PARK_DAY_TRUCKS_V1 | SCENE_TIANBA_PARK_BASE | scene | 天霸物流园白天广场重卡密集停放 | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-10秒，第5组0-13秒 | yes | scene state first appears in ep25 | 建议同步到asset_bible |
| STATE_LINGANG_MASKED_NIGHT_V1 | CHAR_LINGANG_BASE | character | 林刚戴帽子口罩匿名修路 | 第6组0-12秒至第14组0-3秒 | yes | one episode disguise state | 仅本集使用 |
| STATE_SCENE_VILLAGE_ROAD_NIGHT_REPAIR_V1 | SCENE_VILLAGE_ROAD_BASE | scene | 村口坑洼土路夜间施工状态 | 第6组0-12秒至第14组0-10秒 | yes | night roadwork state first appears in ep25 | 建议同步到asset_bible |
| STATE_SCENE_VILLAGE_ROAD_REPAIRED_DAY_V1 | SCENE_VILLAGE_ROAD_BASE | scene | 修好的村口柏油路白天状态 | 第15组0-10秒，第16组0-8秒 | yes | repaired road state first appears in ep25 | 建议同步到asset_bible |
| PROP_ROAD_MARKER_PASSERBY_BASE | PROP_ROAD_MARKER_PASSERBY_BASE | prop | 写有“过客留”的路碑 | 第15组4-10秒，第16组组首空间锁定 | yes | plot marker prop first appears in ep25 | 建议同步到asset_bible |
| PROP_RED_CLOTH_MONEY_BASE | PROP_RED_CLOTH_MONEY_BASE | prop | 村民凑钱的红布包零钱 | 第12组5-11秒，第13组0-11秒，第14组0-7秒 | yes | emotional one episode prop | 仅本集使用 |
| VEHICLE_CONSTRUCTION_TRUCK_BASE | VEHICLE_CONSTRUCTION_TRUCK_BASE | prop | 装砂石和沥青的修路工程车 | 第7组0-12秒，第8组0-10秒，第9组组首空间锁定，第14组7-10秒 | yes | construction vehicle for road repair | 仅本集使用 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 林刚、秦爷、陈天霸的短暂怒视和冷笑 | 第1组至第5组对话镜头 | 属于表演瞬间，不是可复用人物状态 |
| 司机们脱下制服甩到地上 | 第3组0-3秒 | 一次性群体动作，制服本身不作为跨集服装资产新增 |
| 林刚发送语音的手机界面 | 第4组0-5秒 | 属于一次性屏幕操作，且不应生成可读界面文字 |
| 帽子、口罩单件物品 | 第6组至第14组 | 已并入林刚匿名人物状态，无需拆成独立道具 |
| 普通香烟 | 第10组0-11秒，第11组组首空间锁定 | 小型一次性情感动作道具，无跨集稳定生成价值 |
| 工具和普通施工杂物 | 第14组7-10秒 | 由夜间修路场景状态承载，不逐项入库 |
| 村民甲乙丙丁和临时围观村民 | 第15组，第16组 | 临时群众群像，不固定具体脸，不作为跨集人物资产 |
