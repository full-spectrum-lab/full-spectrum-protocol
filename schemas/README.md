# Schemas

This directory is reserved for machine-readable protocol schemas.

Planned schemas:

- [`governance-event.schema.json`](./governance-event.schema.json)
- [`identity-claim.schema.json`](./identity-claim.schema.json)
- [`capability-declaration.schema.json`](./capability-declaration.schema.json)
- `permission-request.schema.json`
- `consent-record.schema.json`
- [`risk-alert.schema.json`](./risk-alert.schema.json)
- [`external-ethics-profile.schema.json`](./external-ethics-profile.schema.json)
- `ess-request.schema.json`
- `ess-result.schema.json`
- `guardian-review.schema.json`
- [`audit-trace.schema.json`](./audit-trace.schema.json)
- [`fshi-dialogue-inspection.schema.json`](./fshi-dialogue-inspection.schema.json)
- [`fshi-dialogue-inspection-response.schema.json`](./fshi-dialogue-inspection-response.schema.json)
- [`cross-enterprise-audit-record.schema.json`](./cross-enterprise-audit-record.schema.json)

The purpose of schemas is to make the Full Spectrum Protocol inspectable and implementable by software systems.

Minimal governance chain:

```text
IdentityClaim
  -> CapabilityDeclaration
  -> GovernanceEvent
  -> RiskAlert
  -> AuditTrace
  -> CrossEnterpriseAuditRecord
```

`IdentityClaim` and `CapabilityDeclaration` form the minimal node contract. `GovernanceEvent` records the AI-related action before risk interpretation and audit tracing.

## Validation helper

The FSHI sample chain can be checked with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-node-contract.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-fshi-contract.ps1
```

The helper currently checks:

- IdentityClaim sample;
- CapabilityDeclaration sample;
- FSHI request sample;
- FSHI response sample;
- RiskAlert sample;
- AuditTrace sample;
- CrossEnterpriseAuditRecord governance sample.

