# 《刚毅物流 ep09》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP09_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_SNOW_WORK_V1 | character | episode_variant | 第1组0-12秒，第2组0-13秒，第3组0-10秒，第4组0-11秒 | 林刚驾驶防滑皮卡、冲坡、遇断桥、下车取钢缆 | conditional | if snow work state not merged |
| EP09_USE_CHAR_002 | CHAR_COUNTY_DRIVER_BASE | BASE | character | episode_new | 第1组3-10秒，第2组9-13秒 | 县城司机站在冷链大货车旁嘲讽和目送皮卡冲坡 | yes | new visible one episode driver |
| EP09_USE_SCENE_001 | SCENE_MOUNTAIN_ROAD_BASE | STATE_SCENE_MOUNTAIN_SNOW_V1 | scene | asset_bible | 第1组0-12秒，第2组0-13秒 | 大雪盘山公路上坡路段、雪坑、堵车和冲坡 | no | reuse existing snowy mountain road state |
| EP09_USE_SCENE_002 | SCENE_OLD_BRIDGE_BASE | STATE_SCENE_OLD_BRIDGE_SNOW_BLOCKED_V1 | scene | episode_new | 第3组0-10秒，第4组0-11秒 | 老桥入口、断树堵死桥面、右侧深渊和皮卡停靠 | yes | new blocked old bridge scene |
| EP09_USE_PROP_001 | VEHICLE_PICKUP_BASE | STATE_PICKUP_ANTISKID_SNOW_V1 | prop | episode_variant | 第1组0-12秒，第2组0-13秒，第3组0-10秒，第4组0-11秒 | 林刚改装重型防滑皮卡疾驰、冲坡、刹在断桥前 | yes | upgraded snowy pickup state |
| EP09_USE_PROP_002 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_COLD_CHAIN_TRUCK_STUCK_SNOW_V1 | prop | episode_variant | 第1组0-10秒，第2组6-13秒 | 十几辆冷链大货车陷在雪坑，轮胎空转堵路 | yes | cold chain truck stuck state |
| EP09_USE_PROP_003 | PROP_ANTI_SKID_CHAIN_BASE | BASE | prop | episode_new | 第2组3-6秒 | 皮卡轮胎特制防滑链咬住冰面 | yes | key close-up prop |
| EP09_USE_PROP_004 | PROP_TOW_CABLE_BASE | STATE_PROP_TOW_CABLE_SNOWY_V1 | prop | episode_new | 第4组8-11秒 | 林刚从后备箱扯出沉重牵引钢缆 | yes | key rescue prop |
| EP09_USE_PROP_005 | PROP_WRISTWATCH_BASE | STATE_PROP_WRISTWATCH_WET_COUNTDOWN_V1 | prop | episode_new | 第3组7-10秒，第4组0-2秒 | 林刚低头看手表，表达交货倒计时 | yes | one episode time pressure prop |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_PICKUP_ANTISKID_SNOW_V1 | VEHICLE_PICKUP_BASE | STATE_PICKUP_SNOW_DRIVING_V1 | prop | prop_condition | 重型防滑皮卡雪路冲坡状态，轮胎装特制防滑链，车身带雪泥 | anti_skid_chain，snow_mud，heavy_winter_driving，headlights | episode_range | ep09 | 第1组0-12秒，第2组0-13秒，第3组0-10秒，第4组0-11秒 | yes | likely important for snowy delivery run | candidate | 深色实用皮卡基于 VEHICLE_PICKUP_BASE，雪路防滑改装状态，轮胎安装金属防滑链，车身沾雪泥，车灯穿过雪雾，车辆厚重但不夸张，无品牌logo无可读车牌，现代现实物流短剧，竖屏电影质感 | 可读车牌，品牌logo，赛车涂装，科幻改装，人物脸部，卡通，3D渲染，水印，字幕 | Dark utility pickup based on VEHICLE_PICKUP_BASE in snowy anti-skid setup, metal tire chains installed, snow mud on body, headlights cutting through snow haze, heavy but realistic vehicle presence, no brand logo or readable license plate, modern realistic logistics drama, vertical cinematic texture | Readable license plate, brand logo, racing livery, sci-fi modification, facial close-up, cartoon, 3D render, watermark, subtitles |
| STATE_VEHICLE_COLD_CHAIN_TRUCK_STUCK_SNOW_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 冷链大货车陷雪坑堵路状态，轮胎空转冒白烟，车身堵住上坡路 | refrigerated_cargo_box，stuck_in_snow，wheel_spin，road_block | one_episode | ep09 | 第1组0-10秒，第2组6-13秒 | yes | convoy obstacle state | no | 大型冷链货车基于 VEHICLE_HEAVY_TRUCK_BASE，白色或浅灰冷藏货箱，陷在上坡雪坑里，轮胎空转卷起雪沫和白烟，车身斜停堵住山路，无品牌logo无可读车牌，真实物流堵车现场 | 可读车牌，真实品牌logo，夸张爆炸，人物脸部，卡通，3D渲染，水印，字幕 | Large cold chain truck based on VEHICLE_HEAVY_TRUCK_BASE, white or light gray refrigerated cargo box, stuck in an uphill snow pit, tires spinning with snow spray and white vapor, body angled and blocking mountain road, no brand logo or readable license plate, realistic logistics traffic scene | Readable license plate, real brand logo, exaggerated explosion, facial close-up, cartoon, 3D render, watermark, subtitles |
| STATE_SCENE_OLD_BRIDGE_SNOW_BLOCKED_V1 | SCENE_OLD_BRIDGE_BASE | BASE | scene | scene_condition | 大雪老桥入口被腰粗断树堵死，桥右侧是深渊，皮卡无法前进 | fallen_tree，snow_cover，cliff_edge，blocked_bridge | episode_range | ep09 | 第3组0-10秒，第4组0-11秒 | yes | new repeated blocked bridge state | candidate | 大雪中的老桥入口空镜，积雪覆盖桥面，一棵腰粗断树横倒压在桥面入口，右侧桥边外露陡直深渊，路面有刹车湿雪痕迹，阴天雪光和车灯边光，无人无人脸，竖屏电影构图 | 人物，人脸，车辆品牌，清晰路牌文字，卡通，3D渲染，古装，水印，字幕，过度灾难化断桥 | Empty old bridge entrance in heavy snow, snow-covered bridge deck blocked by a thick fallen tree across the entrance, steep ravine visible beyond the right bridge edge, wet snow brake marks on road, overcast snow light and vehicle headlight edge light, no people or faces, vertical cinematic framing | People, faces, vehicle brand, readable road sign text, cartoon, 3D render, historical costume, watermark, subtitles, exaggerated disaster bridge collapse |
| STATE_PROP_TOW_CABLE_SNOWY_V1 | PROP_TOW_CABLE_BASE | BASE | prop | prop_condition | 牵引钢缆沾满雪渣，刚从皮卡后备箱拖出 | snow_clumps，metal_cable，trunk_context | episode_range | ep09 | 第4组8-11秒 | yes | useful for vehicle rescue sequence | candidate | 沉重牵引钢缆道具，粗金属编织缆绳从皮卡后备箱拖出，表面沾满雪渣和湿冷高光，缆绳末端有金属挂钩，真实车辆救援比例，无品牌logo无可读文字 | 品牌logo，可读标签，人物脸部，塑料绳，科幻设备，卡通，3D渲染，水印，字幕 | Heavy tow cable prop, thick braided metal cable pulled from pickup trunk, snow clumps and wet cold highlights on surface, metal hook at cable end, realistic vehicle rescue scale, no brand logo or readable text | Brand logo, readable label, facial close-up, plastic rope, sci-fi device, cartoon, 3D render, watermark, subtitles |
| STATE_PROP_WRISTWATCH_WET_COUNTDOWN_V1 | PROP_WRISTWATCH_BASE | BASE | prop | prop_condition | 林刚手表沾融雪水，秒针走动，强调交货时间紧迫 | wet_glass，moving_second_hand，no_brand，wrist_closeup | one_episode | ep09 | 第3组7-10秒，第4组0-2秒 | yes | one episode countdown insert | no | 普通男士手表道具，戴在手腕上，表盘玻璃边缘有融化雪水，秒针清楚但没有可读品牌文字，冷白雪光和仪表盘微蓝反光，真实手部比例，紧迫感特写 | 品牌logo，可读品牌名，数字文字特写过清，奢侈珠宝感，卡通，3D渲染，水印，字幕 | Ordinary men's wristwatch prop worn on a wrist, melted snow water on glass edge, clear second hand but no readable brand text, cold snow light and faint blue dashboard reflection, realistic hand scale, urgent close-up mood | Brand logo, readable brand name, overly readable text close-up, luxury jewelry look, cartoon, 3D render, watermark, subtitles |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_COUNTY_DRIVER_BASE | character | 县城司机 | 县城冷链货车司机，普通成年男性，站在货车旁提醒和嘲讽林刚，本集可见配角 | one_episode | ep09 | no | 中国县城货车司机，30到40多岁男性，普通身材，短发，穿厚外套或物流司机棉服，脸上有雪路堵车后的焦躁和自以为是，真实短剧配角定妆，竖屏电影质感 | 西方人面孔，夸张反派妆，制服警服，品牌logo，可读文字，卡通，3D渲染，水印，字幕 | Chinese county truck driver, male in his 30s to 40s, average build, short hair, thick jacket or logistics driver winter coat, irritated and smug from snowy traffic jam, realistic short drama supporting character reference, vertical cinematic texture | Western face, exaggerated villain makeup, police uniform, brand logo, readable text, cartoon, 3D render, watermark, subtitles |
| SCENE_OLD_BRIDGE_BASE | scene | 老桥前 | 山区老桥入口，桥面、护栏、桥边深渊和山路连接处构成基础空镜 | episode_range | ep09 | candidate | 中国山区老桥入口空镜，窄桥面、旧护栏、山路连接处和桥边深渊，沥青与旧混凝土材质，冬天阴雪自然光，无人无人脸，真实道路比例，竖屏电影构图 | 人物，人脸，车辆品牌，可读路牌，城市高架桥，卡通，3D渲染，水印，字幕 | Empty entrance to an old mountain bridge in China, narrow bridge deck, worn guardrails, road connection and ravine beside bridge, asphalt and old concrete materials, winter overcast snowy natural light, no people or faces, realistic road scale, vertical cinematic framing | People, faces, vehicle brand, readable road signs, urban overpass, cartoon, 3D render, watermark, subtitles |
| PROP_ANTI_SKID_CHAIN_BASE | prop | 特制防滑链 | 安装在皮卡轮胎上的金属防滑链，近景可见铁链咬冰面 | episode_range | ep09 | candidate | 汽车轮胎金属防滑链道具，粗铁链环绕轮胎胎面，链节压进冰雪，碎冰和雪浆挤出，金属冷光清楚，真实车辆比例，无品牌logo无可读文字 | 品牌logo，可读标签，玩具车比例，科幻轮胎，人物，人脸，卡通，3D渲染，水印，字幕 | Metal tire chain prop for a vehicle wheel, thick chain links wrapped around tire tread, links biting into ice and snow with crushed ice and slush, clear cold metal highlights, realistic vehicle scale, no brand logo or readable text | Brand logo, readable label, toy car scale, sci-fi tire, people, faces, cartoon, 3D render, watermark, subtitles |
| PROP_TOW_CABLE_BASE | prop | 牵引钢缆 | 车辆救援用粗金属钢缆，带挂钩，适合拖拽断树或车辆救援 | episode_range | ep09 | candidate | 车辆救援牵引钢缆道具，粗金属编织缆绳，末端有重型挂钩，表面有磨损和湿冷反光，真实工程救援比例，无品牌logo无可读文字 | 品牌logo，可读标签，塑料绳，科幻设备，人物，人脸，卡通，3D渲染，水印，字幕 | Vehicle rescue tow cable prop, thick braided metal cable with heavy hook at the end, worn surface and wet cold reflections, realistic engineering rescue scale, no brand logo or readable text | Brand logo, readable label, plastic rope, sci-fi equipment, people, faces, cartoon, 3D render, watermark, subtitles |
| PROP_WRISTWATCH_BASE | prop | 林刚手表 | 普通男士腕表，作为时间压力特写道具，不显示品牌 | one_episode | ep09 | no | 普通男士腕表道具，简洁深色表带，圆形表盘，表玻璃有轻微磨损和冷光反射，手腕比例真实，无品牌logo无可读品牌文字 | 品牌logo，可读品牌名，奢侈珠宝广告感，科幻表盘，卡通，3D渲染，水印，字幕 | Ordinary men's wristwatch prop, simple dark strap, round dial, slight wear and cold reflections on glass, realistic wrist scale, no brand logo or readable brand text | Brand logo, readable brand name, luxury jewelry advertising look, sci-fi dial, cartoon, 3D render, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_MOUNTAIN_SNOW_V1 | SCENE_MOUNTAIN_ROAD_BASE | scene | 复用雪天盘山公路上坡堵车空间 | 第1组0-12秒，第2组0-13秒 | no | existing bible state | 复用已有状态 |
| STATE_PICKUP_ANTISKID_SNOW_V1 | VEHICLE_PICKUP_BASE | prop | 皮卡装防滑链冲坡的雪路状态 | 第1组0-12秒，第2组0-13秒，第3组0-10秒，第4组0-11秒 | yes | upgraded pickup state for delivery run | 建议同步到asset_bible |
| STATE_VEHICLE_COLD_CHAIN_TRUCK_STUCK_SNOW_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 冷链大货车陷在雪坑、轮胎空转堵路 | 第1组0-10秒，第2组6-13秒 | yes | one episode obstacle convoy | 仅本集使用 |
| STATE_SCENE_OLD_BRIDGE_SNOW_BLOCKED_V1 | SCENE_OLD_BRIDGE_BASE | scene | 老桥入口被断树堵死、右侧深渊 | 第3组0-10秒，第4组0-11秒 | yes | new blocked bridge environment | 建议同步到asset_bible |
| BASE | PROP_ANTI_SKID_CHAIN_BASE | prop | 皮卡轮胎金属防滑链基础道具 | 第2组3-6秒 | yes | key vehicle close-up | 建议同步到asset_bible |
| STATE_PROP_TOW_CABLE_SNOWY_V1 | PROP_TOW_CABLE_BASE | prop | 牵引钢缆从后备箱拖出且沾雪渣 | 第4组8-11秒 | yes | rescue prop state | 建议同步到asset_bible |
| STATE_PROP_WRISTWATCH_WET_COUNTDOWN_V1 | PROP_WRISTWATCH_BASE | prop | 手表沾雪水、秒针走动的倒计时特写 | 第3组7-10秒，第4组0-2秒 | yes | one episode countdown insert | 仅本集使用 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 车窗升降和方向盘手指动作 | 第1组3-12秒，第3组5-7秒 | 属于车辆内表演和操作细节，由车辆状态即时生成即可 |
| 货车司机们的雪雾背景身影 | 第2组6-9秒 | 临时背景群像，不固定角色资产 |
| 断树树皮细节 | 第3组3-5秒，第4组0-11秒 | 已由老桥雪堵场景状态承载，不单独入库为道具 |
| 车门和后备箱边缘 | 第4组2-11秒 | 普通车辆部件，由皮卡车辆状态承载 |
| 林刚咬牙、砸方向盘、握紧手指 | 第3组5-10秒，第4组0-2秒 | 短暂表演动作和情绪，不是可复用资产状态 |
