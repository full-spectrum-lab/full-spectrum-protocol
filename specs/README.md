# Specifications

This directory contains protocol-facing specifications for objects that can be implemented, validated, or mapped by software systems.

The goal of `specs/` is to keep the engineering-facing layer separate from essays, archived theory documents, and product-specific materials.

## Current specifications

| Specification | Purpose | Related schema | Related example |
|---|---|---|---|
| [IdentityClaim](./identity-claim.md) | Minimal declaration of who or what is acting | [`schemas/identity-claim.schema.json`](../schemas/identity-claim.schema.json) | [`examples/governance/identity-claim.sample.json`](../examples/governance/identity-claim.sample.json) |
| [CapabilityDeclaration](./capability-declaration.md) | Minimal declaration of what a subject can and cannot do | [`schemas/capability-declaration.schema.json`](../schemas/capability-declaration.schema.json) | [`examples/governance/capability-declaration.sample.json`](../examples/governance/capability-declaration.sample.json) |
| [Governance Event](./governance-event.md) | Minimal record for an AI-related action before risk interpretation | [`schemas/governance-event.schema.json`](../schemas/governance-event.schema.json) | [`examples/governance/governance-event.sample.json`](../examples/governance/governance-event.sample.json) |
| [RiskAlert](./risk-alert.md) | Minimal object for detected or suspected reviewable risk | [`schemas/risk-alert.schema.json`](../schemas/risk-alert.schema.json) | [`examples/fshi/api-contract/risk-alert.sample.json`](../examples/fshi/api-contract/risk-alert.sample.json) |
| [AuditTrace](./audit-trace.md) | Minimal trace for review, escalation, decision, execution, or recovery | [`schemas/audit-trace.schema.json`](../schemas/audit-trace.schema.json) | [`examples/fshi/api-contract/audit-trace.sample.json`](../examples/fshi/api-contract/audit-trace.sample.json) |
| [IOContract](./io-contract.md) | Minimal mapping contract from business raw input/output to governance objects via a Business Adapter | planned | planned |
| [L1CellProtocol](./l1-cell-protocol.md) | Subject access, identity tiering and certification domain before entering governance workflows | planned | planned |
| [GovernanceOutputEnvelope](./governance-output-envelope.md) | Standard engine output object bundling result, risk vector, safety action, writeback, privacy, conformance | planned | planned |
| [EnterpriseWriteback](./enterprise-writeback.md) | Enterprise-consumable decision object gating auto-reply, commitment and execution | planned | planned |

## Object chain

The current minimal governance chain is:

```text
IdentityClaim
  -> CapabilityDeclaration
  -> GovernanceEvent
  -> RiskAlert
  -> AuditTrace
  -> CrossEnterpriseAuditRecord
```

Adjacent integration and access specs: **I/O Contract** (adapter mapping) and **L1 Cell Protocol** (subject access) feed into this chain.

`IdentityClaim` declares who or what is acting. `CapabilityDeclaration` declares what that subject can and cannot do. `GovernanceEvent` is the local action record. `RiskAlert` interprets risk. `AuditTrace` records the processing and review path. `CrossEnterpriseAuditRecord` is a higher-level envelope for multi-party review.

## Boundary

Specifications in this directory do not:

- replace law, regulation, or enterprise compliance;
- certify external systems;
- prove safety;
- require joining a Full Spectrum network;
- claim production maturity.

They define draft protocol objects so that developers, reviewers, AI agents, and governance teams can discuss the same record format.

## Validation

Current validation helpers:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-node-contract.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-governance-event.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-fshi-contract.ps1
```

The validation scripts are intentionally small. Their purpose is to make the protocol inspectable and reproducible before any claim of production readiness.

