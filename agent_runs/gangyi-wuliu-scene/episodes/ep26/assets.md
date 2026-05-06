# 《刚毅物流 ep26》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP26_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-11秒，第5组0-10秒 | 林刚在王氏中转站应对断油并指挥加油出发 | no | reuse existing convoy stage |
| EP26_USE_CHAR_002 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | 第1组0-10秒，第2组0-11秒，第3组0-10秒 | 王百川焦急说明出口电器上船时限 | no | reuse existing boss stage |
| EP26_USE_CHAR_003 | CHAR_QINYE_BASE | BASE | character | asset_bible | 第2组0-11秒电话画外音 | 秦爷通过电话逼迫王百川放弃林刚 | no | voice only, reuse base if needed for call context |
| EP26_USE_SCENE_001 | SCENE_WANG_TRANSFER_BASE | STATE_SCENE_WANG_TRANSFER_DAY_FUEL_WORK_V1 | scene | episode_variant | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-11秒，第5组0-10秒 | 王氏中转站外场重卡断油与临时加油作业 | conditional | if state not generated |
| EP26_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第1组0-10秒，第3组3-10秒，第4组0-11秒，第5组0-10秒 | 五十台满载重卡、第一辆重卡和第二辆重卡 | no | reuse heavy truck base |
| EP26_USE_PROP_002 | PROP_CRACKED_PHONE_BASE | BASE | prop | asset_bible | 第2组0-11秒，第3组0-3秒 | 王百川接听秦爷电话及林刚挂断电话 | no | reuse phone base without cracked state |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_WANG_TRANSFER_DAY_FUEL_WORK_V1 | SCENE_WANG_TRANSFER_BASE | BASE | scene | scene_condition | 王氏中转站日间外场停满待发重卡，并出现临时加油作业空间 | 晴天外场，重卡队列，出口道路，临时加油管线和油罐位置 | episode_range | ep26 | 第1组0-10秒，第2组0-11秒，第3组0-10秒，第4组0-11秒，第5组0-10秒 | yes | generate transfer station fuel work state | candidate | 王氏物流中转站外场空镜，白天晴朗自然光，钢架仓库和装卸平台旁停着多排大型重卡，出口道路清楚，地面有叉车痕迹和灰尘，第一辆重卡旁预留临时加油作业空间，油管可见但无人物无人脸，竖屏电影质感 | 人物，人脸，人群，品牌logo，可读车牌，可读标语，字幕，水印，卡通，3D渲染，过曝，低清 | Empty shot of Wang logistics transfer yard in clear daytime light, steel warehouse and loading platform with rows of heavy trucks, exit road visible, forklift marks and dust on the ground, temporary fueling work space near the first truck with hose visible, no people, no faces, vertical cinematic realism | people, faces, crowds, brand logos, readable plates, readable signage, subtitles, watermark, cartoon, 3D render, overexposure, low resolution |
| STATE_PROP_MOBILE_FUEL_TANK_MOUNTED_V1 | PROP_MOBILE_FUEL_TANK_BASE | BASE | prop | prop_condition | 军绿移动油罐固定在第一辆重卡车厢内，防水布掀开后暴露 | 车厢固定架，金属阀门，军绿色弧面，防水布被掀开 | episode_range | ep26 | 第3组3-10秒，第4组0-11秒 | yes | generate mounted oil tank state | candidate | 第一辆重卡车厢内的军绿色移动油罐，圆弧金属罐体被固定架牢牢固定，金属阀门和接口清楚，掀开的防水布垂在车厢边缘，晴天日光照出罐体弧面高光，无品牌无可读文字，真实工业运输道具比例 | 品牌logo，可读文字，可读车牌，人物正脸，危险夸张爆炸效果，字幕，水印，卡通，3D渲染，低清 | Military green mobile fuel tank mounted inside the first heavy truck cargo bed, curved metal tank secured by brackets, clear metal valves and connectors, pulled back waterproof tarp hanging over the side, daytime sunlight creating highlights on the tank, no brand, no readable text, realistic industrial transport prop scale | brand logo, readable text, readable license plate, front facing people, exaggerated explosion, subtitles, watermark, cartoon, 3D render, low resolution |
| STATE_PROP_FUEL_NOZZLE_IN_USE_V1 | PROP_FUEL_NOZZLE_HOSE_BASE | BASE | prop | prop_condition | 油枪和加油管从移动油罐拉出，插入第二辆重卡油箱口进行流水线加油 | 油枪插入油箱口，管线垂落地面，油泵作业 | one_episode | ep26 | 第4组0-11秒，第5组0-2秒 | yes | generate fueling prop state | no | 工业加油枪和粗黑加油管连接到大型重卡油箱口，油枪金属口插入油箱，管线从车厢方向垂到地面，晴天自然光下金属和橡胶材质清晰，无品牌logo，无可读文字，真实物流现场比例 | 品牌logo，可读文字，可读车牌，火焰，爆炸，人物正脸，字幕，水印，卡通，3D渲染，低清 | Industrial fuel nozzle and thick black fuel hose connected to a heavy truck fuel port, metal nozzle inserted into the tank, hose dropping from the truck bed to the ground, clear metal and rubber materials in daylight, no brand logo, no readable text, realistic logistics yard scale | brand logo, readable text, readable license plate, flames, explosion, front facing people, subtitles, watermark, cartoon, 3D render, low resolution |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| PROP_MOBILE_FUEL_TANK_BASE | prop | 军绿移动油罐 | 可装在重卡车厢内的定制移动油罐，军绿色金属罐体，带固定架、阀门和接口 | episode_range | ep26 | candidate | 定制军绿色移动油罐道具，圆弧金属罐体，粗壮固定架，金属阀门和接口，工业运输质感，适合放置在重卡车厢内，无品牌logo，无可读文字，真实比例 | 品牌logo，可读文字，车牌号，火焰，爆炸，人物，字幕，水印，卡通，3D渲染，玩具感 | Custom military green mobile fuel tank prop, curved metal body, heavy mounting brackets, metal valves and connectors, industrial transport texture, suitable inside a heavy truck cargo bed, no brand logo, no readable text, realistic scale | brand logo, readable text, license plate, fire, explosion, people, subtitles, watermark, cartoon, 3D render, toy look |
| PROP_FUEL_NOZZLE_HOSE_BASE | prop | 油枪与加油管 | 临时流水线加油使用的工业油枪、油管和接头组合，黑色橡胶管与金属油枪 | one_episode | ep26 | no | 工业加油枪和粗黑橡胶加油管道具，金属油枪口和阀门接头清楚，管身有使用磨损和油污痕迹，无品牌logo，无可读文字，真实手持和车辆比例 | 品牌logo，可读文字，火焰，爆炸，字幕，水印，卡通，3D渲染，塑料玩具感，低清 | Industrial fuel nozzle and thick black rubber hose prop, clear metal nozzle and valve connector, used hose surface with slight oil stains and wear, no brand logo, no readable text, realistic hand and vehicle scale | brand logo, readable text, flames, explosion, subtitles, watermark, cartoon, 3D render, plastic toy look, low resolution |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_WANG_TRANSFER_DAY_FUEL_WORK_V1 | SCENE_WANG_TRANSFER_BASE | scene | 王氏中转站外场断油与临时加油作业状态 | 第1组0-10秒至第5组0-10秒 | yes | scene state first appears in ep26 | 建议同步到asset_bible |
| PROP_MOBILE_FUEL_TANK_BASE | PROP_MOBILE_FUEL_TANK_BASE | prop | 林刚提前准备的军绿移动油罐基础道具 | 第3组6-10秒，第4组0-11秒 | yes | key plot prop first appears in ep26 | 建议同步到asset_bible |
| STATE_PROP_MOBILE_FUEL_TANK_MOUNTED_V1 | PROP_MOBILE_FUEL_TANK_BASE | prop | 移动油罐固定在重卡车厢并掀开防水布 | 第3组3-10秒，第4组0-11秒 | yes | mounted state first appears in ep26 | 建议同步到asset_bible |
| STATE_PROP_FUEL_NOZZLE_IN_USE_V1 | PROP_FUEL_NOZZLE_HOSE_BASE | prop | 油枪和加油管插入重卡油箱口作业 | 第4组0-11秒，第5组0-2秒 | yes | fueling state for this episode | 仅本集使用 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 油表红灯 | 第1组0-2秒 | 仪表盘一次性危机提示，不作为独立跨集道具资产 |
| 林刚手表 | 第1组8-10秒 | 普通随身小物，仅服务看时间动作，无需稳定入库 |
| 王百川额头冒汗和司机甲焦急表情 | 第1组2-8秒，第3组8-10秒 | 短暂表演状态，不是人物资产状态 |
| 防水布 | 第3组3-8秒 | 作为移动油罐暴露状态的一部分承载，不单独入库 |
| 柴油注入和油泵轰鸣 | 第4组8-11秒 | 动作与声音效果，不是静态资产 |
| 出发时卷起的灰尘 | 第5组5-10秒 | 运输动作环境效果，由场景即时生成 |
