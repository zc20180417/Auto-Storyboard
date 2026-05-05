import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const [inputDirArg, outputDirArg, ...optionArgs] = process.argv.slice(2);

if (!inputDirArg || !outputDirArg) {
  console.error("Usage: node extract-flat-storyboard-assets.mjs <flat-storyboard-dir> <output-dir> [--project=<name>] [--bible=<asset_bible.md>] [--allow-missing-bible=true]");
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
const reviewerSkillPath = path.resolve(scriptDir, "..", "..", "asset-reviewer", "SKILL.md");
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
    : "- 全局资产设定：当前未提供；仅允许单集项目继续。多集项目必须先建立 run 级 `asset_bible.md`。";
  const assetSkillRelativePath = path.relative(outputDir, skillPath).replace(/\\/gu, "/");
  const reviewerSkillRelativePath = path.relative(outputDir, reviewerSkillPath).replace(/\\/gu, "/");
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
    `- 资产审核规则：\`${reviewerSkillRelativePath}\``,
    `- 提示词优化规则：\`${optimizeSkillRelativePath}\``,
    "",
    "## 执行要求",
    "",
    "1. 读取 `final.txt`、资产抽取规则、资产审核规则、提示词优化规则和全局资产设定。",
    "2. 由大模型判断本集需要沉淀哪些可复用资产，不使用脚本模板或关键词硬编码代替判断。",
    "3. 生成 `assets.md`，标题为 `《剧名 epXX》资产增量与使用索引`，必须包含：`一、本集复用资产索引`、`二、本集新增资产状态`、`三、本集新增基础资产`、`四、本集关键道具与场景状态`、`五、本集不建议入库元素`。",
    "4. 分集默认不重复输出 `asset_bible` 已有基础资产的完整提示词；已有资产写入复用索引，新状态写入新增资产状态，新人物/场景/服装/道具才写入新增基础资产。",
    "5. 只有状态变了、服装变了、外观条件变了、场景光线/破损状态变了、道具状态变了，才新增 `state_id`；短暂表情、手势、台词眼神通常写入不建议入库元素。",
    "6. 用 `asset-reviewer` 对照 `final.txt`、`assets.md`、`asset_bible.md` 和两份 skill 做真实审核，输出 `asset_review.json`。",
    "7. 如果 reviewer 返回 hard issues，只局部修复对应资产并复审；不要无关重写。通过后写 `asset_status.json`。",
    "8. `asset_status.json` 必须记录 `reviewer_source: \"asset-reviewer\"`、`reviewer_pass`、issues/warnings 数量和 `bible_update_candidates`。",
    "9. 检查 `assets.md` 后，再运行 `assets-md-to-xlsx.mjs --mode=episode` 转换出 `assets.xlsx`。",
    "10. 运行 `validate-assets.mjs` 做机械门禁校验，通过后才算本集资产完成。",
    "",
    "## 输出",
    "",
    "- `assets.md`",
    "- `assets.xlsx`",
    "- `asset_review.json`",
    "- `asset_status.json`",
    "",
  ].join("\n");
}

function nextStepsText(episodes, bibleTarget) {
  const bibleLine = biblePath
    ? `已引用全局资产设定：\`${bibleTarget}\``
    : "未提供全局资产设定。仅允许单集项目继续；多集项目必须先由大模型创建 run 级 `asset_bible.md`。";

  return [
    `# ${projectName} 扁平分镜资产抽取工作区`,
    "",
    "本工作区只完成输入整理。资产表正文必须由大模型按 `agent_skills/asset-extractor/SKILL.md` 生成资产增量与使用索引，并在新增基础资产/新增状态的提示词列中直接采用 `agent_skills/optimize-image-prompts/SKILL.md` 的优化原则；审核必须按 `agent_skills/asset-reviewer/SKILL.md` 真实执行。脚本不得批量生成或伪造资产内容、审核结果或状态。",
    "",
    bibleLine,
    "",
    "## 待处理集数",
    "",
    ...episodes.map((episode) => `- \`${episode.id}\`：读取 \`${episode.taskPath}\` 后生成该集资产表、真实审核并写入状态。`),
    "",
    "## 转换 Excel",
    "",
    "每集 `assets.md` 通过 `asset-reviewer` 后运行：",
    "",
    "```powershell",
    "node .\\agent_skills\\asset-extractor\\scripts\\assets-md-to-xlsx.mjs <episode-dir>\\assets.md <episode-dir>\\assets.xlsx --mode=episode",
    "node .\\agent_skills\\asset-extractor\\scripts\\validate-assets.mjs <episode-dir>",
    "```",
    "",
    "只收集 `asset_status.json` 中 `status=done`、`reviewer_source=asset-reviewer`、`reviewer_pass=true`、`reviewer_issues_count=0` 的 episode。",
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

if (files.length > 1 && !biblePath && options["allow-missing-bible"] !== "true") {
  console.error(
    "Multiple episode files were found, but no --bible was provided. Build a run-level asset_bible.md first, then rerun with --bible=<asset_bible.md>. Use --allow-missing-bible=true only for an explicit bible-building bootstrap pass.",
  );
  process.exit(2);
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
