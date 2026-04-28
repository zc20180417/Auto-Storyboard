import fs from "node:fs/promises";
import path from "node:path";

const [inputDirArg, outputDirArg] = process.argv.slice(2);

if (!inputDirArg || !outputDirArg) {
  console.error("Usage: node extract-flat-storyboard-assets.mjs <flat-storyboard-dir> <output-dir>");
  process.exit(2);
}

const inputDir = path.resolve(inputDirArg);
const outputDir = path.resolve(outputDirArg);

const NEG_CN_SCENE = "模糊，低分辨率，扭曲，变形，卡通，3D渲染，塑料感，过曝，色彩失真，伪影，错误的透视，消失点扭曲，倾斜地平线，墙面不垂直，比例失调，物体断层，桶形畸变，枕形畸变，鱼眼效果，景深不合理，漂浮，塑料光泽，平滑无痕，完美无缺，游戏引擎感，无大气透视，阴影缺失，光线扁平，反射假亮，材质模糊，贴图重复，无接触阴影，人物，人，人脸";
const NEG_CN_PERSON = "模糊，低分辨率，扭曲，变形，卡通，3D渲染，塑料感，过曝，色彩失真，伪影，错误的透视，比例失调，身体比例错误，手部畸形，西方人脸，塑料光泽，平滑无痕，完美无缺，游戏引擎感";
const NEG_CN_ASSET = "模糊，低分辨率，扭曲，变形，卡通，3D渲染，塑料感，过曝，色彩失真，伪影，错误的透视，比例失调，物体断层，桶形畸变，枕形畸变，鱼眼效果，漂浮，塑料光泽，平滑无痕，完美无缺，游戏引擎感";
const NEG_EN_SCENE = "blurry, low resolution, distorted, deformed, cartoon, 3D render, plastic, overexposed, color distortion, artifacts, incorrect perspective, skewed vanishing point, tilted horizon, non-vertical walls, disproportionate, broken geometry, barrel distortion, pincushion distortion, fisheye, warped, stretched, unrealistic depth of field, floating objects, mismatched scale, glossy perfection, smooth and spotless, game-like CGI, no ambient occlusion, flat lighting, missing shadows, no aerial perspective, fake reflections, tiled textures, no contact shadows, people, human faces";
const NEG_EN_PERSON = "blurry, low resolution, distorted, deformed, cartoon, 3D render, plastic, overexposed, color distortion, artifacts, incorrect perspective, disproportionate, distorted hands, western faces, glossy perfection, smooth and spotless, game-like CGI, flat lighting, missing shadows";
const NEG_EN_ASSET = "blurry, low resolution, distorted, deformed, cartoon, 3D render, plastic, overexposed, color distortion, artifacts, incorrect perspective, skewed vanishing point, disproportionate, broken geometry, barrel distortion, pincushion distortion, fisheye, floating objects, mismatched scale, glossy perfection, smooth and spotless, game-like CGI, flat lighting, missing shadows";

const ROLE_PROFILES = {
  "林跃": ["二十多岁男性，农村青年转型创业者", "中等偏高，肩背挺直，体态干练", "黑色短发，眉眼冷静，面部线条清晰，眼神沉稳", "朴素深色夹克或旧衬衫，深色长裤，布鞋/旧皮鞋", "冷静、克制、锋利"],
  "林建国": ["五十岁上下男性，林跃父亲，老实农民", "中等身材，肩背略弯，手掌粗糙", "短发夹白，额纹明显，面容疲惫朴实", "旧棉布上衣，深色裤子，解放鞋", "忠厚、焦急、隐忍"],
  "张桂兰": ["五十岁上下女性，林跃母亲，农村妇人", "中等偏瘦，动作拘谨", "头发挽起或短发夹白，眼角细纹明显，脸色朴素", "深色碎花旧上衣，布裤，布鞋", "心疼、慌乱、坚韧"],
  "林小雅": ["十岁左右女性，林跃妹妹，学生", "瘦小，动作轻快", "黑发扎辫，脸庞稚气，眼神明亮", "干净朴素的儿童上衣，新裙子或学生装，布鞋", "天真、依赖、希望"],
  "赵百川": ["五十岁上下男性，村干部，赵大强父亲", "中等偏壮，站姿端着架子", "短发偏灰，浓眉，法令纹重，眼神阴沉", "旧干部夹克，中山装式外套，深色长裤，黑布鞋", "阴鸷、强势、算计"],
  "赵大强": ["二十多岁男性，村霸式青年，赵百川之子", "偏壮，动作虚张声势", "短发，眉眼浮躁，表情嚣张或惊惧", "不合身西装或花衬衫，深色裤子，皮鞋/布鞋", "嚣张、怯懦、贪婪"],
  "李二狗": ["二十多岁男性，村里混混", "偏瘦，肩膀内缩", "短发，脸颊发紧，眼神躲闪", "旧汗衫或灰旧外套，沾泥长裤，泥鞋", "心虚、猥琐、胆怯"],
  "供水员王四": ["三四十岁男性，村里供水员", "中等身材，动作小心", "短发，眼神闪躲，额头易出汗", "蓝灰色旧工装，深色裤子，胶鞋", "怯懦、听命、紧张"],
  "马主任": ["四十多岁男性，县供销社干部", "中等身材，坐姿端正", "短发，面部严肃，眼镜可选", "灰色干部外套，白衬衫，深色长裤", "谨慎、官气、审视"],
  "马秘书": ["三十多岁男性，镇上秘书", "中等身材，动作利落", "短发，表情刻板，眼神审视", "灰色夹克或干部装，深色裤子，皮鞋", "傲慢、谨慎、官僚"],
  "陈干事": ["三十多岁男性，基层干事", "中等身材，手持本子", "短发，戴眼镜，表情认真", "朴素干部夹克，深色裤子，布鞋", "认真、务实、观察"],
  "纪委老李": ["五十岁上下男性，纪委干部", "中等偏瘦，站姿稳", "短发灰白，眼神锐利，面部严肃", "深色干部夹克，白衬衫，深色长裤", "严肃、压迫、克制"],
  "钱厂长": ["五十岁上下男性，县加工厂厂长", "中等偏胖，坐姿沉稳", "短发，脸部圆厚，眼神精明", "深色西装或厂长夹克，皮鞋", "精明、权衡、体面"],
  "钱秘书": ["三十多岁男性，厂长秘书", "中等身材，动作谨慎", "短发，表情紧绷，眼神会察言观色", "浅色衬衫，深色裤子，夹克或西装外套", "谨慎、圆滑、执行"],
  "赵雷": ["三十岁上下男性，退伍兵/司机队负责人", "高大结实，肩背宽，站姿笔直", "寸头，眉骨硬朗，眼神警觉", "军绿色旧外套，深色工装裤，军靴", "可靠、果断、硬朗"],
  "王总": ["五十岁上下男性，市级企业负责人", "中等偏壮，气场稳", "短发，面部沉稳，眼神有压迫感", "深色西装，白衬衫，皮鞋", "权威、审慎、强势"],
  "吴总": ["五十岁上下男性，药业老板/反派商人", "中等偏胖，姿态松弛但压迫", "背头或短发，眼神阴沉，脸部保养较好", "高档深色西装，皮鞋，手表", "傲慢、危险、老辣"],
  "吴总秘书": ["三十岁上下女性或男性秘书，商务随从", "中等身材，姿态职业", "短发或盘发，表情克制，眼神警惕", "职业西装，衬衫，皮鞋", "冷静、精明、执行"],
  "龙海天": ["五十多岁男性，省城资本大佬", "高大或偏壮，气场强", "背头，眉眼凌厉，面部线条硬", "高档深色西装，皮鞋，腕表", "强势、傲慢、压迫"],
  "阿虎": ["三十多岁男性，杀手打手", "强壮，动作凶狠", "短发，脸部粗硬，眼神狠厉", "深色夹克，工装裤，靴子，雨衣状态可选", "凶狠、危险、沉默"],
  "杀手阿虎": ["三十多岁男性，杀手打手", "强壮，动作凶狠", "短发，脸部粗硬，眼神狠厉", "深色夹克，工装裤，靴子，雨衣状态可选", "凶狠、危险、沉默"],
  "放贷人光头": ["四十岁上下男性，高利贷头目", "偏壮，脖颈粗，压迫感强", "光头，眉骨重，鼻翼粗，眼神凶狠", "黑色短袖或深色夹克，深色裤子，皮鞋", "凶狠、贪婪、暴躁"],
};

function escapeCell(value) {
  return String(value ?? "")
    .replace(/\r?\n/g, "<br>")
    .replace(/\|/g, "｜")
    .trim();
}

function mdTable(headers, rows) {
  const head = `| ${headers.map(escapeCell).join(" |")} |`;
  const sep = `| ${headers.map(() => "---").join(" |")} |`;
  const body = rows.map((row) => `| ${headers.map((h) => escapeCell(row[h])).join(" |")} |`);
  return [head, sep, ...body].join("\n");
}

function splitList(value) {
  return String(value || "")
    .split(/[、,，]/u)
    .map((item) => item.trim())
    .filter((item) => item && item !== "无");
}

function afterFullWidthColon(line) {
  const index = Array.from(line).findIndex((char) => char.charCodeAt(0) === 65306);
  return index >= 0 ? Array.from(line).slice(index + 1).join("") : "";
}

function parseEpisode(text, fileName) {
  const episode = fileName.match(/ep(\d+)/i)?.[1] || "00";
  const groups = [];
  const lines = text.split(/\r?\n/u);
  let current = null;

  for (const line of lines) {
    const groupMatch = line.match(/^=== 第(\d+)组：(.+?)(?:（|\s*===)/u);
    if (groupMatch) {
      current = {
        episode,
        group: groupMatch[1],
        title: groupMatch[2].trim(),
        people: [],
        scenes: [],
        props: [],
        shots: [],
        body: [],
      };
      groups.push(current);
      continue;
    }
    if (!current) continue;

    if (/^\d+-\d+$/u.test(line.trim())) current.shots.push(line.trim());
    current.body.push(line);

    if (line.charCodeAt(0) === 42 && line.charCodeAt(1) === 42) {
      const key = `${line.charCodeAt(2)},${line.charCodeAt(3)}`;
      if (key === "20154,29289") current.people = splitList(afterFullWidthColon(line));
      if (key === "22330,26223") current.scenes = splitList(afterFullWidthColon(line));
      if (key === "36947,20855") current.props = splitList(afterFullWidthColon(line));
    }
  }

  return { episode, groups };
}

function mergeRefs(refs) {
  return [...new Set(refs)].join("，");
}

function groupRefs(group) {
  return group.shots.length ? group.shots.map((shot) => `ep${group.episode}:${shot}`).join("，") : `ep${group.episode}:第${group.group}组`;
}

function addAsset(map, key, group, extra = {}) {
  if (!map.has(key)) {
    map.set(key, { name: key, refs: [], groups: [], ...extra });
  }
  const item = map.get(key);
  item.refs.push(groupRefs(group));
  item.groups.push(group);
  Object.assign(item, extra);
}

function timeOf(groups) {
  const text = groups.map((g) => `${g.title} ${g.body.join(" ")}`).join(" ");
  if (/夜晚|夜色|黑夜|晚/u.test(text)) return "夜晚·室内/外可控光";
  if (/阴天|冷白日光/u.test(text)) return "白天·阴";
  if (/黄昏|傍晚/u.test(text)) return "黄昏·阴";
  if (/正午|烈日|夏日晴天|晴天/u.test(text)) return "白天·晴";
  return "白天·自然光";
}

function sceneDescription(name, groups) {
  const joined = groups
    .map((g) => {
      const lock = g.body.find((line) => line.startsWith("组首空间锁定")) || "";
      return `${g.title} ${lock.replace(/^组首空间锁定：/u, "")}`;
    })
    .join(" ");
  if (/仓库|库/u.test(name)) return `${name}，乡镇创业仓储空间，水泥地面、木门或铁门、药材麻袋/货袋、木桌账本和货架，空间纵深清楚；比例参照：仓库门约2.1米高、麻袋约成人膝高；真实瑕疵：水泥地灰尘、墙皮斑驳、木桌边缘磨损`;
  if (/办公室|厂长室|调解室|大堂|顶层/u.test(name)) return `${name}，八九十年代办公空间，木质办公桌、文件、茶杯、旧墙面和门窗，前中后景层次明确；比例参照：办公桌约0.75米高、门约2.1米高；真实瑕疵：桌角磕碰、墙面泛黄、纸张折痕`;
  if (/晒谷场|村口|院子|土路|水渠|水井|果园|药材基地/u.test(name)) return `${name}，乡村外景空间，黄土/泥地、旧墙、树木、农具和自然光，真实农村年代质感；比例参照：土路宽约3米、院门约2米高；真实瑕疵：泥地车辙、墙角积灰、木桩裂纹`;
  if (/酒楼|包厢|豪华包厢/u.test(name)) return `${name}，商务酒楼包厢，圆桌、茶具、沙发、烟灰缸，暖色室内光，压抑谈判氛围；比例参照：圆桌直径约1.6米、椅背约成人胸口高；真实瑕疵：桌面细划痕、烟灰缸污迹、墙角暗尘`;
  if (/医院|卫生院|病房/u.test(name)) return `${name}，镇卫生院病房，白墙斑驳、病床、白色被褥、搪瓷缸，暖黄顶灯；比例参照：病床约2米长、床头柜约成人腰高；真实瑕疵：墙面水渍、被褥褶皱、搪瓷杯掉漆`;
  if (/公路|车库|街道|广场/u.test(name)) return `${name}，城市/交通外景，车辆、路面、建筑入口和人流动线，商业年代质感；比例参照：车道宽约3.5米、轿车高约成人胸口；真实瑕疵：路面裂缝、车漆灰尘、墙面污渍`;
  if (/修理厂|车间|后院/u.test(name)) return `${name}，工业生产空间，水泥地、机器设备、油污、金属反光、电缆和冷白灯；比例参照：机床约成人胸口高、厂门约2.5米高；真实瑕疵：机油污渍、金属锈痕、灰尘颗粒`;
  return `${name}，${joined.slice(0, 90)}，按分镜原文布置主要空间结构和陈设；比例参照：门约2.1米高、桌面约0.75米高；真实瑕疵：边角磨损、地面积灰、墙面斑驳`;
}

function scenePrompt(name, item) {
  const desc = sceneDescription(name, item.groups);
  return `${name}空镜，${desc}，竖屏构图，35mm镜头，f/8深景深，光源方向与分镜时间一致，阴影方向统一，环境光遮蔽明显，水泥、木材、布料、金属等材质有划痕、灰尘、锈迹和磨损，正确两点透视，地平线水平，墙面垂直，参照物比例真实，轻微大气透视，近处清晰远处略柔，电影质感，8K，物理材质，空镜，无人，无人脸，可作为视频背景资产。--neg ${NEG_CN_SCENE}`;
}

function roleProfile(name) {
  if (ROLE_PROFILES[name]) return ROLE_PROFILES[name];
  if (/村民|群众|工人|司机|打手|保镖|警察|工商人员|民兵|专家|采购商|散户|果农|安保|特警|干事/u.test(name)) {
    return [`${name}，群像或职能配角`, "中等身材，符合职业身份", "中国面孔，普通现实五官，表情服务剧情", "符合身份的旧工装/制服/便装，深色裤子，布鞋或皮鞋", "真实、克制、年代感"];
  }
  if (/秘书/u.test(name)) return [`${name}，商务/机关秘书`, "中等身材，姿态职业", "中国面孔，短发或整齐发型，表情克制", "职业西装或干部夹克，衬衫，皮鞋", "谨慎、职业、执行"];
  return [`${name}，剧情配角`, "中等身材，真实普通体态", "中国面孔，发型朴素，五官自然", "符合八九十年代身份的朴素服装，深色裤子，布鞋或皮鞋", "真实、克制、短剧质感"];
}

function costumeState(name, groups) {
  const text = groups.map((g) => g.body.join(" ")).join(" ");
  if (/病床|鼻青脸肿|纱布|受伤|血痕/u.test(text) && new RegExp(name, "u").test(text)) return "受伤/病房状态";
  if (/西装|皮鞋|商务|酒楼|办公室|老板|大佬/u.test(text)) return "商务/干部状态";
  if (/工装|工人|车间|仓库|司机|退役|军绿/u.test(text)) return "工装/执行状态";
  if (/雨衣|泥水|修理厂|杀手/u.test(text)) return "行动/冲突状态";
  if (name === "林跃" && /被绑|血迹|青紫|伤痕/u.test(text)) return "受伤落难状态";
  return "常规剧情状态";
}

function characterPrompt(name, item) {
  const [identity, body, face, clothes, temperament] = roleProfile(name);
  const state = costumeState(name, item.groups);
  return `${name}角色定妆照，${identity}，${body}，${face}，全身装造：${clothes}，服装状态：${state}，多种姿态，表情动作参考镜号归并：${mergeRefs(item.refs)}，纯色或弱化场景背景，竖屏构图，50mm镜头，浅景深，主光从左前方进入，脸部阴影柔和且方向一致，皮肤有真实毛孔、轻微瑕疵和布料起球磨损，人物身高比例约1:7，身体结构自然，接触阴影真实，电影质感，8K，物理材质。--neg ${NEG_CN_PERSON}`;
}

function costumePrompt(name, item) {
  const owner = name.replace(/服装$/u, "");
  const [, , , clothes] = roleProfile(owner);
  const state = costumeState(owner, item.groups);
  return `${owner}${state}服装，${clothes}，八九十年代中国现实题材，产品特写或平铺服装参考，不带人物脸，不带剧情动作，竖屏构图，50mm镜头，柔和侧前光，布料纹理清晰，边缘磨损、褶皱、起球和缝线细节真实，比例按成人服装真实尺寸，浅景深，电影质感，8K，物理材质。--neg ${NEG_CN_ASSET}`;
}

function propDescription(name) {
  if (/协议|文件|合同|借条|账本|报告|收条|名册|通行证|逮捕令|支票|汇款单|检测报告/u.test(name)) return `${name}，纸质文件类道具，纸张泛旧，约A4或账册真实尺寸，边角有折痕、污点和压痕，红章或手写痕迹只按原文需要呈现`;
  if (/车|卡车|轿车|摩托|吉普|泥头车/u.test(name)) return `${name}，八九十年代车辆道具，相对成人比例真实，车身结构对称、重心稳定，车漆有灰尘、划痕、旧漆剥落和轮胎泥尘`;
  if (/麻袋|药材|草根|苹果|果箱|货袋/u.test(name)) return `${name}，农产品/药材货物道具，麻袋约成人膝高或木箱可搬运尺寸，粗麻布、木箱或散装药材质感，泥土、干草、磨边和污渍清楚`;
  if (/手铐|警械|枪|甩棍|木棍|铁管|刀|美工刀/u.test(name)) return `${name}，冲突类道具，相对手掌比例真实，金属/木质材质清楚，磨损、刮痕、锈点和握持痕迹真实`;
  if (/办公桌|木桌|椅|柜|沙发|茶几|床|被褥/u.test(name)) return `${name}，家具陈设道具，相对成人比例真实，旧木纹或布料质感，边角磕碰、灰尘、褶皱和磨损符合年代空间`;
  if (/电线|阀门|水闸|发电机|切片机|流水线|检测仪/u.test(name)) return `${name}，工业/机械道具，相对成人比例真实，结构稳定，金属、油污、螺丝、刻度、焊痕、旧漆和磨损细节清楚`;
  return `${name}，按分镜原文出现的可复用道具，相对成人或手掌比例真实，材质、尺寸、磨损、污渍和使用状态清楚`;
}

function propPrompt(name, item) {
  return `${name}，${propDescription(name)}，产品特写或场景内道具特写，不带人物脸，不添加原文未出现的文字，竖屏构图，70mm镜头，柔和侧前光，接触阴影明确，材质表面有划痕、灰尘、锈迹、油污或纤维毛边，比例与透视稳定，浅景深，电影质感，8K，物理材质。--neg ${NEG_CN_ASSET}`;
}

function enTime(cnTime) {
  if (cnTime.includes("夜晚")) return "night, controlled practical light";
  if (cnTime.includes("阴")) return "daytime, overcast";
  if (cnTime.includes("黄昏")) return "dusk, overcast";
  if (cnTime.includes("晴")) return "daytime, sunny";
  return "daytime, natural light";
}

function enSceneDescription(name) {
  if (/仓库|库/u.test(name)) return "township startup warehouse space, concrete floor, wooden or iron doors, sacks of herbs or cargo bags, wooden accounting table and storage racks, clear spatial depth, dusty floor, peeling wall paint and worn table edges, real-world scale with a 2.1m door and knee-high sacks";
  if (/办公室|厂长室|调解室|大堂|顶层/u.test(name)) return "1980s-1990s Chinese office interior, wooden desk, documents, teacups, aged walls and doors, layered foreground/midground/background, chipped desk corners, yellowed wall stains and folded papers, real-world scale with a 0.75m desk and 2.1m door";
  if (/晒谷场|村口|院子|土路|水渠|水井|果园|药材基地/u.test(name)) return "rural Chinese exterior, yellow dirt or mud ground, old walls, trees, farm tools and natural light, cart ruts, dusty corners and cracked wooden posts, real-world scale with a 3m dirt road and 2m gate";
  if (/酒楼|包厢|豪华包厢/u.test(name)) return "business restaurant private room, round table, tea set, sofa and ashtray, warm interior light, tense negotiation mood, tabletop scratches, dirty ashtray and dusty corners, real-world scale with a 1.6m round table";
  if (/医院|卫生院|病房/u.test(name)) return "town clinic ward, mottled white walls, hospital bed, white bedding and enamel mug, warm yellow ceiling light, water stains on wall, wrinkled bedding and chipped enamel, real-world scale with a 2m bed";
  if (/公路|车库|街道|广场/u.test(name)) return "urban or traffic exterior, vehicles, road surface, building entrance and movement paths, commercial period texture, cracked asphalt, dusty car paint and stained walls, real-world scale with a 3.5m lane";
  if (/修理厂|车间|后院/u.test(name)) return "industrial production space, concrete floor, machines, oil stains, metal reflections, cables and cool white lamps, rust marks, dust particles and worn paint, real-world scale with chest-high machinery";
  return "realistic 1980s-1990s Chinese drama set following the storyboard layout, stable architecture, aged surfaces, dust, worn edges and scratches, real-world scale references";
}

function enRoleProfile(name) {
  const known = {
    "林跃": ["male in his twenties, rural young entrepreneur", "medium-tall, upright shoulders, capable posture", "short black hair, calm eyes, defined facial lines", "plain dark jacket or worn shirt, dark trousers, cloth shoes or old leather shoes"],
    "林建国": ["male around fifty, Lin Yue's father, honest farmer", "medium build, slightly hunched shoulders, rough hands", "short graying hair, forehead lines, tired plain face", "worn cotton jacket, dark trousers, liberation shoes"],
    "张桂兰": ["female around fifty, Lin Yue's mother, rural woman", "medium-slim build, restrained movements", "tied or short graying hair, fine eye wrinkles, plain face", "dark old floral top, cloth trousers, cloth shoes"],
    "林小雅": ["girl around ten, Lin Yue's younger sister, student", "small and slim, light movements", "black braided hair, youthful face, bright eyes", "clean simple child top, new skirt or student outfit, cloth shoes"],
    "赵百川": ["male around fifty, village cadre and Zhao Daqiang's father", "medium-strong build, authoritative posture", "short graying hair, thick brows, deep nasolabial lines, gloomy eyes", "old cadre jacket, Zhongshan-style outerwear, dark trousers, black cloth shoes"],
    "赵大强": ["male in his twenties, village bully type, Zhao Baichuan's son", "stocky build, blustering posture", "short hair, restless eyes, arrogant or frightened expression", "ill-fitting suit or patterned shirt, dark trousers, leather or cloth shoes"],
    "李二狗": ["male in his twenties, village loafer", "thin build, shoulders pulled inward", "short hair, tense cheeks, evasive eyes", "old undershirt or gray worn jacket, muddy trousers, muddy shoes"],
    "供水员王四": ["male in his thirties or forties, village water-supply worker", "medium build, cautious movements", "short hair, evasive eyes, sweaty forehead", "blue-gray worn workwear, dark trousers, rubber shoes"],
    "赵雷": ["male around thirty, veteran soldier and driver-team lead", "tall, solid build, broad shoulders, upright stance", "buzz cut, hard brow structure, alert eyes", "army-green old jacket, dark work trousers, military boots"],
    "吴总": ["male around fifty, pharmaceutical boss and antagonist businessman", "medium-heavy build, relaxed but oppressive posture", "slicked-back or short hair, gloomy eyes, well-kept face", "high-end dark suit, leather shoes, wristwatch"],
    "龙海天": ["male in his fifties, provincial capital power broker", "tall or strong build, dominant presence", "slicked-back hair, sharp eyes, hard facial lines", "premium dark suit, leather shoes, wristwatch"],
  };
  if (known[name]) return known[name];
  if (/村民|群众|工人|司机|打手|保镖|警察|工商人员|民兵|专家|采购商|散户|果农|安保|特警|干事/u.test(name)) {
    return [`${name}, functional supporting or crowd character`, "medium build matching the occupation", "Chinese face, ordinary realistic features, expression serves the scene", "period-appropriate workwear, uniform or plain clothes, dark trousers, cloth or leather shoes"];
  }
  if (/秘书/u.test(name)) return [`${name}, business or government secretary`, "medium build, professional posture", "Chinese face, neat hair, restrained expression", "business suit or cadre jacket, shirt, leather shoes"];
  return [`${name}, supporting drama character`, "medium realistic body type", "Chinese face, simple hairstyle, natural features", "plain period-appropriate clothing, dark trousers, cloth or leather shoes"];
}

function enPropDescription(name) {
  if (/协议|文件|合同|借条|账本|报告|收条|名册|通行证|逮捕令|支票|汇款单|检测报告/u.test(name)) return "paper document prop, aged paper around A4 or ledger size, folded corners, stains and pressure marks, stamps or handwriting only when explicitly shown in the storyboard";
  if (/车|卡车|轿车|摩托|吉普|泥头车/u.test(name)) return "1980s-1990s vehicle prop, realistic adult-scale proportions, symmetric body structure, stable center of gravity, dusty paint, scratches, worn paint and muddy tires";
  if (/麻袋|药材|草根|苹果|果箱|货袋/u.test(name)) return "agricultural or medicinal goods prop, knee-high sack or portable wooden crate scale, coarse burlap, wooden box or loose herb texture, visible soil, dry grass, worn edges and stains";
  if (/手铐|警械|枪|甩棍|木棍|铁管|刀|美工刀/u.test(name)) return "conflict prop, realistic hand-scale proportion, clear metal or wood material, scratches, rust spots, dents and grip wear";
  if (/办公桌|木桌|椅|柜|沙发|茶几|床|被褥/u.test(name)) return "furniture prop, realistic adult-scale proportion, aged wood grain or textile texture, chipped corners, dust, wrinkles and period-appropriate wear";
  if (/电线|阀门|水闸|发电机|切片机|流水线|检测仪/u.test(name)) return "industrial or mechanical prop, realistic adult-scale proportion, stable structure, metal, oil stains, screws, scale marks, weld marks, worn paint and visible wear";
  return "reusable prop appearing in the storyboard, realistic scale relative to hand or adult body, clear material, size, wear, stains and used condition";
}

function enScenePrompt(name, item) {
  return `${name} empty environment plate, 1980s-1990s Chinese realistic short drama setting, ${enSceneDescription(name)}, no people, no human faces. Vertical composition, 35mm lens, f/8 deep depth of field, stable two-point perspective, level horizon, vertical walls, real-world scale reference with door height around 2.1m where applicable. Key light follows ${enTime(timeOf(item.groups))}, consistent shadow direction, ambient occlusion visible. Concrete, wood, fabric and metal show scratches, dust, rust, worn edges and surface imperfections. Light aerial perspective, near sharp and far slightly softer, cinematic, 8K, physically-based materials. --neg ${NEG_EN_SCENE}`;
}

function enCharacterPrompt(name, item) {
  const [identity, body, face, clothes] = enRoleProfile(name);
  const state = costumeState(name, item.groups);
  return `${name} character design reference, ${identity}, ${body}, ${face}, full-body wardrobe: ${clothes}, costume state: ${state}, multiple poses, expressions and actions referenced by shots ${mergeRefs(item.refs)}. Clean or simplified background, vertical composition, 50mm lens, shallow depth of field, key light from front-left with soft consistent shadows. Realistic skin pores, subtle facial imperfections, fabric pilling and worn edges, correct human proportion around 1:7, natural body structure, grounded contact shadows, cinematic, 8K, physically-based materials. --neg ${NEG_EN_PERSON}`;
}

function enCostumePrompt(name, item) {
  const owner = name.replace(/服装$/u, "");
  const [, , , clothes] = enRoleProfile(owner);
  const state = costumeState(owner, item.groups);
  return `${owner} ${state} costume reference, ${clothes}, 1980s-1990s Chinese realistic drama wardrobe, product close-up or flat-lay garment reference, no human face, no story action. Vertical composition, 50mm lens, soft front-side light, clear fabric weave, seams, wrinkles, pilling, worn edges and realistic textile imperfections, adult-size garment scale, shallow depth of field, cinematic, 8K, physically-based materials. --neg ${NEG_EN_ASSET}`;
}

function enPropPrompt(name, item) {
  return `${name} prop reference, ${enPropDescription(name)}, product close-up or in-scene prop detail, no human face, no text beyond what appears in the storyboard. Vertical composition, 70mm lens, soft front-side light, clear contact shadows, stable perspective and real-world scale relative to hand or adult body where applicable. Surface details include scratches, dust, rust, oil stains, worn paint or fiber edges, cinematic, 8K, physically-based materials. --neg ${NEG_EN_ASSET}`;
}

function specialName(group) {
  const text = group.body.join(" ");
  if (/特写/u.test(text)) return `${group.title}特写构图`;
  if (/俯拍|鸟瞰|航拍/u.test(text)) return `${group.title}俯拍构图`;
  if (/仰拍|低角度/u.test(text)) return `${group.title}低角度构图`;
  if (/越肩/u.test(text)) return `${group.title}越肩构图`;
  if (/主观/u.test(text)) return `${group.title}主观视角构图`;
  if (/远景|全景/u.test(text)) return `${group.title}纵深全景构图`;
  return `${group.title}特殊构图`;
}

function specialDescription(name, groups) {
  const text = groups.map((group) => group.body.join(" ")).join(" ");
  const feature = /特写/u.test(text)
    ? "局部特写，主体占画面较大，背景浅虚化"
    : /俯拍|鸟瞰|航拍/u.test(text)
      ? "高位俯视，地面动线和空间关系清楚"
      : /仰拍|低角度/u.test(text)
        ? "低角度仰视，主体压迫感强，垂直线保持稳定"
        : /越肩/u.test(text)
          ? "越肩视角，前景肩部虚化，焦点落在对面主体"
          : /主观/u.test(text)
            ? "主观视角，视线方向明确，空间比例稳定"
            : "纵深构图，前中后景层次明确";
  return `${name}，${feature}；比例参照：人物约1:7或门高约2.1米；真实瑕疵：地面积灰、边缘磨损、材质划痕，透视线稳定`;
}

function specialPrompt(name, item) {
  return `${name}，${specialDescription(name, item.groups)}，竖屏构图，镜头焦段按分镜视角选择，光源方向与场景一致，阴影方向统一，正确透视，消失点稳定，地平线水平，主体比例真实，接触阴影明确，材质表面有灰尘、磨损和划痕，电影质感，8K，物理材质。--neg ${NEG_CN_ASSET}`;
}

function enSpecialPrompt(name, item) {
  return `${name} special composition reference, ${specialDescription(name, item.groups)}, vertical composition, lens choice follows storyboard angle, stable vanishing point, level horizon, correct proportion and real-world scale reference, consistent light direction and contact shadows, surface imperfections such as dust, worn edges and scratches, cinematic, 8K, physically-based materials. --neg ${NEG_EN_ASSET}`;
}

function buildEpisodeAssets(parsed) {
  const scenes = new Map();
  const chars = new Map();
  const costumes = new Map();
  const props = new Map();
  const specials = new Map();

  for (const group of parsed.groups) {
    for (const scene of group.scenes) addAsset(scenes, scene, group);
    for (const person of group.people) {
      addAsset(chars, person, group);
      if (!/众|群众|村民|工人们|打手|保镖们|旁边的人|现场众人/u.test(person)) {
        addAsset(costumes, `${person}服装`, group);
      }
    }
    for (const prop of group.props) addAsset(props, prop, group);
    const bodyText = group.body.join(" ");
    if (/特写|俯拍|鸟瞰|航拍|仰拍|低角度|越肩|主观|远景|全景/u.test(bodyText)) {
      addAsset(specials, specialName(group), group);
    }
  }

  const sceneRows = [...scenes.values()].map((item) => ({
    "资产名称": item.name,
    "角度/视角": "全景/中远景空镜",
    "时间": timeOf(item.groups),
    "描述": sceneDescription(item.name, item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词(中文)": scenePrompt(item.name, item),
    "静态生图提示词(英文)": enScenePrompt(item.name, item),
  }));

  const charRows = [...chars.values()].map((item) => ({
    "资产名称": item.name,
    "服装状态": costumeState(item.name, item.groups),
    "姿态": "多种姿态",
    "角度/视角": "全身定妆照/半身参考",
    "时间": timeOf(item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词(中文)": characterPrompt(item.name, item),
    "静态生图提示词(英文)": enCharacterPrompt(item.name, item),
  }));

  const costumeRows = [...costumes.values()].map((item) => ({
    "资产名称": item.name,
    "描述": costumePrompt(item.name, item).split("，--neg")[0],
    "适用人物": item.name.replace(/服装$/u, ""),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词(中文)": costumePrompt(item.name, item),
    "静态生图提示词(英文)": enCostumePrompt(item.name, item),
  }));

  const propRows = [...props.values()].map((item) => ({
    "资产名称": item.name,
    "描述": propDescription(item.name),
    "角度/视角": "产品特写/道具参考",
    "时间": timeOf(item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词(中文)": propPrompt(item.name, item),
    "静态生图提示词(英文)": enPropPrompt(item.name, item),
  }));

  const specialRows = [...specials.values()].map((item) => ({
    "资产名称": item.name,
    "描述": specialDescription(item.name, item.groups),
    "角度/视角": item.name.includes("特写") ? "特写/局部构图" : item.name.includes("俯拍") ? "高位俯拍" : item.name.includes("低角度") ? "低角度仰拍" : "特殊构图参考",
    "时间": timeOf(item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词(中文)": specialPrompt(item.name, item),
    "静态生图提示词(英文)": enSpecialPrompt(item.name, item),
  }));

  return { sceneRows, charRows, costumeRows, propRows, specialRows };
}

function renderAssets(title, assets) {
  return [
    `# 《${title}》完整资产表格`,
    "",
    "## 一、场景资产（均为空镜）",
    "",
    mdTable(["资产名称", "角度/视角", "时间", "描述", "适用镜号", "静态生图提示词(中文)", "静态生图提示词(英文)"], assets.sceneRows),
    "",
    "## 二、人物资产",
    "",
    mdTable(["资产名称", "服装状态", "姿态", "角度/视角", "时间", "适用镜号", "静态生图提示词(中文)", "静态生图提示词(英文)"], assets.charRows),
    "",
    "## 三、服装资产",
    "",
    mdTable(["资产名称", "描述", "适用人物", "适用镜号", "静态生图提示词(中文)", "静态生图提示词(英文)"], assets.costumeRows),
    "",
    "## 四、道具资产",
    "",
    mdTable(["资产名称", "描述", "角度/视角", "时间", "适用镜号", "静态生图提示词(中文)", "静态生图提示词(英文)"], assets.propRows),
    "",
    "## 五、特殊视角/构图资产",
    "",
    mdTable(["资产名称", "描述", "角度/视角", "时间", "适用镜号", "静态生图提示词(中文)", "静态生图提示词(英文)"], assets.specialRows),
    "",
  ].join("\n");
}

function combineAssets(allAssets) {
  const combined = { sceneRows: [], charRows: [], costumeRows: [], propRows: [], specialRows: [] };
  for (const key of Object.keys(combined)) {
    const byName = new Map();
    for (const assets of allAssets) {
      for (const row of assets[key]) {
        const name = row["资产名称"];
        if (!byName.has(name)) byName.set(name, { ...row, "适用镜号": [] });
        byName.get(name)["适用镜号"].push(row["适用镜号"]);
      }
    }
    combined[key] = [...byName.values()].map((row) => ({
      ...row,
      "适用镜号": mergeRefs(row["适用镜号"]),
    }));
  }
  return combined;
}

function renderBible(combined) {
  const people = combined.charRows.slice(0, 80).map((row) => {
    const [identity, body, face, clothes, tone] = roleProfile(row["资产名称"]);
    return {
      "角色名": row["资产名称"],
      "身份/关系": identity,
      "年龄段/性别": identity.split("，")[0],
      "身高体态": body,
      "面部稳定特征": face,
      "发型": face.includes("短发") ? "短发/整齐发型" : "按角色身份保持稳定",
      "主要服装状态": row["服装状态"],
      "鞋/配饰": clothes,
      "气质关键词": tone,
      "备注": `适用镜号：${row["适用镜号"]}`,
    };
  });
  const scenes = combined.sceneRows.slice(0, 80).map((row) => ({
    "场景名称": row["资产名称"],
    "年代/题材": "八九十年代中国现实题材短剧",
    "空间结构": row["描述"],
    "主要材质与陈设": "按分镜原文的木门、土墙、水泥地、办公桌、药材货袋、车辆等真实材质固定",
    "光线/色调": row["时间"],
    "可复用状态": `适用镜号：${row["适用镜号"]}`,
    "提示词关键词": row["静态生图提示词(中文)"],
  }));
  const costumes = combined.costumeRows.slice(0, 80).map((row) => ({
    "服装名称": row["资产名称"],
    "对应角色": row["资产名称"].replace(/服装$/u, ""),
    "描述": row["描述"],
    "面料/颜色": "按角色身份保持朴素年代质感，真实面料纹理",
    "年代感/磨损": "八九十年代，轻微磨损和自然褶皱",
    "适用状态": `适用镜号：${row["适用镜号"]}`,
    "提示词关键词": row["静态生图提示词(中文)"],
  }));
  const props = combined.propRows.slice(0, 120).map((row) => ({
    "道具名称": row["资产名称"],
    "描述": row["描述"],
    "材质/尺寸感": "按道具类型表现真实材质、尺寸和使用痕迹",
    "文字限制": "不添加分镜原文未出现的文字",
    "年代质感": "八九十年代真实旧物质感",
    "适用角色/场景": `适用镜号：${row["适用镜号"]}`,
    "提示词关键词": row["静态生图提示词(中文)"],
  }));

  return [
    "# 《谁说泥腿子不能当老板》全局资产设定",
    "",
    "## 一、人物全身装造",
    "",
    mdTable(["角色名", "身份/关系", "年龄段/性别", "身高体态", "面部稳定特征", "发型", "主要服装状态", "鞋/配饰", "气质关键词", "备注"], people),
    "",
    "## 二、核心场景空镜",
    "",
    mdTable(["场景名称", "年代/题材", "空间结构", "主要材质与陈设", "光线/色调", "可复用状态", "提示词关键词"], scenes),
    "",
    "## 三、服装资产基准",
    "",
    mdTable(["服装名称", "对应角色", "描述", "面料/颜色", "年代感/磨损", "适用状态", "提示词关键词"], costumes),
    "",
    "## 四、关键道具基准",
    "",
    mdTable(["道具名称", "描述", "材质/尺寸感", "文字限制", "年代质感", "适用角色/场景", "提示词关键词"], props),
    "",
    "## 五、项目统一风格",
    "",
    "- 画幅：竖屏构图。",
    "- 质感：电影质感，真实光影，真实材质，避免卡通、3D 渲染、塑料感。",
    "- 人物：保持中国短剧人物审美，不使用西方人脸。",
    "- 场景：场景资产必须为空镜、无人、无人脸。",
    "- 年代/题材关键词：八九十年代中国农村创业、县城商业、药材加工、现实题材短剧。",
    "- 禁用新增元素：不添加分镜原文未出现的品牌、文字、徽章、标语。",
    "",
  ].join("\n");
}

await fs.mkdir(outputDir, { recursive: true });
const entries = await fs.readdir(inputDir);
const files = entries
  .filter((name) => /ep\d+.*storyboard\.txt$/iu.test(name))
  .sort((a, b) => a.localeCompare(b, "zh-CN", { numeric: true }));

const allAssets = [];
for (const file of files) {
  const text = await fs.readFile(path.join(inputDir, file), "utf8");
  const parsed = parseEpisode(text, file);
  const assets = buildEpisodeAssets(parsed);
  allAssets.push(assets);
  const epName = `ep${parsed.episode}`;
  await fs.writeFile(
    path.join(outputDir, `${epName}-assets.md`),
    renderAssets(`谁说泥腿子不能当老板-${epName}`, assets),
    "utf8",
  );
}

const combined = combineAssets(allAssets);
await fs.writeFile(
  path.join(outputDir, "all-assets.md"),
  renderAssets("谁说泥腿子不能当老板-全剧", combined),
  "utf8",
);
await fs.writeFile(path.join(outputDir, "asset_bible.md"), renderBible(combined), "utf8");

console.log(`Generated ${files.length} episode asset markdown files in ${outputDir}`);
