# Scoped cross-repository compatibility result (2026-09-05)

**Test ID:** `FS-COMPAT-SCOPED-001`  
**Workflow:** `Scoped cross-repository compatibility`  
**Run:** <https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/runs/33971355683>  
**Result:** `PASS_WITH_SCOPE_LIMITS`

## Pinned inputs

```ini
PROTOCOL = d63c4f1238cc0a7b0830ae047a7516a3ef7ebdf4
ENGINE = v1.5.0 / ab9939b2aaf2a921b6ae6e7a6af5d34cd07af424
OBSERVER = compat/engine-v1.5-observer-v0.4 / 1946f8a0b1ffc67adf4f0095994adab030cdde2e
EVIDENCE_BUNDLE_SHA256 = 00D26D2B488AACC29C114B7DD29400A8E160F416D31CB68068324D526755A5A4
SCOPE = OFFLINE
```

## Checks passed

- Protocol status YAML validates against the published schema.
- Observer evidence bundle hash matches the pinned public artifact.
- Engine v1.5 compatibility API tests: `5/5 PASS`.
- Observer v1.5 adapter and fixture tests: `13/13 PASS`.
- The boundary assertion confirms that Observer's release worker lock remains Engine `v1.0.0`.

## Interpretation

This is a reproducible, pinned, offline scoped composite CI result. It confirms the selected Protocol schema, Engine v1.5 compatibility tests, Observer v1.5 adapter fixtures, and evidence integrity can be checked together.

It does **not** confirm formal Protocol–Engine–Observer release compatibility. The Observer release worker lock remains Engine `v1.0.0`; complete IG4–IG6 on a v1.5 lock, real network requests, credentials, and production deployment were not executed.

```ini
SCOPED_COMPOSITE_CI = PASS
FORMAL_E2E_COMPATIBILITY = NOT_CONFIRMED
PRODUCTION_READY = NO
```
