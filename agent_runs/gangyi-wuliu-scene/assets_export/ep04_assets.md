# 《刚毅物流 ep04》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP04_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | 第1组-第4组 | 林刚从雨夜山道脱险并送达急件，基础身份和脸型沿用全局设定 | no | reuse existing character and township state |
| EP04_USE_SCENE_001 | SCENE_MOUNTAIN_ROAD_BASE | STATE_SCENE_MOUNTAIN_ROAD_RAIN_NIGHT_V1 | scene | asset_bible | 第1组 0-2秒，第1组 4-7秒，第2组 5-12秒 | 死亡山道雨夜急弯、湿滑路面、悬崖边危机 | conditional | if state not generated |
| EP04_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_SEAFOOD_TRUCK_RAIN_DAMAGED_V1 | prop | asset_bible | 第1组-第3组，第4组 | 满载海鲜货车失控、刮擦受损后停到别墅门口 | conditional | if state not generated |
| EP04_USE_PROP_002 | PROP_CRACKED_PHONE_BASE | BASE | prop | asset_bible | 第1组 7-10秒 | 副驾驶手机震动亮屏传出主管催逼声音 | no | reuse generic phone without crack state |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_LINGANG_RAIN_BLOOD_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | injury | 林刚雨夜撞车后额头流血、衣服湿透但仍保持硬气站姿 | 额头血迹、雨水湿发、工装湿透、脸部疲惫 | episode_range | ep04 | 第3组 0-8秒，第4组 4-8秒 | yes | generate injured rain delivery state | candidate | 引用 CHAR_LINGANG_BASE 与 COSTUME_LINGANG_WORK_JACKET_V1，中国乡镇物流人林刚雨夜受伤状态，额头有血水混着雨水滑下，黑色短寸发被雨打湿，深色工装外套湿透贴身并带路尘，站在货车旁仍保持沉稳硬气，竖屏真人实拍电影质感，雨夜车灯和门灯交错照明 | 不要西方人脸，不要改变林刚国字脸和短寸发，不要新增品牌logo、字幕、水印、夸张血腥、卡通、3D渲染、塑料感、面部融合 | Use CHAR_LINGANG_BASE and COSTUME_LINGANG_WORK_JACKET_V1, Lin Gang as a Chinese township logistics worker after a rainy night crash, blood mixed with rain on his forehead, short black crew cut soaked, dark work jacket wet and dusty, standing beside the truck with steady toughness, vertical live action cinematic still, mixed truck light and villa gate light in rain | no Western face, do not change Lin Gang square face or crew cut, no added brand logo, subtitles, watermark, excessive gore, cartoon, 3D render, plastic texture, fused face |
| STATE_SCENE_MOUNTAIN_ROAD_RAIN_NIGHT_V1 | SCENE_MOUNTAIN_ROAD_BASE | BASE | scene | scene_condition | 盘山公路雨夜湿滑急弯状态，车灯撕开雨幕，护栏和悬崖边可见 | 夜雨、湿滑柏油、急弯护栏、悬崖边、车灯冷光 | episode_range | ep04 | 第1组 0-2秒，第1组 4-7秒，第2组 5-12秒 | yes | generate rainy night mountain road state | candidate | 引用 SCENE_MOUNTAIN_ROAD_BASE，中国山区盘山公路雨夜空镜，窄路急弯通向悬崖边，湿滑柏油路反射车灯，护栏和山体护坡被雨水打亮，密集雨幕、冷色夜光、真实路面比例，无人无人脸，竖屏真人实拍电影质感 | 不要人物、人脸、人群、车牌号、品牌logo、字幕、水印，不要卡通、油画、3D渲染、过曝、塑料感 | Use SCENE_MOUNTAIN_ROAD_BASE, empty Chinese mountain road at rainy night, narrow sharp bend toward a cliff edge, wet asphalt reflecting headlights, guardrail and rocky slope lit by rain, dense rainfall, cool night light, realistic road scale, no people and no faces, vertical live action cinematic still | no people, no faces, no crowd, no readable license plate, no brand logo, no subtitles, no watermark, no cartoon, oil painting, 3D render, overexposure, plastic texture |
| STATE_VEHICLE_SEAFOOD_TRUCK_RAIN_DAMAGED_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 满载海鲜货车雨夜失控后车身刮擦、倒后镜断裂、轮胎湿滑冒烟 | 货车满载、雨水、车身刮擦、倒后镜断裂、湿滑轮胎、无品牌车牌 | episode_range | ep04 | 第1组 0-2秒，第2组 0-12秒，第3组 0-2秒 | yes | generate damaged seafood delivery truck state | candidate | 引用 VEHICLE_HEAVY_TRUCK_BASE，中国大型货运货车雨夜受损状态，货箱满载但不展示可读品牌，车身侧面有山体刮擦痕，倒后镜断裂，轮胎湿滑带白烟和泥水，车灯穿过雨幕，真实金属车身和运输比例 | 不要品牌logo、可读车牌、可读公司文字、人物脸、字幕、水印，不要卡通、3D渲染、塑料感、爆炸火焰 | Use VEHICLE_HEAVY_TRUCK_BASE, Chinese heavy cargo truck in rainy night damaged state, loaded cargo box without readable brand, scrape marks along the side, broken side mirror, wet tires with white smoke and muddy water, headlights cutting through rain, realistic metal body and transport scale | no brand logo, no readable license plate, no readable company text, no human face, no subtitles, no watermark, no cartoon, 3D render, plastic texture, explosion or flames |
| STATE_SCENE_VILLA_GATE_RAIN_NIGHT_V1 | SCENE_LUXURY_VILLA_GATE_BASE | BASE | scene | lighting_time | 豪华别墅门口雨夜状态，门廊暖光、门岗和湿地反光清晰 | 雨夜、暖门灯、门岗、湿地反光、大门外停靠区 | episode_range | ep04 | 第3组 0-10秒，第4组 0-11秒 | yes | generate villa gate rainy night state | candidate | 引用 SCENE_LUXURY_VILLA_GATE_BASE，豪华别墅大门外雨夜空镜，大门居中、门岗位于侧边、门廊暖光照出湿亮地面，门前有货车停靠空间但不显示人物，雨线清楚，竖屏真人实拍电影质感，无人无人脸 | 不要人物、人脸、人群、品牌logo、门牌可读文字、字幕、水印，不要卡通、3D渲染、塑料感、过度豪华宫殿化 | Use SCENE_LUXURY_VILLA_GATE_BASE, empty luxury villa gate at rainy night, main gate centered, guard booth on the side, warm porch light reflected on wet pavement, space for a truck outside the gate but no people, visible rainfall, vertical live action cinematic still, no people and no faces | no people, no faces, no crowd, no brand logo, no readable house number, no subtitles, no watermark, no cartoon, 3D render, plastic texture, overly palace like design |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_SECURITY_GUARD_BASE | character | 别墅保安 | 豪华别墅门岗保安，成年男性，中等体态，短发，穿深色保安制服或雨夜执勤外套，神情势利警惕 | episode_range | ep04 | candidate | 中国豪华别墅门岗保安，成年男性，中等体态，短发，深色保安制服或雨夜执勤外套，站姿警惕，神情势利冷硬，竖屏角色定妆照，真人实拍电影质感 | 不要西方人脸，不要夸张黑帮造型，不要真实公司徽章、可读胸牌、品牌logo、字幕、水印、卡通、3D渲染 | Chinese luxury villa gate security guard, adult male, medium build, short hair, dark security uniform or rainy night duty jacket, alert posture, snobbish stern expression, vertical character reference, live action cinematic texture | no Western face, no exaggerated gangster look, no real company badge, no readable name tag, no brand logo, subtitles, watermark, cartoon, 3D render |
| CHAR_BUTLER_BASE | character | 别墅管家 | 豪华别墅管家，40岁左右男性，身形偏瘦，短发整齐，穿深色西装或管家制服，气质冷淡克制 | episode_range | ep04 | candidate | 中国豪华别墅管家，40岁左右男性，身形偏瘦，整齐短发，深色西装或管家制服，手持黑伞可作为随身道具，神情冷淡克制，竖屏角色定妆照，真人实拍电影质感 | 不要西方人脸，不要夸张燕尾服，不要真实家族徽章、品牌logo、可读文字、字幕、水印、卡通、3D渲染 | Chinese luxury villa butler, male around 40, slightly slim build, neat short hair, dark suit or butler uniform, black umbrella as optional hand prop, cold restrained expression, vertical character reference, live action cinematic texture | no Western face, no exaggerated tailcoat, no real family crest, no brand logo, no readable text, subtitles, watermark, cartoon, 3D render |
| SCENE_LUXURY_VILLA_GATE_BASE | scene | 豪华别墅门口 | 豪华别墅外门与门岗空间，包含大门、门廊、门岗、湿地或车道停靠区，基础资产必须为空镜 | episode_range | ep04 | candidate | 中国豪华别墅大门外空镜，宽阔大门、门廊、侧边门岗和车道停靠区，石材或金属门体，地面可反光，现代富人住宅质感，竖屏构图，无人无人脸，真人实拍电影质感 | 不要人物、人脸、人群、可读门牌、品牌logo、字幕、水印，不要宫殿化夸张装饰、卡通、3D渲染、塑料感 | Empty exterior gate of a luxury Chinese villa, wide main gate, porch, side guard booth and driveway stopping area, stone or metal gate materials, reflective ground, modern wealthy residence texture, vertical composition, no people and no faces, live action cinematic still | no people, no faces, no crowd, no readable house number, no brand logo, subtitles, watermark, no palace like exaggerated decoration, cartoon, 3D render, plastic texture |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_LINGANG_RAIN_BLOOD_V1 | CHAR_LINGANG_BASE | character | 林刚额头流血、雨水湿透工装的送货状态 | 第3组 0-8秒，第4组 4-8秒 | yes | injured rain state not in bible | 建议同步到asset_bible |
| STATE_SCENE_MOUNTAIN_ROAD_RAIN_NIGHT_V1 | SCENE_MOUNTAIN_ROAD_BASE | scene | 死亡山道雨夜湿滑急弯与悬崖边状态 | 第1组 0-2秒，第2组 5-12秒 | yes | rainy night road state not in bible | 建议同步到asset_bible |
| STATE_VEHICLE_SEAFOOD_TRUCK_RAIN_DAMAGED_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 满载海鲜货车雨夜受损状态 | 第1组 0-2秒，第2组 0-12秒，第3组 0-2秒 | yes | damaged truck state not in bible | 建议同步到asset_bible |
| STATE_SCENE_VILLA_GATE_RAIN_NIGHT_V1 | SCENE_LUXURY_VILLA_GATE_BASE | scene | 豪华别墅门口雨夜门灯反光状态 | 第3组 0-10秒，第4组 0-11秒 | yes | new scene state | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 方向盘、刹车踏板、离合踏板、手刹、挡杆 | 第1组 2-7秒，第2组 0-3秒 | 属于驾驶表演和车辆局部动作，已由货车状态与驾驶室即时生成承载 |
| 挡风玻璃雨刷间隙、车速表指针 | 第1组 2-7秒 | 一次性镜头细节，服务紧张氛围，不需要跨镜头稳定入库 |
| 山体护坡、大树、悬崖护栏 | 第2组 5-12秒 | 已由盘山公路场景状态承载，不单独作为道具资产 |
| 后车厢门、门岗顶灯、别墅大门局部 | 第3组-第4组 | 已由货车状态和别墅门口场景承载，不独立入库 |
| 管家手表、黑伞伞柄握紧动作 | 第3组 8-10秒，第4组 0-11秒 | 手表和握伞动作只服务本集拒收表演，黑伞可作为管家基础人物随身道具处理 |
