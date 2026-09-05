"""Validate a Full Spectrum status YAML file against the v0.1 schema."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: install PyYAML")

try:
    import jsonschema
except ImportError:
    raise SystemExit("Missing dependency: install jsonschema")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python validate_full_spectrum_status.py <status.yaml>")
        return 2
    status_path = Path(sys.argv[1])
    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "full-spectrum-status.schema.json"
    status = yaml.safe_load(status_path.read_text(encoding="utf-8"))
    schema = __import__("json").loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(status)
    if status["production_readiness"]["boolean"] and status["production_readiness"]["status"] != "READY":
        raise SystemExit("production_readiness boolean/status mismatch")
    if status["production_readiness"]["status"] == "READY" and status["evidence"]["level"] != "PRODUCTION_ACCEPTED":
        raise SystemExit("READY requires PRODUCTION_ACCEPTED evidence")
    print(f"VALID: {status_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
