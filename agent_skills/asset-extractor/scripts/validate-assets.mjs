import fs from "node:fs/promises";
import path from "node:path";

const [episodeDirArg] = process.argv.slice(2);

if (!episodeDirArg) {
  console.error("Usage: node validate-assets.mjs <episode-dir>");
  process.exit(2);
}

const episodeDir = path.resolve(episodeDirArg);
const requiredFiles = {
  assets: path.join(episodeDir, "assets.md"),
  workbook: path.join(episodeDir, "assets.xlsx"),
  review: path.join(episodeDir, "asset_review.json"),
  status: path.join(episodeDir, "asset_status.json"),
};

const REQUIRED_TABLES = [
  "本集复用资产索引",
  "本集新增资产状态",
  "本集新增基础资产",
  "本集关键道具与场景状态",
  "本集不建议入库元素",
];
const REQUIRED_SHEETS = [
  "复用资产索引",
  "新增资产状态",
  "新增基础资产",
  "关键道具与场景状态",
  "不建议入库元素",
];

const REQUIRED_AUDIT_COVERAGE = [
  "asset_coverage",
  "asset_selection",
  "bible_consistency",
  "registry_structure",
  "duplicate_control",
  "state_modeling",
  "category_boundary",
  "prompt_fidelity",
  "bilingual_consistency",
  "time_range_accuracy",
  "xlsx_readiness",
];

const SEMANTIC_COVERAGE_GROUPS = {
  duplicate_control: ["duplicate_base_asset", "unnecessary_regeneration"],
  state_modeling: ["state_should_be_variant", "variant_over_split", "variant_under_split"],
  bible_consistency: ["bible_conflict", "identity_drift", "costume_state_conflict", "scene_state_conflict", "prop_state_conflict"],
  prompt_fidelity: ["prompt_hallucination", "prop_text_violation", "empty_scene_contamination", "bilingual_mismatch"],
  time_or_xlsx: ["time_range_error", "xlsx_readiness"],
};

const ENUMS = {
  source: ["asset_bible", "episode_new", "episode_variant"],
  asset_type: ["character", "costume", "scene", "prop", "composition"],
  status_type: [
    "base",
    "costume_change",
    "dirt_damage",
    "lighting_time",
    "injury",
    "scene_condition",
    "prop_condition",
    "composition_reference",
    "other",
  ],
  reuse_policy: ["global", "episode_range", "one_episode", "shot_only"],
  needs_generation: ["yes", "no", "conditional"],
  sync_to_bible: ["yes", "no", "candidate"],
  semantic_result: ["pass", "warning", "issue"],
};

const REQUIRED_COLUMNS = {
  "复用资产索引": ["使用ID", "asset_id", "state_id", "asset_type", "source", "episode_usage", "本集用途", "needs_generation", "generation_note"],
  "新增资产状态": ["state_id", "asset_id", "parent_state_id", "asset_type", "status_type", "state_summary", "changed_fields", "reuse_policy", "first_seen_episode", "episode_usage", "needs_generation", "generation_note", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
  "新增基础资产": ["asset_id", "asset_type", "asset_name", "description", "reuse_policy", "first_seen_episode", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
  "关键道具与场景状态": ["state_id", "asset_id", "asset_type", "state_summary", "episode_usage", "needs_generation", "generation_note", "入库建议"],
  "不建议入库元素": ["元素", "出现位置", "不入库原因"],
};

const SECTION_TO_SHEET = {
  "一、本集复用资产索引": "复用资产索引",
  "二、本集新增资产状态": "新增资产状态",
  "三、本集新增基础资产": "新增基础资产",
  "四、本集关键道具与场景状态": "关键道具与场景状态",
  "五、本集不建议入库元素": "不建议入库元素",
};

const TABLE_ENUM_COLUMNS = {
  "复用资产索引": {
    source: ENUMS.source,
    asset_type: ENUMS.asset_type,
    needs_generation: ENUMS.needs_generation,
  },
  "新增资产状态": {
    asset_type: ENUMS.asset_type,
    status_type: ENUMS.status_type,
    reuse_policy: ENUMS.reuse_policy,
    needs_generation: ENUMS.needs_generation,
    sync_to_bible: ENUMS.sync_to_bible,
  },
  "新增基础资产": {
    asset_type: ENUMS.asset_type,
    reuse_policy: ENUMS.reuse_policy,
    sync_to_bible: ENUMS.sync_to_bible,
  },
  "关键道具与场景状态": {
    asset_type: ENUMS.asset_type,
    needs_generation: ENUMS.needs_generation,
  },
};

const REQUIRED_NONEMPTY_COLUMNS = {
  "复用资产索引": ["使用ID", "asset_id", "state_id", "asset_type", "source", "episode_usage", "needs_generation"],
  "新增资产状态": ["state_id", "asset_id", "asset_type", "status_type", "reuse_policy", "episode_usage", "needs_generation", "sync_to_bible"],
  "新增基础资产": ["asset_id", "asset_type", "asset_name", "reuse_policy", "first_seen_episode", "sync_to_bible"],
  "关键道具与场景状态": ["state_id", "asset_id", "asset_type", "episode_usage", "needs_generation"],
  "不建议入库元素": ["元素", "出现位置", "不入库原因"],
};

const errors = [];

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function readJson(filePath, label) {
  try {
    return JSON.parse(await fs.readFile(filePath, "utf8"));
  } catch (error) {
    errors.push(`${label} is not valid JSON: ${error.message}`);
    return null;
  }
}

function parseMarkdownRow(row) {
  return row
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
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
    if (!line.startsWith("|")) continue;

    const next = (lines[i + 1] || "").trim();
    if (!next.startsWith("|") || !/^\|[\s:|\-]+\|$/.test(next)) continue;

    const rows = [];
    const tableStart = i;
    for (let j = tableStart; j < lines.length; j += 1) {
      const row = lines[j].trim();
      if (!row.startsWith("|")) break;
      if (j !== tableStart + 1) rows.push(parseMarkdownRow(row));
      i = j;
    }

    if (rows.length > 0) tables.push({ section: currentSection, rows });
  }

  return tables;
}

function validateAssetsMarkdown(markdown) {
  const tables = parseMarkdownTables(markdown);
  const standardTables = tables
    .map((table) => {
      const prefix = Object.keys(SECTION_TO_SHEET).find((candidate) => table.section.startsWith(candidate));
      return prefix ? { ...table, sheetName: SECTION_TO_SHEET[prefix] } : null;
    })
    .filter(Boolean);

  const found = new Set(standardTables.map((table) => table.sheetName));
  for (const table of REQUIRED_SHEETS) {
    if (!found.has(table)) errors.push(`assets.md missing required table: ${table}`);
  }

  for (const table of standardTables) {
    const [header, ...dataRows] = table.rows;
    if (!header) {
      errors.push(`${table.section} missing header row`);
      continue;
    }

    const requiredColumns = REQUIRED_COLUMNS[table.sheetName] || [];
    const missing = requiredColumns.filter((column) => !header.includes(column));
    if (missing.length > 0) {
      errors.push(`${table.section} missing required columns: ${missing.join(", ")}`);
    }

    dataRows.forEach((row, index) => {
      if (row.length !== header.length) {
        errors.push(`${table.section} row ${index + 2} has ${row.length} cells but header has ${header.length}`);
        return;
      }

      validateRowValues(table, header, row, index + 2);
    });
  }
}

function columnValue(header, row, column) {
  const index = header.indexOf(column);
  return index >= 0 ? row[index] : "";
}

function validateRowValues(table, header, row, rowNumber) {
  for (const column of REQUIRED_NONEMPTY_COLUMNS[table.sheetName] || []) {
    if (!columnValue(header, row, column)) {
      errors.push(`${table.section} row ${rowNumber} column ${column} must not be empty`);
    }
  }

  const enumColumns = TABLE_ENUM_COLUMNS[table.sheetName] || {};
  for (const [column, allowedValues] of Object.entries(enumColumns)) {
    const value = columnValue(header, row, column);
    if (value && !allowedValues.includes(value)) {
      errors.push(`${table.section} row ${rowNumber} column ${column} has invalid value "${value}". Allowed: ${allowedValues.join(", ")}`);
    }
  }

  const stateId = columnValue(header, row, "state_id");
  if (header.includes("state_id") && !stateId) {
    errors.push(`${table.section} row ${rowNumber} state_id must not be empty; use BASE when no state applies`);
  }
}

function validateReview(review) {
  if (!review) return;
  if (review.pass !== true) errors.push("asset_review.pass must be true");
  if (!Array.isArray(review.issues)) errors.push("asset_review.issues must be an array");
  if (Array.isArray(review.issues) && review.issues.length !== 0) errors.push("asset_review.issues must be empty");
  if (!Array.isArray(review.warnings)) errors.push("asset_review.warnings must be an array");

  const checkedTables = new Set(Array.isArray(review.checked_tables) ? review.checked_tables : []);
  for (const table of REQUIRED_TABLES) {
    if (!checkedTables.has(table)) errors.push(`asset_review.checked_tables missing: ${table}`);
  }

  for (const key of REQUIRED_AUDIT_COVERAGE) {
    if (review.audit_coverage?.[key] !== "checked") {
      errors.push(`asset_review.audit_coverage.${key} must be "checked"`);
    }
  }

  if (!Array.isArray(review.spot_checks) || review.spot_checks.length < 3) {
    errors.push("asset_review.spot_checks must contain at least 3 entries");
  }

  if (!Array.isArray(review.semantic_checks) || review.semantic_checks.length < 5) {
    errors.push("asset_review.semantic_checks must contain at least 5 entries");
    return;
  }

  review.semantic_checks.forEach((check, index) => {
    for (const field of ["table", "type", "result", "evidence", "fix_instruction"]) {
      if (!check?.[field]) errors.push(`asset_review.semantic_checks[${index}] missing ${field}`);
    }
    if (check?.result && !ENUMS.semantic_result.includes(check.result)) {
      errors.push(`asset_review.semantic_checks[${index}].result has invalid value "${check.result}"`);
    }
    if (review.pass === true && check?.result === "issue") {
      errors.push(`asset_review.semantic_checks[${index}] result=issue but asset_review.pass=true`);
    }
  });

  const semanticTypes = new Set(review.semantic_checks.map((check) => check.type));
  for (const [group, types] of Object.entries(SEMANTIC_COVERAGE_GROUPS)) {
    if (!types.some((type) => semanticTypes.has(type))) {
      errors.push(`asset_review.semantic_checks missing coverage for ${group}: ${types.join(" or ")}`);
    }
  }
}

function validateStatus(status, review) {
  if (!status) return;
  if (status.status !== "done") errors.push('asset_status.status must be "done"');
  if (status.reviewer_source !== "asset-reviewer") errors.push('asset_status.reviewer_source must be "asset-reviewer"');
  if (status.reviewer_pass !== review?.pass) errors.push("asset_status.reviewer_pass must match asset_review.pass");
  if (status.reviewer_issues_count !== (review?.issues || []).length) {
    errors.push("asset_status.reviewer_issues_count must match asset_review.issues.length");
  }
  if (status.reviewer_warnings_count !== (review?.warnings || []).length) {
    errors.push("asset_status.reviewer_warnings_count must match asset_review.warnings.length");
  }
  if (!Array.isArray(status.hard_issues_remaining)) errors.push("asset_status.hard_issues_remaining must be an array");
  if (Array.isArray(status.hard_issues_remaining) && status.hard_issues_remaining.length !== 0) {
    errors.push("asset_status.hard_issues_remaining must be empty");
  }
  if (!Array.isArray(status.bible_update_candidates)) errors.push("asset_status.bible_update_candidates must be an array");
}

async function validateWorkbookFreshness() {
  if (!(await exists(requiredFiles.assets)) || !(await exists(requiredFiles.workbook))) return;
  const assetsStat = await fs.stat(requiredFiles.assets);
  const workbookStat = await fs.stat(requiredFiles.workbook);
  if (workbookStat.mtimeMs + 1000 < assetsStat.mtimeMs) {
    errors.push("assets.xlsx is older than assets.md; rerun assets-md-to-xlsx.mjs");
  }
}

for (const [label, filePath] of Object.entries(requiredFiles)) {
  if (!(await exists(filePath))) errors.push(`Missing ${label}: ${filePath}`);
}

let review = null;
let status = null;

if (await exists(requiredFiles.assets)) {
  validateAssetsMarkdown(await fs.readFile(requiredFiles.assets, "utf8"));
}
if (await exists(requiredFiles.review)) review = await readJson(requiredFiles.review, "asset_review.json");
if (await exists(requiredFiles.status)) status = await readJson(requiredFiles.status, "asset_status.json");

validateReview(review);
validateStatus(status, review);
await validateWorkbookFreshness();

if (errors.length > 0) {
  console.error(`Asset validation failed for ${episodeDir}`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Asset validation passed for ${episodeDir}`);
