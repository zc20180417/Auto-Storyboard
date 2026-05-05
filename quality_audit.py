#!/usr/bin/env python3
"""Quick quality audit across all 20 episodes."""

from pathlib import Path
import re
import json

RUN_DIR = Path("agent_runs/zhangben-zhangba/episodes")

# Patterns to flag
NONSTD_VERBS = re.compile(r"大喊道|嘚瑟道|愣道|骂咧道|哭喊道|打断道")
ABSTRACT_EXPR = re.compile(r"面无表情|眼中闪过一丝冷光|眉头紧锁|视线死死盯着")
LIGHT_TEMPLATE = re.compile(r"前侧光从左侧45度照来|顶光配合正面柔光补光")
SCENE_SPLIT = re.compile(r"[、,]\s*(?:废弃土屋|砖厂|县局|照相馆|办公室|院子)")

results = []

for ep_dir in sorted(RUN_DIR.glob("ep*")):
    final_path = ep_dir / "final.txt"
    if not final_path.exists():
        results.append({"ep": ep_dir.name, "status": "missing_final"})
        continue

    text = final_path.read_text(encoding="utf-8")
    nonstd = NONSTD_VERBS.findall(text)
    abstract = ABSTRACT_EXPR.findall(text)
    light = LIGHT_TEMPLATE.findall(text)

    # Count groups
    groups = list(re.finditer(r"=== 第\d+组[：:]", text))

    results.append({
        "ep": ep_dir.name,
        "status": "ok",
        "groups": len(groups),
        "nonstd_verbs": len(nonstd),
        "abstract_expr": len(abstract),
        "light_template": len(light),
        "chars": len(text),
    })

# Print markdown table
print("| 集号 | 组数 | 非标准动词 | 抽象表情 | 光影模板 | 字符数 |")
print("|------|------|-----------|---------|---------|--------|")
for r in results:
    if r["status"] == "missing_final":
        print(f"| {r['ep']} | ❌ 缺失 | - | - | - | - |")
    else:
        flags = []
        if r["nonstd_verbs"]: flags.append(f"动词×{r['nonstd_verbs']}")
        if r["abstract_expr"]: flags.append(f"表情×{r['abstract_expr']}")
        if r["light_template"]: flags.append(f"光影×{r['light_template']}")
        flag_str = "、".join(flags) if flags else "-"
        print(f"| {r['ep']} | {r['groups']} | {r['nonstd_verbs']} | {r['abstract_expr']} | {r['light_template']} | {r['chars']} | {flag_str}")

# Summary
print("\n---\n")
print("## 建议重点抽检的集")
for r in results:
    if r["status"] != "ok":
        continue
    issues = []
    if r["nonstd_verbs"] >= 2: issues.append("非标准动词较多")
    if r["abstract_expr"] >= 2: issues.append("抽象表情较多")
    if r["light_template"] >= 5: issues.append("光影模板化严重")
    if issues:
        print(f"- **{r['ep']}**: " + "；".join(issues))
