# 《刚毅物流 ep27》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP27_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | 第1组0-10秒，第2组0-15秒，第3组0-13秒，第4组0-10秒，第5组0-15秒，第6组0-13秒，第7组0-10秒 | 林刚在收费站亮证突围并在办公室决定算旧账 | no | reuse existing convoy stage |
| EP27_USE_CHAR_002 | CHAR_QINYE_BASE | BASE | character | asset_bible | 第1组0-10秒，第2组0-15秒，第3组组首空间锁定，第4组组首空间锁定，第5组0-15秒 | 秦爷坐在豪华轿车内拖延扣车后被路政人员按住 | no | reuse existing base character |
| EP27_USE_CHAR_003 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | 第6组0-13秒，第7组0-10秒 | 王百川办公室里告知王强和赵大强新麻烦 | no | reuse existing boss stage |
| EP27_USE_SCENE_001 | SCENE_HIGHWAY_TOLL_BASE | STATE_SCENE_TOLL_BLOCKADE_DAY_V1 | scene | episode_variant | 第1组0-10秒，第2组0-15秒，第3组0-13秒，第4组0-10秒，第5组0-15秒 | 高速收费站被路政车和栏杆拦停的冲突现场 | conditional | if state not generated |
| EP27_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | 第1组0-10秒，第2组0-15秒，第3组0-13秒，第4组0-10秒，第5组0-15秒 | 林刚物流车队在收费站被拦后通过 | no | reuse heavy truck base |
| EP27_USE_PROP_002 | VEHICLE_POLICE_CAR_BASE | BASE | prop | asset_bible | 第1组0-10秒，第2组0-15秒，第5组0-15秒 | 可作为闪警灯执法车辆的既有车辆参考 | no | reuse existing enforcement vehicle base |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_SCENE_TOLL_BLOCKADE_DAY_V1 | SCENE_HIGHWAY_TOLL_BASE | BASE | scene | scene_condition | 日间高速收费站前，物流车队被栏杆、路政车和豪华轿车堵住 | 晴天硬光，栏杆落下，路政车横停，物流车队排队，豪华轿车在后侧 | episode_range | ep27 | 第1组0-10秒，第2组0-15秒，第3组0-13秒，第4组0-10秒，第5组0-15秒 | yes | generate toll blockade state | candidate | 高速收费站检查区日间空镜，收费顶棚和车道白线清楚，栏杆落下挡住物流车道，三辆闪警灯的路政车横停在前方，后侧一辆黑色豪华轿车，物流重卡队列停在车道内，无清晰人物无人脸，真实交通执法现场，竖屏电影质感 | 清晰人脸，品牌logo，可读车牌，可读标语，字幕，水印，卡通，3D渲染，过曝，低清 | Empty daytime shot of a highway toll checkpoint, toll canopy and lane markings visible, barrier lowered across the logistics lane, three road administration cars with warning lights blocking ahead, a black luxury sedan behind them, heavy logistics trucks waiting in lane, no clear people, no faces, realistic traffic enforcement scene, vertical cinematic realism | clear faces, brand logos, readable plates, readable signage, subtitles, watermark, cartoon, 3D render, overexposure, low resolution |
| STATE_PROP_SPECIAL_PASS_DISPLAYED_V1 | PROP_SPECIAL_PASS_BASE | BASE | prop | prop_condition | 红色特别通行证被林刚甩出并压在路政队长面前 | 红色封皮，国徽标识，免检车队关键信息，手持展示 | episode_range | ep27 | 第3组4-13秒，第4组0-5秒 | yes | generate displayed pass state | candidate | 红色特别通行证道具被手指压在画面前景，红色封皮和国徽标识清楚，证件上仅保留“省重点扶持出口免检车队”“卫生局和海关双重特批”等剧情关键信息，其余文字模糊不可读，晴天硬光，真实证件纸张质感 | 多余文字，错字，真实证件编号，品牌logo，人脸，字幕，水印，卡通，3D渲染，低清 | Red special transport pass prop pressed in the foreground by fingers, clear red cover and national emblem mark, only the story relevant wording about provincial key export exempt convoy and health bureau plus customs approval is suggested while other text is blurred, hard daylight, realistic paper document texture | extra text, wrong characters, real document number, brand logo, faces, subtitles, watermark, cartoon, 3D render, low resolution |
| STATE_SCENE_WANG_OFFICE_NIGHT_V1 | SCENE_WANG_OFFICE_BASE | BASE | scene | lighting_time | 夜间王百川办公室，暖色室内灯与窗外冷夜色对比 | 夜间，办公桌电话，沙发茶杯，暖灯，窗外冷色 | episode_range | ep27 | 第6组0-13秒，第7组0-10秒 | yes | generate night office state | candidate | 王百川办公室夜间空镜，右侧办公桌上有电话和文件，左侧沙发旁放着茶杯，窗外是冷色夜景，室内暖色主灯和桌灯形成商务办公室氛围，无人无人脸，真实当代中国物流老板办公室，竖屏电影质感 | 人物，人脸，品牌logo，可读文件文字，字幕，水印，卡通，3D渲染，过曝，低清 | Empty night shot of Wang Baichuan office, desk with telephone and documents on the right, sofa and teacup on the left, cool night outside the window, warm main light and desk lamp creating a business office mood, no people, no faces, realistic contemporary Chinese logistics boss office, vertical cinematic realism | people, faces, brand logos, readable document text, subtitles, watermark, cartoon, 3D render, overexposure, low resolution |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_ROAD_ADMIN_CAPTAIN_BASE | character | 路政队长 | 收费站扣车的路政队长，成年男性，穿路政执法制服，手持大喇叭，神情油滑强硬 | episode_range | ep27 | candidate | 中国路政执法队长，成年男性，中等体态，制式路政制服，短发，手持大喇叭，表情油滑强硬，站在高速收费站车道旁，警灯反光掠过制服，真人实拍电影质感 | 西方人脸，警察制服误用，品牌logo，可读胸牌编号，字幕，水印，卡通，3D渲染，低清 | Chinese road administration captain, adult male with average build, official road enforcement uniform, short hair, holding a megaphone, slick and forceful expression, standing by a highway toll lane, warning light reflections on the uniform, live action cinematic realism | western face, incorrect police uniform, brand logo, readable badge number, subtitles, watermark, cartoon, 3D render, low resolution |
| CHAR_ROAD_ADMIN_PERSONNEL_BASE | character | 路政人员群像 | 收费站执行贴封条和抓人的路政人员群像，不固定具体脸，穿统一执法制服 | episode_range | ep27 | candidate | 中国路政人员群像，成年男性为主，统一路政执法制服，动作整齐，手中可拿封条或靠近车辆，不固定具体脸，高速收费站执法现场，真人实拍电影质感 | 清晰固定个人脸，西方人脸，警察特警误用，品牌logo，可读编号，字幕，水印，卡通，3D渲染，低清 | Chinese road administration personnel group, mostly adult men in matching road enforcement uniforms, orderly movement, may hold sealing strips or stand near vehicles, no fixed individual faces, highway toll enforcement scene, live action cinematic realism | clear fixed individual faces, western faces, incorrect SWAT or police gear, brand logo, readable number, subtitles, watermark, cartoon, 3D render, low resolution |
| VEHICLE_ROAD_ADMIN_CAR_BASE | prop | 路政车 | 收费站横停堵车的路政执法车，警灯闪烁，车身不出现可读单位文字和车牌 | episode_range | ep27 | candidate | 中国高速路政执法车道具，白色或深色公务车辆，车顶警示灯闪烁，车身轮廓真实，横停在收费站车道前，无品牌logo，无可读单位文字，无可读车牌，真实交通执法比例 | 品牌logo，可读车牌，可读单位全称，夸张警车涂装，人物正脸，字幕，水印，卡通，3D渲染 | Chinese highway road administration vehicle prop, white or dark official vehicle with flashing warning lights, realistic body shape, parked sideways before a toll lane, no brand logo, no readable agency text, no readable plate, realistic traffic enforcement scale | brand logo, readable plate, readable agency name, exaggerated police livery, front facing people, subtitles, watermark, cartoon, 3D render |
| VEHICLE_LUXURY_SEDAN_BASE | prop | 秦爷黑色豪华轿车 | 秦爷乘坐的黑色豪华轿车，后排车窗可半降，车内偏暗，不显示品牌标志和车牌 | one_episode | ep27 | no | 黑色豪华轿车道具，后排车窗半降，深色车漆有真实反光，车内光线较暗，适合表现反派坐在后排观察现场，无品牌logo，无可读车牌，真实商务豪车比例 | 品牌logo，可读车牌，真实商标，夸张跑车造型，字幕，水印，卡通，3D渲染，低清 | Black luxury sedan prop with half lowered rear window, dark glossy paint with realistic reflections, dim interior, suitable for an antagonist watching from the back seat, no brand logo, no readable plate, realistic executive car scale | brand logo, readable plate, real trademark, exaggerated sports car shape, subtitles, watermark, cartoon, 3D render, low resolution |
| PROP_SPECIAL_PASS_BASE | prop | 红色特别通行证 | 林刚亮出的红色特别通行证，带国徽和出口免检车队关键信息，用于压住路政队长 | episode_range | ep27 | candidate | 红色特别通行证道具，硬质红色封皮或证件页，国徽标识居中，纸张边缘整齐，内容只保留剧情需要的免检车队和双重特批信息，其余正文模糊不可读，正式公文质感 | 多余可读文字，真实编号，错字，品牌logo，二维码，字幕，水印，卡通，3D渲染 | Red special transport pass prop, rigid red cover or document page, national emblem centered, neat paper edges, only story needed exempt convoy and dual approval information suggested, other text blurred and unreadable, formal document texture | extra readable text, real serial number, wrong characters, brand logo, QR code, subtitles, watermark, cartoon, 3D render |
| SCENE_WANG_OFFICE_BASE | scene | 王百川办公室 | 王百川的物流老板办公室，办公桌、电话、文件柜、沙发、茶杯和办公室门构成主要空间 | episode_range | ep27 | candidate | 当代中国物流老板办公室空镜，办公桌、桌面电话、文件柜、沙发、茶杯和办公室门清楚，商务但不奢华，室内材质真实，无人无人脸，无可读文件文字，电影质感 | 人物，人脸，可读文件文字，品牌logo，字幕，水印，卡通，3D渲染，过度豪华 | Empty contemporary Chinese logistics boss office, desk, desk phone, filing cabinet, sofa, teacup and office door visible, businesslike but not overly luxurious, realistic interior materials, no people, no faces, no readable document text, cinematic realism | people, faces, readable document text, brand logo, subtitles, watermark, cartoon, 3D render, overly luxurious look |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_SCENE_TOLL_BLOCKADE_DAY_V1 | SCENE_HIGHWAY_TOLL_BASE | scene | 收费站被栏杆、路政车和豪华轿车拦截状态 | 第1组0-10秒至第5组0-15秒 | yes | toll blockade state first appears in ep27 | 建议同步到asset_bible |
| CHAR_ROAD_ADMIN_CAPTAIN_BASE | CHAR_ROAD_ADMIN_CAPTAIN_BASE | character | 手持大喇叭的路政队长 | 第1组3-10秒，第2组9-15秒，第3组4-13秒，第4组0-10秒，第5组0-6秒 | yes | recurring episode antagonist role | 建议同步到asset_bible |
| CHAR_ROAD_ADMIN_PERSONNEL_BASE | CHAR_ROAD_ADMIN_PERSONNEL_BASE | character | 贴封条和控制秦爷的路政人员群像 | 第2组9-15秒，第3组组首空间锁定，第4组0-10秒，第5组2-9秒 | yes | enforcement group appears repeatedly | 建议同步到asset_bible |
| VEHICLE_ROAD_ADMIN_CAR_BASE | VEHICLE_ROAD_ADMIN_CAR_BASE | prop | 三辆闪警灯横停堵车的路政车 | 第1组0-10秒，第5组0-15秒 | yes | enforcement vehicle first appears in ep27 | 建议同步到asset_bible |
| VEHICLE_LUXURY_SEDAN_BASE | VEHICLE_LUXURY_SEDAN_BASE | prop | 秦爷后排乘坐的黑色豪华轿车 | 第1组0-10秒，第2组0-15秒，第3组组首空间锁定，第4组组首空间锁定，第5组0-15秒 | yes | one episode antagonist vehicle | 仅本集使用 |
| STATE_PROP_SPECIAL_PASS_DISPLAYED_V1 | PROP_SPECIAL_PASS_BASE | prop | 红色特别通行证被展示并压住路政队长 | 第3组4-13秒，第4组0-5秒 | yes | key document state first appears in ep27 | 建议同步到asset_bible |
| STATE_SCENE_WANG_OFFICE_NIGHT_V1 | SCENE_WANG_OFFICE_BASE | scene | 夜间王百川办公室谈新麻烦 | 第6组0-13秒，第7组0-10秒 | yes | office night scene first appears in ep27 | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 收费站栏杆和车道白线 | 第1组至第5组 | 已由SCENE_HIGHWAY_TOLL_BASE和拦截状态承载，不单独作为道具 |
| 大喇叭 | 第1组3-10秒，第2组组首空间锁定 | 路政队长随身执法小物，已并入人物资产提示词 |
| 雪茄和烟雾 | 第1组组首空间锁定，第2组0-9秒，第5组0-9秒 | 秦爷一次性表演小物，不建议跨集入库 |
| 封条 | 第2组9-15秒，第3组0-4秒，第4组0-3秒 | 扣车动作道具，可即时生成，不需要独立稳定资产 |
| 林刚把证件拍到脸上的动作 | 第3组4-7秒 | 动作节拍，不是资产状态 |
| 办公桌、茶杯、沙发、电话、办公室门 | 第6组，第7组 | 已纳入王百川办公室基础场景，不逐项拆道具 |
| 王强和赵大强的口头提及 | 第6组3-13秒，第7组0-4秒 | 本集没有实体出镜，不生成资产 |
