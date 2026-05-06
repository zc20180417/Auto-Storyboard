# 《刚毅物流 ep30》资产增量与使用索引

## 一、本集复用资产索引

| 使用ID | asset_id | state_id | asset_type | source | episode_usage | 本集用途 | needs_generation | generation_note |
|---|---|---|---|---|---|---|---|---|
| EP30_USE_CHAR_001 | CHAR_LINGANG_BASE | STATE_LINGANG_CONVOY_V1 | character | asset_bible | ep30 第1组-第14组 | 林刚制服赵大强、见证装船、拒绝省城股份、接跨国合同并宣布基金和跨国干线 | no | reuse existing convoy leader state |
| EP30_USE_CHAR_002 | CHAR_ZHAODAQIANG_BASE | STATE_ZHAODAQIANG_VILLAIN_V1 | character | asset_bible | ep30 第1组-第3组 | 赵大强持打火机威胁点油箱后被制服和铐住 | no | reuse existing villain state |
| EP30_USE_CHAR_003 | CHAR_WANGQIANG_BASE | BASE | character | asset_bible | ep30 第2组-第3组 | 王强被特警控制，被王百川拒绝求救 | no | reuse existing character base |
| EP30_USE_CHAR_004 | CHAR_WANGBAICHUAN_BASE | STATE_WANGBAICHUAN_BOSS_V1 | character | asset_bible | ep30 第3组-第14组 | 王百川拒绝王强、感谢林刚、递股份文件并见证跨国干线 | no | reuse existing boss state |
| EP30_USE_CHAR_005 | CHAR_POLICE_BASE | BASE | character | asset_bible | ep30 第2组-第3组 | 警察和特警进入码头、控制混混和反派 | no | reuse existing police crowd base |
| EP30_USE_CHAR_006 | CHAR_POLICE_BASE | STATE_GANGYI_DRIVERS_V1 | character | asset_bible | ep30 第7组-第14组 | 刚毅车队司机群像聚集、听林刚宣布基金和跨国干线、跑向重卡 | no | reuse existing driver crowd proxy |
| EP30_USE_CHAR_007 | CHAR_LAOCUNZHANG_BASE | BASE | character | asset_bible | ep30 第11组-第12组 | 老村长通过林刚手机视频画面激动来电 | no | reuse existing village elder character |
| EP30_USE_SCENE_001 | SCENE_PORT_BASE | STATE_SCENE_PORT_CONFLICT_DAY_V1 | scene | asset_bible | ep30 第1组-第9组、第13组-第14组 | 国际码头重卡旁、装船区、空地和集装箱旁的晴天终段主空间 | no | reuse existing port conflict day state |
| EP30_USE_SCENE_002 | SCENE_VILLAGE_ROAD_BASE | BASE | scene | asset_bible | ep30 第10组-第12组 | 手机照片和视频背景中的村路空间基础设定 | no | reuse existing village road base |
| EP30_USE_PROP_001 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | asset_bible | ep30 第1组-第2组、第7组-第14组 | 重卡副油箱、车队、司机上车和片尾车门车标承载 | no | reuse existing heavy truck asset |
| EP30_USE_PROP_002 | VEHICLE_POLICE_CAR_BASE | BASE | prop | asset_bible | ep30 第2组-第3组 | 海警车、警车和特警防暴车进入码头控制现场 | no | reuse existing police vehicle asset |
| EP30_USE_PROP_003 | PROP_LIGHTER_BASE | BASE | prop | asset_bible | ep30 第1组-第2组 | 赵大强威胁点燃副油箱的打火机，被林刚夺下 | no | reuse existing lighter prop |
| EP30_USE_PROP_004 | PROP_HANDCUFFS_BASE | BASE | prop | asset_bible | ep30 第2组-第3组 | 特警给赵大强、王强和混混上铐 | no | reuse existing handcuffs prop |
| EP30_USE_PROP_005 | PROP_CONTRACT_BASE | BASE | prop | asset_bible | ep30 第5组-第7组 | 王百川递股份文件，神秘外宾引出跨国联运合同 | no | reuse existing contract and share file base |
| EP30_USE_PROP_006 | PROP_CRACKED_PHONE_BASE | BASE | prop | asset_bible | ep30 第10组-第14组 | 林刚展示村路照片、接老村长视频来电、收起手机上车 | no | reuse phone base without cracked state requirement |
| EP30_USE_COMP_001 | COMPOSITION_POLICE_CONTROL_V1 | BASE | composition | asset_bible | ep30 第2组-第3组 | 警车压进、特警控制反派和混混的执法现场构图 | no | reuse existing police control composition |

## 二、本集新增资产状态

| state_id | asset_id | parent_state_id | asset_type | status_type | state_summary | changed_fields | reuse_policy | first_seen_episode | episode_usage | needs_generation | generation_note | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STATE_VEHICLE_TRUCK_FUEL_TANK_THREAT_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 重卡副油箱裸露，赵大强持打火机靠近但未点燃 | 副油箱特写、打火机接近、无火焰、无爆炸 | one_episode | ep30 | ep30 第1组 | yes | generate if fuel tank threat close-up is needed | no | 大型物流重卡侧面副油箱区域特写，油箱盖和金属车身清晰，旁边可见普通打火机的手持比例但没有火焰，日间码头硬光，车身无品牌无车牌，真实紧张道具状态 | 明火、爆炸、烟雾、血腥、品牌logo、可读车牌、字幕、水印、卡通、3D渲染 | Close-up of a large logistics truck side auxiliary fuel tank, clear fuel cap and metal body, a plain lighter visible at handheld scale nearby but no flame, hard daylight at the port, no brand and no license plate, realistic tense prop state | open flame, explosion, smoke, gore, brand logo, readable license plate, subtitles, watermark, cartoon, 3D render |
| STATE_SCENE_PORT_OPERATION_RESTORED_V1 | SCENE_PORT_BASE | STATE_SCENE_PORT_CONFLICT_DAY_V1 | scene | scene_condition | 配电恢复后码头装船区运转，龙门吊移动集装箱，货轮泊位清晰 | 设备指示灯、龙门吊运转、集装箱吊起、货轮泊位 | episode_range | ep30 | ep30 第4组 | yes | generate restored loading operation state | candidate | 国际码头装船区空镜，晴天日光，配电室外墙和设备指示灯亮起，巨型龙门吊正在吊起集装箱并朝远处货轮甲板方向移动，集装箱堆场和海面反光清晰，无人无人脸，竖屏电影构图 | 人物、人脸、人群、可读船名、真实品牌logo、字幕、水印、卡通、3D渲染、过曝 | Empty international port loading area in daylight, power room exterior and equipment indicator lights on, giant gantry crane lifting a container toward a distant cargo ship deck, clear container yard and sea reflections, no people, no faces, vertical cinematic framing | people, faces, crowds, readable ship name, real brand logo, subtitles, watermark, cartoon, 3D render, overexposure |
| STATE_PROP_SHARE_FILE_OFFERED_V1 | PROP_CONTRACT_BASE | BASE | prop | prop_condition | 王百川递出的股份文件，纸面正式但正文不可读 | 股份文件、递交、纸张抖动、正文不可读 | one_episode | ep30 | ep30 第5组 0-6秒、第7组 6-8秒 | yes | generate share file offer state | no | 股份文件道具，A4纸和简洁文件夹，纸面排版正式但正文不可读，边缘被海风吹动轻微抖起，商务质感真实，无真实公司名称，无清晰印章文字，日间港口环境光 | 可读合同全文、真实公司名称、真实公章、品牌logo、二维码、字幕、水印、卡通、3D渲染 | Share document prop, A4 paper and simple folder, formal page layout but unreadable body text, edges slightly fluttering in sea wind, realistic business texture, no real company name, no clear seal text, daylight port ambient light | readable full contract, real company name, real official seal, brand logo, QR code, subtitles, watermark, cartoon, 3D render |
| STATE_SCENE_VILLAGE_ROAD_PAVED_STELE_V1 | SCENE_VILLAGE_ROAD_BASE | BASE | scene | scene_condition | 崭新村路和路边石碑状态，手机照片里可见“过客留”路碑线索 | 新铺道路、路边石碑、村口背景、碑文线索 | episode_range | ep30 | ep30 第10组 6-9秒、第11组-第12组 | yes | generate paved village road and road stele state | candidate | 中国乡村新铺水泥路空镜，路面干净平整，路边有朴素石碑，石碑刻有过客留三个字作为剧情线索，远处低矮民房和田地虚化，白天自然光，无人无人脸，真实乡村振兴物流道路质感 | 人物、人脸、错误额外文字、真实政府标识、二维码、品牌logo、字幕、水印、卡通、3D渲染 | Empty newly paved Chinese village concrete road, clean flat surface, a plain roadside stone stele engraved with the three Chinese characters Guo Ke Liu as a story clue, distant low houses and fields softly blurred, natural daylight, no people, no faces, realistic rural logistics revitalization texture | people, faces, incorrect extra text, real government emblem, QR code, brand logo, subtitles, watermark, cartoon, 3D render |
| STATE_PROP_PHONE_VILLAGE_ROAD_CALL_V1 | PROP_CRACKED_PHONE_BASE | BASE | prop | prop_condition | 林刚手机显示村路照片和老村长视频来电，屏幕内容用于剧情展示 | 村路照片、视频来电、屏幕亮起、可控文字 | one_episode | ep30 | ep30 第10组-第12组、第14组 0-3秒 | yes | generate phone screen state if screen close-up needed | no | 黑色智能手机道具，屏幕亮起显示一张新铺村路照片或老村长视频来电画面，画面内容清晰但界面文字尽量模糊不可读，手机边缘有日光反光，真实手持比例，港口白天环境 | 品牌logo、可读个人信息、真实电话界面、错误字幕、二维码、水印、卡通、3D渲染、手指畸形 | Black smartphone prop with screen lit, showing either a newly paved village road photo or a video call image of the old village head, visual content clear but interface text mostly blurred and unreadable, daylight reflections on phone edges, realistic handheld scale, daytime port setting | brand logo, readable personal information, real phone UI, wrong subtitles, QR code, watermark, cartoon, 3D render, deformed fingers |
| STATE_VEHICLE_GANGYI_LOGO_V1 | VEHICLE_HEAVY_TRUCK_BASE | BASE | prop | prop_condition | 刚毅物流重卡车门上的虚构车标在阳光下发亮，用于片尾意象 | 虚构车标、车门特写、阳光高光、发动震动 | episode_range | ep30 | ep30 第14组 3-14秒 | yes | generate fictional Gangyi truck mark close-up | candidate | 刚毅物流重卡车门特写，车门上贴着虚构的刚毅物流车标，金属或贴膜边缘在阳光下发亮，车身有真实路尘和轻微震动感，不出现真实品牌logo和可读车牌，竖屏片尾意象构图 | 真实品牌logo、可读车牌、额外字幕、片名、演职员表、水印、卡通、3D渲染、塑料感 | Close-up of a Gangyi Logistics heavy truck door, a fictional Gangyi Logistics mark on the door, metallic or decal edges shining in sunlight, realistic road dust and slight engine vibration on the body, no real brand logo and no readable license plate, vertical ending-image composition | real brand logo, readable license plate, extra subtitles, title text, credits, watermark, cartoon, 3D render, plastic texture |

## 三、本集新增基础资产

| asset_id | asset_type | asset_name | description | reuse_policy | first_seen_episode | sync_to_bible | 静态生图提示词(中文) | 负面提示词(中文) | 静态生图提示词(英文) | 负面提示词(英文) |
|---|---|---|---|---|---|---|---|---|---|---|
| CHAR_GLOBAL_SHIPPING_EXEC_BASE | character | 神秘外宾 | 国际航运商务高管，穿整齐西装，从黑色商务直升机下来向林刚递名片，不固定真实国籍 | episode_range | ep30 | candidate | 国际航运商务高管定妆照，成年男性，整齐西装，身形挺拔，手持名片，气质礼貌克制，面孔不绑定真实国籍并符合中国短剧写实审美，港口商务直升机背景虚化，真人实拍电影质感，竖屏人物参考 | 西方刻板脸、夸张富豪造型、真实公司logo、可读名片文字、字幕、水印、卡通、3D渲染 | International shipping business executive character reference, adult man in a neat suit, upright posture, holding a business card, polite and restrained manner, not tied to a real nationality and matching Chinese short-drama live-action aesthetics, blurred port business helicopter background, vertical character reference | stereotypical Western face, exaggerated tycoon styling, real company logo, readable business card text, subtitles, watermark, cartoon, 3D render |
| VEHICLE_BLACK_BUSINESS_HELICOPTER_BASE | prop | 黑色商务直升机 | 港口空地降落的黑色商务直升机，承载神秘外宾登场和跨国合同线索 | episode_range | ep30 | candidate | 黑色商务直升机道具，机身深色哑光与局部高光，螺旋桨低速旋转，停在国际码头空地，周围有轻微尘土和海风感，无真实品牌logo，无清晰编号，真实比例，竖屏电影构图 | 真实品牌logo、清晰编号、军用武装、爆炸、字幕、水印、卡通、3D渲染、玩具感 | Black business helicopter prop, dark matte body with controlled highlights, rotor turning slowly, parked on an international port open ground, slight dust and sea-wind feel, no real brand logo, no clear registration number, realistic scale, vertical cinematic framing | real brand logo, clear registration number, military weapons, explosion, subtitles, watermark, cartoon, 3D render, toy-like look |
| PROP_BUSINESS_CARD_BASE | prop | 神秘外宾名片 | 神秘外宾递给林刚的商务名片，道具应保持正式但不生成可读个人信息 | one_episode | ep30 | no | 商务名片道具，白色或浅灰硬卡纸，简洁高端排版，边缘干净，手持比例真实，文字只保留模糊排版感不可读，无真实公司logo，无二维码，日间港口环境光 | 可读姓名电话、真实公司logo、二维码、品牌商标、字幕、水印、卡通、3D渲染、手指畸形 | Business card prop, white or light-gray thick card paper, clean premium layout, neat edges, realistic handheld scale, text only as blurred unreadable layout, no real company logo, no QR code, daylight port ambient light | readable name or phone number, real company logo, QR code, brand trademark, subtitles, watermark, cartoon, 3D render, deformed fingers |

## 四、本集关键道具与场景状态

| state_id | asset_id | asset_type | state_summary | episode_usage | needs_generation | generation_note | 入库建议 |
|---|---|---|---|---|---|---|---|
| STATE_VEHICLE_TRUCK_FUEL_TANK_THREAT_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 重卡副油箱被打火机威胁但未点燃 | ep30 第1组 | yes | generate only if fuel tank close-up is needed | 仅本集使用 |
| BASE | VEHICLE_POLICE_CAR_BASE | prop | 海警车、警车和特警防暴车压进码头 | ep30 第2组-第3组 | no | reuse police vehicle base | 复用已有基础资产 |
| BASE | PROP_HANDCUFFS_BASE | prop | 特警给赵大强、王强和混混上铐 | ep30 第2组-第3组 | no | reuse handcuffs base | 复用已有基础资产 |
| STATE_SCENE_PORT_OPERATION_RESTORED_V1 | SCENE_PORT_BASE | scene | 配电恢复后龙门吊运转并完成装船 | ep30 第4组 | yes | generate restored port loading state | 建议同步到asset_bible |
| STATE_PROP_SHARE_FILE_OFFERED_V1 | PROP_CONTRACT_BASE | prop | 王百川递出百分之五十股份文件 | ep30 第5组 | yes | generate if share file close-up is needed | 仅本集使用 |
| BASE | VEHICLE_BLACK_BUSINESS_HELICOPTER_BASE | prop | 黑色商务直升机降落和飞离码头 | ep30 第5组-第7组 | yes | generate black business helicopter | 建议同步到asset_bible |
| BASE | PROP_BUSINESS_CARD_BASE | prop | 神秘外宾递给林刚的名片 | ep30 第6组-第7组 | yes | generate business card prop without readable data | 仅本集使用 |
| STATE_SCENE_VILLAGE_ROAD_PAVED_STELE_V1 | SCENE_VILLAGE_ROAD_BASE | scene | 新铺村路和写有过客留的路碑 | ep30 第10组-第12组 | yes | generate paved road scene state | 建议同步到asset_bible |
| STATE_PROP_PHONE_VILLAGE_ROAD_CALL_V1 | PROP_CRACKED_PHONE_BASE | prop | 手机显示村路照片和老村长视频来电 | ep30 第10组-第12组、第14组 | yes | generate phone screen state if needed | 仅本集使用 |
| STATE_VEHICLE_GANGYI_LOGO_V1 | VEHICLE_HEAVY_TRUCK_BASE | prop | 刚毅物流虚构车标在重卡车门上发亮 | ep30 第14组 | yes | generate fictional truck mark ending close-up | 建议同步到asset_bible |

## 五、本集不建议入库元素

| 元素 | 出现位置 | 不入库原因 |
|---|---|---|
| 赵大强挣扎、王强哀嚎、王百川眼眶微红 | ep30 第2组-第5组 | 短暂表演和情绪变化，不是稳定资产状态 |
| 普通码头工人、司机甲、临时司机单人脸 | ep30 第4组、第8组-第13组 | 群像和功能性台词角色，不固定成跨集人物资产 |
| 直升机螺旋桨风、尘土、衣角和文件抖动 | ep30 第5组-第7组 | 动态镜头效果，由分镜即时生成，不单独入库 |
| 归途基金、通村基金、百分之五等概念 | ep30 第8组-第10组 | 属于台词和制度设定，不是可生图资产 |
| 视频来电界面具体按钮和个人信息 | ep30 第11组-第12组 | 屏幕 UI 不应生成真实可读个人信息，保留模糊视觉即可 |
| 片尾字幕和全剧终文字 | ep30 第14组 | 后期字幕元素，不作为资产表入库，也不应提前由生图模型生成 |
