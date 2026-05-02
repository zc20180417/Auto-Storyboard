import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const [inputDirArg, outputDirArg, ...optionArgs] = process.argv.slice(2);

if (!inputDirArg || !outputDirArg) {
  console.error("Usage: node extract-flat-storyboard-assets.mjs <flat-storyboard-dir> <output-dir> [--project=<name>] [--bible=<asset_bible.md>]");
  process.exit(2);
}

const inputDir = path.resolve(inputDirArg);
const outputDir = path.resolve(outputDirArg);
const options = Object.fromEntries(
  optionArgs
    .filter((arg) => arg.startsWith("--"))
    .map((arg) => {
      const [key, ...rest] = arg.slice(2).split("=");
      return [key, rest.join("=") || "true"];
    }),
);

let projectName = options.project || path.basename(inputDir);
const biblePath = options.bible ? path.resolve(options.bible) : "";
const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const skillPath = path.resolve(scriptDir, "..", "SKILL.md");
const optimizeSkillPath = path.resolve(scriptDir, "..", "..", "optimize-image-prompts", "SKILL.md");

function projectNameFromFile(fileName) {
  return fileName.replace(/-?ep\d+.*$/iu, "").replace(/[-_]+$/u, "").trim();
}

function episodeIdFromFile(fileName, fallbackIndex) {
  const match = fileName.match(/ep(\d+)/iu);
  if (match) return `ep${match[1].padStart(2, "0")}`;
  return `ep${String(fallbackIndex + 1).padStart(2, "0")}`;
}

function taskText({ episodeId, sourceFile, bibleRelativePath }) {
  const bibleLine = bibleRelativePath
    ? `- 全局资产设定：\`${bibleRelativePath}\``
    : "- 全局资产设定：当前未提供；如需跨集一致性，请先由大模型读取全剧分镜后创建 run 级 `asset_bible.md`。";
  const assetSkillRelativePath = path.relative(outputDir, skillPath).replace(/\\/gu, "/");
  const optimizeSkillRelativePath = path.relative(outputDir, optimizeSkillPath).replace(/\\/gu, "/");

  return [
    `# ${projectName} ${episodeId} 资产抽取任务`,
    "",
    "本目录由脚本整理输入文件生成。脚本只做文件准备，不抽取资产、不改写提示词、不生成资产表正文。",
    "",
    "## 输入",
    "",
    `- 分镜文件：\`final.txt\``,
    `- 源文件名：\`${sourceFile}\``,
    bibleLine,
    `- 资产抽取规则：\`${assetSkillRelativePath}\``,
    `- 提示词优化规则：\`${optimizeSkillRelativePath}\``,
    "",
    "## 执行要求",
    "",
    "1. 读取 `final.txt`、资产抽取规则、提示词优化规则和全局资产设定。",
    "2. 由大模型判断本集需要沉淀哪些可复用资产，不使用脚本模板或关键词硬编码代替判断。",
    "3. 生成 `assets.md`，包含场景资产、人物资产、服装资产、道具资产、特殊视角/构图资产五部分。",
    "4. 道具资产只保留需要提前稳定生成的关键物件；常驻场景陈设归入场景资产，角色常驻配饰归入人物/服装资产，一次性背景小物不提取。",
    "5. `静态生图提示词(中文)` 和 `静态生图提示词(英文)` 必须在生成时直接采用提示词优化规则，不写待优化占位稿。",
    "6. 检查 `assets.md` 后，再运行 `assets-md-to-xlsx.mjs` 转换出 `assets.xlsx`。",
    "",
    "## 输出",
    "",
    "- `assets.md`",
    "- `assets.xlsx`",
    "",
  ].join("\n");
}

function nextStepsText(episodes, bibleTarget) {
  const bibleLine = biblePath
    ? `已引用全局资产设定：\`${bibleTarget}\``
    : "未提供全局资产设定。多集项目建议先由大模型创建 run 级 `asset_bible.md`，再逐集抽取资产。";

  return [
    `# ${projectName} 扁平分镜资产抽取工作区`,
    "",
    "本工作区只完成输入整理。资产表正文必须由大模型按 `agent_skills/asset-extractor/SKILL.md` 生成，并在提示词列中直接采用 `agent_skills/optimize-image-prompts/SKILL.md` 的优化原则；脚本不得批量生成或伪造资产内容。",
    "",
    bibleLine,
    "",
    "## 待处理集数",
    "",
    ...episodes.map((episode) => `- \`${episode.id}\`：读取 \`${episode.taskPath}\` 后生成该集资产表。`),
    "",
    "## 转换 Excel",
    "",
    "每集 `assets.md` 生成并人工/模型检查后运行：",
    "",
    "```powershell",
    "node .\\agent_skills\\asset-extractor\\scripts\\assets-md-to-xlsx.mjs <episode-dir>\\assets.md <episode-dir>\\assets.xlsx",
    "```",
    "",
  ].join("\n");
}

await fs.mkdir(outputDir, { recursive: true });
const entries = await fs.readdir(inputDir);
const files = entries
  .filter((name) => /ep\d+.*storyboard\.txt$/iu.test(name) || /ep\d+.*final\.txt$/iu.test(name))
  .sort((a, b) => a.localeCompare(b, "zh-CN", { numeric: true }));

if (!files.length) {
  console.error(`No flat storyboard files found in ${inputDir}`);
  process.exit(1);
}

const resolvedProjectName = options.project || projectNameFromFile(files[0]) || projectName;
projectName = resolvedProjectName;

let bibleTarget = "";
if (biblePath) {
  bibleTarget = path.join(outputDir, "asset_bible.md");
  await fs.copyFile(biblePath, bibleTarget);
}

const episodes = [];
for (const [index, file] of files.entries()) {
  const episodeId = episodeIdFromFile(file, index);
  const episodeDir = path.join(outputDir, "episodes", episodeId);
  await fs.mkdir(episodeDir, { recursive: true });
  await fs.copyFile(path.join(inputDir, file), path.join(episodeDir, "final.txt"));

  const bibleRelativePath = bibleTarget ? path.relative(episodeDir, bibleTarget).replace(/\\/gu, "/") : "";
  const taskPath = path.join(episodeDir, "TASK.md");
  await fs.writeFile(taskPath, taskText({ episodeId, sourceFile: file, bibleRelativePath }), "utf8");
  episodes.push({
    id: episodeId,
    taskPath: path.relative(outputDir, taskPath).replace(/\\/gu, "/"),
  });
}

await fs.writeFile(
  path.join(outputDir, "NEXT_STEPS.md"),
  nextStepsText(episodes, bibleTarget ? path.relative(outputDir, bibleTarget).replace(/\\/gu, "/") : ""),
  "utf8",
);

console.log(`Prepared ${episodes.length} episode asset tasks in ${outputDir}`);
console.log("No assets.md or asset_bible.md content was generated by script logic.");
