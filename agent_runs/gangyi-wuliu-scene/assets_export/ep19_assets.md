# 《刚毅物流 ep19》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP19_USE_CHAR_001 | CHAR_SUNBIAO_BASE | BASE | character | asset_bible | 第1组0-10秒，第4组8-10秒，第5组3-7秒 | 孙彪带人设伏并被钉雨反砸 | no | existing base character |
| EP19_USE_CHAR_002 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第2组5-10秒，第3组0-9秒，第5组7-10秒 | 林刚驾驶头车指挥车队 | no | existing convoy-stage state |
| EP19_USE_CHAR_003 | CHAR_POLICE_BASE | STATE_GANGYI_DRIVERS_V1 | character | asset_bible | 第2组5-7秒，第3组9-12秒，第5组7-10秒 | 刚毅车队司机群像和司机甲画外音 | no | existing driver crowd proxy |
| EP19_USE_SCENE_001 | SCENE_MOUNTAIN_ROAD_BASE | BASE | scene | asset_bible | 第1组至第5组 | 盘山公路弯道基础空间 | no | existing mountain road base |
| EP19_USE_PROP_001 | VEHICLE_PICKUP_BASE | BASE | prop | asset_bible | 第2组0-3秒，第3组0-12秒，第4组0-10秒，第5组7-10秒 | 林刚头车皮卡 | no | existing pickup base |
| EP19_USE_PROP_002 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第2组0-3秒，第3组9-12秒，第5组7-10秒 | 五辆崭新重卡车队 | no | existing heavy truck base |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SUNBIAO_FACE_GAUZE_V1 | CHAR_SUNBIAO_BASE | BASE | character | injury | 孙彪脸侧贴纱布，钉雨后纱布歪斜并有汗光 | facial_gauze, sweat, minor_injury | episode_range | ep19 | 第1组3-5秒，第4组8-10秒，第5组5-7秒 | yes | if state not generated | candidate | 基于 CHAR_SUNBIAO_BASE 和 COSTUME_WORKER_LOGISTICS_V1，孙彪脸侧贴白色纱布，深色物流工装，钉雨后纱布略歪并带汗光，真实中国物流园打手形象，竖屏电影质感，日间硬光 | 西方面孔，卡通，3D渲染，夸张伤口，血腥，品牌logo，可读文字，水印，字幕 | Based on CHAR_SUNBIAO_BASE and COSTUME_WORKER_LOGISTICS_V1, Sun Biao with white gauze on one side of his face, dark logistics workwear, the gauze slightly skewed with sweat after the spike attack, realistic Chinese logistics enforcer, vertical cinematic live action, hard daylight | Western face, cartoon, 3D render, exaggerated wound, gore, brand logo, readable text, watermark, subtitles |
| STATE_SCENE_MOUNTAIN_ROAD_SUNNY_SPIKES_V1 | SCENE_MOUNTAIN_ROAD_BASE | BASE | scene | scene_condition | 日间晴天干燥盘山弯道，路面散满三角扎胎钉，路边有草丛和碎石坡 | light, road_condition, spike_scatter | episode_range | ep19 | 第1组0-10秒，第2组0-5秒，第4组0-8秒，第5组0-10秒 | yes | if sunny spike road state not generated | candidate | 中国山区盘山公路弯道空镜，晴天正午硬光，干燥灰色柏油路面，车道中央散布大量银色三角扎胎钉，路边草丛和碎石坡清晰，无人无人脸，真实电影质感，竖屏构图 | 人物，人脸，车牌号，品牌logo，可读文字，卡通，3D渲染，过曝，水印，字幕 | Empty shot of a Chinese mountain road bend, sunny noon hard light, dry gray asphalt, many silver triangular tire spikes scattered across the lane, roadside grass and gravel slope, no people, no faces, realistic cinematic texture, vertical framing | People, faces, license plate, brand logo, readable text, cartoon, 3D render, overexposure, watermark, subtitles |
| STATE_PROP_TRIANGLE_SPIKES_SCATTERED_V1 | PROP_TRIANGLE_TIRE_SPIKES_BASE | BASE | prop | prop_condition | 三角扎胎钉成片撒在柏油路上并被推向路边 | scatter, metal_highlight, road_contact | one_episode | ep19 | 第1组0-10秒，第2组3-5秒，第4组3-8秒，第5组0-3秒 | yes | generate with new base prop | candidate | 银色三角扎胎钉道具状态，大量金属尖角散落在灰色柏油路面，部分被推挤成堆，尖端有日光高光，真实比例，近景产品式写实，无遮挡品牌文字 | 手持人物，血腥，品牌logo，可读文字，卡通，3D渲染，塑料感，水印 | Silver triangular tire spike prop state, many metal spikes scattered on gray asphalt, some pushed into a small pile, sharp tips catching daylight highlights, realistic scale, close-up product-like realism, no brand text | Holding hands, gore, brand logo, readable text, cartoon, 3D render, plastic look, watermark |
| STATE_PROP_HYDRAULIC_PLOW_DEPLOYED_V1 | PROP_HYDRAULIC_SNOWPLOW_BASE | BASE | prop | prop_condition | 皮卡车头液压推雪铲降下并贴近路面扫钉 | deployed_blade, hydraulic_linkage, road_scrape | one_episode | ep19 | 第3组3-12秒，第4组0-8秒，第5组0-3秒 | yes | generate with new base prop | candidate | 皮卡前方液压推雪铲展开状态，宽大金属铲刃贴近灰色柏油路面，液压连杆和铲刃磨痕清晰，日间硬光下有金属反光，真实工程改装质感，无品牌无车牌文字 | 品牌logo，车牌号，可读文字，卡通，3D渲染，比例畸形，水印，字幕 | Deployed hydraulic snowplow blade on the front of a pickup, wide metal blade close to gray asphalt, visible hydraulic linkage and scraped blade edge, daylight metal highlights, realistic utility modification, no brand or plate text | Brand logo, license plate, readable text, cartoon, 3D render, distorted proportions, watermark, subtitles |
| STATE_COMPOSITION_PLOW_SWEEP_SPIKES_V1 | COMPOSITION_PLOW_SWEEP_SPIKES_V1 | BASE | composition | composition_reference | 皮卡推雪铲贴地扫开钉阵，重卡在后方保持车距 | foreground_blade, spike_motion, convoy_depth | one_episode | ep19 | 第4组0-8秒，第5组7-10秒 | yes | key action composition | candidate | 竖屏动态构图，前景是皮卡车头和贴地液压推雪铲，铲刃把银色三角扎胎钉从车道中央推向路边，后景五辆重卡保持距离，晴天硬光和低灰尘增强纵深，真实电影动作场面 | 品牌logo，车牌号，可读文字，卡通，3D渲染，夸张爆炸，水印，字幕 | Vertical action composition, pickup front and low hydraulic plow blade in the foreground, the blade pushing silver tire spikes from the lane center to the roadside, five heavy trucks keeping distance behind, sunny hard light and low dust for depth, realistic cinematic action | Brand logo, license plate, readable text, cartoon, 3D render, exaggerated explosion, watermark, subtitles |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| PROP_TRIANGLE_TIRE_SPIKES_BASE | prop | 三角扎胎钉 | 银色金属三角扎胎钉，尖角多向外伸，用于路面扎胎设伏，适合近景和路面散布镜头 | episode_range | ep19 | candidate | 银色金属三角扎胎钉基础道具，三角立体结构，多向尖角，边缘有磨损和冷硬反光，放在灰色柏油路面上作比例参照，真实危险路障道具质感 | 血腥，人物手部，品牌logo，可读文字，卡通，3D渲染，塑料感，水印 | Base prop of silver metal triangular tire spikes, three-dimensional triangular structure with points facing multiple directions, worn edges and cold reflections, placed on gray asphalt for scale, realistic hazardous road obstacle | Gore, human hands, brand logo, readable text, cartoon, 3D render, plastic look, watermark |
| PROP_HYDRAULIC_SNOWPLOW_BASE | prop | 皮卡液压推雪铲 | 安装在皮卡车头下方的宽大金属推雪铲，带液压连杆和可升降结构，用于清开路面障碍 | episode_range | ep19 | candidate | 皮卡前置液压推雪铲基础道具，宽大弧形金属铲刃，黑色液压连杆和安装支架，铲刃边缘有刮擦磨损，真实车辆改装设备，日间自然光，无品牌文字 | 车牌号，品牌logo，可读文字，卡通，3D渲染，玩具感，水印 | Base prop of a front-mounted hydraulic snowplow for a pickup, wide curved metal blade, black hydraulic linkage and mounting bracket, scratched blade edge, realistic vehicle modification equipment in daylight, no brand text | License plate, brand logo, readable text, cartoon, 3D render, toy-like look, watermark |
| COMPOSITION_PLOW_SWEEP_SPIKES_V1 | composition | 推雪铲扫开钉阵构图 | 低机位或全景强调推雪铲贴地、钉子被推向路边、重卡车队跟随的动作关系 | one_episode | ep19 | candidate | 竖屏电影动作构图，皮卡前置液压推雪铲贴地推进，银色扎胎钉被铲刃推离车道，后方重卡车队保持距离，盘山公路晴天硬光，低角度带速度感 | 品牌logo，车牌号，可读文字，卡通，3D渲染，过度火花，水印，字幕 | Vertical cinematic action composition, pickup-mounted hydraulic plow scraping low over the road, silver tire spikes pushed out of the lane, heavy truck convoy behind at safe distance, sunny mountain road hard light, low angle with motion energy | Brand logo, license plate, readable text, cartoon, 3D render, excessive sparks, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_MOUNTAIN_ROAD_SUNNY_SPIKES_V1 | SCENE_MOUNTAIN_ROAD_BASE | scene | 晴天干燥盘山公路弯道带钉阵 | 第1组0-10秒，第2组0-5秒，第4组0-8秒 | yes | 新增晴天钉阵状态 | 建议同步到asset_bible |
| STATE_PROP_TRIANGLE_SPIKES_SCATTERED_V1 | PROP_TRIANGLE_TIRE_SPIKES_BASE | prop | 大量三角扎胎钉散落并被推挤 | 第1组0-10秒，第4组3-8秒，第5组0-3秒 | yes | 新增关键障碍道具状态 | 建议同步到asset_bible |
| STATE_PROP_HYDRAULIC_PLOW_DEPLOYED_V1 | PROP_HYDRAULIC_SNOWPLOW_BASE | prop | 皮卡液压推雪铲降下贴路清障 | 第3组3-12秒，第4组0-8秒 | yes | 新增关键车辆改装道具状态 | 建议同步到asset_bible |
| STATE_SUNBIAO_FACE_GAUZE_V1 | CHAR_SUNBIAO_BASE | character | 孙彪脸侧纱布伤势状态 | 第1组3-5秒，第4组8-10秒，第5组5-7秒 | yes | 可能延续到后续集 | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 红色按钮 | 第3组0-3秒 | 只作为一次性操作细节，已由推雪铲状态承载 |
| 纱布瞬间歪斜动作 | 第5组5-7秒 | 属于孙彪伤势状态中的短暂变化，不单独建道具 |
| 火星和扬尘 | 第4组3-6秒，第5组7-10秒 | 动作特效和环境瞬态，不是可复用资产 |
| 草叶遮挡和碎石坡 | 第1组至第5组 | 已由盘山公路场景状态承载，无需拆成独立道具 |
| 打手表情和抬手遮挡 | 第1组5-7秒，第5组3-7秒 | 临时群演表演，不固定为跨集人物或状态 |
