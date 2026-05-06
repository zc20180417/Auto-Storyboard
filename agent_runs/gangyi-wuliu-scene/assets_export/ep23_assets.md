# 《刚毅物流ep23》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP23_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组0-9秒，第2组7-9秒，第3组7-14秒 | 林刚准时送达、开车厢验货并质疑陈天霸和李主任 | no | reuse existing character state |
| EP23_USE_CHAR_002 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | 第1组0-4秒，第3组4-7秒 | 王百川在医院月台确认货物安全并替林刚解释手续 | no | reuse existing character state |
| EP23_USE_CHAR_003 | CHAR_LIZHUREN_BASE | STATE_LIZHUREN_HOSPITAL_WHITE_COAT_V1 | character | episode_variant | 第1组9-12秒，第2组9-11秒，第3组0-14秒 | 李主任穿白大褂手持平板，在接收区拒收林刚货物 | conditional | if state not generated |
| EP23_USE_CHAR_004 | CHAR_CHENTIANBA_BASE | BASE | character | asset_bible | 第2组5-11秒，第3组7-14秒 | 陈天霸插队抢入库、递黑卡并嘲讽林刚 | no | reuse existing character base |
| EP23_USE_SCENE_001 | SCENE_HOSPITAL_RECEIVING_BASE | STATE_SCENE_HOSPITAL_RECEIVING_OVERCAST_COLDCHAIN_V1 | scene | episode_new | 第1组0-12秒，第2组0-11秒，第3组0-14秒 | 省医院接收区月台外，冷链车停靠、车厢打开、接收门和月台形成对峙空间 | yes | new hospital receiving scene |
| EP23_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_COLD_CHAIN_DELIVERY_V1 | prop | episode_variant | 第1组0-9秒，第2组0-3秒，第3组4-7秒 | 林刚冷链货车准时到达并打开车厢验货 | conditional | if state not generated |
| EP23_USE_PROP_002 | PROP_MEDICAL_COLD_BOX_BASE | STATE_PROP_MEDICAL_BOX_URGENT_V1 | prop | asset_bible | 第1组6-9秒，第3组4-7秒 | 车厢内药品箱码放整齐，作为本集待验收货物 | no | reuse existing medical cold box state |
| EP23_USE_PROP_003 | PROP_BLACK_CARD_BASE | STATE_PROP_BLACK_CARD_BRIBE_OFFERED_V1 | prop | episode_new | 第2组9-11秒，第3组0-4秒 | 陈天霸递给李主任的黑卡，触发行贿受贿线索 | yes | new key evidence prop |
| EP23_USE_PROP_004 | PROP_VIBRATION_MONITOR_BASE | STATE_PROP_VIBRATION_MONITOR_GREEN_V1 | prop | episode_new | 第1组6-9秒，第2组3-5秒 | 震动仪或货厢仪表显示一路绿灯，与陈家货物警报形成对照 | yes | new logistics device prop |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_LIZHUREN_HOSPITAL_WHITE_COAT_V1 | CHAR_LIZHUREN_BASE | BASE | character | costume_change | 李主任在医院接收区穿白大褂，手持平板，神情冷硬 | costume, handheld_tablet, authority_posture | episode_range | ep23 | 第1组9-12秒，第2组9-11秒，第3组0-14秒 | yes | generate white coat state | candidate | CHAR_LIZHUREN_BASE人物状态，中国中年项目负责人穿白大褂，内搭浅色衬衫，手持无品牌平板，医院接收区冷白光，姿态板正，神情冷硬，真人实拍电影质感 | 西方人脸，品牌logo，可读屏幕文字，夸张反派妆，卡通，3D渲染，塑料感，水印，字幕 | CHAR_LIZHUREN_BASE character state, middle aged Chinese project supervisor wearing a white lab coat over a light shirt, holding an unbranded tablet, cold white hospital receiving light, rigid posture and cold expression, live action cinematic realism | western faces, brand logos, readable screen text, exaggerated villain makeup, cartoon, 3D render, plastic look, watermark, subtitles |
| STATE_SCENE_HOSPITAL_RECEIVING_OVERCAST_COLDCHAIN_V1 | SCENE_HOSPITAL_RECEIVING_BASE | BASE | scene | lighting_time | 阴天医院接收月台，冷链车停靠，车厢口有冷气 | light, vehicle_position, cold_mist | episode_range | ep23 | 第1组0-12秒，第2组0-11秒，第3组0-14秒 | yes | generate overcast cold chain receiving state | candidate | 省医院接收区月台外空镜，阴天日景，白色月台墙面、接收门、装卸边线和冷链货车停靠位清晰，车厢口有少量白色冷气，地面干净偏冷调，无人无人脸，竖屏电影质感 | 人物，人脸，人群，品牌logo，可读医院名称，可读车牌，字幕，水印，卡通，3D渲染，过曝 | Empty exterior shot of a provincial hospital receiving dock under overcast daylight, white dock walls, receiving doors, loading edge lines and cold chain truck bay visible, light white cold mist near the cargo door, clean cool-toned ground, no people, no faces, vertical cinematic realism | people, faces, crowd, brand logos, readable hospital name, readable plates, subtitles, watermark, cartoon, 3D render, overexposure |
| STATE_VEHICLE_COLD_CHAIN_DELIVERY_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 冷链货车停靠月台，车厢大门打开，内侧冷白光和冷气可见 | refrigerated_cargo, open_door, cold_light | episode_range | ep23 | 第1组0-9秒，第2组7-9秒，第3组4-7秒 | yes | generate refrigerated delivery truck state | candidate | 中国大型冷链物流货车停靠医院接收月台，车厢大门打开，内部冷白灯照亮整齐药品箱，门口有轻微冷气，无品牌logo无车牌，真实运输比例，竖屏电影质感 | 品牌logo，可读车牌，可读公司名，人物脸，卡通，3D渲染，塑料感，过曝，水印，字幕 | Chinese refrigerated logistics truck parked at a hospital receiving dock, cargo doors open, cold white interior light illuminating neatly stacked medical boxes, light cold mist at the doorway, no brand logo, no readable plate, realistic transport scale, vertical cinematic realism | brand logos, readable plates, readable company names, faces, cartoon, 3D render, plastic look, overexposure, watermark, subtitles |
| STATE_VEHICLE_CHEN_CARGO_ALARM_V1 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_CHEN_AIR_SUSPENSION_FAILED_V1 | prop | prop_condition | 陈家货车底盘擦地、车厢红色警报灯闪烁，药品失效警报 | undercarriage_scrape, red_alarm, cargo_failure | one_episode | ep23 | 第2组0-5秒，第3组0-14秒 | yes | generate failed cargo alarm state | candidate | 大型物流货车冲入医院接收区，底盘擦地带出短促火花，半开车厢内红色警报灯闪烁，仪表屏呈模糊失效警示感，无品牌无车牌，真实事故现场质感 | 可读文字，品牌logo，可读车牌，大火爆炸，卡通，3D渲染，塑料感，水印，字幕 | Large logistics truck rushing into a hospital receiving area, undercarriage scraping the ground with brief sparks, red warning light flashing inside the half-open cargo box, instrument screen suggesting blurred failure warning, no brand or plate, realistic incident texture | readable text, brand logos, readable plates, large fire or explosion, cartoon, 3D render, plastic look, watermark, subtitles |
| STATE_PROP_VIBRATION_MONITOR_GREEN_V1 | PROP_VIBRATION_MONITOR_BASE | BASE | prop | prop_condition | 震动仪屏幕显示绿色稳定状态 | screen_color, status_indicator | episode_range | ep23 | 第1组6-9秒 | yes | generate green stable monitor state | candidate | 便携式物流震动监测仪道具，黑灰外壳，小型屏幕亮起绿色稳定数据条，放在冷链车厢药品箱旁，屏幕无清晰可读数字，真实工业设备质感 | 可读数字，品牌logo，二维码，字幕，水印，卡通，3D渲染，塑料感，人物脸 | Portable logistics vibration monitor prop, black gray casing, small screen glowing with green stable data bars, placed beside medical boxes inside a cold chain truck, no clearly readable numbers, realistic industrial device texture | readable numbers, brand logos, QR codes, subtitles, watermark, cartoon, 3D render, plastic look, faces |
| STATE_PROP_BLACK_CARD_BRIBE_OFFERED_V1 | PROP_BLACK_CARD_BASE | BASE | prop | prop_condition | 黑卡被陈天霸递向李主任，作为行贿线索 | handoff_position, evidence_context | episode_range | ep23 | 第2组9-11秒，第3组0-4秒 | yes | generate black card offered state | candidate | 无品牌黑色卡片道具，哑光黑卡面，边缘有冷光反射，被手递出到白大褂和平板下方，卡面无可读文字无logo，真实手持比例，电影质感 | 品牌logo，可读卡号，可读姓名，银行卡真实标识，水印，字幕，卡通，3D渲染，过曝 | Unbranded black card prop, matte black surface with cool edge reflection, handed below a white lab coat and tablet, no readable text or logo on the card, realistic hand-held scale, cinematic realism | brand logos, readable card numbers, readable names, real bank marks, watermark, subtitles, cartoon, 3D render, overexposure |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| SCENE_HOSPITAL_RECEIVING_BASE | scene | 省医院接收区月台外 | 医院后勤接收月台，白色墙面、接收门、月台边线、车道和装卸区域，基础资产必须为空镜 | episode_range | ep23 | yes | 省医院后勤接收区月台外空镜，白色墙面和接收门，混凝土地面，装卸边线，冷链货车停靠位，冷白医院后勤光线，无人无人脸，真实比例，竖屏电影质感 | 人物，人脸，人群，真实医院名称，品牌logo，可读车牌，字幕，水印，卡通，3D渲染 | Empty shot of a provincial hospital logistics receiving dock, white walls and receiving doors, concrete ground, loading edge markings, cold chain truck bay, cool white hospital back-of-house lighting, no people, no faces, realistic proportions, vertical cinematic realism | people, faces, crowd, real hospital name, brand logos, readable plates, subtitles, watermark, cartoon, 3D render |
| COSTUME_LIZHUREN_WHITE_COAT_V1 | costume | 李主任白大褂 | 医院接收区穿着的白大褂，内搭浅色衬衫，可配无品牌平板，不包含人物脸部设定 | episode_range | ep23 | yes | 医院项目负责人白大褂服装资产，干净白色长款医用外套，内搭浅色衬衫，口袋平整，可搭配无品牌平板，真实布料褶皱，产品式服装参考，无人物脸 | 人脸，品牌logo，可读胸牌，可读文字，卡通，3D渲染，塑料感，水印，字幕 | White lab coat costume asset for a hospital project supervisor, clean long white medical coat over a light shirt, neat pockets, optional unbranded tablet, realistic fabric folds, product style costume reference, no face | faces, brand logos, readable name badges, readable text, cartoon, 3D render, plastic look, watermark, subtitles |
| PROP_VIBRATION_MONITOR_BASE | prop | 震动仪 | 冷链运输随车震动监测设备，小型黑灰外壳、电子屏和状态灯，不显示可读品牌或具体数值 | episode_range | ep23 | yes | 小型物流震动监测仪道具，黑灰耐用外壳，电子屏和状态灯，工业运输设备比例，屏幕只呈现模糊数据条，不出现可读品牌或精确数字，真实材质 | 可读品牌，可读数字，二维码，水印，字幕，卡通，3D渲染，塑料玩具感 | Small logistics vibration monitor prop, durable black gray casing, electronic screen and status light, industrial transport device scale, screen only showing blurred data bars, no readable brand or exact numbers, realistic materials | readable brands, readable numbers, QR codes, watermark, subtitles, cartoon, 3D render, toy plastic look |
| PROP_BLACK_CARD_BASE | prop | 黑卡 | 陈天霸用于行贿的无品牌黑色卡片，哑光黑面，边缘冷光反射，不出现卡号和真实银行标识 | episode_range | ep23 | yes | 无品牌黑色卡片道具，哑光黑色卡面，薄卡片比例，边缘有冷白反光，适合行贿证据特写，无卡号无姓名无银行logo，真实手持比例 | 可读卡号，姓名，银行logo，品牌标识，二维码，水印，字幕，卡通，3D渲染 | Unbranded black card prop, matte black card surface, thin card proportions, cool white edge reflection, suitable for a bribery evidence close-up, no card number, no name, no bank logo, realistic hand-held scale | readable card numbers, names, bank logos, brand marks, QR codes, watermark, subtitles, cartoon, 3D render |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_HOSPITAL_RECEIVING_OVERCAST_COLDCHAIN_V1 | SCENE_HOSPITAL_RECEIVING_BASE | scene | 阴天医院接收月台和冷链车停靠状态 | 第1组0-12秒，第2组0-11秒，第3组0-14秒 | yes | new core hospital receiving state | 建议同步到asset_bible |
| STATE_VEHICLE_COLD_CHAIN_DELIVERY_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 冷链货车打开车厢，药品箱和冷白灯可见 | 第1组0-9秒，第2组7-9秒 | yes | cold chain delivery truck state | 建议同步到asset_bible |
| STATE_PROP_VIBRATION_MONITOR_GREEN_V1 | PROP_VIBRATION_MONITOR_BASE | prop | 震动仪绿色稳定状态 | 第1组6-9秒 | yes | new proof device state | 建议同步到asset_bible |
| STATE_PROP_BLACK_CARD_BRIBE_OFFERED_V1 | PROP_BLACK_CARD_BASE | prop | 黑卡被递给李主任 | 第2组9-11秒，第3组0-4秒 | yes | evidence prop state | 建议同步到asset_bible |
| STATE_VEHICLE_CHEN_CARGO_ALARM_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 陈家货车红色警报和底盘擦地状态 | 第2组0-5秒，第3组0-14秒 | yes | failed cargo alarm state | 候选同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 平板 | 第1组9-12秒，第2组9-11秒，第3组0-14秒 | 普通手持办公设备，已由李主任白大褂状态携带，不单独作为关键道具入库 |
| 车厢大门、月台边线、接收门 | 第1组0-9秒 | 属于医院接收区场景结构，由SCENE_HOSPITAL_RECEIVING_BASE承载 |
| 王百川跑动、林刚跳下车、陈天霸大笑 | 第1组0-6秒，第3组7-14秒 | 短暂表演动作和情绪，不是资产状态 |
| 屏幕上的具体失效文字 | 第2组3-5秒 | 生产资产避免可读文字，使用模糊警报屏状态表达即可 |
