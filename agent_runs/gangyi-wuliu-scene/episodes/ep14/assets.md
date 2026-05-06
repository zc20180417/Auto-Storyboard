# 《刚毅物流 ep14》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP14_USE_CHAR_001 | CHAR_LINGANG_BASE | BASE | character | asset_bible | ep14 第1组0-13秒，第2组0-11秒，第3组0-13秒，第4组0-5秒 | 林刚在银行门口提箱、撕旧账本并离开 | conditional | use existing base; outfit detail is not explicitly stable in this episode |
| EP14_USE_CHAR_002 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep14 第4组0-8秒 | 赵大强藏在树后煽动村民冲击车场 | no | reuse existing villain state |
| EP14_USE_PROP_001 | PROP_LEDGER_BASE | STATE_PROP_LEDGER_TORN_EP14 | prop | episode_variant | ep14 第2组0-11秒，第3组0-3秒，第4组0-5秒 | 林刚展示旧账本后撕碎，碎纸片落到村民脸上和地面 | conditional | if torn ledger state not generated |
| EP14_USE_VEHICLE_001 | VEHICLE_PICKUP_BASE | BASE | prop | asset_bible | ep14 第3组10-13秒，第4组0-5秒 | 路边皮卡作为林刚离开银行门口的车辆 | no | reuse existing pickup vehicle base |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_PROP_LEDGER_TORN_EP14 | PROP_LEDGER_BASE | BASE | prop | prop_condition | 旧运输账本被林刚撕成碎纸片，纸片砸到村民脸上后散落银行门口地面 | paper_condition | one_episode | ep14 | ep14 第2组8-11秒，第3组0-3秒，第4组0-5秒 | yes | generate torn ledger and scattered paper state if needed | no | 旧运输账本道具被撕碎后的状态，泛黄纸页变成不规则碎纸片，部分纸屑散落在水泥地上，纸面仅有模糊表格感不可读，晴天日光，真实手持和落地比例，电影质感 | 可读账目文字，真实个人信息，品牌logo，字幕，水印，卡通，3D渲染，塑料感，过度整齐纸片 | Torn old transport ledger prop, yellowed pages ripped into irregular paper scraps, some pieces scattered on cement ground, only blurred table texture with no readable text, sunny daylight, realistic hand and ground scale, cinematic realism | readable account text, real personal information, brand logo, subtitles, watermark, cartoon, 3D render, plastic texture, overly neat paper scraps |
| STATE_SCENE_BANK_ENTRANCE_DAY_EP14 | SCENE_BANK_ENTRANCE_BASE | BASE | scene | lighting_time | 晴天银行门口空镜，台阶、水泥空地和路边区域清晰，可承载围堵和清路调度 | light, layout | episode_range | ep14 | ep14 第1组0-13秒，第2组0-11秒，第3组0-13秒，第4组0-10秒 | yes | generate bank entrance empty scene state | candidate | 日间晴天的中国县城银行门口空镜，银行大门和台阶位于背景中央，门前水泥空地连接路边，阳光明亮，地面反光清楚，无人无人脸，真实城市边缘质感，竖屏构图 | 人物，人脸，人群，背影，银行真实logo，可读招牌，车牌号，字幕，水印，卡通，3D渲染，塑料感 | Empty daytime sunny entrance of a Chinese county bank, bank doors and steps centered in the background, cement forecourt connected to the roadside, bright sunlight and clear ground reflection, no people and no faces, realistic urban edge texture, vertical composition | people, faces, crowd, back view figures, real bank logo, readable signboard, license plate, subtitles, watermark, cartoon, 3D render, plastic texture |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| SCENE_BANK_ENTRANCE_BASE | scene | 银行门口与路边空地 | 县城银行门口外部空间，包含大门、台阶、水泥空地和路边皮卡停靠区域，场景基础资产必须为空镜 | episode_range | ep14 | candidate | 中国县城银行门口外部空镜，玻璃大门和台阶，门前水泥空地连接路边停靠区，晴天自然光，地面轻微反光，建筑真实但无可读银行品牌，无人无人脸，电影质感，竖屏构图 | 人物，人脸，人群，真实银行logo，可读招牌，车牌号，字幕，水印，卡通，3D渲染，塑料感 | Exterior empty shot of a Chinese county bank entrance, glass doors and steps, cement forecourt connected to a roadside parking area, sunny natural light, slight ground reflection, realistic building without readable bank branding, no people and no faces, cinematic realism, vertical composition | people, faces, crowd, real bank logo, readable signboard, license plate, subtitles, watermark, cartoon, 3D render, plastic texture |
| CHAR_VILLAGER_DEBTORS_BASE | character | 讨债村民甲乙及村民群像 | 中国乡村村民群像，可包含中年男性和女性，衣着朴素旧外套，表情焦急愤怒，用于银行围堵和被煽动场面，不固定单一脸 | episode_range | ep14 | candidate | 中国乡村讨债村民群像，30到60岁男女混合，朴素旧夹克和深色长裤，体态高矮胖瘦不同，面部真实不重复，围堵时焦急愤怒，真人实拍电影质感，竖屏群像定妆 | 卡通，3D渲染，塑料感，西方人脸，复制脸，统一制服，品牌标志，可读标语，字幕，水印 | Chinese rural debtor villagers crowd, mixed men and women aged 30 to 60, plain old jackets and dark trousers, varied body types, realistic non duplicated faces, anxious and angry during a blockade, live action cinematic realism, vertical crowd look image | cartoon, 3D render, plastic texture, western faces, cloned faces, identical uniforms, brand logos, readable slogans, subtitles, watermark |
| PROP_BLACK_CASH_SUITCASES_BASE | prop | 两个黑色大皮箱 | 两个黑色大皮箱，硬壳或皮革质感，尺寸偏大，可手提，剧情中被村民认为装钱，不出现品牌和可读文字 | episode_range | ep14 | candidate | 两个黑色大皮箱道具，硬壳或旧皮革表面，边角有轻微磨损，金属扣件低调反光，可手提的大尺寸比例，放在水泥地或手边，无品牌无文字，真人实拍电影质感 | 品牌logo，可读文字，现金外露，夸张珠宝，卡通，3D渲染，塑料感，字幕，水印 | Two large black suitcases prop, hard shell or aged leather surface, slightly worn corners, subtle metal latch highlights, large hand carried scale, placed on cement ground or beside hands, no brand and no text, live action cinematic realism | brand logo, readable text, exposed cash, exaggerated jewelry, cartoon, 3D render, plastic texture, subtitles, watermark |
| CHAR_BANK_SECURITY_BASE | character | 持棍银行保安群像 | 银行门边四个持棍保安，成年男性为主，深色保安服或夹克，动作整齐，用于清路驱散围堵村民 | one_episode | ep14 | candidate | 中国县城银行保安群像，四名成年男性，深色保安制服或深色夹克，体态普通偏结实，短发，手持木棍清路，表情严肃，真人实拍电影质感，竖屏群像定妆 | 警察制服，特警装备，西方人脸，复制脸，品牌logo，可读文字，卡通，3D渲染，塑料感，字幕，水印 | Chinese county bank security guards crowd, four adult men, dark security uniforms or dark jackets, average sturdy bodies, short hair, holding wooden sticks to clear a path, serious expressions, live action cinematic realism, vertical group look image | police uniform, SWAT gear, western faces, cloned faces, brand logo, readable text, cartoon, 3D render, plastic texture, subtitles, watermark |
| PROP_SECURITY_WOODEN_STICK_BASE | prop | 保安木棍 | 普通木棍，约手臂长度，表面有磨损，用于保安清路，不带文字和品牌 | one_episode | ep14 | no | 普通保安木棍道具，手臂长度，木质表面有使用磨损，圆柱形棍身，手持比例真实，无品牌无文字，真人实拍电影质感 | 血腥，倒刺，金属武器，品牌logo，可读文字，卡通，3D渲染，塑料感，字幕，水印 | Ordinary security wooden stick prop, arm length, used worn wooden surface, cylindrical body, realistic hand held scale, no brand and no text, live action cinematic realism | gore, spikes, metal weapon, brand logo, readable text, cartoon, 3D render, plastic texture, subtitles, watermark |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_BANK_ENTRANCE_DAY_EP14 | SCENE_BANK_ENTRANCE_BASE | scene | 晴天银行门口空镜，承载围堵、撕账本、保安清路和树后煽动 | ep14 第1组0-13秒，第2组0-11秒，第3组0-13秒，第4组0-10秒 | yes | new bank entrance scene state | 建议同步到asset_bible候选 |
| BASE | PROP_BLACK_CASH_SUITCASES_BASE | prop | 两个黑色大皮箱，林刚从银行拎出并放到水泥地上 | ep14 第1组0-13秒，第2组0-3秒，第3组0-13秒，第4组0-5秒 | yes | new black suitcase prop | 建议同步到asset_bible候选 |
| STATE_PROP_LEDGER_TORN_EP14 | PROP_LEDGER_BASE | prop | 旧账本撕碎后变成碎纸片，砸到村民脸上并散落地面 | ep14 第2组8-11秒，第3组0-3秒，第4组0-5秒 | yes | new torn ledger state | 仅本集使用 |
| BASE | CHAR_BANK_SECURITY_BASE | character | 四个持棍保安从银行门边冲出清路 | ep14 第3组5-13秒，第4组组首背景 | yes | new one episode security crowd | 仅本集使用，主线程可视后续复用决定 |
| BASE | VEHICLE_PICKUP_BASE | prop | 路边皮卡停在银行门口右后方，林刚提箱走向车辆 | ep14 第3组10-13秒，第4组组首 | no | reuse existing pickup base | 复用已有基础资产 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 银行大门和台阶 | ep14 第1组到第4组 | 已由银行门口场景基础资产承载，不单独作为道具入库 |
| 树干和树影 | ep14 第4组0-8秒 | 路边环境遮挡元素，可由场景即时生成，不是独立跨集资产 |
| 村民哭喊、跪地、抱裤腿、握拳 | ep14 第1组0-13秒，第4组8-10秒 | 短暂表演动作和情绪，不是人物状态资产 |
| 碎纸片贴脸动作 | ep14 第3组0-3秒，第4组0-5秒 | 已归入旧账本撕碎状态，不再单独建道具 |
| 保安拉拽村民的临时站位 | ep14 第3组7-13秒 | 调度动作来自分镜，后续镜头即时生成即可 |
