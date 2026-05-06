# 《刚毅物流 ep06》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP06_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | 第1组-第4组 | 林刚在自家院中准备防滑链、提醒村民暴雪风险并开走皮卡 | no | reuse existing character state |
| EP06_USE_CHAR_002 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | 第1组-第4组 | 赵大强带村民冒险出村拉海鲜 | no | reuse existing villain state |
| EP06_USE_SCENE_001 | SCENE_VILLAGE_ROAD_BASE | STATE_SCENE_VILLAGE_ROAD_OVERCAST_PRESNOW_V1 | scene | asset_bible | 第4组 9-11秒 | 阴沉天色下破面包车摇晃驶出村口 | conditional | if state not generated |
| EP06_USE_PROP_001 | VEHICLE_PICKUP_BASE | STATE_VEHICLE_PICKUP_NEW_WINTER_PREP_V1 | prop | asset_bible | 第1组-第4组 | 林刚的新大皮卡，装行李、绑防滑链并平稳驶出院门 | conditional | if state not generated |
| EP06_USE_PROP_002 | VEHICLE_OLD_VAN_BASE | STATE_VEHICLE_OLD_VAN_OVERLOADED_V1 | prop | asset_bible | 第2组 6-11秒，第4组 4-11秒 | 赵大强和村民挤上快报废破面包车冒险出村 | conditional | if state not generated |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_LINGANG_HOME_YARD_OVERCAST_V1 | SCENE_LINGANG_HOME_YARD_BASE | BASE | scene | lighting_time | 林刚家院子阴天日景状态，院门、泥地石缝和车辆停靠空间清晰 | 阴天漫射光、乡村院门、泥地石缝、皮卡停靠区、院墙反光 | episode_range | ep06 | 第1组-第4组 | yes | generate home yard overcast state | candidate | 引用 SCENE_LINGANG_HOME_YARD_BASE，中国乡村家庭院子阴天日景空镜，院门、低矮院墙、泥地和石缝清晰，院内有车辆停靠空间，灰白漫射光均匀铺开，地面真实尘土和湿痕质感，无人无人脸，竖屏真人实拍电影质感 | 不要人物、人脸、人群、可读门牌、品牌logo、字幕、水印，不要卡通、3D渲染、塑料感、过度精装修 | Use SCENE_LINGANG_HOME_YARD_BASE, empty Chinese rural home yard on an overcast day, yard gate, low walls, dirt ground and stone cracks visible, space for a vehicle, even gray diffuse light, realistic dusty ground and wet marks, no people and no faces, vertical live action cinematic still | no people, no faces, no crowd, no readable house number, no brand logo, no subtitles, no watermark, no cartoon, 3D render, plastic texture, no overly renovated look |
| STATE_VEHICLE_PICKUP_NEW_WINTER_PREP_V1 | VEHICLE_PICKUP_BASE | BASE | prop | prop_condition | 崭新大皮卡冬季出车准备状态，车斗打开，前轮旁绑防滑链 | 新车身、车斗打开、防滑链、行李装车、阴天反光、无品牌车牌 | episode_range | ep06 | 第1组 0-12秒，第2组 0-11秒，第3组 0-12秒，第4组 0-11秒 | yes | generate new pickup winter prep state | candidate | 引用 VEHICLE_PICKUP_BASE，中国崭新实用大皮卡冬季准备状态，车斗打开，车身干净有柔和阴天反光，前轮旁可见防滑链安装位置，少量行李在车斗附近，真实运输比例，无品牌logo无车牌文字 | 不要品牌logo、可读车牌、豪华跑车化、人物脸、字幕、水印、卡通、3D渲染、塑料感 | Use VEHICLE_PICKUP_BASE, new practical Chinese large pickup in winter preparation state, open cargo bed, clean body with soft overcast reflection, snow chain position visible near front wheel, small amount of luggage near cargo bed, realistic transport scale, no brand logo and no license plate text | no brand logo, readable license plate, luxury sports car styling, human face, subtitles, watermark, cartoon, 3D render, plastic texture |
| STATE_VEHICLE_OLD_VAN_OVERLOADED_V1 | VEHICLE_OLD_VAN_BASE | BASE | prop | prop_condition | 快报废破面包车载着赵大强和村民摇晃出村状态 | 老旧车身、锈迹、车门被拉开、多人上车导致晃动、阴沉天色 | episode_range | ep06 | 第2组 6-11秒，第4组 4-11秒 | yes | generate overloaded old van state | candidate | 引用 VEHICLE_OLD_VAN_BASE，中国乡镇快报废破面包车状态，车漆斑驳有锈迹，车门被拉开，车身因多人挤上车轻微下沉和晃动，轮胎沾泥，阴沉天色下真实旧车比例，无品牌logo无车牌文字 | 不要品牌logo、可读车牌、现代新车质感、人物脸特写、字幕、水印、卡通、3D渲染 | Use VEHICLE_OLD_VAN_BASE, nearly scrapped Chinese rural van, chipped paint and rust, door pulled open, body slightly sagging and shaking from multiple people boarding, muddy tires, realistic old vehicle scale under overcast sky, no brand logo and no license plate text | no brand logo, readable license plate, modern new car look, close human face, subtitles, watermark, cartoon, 3D render |
| STATE_PROP_ANTIFREEZE_SPILLED_V1 | PROP_ANTIFREEZE_BOTTLE_BASE | BASE | prop | prop_condition | 防冻液瓶被踢翻，淡色液体沿泥地和石缝洒开 | 瓶子横倒、淡色液体、泥地石缝湿痕、无可读标签 | one_episode | ep06 | 第2组 0-2秒，第3组组首，第4组组首 | yes | generate spilled antifreeze prop state | candidate | 引用 PROP_ANTIFREEZE_BOTTLE_BASE，防冻液瓶被踢翻的道具状态，塑料瓶横倒在乡村院中泥地和石缝旁，淡色液体流出形成湿痕，瓶身标签模糊不可读，真实小道具比例 | 不要可读品牌、可读警示文字、夸张毒液颜色、人物脸、字幕、水印、卡通、3D渲染 | Use PROP_ANTIFREEZE_BOTTLE_BASE, knocked over antifreeze bottle prop state, plastic bottle lying beside dirt ground and stone cracks in a rural yard, pale liquid spilled into wet marks, label blurred and unreadable, realistic small prop scale | no readable brand, readable warning text, exaggerated toxic color, human face, subtitles, watermark, cartoon, 3D render |
| STATE_SCENE_VILLAGE_ROAD_OVERCAST_PRESNOW_V1 | SCENE_VILLAGE_ROAD_BASE | BASE | scene | lighting_time | 暴雪前阴沉村口道路状态，路面湿暗，远处山路被灰色天幕压低 | 阴天冷光、村口道路、湿暗路面、山路灰天、车辆驶出空间 | episode_range | ep06 | 第4组 9-11秒 | yes | generate overcast pre snow village road state | candidate | 引用 SCENE_VILLAGE_ROAD_BASE，中国乡村村口道路暴雪前阴沉空镜，土路和简易水泥路湿暗，远处山路被灰色天幕压低，两侧低矮民房和田地，冷色阴天自然光，无人无人脸，真实交通空间 | 不要人物、人脸、人群、可读标语、品牌logo、字幕、水印，不要卡通、3D渲染、过曝、塑料感 | Use SCENE_VILLAGE_ROAD_BASE, empty Chinese village road before a snowstorm, dirt and simple concrete road dark and damp, distant mountain road pressed by gray sky, low houses and fields on both sides, cool overcast natural light, no people and no faces, realistic traffic space | no people, no faces, no crowd, no readable slogan, no brand logo, subtitles, watermark, cartoon, 3D render, overexposure, plastic texture |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| SCENE_LINGANG_HOME_YARD_BASE | scene | 林刚家院子 | 乡村家庭院子，院门、低矮院墙、泥地石缝和车辆停靠空间，基础资产为空镜 | episode_range | ep06 | candidate | 中国乡村家庭院子空镜，低矮院墙、院门、泥地和石缝，院内留有皮卡停靠空间，朴素生活痕迹，真实乡村比例，竖屏构图，无人无人脸，真人实拍电影质感 | 不要人物、人脸、人群、可读门牌、品牌logo、字幕、水印，不要豪宅化、卡通、3D渲染、塑料感 | Empty Chinese rural home yard, low courtyard wall, yard gate, dirt ground and stone cracks, space for a pickup to park, simple lived in rural texture, realistic scale, vertical composition, no people and no faces, live action cinematic still | no people, no faces, no crowd, no readable house number, no brand logo, subtitles, watermark, no mansion style, cartoon, 3D render, plastic texture |
| PROP_SNOW_CHAIN_BASE | prop | 防滑链 | 车辆轮胎防滑链，金属链条，冬季出车关键装备，可绕在皮卡前轮旁 | episode_range | ep06 | candidate | 汽车轮胎防滑链道具，银灰金属链条，链节粗细真实，可铺在轮胎旁或半绕在轮胎上，冬季道路装备质感，近景产品参考，无品牌文字 | 不要品牌logo、可读包装文字、人物脸、字幕、水印、卡通、3D渲染、塑料玩具感 | Vehicle snow chain prop, silver gray metal chains, realistic link thickness, can be laid beside a tire or partly wrapped around it, winter road equipment texture, close product reference, no brand text | no brand logo, readable package text, human face, subtitles, watermark, cartoon, 3D render, plastic toy look |
| PROP_ANTIFREEZE_BOTTLE_BASE | prop | 防冻液瓶子 | 车辆防冻液塑料瓶，淡色液体容器，标签不可读，是暴雪前准备和被踢翻的关键道具 | episode_range | ep06 | candidate | 车辆防冻液塑料瓶道具，半透明或浅色塑料瓶，瓶身有模糊标签但不可读，内部淡色液体，单手可拿比例，真实汽车养护用品质感 | 不要可读品牌、可读警示文字、二维码、人物脸、字幕、水印、卡通、3D渲染 | Vehicle antifreeze plastic bottle prop, translucent or light colored plastic bottle, blurred unreadable label, pale liquid inside, one hand scale, realistic car maintenance supply texture | no readable brand, readable warning text, QR code, human face, subtitles, watermark, cartoon, 3D render |
| PROP_VILLAGE_POLE_SPEAKER_BASE | prop | 村里大喇叭 | 固定在院外电线杆高处的村广播喇叭，金属或塑料扩音口，用于播报暴雪紧急通知 | episode_range | ep06 | candidate | 村里固定广播大喇叭道具，安装在乡村电线杆高处，灰白金属或塑料扩音口，支架和电线清楚，旧化但可用，真实乡村公共广播质感，无可读文字 | 不要可读标语、品牌logo、人物脸、字幕、水印、卡通、3D渲染、舞台音箱化 | Fixed village public address loudspeaker prop, mounted high on a rural utility pole, gray white metal or plastic horn, visible bracket and wires, aged but functional, realistic rural broadcast texture, no readable text | no readable slogan, brand logo, human face, subtitles, watermark, cartoon, 3D render, no stage speaker styling |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_LINGANG_HOME_YARD_OVERCAST_V1 | SCENE_LINGANG_HOME_YARD_BASE | scene | 林刚家院子阴天日景状态 | 第1组-第4组 | yes | new home yard state | 建议同步到asset_bible |
| STATE_VEHICLE_PICKUP_NEW_WINTER_PREP_V1 | VEHICLE_PICKUP_BASE | prop | 新皮卡冬季准备状态 | 第1组-第4组 | yes | new pickup condition | 建议同步到asset_bible |
| STATE_VEHICLE_OLD_VAN_OVERLOADED_V1 | VEHICLE_OLD_VAN_BASE | prop | 破面包车多人挤上后摇晃出村状态 | 第2组 6-11秒，第4组 4-11秒 | yes | overloaded van state | 建议同步到asset_bible |
| STATE_PROP_ANTIFREEZE_SPILLED_V1 | PROP_ANTIFREEZE_BOTTLE_BASE | prop | 防冻液瓶被踢翻洒开状态 | 第2组 0-2秒，第3组组首，第4组组首 | yes | spilled antifreeze state | 建议同步到asset_bible |
| STATE_SCENE_VILLAGE_ROAD_OVERCAST_PRESNOW_V1 | SCENE_VILLAGE_ROAD_BASE | scene | 暴雪前阴沉村口道路状态 | 第4组 9-11秒 | yes | pre snow road condition | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 最后一件行李、普通行李堆 | 第1组 0-2秒 | 一次性搬运行李，不是剧情线索，生产价值低 |
| 村民甲、村民乙的临时表情和嘲讽动作 | 第1组-第3组 | 群众角色和短暂表演，不建立跨集固定人物或状态 |
| 拍掌、抬头听广播、挥手催促、挤车动作 | 第3组-第4组 | 动作编排由分镜即时生成，不是资产状态 |
| 院外电线杆、电线、普通院墙局部 | 第3组 2-7秒 | 已由林刚家院子场景和村里大喇叭道具承载，不单独入库 |
| 防冻液湿痕的每一处流向 | 第2组-第4组 | 已归入防冻液洒出状态，不需要逐痕迹拆分 |
