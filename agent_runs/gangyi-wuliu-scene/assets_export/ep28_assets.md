# 《刚毅物流 ep28》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP28_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | ep28 第1组-第5组 | 林刚带车队抢时抵达码头、对峙码头主管和混混、脱外套准备破局 | no | reuse existing convoy leader state |
| EP28_USE_CHAR_002 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | ep28 第1组-第5组 | 王百川在码头催装、解释加急费、面对违约风险 | no | reuse existing boss state |
| EP28_USE_CHAR_003 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | ep28 第3组-第5组 | 王强带赵大强和刀疤现身，挑衅林刚并封锁吊装 | no | reuse existing character base |
| EP28_USE_CHAR_004 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep28 第3组-第5组 | 赵大强参与码头堵局，揭出收买主管和电闸全拔 | no | reuse existing villain state |
| EP28_USE_CHAR_005 | CHAR_POLICE_BASE | STATE_GANGYI_DRIVERS_V1 | character | asset_bible | ep28 第1组、第2组、第5组 | 刚毅重卡司机群像降下车厢挡板、等待吊装、被围堵时停在车辆旁 | no | reuse existing driver crowd proxy |
| EP28_USE_SCENE_001 | SCENE_PORT_BASE | STATE_SCENE_PORT_CONFLICT_DAY_V1 | scene | asset_bible | ep28 第1组-第5组 | 国际码头外侧泊位、吊装区、集装箱堆垛和通道的晴天冲突主场景 | no | reuse existing port day conflict state |
| EP28_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | ep28 第1组-第5组 | 五十台满载货物的刚毅重卡车队、货箱挡板和码头队列 | no | reuse existing heavy truck asset |
| EP28_USE_COMP_001 | COMPOSITION_PORT_CONVOY_V1 | BASE | composition | asset_bible | ep28 第1组、第5组 | 重卡车队抵达码头、车辆与集装箱形成纵深列阵 | no | reuse existing port convoy composition |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_PORT_CRANE_STOPPED_V1 | SCENE_PORT_BASE | STATE_SCENE_PORT_CONFLICT_DAY_V1 | scene | scene_condition | 国际码头吊装区晴天停摆，龙门吊吊钩悬空，重卡挡板降下等待吊装 | 停摆龙门吊、吊钩悬空、车厢挡板降下、紧张等待 | episode_range | ep28 | ep28 第2组-第5组 | yes | generate stopped crane port state if not available | candidate | 国际码头吊装区空镜，晴天硬光，巨型龙门吊停在半空，吊钩垂下不动，重卡停放区和集装箱堆垛清晰，部分货箱挡板已经降下，地面水泥与金属阴影真实，无人无人脸，竖屏电影构图 | 人物、人脸、人群、可读车牌、真实品牌logo、字幕、水印、卡通、3D渲染、过曝、塑料感 | Empty international port loading area in bright hard daylight, giant gantry cranes stopped in midair, hooks hanging still, heavy truck parking lanes and container stacks clearly visible, some cargo box side panels lowered, realistic concrete ground and metal shadows, no people, no faces, vertical cinematic framing | people, faces, crowds, readable license plates, real brand logos, subtitles, watermark, cartoon, 3D render, overexposure, plastic texture |
| STATE_LINGANG_PORT_JACKET_OFF_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | costume_change | 林刚在围堵中心脱下外套，外套垂在一侧手臂上，准备正面压场 | 外套脱下、手臂挂外套、站姿更硬朗 | one_episode | ep28 | ep28 第5组 9-13秒 | yes | generate if jacket-off continuity is needed | no | 林刚基于 CHAR_LINGANG_BASE 和 COSTUME_LINGANG_WORK_JACKET_V1 的码头脱外套状态，深色工装外套被脱下垂在一侧手臂上，内搭普通深色上衣，站姿稳定，晴天港口硬光，真人实拍电影质感 | 换脸、改变发型、改变体态、夸张肌肉、品牌logo、字幕、水印、卡通、3D渲染、西方人面孔 | Lin Gang jacket-off state based on CHAR_LINGANG_BASE and COSTUME_LINGANG_WORK_JACKET_V1, dark work jacket removed and hanging over one forearm, plain dark inner shirt, steady stance, hard daylight at the port, live-action cinematic texture | changed face, changed hairstyle, changed body type, exaggerated muscles, brand logo, subtitles, watermark, cartoon, 3D render, Western face |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_DOCK_SUPERVISOR_BASE | character | 码头主管 | 港口吊装区主管，中年男性，肚腹微凸，夹公文包，表面冷淡但遇强势压迫会慌张 | episode_range | ep28 | candidate | 中国港口码头主管定妆照，40多岁男性，中等偏胖，肚腹微凸，短发整齐，穿深色商务夹克或港口管理外套，腋下夹普通黑色公文包，神情冷淡又心虚，真人实拍电影质感，竖屏半身到全身参考 | 西方人面孔、夸张反派妆、品牌logo、可读工牌、字幕、水印、卡通、3D渲染、塑料感 | Chinese port operations supervisor character reference, man in his forties, medium build with slight belly, neat short hair, dark business jacket or port management coat, plain black briefcase under one arm, cold but nervous expression, live-action cinematic texture, vertical half-body to full-body reference | Western face, exaggerated villain makeup, brand logo, readable badge, subtitles, watermark, cartoon, 3D render, plastic texture |
| CHAR_DAOBA_BASE | character | 刀疤 | 码头一霸，壮汉打手头目，满脸刀疤，凶狠压迫，负责带混混围堵吊装区 | episode_range | ep28 | candidate | 中国码头打手头目定妆照，30多岁到40岁男性，壮硕宽肩，脸上有明显旧刀疤但不血腥，短发，穿深色背心或粗糙夹克，眼神凶狠，港口工业背景虚化，真人实拍电影质感，竖屏角色参考 | 西方人面孔、新鲜血腥伤口、过度恐怖妆、品牌logo、字幕、水印、卡通、3D渲染、面部畸形 | Chinese dock enforcer leader character reference, man in his thirties or forties, broad and muscular, visible old facial scars without gore, short hair, dark vest or rough jacket, fierce eyes, blurred industrial port background, live-action cinematic texture, vertical character reference | Western face, fresh bloody wounds, horror makeup, brand logo, subtitles, watermark, cartoon, 3D render, facial distortion |
| CHAR_DOCK_GANG_BASE | character | 码头混混群像 | 码头通道和车辆缝隙中涌出的临时打手群像，可持铁钩和砍刀但不固定单人脸 | episode_range | ep28 | candidate | 中国码头混混群像参考，成年男性为主，深色廉价外套、背心和工装混搭，体态参差，手持铁钩或砍刀形成威胁感，不固定具体脸，港口集装箱通道背景，真人实拍电影质感 | 固定单人脸、清晰个人身份、真实帮派标志、品牌logo、血腥、字幕、水印、卡通、3D渲染、西方人面孔 | Chinese dock thug crowd reference, mostly adult men, mixed cheap dark jackets, vests, and workwear, varied body types, some holding hooks or machetes for threat, no fixed individual faces, container passage background, live-action cinematic texture | fixed individual face, clear personal identity, real gang symbol, brand logo, gore, subtitles, watermark, cartoon, 3D render, Western face |
| PROP_DOCK_WEAPONS_BASE | prop | 码头铁钩与砍刀 | 码头混混用于威胁的铁钩和砍刀组合，道具级别保留金属形态，不展示血迹 | episode_range | ep28 | candidate | 码头混混武器道具组合，旧铁钩和普通砍刀摆在水泥地或手持比例参考中，金属有磨损和冷亮反光，无血迹，无品牌，无可读文字，真实港口冲突道具质感，竖屏道具参考 | 血迹、断肢、品牌logo、可读文字、过度奇幻武器、字幕、水印、卡通、3D渲染 | Dock thug weapon prop set, worn iron hooks and plain machetes shown on concrete ground or in handheld scale reference, scuffed metal with cold highlights, no blood, no brand, no readable text, realistic port-conflict prop texture, vertical prop reference | blood, severed limbs, brand logo, readable text, fantasy weapon design, subtitles, watermark, cartoon, 3D render |
| PROP_BLACK_BRIEFCASE_BASE | prop | 码头主管公文包 | 码头主管夹在腋下的普通黑色公文包，作为其身份和收买关系的随身物 | one_episode | ep28 | no | 普通黑色公文包道具，商务硬壳或仿皮材质，边角轻微磨损，夹在腋下或单独摆放均可参考，无品牌logo，无可读文字，真实工作场景质感 | 品牌logo、可读文件、现金外露、夸张奢侈品外观、字幕、水印、卡通、3D渲染 | Plain black briefcase prop, business hard shell or faux leather texture, slightly worn corners, usable as under-arm or standalone reference, no brand logo, no readable text, realistic workplace texture | brand logo, readable documents, exposed cash, exaggerated luxury design, subtitles, watermark, cartoon, 3D render |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_PORT_CONFLICT_DAY_V1 | SCENE_PORT_BASE | scene | 国际码头重卡停放区白天冲突状态 | ep28 第1组-第5组 | no | reuse existing port conflict day state | 复用已有状态 |
| STATE_SCENE_PORT_CRANE_STOPPED_V1 | SCENE_PORT_BASE | scene | 龙门吊停摆、吊钩悬空、货箱挡板降下等待吊装 | ep28 第2组-第5组 | yes | generate stopped crane scene state | 建议同步到asset_bible |
| BASE | VEHICLE_HEAVY_TRUCK_BASE | prop | 满载刚毅重卡和车厢挡板 | ep28 第1组-第5组 | no | reuse heavy truck base and generate shot-specific side panels if needed | 复用已有基础资产 |
| BASE | PROP_DOCK_WEAPONS_BASE | prop | 铁钩和砍刀用于混混围堵威胁 | ep28 第5组 0-13秒 | yes | generate dock weapon prop set | 建议同步到asset_bible |
| BASE | PROP_BLACK_BRIEFCASE_BASE | prop | 码头主管夹着的黑色公文包 | ep28 第2组-第4组 | yes | generate only if supervisor prop continuity is needed | 仅本集使用 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 远洋货轮、普通货物、车厢挡板边缘 | ep28 第1组 | 作为港口和重卡场景陈设或车辆局部状态承载，不需要拆成独立基础资产 |
| 擦汗、摊手、后退、抬手指人、吹口哨 | ep28 第1组-第5组 | 短暂表演动作，不是稳定资产状态 |
| 吊钩阴影、地面投影、金属高光 | ep28 第2组-第5组 | 光影与镜头表现元素，由场景状态和分镜即时生成 |
| 临时站位的重卡司机和围堵群众单人脸 | ep28 第1组、第5组 | 群像不固定单人脸，避免误建跨集角色 |
| 十万块、电闸全拔等台词信息 | ep28 第4组 | 剧情信息通过台词表达，不建立可读文字或现金道具资产 |
