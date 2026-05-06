# 《刚毅物流 ep16》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP16_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | 第1组0-2秒，第1组10-12秒，第2组5-7秒，第3组0-2秒，第4组0-3秒，第5组7-10秒 | 林刚在废车回收站门口设局取证并对峙 | no | reuse existing character and township state |
| EP16_USE_CHAR_002 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | 第1组4-10秒，第2组0-9秒，第3组7-9秒，第4组3-6秒，第5组0-7秒 | 王强跟踪挑衅并被警察控制 | no | reuse base character |
| EP16_USE_CHAR_003 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | 第1组4-10秒，第2组3-11秒，第3组11-13秒，第4组8-10秒，第5组0-3秒 | 赵大强参与炫耀破坏并试图逃跑 | no | reuse villain state |
| EP16_USE_CHAR_004 | CHAR_POLICE_BASE | BASE | character | asset_bible | 第4组6-8秒，第5组0-5秒 | 执法人员冲下警车并上铐 | no | reuse police group asset |
| EP16_USE_PROP_001 | PROP_CRACKED_PHONE_BASE | STATE_PROP_PHONE_CRACKED_RECORDING_V1 | prop | asset_bible | 第4组0-3秒，第5组7-10秒 | 林刚展示监控和录音证据 | no | reuse existing phone recording state |
| EP16_USE_PROP_002 | PROP_HANDCUFFS_BASE | BASE | prop | asset_bible | 第5组3-5秒 | 警察扣住王强和赵大强手腕 | no | reuse handcuffs base prop |
| EP16_USE_PROP_003 | VEHICLE_POLICE_CAR_BASE | BASE | prop | asset_bible | 第4组3-8秒，第5组0-7秒 | 两辆警车冲进回收站并提供大灯压制 | no | reuse police vehicle base |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_RECYCLING_GATE_NIGHT_SMOKE_V1 | SCENE_RECYCLING_YARD_GATE_BASE | BASE | scene | scene_condition | 夜晚阴天的废车回收站门口，门灯昏黄，碎石地面，破重卡冒黑烟，车灯和警车灯扫过空间 | 光线时间，烟雾，车辆停放压迫感，碎石反光 | episode_range | ep16 | 第1组0-12秒，第2组0-11秒，第3组0-13秒，第4组0-10秒，第5组0-10秒 | yes | generate empty scene state without people | candidate | 当代中国废车回收站门口空镜，夜晚阴天，铁皮办公室和回收站大门，碎石地面有油污水痕，昏黄门灯与车辆大灯交叉照明，一辆报废重卡停在门口并从车头冒黑烟，无人无人脸，竖屏电影质感，真实材质和冷暖混合光 | 人物，人脸，人群，清晰品牌logo，可读车牌号，可读广告字，字幕，水印，卡通，3D渲染，塑料感，过曝，低清晰度 | Empty shot of a contemporary Chinese scrap vehicle recycling yard gate at night under cloudy sky, corrugated metal office and yard entrance, gravel ground with oil stains and wet reflections, warm yellow doorway lamp mixed with vehicle headlights, a scrapped heavy truck at the gate with black smoke rising from the front, no people, no faces, vertical cinematic realism, authentic industrial materials | people, faces, crowd, clear brand logo, readable license plate, readable signage, subtitles, watermark, cartoon, 3D render, plastic texture, overexposure, low resolution |
| STATE_VEHICLE_TRUCK_SCRAP_SMOKING_V1 | VEHICLE_HEAVY_TRUCK_BASE | STATE_VEHICLE_TRUCK_SABOTAGED_V1 | prop | prop_condition | 破重卡报废状态，发动机舱冒黑烟，车头停在回收站门口，外观破旧但仍保持重卡比例 | 报废外观，黑烟，车头故障，夜间大灯反光 | one_episode | ep16 | 第1组0-2秒，第2组5-9秒，第3组2-11秒，第5组7-10秒 | yes | if the smoking scrap state has not been generated | candidate | 基于大型物流重卡资产的报废破车状态，车身厚重但漆面斑驳，车头和发动机舱有黑烟上升，金属外壳带油污和旧划痕，夜晚车辆大灯和回收站门灯映出冷暖反光，无品牌logo，无车牌文字，真实手持或中景比例 | 清晰品牌logo，可读车牌号，爆炸火焰，夸张改装，卡通，玩具车比例，文字贴纸，水印，低清晰度 | Scrapped broken state based on a large logistics heavy truck, heavy body with chipped paint, black smoke rising from the front engine area, oily metal shell with old scratches, night headlights and recycling yard doorway lamp creating mixed reflections, no brand logo, no license plate text, realistic medium shot scale | clear brand logo, readable license plate, explosion flames, exaggerated custom parts, cartoon, toy scale, text stickers, watermark, low resolution |
| STATE_PROP_PHONE_RECORDING_EVIDENCE_V2 | PROP_CRACKED_PHONE_BASE | STATE_PROP_PHONE_CRACKED_RECORDING_V1 | prop | prop_condition | 手机作为监控和录音证据展示，屏幕亮光照到林刚手指和下颌，屏幕内容不显示可读信息 | 证据展示用途，屏幕冷光，不显示可读内容 | one_episode | ep16 | 第4组0-3秒，第5组7-10秒 | conditional | if close-up evidence phone state is needed | no | 黑色智能手机证据展示状态，手掌比例，屏幕发出冷白亮光但没有可读文字和具体应用界面，边缘有使用磨损，适合近景照亮手指和下颌，真实材质，无品牌logo | 可读聊天内容，可读录像文字，品牌logo，字幕，水印，过曝屏幕，卡通，3D渲染，畸形手指 | Black smartphone used as evidence display, palm-sized scale, screen emits cool white light without readable text or specific app interface, worn edges, suitable for close-up light on fingers and jaw, realistic material, no brand logo | readable chat text, readable recording text, brand logo, subtitles, watermark, overexposed screen, cartoon, 3D render, malformed fingers |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| SCENE_RECYCLING_YARD_GATE_BASE | scene | 废车回收站门口 | 当代乡镇或县郊废车回收站入口，铁皮办公室，院门，碎石和油污地面，可停放报废车辆；基础资产必须为空镜 | episode_range | ep16 | candidate | 当代中国县郊废车回收站门口空镜，铁皮办公室靠近院门，旧金属门框，碎石地面混有油污和水痕，背景有废旧车辆轮廓和低矮围挡，基础夜间或白天都可扩展，无人无人脸，竖屏电影质感，真实工业材质 | 人物，人脸，人群，清晰品牌logo，可读车牌号，可读招牌文字，字幕，水印，卡通，3D渲染，塑料感，过度美化 | Empty shot of a contemporary Chinese suburban scrap vehicle recycling yard gate, corrugated metal office near the entrance, old metal gate frame, gravel ground with oil stains and wet marks, silhouettes of scrapped vehicles and low fencing in the background, extendable for day or night states, no people, no faces, vertical cinematic realism | people, faces, crowd, clear brand logo, readable license plate, readable sign text, subtitles, watermark, cartoon, 3D render, plastic texture, overly polished look |
| CHAR_RECYCLING_BOSS_BASE | character | 回收站老板 | 废车回收站老板，成年男性，站在铁皮办公室门口，能自然提起大铁锤；仅记录稳定身份和外观，不写本集台词表情 | one_episode | ep16 | candidate | 中国县郊废车回收站老板，40到50岁男性，中等偏壮体态，脸部有风吹日晒痕迹，短发，穿旧工装外套和耐磨裤，气质粗粝务实，站姿稳定，真人实拍电影质感，竖屏角色定妆照 | 西方人脸，夸张肌肉，黑帮造型，品牌logo，可读文字，卡通，3D渲染，塑料皮肤，过度精修 | Chinese suburban scrap yard owner, male in his 40s to 50s, medium sturdy build, weathered face, short hair, old work jacket and durable pants, rough practical temperament, stable stance, live-action cinematic character reference, vertical framing | Western face, exaggerated muscles, gangster styling, brand logo, readable text, cartoon, 3D render, plastic skin, over-retouched look |
| VEHICLE_BLACK_SEDAN_BASE | prop | 黑轿车 | 王强和赵大强跟踪林刚使用的黑色轿车，夜间车灯强，可作为反派交通工具临时复用 | one_episode | ep16 | candidate | 黑色普通轿车道具，车身低调无豪车品牌特征，夜间大灯明亮，车门漆面可反射警车灯和手电光，车牌不可读，无品牌logo，真实中国县城道路车辆比例 | 清晰车牌号，品牌logo，豪华超跑外观，夸张改装，字幕，水印，卡通，3D渲染，玩具车比例 | Ordinary black sedan prop, understated body without luxury brand traits, bright headlights at night, glossy doors reflecting police lights and flashlight beams, unreadable license plate, no brand logo, realistic Chinese county-road vehicle scale | readable license plate, brand logo, luxury supercar design, exaggerated tuning, subtitles, watermark, cartoon, 3D render, toy scale |
| PROP_FLASHLIGHT_BASE | prop | 手电筒 | 王强和赵大强手持照向破重卡驾驶室的普通手电筒，掌心尺寸，强冷白光束 | one_episode | ep16 | candidate | 普通手电筒道具，掌心到小臂长度，黑色金属或塑料外壳，前端透镜发出冷白光束，表面有轻微划痕，无品牌logo，适合夜间近景和手持动作 | 品牌logo，可读文字，科幻武器造型，过曝光团，卡通，3D渲染，水印，畸形手部 | Ordinary flashlight prop, palm-to-forearm length, black metal or plastic body, front lens emitting a cool white beam, lightly scratched surface, no brand logo, suitable for night close-ups and handheld action | brand logo, readable text, sci-fi weapon design, blown-out light blob, cartoon, 3D render, watermark, malformed hand |
| PROP_SLEDGEHAMMER_BASE | prop | 大铁锤 | 回收站老板提在身侧的重型铁锤，用于砸报废车，金属锤头和木柄或深色手柄 | one_episode | ep16 | candidate | 重型大铁锤道具，厚重金属锤头带磨损和油污，长木柄或深色手柄，比例适合成年人单手垂提，夜间车灯在锤头边缘形成冷光反射，无品牌无文字 | 血迹，夸张武器化造型，品牌logo，可读文字，卡通，3D渲染，水印，比例失真 | Heavy sledgehammer prop, worn oily metal head, long wooden or dark handle, adult scale for being held down at one side, night vehicle light creating cool highlights on the hammer edge, no brand, no text | blood stains, exaggerated weaponized design, brand logo, readable text, cartoon, 3D render, watermark, distorted scale |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_RECYCLING_GATE_NIGHT_SMOKE_V1 | SCENE_RECYCLING_YARD_GATE_BASE | scene | 夜晚阴天回收站门口，破重卡冒黑烟，车灯和警车灯扫过碎石地面 | 第1组0-12秒，第2组0-11秒，第3组0-13秒，第4组0-10秒，第5组0-10秒 | yes | recurring setting for this episode and possible later flashback use | 建议同步到asset_bible |
| STATE_VEHICLE_TRUCK_SCRAP_SMOKING_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 报废重卡冒黑烟，外观破旧，车头停在回收站门口 | 第1组0-2秒，第2组5-9秒，第3组2-11秒 | yes | derived from existing heavy truck with scrap smoking state | 建议同步到asset_bible |
| BASE | VEHICLE_BLACK_SEDAN_BASE | prop | 黑轿车急刹停在破重卡后方，后续作为压制和反光载体 | 第1组2-10秒，第2组组首，第4组8-10秒，第5组0-5秒 | yes | new episode vehicle prop | 仅本集使用 |
| BASE | PROP_FLASHLIGHT_BASE | prop | 王强和赵大强手持手电扫向驾驶室，形成夜间下方冷光 | 第1组4-10秒，第2组0-9秒，第3组7-9秒 | yes | repeated handheld lighting prop in the episode | 仅本集使用 |
| BASE | PROP_SLEDGEHAMMER_BASE | prop | 回收站老板提着大铁锤出场并询问是否砸车 | 第3组2-7秒，第4组组首，第5组组首 | yes | new prop tied to scrap yard owner | 可候选同步到asset_bible |
| BASE | PROP_HANDCUFFS_BASE | prop | 手铐扣住王强和赵大强手腕 | 第5组3-5秒 | no | already in asset_bible | 复用已有状态 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 王强大笑、冷笑、咬牙等表情 | 第1组6-10秒，第2组7-9秒，第5组5-7秒 | 属于分镜表演和短暂情绪，不是可复用资产状态 |
| 赵大强抬下巴、拍手、腿软后缩 | 第1组6-10秒，第2组9-11秒，第4组8-10秒 | 属于一次性动作表演，不单独入库 |
| 碎石、油污、水痕和门灯反光 | 多组回收站门口镜头 | 已由回收站场景基础资产和夜间状态承载，不拆成道具 |
| 车窗反光和车门亮边 | 第1组组首，第5组0-5秒 | 属于车辆和灯光状态的画面效果，不是独立资产 |
| 警察冲下车、按肩膀、挡退路动作 | 第4组6-8秒，第5组0-3秒 | 属于调度动作，复用警察角色和警车资产即可 |
