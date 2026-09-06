"""Generate a conservative, read-only project status snapshot.

The generator consumes repository status files and the compatibility matrix. It
never promotes a status; missing or contradictory facts are rendered as
UNKNOWN/NOT_CONFIRMED and publication is classified from the caller's input.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"status file must contain an object: {path}")
    return data


def publication_state(data: dict[str, Any], source: Path) -> str:
    state = data.get("publication", {}).get("state")
    if state in {"LOCAL_ONLY", "COMMITTED_NOT_PUSHED", "PUBLISHED_REMOTE"}:
        return state
    return "LOCAL_ONLY" if ".git" not in source.parts else "UNKNOWN"


def project_record(source: Path, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "project": data.get("project", source.parent.parent.name),
        "source": str(source),
        "authority": data.get("authority", {}),
        "publication": publication_state(data, source),
        "release": data.get("release", {}),
        "implementation_status": data.get("implementation_status", "UNKNOWN"),
        "verification_status": data.get("verification_status", "UNKNOWN"),
        "maturity_level": data.get("maturity_level", "DESIGNED"),
        "production_readiness": data.get("production_readiness", {"status": "UNKNOWN", "boolean": False}),
        "capability": data.get("capability", {}),
        "evidence": {
            "level": data.get("evidence", {}).get("level"),
            "scope": data.get("evidence", {}).get("scope"),
            "bundle": data.get("evidence", {}).get("bundle"),
            "bundle_sha256": data.get("evidence", {}).get("bundle_sha256"),
        },
        "unknowns": data.get("unknowns", []),
    }


def markdown(snapshot: dict[str, Any]) -> str:
    lines = ["# Full Spectrum 状态快照（只读生成）", "", f"- 生成时间：`{snapshot['generated_at']}`", "- 生成模式：`READ_ONLY`", "- 高风险自动升级：`FORBIDDEN`", "", "## 项目状态", "", "| 项目 | 发布状态 | 实现 | 验证 | 成熟度 | 生产就绪 |", "|---|---|---|---|---|---|"]
    for item in snapshot["projects"]:
        ready = item["production_readiness"].get("status", "UNKNOWN")
        lines.append(f"| {item['project']} | {item['publication']} | {item['implementation_status']} | {item['verification_status']} | {item['maturity_level']} | {ready} |")
    lines += ["", "## 三角兼容性", "", "```json", json.dumps(snapshot["triangle_status"], ensure_ascii=False, indent=2), "```", "", "## 约束", "", "- 本快照不把离线验证升级为真实网络、跨仓库正式兼容或生产就绪。", "- `LOCAL_ONLY`、`COMMITTED_NOT_PUSHED` 不得写成 `PUBLISHED_REMOTE`。", "- `NOT_CONFIRMED`、`UNKNOWN` 只能由人工裁决升级。", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", required=True, type=Path)
    parser.add_argument("--status", action="append", required=True, type=Path)
    parser.add_argument("--json-out", required=True, type=Path)
    parser.add_argument("--md-out", required=True, type=Path)
    args = parser.parse_args()
    matrix = json.loads(args.matrix.read_text(encoding="utf-8"))
    snapshot = {
        "schema_version": "0.1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "mode": "READ_ONLY",
        "projects": [project_record(path, load_yaml(path)) for path in args.status],
        "triangle_status": matrix.get("triangle_status", {}),
        "source_matrix": str(args.matrix),
        "rules": matrix.get("capability_rules", {}),
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.md_out.write_text(markdown(snapshot), encoding="utf-8")
    print(f"GENERATED: {args.json_out}")
    print(f"GENERATED: {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
