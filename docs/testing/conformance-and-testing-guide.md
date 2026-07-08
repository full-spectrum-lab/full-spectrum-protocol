# Conformance and Testing Guide v0.1

This guide explains how to test the current Full Spectrum protocol draft artifacts.

Current status: early draft. The repository can validate selected schemas and samples, but it does not yet provide full conformance certification.

---

## 1. What "conformance" means at this stage

At this stage, conformance means:

- JSON samples match their declared JSON Schemas;
- common mojibake patterns are not detected in repository text files;
- the minimal FSHI request -> response -> RiskAlert -> AuditTrace chain can be validated;
- the minimal GovernanceEvent sample can be validated.

It does not mean:

- legal approval;
- regulatory recognition;
- production safety;
- Full Spectrum certification;
- proof that a system is ethically correct.

---

## 2. Local validation commands

Run from the repository root.

### 2.1 Text hygiene

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-mojibake.ps1
```

Expected result:

```text
No common mojibake patterns detected.
```

### 2.2 FSHI contract chain

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-fshi-contract.ps1
```

This validates:

```text
examples/fshi/api-contract/request.sample.json
  -> examples/fshi/api-contract/response.sample.json
  -> examples/fshi/api-contract/risk-alert.sample.json
  -> examples/fshi/api-contract/audit-trace.sample.json
  -> examples/governance/cross-enterprise-audit-record.example.json
```

Expected result:

```text
FSHI contract validation OK
```

### 2.3 GovernanceEvent

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-governance-event.ps1
```

Expected result:

```text
GovernanceEvent validation OK
```

---

## 3. GitHub Actions

The workflow is defined in:

```text
.github/workflows/validate.yml
```

It runs on:

- push to `main`;
- pull request into `main`;
- manual `workflow_dispatch`.

Current checks:

1. common mojibake pattern check;
2. FSHI contract chain validation;
3. GovernanceEvent sample validation.

---

## 4. How to add a new protocol object

For a new protocol object, add four items:

1. a human-readable specification under `specs/`;
2. a machine-readable JSON Schema under `schemas/`;
3. at least one synthetic sample under `examples/`;
4. a validation script under `scripts/`, then add it to `.github/workflows/validate.yml`.

Recommended naming:

```text
specs/{object-name}.md
schemas/{object-name}.schema.json
examples/{domain}/{object-name}.sample.json
scripts/validate-{object-name}.ps1
```

---

## 5. What must be true before claiming v1.0-beta readiness

Before public v1.0-beta, the repository should at least have:

- README and boundary documents reviewed;
- all linked core schemas validated;
- at least three synthetic CASE examples;
- documentation links checked;
- a clear relationship to the minimal local-first engine;
- a public statement that examples are synthetic and do not represent real enterprise production data.

See:

- [`docs/roadmap/v1.0-beta-release-criteria.md`](../roadmap/v1.0-beta-release-criteria.md)

---

## 6. Boundary reminder

Validation checks whether artifacts match declared formats.

Validation does not decide whether:

- an AI action is morally right;
- a business decision is lawful;
- an organization has fulfilled its duty;
- a node is Full Spectrum certified.

Those require additional review, context, legal compliance, and responsible human or organizational judgment.

