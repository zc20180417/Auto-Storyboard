import fs from "node:fs/promises";
import { createRequire } from "node:module";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [inputPath, outputPath, ...optionArgs] = process.argv.slice(2);
const options = Object.fromEntries(
  optionArgs
    .filter((arg) => arg.startsWith("--"))
    .map((arg) => {
      const [key, ...rest] = arg.slice(2).split("=");
      return [key, rest.join("=") || "true"];
    }),
);
const mode = options.mode || "episode";

if (!inputPath || !outputPath) {
  console.error("Usage: node assets-md-to-xlsx.mjs <assets.md> <assets.xlsx> [--mode=episode|registry]");
  process.exit(2);
}

const SCHEMAS = {
  episode: {
    sheetNames: {
      "一、本集复用资产索引": "复用资产索引",
      "二、本集新增资产状态": "新增资产状态",
      "三、本集新增基础资产": "新增基础资产",
      "四、本集关键道具与场景状态": "关键道具与场景状态",
      "五、本集不建议入库元素": "不建议入库元素",
      "六、本集分镜资产绑定索引": "分镜资产绑定索引",
    },
    requiredColumns: {
      "复用资产索引": ["使用ID", "episode_id", "cut_ids", "asset_id", "state_id", "asset_type", "source", "episode_usage", "本集用途", "needs_generation", "generation_note"],
      "新增资产状态": ["state_id", "episode_id", "cut_ids", "asset_id", "parent_state_id", "asset_type", "status_type", "state_summary", "changed_fields", "reuse_policy", "first_seen_episode", "episode_usage", "needs_generation", "generation_note", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
      "新增基础资产": ["asset_id", "asset_type", "asset_name", "description", "reuse_policy", "first_seen_episode", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
      "关键道具与场景状态": ["state_id", "episode_id", "cut_ids", "asset_id", "asset_type", "state_summary", "episode_usage", "needs_generation", "generation_note", "入库建议"],
      "不建议入库元素": ["元素", "出现位置", "不入库原因"],
      "分镜资产绑定索引": ["binding_id", "episode_id", "cut_id", "asset_id", "state_id", "asset_type", "binding_role", "reference_priority", "use_for_video", "required_for_generation", "source", "note"],
    },
  },
  registry: {
    sheetNames: {
      "一、基础人物资产": "基础人物资产",
      "二、人物状态资产": "人物状态资产",
      "三、服装资产": "服装资产",
      "四、场景基础资产": "场景基础资产",
      "五、场景状态资产": "场景状态资产",
      "六、道具基础资产": "道具基础资产",
      "七、道具状态资产": "道具状态资产",
      "八、特殊构图资产": "特殊构图资产",
      "九、项目统一风格": "项目统一风格",
    },
    requiredColumns: {
      "基础人物资产": ["asset_id", "角色名", "身份/关系", "年龄段/性别", "身高体态", "面部稳定特征", "发型", "气质关键词", "基础提示词"],
      "人物状态资产": ["state_id", "asset_id", "状态类型", "状态名称", "服装ID", "外观变化", "首次出现", "复用范围", "状态提示词"],
      "服装资产": ["costume_id", "对应角色asset_id", "服装名称", "描述", "面料/颜色", "年代感/磨损", "复用范围", "提示词"],
      "场景基础资产": ["scene_id", "场景名称", "空间结构", "主要材质", "核心陈设", "基础光线", "基础提示词"],
      "场景状态资产": ["scene_state_id", "scene_id", "状态类型", "光线/时间", "空间状态", "变化字段", "首次出现", "状态提示词"],
      "道具基础资产": ["prop_id", "道具名称", "材质/形状", "尺寸感", "文字限制", "基础提示词"],
      "道具状态资产": ["prop_state_id", "prop_id", "状态类型", "状态说明", "变化字段", "首次出现", "状态提示词"],
      "特殊构图资产": ["composition_id", "构图名称", "关联资产ID", "是否含人物", "构图用途", "复用范围", "提示词"],
      "项目统一风格": ["项目", "内容"],
    },
  },
};

const schema = SCHEMAS[mode];
if (!schema) {
  console.error(`Unknown mode: ${mode}. Use --mode=episode or --mode=registry.`);
  process.exit(2);
}

async function loadArtifactTool() {
  try {
    return await import("@oai/artifact-tool");
  } catch (error) {
    if (error?.code !== "ERR_MODULE_NOT_FOUND") {
      throw error;
    }
  }

  const require = createRequire(import.meta.url);
  const nodePathCandidates = (process.env.NODE_PATH || "")
    .split(path.delimiter)
    .filter(Boolean);
  const codexRuntimeModules = path.join(
    os.homedir(),
    ".cache",
    "codex-runtimes",
    "codex-primary-runtime",
    "dependencies",
    "node",
    "node_modules",
  );
  const searchPaths = [process.cwd(), codexRuntimeModules, ...nodePathCandidates];
  const resolved = require.resolve("@oai/artifact-tool", { paths: searchPaths });
  return import(pathToFileURL(resolved).href);
}

function parseMarkdownTables(markdown) {
  const lines = markdown.split(/\r?\n/);
  const tables = [];
  let currentSection = "";

  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (/^#{1,3}\s+/.test(line)) {
      currentSection = line.replace(/^#{1,3}\s+/, "").trim();
      continue;
    }
    if (!line.startsWith("|")) {
      continue;
    }

    const next = (lines[i + 1] || "").trim();
    if (!next.startsWith("|") || !/^\|[\s:|\-]+\|$/.test(next)) {
      continue;
    }

    const rows = [];
    const tableStart = i;
    for (let j = tableStart; j < lines.length; j += 1) {
      const row = lines[j].trim();
      if (!row.startsWith("|")) {
        break;
      }
      if (j === tableStart + 1) {
        continue;
      }
      rows.push(parseMarkdownRow(row));
      i = j;
    }

    if (rows.length > 0) {
      tables.push({ section: currentSection, rows });
    }
  }

  return tables;
}

function parseMarkdownRow(row) {
  return row
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim().replace(/<br\s*\/?>/gi, "\n"));
}

function clampWidthPx(text, min, max) {
  const length = String(text || "").length;
  return Math.max(min, Math.min(max, length * 7 + 28));
}

function safeSheetName(section, fallbackIndex) {
  const key = Object.keys(schema.sheetNames).find((prefix) => section.startsWith(prefix));
  return key ? schema.sheetNames[key] : `资产表${fallbackIndex + 1}`;
}

function standardSheetName(section) {
  const key = Object.keys(schema.sheetNames).find((prefix) => section.startsWith(prefix));
  return key ? schema.sheetNames[key] : "";
}

function validateTables(tables) {
  const standardTables = tables
    .map((table) => ({ ...table, sheetName: standardSheetName(table.section) }))
    .filter((table) => table.sheetName);
  const foundSheets = new Set(standardTables.map((table) => table.sheetName));
  const missing = Object.values(schema.sheetNames).filter((sheet) => !foundSheets.has(sheet));
  if (missing.length > 0) {
    throw new Error(`Missing required asset tables: ${missing.join(", ")}`);
  }

  for (const table of standardTables) {
    const [header, ...dataRows] = table.rows;
    if (!header || header.length === 0) {
      throw new Error(`Missing header row in ${table.section}`);
    }

    const required = schema.requiredColumns[table.sheetName] || [];
    const missingColumns = required.filter((column) => !header.includes(column));
    if (missingColumns.length > 0) {
      throw new Error(`${table.section} is missing required columns: ${missingColumns.join(", ")}`);
    }

    dataRows.forEach((row, index) => {
      if (row.length !== header.length) {
        throw new Error(
          `${table.section} row ${index + 2} has ${row.length} cells but header has ${header.length}. Avoid raw "|" inside cells; use Chinese punctuation or <br>.`,
        );
      }
    });
  }

  return standardTables;
}

function rowsBySheet(sheetName) {
  const table = standardTables.find((candidate) => candidate.sheetName === sheetName);
  if (!table) return [];
  const [header, ...dataRows] = table.rows;
  if (!header) return [];
  return dataRows.map((row) => Object.fromEntries(header.map((column, index) => [column, row[index] || ""])));
}

function buildAssetBindingsPayload() {
  const rows = rowsBySheet("分镜资产绑定索引");
  const episodeId = options.episode || rows.find((row) => row.episode_id)?.episode_id || "";
  const project =
    options.project ||
    path.basename(path.dirname(path.resolve(outputPath))) ||
    path.basename(path.dirname(path.resolve(inputPath)));
  return {
    project,
    episode_id: episodeId,
    bindings: rows.map((row) => ({
      binding_id: row.binding_id || "",
      cut_id: row.cut_id || "",
      asset_id: row.asset_id || "",
      state_id: row.state_id || "",
      asset_type: row.asset_type || "",
      binding_role: row.binding_role || "",
      reference_priority: row.reference_priority || "",
      use_for_video: row.use_for_video || "",
      required_for_generation: row.required_for_generation || "",
      source: row.source || "",
      note: row.note || "",
    })),
  };
}

function columnName(colCount) {
  let n = colCount;
  let name = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    name = String.fromCharCode(65 + rem) + name;
    n = Math.floor((n - 1) / 26);
  }
  return name;
}

const markdown = await fs.readFile(inputPath, "utf8");
const tables = parseMarkdownTables(markdown);

if (tables.length === 0) {
  console.error(`No markdown tables found in ${inputPath}`);
  process.exit(1);
}

let standardTables;
try {
  standardTables = validateTables(tables);
} catch (error) {
  console.error(error.message);
  process.exit(1);
}

const { SpreadsheetFile, Workbook } = await loadArtifactTool();
const workbook = Workbook.create();

standardTables.forEach((table, index) => {
  const sheet = workbook.worksheets.add(safeSheetName(table.section, index));
  const rows = table.rows;
  const rowCount = rows.length;
  const colCount = Math.max(...rows.map((row) => row.length));
  const matrix = rows.map((row) => {
    const padded = [...row];
    while (padded.length < colCount) padded.push("");
    return padded;
  });

  const used = sheet.getRangeByIndexes(0, 0, rowCount, colCount);
  used.values = matrix;
  used.format.wrapText = true;
  used.format.verticalAlignment = "top";

  const header = sheet.getRangeByIndexes(0, 0, 1, colCount);
  header.format.fill.color = "#1F4E78";
  header.format.font.color = "#FFFFFF";
  header.format.font.bold = true;
  header.format.horizontalAlignment = "center";
  header.format.rowHeightPx = 34;

  for (let c = 0; c < colCount; c += 1) {
    const columnText = matrix.map((row) => row[c] || "").join("");
    const max = c === colCount - 1 ? 560 : 240;
    sheet.getRangeByIndexes(0, c, rowCount, 1).format.columnWidthPx = clampWidthPx(columnText, 90, max);
  }

  sheet.getRangeByIndexes(0, 0, rowCount, colCount).format.rowHeightPx = 72;
  sheet.freezePanes.freezeRows(1);

  const tableRange = `A1:${columnName(colCount)}${rowCount}`;
  const tableName = `${sheet.name.replace(/[^\p{L}\p{N}]/gu, "")}Table`;
  sheet.tables.add(tableRange, true, tableName);
});

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

if (mode === "episode") {
  const bindingsPath = options["asset-bindings"]
    ? path.resolve(options["asset-bindings"])
    : path.join(path.dirname(path.resolve(outputPath)), "asset_bindings.json");
  await fs.writeFile(bindingsPath, `${JSON.stringify(buildAssetBindingsPayload(), null, 2)}\n`, "utf8");
  console.log(`saved ${bindingsPath}`);
}

const inspect = await workbook.inspect({
  kind: "sheet",
  include: "id,name",
});
console.log(inspect.ndjson);
console.log(`saved ${outputPath}`);
