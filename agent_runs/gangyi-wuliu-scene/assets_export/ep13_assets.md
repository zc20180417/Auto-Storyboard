# 《刚毅物流 ep13》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP13_USE_CHAR_001 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep13 第1组0-10秒，第2组0-10秒，第3组0-11秒 | 赵大强被村民逼债、接王强电话并挥刀逃脱 | no | reuse existing villain identity and costume base |
| EP13_USE_CHAR_002 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | ep13 第2组3-10秒，第3组0-4秒 | 王强只以电话画外音出现，作为后续合谋关系引用 | no | voice only, visual generation not required in this episode |
| EP13_USE_CHAR_003 | CHAR_LINGANG_BASE | STATE_LINGANG_BUSINESS_SUIT_EP13 | character | episode_variant | ep13 第4组0-13秒 | 林刚在总裁办公室与王百川谈刚毅物流合同和购车资金 | conditional | if business suit state not generated |
| EP13_USE_CHAR_004 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | ep13 第4组0-13秒 | 王百川坐在办公室审核合同并询问首批重卡 | no | reuse existing boss state |
| EP13_USE_PROP_001 | PROP_CONTRACT_BASE | STATE_PROP_CONTRACT_SIGNED_V1 | prop | asset_bible | ep13 第4组0-6秒，第4组8-13秒 | 茶几上的签好字物流合同，推动合作和购车话题 | no | reuse signed contract state |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_ZHAODAQIANG_BEATEN_DIRTY_EP13 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | dirt_damage | 赵大强被村民围殴后蜷在墙角，旧夹克起皱沾灰，脸和肩背有被打乱的狼狈感 | 服装皱旧沾灰，姿态蜷缩，肩背受击后的狼狈状态 | one_episode | ep13 | ep13 第1组0-10秒，第2组0-10秒，第3组0-6秒 | yes | generate if beating aftermath continuity is needed | no | 基于 CHAR_ZHAODAQIANG_BASE 和 COSTUME_ZHAODAQIANG_DARK_JACKET_V1，赵大强缩在破旧室内墙角，深色旧夹克皱起并沾灰，肩背和脸部带被殴打后的狼狈痕迹，阴天窗光，真人实拍电影质感，竖屏角色状态图 | 卡通，3D渲染，塑料感，西方人脸，夸张血腥，新增纹身，品牌标志，可读文字，字幕，水印 | Based on CHAR_ZHAODAQIANG_BASE and COSTUME_ZHAODAQIANG_DARK_JACKET_V1, Zhao Daqiang crouches in a shabby interior corner, his dark old jacket wrinkled and dusty, his shoulders and face showing a messy beaten aftermath, overcast window light, live action cinematic realism, vertical character state image | cartoon, 3D render, plastic texture, western face, excessive gore, new tattoos, brand logo, readable text, subtitles, watermark |
| STATE_LINGANG_BUSINESS_SUIT_EP13 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | costume_change | 林刚在总裁办公室谈合同时穿更正式的深色西装或商务外套，状态沉稳挺拔 | 服装从工装变为深色商务装，场景从乡镇工作现场转为正式办公室 | episode_range | ep13 | ep13 第4组0-13秒 | yes | generate if office negotiation state is not in the bible | candidate | 基于 CHAR_LINGANG_BASE，林刚穿深色西装或深色商务外套，内搭浅色衬衫，站姿挺拔克制，保持黑色短寸发和硬朗国字脸，晴天办公室窗光，真人实拍电影质感，竖屏角色定妆 | 卡通，3D渲染，塑料感，西方人脸，改变脸型发型，鲜艳潮牌，品牌标志，可读文字，字幕，水印 | Based on CHAR_LINGANG_BASE, Lin Gang wears a dark suit or dark business jacket with a light shirt, upright and restrained, keeping the short black crew cut and rugged square face, sunny office window light, live action cinematic realism, vertical character look image | cartoon, 3D render, plastic texture, western face, changed face shape or hairstyle, flashy fashion brand, brand logo, readable text, subtitles, watermark |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_VILLAGER_DEBTORS_BASE | character | 讨债村民甲乙及村民群像 | 中国乡村村民群像，可包含中年男性和女性，衣着朴素旧外套，表情焦急愤怒，用于逼债、围堵和被煽动场面，不固定单一脸 | episode_range | ep13 | candidate | 中国乡村讨债村民群像，30到60岁男女混合，朴素旧夹克和深色长裤，体态高矮胖瘦不同，面部真实不重复，焦急愤怒的群体状态，真人实拍电影质感，竖屏群像定妆 | 卡通，3D渲染，塑料感，西方人脸，复制脸，统一制服，品牌标志，字幕，水印，可读标语 | Chinese rural debtor villagers crowd, mixed men and women aged 30 to 60, plain old jackets and dark trousers, varied body types, realistic non duplicated faces, anxious and angry group mood, live action cinematic realism, vertical crowd look image | cartoon, 3D render, plastic texture, western faces, cloned faces, identical uniforms, brand logos, subtitles, watermark, readable slogans |
| SCENE_ZHAODAQIANG_HOME_BASE | scene | 赵大强家内 | 破旧乡镇民房室内，墙角堆杂物，旧窗透入阴天日光，墙面斑驳，水泥地灰暗，必须为空镜 | one_episode | ep13 | candidate | 破旧中国乡镇民房室内空镜，墙角堆着杂物，斑驳墙面和水泥地，破旧窗户透入阴天冷日光，室内灰暗但结构清楚，无人无人脸，真人实拍电影质感，竖屏构图 | 人物，人脸，人群，背影，卡通，3D渲染，塑料感，西方建筑风格，品牌标志，可读文字，字幕，水印 | Empty interior of a shabby Chinese township house, clutter piled in the corner, mottled walls and cement floor, old window bringing in cool overcast daylight, dim but readable space, no people and no faces, live action cinematic realism, vertical composition | people, faces, crowd, back view figures, cartoon, 3D render, plastic texture, western architecture, brand logo, readable text, subtitles, watermark |
| SCENE_EXECUTIVE_OFFICE_BASE | scene | 总裁办公室内 | 现代物流老板办公室，落地窗、真皮沙发、茶几、书柜和晴天自然光，必须为空镜 | episode_range | ep13 | candidate | 中国物流老板总裁办公室空镜，落地窗引入晴天自然光，真皮沙发和茶几位于中央，背景书柜略暗，商务质感克制，无人无人脸，真人实拍电影质感，竖屏构图 | 人物，人脸，人群，卡通，3D渲染，塑料感，豪华酒店化，品牌标志，可读文字，字幕，水印 | Empty executive office for a Chinese logistics boss, sunny daylight through floor to ceiling windows, leather sofa and tea table in the center, darker bookcase in the background, restrained business atmosphere, no people and no faces, live action cinematic realism, vertical composition | people, faces, crowd, cartoon, 3D render, plastic texture, hotel luxury look, brand logo, readable text, subtitles, watermark |
| COSTUME_LINGANG_BUSINESS_SUIT_V1 | costume | 林刚深色商务装 | 深色西装或商务夹克，浅色衬衫，黑色皮鞋，整洁但不过分奢华，用于正式谈判和资金场景 | episode_range | ep13 | candidate | 当代中国男性深色商务装，深色西装或商务夹克，浅色衬衫，黑色皮鞋，剪裁利落但现实克制，布料有自然褶皱，产品式服装参考图，真人实拍质感 | 人脸，人体，卡通，3D渲染，塑料感，潮牌logo，夸张奢华，字幕，水印，可读文字 | Contemporary Chinese male dark business outfit, dark suit or business jacket, light shirt, black leather shoes, neat but realistic restrained tailoring, natural fabric creases, product style costume reference, live action texture | face, body, cartoon, 3D render, plastic texture, fashion brand logo, exaggerated luxury, subtitles, watermark, readable text |
| PROP_BROKEN_KITCHEN_KNIFE_BASE | prop | 破菜刀 | 旧菜刀，金属刀身磨损有缺口，木柄或旧塑料柄，用作赵大强挥舞威胁道具，不带文字和品牌 | one_episode | ep13 | candidate | 破旧菜刀道具，磨损金属刀身，刀刃边缘有小缺口，旧木柄或深色旧塑料柄，掌握比例真实，冷光边缘反光，无品牌无文字，真人实拍电影质感 | 血腥，断肢，品牌logo，可读文字，卡通，3D渲染，塑料感，过度夸张武器，字幕，水印 | Worn kitchen cleaver prop, scuffed metal blade with small nicks on the edge, old wooden handle or dark aged plastic handle, realistic hand scale, cool edge highlight, no brand and no text, live action cinematic realism | gore, dismemberment, brand logo, readable text, cartoon, 3D render, plastic texture, exaggerated fantasy weapon, subtitles, watermark |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| BASE | SCENE_ZHAODAQIANG_HOME_BASE | scene | 阴天日光下的破旧室内墙角，是逼债和挥刀动作的主场景 | ep13 第1组0-10秒，第2组0-10秒，第3组0-11秒 | yes | new empty scene base for episode 13 | 建议同步到asset_bible候选 |
| BASE | SCENE_EXECUTIVE_OFFICE_BASE | scene | 晴天落地窗总裁办公室，承载合同与购车资金谈判 | ep13 第4组0-13秒 | yes | new empty office scene base | 建议同步到asset_bible候选 |
| STATE_LINGANG_BUSINESS_SUIT_EP13 | CHAR_LINGANG_BASE | character | 林刚正式商务装状态，用于总裁办公室谈判 | ep13 第4组0-13秒 | yes | if business state has not been generated | 建议同步到asset_bible候选 |
| BASE | PROP_BROKEN_KITCHEN_KNIFE_BASE | prop | 赵大强抓起并乱挥的破菜刀，推动村民后退 | ep13 第3组6-11秒 | yes | new knife prop for threat scene | 仅本集使用，主线程可视后续复用决定 |
| STATE_PROP_CONTRACT_SIGNED_V1 | PROP_CONTRACT_BASE | prop | 签好字的物流合同，已在全局资产库存在 | ep13 第4组0-6秒，第4组8-13秒 | no | reuse existing signed contract state | 复用已有状态 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 扫帚 | ep13 第1组0-8秒，第2组0-3秒，第3组4-6秒 | 普通临时殴打道具，不承担跨集稳定剧情线索 |
| 茶杯 | ep13 第4组0-13秒 | 办公室普通陈设和表演道具，可由场景即时生成 |
| 真皮沙发和茶几 | ep13 第4组0-13秒 | 已由总裁办公室场景基础资产承载，不单独入库 |
| 赵大强摸衣兜和手机震动 | ep13 第1组8-10秒，第2组0-3秒 | 属于短暂表演动作和普通通信道具状态，不需要跨集资产 |
| 村民的踹腿、抱怨和后退半步 | ep13 第1组0-10秒，第3组9-11秒 | 临时动作和情绪反应，不是资产状态 |
