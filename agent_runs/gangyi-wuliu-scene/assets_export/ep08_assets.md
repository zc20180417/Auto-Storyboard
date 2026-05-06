# 《刚毅物流 ep08》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP08_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_SNOW_WORK_V1 | character | episode_variant | 第1组0-11秒，第2组0-12秒，第3组0-10秒，第4组0-10秒，第5组0-12秒 | 林刚雪天守门、喷水结冰、接电话后驾驶皮卡出车 | conditional | if ep07 snow work state not merged |
| EP08_USE_CHAR_002 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | 第1组0-11秒，第2组8-12秒，第3组0-13秒 | 赵大强带村民逼赔抢钥匙、被冰面逼退 | no | reuse existing villain state |
| EP08_USE_CHAR_003 | CHAR_VILLAGER_CROWD_BASE | BASE | character | episode_new | 第1组0-11秒，第2组2-12秒，第3组0-13秒 | 门外村民群像冲门、摔倒、退走 | yes | new crowd base if not already generated |
| EP08_USE_SCENE_001 | SCENE_LINGANG_HOME_GATE_BASE | STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | scene | episode_new | 第1组0-11秒，第2组0-12秒，第3组0-13秒 | 林刚家院门外雪天冲突空间 | yes | new home gate scene if not merged |
| EP08_USE_SCENE_002 | SCENE_LINGANG_HOME_COURTYARD_BASE | STATE_SCENE_LINGANG_HOME_COURTYARD_SNOW_V1 | scene | episode_new | 第4组0-3秒，第5组10-12秒 | 林刚家院内雪地、屋门到皮卡、皮卡冲出院门 | yes | new courtyard scene |
| EP08_USE_PROP_001 | PROP_HIGH_PRESSURE_WASHER_BASE | STATE_PROP_HIGH_PRESSURE_WASHER_SPRAYING_V1 | prop | episode_variant | 第1组4-11秒，第2组0-2秒，第3组0-7秒，第4组0-3秒 | 高压水枪喷向院门前泥地并被林刚收回扔下 | conditional | if water gun base not merged |
| EP08_USE_PROP_002 | VEHICLE_PICKUP_BASE | STATE_PICKUP_SNOW_DRIVING_V1 | prop | episode_variant | 第4组0-10秒，第5组0-12秒 | 林刚坐进皮卡、发动、离开院子去送货 | conditional | if snow pickup state not generated |
| EP08_USE_PROP_003 | PROP_CRACKED_PHONE_BASE | STATE_PROP_PHONE_ACTIVE_CALL_V1 | prop | episode_variant | 第4组3-10秒，第5组0-8秒 | 林刚手机接到刘福断供电话和二十万悬赏 | conditional | generate call state only if needed |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_LINGANG_HOME_GATE_ICE_V1 | SCENE_LINGANG_HOME_GATE_BASE | STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | scene | scene_condition | 院门前雪泥被高压水枪浇成薄冰，冰面贴着泥地向外铺开 | thin_ice，wet_mud，sprayed_water，cold_daylight | episode_range | ep08 | 第2组0-12秒，第3组0-13秒 | yes | useful for the gate conflict aftermath | candidate | 林刚家院门外雪天空镜，门前泥地和雪水被浇出一层发亮薄冰，冰面边缘贴着泥土和脚印向外铺开，大铁门和旧院墙在冷白阴雪光中，无人无人脸，真实乡镇院落，竖屏电影构图 | 人物，人脸，摔倒人群，卡通，3D渲染，过度镜面冰场，品牌logo，可读文字，水印，字幕 | Empty snowy exterior of Lin Gang home gate, muddy snow before the gate covered by a thin shiny ice sheet spreading over footprints, large iron gate and old courtyard wall in cold overcast snow light, no people or faces, realistic township courtyard, vertical cinematic framing | People, faces, falling crowd, cartoon, 3D render, exaggerated ice rink, brand logo, readable text, watermark, subtitles |
| STATE_SCENE_LINGANG_HOME_COURTYARD_SNOW_V1 | SCENE_LINGANG_HOME_COURTYARD_BASE | BASE | scene | scene_condition | 林刚家院内雪天状态，屋门、雪地、停放皮卡和院门通道清楚 | snow_cover，parked_pickup_space，courtyard_path，cold_light | episode_range | ep08 | 第4组0-3秒，第5组10-12秒 | yes | courtyard and pickup staging may recur | candidate | 林刚家院内雪天空镜，普通乡镇院子，屋门到院门之间有被踩乱的雪地，右侧可留出皮卡停放位置，院墙和大铁门构成出口方向，冷白雪天自然光，无人无人脸，写实电影质感 | 人物，人脸，豪宅，城市车库，品牌logo，可读文字，卡通，3D渲染，水印，字幕 | Empty snowy courtyard of Lin Gang home, ordinary township yard, trampled snow path from house door to gate, space for a pickup on the right, courtyard wall and large iron gate forming exit direction, cold natural snowy light, no people or faces, realistic cinematic texture | People, faces, mansion, urban garage, brand logo, readable text, cartoon, 3D render, watermark, subtitles |
| STATE_PROP_HIGH_PRESSURE_WASHER_SPRAYING_V1 | PROP_HIGH_PRESSURE_WASHER_BASE | BASE | prop | prop_condition | 高压水枪喷水状态，水柱斜打泥地，枪口和金属接口有水珠 | spraying_water，wet_nozzle，black_hose | episode_range | ep08 | 第2组0-2秒，第3组0-7秒 | yes | active spraying state for ice scene | candidate | 高压洗车水枪基于 PROP_HIGH_PRESSURE_WASHER_BASE，黑色枪身和金属喷嘴清楚，喷出斜向高压水柱，接口和软管带水珠，冷白雪天反光，手持比例真实，无品牌logo无可读文字 | 品牌logo，可读标签，科幻武器，火焰，人物脸部，卡通，3D渲染，水印，字幕 | High pressure car wash gun based on PROP_HIGH_PRESSURE_WASHER_BASE, clear black body and metal nozzle, spraying a diagonal high pressure water jet, droplets on connector and hose, cold snowy reflections, realistic handheld scale, no brand logo or readable text | Brand logo, readable label, sci-fi weapon, flames, facial close-up, cartoon, 3D render, watermark, subtitles |
| STATE_PROP_PHONE_ACTIVE_CALL_V1 | PROP_CRACKED_PHONE_BASE | BASE | prop | prop_condition | 林刚手机通话状态，屏幕亮起但不显示可读文字，免提放在中控台 | screen_glow，active_call，no_readable_text，dashboard_context | one_episode | ep08 | 第4组3-10秒，第5组0-8秒 | yes | only for phone call closeups | no | 黑色智能手机基于 PROP_CRACKED_PHONE_BASE，放在皮卡中控台或贴近耳侧，屏幕亮起形成白光但没有可读文字，车内仪表盘冷光辅助，真实手持比例，无品牌logo | 可读电话号码，可读来电姓名，聊天文字，品牌logo，二维码，水印，字幕，卡通，3D渲染 | Black smartphone based on PROP_CRACKED_PHONE_BASE, on pickup center console or near ear, screen glowing white with no readable text, cool dashboard light in vehicle interior, realistic handheld scale, no brand logo | Readable phone number, readable caller name, chat text, brand logo, QR code, watermark, subtitles, cartoon, 3D render |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_VILLAGER_CROWD_BASE | character | 村民群像 | 十几个乡村村民群像，不固定单人脸，承载冲门、摔倒、退走的群众表演 | episode_range | ep08 | candidate | 中国乡村村民群像，成年男女混合，冬天深色棉衣和旧外套，体态普通，不固定单人脸，适合围堵院门和雪地混乱动作，真实短剧群众定妆，竖屏电影质感 | 固定明星脸，西方人面孔，统一制服，古装，卡通，3D渲染，品牌logo，可读文字，水印，字幕 | Chinese village crowd, mixed adult men and women, dark winter padded coats and worn jackets, ordinary body types, no fixed individual faces, suitable for gate crowding and snowy chaotic action, realistic short drama crowd reference, vertical cinematic style | Celebrity face, Western faces, uniforms, historical costume, cartoon, 3D render, brand logo, readable text, watermark, subtitles |
| SCENE_LINGANG_HOME_GATE_BASE | scene | 林刚家院门外 | 乡镇民宅院门外空间，核心是大铁门、旧院墙、门檐和门前泥地，基础资产为空镜 | episode_range | ep08 | candidate | 中国乡镇民宅院门外空镜，大铁门、旧院墙、门檐、门环、门前泥地和院内阴影层次，现代乡村住宅质感，冷天自然光，无人无人脸，竖屏电影构图 | 人物，人脸，围观群众，豪宅别墅，古装建筑，品牌logo，可读文字，卡通，3D渲染，水印，字幕 | Empty exterior of a Chinese township home gate, large iron gate, old courtyard wall, eaves, door ring, muddy ground and layered shadows inside, modern rural residence texture, cold natural light, no people or faces, vertical cinematic framing | People, faces, crowd, luxury villa, historical architecture, brand logo, readable text, cartoon, 3D render, watermark, subtitles |
| SCENE_LINGANG_HOME_COURTYARD_BASE | scene | 林刚家院内 | 林刚家普通乡镇院子，屋门、雪地、院墙、院门和皮卡停放位构成出车空间 | episode_range | ep08 | candidate | 中国乡镇民宅院内空镜，普通屋门、旧院墙、大铁门出口、院内泥地和皮卡停放空间，冬天自然冷光，现代农村生活质感，无人无人脸，竖屏电影构图 | 人物，人脸，豪宅，城市车库，古装建筑，品牌logo，可读文字，卡通，3D渲染，水印，字幕 | Empty courtyard inside a Chinese township home, ordinary house door, old courtyard wall, large iron gate exit, muddy yard ground and pickup parking space, winter cold natural light, modern rural texture, no people or faces, vertical cinematic framing | People, faces, mansion, urban garage, historical architecture, brand logo, readable text, cartoon, 3D render, watermark, subtitles |
| PROP_HIGH_PRESSURE_WASHER_BASE | prop | 高压洗车水枪 | 粗大的高压洗车水枪，黑色枪身、金属喷嘴、软管和水珠清楚 | episode_range | ep08 | candidate | 高压洗车水枪道具，粗黑枪身，金属喷嘴和接口，连接黑色高压软管，表面有水珠和冷光反射，手持比例真实，无品牌logo无可读文字 | 品牌logo，可读标签，玩具感，科幻武器，人物，人脸，卡通，3D渲染，水印，字幕 | High pressure car wash gun prop, thick black body, metal nozzle and connector, attached black high pressure hose, water droplets and cold reflections, realistic handheld scale, no brand logo or readable text | Brand logo, readable label, toy-like look, sci-fi weapon, people, faces, cartoon, 3D render, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_LINGANG_HOME_GATE_SNOW_V1 | SCENE_LINGANG_HOME_GATE_BASE | scene | 林刚家院门雪天冲突基础状态 | 第1组0-11秒，第2组0-12秒，第3组0-13秒 | yes | if not merged from ep07 | 建议同步到asset_bible |
| STATE_SCENE_LINGANG_HOME_GATE_ICE_V1 | SCENE_LINGANG_HOME_GATE_BASE | scene | 院门前泥地被水枪浇成薄冰 | 第2组0-12秒，第3组0-13秒 | yes | new ice aftermath state | 建议同步到asset_bible |
| STATE_SCENE_LINGANG_HOME_COURTYARD_SNOW_V1 | SCENE_LINGANG_HOME_COURTYARD_BASE | scene | 林刚家院内雪天皮卡出车空间 | 第4组0-3秒，第5组10-12秒 | yes | new courtyard state | 建议同步到asset_bible |
| STATE_PROP_HIGH_PRESSURE_WASHER_SPRAYING_V1 | PROP_HIGH_PRESSURE_WASHER_BASE | prop | 高压水枪喷水结冰状态 | 第2组0-2秒，第3组0-7秒 | yes | active prop state | 建议同步到asset_bible |
| STATE_PROP_PHONE_ACTIVE_CALL_V1 | PROP_CRACKED_PHONE_BASE | prop | 手机亮屏通话和免提状态 | 第4组3-10秒，第5组0-8秒 | yes | one episode phone call closeup | 仅本集使用 |
| STATE_PICKUP_SNOW_DRIVING_V1 | VEHICLE_PICKUP_BASE | prop | 皮卡雪天发动并冲出院门 | 第4组7-10秒，第5组8-12秒 | yes | if not merged from ep07 | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 院门本身的门框和门环细节 | 第1组0-11秒，第3组7-10秒 | 已由林刚家院门场景基础资产承载，不需要拆成独立道具 |
| 薄冰上的摔倒姿态 | 第2组2-12秒，第3组10-13秒 | 属于动作表演和镜头调度，不是可复用资产状态 |
| 车钥匙、离合、油门踏板、挡杆 | 第4组7-10秒，第5组0-10秒 | 普通车内部件，由皮卡车辆状态即时生成即可 |
| 手机来电界面文字 | 第4组3-10秒，第5组0-8秒 | final.txt 没有指定可读文字，资产提示词必须避免可读号码和姓名 |
| 刘福电话画外音 | 第4组5-7秒，第5组0-8秒 | 仅声音出现，没有可视人物造型依据，不建立人物基础资产 |
