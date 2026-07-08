# FSHI Customer-Service Quality Inspection Example

This directory provides a minimal engineering example showing how an FSHI-style customer-service inspection can be mapped into Full Spectrum Protocol objects.

FSHI is used here as an example, not as a required implementation.

The example follows this chain:

```text
desensitized dialogue
  -> FSHI-style multi-turn inspection
  -> RiskAlert
  -> AuditTrace
  -> human-readable report
```

The API contract example follows this chain:

```text
inspection request
  -> inspection response
  -> RiskAlert
  -> AuditTrace
  -> enterprise-owned execution or review
```

## Why this example exists

The Full Spectrum Protocol is not only a philosophical framework. It needs concrete protocol objects that can be inspected, disputed, reviewed, and reused.

Customer-service quality inspection is a good first sample because it naturally includes:

- multi-turn context;
- risk accumulation;
- state changes;
- possible unauthorized promise;
- affected user;
- enterprise responsibility owner;
- human review or handoff;
- non-invasive data input through desensitized dialogue.

## Source alignment

This example is inspired by the public FSHI project materials and product pages:

- FSHI Wiki: `https://gitee.com/full-spectrum/FSHI/wikis/Home`
- Zhaoying FSHI Wiki: `https://gitee.com/shanghai-zhaoying/FSHI/wikis/Home`
- AgentGuard H5: `https://h5.agentguard.com.cn/`
- CCRI questionnaire: `https://www.agentguard.com.cn/products/ccri-questionnaire.html`
- AI Scan questionnaire: `https://www.agentguard.com.cn/products/ai-scan-questionnaire.html`

This repository does not copy proprietary business assets from those projects. It only extracts the protocol-level pattern:

- desensitized input;
- structured risk output;
- reviewable audit trace;
- minimal report.

## Files

- [`desensitized-dialogue.example.json`](./desensitized-dialogue.example.json): mock customer-service dialogue input.
- [`fshi-risk-alert.example.json`](./fshi-risk-alert.example.json): RiskAlert mapped from the inspection result.
- [`fshi-audit-trace.example.json`](./fshi-audit-trace.example.json): AuditTrace linking action, risk, review, and responsibility.
- [`minimal-report.example.md`](./minimal-report.example.md): human-readable report.
- [`api-contract/request.sample.json`](./api-contract/request.sample.json): minimal API-style inspection request.
- [`api-contract/response.sample.json`](./api-contract/response.sample.json): minimal API-style inspection response.
- [`api-contract/risk-alert.sample.json`](./api-contract/risk-alert.sample.json): RiskAlert generated from API-style inspection.
- [`api-contract/audit-trace.sample.json`](./api-contract/audit-trace.sample.json): AuditTrace generated from API-style inspection.
- [`../../schemas/fshi-dialogue-inspection.schema.json`](../../schemas/fshi-dialogue-inspection.schema.json): machine-readable request schema.
- [`../../schemas/fshi-dialogue-inspection-response.schema.json`](../../schemas/fshi-dialogue-inspection-response.schema.json): machine-readable response schema.
- [FSHI API Contract Mapping](../../docs/mapping/fshi-api-contract-mapping.md): protocol-level mapping between product-facing API fields and Full Spectrum objects.

## Validate the contract chain

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-fshi-contract.ps1
```

The script checks:

- request sample against the minimal request contract;
- response sample against the minimal response contract;
- RiskAlert sample against RiskAlert requirements;
- AuditTrace sample against AuditTrace requirements;
- cross-object consistency across request, response, RiskAlert, and AuditTrace.

## Boundary

This example does not claim:

- production accuracy;
- real enterprise validation;
- legal, medical, financial, or employment decision authority;
- Full Spectrum certification of any external system.

It is a protocol demonstration only.

