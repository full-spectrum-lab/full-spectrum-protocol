"""Read-only consistency checks for project status files.

This pilot never upgrades a status. It reports publication, authority,
capability, evidence, and high-risk promotion problems for CI review.
"""
from pathlib import Path
import json
import sys

import yaml


HIGH_RISK = {
    ("production_readiness", "READY"),
    ("verification_status", "PRODUCTION_ACCEPTED"),
    ("capability.network_capability.verified", "PROTOCOL_INTEROP"),
}


def get_path(data, path):
    current = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def check(path: Path) -> list[str]:
    issues = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    publication = data.get("publication", {})
    authority = data.get("authority", {})
    evidence = data.get("evidence", {})

    if publication.get("state") == "PUBLISHED_REMOTE" and not authority.get("canonical_commit"):
        issues.append("published status requires authority.canonical_commit")
    if publication.get("state") == "PUBLISHED_REMOTE" and publication.get("last_checked_at") is None:
        issues.append("published status requires publication.last_checked_at")
    if evidence.get("bundle") and not evidence.get("bundle_sha256"):
        issues.append("evidence.bundle requires evidence.bundle_sha256")
    if data.get("production_readiness", {}).get("status") == "READY":
        if evidence.get("level") != "PRODUCTION_ACCEPTED":
            issues.append("READY requires PRODUCTION_ACCEPTED evidence")
    if get_path(data, "capability.network_capability.verified") == "PROTOCOL_INTEROP":
        if data.get("verification_status") not in {"PILOT_VALIDATED", "PRODUCTION_ACCEPTED"}:
            issues.append("PROTOCOL_INTEROP requires pilot or production verification")
    for path_name, value in HIGH_RISK:
        if get_path(data, path_name) == value and not data.get("confirmed"):
            issues.append(f"high-risk value {path_name}={value} requires confirmed evidence")
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python check_status_drift.py <status.yaml> [...]")
        return 2
    failed = False
    for raw in sys.argv[1:]:
        path = Path(raw)
        issues = check(path)
        if issues:
            failed = True
            print(f"DRIFT: {path}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"OK: {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
