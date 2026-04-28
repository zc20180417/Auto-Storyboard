import fs from "node:fs/promises";
import path from "node:path";

const [inputDirArg, outputDirArg] = process.argv.slice(2);

if (!inputDirArg || !outputDirArg) {
  console.error("Usage: node extract-flat-storyboard-assets.mjs <flat-storyboard-dir> <output-dir>");
  process.exit(2);
}

const inputDir = path.resolve(inputDirArg);
const outputDir = path.resolve(outputDirArg);

const NEG_SCENE = "模糊，低分辨率，卡通，3D渲染，塑料感，西方人脸，过曝，AI感，人物，人，人脸";
const NEG_ASSET = "模糊，低分辨率，卡通，3D渲染，塑料感，西方人脸，过曝，AI感";

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
  if (/夜晚|夜色|黑夜|晚/u.test(text)) return "夜晚";
  if (/阴天|冷白日光/u.test(text)) return "阴天日光";
  if (/黄昏|傍晚/u.test(text)) return "傍晚";
  if (/正午|烈日|夏日晴天|晴天/u.test(text)) return "白天";
  return "白天/室内可控光";
}

function sceneDescription(name, groups) {
  const joined = groups
    .map((g) => {
      const lock = g.body.find((line) => line.startsWith("组首空间锁定")) || "";
      return `${g.title} ${lock.replace(/^组首空间锁定：/u, "")}`;
    })
    .join(" ");
  if (/仓库|库/u.test(name)) return `${name}，乡镇创业仓储空间，水泥地面、木门或铁门、药材麻袋/货袋、木桌账本和货架，空间纵深清楚，带年代感生产痕迹`;
  if (/办公室|厂长室|调解室|大堂|顶层/u.test(name)) return `${name}，八九十年代办公空间，木质办公桌、文件、茶杯、旧墙面和门窗，前中后景层次明确`;
  if (/晒谷场|村口|院子|土路|水渠|水井|果园|药材基地/u.test(name)) return `${name}，乡村外景空间，黄土/泥地、旧墙、树木、农具和自然光，真实农村年代质感`;
  if (/酒楼|包厢|豪华包厢/u.test(name)) return `${name}，商务酒楼包厢，圆桌、茶具、沙发、烟灰缸，暖色室内光，压抑谈判氛围`;
  if (/医院|卫生院|病房/u.test(name)) return `${name}，镇卫生院病房，白墙斑驳、病床、白色被褥、搪瓷缸，暖黄顶灯`;
  if (/公路|车库|街道|广场/u.test(name)) return `${name}，城市/交通外景，车辆、路面、建筑入口和人流动线，商业年代质感`;
  if (/修理厂|车间|后院/u.test(name)) return `${name}，工业生产空间，水泥地、机器设备、油污、金属反光、电缆和冷白灯`;
  return `${name}，${joined.slice(0, 90)}，按分镜原文布置主要空间结构和陈设`;
}

function scenePrompt(name, item) {
  return `${name}，八九十年代中国短剧现实题材，${sceneDescription(name, item.groups)}，${timeOf(item.groups)}，空镜，无人，无人脸，可作为视频背景资产，电影质感，4K，竖屏构图，真实材质，--neg ${NEG_SCENE}`;
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
  return `${name}，${identity}，${body}，${face}，全身装造：${clothes}，服装状态：${state}，表情动作参考镜号归并：${mergeRefs(item.refs)}，角色定妆照，全身/半身，浅景深，电影质感，4K，竖屏构图，真实中国短剧人物，--neg ${NEG_ASSET}`;
}

function costumePrompt(name, item) {
  const owner = name.replace(/服装$/u, "");
  const [, , , clothes] = roleProfile(owner);
  const state = costumeState(owner, item.groups);
  return `${owner}${state}服装，${clothes}，八九十年代中国现实题材，真实面料纹理，磨损和褶皱自然，产品特写/平铺服装参考，不带人物脸，电影质感，4K，竖屏构图，--neg ${NEG_ASSET}`;
}

function propDescription(name) {
  if (/协议|文件|合同|借条|账本|报告|收条|名册|通行证|逮捕令|支票|汇款单|检测报告/u.test(name)) return `${name}，纸质文件类道具，纸张泛旧，边角有折痕，红章或手写痕迹只按原文需要呈现`;
  if (/车|卡车|轿车|摩托|吉普|泥头车/u.test(name)) return `${name}，八九十年代车辆道具，车漆有使用痕迹，金属反光真实，轮胎带泥尘`;
  if (/麻袋|药材|草根|苹果|果箱|货袋/u.test(name)) return `${name}，农产品/药材货物道具，粗麻布、木箱或散装药材质感，带泥土和干草细节`;
  if (/手铐|警械|枪|甩棍|木棍|铁管|刀|美工刀/u.test(name)) return `${name}，冲突类道具，金属/木质材质清楚，磨损、刮痕和握持痕迹真实`;
  if (/办公桌|木桌|椅|柜|沙发|茶几|床|被褥/u.test(name)) return `${name}，家具陈设道具，旧木纹或布料质感，符合年代空间`;
  if (/电线|阀门|水闸|发电机|切片机|流水线|检测仪/u.test(name)) return `${name}，工业/机械道具，金属、油污、刻度、螺丝和磨损细节清楚`;
  return `${name}，按分镜原文出现的可复用道具，材质、尺寸、磨损和使用状态清楚`;
}

function propPrompt(name, item) {
  return `${name}，${propDescription(name)}，产品特写或场景内道具特写，不带人物脸，不添加原文未出现的文字，真实光影，电影质感，4K，竖屏构图，--neg ${NEG_ASSET}`;
}

function buildEpisodeAssets(parsed) {
  const scenes = new Map();
  const chars = new Map();
  const costumes = new Map();
  const props = new Map();

  for (const group of parsed.groups) {
    for (const scene of group.scenes) addAsset(scenes, scene, group);
    for (const person of group.people) {
      addAsset(chars, person, group);
      if (!/众|群众|村民|工人们|打手|保镖们|旁边的人|现场众人/u.test(person)) {
        addAsset(costumes, `${person}服装`, group);
      }
    }
    for (const prop of group.props) addAsset(props, prop, group);
  }

  const sceneRows = [...scenes.values()].map((item) => ({
    "资产名称": item.name,
    "角度/视角": "全景/中远景空镜",
    "时间": timeOf(item.groups),
    "描述": sceneDescription(item.name, item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词": scenePrompt(item.name, item),
  }));

  const charRows = [...chars.values()].map((item) => ({
    "资产名称": item.name,
    "服装状态": costumeState(item.name, item.groups),
    "角度/视角": "全身定妆照/半身参考",
    "时间": timeOf(item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词（含面部特征）": characterPrompt(item.name, item),
  }));

  const costumeRows = [...costumes.values()].map((item) => ({
    "资产名称": item.name,
    "描述": costumePrompt(item.name, item).split("，--neg")[0],
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词": costumePrompt(item.name, item),
  }));

  const propRows = [...props.values()].map((item) => ({
    "资产名称": item.name,
    "描述": propDescription(item.name),
    "角度/视角": "产品特写/道具参考",
    "时间": timeOf(item.groups),
    "适用镜号": mergeRefs(item.refs),
    "静态生图提示词": propPrompt(item.name, item),
  }));

  return { sceneRows, charRows, costumeRows, propRows };
}

function renderAssets(title, assets) {
  return [
    `# 《${title}》完整资产表格`,
    "",
    "## 一、场景资产（均为空镜）",
    "",
    mdTable(["资产名称", "角度/视角", "时间", "描述", "适用镜号", "静态生图提示词"], assets.sceneRows),
    "",
    "## 二、人物资产",
    "",
    mdTable(["资产名称", "服装状态", "角度/视角", "时间", "适用镜号", "静态生图提示词（含面部特征）"], assets.charRows),
    "",
    "## 三、服装资产",
    "",
    mdTable(["资产名称", "描述", "适用镜号", "静态生图提示词"], assets.costumeRows),
    "",
    "## 四、道具资产",
    "",
    mdTable(["资产名称", "描述", "角度/视角", "时间", "适用镜号", "静态生图提示词"], assets.propRows),
    "",
  ].join("\n");
}

function combineAssets(allAssets) {
  const combined = { sceneRows: [], charRows: [], costumeRows: [], propRows: [] };
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
    "提示词关键词": row["静态生图提示词"],
  }));
  const costumes = combined.costumeRows.slice(0, 80).map((row) => ({
    "服装名称": row["资产名称"],
    "对应角色": row["资产名称"].replace(/服装$/u, ""),
    "描述": row["描述"],
    "面料/颜色": "按角色身份保持朴素年代质感，真实面料纹理",
    "年代感/磨损": "八九十年代，轻微磨损和自然褶皱",
    "适用状态": `适用镜号：${row["适用镜号"]}`,
    "提示词关键词": row["静态生图提示词"],
  }));
  const props = combined.propRows.slice(0, 120).map((row) => ({
    "道具名称": row["资产名称"],
    "描述": row["描述"],
    "材质/尺寸感": "按道具类型表现真实材质、尺寸和使用痕迹",
    "文字限制": "不添加分镜原文未出现的文字",
    "年代质感": "八九十年代真实旧物质感",
    "适用角色/场景": `适用镜号：${row["适用镜号"]}`,
    "提示词关键词": row["静态生图提示词"],
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
