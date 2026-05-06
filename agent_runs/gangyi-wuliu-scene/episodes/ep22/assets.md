# 《刚毅物流ep22》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP22_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组4-6秒，第4组2-10秒 | 林刚作为刚毅车队负责人在驾驶室内稳车、与陈天霸隔窗交锋 | no | reuse existing character state |
| EP22_USE_CHAR_002 | CHAR_CHENTIANBA_BASE | BASE | character | asset_bible | 第2组0-11秒，第3组10-12秒，第4组0-12秒 | 陈天霸在头车副驾强令挡车，抛锚后与林刚对峙 | no | reuse existing character base |
| EP22_USE_SCENE_001 | SCENE_MOUNTAIN_ROAD_BASE | STATE_SCENE_MOUNTAIN_MUDDY_OVERCAST_V1 | scene | episode_variant | 第1组0-10秒，第3组0-12秒，第4组0-12秒 | 阴天烂泥路段、尖石、深坑和泥水作为车队追赶主场景 | conditional | if state not generated |
| EP22_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_GANGYI_DEFLATED_TIRE_MUD_V1 | prop | episode_variant | 第1组0-10秒，第4组0-12秒 | 刚毅重卡放气轮胎稳住泥路并越过抛锚车 | conditional | if state not generated |
| EP22_USE_PROP_002 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_CHEN_AIR_SUSPENSION_FAILED_V1 | prop | episode_variant | 第3组0-12秒，第4组0-12秒 | 陈家重卡气囊减震爆裂后陷入烂泥、警报灯闪烁 | conditional | if state not generated |
| EP22_USE_COMP_001 | COMPOSITION_TRUCK_UNDERCARRIAGE_V1 | BASE | composition | asset_bible | 第3组2-6秒 | 低机位呈现重卡底盘、尖石和减震器破裂 | no | reuse existing composition |
| EP22_USE_COMP_002 | COMPOSITION_ROAD_BLOCKADE_V1 | BASE | composition | asset_bible | 第1组6-10秒，第4组0-2秒 | 两支车队在泥路上逼近、并行和越过的空间关系 | no | reuse existing composition |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_MOUNTAIN_MUDDY_OVERCAST_V1 | SCENE_MOUNTAIN_ROAD_BASE | BASE | scene | scene_condition | 阴天烂泥路段，泥坑、尖石、碎石和积水明显 | light, road_condition, debris | episode_range | ep22 | 第1组0-10秒，第3组0-12秒，第4组0-12秒 | yes | generate muddy overcast road state | candidate | 中国山区或乡道烂泥路空镜，阴天灰白漫射光，路面布满深泥坑、尖石、碎石和积水，湿泥反光真实，适合重卡车队通行冲突，无人无人脸，竖屏电影质感 | 人物，人脸，车牌号，品牌logo，可读文字，卡通，3D渲染，塑料感，过曝，低清晰度，水印，字幕 | Empty shot of a muddy Chinese mountain or rural road under overcast gray daylight, deep mud pits, sharp stones, gravel and puddles on the road, realistic wet mud reflections, suitable for a heavy truck convoy conflict, no people, no faces, vertical cinematic realism | people, faces, license plates, brand logos, readable text, cartoon, 3D render, plastic look, overexposure, low resolution, watermark, subtitles |
| STATE_VEHICLE_GANGYI_DEFLATED_TIRE_MUD_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 刚毅重卡轮胎放气后压宽，胎纹咬住泥坑边缘 | tire_condition, mud_contact | episode_range | ep22 | 第1组0-2秒，第1组6-10秒，第4组10-12秒 | yes | generate deflated tire mud state | candidate | 中国大型物流重卡在烂泥路行驶，宽大轮胎放气后胎面压宽，胎纹咬住湿泥和碎石，车身有泥点和路尘，无品牌logo无车牌，真实比例，竖屏电影质感 | 品牌logo，可读车牌，夸张改装，卡通，3D渲染，塑料感，文字水印，人物脸部特写，低清晰度 | Chinese heavy logistics truck driving on a muddy road, wide tires slightly deflated with flattened tread gripping wet mud and gravel, mud specks and road dust on the body, no brand logo, no readable plate, realistic proportions, vertical cinematic realism | brand logos, readable license plates, exaggerated tuning, cartoon, 3D render, plastic look, text watermark, facial close-up, low resolution |
| STATE_VEHICLE_CHEN_AIR_SUSPENSION_FAILED_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 陈家重卡底盘气囊减震破裂，车身陷泥并有红色警报灯 | suspension_damage, mud_trap, warning_light | one_episode | ep22 | 第3组4-12秒，第4组0-12秒 | yes | generate damaged suspension state | candidate | 大型物流重卡陷在烂泥深坑中，底盘区域受尖石冲击，气囊减震器破裂喷出泥水，车顶红色警报灯闪烁，车身无品牌无车牌，低机位真实工业细节 | 可读车牌，品牌logo，爆炸火焰，虚构文字，卡通，3D渲染，过度血腥，人物脸部遮挡主体，水印 | Large logistics truck stuck in a deep muddy pit, undercarriage struck by sharp stones, broken air suspension bag spraying muddy water, red warning light flashing on the roof, no brand or plate, low angle realistic industrial detail | readable plates, brand logos, explosion flames, fictional text, cartoon, 3D render, gore, faces blocking the subject, watermark |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_CHEN_DRIVER_BASE | character | 陈家司机 | 陈天霸车队头车司机，成年中国男性，普通运输司机体态，短发，穿深色驾驶工装，气质紧张怕事，只记录本集驾驶与惊慌基础形象 | one_episode | ep22 | no | 中国物流车队司机，30多岁男性，普通运输司机体态，短发，深色驾驶工装，神情紧张但不夸张，驾驶室环境，真人实拍电影质感 | 西方人脸，夸张丑化，品牌logo，可读文字，卡通，3D渲染，塑料感，水印，字幕 | Chinese logistics truck driver, man in his 30s, ordinary transport driver build, short hair, dark driving workwear, tense but realistic expression, truck cab environment, live action cinematic realism | western faces, caricature, brand logos, readable text, cartoon, 3D render, plastic look, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_MOUNTAIN_MUDDY_OVERCAST_V1 | SCENE_MOUNTAIN_ROAD_BASE | scene | 阴天烂泥、尖石和深坑路况 | 第1组0-10秒，第3组0-12秒，第4组0-12秒 | yes | new reusable muddy road state | 建议同步到asset_bible |
| STATE_VEHICLE_GANGYI_DEFLATED_TIRE_MUD_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 刚毅重卡放气轮胎泥路抓地状态 | 第1组0-10秒，第4组10-12秒 | yes | new truck tire condition | 建议同步到asset_bible |
| STATE_VEHICLE_CHEN_AIR_SUSPENSION_FAILED_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 陈家重卡气囊减震破裂并陷泥 | 第3组4-12秒，第4组0-12秒 | yes | one episode damage state but useful as evidence visual | 候选同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 方向盘、中控台、后视镜、仪表屏 | 第1组2-6秒，第2组0-8秒，第3组6-8秒 | 驾驶室常规陈设，服务单镜头叙事，可随车辆和驾驶室即时生成 |
| 司机甲画外音 | 第1组2-4秒 | 只有声音，没有稳定视觉资产 |
| 泥水飞溅、碎石滚开 | 第1组0-2秒，第4组10-12秒 | 属于场景动态效果，已由烂泥路状态承载 |
| 陈天霸额头撞击、怒吼表情 | 第3组10-12秒，第4组6-8秒 | 短暂表演和情绪，不是可复用资产状态 |
