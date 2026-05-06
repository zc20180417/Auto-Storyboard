# 《刚毅物流 ep17》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP17_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | asset_bible | 第1组0-5秒，第2组6-8秒，第3组0-8秒，第4组2-14秒 | 林刚带现金买五台重卡并准备迎战 | no | reuse existing Lingang township state before jacket-off variant |
| EP17_USE_CHAR_002 | CHAR_SUNBIAO_BASE | BASE | character | asset_bible | 第1组8-12秒，第2组3-11秒，第3组2-10秒，第4组8-10秒 | 孙彪抢车压规矩并叫打手围攻 | no | reuse existing Sun Biao base character |
| EP17_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第1组组首，第1组2-5秒 | 玻璃门外五台重卡的车头轮廓 | no | reuse heavy truck base for dealership display trucks |
| EP17_USE_COSTUME_001 | COSTUME_LINGANG_WORK_JACKET_V1 | BASE | costume | asset_bible | 第1组0-5秒，第2组6-8秒，第3组0-8秒，第4组2-8秒 | 林刚穿深色工装外套进入销售大厅 | no | reuse existing costume asset |
| EP17_USE_COSTUME_002 | COSTUME_WORKER_LOGISTICS_V1 | BASE | costume | asset_bible | 第3组10-12秒，第4组0-12秒 | 孙彪和打手的深色工装或粗粝现场服装基调 | no | reuse worker logistics clothing style as visual base |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_TRUCK_DEALER_HALL_DAY_V1 | SCENE_TRUCK_DEALER_HALL_BASE | BASE | scene | lighting_time | 重卡经销店销售大厅晴日光状态，玻璃门外可见重卡车头轮廓，销售台位于中央 | 晴日光，玻璃门透光，销售台，外部重卡轮廓 | episode_range | ep17 | 第1组0-12秒，第2组0-11秒，第3组0-12秒，第4组0-14秒 | yes | generate empty hall state without people | candidate | 当代中国重卡经销店销售大厅空镜，玻璃大门引入晴日光，中央销售台，地面干净反光，门外隐约可见五台大型重卡车头轮廓，墙面有普通销售大厅质感但无可读品牌文字，无人无人脸，竖屏电影质感，真实材质和自然室内反光 | 人物，人脸，人群，清晰品牌logo，可读车牌号，可读广告字，字幕，水印，卡通，3D渲染，塑料感，过曝 | Empty shot of a contemporary Chinese heavy truck dealership sales hall, sunny daylight through glass doors, central sales counter, clean reflective floor, five large heavy truck front silhouettes visible outside, ordinary showroom walls without readable brand text, no people, no faces, vertical cinematic realism with natural indoor bounce light | people, faces, crowd, clear brand logo, readable license plate, readable advertising text, subtitles, watermark, cartoon, 3D render, plastic texture, overexposure |
| STATE_LINGANG_JACKET_OFF_FIGHT_READY_V1 | CHAR_LINGANG_BASE | STATE_LINGANG_TOWNSHIP_V1 | character | costume_change | 林刚脱下工装外套搭在销售台边，肩背放松后迅速绷起，准备迎战 | 外套脱下，内搭露出，战斗前姿态 | one_episode | ep17 | 第4组2-14秒 | yes | if fight-ready Lingang state is needed for the dealership confrontation | candidate | 基于林刚基础人物和深色工装资产的迎战状态，深色工装外套已脱下并搭在旁边，露出朴素内搭，肩背结实，站姿放松后带压迫感，销售大厅晴日光和室内反光照亮轮廓，真人实拍电影质感 | 西方人脸，改变发型脸型，新增纹身，夸张肌肉，品牌logo，可读文字，卡通，3D渲染，塑料皮肤，字幕 | Fight-ready state based on Lingang base character and dark workwear asset, dark work jacket removed and placed aside, plain inner shirt visible, solid shoulders, relaxed but tense stance, lit by sunny dealership hall daylight and indoor bounce light, live-action cinematic realism | Western face, changed hairstyle or facial structure, new tattoo, exaggerated muscles, brand logo, readable text, cartoon, 3D render, plastic skin, subtitles |
| STATE_PROP_BLACK_CASE_CASH_OPEN_V1 | PROP_BLACK_CASE_CASH_BASE | BASE | prop | prop_condition | 两个黑皮箱砸在销售台上后弹开，成沓现金外露并震动 | 箱口打开，现金外露，销售台反光 | one_episode | ep17 | 第1组0-8秒，第2组组首，第3组组首，第4组组首 | yes | key cash purchase prop for this episode | candidate | 两个黑色皮箱道具打开在销售台上，箱扣弹开，内部成沓现金整齐外露，纸币只呈现模糊钞票质感不显示具体可读编号，皮箱边缘有真实磨损，晴日光和室内柔光照出现金纸张纹理，无品牌logo | 可读钞票编号，真实银行标识特写，品牌logo，字幕，水印，过曝，卡通，3D渲染，假币文字，畸形手指 | Two black leather suitcases opened on a sales counter, latches popped open, stacks of cash visible inside, bills shown as blurred currency texture without readable serial numbers, worn suitcase edges, sunny daylight and soft indoor light revealing paper texture, no brand logo | readable bill serial numbers, real bank logo close-up, brand logo, subtitles, watermark, overexposure, cartoon, 3D render, fake-money text, malformed fingers |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| SCENE_TRUCK_DEALER_HALL_BASE | scene | 重卡经销店销售大厅 | 重卡销售大厅，玻璃大门，销售台，外部可见重卡停车区；基础资产为空镜，不含人物 | episode_range | ep17 | candidate | 当代中国重卡经销店销售大厅空镜，宽玻璃门，中央销售台，普通商务瓷砖地面，门外连接重卡展示停车区，室内简洁但有物流车辆销售场所质感，无人无人脸，无可读品牌标识，竖屏电影质感 | 人物，人脸，人群，清晰品牌logo，可读标语，可读车牌号，字幕，水印，豪华展厅过度包装，卡通，3D渲染 | Empty shot of a contemporary Chinese heavy truck dealership sales hall, wide glass doors, central sales counter, plain business tile floor, exterior connected to a heavy truck display parking area, simple vehicle-sales atmosphere, no people, no faces, no readable brand signage, vertical cinematic realism | people, faces, crowd, clear brand logo, readable slogan, readable license plate, subtitles, watermark, overly luxurious showroom design, cartoon, 3D render |
| CHAR_TRUCK_DEALER_MANAGER_BASE | character | 重卡经销店经理 | 销售大厅经理，成年男性，职业销售人员，面对现金和孙彪威胁时紧张；不写短暂表情入基础设定 | one_episode | ep17 | candidate | 中国重卡经销店经理，30到40多岁男性，中等身材，短发，穿普通商务衬衫或销售夹克，五官端正，职业销售气质，站在销售大厅环境中，真人实拍电影质感，竖屏角色定妆照 | 西方人脸，夸张表情，奢侈品牌logo，可读胸牌文字，卡通，3D渲染，塑料皮肤，水印 | Chinese heavy truck dealership manager, male in his 30s to 40s, average build, short hair, ordinary business shirt or sales jacket, neat facial features, professional salesperson temperament, standing in a sales hall environment, live-action cinematic character reference, vertical framing | Western face, exaggerated expression, luxury brand logo, readable name badge text, cartoon, 3D render, plastic skin, watermark |
| CHAR_SUNBIAO_THUGS_BASE | character | 孙彪打手群像 | 十几个跟随孙彪的打手群像，手持棒球棍堵门，不固定具体脸，用于群体压迫关系 | one_episode | ep17 | candidate | 中国县城物流打手群像，成年男性为主，深色工装或粗糙休闲外套，体态壮实或结实，手持棒球棍形成堵门队形，面部不固定，真实短剧打斗现场质感，竖屏群像构图 | 西方人脸，统一复制脸，黑帮夸张纹身，枪械，品牌logo，可读文字，卡通，3D渲染，水印 | Chinese county-level logistics thug crowd, mostly adult men, dark workwear or rough casual jackets, sturdy builds, holding baseball bats and blocking an entrance, faces not fixed individually, realistic short-drama fight scene texture, vertical group composition | Western faces, identical cloned faces, exaggerated gang tattoos, firearms, brand logo, readable text, cartoon, 3D render, watermark |
| PROP_BLACK_CASE_CASH_BASE | prop | 黑皮箱现金 | 两个黑色皮箱和成沓现金，林刚买车付款核心道具；现金不可出现可读编号或真实金融标识 | one_episode | ep17 | candidate | 黑色皮箱和现金道具，两个硬质黑皮箱，金属箱扣，箱内装成沓纸币，纸币边缘真实但无可读编号和真实银行标识，适合销售台近景，真实比例，无品牌logo | 可读钞票编号，真实银行标识，品牌logo，字幕，水印，卡通，3D渲染，过曝，虚假夸张金光 | Black suitcases and cash prop, two hard black leather cases with metal latches, stacks of bills inside, realistic bill edges without readable serial numbers or real bank marks, suitable for sales counter close-ups, real scale, no brand logo | readable bill serial numbers, real bank marks, brand logo, subtitles, watermark, cartoon, 3D render, overexposure, exaggerated golden glow |
| PROP_CIGAR_BASE | prop | 雪茄 | 孙彪夹在手里或咬在嘴角的雪茄，烟灰落在箱沿或地面，不出现品牌 | one_episode | ep17 | candidate | 普通雪茄道具，深棕色烟草卷，前端有少量烟灰和微弱烟雾，成年人手指夹持比例，表面纹理真实，无品牌环标和可读文字 | 品牌环标，可读文字，夸张火焰，毒品暗示，卡通，3D渲染，水印，比例失真 | Ordinary cigar prop, dark brown tobacco roll, small ash at the tip and faint smoke, adult finger-holding scale, realistic surface texture, no brand band or readable text | brand band, readable text, exaggerated flames, drug implication, cartoon, 3D render, watermark, distorted scale |
| PROP_BASEBALL_BAT_BASE | prop | 棒球棍 | 打手手持的棒球棍，木质或深色金属质感，用于堵门和冲向林刚 | one_episode | ep17 | candidate | 棒球棍道具，木质或深色金属表面，长度适合成年人双手或单手握持，边缘有轻微磨损，适合销售大厅打斗前压迫场面，无品牌logo，无文字 | 血迹，枪械化改造，品牌logo，可读文字，卡通，3D渲染，水印，比例失真 | Baseball bat prop, wooden or dark metal surface, adult scale for one-hand or two-hand grip, lightly worn edges, suitable for pre-fight intimidation inside a sales hall, no brand logo, no text | blood stains, firearm-like modification, brand logo, readable text, cartoon, 3D render, watermark, distorted scale |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_TRUCK_DEALER_HALL_DAY_V1 | SCENE_TRUCK_DEALER_HALL_BASE | scene | 晴日光重卡经销店销售大厅，销售台中央，门外五台重卡轮廓 | 第1组0-12秒，第2组0-11秒，第3组0-12秒，第4组0-14秒 | yes | recurring setting for the whole episode | 建议同步到asset_bible |
| STATE_PROP_BLACK_CASE_CASH_OPEN_V1 | PROP_BLACK_CASE_CASH_BASE | prop | 两个黑皮箱打开露出成沓现金 | 第1组0-8秒，第2组组首，第3组组首，第4组组首 | yes | key payment evidence prop | 可候选同步到asset_bible |
| BASE | PROP_CIGAR_BASE | prop | 孙彪夹雪茄、吐烟、烟灰落在箱沿或地面 | 第1组8-12秒，第2组3-11秒，第3组8-10秒，第4组8-10秒 | yes | repeated character prop for Sun Biao | 仅本集使用 |
| BASE | PROP_BASEBALL_BAT_BASE | prop | 打手持棒球棍堵住玻璃门并冲向林刚 | 第3组10-12秒，第4组0-12秒 | yes | repeated group threat prop | 仅本集使用 |
| STATE_LINGANG_JACKET_OFF_FIGHT_READY_V1 | CHAR_LINGANG_BASE | character | 林刚脱下外套搭在销售台边，准备迎战 | 第4组2-14秒 | yes | visual continuity for the fight posture | 可候选同步到asset_bible |
| BASE | VEHICLE_HEAVY_TRUCK_BASE | prop | 玻璃门外五台重卡车头轮廓 | 第1组组首，第1组2-5秒 | no | existing heavy truck asset can be reused in group formation | 复用已有资产 |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 销售台、箱扣弹开、经理手僵住 | 第1组0-8秒 | 销售台属于场景陈设，箱扣和手部反应属于道具局部或表演动作 |
| 经理额头冒汗、肩膀缩紧 | 第2组0-3秒，第4组2-8秒 | 短暂情绪和表演，不作为人物状态入库 |
| 孙彪瞪眼、冷笑、挥手 | 第2组3-11秒，第4组8-10秒 | 属于角色表演，不是稳定资产变化 |
| 打手甲单独脸和喊话姿势 | 第4组0-2秒 | 群像资产已覆盖，不为临时打手创建单独角色 |
| 门口逆光、棍影压近 | 第3组10-12秒，第4组10-12秒 | 属于镜头光影和调度效果，由场景状态和棒球棍道具承载 |
