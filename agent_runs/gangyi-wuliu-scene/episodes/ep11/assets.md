# 《刚毅物流 ep11》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP11_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | 第1组-第6组 | 林刚验车、发现制冷机故障、徒手接线并驾驶冷藏车离开 | conditional | if black oil repair state not generated |
| EP11_USE_CHAR_002 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | 第1组-第6组 | 王百川旁观验车、提醒货值并训斥王强 | no | reuse existing boss state |
| EP11_USE_CHAR_003 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | 第1组-第6组 | 王强带林刚看车、否认故障并暗中打电话叫人堵车 | no | reuse base character |
| EP11_USE_SCENE_001 | SCENE_LOGISTICS_YARD_BASE | STATE_SCENE_LOGISTICS_YARD_OVERCAST_REEFER_V1 | scene | asset_bible | 第1组-第6组 | 阴天货运场、冷藏车停放区、车头和大门附近 | conditional | if overcast reefer yard state not generated |
| EP11_USE_PROP_001 | VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | STATE_VEHICLE_REEFER_DIRTY_FAULTY_V1 | prop | episode_new | 第1组-第6组 | 老旧重型冷藏车作为送货挑战车辆并带故障状态 | yes | new core vehicle state |
| EP11_USE_PROP_002 | PROP_REEFER_CONTROL_PANEL_BASE | STATE_PROP_REEFER_PANEL_CUT_WIRES_V1 | prop | episode_new | 第3组 | 制冷机控制面板被撬开，内部两根电源线被新剪断 | yes | new evidence prop state |
| EP11_USE_PROP_003 | PROP_REEFER_CONTROL_PANEL_BASE | STATE_PROP_REEFER_PANEL_TAPED_REPAIR_V1 | prop | episode_new | 第4组 | 林刚用绝缘黑胶布接线并恢复制冷机运转 | yes | new repaired prop state |
| EP11_USE_PROP_004 | PROP_LINGANG_WRISTWATCH_BASE | BASE | prop | episode_new | 第5组 0-2秒 | 林刚查看手表确认抢修用时 | conditional | if ep10 wristwatch candidate not merged |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_LOGISTICS_YARD_OVERCAST_REEFER_V1 | SCENE_LOGISTICS_YARD_BASE | BASE | scene | lighting_time | 阴天日景货运场冷藏车停放区，地面潮湿泥点和车辙明显 | 阴天漫射光、潮湿车辙、泥点、冷藏车停放区、大门附近 | episode_range | ep11 | 第1组-第6组 | yes | generate overcast reefer yard state | candidate | 中国货运场冷藏车停放区空镜，阴天日景，开阔水泥地有潮湿车辙和泥点，货场棚架、堆货角落和大门可见，冷灰漫射光，无人无人脸，竖屏电影质感，真实工业物流环境 | 人物、人脸、人群、可读标牌、品牌logo、车牌号、卡通、3D渲染、塑料感、水印、字幕 | Empty vertical cinematic shot of a Chinese freight yard refrigerated truck parking area on an overcast day, wet tire ruts and mud spots on concrete, yard sheds, cargo corner and gate visible, cool gray diffuse light, no people, no faces, realistic industrial logistics environment | people, faces, crowds, readable signs, brand logos, license plates, cartoon style, 3D render, plastic look, watermark, subtitles |
| STATE_VEHICLE_REEFER_DIRTY_FAULTY_V1 | VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | BASE | prop | prop_condition | 满是泥污的老旧重型冷藏车，轮胎泥污、制冷机故障待查 | 车身泥污、轮胎胎纹、外挂制冷机、老旧金属外壳 | episode_range | ep11 | 第1组-第6组 | yes | generate dirty old refrigerated truck | candidate | 老旧重型冷藏车车辆资产，白色或浅灰冷藏厢体布满泥污，轮胎胎纹和潮湿泥点清楚，车头外挂制冷机外壳陈旧，阴天货运场环境，车身无品牌无车牌可读文字，真实比例 | 品牌logo、清晰车牌号、可读公司名称、人物脸、卡通、3D渲染、塑料感、水印、字幕 | Old heavy refrigerated truck vehicle asset, white or light gray refrigerated cargo body covered with mud, clear tire tread and wet mud spots, aged front-mounted refrigeration unit, overcast freight yard setting, no brand or readable license plate, realistic scale | brand logos, clear license plates, readable company names, faces, cartoon style, 3D render, plastic look, watermark, subtitles |
| STATE_VEHICLE_REEFER_COMPRESSOR_OIL_LEAK_V1 | VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | STATE_VEHICLE_REEFER_DIRTY_FAULTY_V1 | prop | prop_condition | 制冷机压缩机漏油，底盘面板和手掌出现黑油湿亮痕迹 | 压缩机漏油、底盘黑油、湿亮油迹 | episode_range | ep11 | 第2组 3-8秒 | yes | generate compressor oil leak detail | candidate | 老旧冷藏车车头制冷机和底盘面板特写，黑油从压缩机区域渗出并在金属面板上形成湿亮油迹，阴天冷灰光，真实维修检查质感，无品牌无可读文字 | 人物脸、品牌logo、可读文字、夸张爆炸、火焰、卡通、3D渲染、塑料感、水印、字幕 | Close-up of the refrigeration unit and underbody panel of an old refrigerated truck, black oil leaking from the compressor area and forming wet glossy stains on metal, cool overcast light, realistic maintenance inspection texture, no brand or readable text | faces, brand logos, readable text, exaggerated explosion, flames, cartoon style, 3D render, plastic look, watermark, subtitles |
| STATE_PROP_REEFER_PANEL_CUT_WIRES_V1 | PROP_REEFER_CONTROL_PANEL_BASE | BASE | prop | prop_condition | 制冷机控制面板打开，两根粗电源线被整齐剪断，铜丝断口新亮 | 面板打开、两根断线、铜丝新亮、灰尘油渍 | episode_range | ep11 | 第3组 0-10秒 | yes | generate cut wire evidence state | candidate | 冷藏车制冷机控制面板特写，面板被撬开，内部两根粗电源线整齐剪断，铜丝断口新亮，周围有灰尘和油渍，阴天冷光，真实车辆电路维修质感，无可读品牌文字 | 人物脸、额外文字标签、品牌logo、火花爆炸、科幻线路、卡通、3D渲染、水印、字幕 | Close-up of a refrigerated truck refrigeration control panel pried open, two thick power wires cleanly cut with fresh bright copper ends, dust and oil stains around the panel, cool overcast light, realistic vehicle electrical repair texture, no readable brand text | faces, extra text labels, brand logos, sparks or explosions, sci-fi wiring, cartoon style, 3D render, watermark, subtitles |
| STATE_PROP_REEFER_PANEL_TAPED_REPAIR_V1 | PROP_REEFER_CONTROL_PANEL_BASE | STATE_PROP_REEFER_PANEL_CUT_WIRES_V1 | prop | prop_condition | 断开的电源线被铜丝拧紧并用绝缘黑胶布缠成黑色结点，指示灯恢复亮起 | 铜丝拧接、黑胶布缠绕、指示灯亮、冷风雾气 | episode_range | ep11 | 第4组 0-11秒 | yes | generate taped repair state | candidate | 冷藏车制冷机控制面板抢修后状态，断线铜丝被拧接，绝缘黑胶布一圈圈缠成黑色结点，旁边指示灯发出冷绿亮点，少量冷风雾气贴着车头散开，真实维修细节，无品牌无可读文字 | 人物脸、额外文字标签、品牌logo、火花爆炸、科幻设备、卡通、3D渲染、塑料感、水印、字幕 | Repaired state of a refrigerated truck refrigeration control panel, cut copper wires twisted together and wrapped with black electrical tape into a dark joint, nearby indicator light glowing cold green, slight cold-air mist near the truck front, realistic repair detail, no brand or readable text | faces, extra text labels, brand logos, sparks or explosions, sci-fi devices, cartoon style, 3D render, plastic look, watermark, subtitles |
| STATE_LINGANG_BLACK_OIL_REPAIR_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | dirt_damage | 林刚验车抢修时手指和指节沾黑油，仍穿乡镇物流工装 | 手部黑油、维修动作、工装保持、表情不入库 | episode_range | ep11 | 第2组 3-8秒，第4组 0-8秒 | yes | generate if black oil hand continuity needed | candidate | 基于 CHAR_LINGANG_BASE 和 COSTUME_LINGANG_WORK_JACKET_V1 的林刚抢修状态，手指和指节沾黑油，深色工装保持乡镇物流工作服质感，正在冷藏车控制面板旁维修，脸型发型保持 asset_bible 设定，真人实拍电影质感 | 西方人脸、改换发型、改换脸型、血迹、品牌logo、可读文字、卡通、3D渲染、塑料感、水印、字幕 | Lin Gang repair state based on CHAR_LINGANG_BASE and COSTUME_LINGANG_WORK_JACKET_V1, fingers and knuckles stained with black oil, same dark logistics workwear, repairing beside a refrigerated truck control panel, same face shape and hair as the bible, realistic cinematic live-action look | Western face, changed hairstyle, changed face shape, blood, brand logos, readable text, cartoon style, 3D render, plastic look, watermark, subtitles |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | prop | 老旧重型冷藏车 | 本集送货挑战的核心车辆，老旧重型冷藏车，白色或浅灰冷藏厢体、外挂制冷机、重型轮胎，禁止品牌和车牌 | episode_range | ep11 | candidate | 老旧重型冷藏车基础资产，白色或浅灰冷藏厢体，车头外挂制冷机，重型轮胎和金属车身比例真实，车漆有运输磨损，车身无品牌logo无可读车牌号，当代中国货运场质感 | 品牌logo、清晰车牌号、可读公司名称、人物、人脸、卡通、3D渲染、塑料感、水印、字幕 | Old heavy refrigerated truck base asset, white or light gray refrigerated cargo body, front-mounted refrigeration unit, heavy tires and realistic metal body proportions, worn transport paint, no brand logo and no readable license plate, contemporary Chinese freight yard feel | brand logos, clear license plates, readable company names, people, faces, cartoon style, 3D render, plastic look, watermark, subtitles |
| PROP_REEFER_CONTROL_PANEL_BASE | prop | 冷藏车制冷机控制面板 | 冷藏车外挂制冷机的控制面板和内部线路，作为故障证据和抢修画面核心道具 | episode_range | ep11 | candidate | 冷藏车制冷机控制面板基础道具，金属或硬塑面板嵌在车头制冷机外壳上，可打开露出内部线路，螺丝孔、边框和线束结构清楚，无品牌无可读文字，真实车辆维修比例 | 可读品牌文字、警示标签特写、人物脸、科幻界面、火花爆炸、卡通、3D渲染、塑料玩具感、水印、字幕 | Refrigerated truck refrigeration control panel base prop, metal or hard plastic panel mounted on the front refrigeration unit, can open to reveal internal wiring, clear screw holes, frame and wire harness structure, no brand or readable text, realistic vehicle repair scale | readable brand text, warning label close-ups, faces, sci-fi interface, sparks or explosions, cartoon style, 3D render, toy-like plastic, watermark, subtitles |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_LOGISTICS_YARD_OVERCAST_REEFER_V1 | SCENE_LOGISTICS_YARD_BASE | scene | 阴天货运场冷藏车停放区状态 | 第1组-第6组 | yes | generate for all yard shots | 建议同步到asset_bible |
| STATE_VEHICLE_REEFER_DIRTY_FAULTY_V1 | VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | prop | 老旧泥污冷藏车故障待查状态 | 第1组-第6组 | yes | generate core vehicle state | 建议同步到asset_bible |
| STATE_VEHICLE_REEFER_COMPRESSOR_OIL_LEAK_V1 | VEHICLE_OLD_REFRIGERATED_TRUCK_BASE | prop | 制冷机压缩机漏油特写状态 | 第2组 3-8秒 | yes | generate oil leak detail | 建议同步到asset_bible |
| STATE_PROP_REEFER_PANEL_CUT_WIRES_V1 | PROP_REEFER_CONTROL_PANEL_BASE | prop | 控制面板打开且两根电源线被新剪断 | 第3组 0-10秒 | yes | generate evidence state | 建议同步到asset_bible |
| STATE_PROP_REEFER_PANEL_TAPED_REPAIR_V1 | PROP_REEFER_CONTROL_PANEL_BASE | prop | 断线被黑胶布缠紧后指示灯亮起 | 第4组 0-11秒 | yes | generate repaired state | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 螺丝刀、绝缘黑胶布、制冷机开关 | 第3组-第4组 | 属于一次性维修小工具和局部操作件，已由控制面板状态承载 |
| 黑油本身、指缝油亮、冷风雾气 | 第2组-第4组 | 属于故障状态和维修效果，不单独作为基础道具入库 |
| 王强掏手机拨号、手机屏幕冷光 | 第6组 | 普通手机通话动作，一次性剧情动作，无需稳定资产 |
| 货箱、堆货角落、驾驶室车门、车辙泥点 | 第1组-第6组 | 已由货运场场景状态和冷藏车车辆状态承载 |
| 王强脸色骤变、林刚皱眉、王百川铁青 | 第2组-第5组 | 短暂表情，属于表演，不拆成资产状态 |
