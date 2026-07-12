#!/usr/bin/env python3
"""
Full Spectrum Protocol - Example Schema Conformance Checker.

Walks every JSON example under examples/ and validates it against the
matching JSON Schema under schemas/. Files that cannot be mapped to a
schema are skipped (not failed), so adding new business samples never
breaks CI until a schema exists for them.

Mapping is by filename keyword -> schema filename. This mirrors the
published object vocabulary (Governance Event, Canonical Context,
Enterprise Writeback, ...).

Primary validator: jsonschema (draft 2020-12). If jsonschema is not
installed, a built-in lightweight checker is used as a fallback so the
script never crashes in a minimal environment.
"""
import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMAS_DIR = os.path.join(ROOT, "schemas")
EXAMPLES_DIR = os.path.join(ROOT, "examples")

# filename keyword -> schema filename
MAPPING = {
    "identity-claim": "identity-claim.schema.json",
    "capability-declaration": "capability-declaration.schema.json",
    "governance-event": "governance-event.schema.json",
    "audit-trace": "audit-trace.schema.json",
    "risk-alert": "risk-alert.schema.json",
    "cell-manifest": "l1-cell-protocol.schema.json",
    "output-envelope": "governance-output-envelope.schema.json",
    "governance-output-envelope": "governance-output-envelope.schema.json",
    "enterprise-writeback": "enterprise-writeback.schema.json",
    "canonical-context": "canonical-context.schema.json",
    "cross-enterprise-audit-record": "cross-enterprise-audit-record.schema.json",
    "external-ethics-profile": "external-ethics-profile.schema.json",
    "io-contract": "io-contract.schema.json",
    "subject-declaration": "subject-declaration.schema.json",
}


def map_schema(fname):
    for key, schema_file in MAPPING.items():
        if key in fname:
            return schema_file
    return None


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def lightweight_errors(inst, schema, path=""):
    """Minimal conformance check used only when jsonschema is unavailable."""
    import re
    errs = []
    props = schema.get("properties", {})
    for k in schema.get("required", []):
        if k not in inst:
            errs.append(f"{path}missing required '{k}'")
    for k, v in inst.items():
        if k in props:
            sub = props[k]
            t = sub.get("type")
            if t == "object" and not isinstance(v, dict):
                errs.append(f"{path}{k} not object")
            if t == "array" and not isinstance(v, list):
                errs.append(f"{path}{k} not array")
            if t == "string" and not isinstance(v, str):
                errs.append(f"{path}{k} not string")
            if t == "boolean" and not isinstance(v, bool):
                errs.append(f"{path}{k} not boolean")
            if t in ("number", "integer") and not isinstance(v, (int, float)):
                errs.append(f"{path}{k} not number")
            if "enum" in sub and v not in sub["enum"]:
                errs.append(f"{path}{k}={v!r} not in enum")
            if "const" in sub and v != sub["const"]:
                errs.append(f"{path}{k}={v!r} != const {sub['const']}")
            if isinstance(v, dict) and sub.get("type") == "object":
                errs += lightweight_errors(v, sub, path + k + ".")
            if isinstance(v, list) and sub.get("type") == "array":
                for i, it in enumerate(v):
                    if isinstance(it, dict) and sub.get("items", {}).get("type") == "object":
                        errs += lightweight_errors(it, sub["items"], path + k + f"[{i}].")
    addl = schema.get("additionalProperties", True)
    if addl is False:
        for k in inst.keys():
            if k not in props and not any(re.match(p, k) for p in schema.get("patternProperties", {})):
                errs.append(f"{path}extra prop '{k}' not allowed")
    if "minProperties" in schema and isinstance(inst, dict) and len(inst) < schema["minProperties"]:
        errs.append(f"{path}minProperties not met")
    return errs


def main():
    schemas = {}
    for name in os.listdir(SCHEMAS_DIR):
        if name.endswith(".json"):
            try:
                schemas[name] = load_json(os.path.join(SCHEMAS_DIR, name))
            except Exception as e:
                print(f"[WARN ] cannot parse schema {name}: {e}")

    try:
        import jsonschema
        from jsonschema import Draft202012Validator
        use_strict = True
    except ImportError:
        print("[INFO ] jsonschema not installed; using built-in lightweight checker.")
        use_strict = False

    failures = []
    checked = 0
    skipped = 0

    for dirpath, _, filenames in os.walk(EXAMPLES_DIR):
        for fn in sorted(filenames):
            if not fn.endswith(".json"):
                continue
            full = os.path.join(dirpath, fn)
            schema_file = map_schema(fn)
            if not schema_file or schema_file not in schemas:
                skipped += 1
                print(f"[SKIP ] {os.path.relpath(full, ROOT)} (no schema)")
                continue
            inst = load_json(full)
            schema = schemas[schema_file]
            checked += 1
            if use_strict:
                validator = Draft202012Validator(schema)
                errs = sorted(validator.iter_errors(inst), key=lambda e: list(e.path))
                if errs:
                    failures.append((full, schema_file, errs))
                    print(f"[FAIL ] {os.path.relpath(full, ROOT)} -> {schema_file}: "
                          f"{errs[0].message} (path {'/'.join(map(str, errs[0].path)) or '<root>'})")
                else:
                    print(f"[PASS ] {os.path.relpath(full, ROOT)} -> {schema_file}")
            else:
                errs = lightweight_errors(inst, schema)
                if errs:
                    failures.append((full, schema_file, errs))
                    print(f"[FAIL ] {os.path.relpath(full, ROOT)} -> {schema_file}: {errs[0]}")
                else:
                    print(f"[PASS ] {os.path.relpath(full, ROOT)} -> {schema_file}")

    print(f"\nSummary: {checked} checked, {skipped} skipped, {len(failures)} failed.")
    if failures:
        sys.exit(1)
    print("ALL EXAMPLES CONFORM.")


if __name__ == "__main__":
    main()
