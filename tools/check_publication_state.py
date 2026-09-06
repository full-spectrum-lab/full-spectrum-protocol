"""Read-only publication and authority checks for a status file.

This tool verifies that the declared canonical commit is present in the local
repository and, when requested, reachable from a supplied remote ref. It never
changes status.yaml and never promotes a publication state.
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

import yaml


def git(repo: Path, *args: str) -> tuple[int, str]:
    p = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    return p.returncode, (p.stdout or p.stderr).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--status", required=True, type=Path)
    ap.add_argument("--remote-ref", default="origin/main")
    args = ap.parse_args()
    data = yaml.safe_load(args.status.read_text(encoding="utf-8")) or {}
    authority = data.get("authority", {})
    commit = authority.get("canonical_commit") or data.get("target_commit")
    if not commit:
        print("UNKNOWN: no canonical or target commit")
        return 1
    rc, resolved = git(args.repo, "rev-parse", "--verify", f"{commit}^{{commit}}")
    if rc:
        print(f"INVALID: commit not present locally: {commit}")
        return 1
    print(f"COMMIT_PRESENT: {resolved}")
    rc, remote_tip = git(args.repo, "rev-parse", "--verify", f"{args.remote_ref}^{{commit}}")
    if rc:
        print(f"REMOTE_UNKNOWN: {args.remote_ref}")
        return 2
    rc, _ = git(args.repo, "merge-base", "--is-ancestor", resolved, remote_tip)
    if rc == 0:
        print(f"REMOTE_REACHABLE: {args.remote_ref}")
        return 0
    print(f"REMOTE_NOT_REACHABLE: {args.remote_ref}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
