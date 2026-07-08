# Protocol Mapping Center

This directory collects mapping documents that explain how Full Spectrum protocol objects relate to existing standards, engineering samples, and cross-organization audit workflows.

These documents are not new standards. They are orientation layers for implementers, reviewers, and AI agents that need to understand how protocol objects connect.

---

## Current mappings

| Document | Purpose | Best starting reader |
| --- | --- | --- |
| [Standards and ecosystem mapping](./standards-mapping.md) | Maps Full Spectrum to AIP-style national agent interconnection standards, A2A, MCP, data-governance trends, and AI risk frameworks | Standards researchers, governance readers, ecosystem reviewers |
| [FSHI API Contract Mapping](./fshi-api-contract-mapping.md) | Maps an FSHI-style customer-service inspection request/response to `RiskAlert` and `AuditTrace` | Developers, product reviewers, FSHI implementers |
| [Cross-Enterprise Audit Record Mapping](./cross-enterprise-audit-record-mapping.md) | Maps `RiskAlert` and `AuditTrace` into a multi-party audit envelope for cross-enterprise workflows | Enterprise compliance teams, multi-agent workflow designers, cross-organization audit reviewers |

---

## How the mappings fit together

```text
Standards mapping
  -> explains the external ecosystem and interconnection layer

FSHI API Contract Mapping
  -> shows how one product-facing inspection workflow becomes protocol objects

Cross-Enterprise Audit Record Mapping
  -> shows how those protocol objects become a shared audit envelope across organizations
```

In short:

```text
AIP / A2A / MCP / enterprise systems
  -> connection, identity, tool invocation, and data flow

FSHI request / response
  -> inspection and recommendation

RiskAlert / AuditTrace
  -> risk and responsibility chain

CrossEnterpriseAuditRecord
  -> multi-party audit context, access, retention, and responsibility claims
```

---

## Boundary

The mapping documents do not:

- replace law, regulation, contracts, or enterprise compliance systems;
- certify that a system is safe;
- claim that any external company has adopted Full Spectrum;
- require all AI systems to become Full Spectrum certified.

They exist to make protocol relationships explicit, inspectable, and easier to implement.

